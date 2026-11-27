import Mathlib.Analysis.Calculus.Deriv.Polynomial
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Kernel-checked statements for the reduced quadrupolar radial equation.
The reduction from the Ernst equation and metric regularity are not formalized here.
-/

noncomputable section

namespace KerrRadial

def p (x : ℝ) : ℝ := x ^ 2 - 1
def legendreP (x : ℝ) : ℝ := (3 * x ^ 2 - 1) / 2

def radialJet (x r r₁ r₂ : ℝ) : ℝ := p x * r₂ + 2 * x * r₁ - 6 * r
def fluxJet (x r r₁ : ℝ) : ℝ := p x * (legendreP x * r₁ - 3 * x * r)

theorem p_hasDerivAt (x : ℝ) : HasDerivAt p (2 * x) x := by
  convert ((hasDerivAt_id x).pow 2).sub_const 1 using 1; simp [p]

theorem legendreP_hasDerivAt (x : ℝ) : HasDerivAt legendreP (3 * x) x := by
  convert ((((hasDerivAt_id x).pow 2).const_mul 3).sub_const 1).div_const 2 using 1
  simp only [id_eq]
  ring

/-- Lagrange identity, with the two derivative hypotheses explicit. -/
theorem flux_hasDerivAt (R R₁ : ℝ → ℝ) (x r₂ : ℝ)
    (hR : HasDerivAt R (R₁ x) x) (hR₁ : HasDerivAt R₁ r₂ x) :
    HasDerivAt (fun t => fluxJet t (R t) (R₁ t))
      (legendreP x * radialJet x (R x) (R₁ x) r₂) x := by
  convert (p_hasDerivAt x).mul
    (((legendreP_hasDerivAt x).mul hR₁).sub
      (((hasDerivAt_id x).const_mul 3).mul hR)) using 1
  dsimp [p, legendreP, radialJet]
  ring

/-- If both the ODE and primitive relation hold, the connection has derivative zero. -/
theorem connection_hasDerivAt_zero (R R₁ J : ℝ → ℝ) (x r₂ F : ℝ)
    (hR : HasDerivAt R (R₁ x) x) (hR₁ : HasDerivAt R₁ r₂ x)
    (hJ : HasDerivAt J (legendreP x * F) x)
    (hODE : radialJet x (R x) (R₁ x) r₂ = F) :
    HasDerivAt (fun t => J t - fluxJet t (R t) (R₁ t)) 0 x := by
  simpa only [hODE, sub_self] using hJ.sub (flux_hasDerivAt R R₁ x r₂ hR hR₁)

/-- A source-dependent change of primitive shifts the connection by the same amount. -/
theorem subtraction_shift (J C κ : ℝ) : (J + κ) - C = (J - C) + κ := by ring

/-- Same-source differences eliminate the primitive, irrespective of its normalization. -/
theorem same_source_difference (J C₁ C₂ : ℝ) :
    (J - C₁) - (J - C₂) = C₂ - C₁ := by ring

/-- Flux is linear in the solution and its first derivative. -/
theorem flux_linear (x r r₁ q q₁ b : ℝ) :
    fluxJet x (r + b * q) (r₁ + b * q₁) =
      fluxJet x r r₁ + b * fluxJet x q q₁ := by
  dsimp [fluxJet]
  ring

/-- Adding a mode with flux −1 shifts the connection coefficient by its amplitude. -/
theorem homogeneous_connection_shift (x r r₁ q q₁ J b : ℝ)
    (hQ : fluxJet x q q₁ = -1) :
    J - fluxJet x (r + b * q) (r₁ + b * q₁) = (J - fluxJet x r r₁) + b := by
  rw [flux_linear, hQ]
  ring

/-- Two solutions of the same sourced jet equation have a homogeneous difference. -/
theorem same_source_radial_difference (x r r₁ r₂ s s₁ s₂ F : ℝ)
    (hR : radialJet x r r₁ r₂ = F) (hS : radialJet x s s₁ s₂ = F) :
    radialJet x (r - s) (r₁ - s₁) (r₂ - s₂) = 0 := by
  calc
    radialJet x (r - s) (r₁ - s₁) (r₂ - s₂) =
        radialJet x r r₁ r₂ - radialJet x s s₁ s₂ := by dsimp [radialJet]; ring
    _ = 0 := by rw [hR, hS]; ring

theorem horizon_coefficient_arithmetic :
    (-30316 : ℚ) / 218295 + 13 * (1088 / 218295) = -16172 / 218295 := by norm_num

end KerrRadial
