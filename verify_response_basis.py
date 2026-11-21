"""Exact STF algebra and coordinate calibration; no Kerr response is computed."""

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path

import sympy as sp


def stf2(n):
    norm = sum(v * v for v in n)
    return sp.Matrix(3, 3, lambda i, j: n[i] * n[j] - norm * sp.KroneckerDelta(i, j) / 3)


def stf4(n):
    norm = sum(v * v for v in n)
    d = sp.KroneckerDelta
    return {
        (i, j, k, l): n[i] * n[j] * n[k] * n[l]
        - norm * (
            d(i, j) * n[k] * n[l] + d(i, k) * n[j] * n[l]
            + d(i, l) * n[j] * n[k] + d(j, k) * n[i] * n[l]
            + d(j, l) * n[i] * n[k] + d(k, l) * n[i] * n[j]
        ) / 7
        + norm**2 * (d(i, j) * d(k, l) + d(i, k) * d(j, l) + d(i, l) * d(j, k)) / 35
        for i, j, k, l in product(range(3), repeat=4)
    }


def invariants(a, b, s):
    indices4 = list(product(range(3), repeat=4))
    norm = sum(v * v for v in s)
    i0 = norm * sum(a[i, j] * a[k, l] * b[i, j, k, l] for i, j, k, l in indices4)
    i1 = sum(s[i] * s[j] * b[i, j, k, l] * a[k, m] * a[l, m]
             for i, j, k, l, m in product(range(3), repeat=5))
    i2 = sum(s[i] * a[i, j] * b[j, k, l, m] * a[k, l] * s[m]
             for i, j, k, l, m in product(range(3), repeat=5))
    return [sp.expand(v) for v in (i0, i1, i2)]


