"""Reconstruct mixed-quadrupole horizon asymptotics using exact algebra.

The frame calculation independently contracts the stationary Riemann tensor.
No full mixed Kerr metric or EFT response coefficient is computed here.
"""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s


def reduced_kretschmann():
    """Return K / exp(4U-4gamma) for a reflection-symmetric vacuum point.

    Frame: e0=exp(U)(dt-omega*dphi), e1=exp(gamma-U)*dr,
    e2=exp(gamma-U)*dz, e3=r*exp(-U)*dphi; signature -+++.
    Define v=U_r and t=exp(2U)*omega_r/r. Derivatives are coordinate
    derivatives, not frame derivatives. Work with the common frame factor
    L=exp(U-gamma) removed until the final contraction.
    """
    r = s.Symbol("r", positive=True)
    v, w, g, h, t, b = s.symbols("v w g h t b", real=True)
    vr, vz, wz, gr, gz, hz, tr, tz, br, bz = s.symbols(
        "vr vz wz gr gz hz tr tz br bz", real=True
    )
    variables = (r, v, w, g, h, t, b)
    dr = (1, vr, vz, gr, gz, tr, br)
    dz = (0, vz, wz, gz, hz, tz, bz)

    def derivative(expr, direction):
        rates = dr if direction == 1 else dz
        return sum(s.diff(expr, x) * rate for x, rate in zip(variables, rates))

    C = s.MutableDenseNDimArray.zeros(4, 4, 4)

    def set_c(a, j, k, value):
        C[a, j, k] = value
        C[a, k, j] = -value

    # d e^a = -1/2 L C^a_bc e^b wedge e^c.
    set_c(0, 0, 1, v)
    set_c(0, 0, 2, w)
    set_c(0, 1, 3, t)
    set_c(0, 2, 3, b)
    set_c(1, 1, 2, h - w)
    set_c(2, 1, 2, -(g - v))
    set_c(3, 1, 3, -(1 / r - v))
    set_c(3, 2, 3, w)
    eta = (-1, 1, 1, 1)
    connection = s.MutableDenseNDimArray.zeros(4, 4, 4)
    for a in range(4):
        for j in range(4):
            for k in range(4):
                connection[a, j, k] = (
                    eta[a] * C[a, k, j]
                    - eta[k] * C[k, j, a]
                    + eta[j] * C[j, a, k]
                ) / (2 * eta[a])

    def frame_derivative(expr, direction):
        if direction not in (1, 2):
            return s.S.Zero
        log_factor_derivative = v - g if direction == 1 else w - h
        return derivative(expr, direction) + log_factor_derivative * expr

    # Reflection plus the local stationary vacuum equations. They do not
    # assert that an arbitrary proposed metric solves the global equations.
    vacuum = {
        w: 0, h: 0, b: 0, vz: 0, gz: 0, tz: 0, br: 0,
        g: r * v**2 - r * t**2 / 4,
        wz: -vr - v / r - t**2 / 2,
        bz: -tr - 2 * v * t,
        gr: v**2 + 2 * r * v * vr - t**2 / 4 - r * t * tr / 2,
        hz: -2 * r * v * vr - 2 * v**2 + r * t * tr / 2,
    }
    R = s.MutableDenseNDimArray.zeros(4, 4, 4, 4)
    K = s.S.Zero
    for a in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    value = frame_derivative(connection[a, j, l], k) - frame_derivative(
                        connection[a, j, k], l
                    )
                    value += sum(
                        connection[m, j, l] * connection[a, m, k]
                        - connection[m, j, k] * connection[a, m, l]
                        - C[m, k, l] * connection[a, j, m]
                        for m in range(4)
                    )
                    value = s.factor(value.subs(vacuum, simultaneous=True))
                    R[a, j, k, l] = value
                    K += eta[a] * eta[j] * eta[k] * eta[l] * value**2
    for j in range(4):
        for l in range(4):
            ricci = s.simplify(sum(R[a, j, a, l] for a in range(4)))
            if ricci != 0:
                raise AssertionError(f"Frame vacuum check failed: Ricci[{j},{l}]={ricci}")
    return (r, v, vr, t, tr), s.factor(K)


