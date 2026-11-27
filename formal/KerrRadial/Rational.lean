import KerrRadial.Basic

noncomputable section

namespace KerrRadial

open Polynomial

/-- Polynomial fractions together with a quotient-rule derivative. -/
structure Fraction where
  numerator : Polynomial ℝ
  denominator : Polynomial ℝ

namespace Fraction

def eval (r : Fraction) (x : ℝ) : ℝ := r.numerator.eval x / r.denominator.eval x

def diff (r : Fraction) : Fraction :=
  ⟨r.numerator.derivative * r.denominator - r.numerator * r.denominator.derivative,
    r.denominator ^ 2⟩

theorem hasDerivAt (r : Fraction) (x : ℝ) (h : r.denominator.eval x ≠ 0) :
    HasDerivAt r.eval (r.diff.eval x) x := by
  simpa only [eval, diff, eval_sub, eval_mul, eval_pow] using
    (r.numerator.hasDerivAt x).div (r.denominator.hasDerivAt x) h

end Fraction

/-- The rational solution recorded for the spin-squared quadrupolar channel. -/
def solution2 : Fraction := ⟨
  -2376 * X^9 - 3168 * X^8 - 3960 * X^7 + 4536 * X^6 + 8744 * X^5 +
    26152 * X^4 + 14264 * X^3 - 46392 * X^2 - 15072 * X + 21624,
  218295 * (X - 1) * (X + 1)^2⟩

/-- Independently stated source, not defined by differentiating `solution2`. -/
def source2 : Fraction := ⟨
  -85536 * X^11 - 104544 * X^10 + 145728 * X^9 + 260064 * X^8 +
    88992 * X^7 - 309536 * X^6 - 341472 * X^5 + 379296 * X^4 +
    261376 * X^3 - 360960 * X^2 - 69600 * X + 153600,
  218295 * (X - 1)^2 * (X + 1)^3⟩

/-- Independently stated source primitive, in the zero-polynomial-constant convention. -/
def primitive2 : Fraction := ⟨
  -14256 * X^12 - 17820 * X^11 + 15444 * X^10 + 38484 * X^9 +
    35316 * X^8 - 70824 * X^7 - 67784 * X^6 + 147864 * X^5 +
    8232 * X^4 - 178984 * X^3 + 23176 * X^2 + 74624 * X - 2176,
  218295 * (X - 1) * (X + 1)^2⟩

theorem solution2_denominator_ne_zero (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    solution2.denominator.eval x ≠ 0 := by
  simp [solution2, hm, hp]

theorem primitive2_denominator_ne_zero (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    primitive2.denominator.eval x ≠ 0 := by
  simp [primitive2, hm, hp]

set_option maxRecDepth 4096 in
set_option maxHeartbeats 2000000 in
theorem primitive2_derivative_identity (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    primitive2.diff.eval x = legendreP x * source2.eval x := by
  simp [Fraction.eval, Fraction.diff, primitive2, source2, legendreP,
    derivative_pow, derivative_mul, derivative_sub, derivative_add]
  field_simp [hm, hp]
  ring

/-- The primitive differentiates to P₂ F₂ away from the two poles. -/
theorem primitive2_hasDerivAt (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    HasDerivAt primitive2.eval (legendreP x * source2.eval x) x := by
  rw [← primitive2_derivative_identity x hm hp]
  exact primitive2.hasDerivAt x (primitive2_denominator_ne_zero x hm hp)

set_option maxRecDepth 4096 in
set_option maxHeartbeats 4000000 in
/-- The recorded connection is constant in the stated primitive convention. -/
theorem connection2_identity (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    primitive2.eval x - fluxJet x (solution2.eval x) (solution2.diff.eval x) =
      -16172 / 218295 := by
  simp [Fraction.eval, Fraction.diff, primitive2, solution2, fluxJet, p, legendreP,
    derivative_pow, derivative_mul, derivative_sub, derivative_add]
  field_simp [hm, hp]
  ring

set_option maxRecDepth 4096 in
set_option maxHeartbeats 8000000 in
/-- The independently specified rational solution satisfies the independently specified source. -/
theorem solution2_radial_identity (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    radialJet x (solution2.eval x) (solution2.diff.eval x) (solution2.diff.diff.eval x) =
      source2.eval x := by
  simp [Fraction.eval, Fraction.diff, solution2, source2, radialJet, p,
    derivative_pow, derivative_mul, derivative_sub, derivative_add]
  field_simp [hm, hp]
  ring

/-- First analytic derivative of the rational solution. -/
theorem solution2_hasDerivAt (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    HasDerivAt solution2.eval (solution2.diff.eval x) x :=
  solution2.hasDerivAt x (solution2_denominator_ne_zero x hm hp)

/-- Second analytic derivative; the quotient-rule certificate is an actual derivative. -/
theorem solution2_diff_hasDerivAt (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    HasDerivAt solution2.diff.eval (solution2.diff.diff.eval x) x := by
  apply solution2.diff.hasDerivAt
  simpa only [Fraction.diff, eval_pow] using
    pow_ne_zero 2 (solution2_denominator_ne_zero x hm hp)

/-- Analytic radial ODE, with the first derivative represented by its proved fraction. -/
theorem solution2_ode_certificate (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    p x * deriv solution2.diff.eval x + 2 * x * deriv solution2.eval x -
      6 * solution2.eval x = source2.eval x := by
  rw [(solution2_diff_hasDerivAt x hm hp).deriv, (solution2_hasDerivAt x hm hp).deriv]
  exact solution2_radial_identity x hm hp

/-- The derivative fraction agrees locally with the analytic derivative, away from its poles. -/
theorem solution2_second_hasDerivAt (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    HasDerivAt (deriv solution2.eval) (solution2.diff.diff.eval x) x := by
  apply (solution2_diff_hasDerivAt x hm hp).congr_of_eventuallyEq
  have hden : ∀ᶠ y in nhds x, solution2.denominator.eval y ≠ 0 :=
    (solution2.denominator.hasDerivAt x).continuousAt.eventually_ne
      (solution2_denominator_ne_zero x hm hp)
  exact hden.mono fun y hy => (solution2.hasDerivAt y hy).deriv

/-- The ordinary second-order radial equation, stated with two analytic derivatives. -/
theorem solution2_ode (x : ℝ) (hm : x - 1 ≠ 0) (hp : x + 1 ≠ 0) :
    p x * deriv (deriv solution2.eval) x + 2 * x * deriv solution2.eval x -
      6 * solution2.eval x = source2.eval x := by
  rw [(solution2_second_hasDerivAt x hm hp).deriv, (solution2_hasDerivAt x hm hp).deriv]
  exact solution2_radial_identity x hm hp

end KerrRadial
