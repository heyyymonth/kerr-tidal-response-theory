"""Quadrupolar radial reduction and a declared finite-part connection coefficient.

The reference primitive is constructed from the source alone. The resulting
coefficient is subtraction dependent and is not a matched physical Love number.
"""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

from verify_linear_drivers import B, D, x, y
from verify_mixed_solution import mixed_fields, mixed_source, polynomial_part, project


X = x*x-1
P = sp.legendre(2, x)
Q = P*sp.log((x+1)/(x-1))/2-3*x/2
f = (x-1)/(x+1)


def radial_operator(r):
    return sp.diff(X*sp.diff(r, x), x)-6*r


def flux(r):
    return X*(P*sp.diff(r, x)-sp.diff(P, x)*r)


def finite_part_infinity(r):
    return sp.expand(polynomial_part(r)).coeff(x, 0)


def radial_sources():
    # The spin-squared source uses only already fixed lower spin coefficients.
    w0, w1 = mixed_fields()[:2]
    s0, _, s2 = mixed_source()
    t = 2*y/(x+1)**2
    g = (-x*(x+1)+2*y*y)/(x+1)**3
    effective2 = s2-g*D(w0)-w0*D(g)+2*B(g, w0)-2*B(t, w1)
    return [sp.factor(project(sp.cancel(v), 2)/f**2) for v in (s0, effective2)]


def source_primitive(source):
    """Integrate P*source using only its polynomial part and its pole data.

    This declared source class has poles only at +/-1 of order at most three,
    with no simple-pole residues. Reject any input outside that class.
    """
    integrand = sp.cancel(P*source)
    poly = polynomial_part(integrand)
    reconstruction = poly
    primitive = sp.integrate(poly, x)
    residues = {}
    for center in (-1, 1):
        cleared = sp.cancel((x-center)**3*integrand)
        for order in (1, 2, 3):
            coefficient = sp.factor(sp.diff(cleared, x, 3-order).subs(x, center)/sp.factorial(3-order))
            if order == 1:
                residues[str(center)] = coefficient
                if coefficient != 0:
                    raise ValueError("A simple pole would require a logarithmic prescription")
            else:
                primitive += coefficient*(x-center)**(1-order)/(1-order)
            reconstruction += coefficient/(x-center)**order
    if sp.cancel(integrand-reconstruction) != 0:
        raise ValueError("Source is outside the declared rational pole class")
    return sp.factor(primitive), residues


def laurent_coefficients(r, lower=-7, upper=6):
    z = sp.Symbol("z", positive=True)
    series = sp.series(sp.cancel(r.subs(x, 1/z)), z, 0, -lower+1).removeO().expand()
    return {n: series.coeff(z, -n) for n in range(lower, upper+1)}


def frobenius_particular(source):
    """Source-only formal reference, with a_2=a_-3=0, through x^-7."""
    fc = laurent_coefficients(source)
    ac, compatibility = {}, {}
    for n in range(6, -8, -1):
        rhs = sp.factor(fc[n]+(n+2)*(n+1)*ac.get(n+2, 0))
        if n in (2, -3):
            compatibility[n] = rhs
            if rhs != 0:
                raise ValueError("Resonance requires logarithms")
            ac[n] = sp.Integer(0)
        else:
            ac[n] = rhs/((n-2)*(n+3))
    return ac, compatibility


