# What the verification establishes

The equations are checked in two ways: symbolic substitution into the stated
field equations, and Lean proofs of selected radial statements. Neither method
can decide whether a mathematical definition is the most useful one for the
research question. That requires checking the assumptions, the encoding of the
problem and the interpretation of the result.

## Evidence by claim

| Claim | Verification | What remains outside it |
|---|---|---|
| The first and mixed Ernst variations have the stated sources. | Exact arbitrary-function and explicit-field substitutions in the [baseline](../verify_baseline.py) and [mixed](../verify_mixed_solution.py) scripts. | Derivation of the stationary vacuum reduction from the full Einstein equations is taken from the cited theory. |
| The constructed linear and mixed fields satisfy their equations through spin squared. | Full rational PDE residuals vanish, not just sampled values. | Higher spin orders, arbitrary applied data and a pure-electric physical source map. |
| Metric expressions have the required algebraic cancellations. | Exact block, horizon and axis identities. | Joint smoothness in horizon–axis corner charts and the complete analytic extension argument. |
| Solutions are unique for the complete prescribed data in the finite angular class. | Handwritten homogeneous-kernel and difference argument, with representative symbolic checks. | A formal all-mode kernel proof; convergence and uniqueness for infinite expansions. |
| The radial primitive is determined from the source without using the unknown spin-squared field. | The source uses the linear fields and lower mixed orders; its partial fractions construct the primitive directly. | A general existence theorem for source classes beyond the one studied. |
| The declared radial connection has the stated rational value. | Direct evaluation agrees with the source-and-horizon derivation; selected identities are also checked in [Lean](../formal/README.md). | A preferred subtraction, or an independently matched physical Love coefficient. |
| Expected evidence can be reproduced. | Complete JSON and hash comparison with pinned Python packages. | Correctness of every premise or interpretation. Reproduction alone is not a proof. |

The 16 Ricci-component checks impose local vacuum relations before contraction.
They check the frame calculation's consistency, not the full distorted metric
against the vacuum equations from scratch. Two nonzero-spin Kerr curvature
samples are implementation controls. Boundary decompositions and bookkeeping
checks also contribute to the recorded total; the total is not a count of
independent theorems.

## Lean coverage and trust

[formal/README.md](../formal/README.md) maps the compiled theorem names to the
radial note, lists the toolchain and dependencies, and gives the build and axiom
audit commands. The formal files state their own definitions, derivative
hypotheses and domain restrictions. In particular, the rational source must be
written independently of the proposed solution: defining it to be the result of
applying the differential operator would make a purported solution check
circular.

[verify_formal_transcription.py](../verify_formal_transcription.py) compares the
three explicit Lean rational functions with the saved radial source, solution
and primitive by exact symbolic equality. CI first reproduces that record and
then checks the transcription. This connects the two representations without
making the symbolic system part of Lean's proof kernel.

Lean constructs a proof term and checks it with its kernel. Its
[proof-validation documentation](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
explains the distinction between checking a proof and checking that its statement
encodes the intended mathematics. This project excludes unfinished proofs,
custom axioms and native-evaluation shortcuts from its formal statements; the
axiom audit makes the remaining foundational dependencies visible.

The formal layer is deliberately limited. It does not yet include the Ernst
reduction, the distorted-Kerr vacuum family, metric regularity, completeness of
the homogeneous kernel, asymptotic existence or physical matching. The rational
radial identities can be proved while one of those larger premises remains
unformalized. Review [CLAIMS.md](../CLAIMS.md) alongside any build result.

## What would strengthen the argument next

The current mathematical result is that a source subtraction is needed and that
the stated calibration conditions leave freedom in it. Further decimal accuracy
in the resulting coefficient would not resolve that freedom.

A useful next theorem would specify a space of sources and admissible reference
maps, then classify the additive source functionals that preserve the chosen
calibrations. It should identify any quantities unchanged by that freedom.
Alternatively, an additional mathematical normalization could select a
reference, with its consequences stated explicitly. Physical matching is a
possible later selection principle, not a prerequisite for this mathematical
classification.

For the construction itself, the next proof obligations are the full
homogeneous-kernel classification under the stated horizon assumptions and an
explicit smoothness argument at the horizon–axis corners. Formalizing these
would extend verification beyond rational identities. The current results do
not decide the original vanishing conjecture.

## Reproduce and review

Run the Python instructions in the [README](../README.md) and the separate
[Lean instructions](../formal/README.md). The original scientific JSON records
are preserved. Historical scope statements inside them refer to the individual
calculation; the current claim table accounts for later results.

When adding a proof, review four things: the equation being encoded, every
hypothesis, the proof's actual dependencies, and the inference made from it in
the prose. A successful build addresses the third item; it does not remove the
other three.
