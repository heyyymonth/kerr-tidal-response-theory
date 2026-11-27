# What we are trying to prove, and how we reached the question

Venkata Hemanth Athota · Research and learning context · 13 November 2026

This record preserves the scientific question, earlier work, reasons for narrowing the approach, and the limits of the current evidence. It accompanies the technical [starting equations](README.md) and [horizon-curvature calculation](mixed-horizon.md). It is a learning and continuity record, not a manuscript or a claim of a completed new theorem.

**Current direction, 24 November 2026:** the user explicitly prioritized a
mathematical problem with physical interpretation. The immediate deliverables
are constructions, boundary conditions, and proofs; physical EFT matching is a
later interpretation task rather than a prerequisite for every mathematical
result. [The linear-construction note](docs/linear-construction.md) now supplies
six Ernst functions through spin squared, a local metric extension argument,
and restricted uniqueness for fully specified boundary data. Those data contain
spin-linked odd growing modes. [The mixed construction](docs/mixed-construction.md)
now supplies their regular driven interaction through spin squared, its complete
boundary data, and a restricted uniqueness proof. The [radial note](docs/radial-response.md)
then defines a source-only finite-part connection coefficient, giving zero at
spin zero and -16172/218295 at spin squared. Its 45 checks bring the collection
to 262 checks/components. A source-and-horizon derivation agrees with direct
evaluation, while alternative subtractions change the value. No preferred
invariant response or physical Love coefficient is identified. Next determine
what additional structure could justify an absolute normalization, or formulate
the result using subtraction-invariant differences. This family has not been
identified with the original pure-electric physical conjecture. The historical
discussion below retains the earlier stages.

**Continuation, 20 November 2026:** [The response-definition note](docs/response-definition.md)
now resolves the three-scalar algebraic sector and the single combination
accessible in alignment, with 33 exact checks and a harmonic-coordinate
calibration. The physical source map, full EFT reduction and matching remain
open. Statements below about an undefined combination describe the earlier
checkpoint. Consult the updated [claims](CLAIMS.md) and [literature audit](docs/literature-audit.md)
before continuing; no physical Kerr response has been computed.

## The question in ordinary language

A distant companion or other external matter produces a gravitational field that varies across the black hole's neighborhood. That variation is a tidal field. We want to understand the black hole's independently identifiable conservative response when different components of the applied tide interact and the black hole rotates.

The candidate conjecture is that, in a carefully specified perturbative setting, the independent response combination is exactly zero once the horizon and axis are regular and the external field is correctly matched. A zero response coefficient would not mean that the horizon or surrounding spacetime has no tidal deformation. The external field and its nonlinear gravitational interactions can deform the geometry even when this additional response coefficient vanishes.

The provisional first setting is four-dimensional vacuum general relativity near a subextremal rotating black hole, with stationary, axisymmetric electric-type quadrupole and hexadecapole tidal fields aligned with its spin axis. We are considering their mixed contribution to a mass-quadrupole response, including the term quadratic in the dimensionless spin. In the existing notation its order is $\eta_2\eta_4\chi^2$, where $\chi=J/M^2$ in geometric units. This identifies a possible sector, not a fully defined physical coefficient or a verified novelty claim.

The response definition, independent tensor structures, regular boundary conditions, and matching conventions still have to be fixed. An aligned calculation may constrain a combination of coefficients rather than every coefficient separately. We must determine what this setting actually identifies before formulating a final theorem.

## How the scientific question developed

| Stage | Question or motivation | What carries forward |
|---|---|---|
| Gravitational-wave source origins | How are black-hole binaries assembled, and which remnants can merge again? | The motivation to understand black-hole remnants through classical gravitational physics. Quantum effects were excluded by the user's chosen scope. |
| Retention, return, and companion access | Does a retained remnant remain available for further encounters? | Retention alone does not determine time spent in a dense region or the acquisition of another companion. These are separate physical steps. |
| Idealized cluster calculations | What do simple trajectories reveal about return and exposure? | Useful controls under explicit assumptions. A universal Plummer environment, a forced central launch, and permanent rest after return cannot stand in for every actual host or trajectory. |
| Observed clusters and consistent transport | Can host gravity, species distributions, encounters, and exposure be connected consistently? | The existing cluster repository preserves six conditional reference hosts, source provenance, collisionless controls, local scattering calculations, and transport tests. |
| Response accuracy | When can diffusion predict residence under finite gravitational encounters? | The question depends on the occupation observable, encounter distribution, stopping rules, and numerical uncertainty. Several executed tests remain inconclusive at their declared tolerances. |
| Proof-centered theoretical work | Can we establish an exact statement about a black hole's intrinsic response? | The present investigation of nonlinear Kerr tidal response, with existing analytical results as controls. |