def run():
    checks, sectors = [], {}

    def check(name, actual, expected=0):
        residual = sp.cancel(sp.expand(actual-expected))
        if residual != 0:
            raise AssertionError(f"{name}: {sp.factor(residual)}")
        checks.append({"name": name, "expected": str(expected), "status": "verified"})

    check("Growing Legendre branch equation", radial_operator(P))
    check("Decaying Legendre branch equation", radial_operator(Q))
    check("Growing branch flux", flux(P))
    check("Decaying branch Wronskian normalization", flux(Q), -1)
    z = sp.Symbol("z", positive=True)
    check("Q2 asymptotic normalization", sp.expand(sp.series(Q.subs(x, 1/z), z, 0, 4).removeO()).coeff(z, 3), sp.Rational(2, 15))
    r = sp.Function("r")(x)
    check("Arbitrary-function Lagrange identity", sp.diff(flux(r), x), P*radial_operator(r))
    check("Real quadrupolar operator reduction",
          f*D(f*r*sp.legendre(2, y))+f*r*sp.legendre(2, y)*D(f)-2*B(f, f*r*sp.legendre(2, y)),
          f**2*sp.legendre(2, y)*radial_operator(r))

    w0, _, w2 = mixed_fields()
    sources = radial_sources()
    aa, bb, lam = sp.symbols("aa bb lambda", real=True)
    expected_b = [sp.Integer(0), -sp.Rational(16172, 218295)]
    expected_laurent = [sp.Integer(0), -sp.Rational(1184, 14553)]
    for index, (order, field, source) in enumerate(zip((0, 2), (w0, w2), sources)):
        label = f"spin{order}"
        radial = sp.factor(project(field, 2)/f)
        J, residues = source_primitive(source)
        C = sp.factor(flux(radial))
        response = sp.factor(J-C)
        check(f"{label} projected forced equation", radial_operator(radial), source)
        for center, residue in residues.items():
            check(f"{label} source simple-pole residue {center}", residue)
        check(f"{label} source-only primitive derivative", sp.diff(J, x), P*source)
        check(f"{label} primitive zero finite part", finite_part_infinity(J))
        check(f"{label} flux source identity", sp.diff(C, x), P*source)
        check(f"{label} connection coefficient", response, expected_b[index])
        check(f"{label} asymptotic extraction", -finite_part_infinity(C), response)
        check(f"{label} homogeneous additions", J-flux(radial+aa*P+bb*Q), response+bb)

        # Source-determined horizon pole and regularity-derived coefficient.
        horizon_pole = sp.limit((x-1)**2*source, x, 1, dir="+")/2
        check(f"{label} source fixes horizon pole", sp.limit((x-1)*radial, x, 1, dir="+"), horizon_pole)
        horizon_J = sp.limit(J+2*horizon_pole/(x-1), x, 1, dir="+")
        check(f"{label} source and horizon derive response", horizon_J+13*horizon_pole, response)
        check(f"{label} finite projected Ernst horizon value", project(field, 2).subs(x, 1), horizon_pole/2)

        # A second, source-only formal reference demonstrates subtraction dependence.
        ref, resonances = frobenius_particular(source)
        for n, residual in resonances.items():
            check(f"{label} Frobenius compatibility n={n}", residual)
        rc = laurent_coefficients(radial)
        b_laurent = sp.Rational(15, 2)*rc[-3]
        check(f"{label} Laurent-reference coefficient", b_laurent, expected_laurent[index])
        check(f"{label} flux coefficient formula", sp.Rational(15, 2)*rc[-3]-5*rc[-1]-rc[1]/2, response)
        formal_reference = sum(a*x**n for n, a in ref.items())
        difference_coeffs = laurent_coefficients(radial-formal_reference-sp.Rational(2, 3)*rc[2]*P-b_laurent*Q)
        check(f"{label} independent Frobenius reference through x^-7", sum(a*x**n for n, a in difference_coeffs.items()))
        # This shift vanishes for zero source and for the static source.
        check(f"{label} source-dependent subtraction shift", (J+lam*horizon_pole)-C, response+lam*horizon_pole)

        sectors[str(order)] = {
            "radial_solution": str(sp.apart(radial, x)), "radial_source": str(sp.apart(source, x)),
            "source_only_primitive": str(sp.apart(J, x)), "flux": str(sp.apart(C, x)),
            "finite_part_connection_coefficient": str(response),
            "horizon_forced_pole": str(horizon_pole), "horizon_primitive_finite_part": str(horizon_J),
            "reference_horizon_log_coefficient": str(response/2),
            "laurent_reference_coefficient": str(b_laurent),
            "laurent_reference_coefficients": {str(n): str(a) for n, a in ref.items()},
            "selected_solution_laurent_coefficients": {str(n): str(rc[n]) for n in (2, 1, -1, -3)},
        }

    # Leading horizon balance for a forced pole plus a possible logarithm.
    s = sp.Symbol("s", positive=True)
    pole, logc = sp.symbols("pole logc", real=True)
    trial = pole/(x-1)+logc*sp.log(x-1)
    check("Horizon flux finite part with forced pole and logarithm",
          sp.limit((flux(trial)+2*pole/(x-1)).subs(x, 1+s), s, 0, dir="+"), 2*logc-13*pole)
    # Domain/Legendre basis are transformed together in this coordinate diagnostic.
    C2 = sp.sympify(sectors["2"]["flux"], locals={"x": x})
    shifted_fp = finite_part_infinity(C2.subs(x, x+1))
    check("Shifted-coordinate finite part diagnostic", -shifted_fp, sp.Rational(2944, 43659))

    return {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__, "checks_passed": len(checks), "checks": checks,
        "evidence_level": "Exact quadrupolar reduction and source-only finite-part connection coefficient in fixed coordinates; subtraction dependent",
        "definition": "b=J[F]-(x^2-1)(P2 R'-P2' R), J'=P2 F, FP_infinity J=0, R=Pi2(w)/f",
        "sectors": sectors,
        "not_established": ["Canonical response independent of subtraction or coordinates", "Physical Love coefficient",
                            "Pure-electric tidal calibration", "Disproof of the independently matched vanishing conjecture"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write:
        destination = Path(__file__).resolve().parent / "results/radial-response.json"
        destination.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Verified {result['checks_passed']} radial-response checks; the connection coefficient depends on the declared subtraction.")
