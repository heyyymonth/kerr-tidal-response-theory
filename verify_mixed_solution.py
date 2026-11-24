"""Mixed two-seed Ernst solution through spin squared, with declared data.

Differentiate a known exact vacuum family; independently check the forced
equations and polynomial boundary data. No matched Love coefficient is inferred.
"""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

from verify_linear_drivers import B, D, driver, harmonics, x, y


def mixed_fields():
    _, (p, a, b) = driver(2)
    _, (q, c, d) = driver(4)
    n = sp.Rational(1, 315)
    f = (x-1)/(x+1)
    w0 = 4*n*f*p*q
    w1 = n*((y-x)*(2*p+a)*(2*q+c)+(y+x)*(2*p+b)*(2*q+d))/(x+1)**2
    w2 = n*((y+1)*(y-x)*(2*p+2*a)*(2*q+2*c)
            +(y-1)*(y+x)*(2*p+2*b)*(2*q+2*d)
            +2*(y*y-x*x)*(2*p+a+b)*(2*q+c+d))/(2*(x+1)**3)-3*w0
    return [sp.factor(v) for v in (w0, w1, w2)]


def mixed_source():
    a0, a1, a2 = driver(2)[0]
    b0, b1, b2 = driver(4)[0]
    return [sp.factor(v) for v in (
        2*B(a0, b0)-a0*D(b0)-b0*D(a0),
        2*B(a0, b1)+2*B(a1, b0)-a0*D(b1)-b0*D(a1),
        2*B(a0, b2)+2*B(a2, b0)-2*B(a1, b1)
        -a0*D(b2)-a2*D(b0)-b0*D(a2)-b2*D(a0),
    )]


def polynomial_part(field):
    return sp.factor(sp.div(*sp.fraction(sp.cancel(field)), x)[0])


def project(field, ell):
    return sp.factor(sp.Rational(2*ell+1, 2)*sp.integrate(sp.expand(field)*sp.legendre(ell, y), (y, -1, 1)))


