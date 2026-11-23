"""Linear distorted-Kerr drivers, exact spin recursion and regularity identities.

This is a declared solution-generating boundary prescription, not a physical
pure-electric source calibration or a computed mixed Love coefficient.
"""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


x, y = sp.symbols("x y", real=True)


def D(h):
    return sp.diff((x*x-1)*sp.diff(h, x), x) + sp.diff((1-y*y)*sp.diff(h, y), y)


def B(a, b):
    return (x*x-1)*sp.diff(a, x)*sp.diff(b, x) + (1-y*y)*sp.diff(a, y)*sp.diff(b, y)


def harmonics():
    r2, z = x*x+y*y-1, x*y
    return [sp.Integer(1), z, (3*z*z-r2)/2, (5*z**3-3*z*r2)/2,
            (35*z**4-30*z*z*r2+3*r2*r2)/8]


def driver(ell):
    H = harmonics()
    n = {2: sp.Rational(1, 3), 4: sp.Rational(1, 105)}[ell]
    psi = sp.expand(H[ell]-1)
    a = 2*(x-y)*sum(H[:ell])
    b = 2*(x+y)*sum((-1)**j*H[j] for j in range(ell))
    sigma, delta = sp.expand(a+b), sp.expand(a-b)
    f = (x-1)/(x+1)
    g = (-x*(x+1)+2*y*y)/(x+1)**3
    u0 = 2*n*f*psi
    v1 = n*(4*y*psi+y*sigma-x*delta)/(x+1)**2
    u2 = n*(2*psi*g+(-x*sigma+y*delta)/(x+1)**2
            + 2*y*(y*sigma-x*delta)/(x+1)**3) - sp.Rational(ell, 2)*u0
    return [sp.factor(v) for v in (u0, v1, u2)], (psi, a, b)


