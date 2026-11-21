# Literature scope and source-version audit

Checked 13 November 2026 (America/Los_Angeles). This is a bounded audit of the
foundation and nearby literature, not an exhaustive priority search. The
candidate aligned mixed quadrupole--hexadecapole spin-squared channel remains
unresolved in this repository. Its novelty is **not established**.

The foundation audit below is historical. The [20 November update](#20-november-2026-channel-audit)
adds a recent competing result and more focused matching references.

## Sources checked

| Source and version | What was inspected | Relevance and limits |
|---|---|---|
| Gounis, Kehagias and Riotto, [JCAP 03 (2025) 002](https://doi.org/10.1088/1475-7516/2025/03/002), published 4 March 2025 | Published PDF, especially Eqs. (2.11), (5.7)--(5.18), (5.26), (6.7), and the paragraph after (5.18); compared with arXiv:2412.08249v1. | The quadrupolar singular-seed argument is prior work. The published paper already discusses simultaneous growing and decaying quadrupoles. This is not the same question as a separately normalized, mixed applied ell=2 and ell=4 response matched at quadratic spin order. The present reconstruction does not prove their equivalence or inequivalence. |
| Combaluzier-Szteinsznaider, Hui, Santoni, Solomon and Wong, [JHEP 03 (2025) 124](https://doi.org/10.1007/JHEP03(2025)124), published 18 March 2025 | Published article and PDF, especially section 4.3 and the discussion of operator degeneracy; appendix D identifies tensor-basis issues. | Establishes an infinite subset of nonlinear static parity-even Schwarzschild response couplings through Weyl/EFT matching. The paper explains when axisymmetric data do not determine every coupling. It is a foundation, not an uncomputed result to claim here. |
| Iteanu, Riva, Santoni, Savic and Vernizzi, [JHEP 02 (2025) 174](https://doi.org/10.1007/JHEP02(2025)174), published 26 February 2025 | Published article and PDF, particularly sections 5.3 and 6.2. | Quadratic Schwarzschild response is treated with even and odd perturbations and matching across multipoles. The zero-spin limit of the proposed quadratic channel is therefore not a prospective discovery. A Kerr extension still needs spin-dependent structures and matching. |
| Rodriguez, Santoni and Solomon, [arXiv:2604.08653v1](https://arxiv.org/html/2604.08653v1), 9 April 2026 | Version history and sections 2.2.4 and 6.3.2. | An invited-review preprint. Section 6.3.2 distinguishes the quadrupolar Kerr tail result from a full all-multipole stationary axisymmetric Kerr computation with EFT matching, which it describes as unfinished. This is a dated scope assessment, not proof that our particular channel is unpublished. No journal publication is verified here. |
| Gralla, [CQG 35 (2018) 085002](https://doi.org/10.1088/1361-6382/aab186); [arXiv:1710.11096v3](https://arxiv.org/html/1710.11096v3), 6 March 2018 | Author version marked as matching publication; sections 2--3. | Demonstrates why reading a decaying metric coefficient without specifying coordinates and response conventions is insufficient. Its historical statements about waveform knowledge are not adopted as current facts. |
| Parra-Martinez and Podo, [arXiv:2510.20694v2](https://arxiv.org/html/2510.20694v2), 19 November 2025 | Version history, introduction, symmetry and EFT argument. | A broader nonlinear Schwarzschild vanishing argument, including electric and magnetic tides. The introduction explicitly leaves spinning black holes for future work. This extends the nonrotating foundation; it does not by itself settle the proposed Kerr sector. Cited here as a preprint. |

Names with accents and full bibliographic details are preserved in
[references.bib](../references.bib). The machine-readable source register is
[provenance/sources.json](../provenance/sources.json).

## Published Kerr version and formula audit

The [University of Geneva published PDF](https://access.archive-ouverte.unige.ch/access/metadata/6f750ab1-3a83-4f83-b11c-4d26903dce33/download)
was retrieved again. Its SHA-256 remains
`58d49474ca3438ce77fa3c9dc87002cb930c48710bbccfb246bebb3df65cd1d6`.
PDF pages 7, 13, 14, 15 and 18 were rendered and visually inspected; these are
printed pages 4, 10, 11, 12 and 15. In particular, printed page 12 contains the
simultaneous-amplitude paragraph. In arXiv v1, the corresponding pure-decaying
argument is followed directly by the growing-mode subsection.

The [baseline](../results/baseline.json) checks a normalization residual and a
counterexample to the stated arbitrary-holomorphic prescription. The
[curvature record](../results/mixed-horizon.json) checks the static-potential
sign mismatch and a divergent mixed derivative. These are specific formula and
limit checks. They neither refute the paper's physical conclusion nor supply
the missing global solution and matching. The controlled asymptotic argument
uses dominance of the leading divergence, not boundedness of every mixed term.

## Nearby results screened

- Pani et al., [Tidal deformations of a spinning compact object](https://arxiv.org/abs/1503.07365), PRD 92 (2015) 024010: the primary abstract describes linear tidal response through second order in spin. Spin order and order in applied tides are distinct. This is relevant prior work for a future linear-field construction.
- Bhatt, Chakraborty and Bose, [Response of a Kerr black hole to a generic tidal perturbation](https://doi.org/10.1103/ftwb-vvnl), PRD 112 (2025) 084065: the publisher abstract was screened for static/dynamical and spin scope. A generic-perturbation title alone does not establish the mixed nonlinear calculation requested here; a full channel audit should examine the derivation.
- Kumar, [Highest-weight truncation, graded EFT structure, and renormalization of black hole Love numbers](https://doi.org/10.1007/JHEP05(2026)294), published 26 May 2026: the publisher abstract was screened. It discusses scalar and Schwarzschild Regge--Wheeler/Zerilli truncation and low-frequency structure. Its derivation was not reproduced and is not imported as a mixed Kerr theorem.

## Search scope and remaining novelty work

Searches included `nonlinear Love numbers Kerr black holes`,
`quadratic tidal response Kerr hexadecapole`, `Kerr nonlinear matching Love 2026`,
`Kerr hexadecapole quadrupole tidal response`, and a dated search for
`Kerr nonlinear Love` after 9 April and before 14 November 2026. Searches included
arXiv and journal sites, and references in the 2026 review were followed. Some
exact-phrase searches returned no relevant results; this is not affirmative
evidence of absence. Search indexing and terminology are incomplete.

Before making a priority claim, define the actual spin-dependent operator
combination and compare its normalization, symmetry restrictions, perturbative
order, and matching prescription with the relevant full papers and later
versions. The supported conclusion now is that the proposed calculation is
motivated and has not been carried out here; no discovery claim is made.

## 20 November 2026 channel audit

The [response-definition note](response-definition.md) now fixes the algebraic
projection under examination. The following primary-source sections were read:

| Source | Inspection and implication |
|---|---|
| [Combaluzier-Szteinsznaider et al., arXiv:2410.10952v2](https://arxiv.org/html/2410.10952v2), sections 4.1--4.2 and appendix D | Axisymmetric matching determines combinations of operators, not necessarily all their coefficients. This motivates the aligned rank-one projection; no new general identifiability principle is claimed. |
| [Saketh, Zhou and Ivanov, arXiv:2307.10391v2](https://arxiv.org/html/2307.10391v2), sections 2, 5 and 7 | The tidal-amplitude expansion is linear, with quadratic-curvature worldline terms. Their all-spin dynamical matching and quadrupole--octupole mixing do not compute our cubic-action electric 224 sector. |

[Bucciotti, arXiv:2611.25059v1](https://arxiv.org/html/2611.25059v1), submitted
18 November 2026, reports a nonzero non-axisymmetric octupolar response at cubic
tidal order for Schwarzschild, using EFT matching. Sections on setup, matching
and discussion were inspected. Its axisymmetric combination still vanishes.
This challenges the broader all-orders argument of Parra-Martinez and Podo;
it does not settle our aligned quadratic-tide Kerr sector. It is an unreviewed
preprint whose calculation has not been reproduced here. Cubic **response**
uses quartic tidal operators; our cubic operators produce quadratic response.

The search included `Kerr nonlinear Love numbers spin squared quadrupole
hexadecapole matching`, `Kerr quadratic Love`, `nonlinear Kerr Love numbers
matching`, cubic tidal-operator queries, and dated nonlinear Love searches
through 20 November. No exact matching calculation for our proposed channel
was located. Optical-Kerr search noise and alternate operator conventions
limit that finding; it is not a novelty certification. The April review is a
dated scope assessment and predates the new preprint.