The transition to Kerr tidal response was a choice to pursue the user's interest in proof-centered theory. It was not a deduction that the cluster work was false. The two projects address different physical questions, and their evidence cannot be substituted for one another.

## What the cluster work does and does not tell us

The current [cluster repository overview](https://github.com/heyyymonth/black-hole-recoil-dynamics/blob/96f93a706f55f2c4f5d4fd1c734157553dc022a7/README.md) and [transport hypothesis](https://github.com/heyyymonth/black-hole-recoil-dynamics/blob/96f93a706f55f2c4f5d4fd1c734157553dc022a7/docs/transport-hypothesis.md) describe completed conditional calculations and executed response experiments. Their contents were checked when preparing this record; older progress notes that describe the encounter implementation as wholly unfinished are superseded on that point.

The stopped-generator occupation identity is a mathematical relation subject to its stated assumptions. The separate prediction under test approximates the full encounter-process expectation using a diffusion-process first-response calculation, then extrapolates to finite changes. Those are different statements.

Improved sampling reduced estimated uncertainty in that predictor, but the declared endpoint accuracy remained unresolved. Rare contributions, numerical refinement, continuation of stopped paths, and physical calibration require distinct controls. An inconclusive test is not a falsification, and increasing sample count alone does not settle every kind of uncertainty.

None of these cluster results determines a strong-field tidal response coefficient for Kerr. They remain relevant to environmental transport and possible later interaction models. No cluster paper, result, or source dataset is deleted or relabeled by the present analytical work.

## Which arguments we set aside, and why

“Set aside” has several meanings here. Some ideas address a different question; some are established results rather than prospective discoveries; some are insufficient arguments; and a few printed formulas fail direct checks.

| Argument or approach | Reason it cannot establish the present conjecture | Retained value |
|---|---|---|
| More permutations of cluster experiments | They concern transport and residence, not the intrinsic Kerr tidal boundary-value problem. | Conditional transport evidence and methods for controlling numerical uncertainty. |
| Re-proving the nonrotating response results | Relevant Schwarzschild results already exist in the literature cited in README. | Exact backgrounds and limits against which a rotation-dependent result must be checked. |
| Treating a singular decaying seed as the whole nonlinear response | The nonlinear equation has a source produced by interacting applied fields. Excluding one homogeneous branch does not determine the regular driven solution. | A necessary regularity check within the family examined. |
| Assuming all terms containing the applied amplitude remain finite near the horizon | Pointwise amplitude analyticity does not imply a uniform horizon limit. The static mixed-field calculation supplies divergent mixed contributions. | The leading divergence can still dominate; that is the argument reconstructed in the horizon note. |
| Using arbitrary real parts of holomorphic functions as axisymmetric harmonic seeds | The two-dimensional Laplacian differs from the three-dimensional axisymmetric Laplacian. The example $\rho^2-z^2$ distinguishes them. | Correctly separated harmonic seeds and checked identities remain available. |
| Importing every printed equation unchanged | Background substitution exposes an Ernst normalization issue; a static limit exposes a sign inconsistency in a printed metric potential. | The equations are independently normalized and checked. These issues do not by themselves refute the paper's physical conclusion. |
| Claiming simultaneous growing and decaying quadrupoles were omitted in the existing paper | The published version includes that discussion; arXiv v1 omits it. | Published-version provenance prevents a false novelty claim. |
| Applying isolated-black-hole uniqueness directly | A black hole in a prescribed external tidal field has different boundary conditions. | Regularity remains essential, but the tidal boundary-value problem must be solved on its own terms. |
| Claiming an all-orders, all-multipoles theorem from one aligned channel | Such a calculation has restricted angular information and perturbative order. | It could establish an identifiable response combination in a precisely stated sector. |

These are reasons to refine the argument, not reasons to discard every earlier calculation.

## What we have actually established in the Kerr investigation

The local working files contain:

1. A normalized Ernst equation checked against Schwarzschild and Kerr backgrounds.
2. A reconstruction of the known static seed regularity argument for finite separated multipole sums.
3. The mixed nonlinear Ernst source equation, derived without solving the tidal boundary-value problem.
4. An independent stationary-frame curvature contraction and an exact static mixed-quadrupole limit.
5. A conditional rotating asymptotic argument within a specified reflection-symmetric vacuum solution family.

For the last calculation, with fixed decaying Weyl-spherical quadrupole amplitude $d\ne0$, finite applied amplitude $c$, and the stated nonzero Kerr-seed parameter, the dimensionless curvature obeys

$$
\lim_{r\to0^+}r^6\log\mathcal K=\frac32d^2>0.
$$

Here $r$ is the dimensionless equatorial Weyl radius. The result controls the leading logarithmic divergence. It does not reproduce the full published curvature prefactor or establish a global event-horizon classification. Static and rotating branches need not share subleading factors. The limits in tidal amplitude, spin, and distance from the background horizon are not interchangeable without further justification.

The saved baseline and curvature records report 32 and 18 symbolic checks respectively; the curvature calculation also checks 16 vacuum Ricci components. Their stored script hashes were confirmed to match the current scripts when this record was written. These are checks of the declared algebra and controls, not experimental observations or a computed nonlinear Love coefficient.

This work reconstructs an existing local obstruction and clarifies its assumptions. No new matched tidal-response coefficient or general Kerr Love theorem has been obtained.

## The unresolved proof step

Schematically, the mixed equation has the form

$$
\mathcal L_0\mathcal E_{AB}=S[\mathcal E_A,\mathcal E_B].
$$

The left side describes a perturbation about Kerr; the right side is the source generated by the interaction of the two applied fields. A formal solution consists of a driven particular solution plus homogeneous solutions. Removing a singular homogeneous contribution does not identify the physical content of the remaining solution.

We therefore need to fix the allowed response structures and conventions, solve with regular boundary conditions, and match to the external-field description. Matching means identifying which part of the solution is already fixed by the applied tide and background parameters, and which part would represent an additional response of the black hole.

A successful result could be a vanishing proof for an identifiable response combination throughout the stated sector, or a regular, consistently matched nonzero counterexample. A zero found at one perturbative order is not an all-orders theorem. A nonzero coordinate coefficient alone is not a physical counterexample. Novelty remains subject to a focused literature audit of the chosen channel.

## Learning checkpoint

The user is currently asking to understand the problem before advancing the calculation. Resume with one concept at a time:

1. What a tidal field is and how it differs from a uniform gravitational acceleration.
2. What “applied field,” “deformed geometry,” and “independent response” mean.
3. Why rotation and nonlinear interactions introduce the mixed problem.
4. Why a regular horizon is a physical boundary condition.
5. Why removing a singular solution does not finish the proof.
6. How matching turns a mathematical coefficient into a physical statement.

The candidate conjecture is a target to investigate, not a conclusion to defend. Keep the original cluster question, the verified analytical reconstruction, and the unresolved matching question distinct while learning.

## Locations and continuity

- [Cluster project](https://github.com/heyyymonth/black-hole-recoil-dynamics/blob/96f93a706f55f2c4f5d4fd1c734157553dc022a7/README.md): original environmental-transport work and manuscript; unchanged by this learning checkpoint.
- [Kerr starting equations and references](README.md): literature versions, mathematical conventions, and candidate mixed sector.
- [Controlled horizon calculation](mixed-horizon.md): derivation, assumptions, and scope of the curvature obstruction.
- [Baseline record](results/baseline.json) and [curvature record](results/mixed-horizon.json): exact checks and their declared limitations.

The Kerr notes are analytical working material in the separate Kerr Tidal Response Theory research collection. The cluster repository and its unreviewed manuscript remain unchanged. This is not a journal publication or a priority claim. See [provenance](PROVENANCE.md) for the preserved starting checkpoint and [the next lesson](docs/regularity-and-matching.md) for the unresolved matching step.