def run():
    symbols, Kbar = reduced_kretschmann()
    r, v, vr, t, tr = symbols
    c, d = s.symbols("c d", real=True)
    x = s.sqrt(1 + r**2)
    checks = []

    def check(name, actual, expected=0):
        residual = s.simplify(actual - expected)
        if residual != 0:
            raise AssertionError(f"{name}: {residual}")
        checks.append({"name": name, "expected": str(expected), "status": "verified"})

    A = vr + 2 * v**2 - r * v**3
    B = -vr - v / r + r * v**3 - v**2
    C = v / r - v**2
    static = 8 * (A**2 + B**2 + C**2)
    check("Independent frame contraction gives static electric-Weyl formula", Kbar.subs({t: 0, tr: 0}), static)
    check("Reduced curvature vanishes in flat space", Kbar.subs({v: 0, vr: 0, t: 0, tr: 0}))

    US = s.log((x - 1) / (x + 1)) / 2
    gammaS = s.log(r**2 / (1 + r**2)) / 2
    psi = -c * r**2 / 2 - d / (2 * r**3)
    U = US + psi
    W = x * (2 * r**2 - 1) / r**3
    V = -2 * c * x + d * W + c**2 * r**4 / 4 + 3 * c * d / r - 3 * d**2 / (8 * r**6)
    vp = 1 / (r * x) - c * r + 3 * d / (2 * r**4)
    check("Exact mixed static equatorial gamma equation", s.diff(gammaS + V, r), r * vp**2)
    schwarz = static.subs({v: 1 / (r * x), vr: s.diff(1 / (r * x), r)})
    check("Full Schwarzschild Kretschmann scalar", s.simplify(schwarz * s.exp(4 * US - 4 * gammaS)), 48 / (x + 1)**6)

    # A genuinely stationary control, evaluated at rational x and r to avoid
    # unnecessary algebraic-number simplification. These are exact checks,
    # not a numerical sample establishing the general curvature identity.
    alpha = s.Rational(1, 3)
    Sk = x + 1 - (x - 1) * alpha**2
    Tk = x - 1 - (x + 1) * alpha**2
    fk = Tk / Sk
    omegak = 4 * alpha * x / Tk
    vk = s.diff(fk, r) / (2 * fk)
    tk = fk * s.diff(omegak, r) / r
    frame_factor = x**4 * (1 - alpha**2)**4 / Sk**4
    mass = (1 + alpha**2) / (1 - alpha**2)
    for point in (s.Rational(4, 3), s.Rational(12, 5)):
        values = {
            r: point,
            v: s.simplify(vk.subs(r, point)),
            vr: s.simplify(s.diff(vk, r).subs(r, point)),
            t: s.simplify(tk.subs(r, point)),
            tr: s.simplify(s.diff(tk, r).subs(r, point)),
        }
        check(
            f"Rotating Kerr equatorial curvature at rho={point}, alpha=1/3",
            Kbar.subs(values) * frame_factor.subs(r, point),
            (48 * mass**2 / (x + mass)**6).subs(r, point),
        )

    Q = s.factor(static.subs({v: vp, vr: s.diff(vp, r)}))
    check("Static reduced curvature leading coefficient", s.limit(r**22 * Q, r, 0, dir="+"), 729 * d**6 / 4)
    check("Mixed static metric exponential leading coefficient", s.limit(r**6 * (4 * U - 4 * gammaS - 4 * V), r, 0, dir="+"), 3 * d**2 / 2)
    check("Finite c cannot change the leading exponential coefficient", s.limit(r**6 * s.diff(4 * U - 4 * gammaS - 4 * V, c), r, 0, dir="+"))
    # log Q is algebraic/logarithmic, so r^6 log Q -> 0 for fixed d != 0.
    # The derivative check isolates a divergent mixed-amplitude contribution.
    dlogKdc = 4 * s.diff(U - gammaS - V, c) + s.diff(Q, c) / Q
    check("Mixed curvature coefficient is not generally finite", s.limit(r * dlogKdc.subs(c, 0), r, 0, dir="+"), -12 * d)
    check("Published V sign issue in the pure growing equatorial limit", s.diff(c**2 * (x**4 - 2 * x**2) / 4 + 2 * c * x - V.subs(d, 0), r), 4 * c * r / x)

    # Both static branches used by the rotating asymptotic reduction.
    vm = -1 / (r * x) - c * r + 3 * d / (2 * r**4)
    check("Inverse Schwarzschild seed has same leading reduced curvature", s.limit(r**22 * static.subs({v: vm, vr: s.diff(vm, r)}), r, 0, dir="+"), 729 * d**6 / 4)
    check("Kerr auxiliary amplitude equation", s.diff(2 * c * x - d * W, r), -2 * s.diff(psi, r) / x)

    xx, k = s.symbols("xx k", positive=True)
    S = xx + 1 - (xx - 1) * k**2
    T = xx - 1 - (xx + 1) * k**2
    check("Equatorial Kerr seed factorization", (xx**2 - 1) * (1 - k**2)**2 - 4 * k**2, S * T)
    check("Small-k Ernst metric ratio", s.limit(T / S, k, 0), (xx - 1) / (xx + 1))
    check("Large-k Ernst metric ratio", s.limit(T / S, k, s.oo), (xx + 1) / (xx - 1))
    # This only establishes algebraic branches. Uniform derivative estimates
    # and the vacuum/normalization assumptions are stated in the proof note.
    stationary_correction = s.factor(Kbar - static)
    compact_correction = (
        -4 * tr**2 + (8 * r * v**2 - 24 * v - 2 * r * t**2) * t * tr
        + (-12 * r**2 * v**4 + 24 * r * v**3 + 8 * r * v * vr
           - 20 * v**2 + 12 * vr + 12 * v / r) * t**2
        + 3 * (r**2 * v**2 - r * v + 1) * t**4 - r**2 * t**6 / 4
    )
    check("Compact physical-twist curvature correction", stationary_correction, compact_correction)
    check("Twist corrections vanish when physical twist and its derivative vanish", stationary_correction.subs({t: 0, tr: 0}))

    return {
        "evidence_level": "exact stationary frame identities and static mixed-field limits; conditional rotating asymptotic argument is in the accompanying note",
        "sympy_version": s.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks_passed": len(checks),
        "vacuum_ricci_components_checked": 16,
        "checks": checks,
        "reduced_stationary_kretschmann": str(Kbar),
        "reduced_twist_correction": str(stationary_correction),
        "static_scaled_log_limit": "lim(r->0+) r^6 log(K_dimless) = 3*d^2/2, fixed d != 0 and finite c",
        "not_established": [
            "No full mixed Kerr Kretschmann expression or published prefactor is reproduced.",
            "No global nakedness, event-horizon classification, or completeness of the solution-generating ansatz is proved.",
            "No uniform d->0, spin->0, or extremal limit is proved.",
            "No EFT-matched Love coefficient or novel all-multipole theorem is obtained.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write:
        target = Path(__file__).parent / "results" / "mixed-horizon.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Verified {result['checks_passed']} checks and 16 vacuum Ricci components.")
    print(result["evidence_level"])
