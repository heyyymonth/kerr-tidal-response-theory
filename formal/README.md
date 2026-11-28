# Lean verification of the radial equation

This package checks a small part of the quadrupolar radial calculation in Lean.
It proves identities for real functions, including their analytic derivatives.
The source is stated independently of the proposed solution.

The statements use

```math
p(x)=x^2-1,\qquad P_2(x)=\frac{3x^2-1}{2},
```

```math
L_2R=pR''+2xR'-6R,\qquad
C[R]=p(P_2R'-3xR).
```

The rational functions `solution2`, `source2`, and `primitive2` are the recorded
$R_2,F_2,J_2$ from [`results/radial-response.json`](../results/radial-response.json),
written with polynomial numerators and denominators. Their scientific derivation
is in [`docs/radial-response.md`](../docs/radial-response.md) and
[`verify_radial_response.py`](../verify_radial_response.py). The separate
[`verify_formal_transcription.py`](../verify_formal_transcription.py) checks the
transcription against that saved record using exact symbolic equality. This
bridge is a computational check; Lean proves the statements about the formulas
written in this package.

## Proved statements

All theorem names below are in the `KerrRadial` namespace.

| Theorem | Statement and assumptions |
|---|---|
| `flux_hasDerivAt` | $C[R]'=P_2L_2R$, given explicit first and second derivative hypotheses at the point. |
| `connection_hasDerivAt_zero` | $(J-C[R])'=0$ if $L_2R=F$ and $J'=P_2F$. This theorem states a derivative at a point, not a global boundary-value uniqueness result. |
| `same_source_radial_difference` | The difference of two solutions with the same source satisfies the homogeneous radial equation. |
| `homogeneous_connection_shift` | Adding a mode with flux $-1$ shifts $J-C[R]$ by its amplitude. The flux normalization is a hypothesis; the logarithmic Legendre solution is not formalized here. |
| `subtraction_shift`, `same_source_difference` | An additive change to $J$ shifts the connection by that amount, while differences with the same $J$ cancel it. |
| `primitive2_hasDerivAt` | The recorded $J_2$ satisfies $J_2'=P_2F_2$. |
| `solution2_ode` | The recorded $R_2$ satisfies $pR_2''+2xR_2'-6R_2=F_2$, with ordinary analytic derivatives. |
| `connection2_identity` | $J_2-C[R_2]=-16172/218295$ in the recorded primitive convention. |
| `horizon_coefficient_arithmetic` | The exact arithmetic $-30316/218295+13(1088/218295)=-16172/218295$. This alone does not prove a horizon expansion. |

The three rational-function statements require $x-1\ne0$ and $x+1\ne0$.
They therefore apply throughout the exterior interval $x>1$, but do not assert
regularity at the horizon $x=1$. Supporting lemmas prove the quotient rule,
denominator conditions, polynomial identities, and correspondence between the
fraction derivative and Lean's analytic `deriv`.

## Reproduce

Install Lean through the official [Lean community setup guide](https://leanprover-community.github.io/install/project.html).
From this directory, run:

```sh
lake exe cache get
lake build
lake env lean CheckAxioms.lean
```

[`lean-toolchain`](lean-toolchain) pins Lean 4.19.0.
[`lakefile.toml`](lakefile.toml) selects
[Mathlib v4.19.0](https://github.com/leanprover-community/mathlib4/releases/tag/v4.19.0);
[`lake-manifest.json`](lake-manifest.json) pins Mathlib to
`c44e0c8ee63ca166450922a373c7409c5d26b00b` and records every transitive dependency.
Keep the manifest when reproducing the build. The cache is a build convenience;
it does not supply extra proof assumptions.

The local validation used an isolated Elan installation in the ignored
`.tools/elan/` directory. With that installation, prefix each command with
`ELAN_HOME="$PWD/.tools/elan"` and use `.tools/elan/bin/lake` instead of `lake`.
On the validation machine, macOS could not load Mathlib's compiled cache helper.
After `lake build cache`, the interpreter provided the same cache operation:

```sh
lake env lean --run .lake/packages/mathlib/Cache/Main.lean get \
  Mathlib.Analysis.Calculus.Deriv.Polynomial \
  Mathlib.Analysis.Calculus.Deriv.Inv \
  Mathlib.Tactic.FieldSimp Mathlib.Tactic.Ring Mathlib.Tactic.NormNum
```

## Trust and limits

`CheckAxioms.lean` inspects every theorem in the project namespace. It fails if a
project axiom is declared or a theorem depends on any axiom beyond `propext`,
`Classical.choice`, and `Quot.sound`, the standard foundations used here. The
saved [`axiom-audit.txt`](axiom-audit.txt) records the dependency report. The audit also rejected temporary controls containing a custom axiom or an
admitted proof. Its report covers 73 declarations, including 22 explicitly
written theorems and Lean-generated supporting theorems. The
proofs contain no admitted steps, custom axioms, or native decision oracle.
Tactics produce proof terms checked by Lean's kernel; the axiom audit is a
separate diagnostic program.

This package does not formalize the reduction from the Einstein or Ernst
equations, the angular projection, tensor reconstruction, horizon admissibility,
asymptotic matching, or an invariant response definition. It does not prove the
vanishing conjecture or establish a physical Love coefficient. In particular,
the nonzero connection above belongs to an explicitly chosen subtraction
convention. Checking the identity cannot make that convention canonical. The zero finite
part assigned to the recorded primitive and uniqueness of that normalization
have not been formalized.

The next mathematical obligations are to state the admissible tensor fields and
coordinate equivalences, justify the reduced equation for that space, and
specify the asymptotic normalization. Those choices determine which theorem
would answer the research question. A proof assistant can check their
consequences once they are stated; it cannot choose them on scientific grounds.