def run():
    checks = []

    def check(name, actual, expected=0):
        residual = sp.cancel(sp.expand(actual-expected))
        if residual != 0:
            raise AssertionError(f"{name}: {sp.factor(residual)}")
        checks.append({"name": name, "expected": str(expected), "status": "verified"})

    # Derive the spin expansion of the exact map with independent exponentials.
    # This avoids invoking the claimed field equations to construct a solution.
    alpha, ea, eb = sp.symbols("alpha ea eb", real=True)
    z = x*(1-alpha**2*ea*eb)+sp.I*alpha*y*(ea+eb)
    ce = 1+alpha**2*ea*eb+sp.I*alpha*(ea-eb)
    ratio = (z-ce)/(z+ce)
    f, t = (x-1)/(x+1), 2*y/(x+1)**2
    g = (-x*(x+1)+2*y*y)/(x+1)**3
    check("Exact map at spin zero", ratio.subs(alpha, 0), f)
    r1 = ((y-x)*ea+(y+x)*eb)/(x+1)**2
    r2 = ((y+1)*(y-x)*ea**2+(y-1)*(y+x)*eb**2
          +2*(y*y-x*x)*ea*eb)/(2*(x+1)**3)
    check("Exact map at first spin order", sp.diff(ratio, alpha).subs(alpha, 0)/2, sp.I*r1)
    check("Exact map at second spin order", sp.diff(ratio, alpha, 2).subs(alpha, 0)/8, r2)
    check("Kerr first spin coefficient", r1.subs({ea: 1, eb: 1}), t)
    check("Kerr second spin coefficient", r2.subs({ea: 1, eb: 1}), g)

    # Independent amplitude derivatives of the exponential form at fixed c2,c4.
    c2, c4 = sp.symbols("c2 c4", real=True)
    p, aa, bb = driver(2)[1]
    q, cc, dd = driver(4)[1]
    U = c2*p+c4*q
    exponents = {ea: sp.exp(c2*aa+c4*cc), eb: sp.exp(c2*bb+c4*dd)}
    w0, w1, w2 = mixed_fields()
    for label, coefficient, target in (("w0", f, w0), ("w1", r1, w1), ("w2", r2, w2+3*w0)):
        exact = sp.exp(2*U)*coefficient.subs(exponents)
        derived = sp.diff(exact, c2, c4).subs({c2: 0, c4: 0})/315
        check(f"Mixed amplitude derivative {label}", derived, target)
    chi = sp.symbols("chi", real=True)
    check("Combined k to sixth power correction", sp.diff((1-chi**2)**3, chi, 2).subs(chi, 0)/2, -3)

    s0, s1, s2 = mixed_source()
    check("Forced mixed equation spin0", f*D(w0)+w0*D(f)-2*B(f, w0), s0)
    check("Forced mixed equation spin1", f*D(w1)+w0*D(t)-2*B(f, w1)-2*B(t, w0), s1)
    check("Forced mixed equation spin2", f*D(w2)+g*D(w0)+w2*D(f)+w0*D(g)
          -2*B(f, w2)-2*B(g, w0)+2*B(t, w1), s2)
    check("Static product identity", w0, driver(2)[0][0]*driver(4)[0][0]/f)

    fields, sources = {}, {}
    for label, field, source, parity in zip(("w0", "w1", "w2"), (w0, w1, w2), (s0, s1, s2), (1, -1, 1)):
        check(f"{label} reflection", field.subs(y, -y), parity*field)
        check(f"{label} source reflection", source.subs(y, -y), parity*source)
        poly = polynomial_part(field)
        tail = sp.factor(field-poly)
        check(f"{label} boundary split", field, poly+tail)
        check(f"{label} remainder decays", sp.limit(tail, x, sp.oo))
        # Exact angular reconstruction independently records every finite mode.
        degree = sp.Poly(sp.fraction(field)[0], y).degree()
        modes = {str(j): project(field, j) for j in range(0 if parity == 1 else 1, degree+1, 2)}
        check(f"{label} Legendre reconstruction", field, sum(v*sp.legendre(int(j), y) for j, v in modes.items()))
        fields[label] = {"expression": str(field), "polynomial_boundary_data": str(poly),
                         "decaying_remainder": str(tail), "angular_modes": {j: str(v) for j, v in modes.items()}}
        sources[label] = str(source)

    check("Mixed horizon w0", w0.subs(x, 1))
    check("Mixed horizon w1", w1.subs(x, 1))
    # The spin-squared horizon coefficient follows independently from gtt,H.
    horizon_w2 = -sp.Rational(1, 315)*(1-y*y)**3*(1+y*y)
    check("Mixed horizon w2", w2.subs(x, 1), horizon_w2)

    H = harmonics()
    cross_V = sp.Rational(8, 3)*(H[2]*H[4]-(x*x+y*y-1)*H[1]*H[3])
    check("Mixed V horizon identity", cross_V.subs(x, 1))
    for pole in (-1, 1):
        check(f"Mixed V axis identity {pole}", cross_V.subs(y, pole))
    # Cross term coefficient in the published symmetric double sum.
    check("Mixed V coefficient counts both indices", sp.Rational(2*4, 2+4)+sp.Rational(4*2, 4+2), sp.Rational(8, 3))

    dipole = project(w1, 1)
    zeta = sp.symbols("zeta", real=True)
    residue = sp.expand(sp.apart(dipole.subs(x, zeta-1), zeta)).coeff(zeta, -2)
    # A numerical value is prescribed and verified, not identified with a charge.
    spin_residue = sp.factor(residue)
    check("Declared mixed spin-mode residue", spin_residue, sp.Rational(1024, 33075))
    quadrupoles = {}
    for label, field in (("w0", w0), ("w2", w2)):
        radial = project(field, 2)
        # Raw x^-3 coefficient, not a homogeneous Q2 branch amplitude.
        inverse = sp.cancel((radial-polynomial_part(radial)).subs(x, 1/zeta))
        raw = sp.factor(sp.diff(inverse, zeta, 3).subs(zeta, 0)/6)
        quadrupoles[label] = {"radial_projection": str(radial), "polynomial_part": str(polynomial_part(radial)),
                             "raw_x_minus3_coefficient": str(raw)}

    return {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__, "checks_passed": len(checks), "checks": checks,
        "evidence_level": "Explicit forced mixed solution and local regularity in a known family with declared boundary data; no response matching",
        "mixed_convention": "Coefficient of epsilon2 epsilon4, with no factorial; w0+i chi w1+chi^2 w2",
        "solutions": fields, "sources": sources,
        "mixed_V_cross_coefficient_in_c2_c4": str(sp.factor(cross_V)),
        "spin_dipole": str(sp.apart(dipole, x)), "spin_mode_residue": str(spin_residue),
        "coordinate_quadrupoles_not_responses": quadrupoles,
        "not_established": ["Pure-electric physical source calibration", "A canonical mathematical response functional",
                            "Independent Love coefficient", "Unrestricted uniqueness or convergence of the spin series", "Novelty of the exact family"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write:
        destination = Path(__file__).resolve().parent / "results/mixed-solution.json"
        destination.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Verified {result['checks_passed']} mixed-solution checks; no independent response coefficient computed.")
