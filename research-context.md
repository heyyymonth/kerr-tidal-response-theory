# Research question, history and current state

Venkata Hemanth Athota

This project studies nonlinear tidal perturbations of Kerr as a mathematical
boundary-value problem, with physical interpretation alongside the proofs.
Constructions, explicit assumptions and verified identities are the immediate
results. Identifying a physical Love coefficient requires additional calibration
and matching. The detailed earlier record is preserved in
[the historical version of this file](https://github.com/heyyymonth/kerr-tidal-response-theory/blob/c5e7faaae858c8a060da524691f33ab08d1a20b6/research-context.md).

## The question

A tidal field is the spatial variation of external gravity near an object. A
quadrupole and a hexadecapole describe different angular patterns of that field.
When both act on a rotating black hole, their interaction changes the geometry.
The question is whether an additional conservative response remains after the
contribution fixed by the applied fields and background parameters is accounted
for.

The original candidate conjecture concerns four-dimensional vacuum general
relativity near a subextremal Kerr black hole, with stationary, axisymmetric,
aligned electric quadrupole and hexadecapole tides. Its first target is the mixed
mass-quadrupole response at order $\eta_2\eta_4\chi^2$, where $\chi=J/M^2$ in
geometric units. A vanishing proof and a consistently matched nonzero result are
both admissible outcomes. Neither the value nor channel-specific novelty is
established.

A zero independent response would still allow tidal deformation of the horizon
and surrounding spacetime. Conversely, a nonzero decaying term in a coordinate
expansion does not by itself identify an independent response.

## Current mathematical results

| Calculation | Result and scope |
|---|---|
| [Ernst equation and seeds](docs/ernst-equation.md) | The stationary axisymmetric vacuum equation is normalized against Schwarzschild and Kerr. The known static regularity argument applies to finite separated multipole sums. The mixed nonlinear source follows by variation. |
| [Horizon curvature](mixed-horizon.md) | An exact static calculation and a conditional rotating asymptotic argument reconstruct a singular-seed obstruction within a specified reflection-symmetric local vacuum family. |
| [Response algebra](docs/response-definition.md) | Three scalars span the declared algebraic electric sector; alignment probes one coefficient combination. The full EFT reduction and physical source map remain open. |
| [Linear fields](docs/linear-construction.md) | Six rational Ernst functions through spin squared satisfy the linear equations. Metric reconstruction gives local horizon/axis smoothness; uniqueness holds in a fixed-gauge finite-mode class with complete growing data and exceptional modes fixed. |
| [Mixed field](docs/mixed-construction.md) | The two drivers generate an explicit regular interaction through spin squared. The forced equations, mixed boundary data and restricted uniqueness argument are recorded. Its quadrupolar projection is nonzero. |
| [Radial connection coefficient](docs/radial-response.md) | A source-only finite-part subtraction gives $b^{(0)}=0$ and $b^{(2)}=-16172/218295$. A source-and-horizon derivation agrees with direct extraction. Alternative subtractions change the value while preserving homogeneous normalization and the static zero. |

The linear and mixed constructions differentiate a known distorted-Kerr family.
Their seed amplitudes are mathematical data, and their spin-linked odd growing
modes have not been converted to the original pure-electric convention. These
constructions therefore solve a specified mathematical problem without settling
the independently matched conjecture.

For the curvature calculation, fixed nonzero decaying Weyl-spherical quadrupole
amplitude $d$ and finite applied amplitude $c$ give

$$
\lim_{r\to0^+}r^6\log\mathcal K=\frac32d^2>0.
$$

Here $r$ is dimensionless equatorial Weyl radius and $\mathcal K$ is dimensionless
curvature. The rotating argument also fixes a nonzero Kerr-seed parameter and
uses the declared local vacuum family. It controls the leading logarithmic
divergence, not the full published prefactor, a global horizon classification
or completeness of the solution family. No uniform zero-amplitude, zero-spin or
extremal limit is proved.

[CLAIMS.md](CLAIMS.md) connects results to their assumptions and evidence.
[Verification](docs/verification.md) describes the executable checks and their
limits. Symbolic identities, analytic arguments and formally checked lemmas have
different scopes; no complete formal verification of the Kerr research is claimed.

## The remaining mathematical issue

The mixed equation has the form

$$
\mathcal L_0\mathcal E_{AB}=S[\mathcal E_A,\mathcal E_B].
$$

Once the two linear fields are fixed, their interaction fixes the source. A
particular solution plus homogeneous terms describes the remaining boundary
freedom. Regularity constrains their sum. It does not select an origin for a
response coefficient extracted relative to a sourced reference solution.

The radial calculation makes this ambiguity explicit. The next question is
whether some additional mathematical structure selects an absolute
normalization, or whether the invariant statement should concern differences
between solutions of the same source problem. Choosing the regular solution as
its own reference would force zero by definition. Physical matching could supply
an additional criterion, but it is a separate task involving calibrated external
fields, background parameters, a gauge map and a common subtraction convention.

## How the project developed

The earlier research studied kicked merger remnants in stellar clusters:
retention, return, residence, exposure and access to possible companions.
Idealized trajectory controls developed into conditional models for six
reference hosts, with local scattering, transport and response calculations.
The move to Kerr reflects a preference for proof-centered classical theory;
quantum effects are outside the chosen scope.

The [cluster overview](https://github.com/heyyymonth/black-hole-recoil-dynamics/blob/96f93a706f55f2c4f5d4fd1c734157553dc022a7/README.md)
and [transport hypothesis](https://github.com/heyyymonth/black-hole-recoil-dynamics/blob/96f93a706f55f2c4f5d4fd1c734157553dc022a7/docs/transport-hypothesis.md)
record completed conditional calculations and inconclusive predictive-accuracy
tests. The stopped-generator occupation identity is a mathematical relation;
the diffusion-based first-response predictor and its finite-change extrapolation
are separate approximations. Improved sampling reduced estimated uncertainty
without resolving the declared endpoint accuracy. Refinement, rare contributions,
continuation of stopped paths and physical calibration require distinct controls.

These tests were not a falsification of the cluster work. They address
environmental transport, and cannot establish an intrinsic Kerr response theorem.
The projects retain separate repositories, manuscripts and evidence.

## Arguments set aside

| Shortcut or alternative | Why it is insufficient | What remains useful |
|---|---|---|
| Further cluster experiments as evidence for the Kerr conjecture | Transport and the strong-field tidal boundary problem concern different observables and assumptions. | Conditional transport results and numerical uncertainty methods. |
| Recasting known Schwarzschild results as a discovery | Nonrotating nonlinear response calculations already exist. | Backgrounds and matching limits for a rotating calculation. |
| Equating a singular decaying seed with the entire nonlinear response | The interacting applied fields also produce a driven solution. | The singular-seed obstruction is a regularity test within its stated family. |
| Assuming all mixed terms stay finite near the horizon | Pointwise analyticity in amplitudes does not imply a uniform horizon limit; mixed contributions can diverge. | The controlled curvature argument uses dominance of the leading divergence. |
| Using arbitrary real parts of holomorphic functions as axisymmetric seeds | The two-dimensional and three-dimensional axisymmetric Laplacians differ; $\rho^2-z^2$ is a counterexample. | Correctly separated harmonic seeds. |
| Importing printed equations without checks | Background substitution exposes an Ernst normalization issue; a static limit exposes a metric-potential sign inconsistency. | Independently checked formulas; these discrepancies alone do not refute the paper's physical conclusion. |
| Claiming simultaneous applied and decaying quadrupoles were omitted | The published Gounis–Kehagias–Riotto paper contains that discussion, although arXiv v1 does not. | Published-version provenance prevents a false novelty claim. |
| Applying isolated asymptotically flat uniqueness directly | External tidal data impose different boundary conditions. | Regularity and uniqueness arguments for the actual prescribed data. |
| Reading a coordinate tail as a Love number, or defining a reference to force zero | Both skip the independent response definition and its normalization. | Explicit radial coefficients and comparisons between subtraction conventions. |
| Generalizing one aligned channel to all orders and multipoles | Alignment loses tensor information and the calculation retains finite perturbative order. | A precisely identified combination under explicit assumptions. |

The [literature audit](docs/literature-audit.md) records source versions and the
scope of each comparison. The [regularity and matching note](docs/regularity-and-matching.md)
explains the central distinctions step by step. This collection is research
working material, with no claim of a new general Kerr Love theorem or a completed
physical matching calculation.
