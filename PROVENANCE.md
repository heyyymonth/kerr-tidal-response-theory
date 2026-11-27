# Provenance and reproduction

## Inherited foundation

The starting directory held nine research files and had no Git history. All nine
were read and the two calculations were rerun in a newly created Python 3.11.1
environment before the first commit. The complete fresh results matched the
saved records, including their script hashes: 32 baseline checks, 18 curvature
checks, and 16 vacuum Ricci components. No expected result was rewritten.

The original nine files are preserved byte for byte in
[commit af774499c43b306a41612c37d629a2e41768ca43](https://github.com/heyyymonth/kerr-tidal-response-theory/commit/af774499c43b306a41612c37d629a2e41768ca43).
[provenance/import.json](provenance/import.json) records their SHA-256 hashes.
The original handoff describes its own pre-repository checkpoint. Later Git
commits record publication edits and the user's chosen public name,
**Kerr Tidal Response Theory** (`kerr-tidal-response-theory`). The local directory
retains its original name so existing local handoff paths continue to work.

The historical context was read from the sibling project at
[96f93a706f55f2c4f5d4fd1c734157553dc022a7](https://github.com/heyyymonth/black-hole-recoil-dynamics/tree/96f93a706f55f2c4f5d4fd1c734157553dc022a7),
verified to exist on GitHub. Its README, transport hypothesis, author and
contribution conventions, and manuscript README were consulted read-only. Public
cross-project links use this revision. No sibling calculation, manuscript, or
synced parent `sources/` file was modified or imported as Kerr evidence.

## Scientific evidence and execution records

| File | Role |
|---|---|
| [verify_baseline.py](verify_baseline.py) | Original exact Ernst, Legendre, variation, and angular checks. |
| [verify_mixed_horizon.py](verify_mixed_horizon.py) | Original reflected vacuum frame contraction, curvature controls, and static limits. |
| [baseline.json](results/baseline.json), [mixed-horizon.json](results/mixed-horizon.json) | Inherited deterministic scientific records; retained unchanged at publication. |
| [verify_response_basis.py](verify_response_basis.py), [response-basis.json](results/response-basis.json) | 20 November continuation: 33 exact STF, response-normalization and harmonic-coordinate checks; no physical coefficient value. |
| [verify_linear_drivers.py](verify_linear_drivers.py), [linear-drivers.json](results/linear-drivers.json) | 22 November continuation: 82 exact linear recursion, metric identity, boundary normalization and kernel checks. |
| [verify_mixed_solution.py](verify_mixed_solution.py), [mixed-solution.json](results/mixed-solution.json) | 23 November continuation: 36 exact mixed-map, forced-equation, angular, boundary and regularity-identity checks. |
| [verify_radial_response.py](verify_radial_response.py), [radial-response.json](results/radial-response.json) | 24 November continuation: 45 exact radial, primitive, horizon, Frobenius and subtraction-convention checks. |
| [verify_reproduction.py](verify_reproduction.py) | Read-only comparison of all six fresh complete outputs, pinned package versions, and script/result hashes; also checks local Markdown file targets. |
| [reproduction.json](results/reproduction.json) | Fresh execution receipt with actual time, interpreter, platform, package versions, input hashes, and comparisons. |

Run with Python 3.11:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/python verify_reproduction.py
```

The default command never writes results. To retain a new execution receipt,
use `--report tmp/reproduction.json`. This option cannot target any expected
scientific record. The calculation scripts' `--write` options deliberately
regenerate expected records and should be used only for a reviewed scientific
change, as described in [CONTRIBUTING.md](CONTRIBUTING.md).

The CI workflow installs the same pinned SymPy and mpmath versions in a fresh
Python 3.11 environment, checks dependencies, reruns all six calculations, checks
local file links, and uploads its execution receipt. Actions are pinned to
verified commit SHAs. The receipt records the actual Python patch version;
the entire operating system and Python build are not frozen. Dependency pins
support reproducibility and are not a claim that those releases are the newest.

Publication validation also confirmed, in a temporary copy, that a changed expected result, a changed calculation script, and an attempt to overwrite an expected record with an execution receipt are rejected.

CI reports numerical/algebraic execution status. It does not review the
conditional asymptotic proof, validate global boundary conditions, or perform
EFT matching. The 16 Ricci components are checked after imposing the declared
local vacuum relations; they do not establish an arbitrary full metric as vacuum.

## Response-definition continuation

On 20 November 2026, the declared parity-even electric 224 spin-squared algebraic
sector was reconstructed by an SO(3) multiplicity count and three independent
Cartesian contractions. Exact aligned weights, two invisible coefficient
directions, the STF functional derivative and a prolate-to-solid-harmonic
calibration were checked. A separate review independently confirmed the
formulas and all 33 new checks. This review used AI assistance as disclosed in
[AUTHORS.md](AUTHORS.md); it is not scientific peer review.

The new [definition note](docs/response-definition.md) records the conditional
normalization and remaining matching prescription. Its algebraic completeness
does not establish a full on-shell EFT basis, physical source map or a Kerr
coefficient. The original scripts and two expected records remain unchanged.
The execution receipt is refreshed for the expanded collection; the earlier
receipt remains available in Git history. No third-party paper is distributed.

## Linear and mixed construction continuation

The 22 November [linear-construction note](docs/linear-construction.md) uses the
known distorted-Kerr metric and Ernst map with explicitly chosen seed and
parameter conventions. Two derivations of the spin coefficients agreed, and
the final script checks their differential equations directly. The metric
extension and finite-mode uniqueness arguments are stated separately from the
82 algebra checks. Review assistance is AI-assisted, not peer review. The
published Gounis Eq. (4.1) was checked in the saved published text, and
Abdolrahimi et al. arXiv:1509.01665v2 section 2 was read in primary HTML.
Its later rescaled coordinate/charge conventions are not silently imported.
No pure-electric physical source map or new Love coefficient is claimed.

On 23 November 2026, the same known family was differentiated in both even
seed amplitudes. The [mixed note](docs/mixed-construction.md) states the
resulting forced solution, full mixed exterior data, local metric extension,
and finite-mode uniqueness assumptions. All three forced equations vanish
identically under direct differential substitution. Independent AI-assisted
derivation and review agreed on the fields, spin residue, horizon values and
quadrupolar projections. The nonzero decaying coordinate terms are explicitly
distinguished from independent response. This review is not peer review.
The four older deterministic records are unchanged; the expanded reproduction
receipt covers 217 checks/components. The extra quadratic term in the exact
metric potential was checked against the primary 2015 source's ordered double
sum, including both cross terms. No third-party paper is redistributed.

## Literature and rights

The [24 November radial note](docs/radial-response.md) constructs a finite-part
primitive from source data alone, before evaluating the regular solution. Its
nonzero spin-squared connection coefficient is independently recovered from
source data and horizon smoothness. Two AI-assisted derivations agreed on
the value and subtraction ambiguity; a separate run reproduced all 45 new
checks and the complete saved output. This is not peer review. The five older
deterministic records remain unchanged, and the updated receipt covers 262
checks/components. Standard Legendre identities were checked directly, with
NIST DLMF section 14.2 as a mathematical reference. Gralla's convention analysis
provides context, not this calculation's numerical value or a current novelty
verdict. No physically matched Love coefficient is claimed.

[sources.json](provenance/sources.json) records versioned source locations,
inspection scope and available download hashes. The
[literature audit](docs/literature-audit.md) distinguishes published papers,
preprints, and abstract-only screening. The published Kerr PDF was retrieved
again and its hash matched the inherited value. Rendered pages checked the
formulas independently of text extraction. Downloaded papers and rendered pages
are temporary, ignored working references, not distributed with this repository.

Original code and documentation are available under the [MIT license](LICENSE).
Referenced papers, dependency packages and other third-party materials retain
their own rights. Mathematical reconstruction does not transfer authorship of
prior results. See [AUTHORS.md](AUTHORS.md) for personal metadata and assistance
disclosure, and [CITATION.cff](CITATION.cff) for citing this collection. No DOI,
journal publication, or peer review is claimed for this repository.