def run():
    checks, solutions = [], {}

    def check(name, actual, expected=0):
        if sp.cancel(sp.expand(actual-expected)) != 0:
            raise AssertionError(f"{name}: {sp.factor(actual-expected)}")
        checks.append({"name": name, "expected": str(expected), "status": "verified"})

    f, t = (x-1)/(x+1), 2*y/(x+1)**2
    g = (-x*(x+1)+2*y*y)/(x+1)**3
    # Independently expand the rational linearization of the exact Ernst map.
    alpha, P, S, T = sp.symbols("alpha P S T", real=True)
    z0, c0 = x*(1-alpha**2)+2*sp.I*alpha*y, 1+alpha**2
    dz, dc = S*(-x*alpha**2+sp.I*alpha*y), alpha**2*S+sp.I*alpha*T
    exact_linear = 2*P*(z0-c0)/(z0+c0)+2*(c0*dz-z0*dc)/(z0+c0)**2
    check("Soliton derivative at spin zero", exact_linear.subs(alpha, 0), 2*f*P)
    check("Soliton derivative at first spin order", sp.diff(exact_linear, alpha).subs(alpha, 0)/2,
          sp.I*(4*y*P+y*S-x*T)/(x+1)**2)
    check("Soliton derivative at second spin order", sp.diff(exact_linear, alpha, 2).subs(alpha, 0)/8,
          2*P*g+(-x*S+y*T)/(x+1)**2+2*y*(y*S-x*T)/(x+1)**3)

    H = harmonics()
    for ell in (2, 4):
        (u0, v1, u2), (psi, aa, bb) = driver(ell)
        check(f"ell{ell} harmonic seed", D(psi))
        check(f"ell{ell} recursion spin0", f*D(u0)+u0*D(f)-2*B(f, u0))
        check(f"ell{ell} recursion spin1", f*D(v1)+u0*D(t)-2*B(f, v1)-2*B(t, u0))
        check(f"ell{ell} recursion spin2", f*D(u2)+g*D(u0)+u2*D(f)+u0*D(g)
              -2*B(f, u2)-2*B(g, u0)+2*B(t, v1))
        for label, field, parity in (("u0", u0, 1), ("v1", v1, -1), ("u2", u2, 1)):
            check(f"ell{ell} {label} reflection", field.subs(y, -y), parity*field)
        check(f"ell{ell} horizon u0", u0.subs(x, 1))
        check(f"ell{ell} horizon v1", v1.subs(x, 1))
        horizon_u2 = -(1-y*y)**2 / 6 if ell == 2 else -(1-y*y)**2*(1+y*y)/210
        check(f"ell{ell} horizon u2", u2.subs(x, 1), horizon_u2)
        check(f"ell{ell} auxiliary horizon a", aa.subs(x, 1), 2*(1-y**ell))
        check(f"ell{ell} auxiliary horizon b", bb.subs(x, 1), 2*(1-y**ell))
        vlin = sum(((-1)**(ell-j+1)*(x+y)-x+y)*H[j] for j in range(ell))
        vquad = sp.Rational(ell, 2)*(H[ell]**2-(x*x+y*y-1)*H[ell-1]**2)
        check(f"ell{ell} V linear horizon", vlin.subs(x, 1), 2*(y**ell-1))
        check(f"ell{ell} V quadratic horizon", vquad.subs(x, 1))
        for pole in (-1, 1):
            check(f"ell{ell} auxiliary axis balance {pole}", (aa+bb).subs(y, pole))
            check(f"ell{ell} auxiliary axis normalization {pole}", aa.subs(y, pole), 2*pole*(x**ell-1))
            check(f"ell{ell} V linear axis {pole}", vlin.subs(y, pole))
            check(f"ell{ell} V quadratic axis {pole}", vquad.subs(y, pole))
        # All polynomial (nondecaying) radial terms are part of the boundary data.
        polynomial_parts = [sp.div(*sp.fraction(v), x)[0] for v in (u0, v1, u2)]
        solutions[str(ell)] = {key: str(val) for key, val in zip(("u0", "v1", "u2"), (u0, v1, u2))}
        solutions[str(ell)]["polynomial_boundary_data"] = [str(sp.factor(v)) for v in polynomial_parts]
        dipole = sp.Rational(3, 2)*sp.integrate(v1*y, (y, -1, 1))
        spin_residue = sp.limit((x+1)**2*dipole, x, -1)
        check(f"ell{ell} declared spin-mode normalization", spin_residue,
              {2: -sp.Rational(16, 15), 4: -sp.Rational(32, 735)}[ell])
        solutions[str(ell)]["spin_mode_residue"] = str(spin_residue)
        leading_imag = sp.Poly(polynomial_parts[1], x).coeff_monomial(x**(ell-1))
        n = {2: sp.Rational(1, 3), 4: sp.Rational(1, 105)}[ell]
        check(f"ell{ell} spin-linked odd growing term", leading_imag, -4*n*sp.legendre(ell-1, y))

    # A denominators cancel from the stationary metric block, including ergosurfaces.
    a, b = sp.symbols("a b", real=True)
    X, Y = x*x-1, 1-y*y
    A = X*(1+a*b)**2-Y*(b-a)**2
    BB = (x+1+(x-1)*a*b)**2+((1+y)*a+(1-y)*b)**2
    C = X*(1+a*b)*(b-a-y*(a+b))+Y*(b-a)*(1+a*b+x*(1-a*b))
    DD = Y*((x+1)**2+a*b*(x-1)**2)**2-X*(a*(1+y)**2-b*(1-y)**2)**2
    check("Stationary block removes A denominators", BB**2*X*Y-4*C**2, A*DD)
    sig, e, K = sp.symbols("sig e K", nonzero=True, real=True)
    gtt = -e*A/BB
    gtp = (2*sig*C+K*e*A)/BB
    gpp = (sig**2*DD/e-4*sig*K*C-K*K*e*A)/BB
    check("Stationary block determinant", gtt*gpp-gtp**2, -sig**2*X*Y)
    horizon = {x: 1, a: -alpha/e, b: alpha/e, K: -4*sig*alpha/(1-alpha**2)}
    tt, tp, pp = [sp.factor(v.subs(horizon, simultaneous=True)) for v in (gtt, gtp, gpp)]
    omega = -alpha*(1-alpha**2)/(2*sig*(1+alpha**2))
    area_scale = 4*sig**2*(1+alpha**2)/(1-alpha**2)**2
    gyy = 4*sig**2*(e*e+alpha*alpha*y*y)/(e*(1-alpha**2)**2*Y)
    check("Horizon generator is null", tt+2*omega*tp+omega**2*pp)
    check("Horizon generator orthogonal to axial direction", tp+omega*pp)
    check("Horizon area determinant", gyy*pp, area_scale**2)
    ingoing_residue = area_scale/sig
    check("Ingoing radial pole cancellation", gyy*Y-ingoing_residue**2*sig**2*Y/pp)
    shape = (1+alpha**2)*Y*e/(alpha**2*y*y+e*e)
    # At either pole e=1, and the e' term vanishes because Y=0.
    for pole in (-1, 1):
        check(f"Horizon axis slope {pole}", sp.diff(shape, y).subs({y: pole, e: 1}), -2*pole)

    # Schwarzschild operator reduction and representative radial branches.
    U, W = sp.Function("U")(x, y), sp.Function("W")(x, y)
    check("Real kernel reduction", f*D(f*U)+f*U*D(f)-2*B(f, f*U), f*f*D(U))
    check("Imaginary kernel reduction", f*D(W)-2*B(f, W), f*(D(W)-4*sp.diff(W, x)))
    ell_symbol = sp.Symbol("ell", integer=True, nonnegative=True)
    leg = sp.Function("leg")(x)
    radial = (x-1)**2*sp.diff(leg, x, 2)
    legendre_equation = (x*x-1)*sp.diff(leg, x, 2)+2*x*sp.diff(leg, x)-ell_symbol*(ell_symbol+1)*leg
    check("All-ell differentiated Legendre identity", (x*x-1)*sp.diff(radial, x, 2)
          +(2*x-4)*sp.diff(radial, x)-ell_symbol*(ell_symbol+1)*radial,
          (x-1)**2*sp.diff(legendre_equation, x, 2))
    Q = [sp.log((x+1)/(x-1))/2]
    Q.append(x*Q[0]-1)
    for ell in range(1, 5):
        Q.append(((2*ell+1)*x*Q[ell]-ell*Q[ell-1])/(ell+1))
    for ell in (2, 3, 4, 5):
        for label, leg in (("P", sp.legendre(ell, x)), ("Q", Q[ell])):
            radial = (x-1)**2*sp.diff(leg, x, 2)
            check(f"Imaginary {label}{ell} radial equation", (x*x-1)*sp.diff(radial, x, 2)
                  +(2*x-4)*sp.diff(radial, x)-ell*(ell+1)*radial)
        radial = (x-1)**2*sp.diff(Q[ell], x, 2)
        check(f"Imaginary Q{ell} finite horizon value", sp.limit(radial, x, 1, dir="+"), sp.Rational(1, 2))
        check(f"Imaginary Q{ell} horizon derivative", sp.limit(sp.diff(radial, x), x, 1, dir="+"), -sp.Rational(ell*(ell+1), 4))
    for label, radial, ell in (("rotation", x-2, 1), ("spin", 1/(x+1)**2, 1),
                               ("twist constant", 1, 0), ("NUT", x/(x+1)**2, 0)):
        check(f"Exceptional radial mode {label}", (x*x-1)*sp.diff(radial, x, 2)
              +(2*x-4)*sp.diff(radial, x)-ell*(ell+1)*radial)

    return {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__, "checks_passed": len(checks), "checks": checks,
        "evidence_level": "Exact linear Ernst recursion and metric regularity identities for a prescribed family; conditional finite-mode uniqueness",
        "solutions": solutions,
        "not_established": ["Pure-electric physical tidal calibration", "Unrestricted global uniqueness or convergent spin series",
                            "Mixed driven solution or independent response coefficient", "Novelty of this reconstruction"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write:
        (Path(__file__).parent / "results" / "linear-drivers.json").write_text(json.dumps(result, indent=2)+"\n")
    print(f"Verified {result['checks_passed']} linear-driver checks; no mixed response computed.")
