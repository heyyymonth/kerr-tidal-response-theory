"""Exact algebra checks for the local Kerr tidal-response proof reconstruction.

These checks establish identities and counterexamples to two printed formulas.
They do not solve a distorted Kerr boundary-value problem or determine a Love
coefficient. Run with --write to save results/baseline.json; otherwise read-only.
"""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def run():
    x, y, p, q = sp.symbols("x y p q", real=True)
    rho, z = sp.symbols("rho z", real=True, positive=True)
    checks = []

    def D(h):
        return sp.diff((x**2 - 1) * sp.diff(h, x), x) + sp.diff(
            (1 - y**2) * sp.diff(h, y), y
        )

    def G(a, b):
        # Bilinear product; there is no complex conjugation in the Ernst PDE.
        return (x**2 - 1) * sp.diff(a, x) * sp.diff(b, x) + (
            1 - y**2
        ) * sp.diff(a, y) * sp.diff(b, y)

    def check(name, actual, expected=0):
        residual = sp.simplify(sp.expand(actual - expected))
        if residual != 0:
            raise AssertionError(f"{name}: residual {residual}")
        checks.append(
            {"name": name, "expected": str(expected), "status": "verified"}
        )

    # Independent exact backgrounds test normalization, including rotating Kerr.
    es = (x - 1) / (x + 1)
    check("Schwarzschild satisfies normalized Ernst equation", es * D(es) - G(es, es))
    printed_residual = sp.factor(2 * es * D(es) - G(es, es))
    check(
        "Printed Eq. 2.11 has nonzero Schwarzschild residual",
        printed_residual,
        4 * (x - 1) / (x + 1) ** 3,
    )
    ek = 1 - 2 * p / (x + p + sp.I * q * y)
    fk = 1 - 2 * p * (x + p) / ((x + p) ** 2 + q**2 * y**2)
    kerr_residual = sp.factor(sp.cancel(fk * D(ek) - G(ek, ek)))
    check(
        "Kerr satisfies normalized Ernst equation for p^2-q^2=1",
        kerr_residual.subs(p**2, q**2 + 1),
    )
    check("Kerr reduces to Schwarzschild", ek.subs({p: 1, q: 0}) - es)

    # A counterexample to using arbitrary flat-2D holomorphic seeds.
    h = rho**2 - z**2
    flat = sp.diff(h, rho, 2) + sp.diff(h, z, 2)
    axisymmetric = flat + sp.diff(h, rho) / rho
    check("Holomorphic example is flat-2D harmonic", flat)
    check("Same example is not axisymmetric-3D harmonic", axisymmetric, 2)

    # Static, nonrotating reduction: E=exp(2u) obeys N(E)=2 E^2 D(u).
    u = sp.Function("u")(x, y)
    eu = sp.exp(2 * u)
    check("Static Weyl reduction", eu * D(eu) - G(eu, eu) - 2 * eu**2 * D(u))

    # Legendre identities illustrate the known static seed boundary condition.
    Q = [sp.log((x + 1) / (x - 1)) / 2]
    Q.append(x * Q[0] - 1)
    for ell in range(1, 4):
        Q.append(sp.expand(((2 * ell + 1) * x * Q[ell] - ell * Q[ell - 1]) / (ell + 1)))
    for ell in range(5):
        P = sp.legendre(ell, x)
        check(f"P_{ell} radial equation", D(P) - ell * (ell + 1) * P)
        check(f"Q_{ell} radial equation", D(Q[ell]) - ell * (ell + 1) * Q[ell])
        check(f"P_{ell} regular value at horizon", P.subs(x, 1), 1)
        check(
            f"Q_{ell} logarithmic derivative at horizon",
            sp.limit((x - 1) * sp.diff(Q[ell], x), x, 1, dir="+"),
            -sp.Rational(1, 2),
        )
    check("Q_2 decays at infinity", sp.limit(x**3 * Q[2], x, sp.oo), sp.Rational(2, 15))

    # Derive the first and mixed second variations for arbitrary complex fields.
    f0, f1, f2, f12 = [sp.Function(n)(x, y) for n in ("f0", "f1", "f2", "f12")]
    w0, w1, w2, w12 = [sp.Function(n)(x, y) for n in ("w0", "w1", "w2", "w12")]
    e0, e1, e2, e12 = [f + sp.I * w for f, w in zip((f0, f1, f2, f12), (w0, w1, w2, w12))]

    def L(h, real_h):
        return f0 * D(h) + real_h * D(e0) - 2 * G(e0, h)

    alpha, beta, epsilon = sp.symbols("alpha beta epsilon", real=True)
    e = e0 + epsilon * e1 + epsilon**2 * e2
    f = f0 + epsilon * f1 + epsilon**2 * f2
    polynomial = sp.expand(f * D(e) - G(e, e))
    check("First variation of Ernst equation", polynomial.coeff(epsilon, 1) - L(e1, f1))
    check(
        "Second variation with no factorial convention",
        polynomial.coeff(epsilon, 2) - (L(e2, f2) + f1 * D(e1) - G(e1, e1)),
    )
    e = e0 + alpha * e1 + beta * e2 + alpha * beta * e12
    f = f0 + alpha * f1 + beta * f2 + alpha * beta * f12
    mixed = sp.expand(f * D(e) - G(e, e)).coeff(alpha, 1).coeff(beta, 1)
    source = 2 * G(e1, e2) - f1 * D(e2) - f2 * D(e1)
    check("Mixed second variation of Ernst equation", mixed - (L(e12, f12) - source))

    # Angular allowance is not proof of a physical induced response.
    product = sp.legendre(2, y) * sp.legendre(4, y)
    decomposition = (
        sp.Rational(2, 7) * sp.legendre(2, y)
        + sp.Rational(20, 77) * sp.legendre(4, y)
        + sp.Rational(5, 11) * sp.legendre(6, y)
    )
    check("Quadrupole-hexadecapole angular product", product - decomposition)

    return {
        "evidence_level": "exact symbolic consistency checks; no tidal-response coefficient computed",
        "sympy_version": sp.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks_passed": len(checks),
        "checks": checks,
        "diagnostics": {
            "printed_ernst_schwarzschild_residual": str(printed_residual),
            "kerr_residual_before_constraint": str(kerr_residual),
            "holomorphic_axisymmetric_residual": str(axisymmetric),
        },
        "not_established": [
            "The published quadrupolar Kretschmann calculation has not been reproduced.",
            "No all-multipole nonlinear Kerr Love theorem or physical counterexample is proved.",
            "The mixed-field boundary-value problem and effective-field-theory matching are unsolved.",
            "Finite Legendre checks do not replace the general analytic boundary argument.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Save the verified result beside this script.")
    arguments = parser.parse_args()
    result = run()
    if arguments.write:
        target = Path(__file__).parent / "results" / "baseline.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Verified {result['checks_passed']} exact algebra checks (SymPy {sp.__version__}).")
    print(result["evidence_level"])