def run():
    checks = []

    def check(name, actual, expected=0):
        if sp.simplify(sp.expand(actual - expected)) != 0:
            raise AssertionError(f"{name}: {actual} != {expected}")
        checks.append({"name": name, "expected": str(expected), "status": "verified"})

    n = sp.Matrix([0, 0, 1])
    a, b = stf2(n), stf4(n)
    check("Rank-two axial tensor is trace free", sp.trace(a))
    check("Rank-two axial tensor norm", sp.trace(a * a), sp.Rational(2, 3))
    check("Rank-four axial tensor norm", sum(v * v for v in b.values()), sp.Rational(8, 35))
    for k in range(3):
        for l in range(k, 3):
            check(f"Rank-four trace ({k},{l})", sum(b[i, i, k, l] for i in range(3)))

    # STF(n^l) X^l = l!/(2l-1)!! R^l P_l(cos theta).
    X, Y, Z = sp.symbols("X Y Z", real=True)
    pos = [X, Y, Z]
    r2 = X**2 + Y**2 + Z**2
    h2 = (3 * Z**2 - r2) / 2
    h4 = (35 * Z**4 - 30 * Z**2 * r2 + 3 * r2**2) / 8
    check("Quadrupole Taylor normalization", sum(a[i, j] * pos[i] * pos[j]
          for i, j in product(range(3), repeat=2)) / 2, h2 / 3)
    check("Hexadecapole Taylor normalization", sum(b[idx] * sp.prod(pos[i] for i in idx)
          for idx in b) / 24, h4 / 105)

    weights = invariants(a, b, n)
    for index, value in enumerate([sp.Rational(8, 35), sp.Rational(8, 105), sp.Rational(16, 105)]):
        check(f"Aligned invariant I{index}", weights[index], value)

    witness = sp.Matrix([weights, invariants(a, b, [1, 0, 0]),
                         invariants(sp.diag(1, -1, 0), b, n)])
    check("Independent-contraction witness determinant", witness.det(), -sp.Rational(128, 25725))
    # Angular momenta j of Sym^2(V2) are even; spin-square has L=0,2.
    channels = [(j, ell) for j in (0, 2, 4) for ell in (0, 2) if abs(j - 4) <= ell <= j + 4]
    check("SO(3) scalar multiplicity in declared sector", len(channels), 3)
    check("Aligned measurement rank", sp.Matrix([weights]).rank(), 1)
    for index, null in enumerate(([1, -3, 0], [0, -2, 1])):
        check(f"Unmeasurable aligned direction {index}", (sp.Matrix([weights]) * sp.Matrix(null))[0])

    # A nontrivial rational spatial rotation checks all three contractions.
    rotation = sp.Matrix([[sp.Rational(3, 5), 0, sp.Rational(4, 5)], [0, 1, 0],
                          [-sp.Rational(4, 5), 0, sp.Rational(3, 5)]])
    generic_a = sp.Matrix([[1, 2, 3], [2, -2, 4], [3, 4, 1]])
    generic_s = sp.Matrix([2, -1, 3])
    rotated = invariants(rotation * generic_a * rotation.T, stf4(rotation * n), rotation * generic_s)
    for index, (left, right) in enumerate(zip(rotated, invariants(generic_a, b, generic_s))):
        check(f"Rotation covariance I{index}", left, right)

    eta2, eta4, chi, c0, c1, c2 = sp.symbols("eta2 eta4 chi c0 c1 c2", real=True)
    w = sum(c * value for c, value in zip((c0, c1, c2), weights)) * eta2**2 * eta4 * chi**2
    kappa = -sp.Rational(16, 35) * (3 * c0 + c1 + 2 * c2)
    check("Projected quadrupole response normalization", -3 * sp.diff(w, eta2), kappa * eta2 * eta4 * chi**2)
    # Check all five independent STF variations, not only the axial derivative.
    variations = [sp.diag(1, -1, 0), sp.diag(0, 1, -1)]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        t = sp.zeros(3)
        t[i, j] = t[j, i] = 1
        variations.append(t)
    epsilon = sp.Symbol("epsilon")
    for index, t in enumerate(variations):
        varied = invariants(eta2 * a + epsilon * t, {key: eta4 * val for key, val in b.items()}, chi * n)
        dw = sp.diff(sum(c * value for c, value in zip((c0, c1, c2), varied)), epsilon).subs(epsilon, 0)
        check(f"Full STF response variation {index}", -2 * dw, kappa * eta2 * eta4 * chi**2 * sp.trace(a * t))

    # These are harmonic-coordinate identities, not the Kerr source/response map.
    x, y, k, u2, u4 = sp.symbols("x y k u2 u4", real=True, nonzero=True)
    R2, z = k**2 * (x**2 + y**2 - 1), k * x * y
    H2, H4 = (3 * z**2 - R2) / 2, (35 * z**4 - 30 * z**2 * R2 + 3 * R2**2) / 8
    p2, p4 = sp.legendre(2, x) * sp.legendre(2, y), sp.legendre(4, x) * sp.legendre(4, y)
    check("Prolate quadrupole to solid harmonic", p2, 3 * H2 / (2 * k**2) - sp.Rational(1, 2))
    check("Prolate hexadecapole to solid harmonics", p4, 35 * H4 / (8 * k**4) - 15 * H2 / (4 * k**2) + sp.Rational(3, 8))
    alpha4 = sp.Rational(8, 35) * k**4 * u4
    alpha2 = sp.Rational(2, 3) * k**2 * u2 + sp.Rational(4, 7) * k**4 * u4
    alpha0 = sp.Rational(1, 3) * k**2 * u2 + sp.Rational(1, 5) * k**4 * u4
    check("Pure prescribed harmonic data after calibration", alpha0 + alpha2 * p2 + alpha4 * p4, u2 * H2 + u4 * H4)
    check("Spin-square scale correction to alpha4", sp.expand(alpha4.subs(k**4, (1 - chi**2)**2)).coeff(chi, 2), -sp.Rational(16, 35) * u4)
    check("Spin-square scale correction to alpha2", sp.expand(alpha2.subs(k**4, (1 - chi**2)**2).subs(k**2, 1 - chi**2)).coeff(chi, 2), -sp.Rational(2, 3) * u2 - sp.Rational(8, 7) * u4)

    return {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__,
        "evidence_level": "Exact local STF algebra and harmonic-coordinate calibration; no matched Kerr coefficient",
        "checks_passed": len(checks), "checks": checks,
        "aligned_invariant_weights": [str(v) for v in weights],
        "independence_witness": [[str(v) for v in witness.row(i)] for i in range(3)],
        "angular_momentum_channels": [list(channel) for channel in channels],
        "kappa_parallel_convention": str(kappa),
        "not_established": ["Full on-shell EFT basis and source map", "Horizon/axis boundary solution",
                            "Any physical value of c0,c1,c2 or kappa_parallel", "Channel-specific novelty"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Save this new deterministic algebra record.")
    args = parser.parse_args()
    result = run()
    if args.write:
        (Path(__file__).parent / "results" / "response-basis.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"Verified {result['checks_passed']} response-basis checks; no physical coefficient computed.")
