# Kerr Tidal Response Theory: research handoff

Author: **Venkata Hemanth Athota**

Public research contact: **bharadwaj.hemanth.002@gmail.com**

Repository: [heyyymonth/kerr-tidal-response-theory](https://github.com/heyyymonth/kerr-tidal-response-theory)

This is the current continuation brief for an existing public research
repository. The pre-repository instructions and subsequent checkpoints remain
available in [the historical handoff](https://github.com/heyyymonth/kerr-tidal-response-theory/blob/c5e7faaae858c8a060da524691f33ab08d1a20b6/NEW_CHAT_HANDOFF.md)
and [historical research context](https://github.com/heyyymonth/kerr-tidal-response-theory/blob/c5e7faaae858c8a060da524691f33ab08d1a20b6/research-context.md).
Neither document is a fresh execution record or a manuscript.

## Objective and interpretation

Continue a proof-centered investigation in classical general relativity. The
user prioritizes a mathematical problem with physical interpretation:
construct solutions, state their boundary conditions and prove precisely scoped
results. Physical EFT matching is a later interpretation task, rather than a
prerequisite for every mathematical result. Explain concepts one step at a time.
Quantum effects are outside the chosen scope.

The original candidate conjecture asks whether a regular subextremal rotating
black hole has zero independently matched conservative response when stationary,
axisymmetric tidal fields interact. The first proposed physical sector is the
aligned electric quadrupole–hexadecapole contribution to a mass quadrupole,
including order $\eta_2\eta_4\chi^2$ with $\chi=J/M^2$. Investigate the answer;
do not assume vanishing. A proof with explicit assumptions and a regular,
consistently matched nonzero result are both valid outcomes. Channel-specific
novelty remains unestablished.

An independent response differs from the deformation produced by the applied
tides and their nonlinear gravitational interaction. A zero response can coexist
with a deformed horizon. A nonzero coordinate tail alone is not a physical
counterexample.

## Current results and open work

- [The Ernst note](docs/ernst-equation.md) gives the normalized stationary
  axisymmetric equation, known static seed regularity and mixed source equation.
- [The curvature note](mixed-horizon.md) reconstructs the local singular-seed
  obstruction. The static calculation is exact; the rotating limit is conditional
  on a specified reflection-symmetric local vacuum family. For fixed decaying
  Weyl-spherical amplitude $d\ne0$, finite applied amplitude $c$ and the stated
  fixed nonzero Kerr-seed parameter, it gives
  $\lim_{r\to0^+}r^6\log\mathcal K=3d^2/2$. Here $r$ and $\mathcal K$ are
  dimensionless equatorial Weyl radius and curvature. This is a leading
  logarithmic limit, with no full-prefactor, global-horizon, family-completeness
  or uniform zero-amplitude/zero-spin/extremal claim.
- [The response definition](docs/response-definition.md) derives three scalars
  in the declared algebraic electric sector and the single combination probed
  in alignment. The full EFT reduction and physical source calibration are open.
- [The linear](docs/linear-construction.md) and
  [mixed](docs/mixed-construction.md) notes construct rational fields through
  spin squared, check the forced equations, and establish local horizon/axis
  smoothness. Uniqueness is restricted to a fixed gauge, finite angular expansions
  and the complete stated exterior data, including exceptional modes. The known
  distorted-Kerr family is prior work. Its spin-linked odd growing data have not
  been transformed to the original pure-electric prescription.
- [The radial note](docs/radial-response.md) defines a connection coefficient
  through a source-only finite-part subtraction. It gives $b^{(0)}=0$ and
  $b^{(2)}=-16172/218295$, with agreement between direct extraction and a
  source-and-horizon derivation. Alternative subtractions change the coefficient
  while preserving homogeneous normalization and the static zero. This is a
  conditional mathematical value, not a preferred invariant response or a
  physical Love coefficient.

The next mathematical issue is the normalization of an absolute response:
identify additional structure that selects it, or formulate the result in terms
of subtraction-invariant differences between solutions of the same source
problem. Regularity and homogeneous calibration alone do not fix that origin.
Physical matching could supply an additional criterion, but would also require
calibrated external fields, fixed parameter and gauge conventions, a reference
prediction and a common matching region.

## Reading and verification

Start with [README](README.md), [research context](research-context.md) and
[CLAIMS.md](CLAIMS.md), then the technical note for the calculation being
continued. [Regularity and matching](docs/regularity-and-matching.md) supplies a
step-by-step explanation of the logical distinctions. Read
[PROVENANCE.md](PROVENANCE.md), the [literature audit](docs/literature-audit.md)
and [source register](provenance/sources.json) before making attribution or
novelty claims.

The six verification scripts and their saved records cover the baseline,
curvature, response basis, linear fields, mixed field and radial calculation.
[Verification](docs/verification.md) records their reproduction procedure and
limits. Dependencies are pinned in `requirements.txt`. Check actual execution
results and script hashes; a saved record or this handoff does not establish
that a later version has been run. For formal verification, consult
[formal/README.md](formal/README.md) for the exact Lean statements and coverage.
Do not describe checked algebraic lemmas as a formal proof of the whole Kerr
construction, its analytic regularity arguments or the physical conjecture.

Important source distinctions are preserved in the literature audit. Use the
published Gounis–Kehagias–Riotto paper for the simultaneous-amplitude discussion;
arXiv v1 omits it. Existing Schwarzschild results and the distorted-Kerr map are
prior work. Review preprints and titles alone do not establish novelty or supply
the missing matching calculation. Check current primary literature before any
new claim about the selected channel's status.

## Arguments and earlier work to preserve

The mixed equation is sourced by the interacting linear fields. Excluding a
singular homogeneous seed does not determine the remaining driven solution or
its independent response. Choosing the regular solution as its own reference
would force zero by definition. Neither shortcut settles the conjecture.

Pointwise amplitude analyticity does not justify a uniform horizon limit: mixed
terms can diverge, and the curvature argument uses asymptotic dominance. The
printed Ernst normalization and one static-potential sign fail direct checks;
an arbitrary-holomorphic seed prescription fails the axisymmetric Laplace
equation. These formula checks alone do not disprove the source paper's physical
conclusion. Isolated asymptotically flat uniqueness does not transfer unchanged
to prescribed external tides. A finite aligned calculation is not an all-orders,
all-multipoles theorem.

The separate [black-hole-recoil-dynamics repository](https://github.com/heyyymonth/black-hole-recoil-dynamics)
studies kicked remnants, residence and encounters in stellar clusters. Its
conditional calculations and inconclusive endpoint-accuracy tests remain valid
parts of that record; they were not falsified by the change of research topic.
The occupation identity is mathematical, while the diffusion-based first-response
predictor is a separate approximation. Increased sampling did not resolve every
refinement, rare-event, continuation or calibration uncertainty. Cluster evidence
cannot establish an intrinsic Kerr theorem. Preserve that repository and its
manuscript; do not substitute more cluster experiments or broad numerical sweeps
for the present proof problem.

## Repository and publication constraints

- Keep the public project name **Kerr Tidal Response Theory**, under the personal
  account `heyyymonth`; the repository is already established. Preserve its Git
  history and provenance. Avoid overwriting unrelated work.
- Retain the author and contact above, the credit **Contributed by Hemanth.**, and
  independent-researcher status. Do not invent an institutional affiliation or
  incorporated organization. Keep assistance attribution accurate in
  [AUTHORS.md](AUTHORS.md).
- Original code and documentation use the MIT license. Preserve third-party
  rights, source attribution and accurate citation metadata. A GitHub version is
  neither a DOI nor a peer-reviewed publication.
- Keep the structure focused on assumptions, derivations, meaningful checks,
  reproducible results and claims tied to evidence. Validate before committing
  and publishing. Never fill missing results, alter evidence to force agreement,
  or describe unrun calculations as complete.
- Preserve portable repository links. Pin cross-project historical references
  where appropriate; avoid relying on sibling paths for public documentation.
- The eventual manuscript preference is two-column APS/PRD REVTeX, with no
  watermark, standard academic typography and citations. Titles and abstracts
  must reflect supported results. Avoid experiment IDs as prose labels,
  recursive self-citations, promotional language, artificial 90-day plans and
  invented discoveries. Keep tooling details in repository documentation.
  Compile and visually inspect any manuscript; maintain source, PDF and source
  archive consistently when publishing. Do not modify the cluster manuscript to
  report this separate investigation or assert a new theorem prematurely.
- The user has requested natural, concise research prose and verifiable
  mathematics. Preserve substantive assumptions and limitations while removing
  repetitive progress language. Teach the distinction between applied field,
  changed geometry, homogeneous freedom and independent response.

The local checkout is
`/Users/sravanbharadwaj/.codex/.chatgpt-projects/g-p-6a0133858c1081919cca37ecfc2582fa/research/kerr-tidal-response`.
The cluster checkout is its sibling `black-hole-recoil-dynamics`. Files under the
parent project's `sources/` are read-only synced references: do not edit, rename,
move or delete them. If a future environment lacks the required material, report
that access gap rather than claiming a reproduction or guessing credentials.
