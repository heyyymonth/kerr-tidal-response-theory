# Provenance and reproduction

## History

The starting directory contained nine research files and had no Git history.
All nine were read and both calculations were rerun before publication. The
fresh results matched the saved records, including script hashes. The original
files are preserved byte for byte in
[the initial import](https://github.com/heyyymonth/kerr-tidal-response-theory/commit/af774499c43b306a41612c37d629a2e41768ca43);
[import.json](provenance/import.json) records their hashes.

Subsequent commits contain the response basis, linear and mixed constructions,
and radial reduction. The
[checkpoint before the documentation review](https://github.com/heyyymonth/kerr-tidal-response-theory/tree/c5e7faaae858c8a060da524691f33ab08d1a20b6)
preserves the full accumulated handoff and research history. The review shortened
the public notes and separated the governing equations from the README. It did
not change the six calculation scripts or their expected scientific records.

The public name is **Kerr Tidal Response Theory**. The local directory retains
`kerr-tidal-response` for continuity with earlier handoff paths. Historical
context from the separate recoil project was consulted at
[revision 96f93a7](https://github.com/heyyymonth/black-hole-recoil-dynamics/tree/96f93a706f55f2c4f5d4fd1c734157553dc022a7).
No sibling or synced parent `sources/` files were changed, and none of that
project's calculations serves as evidence for the Kerr conjecture.

## Evidence records

| Calculation | Saved record | Checks and scope |
|---|---|---|
| [Baseline](verify_baseline.py) | [baseline.json](results/baseline.json) | 32 Ernst, Legendre, variation and angular checks. |
| [Horizon curvature](verify_mixed_horizon.py) | [mixed-horizon.json](results/mixed-horizon.json) | 18 curvature checks and 16 Ricci components after imposing local vacuum relations. |
| [Response basis](verify_response_basis.py) | [response-basis.json](results/response-basis.json) | 33 tensor, normalization and harmonic-coordinate checks. |
| [Linear drivers](verify_linear_drivers.py) | [linear-drivers.json](results/linear-drivers.json) | 82 recursion, metric identity, boundary and representative kernel checks. |
| [Mixed solution](verify_mixed_solution.py) | [mixed-solution.json](results/mixed-solution.json) | 36 map, forced-equation, angular, boundary and regularity-identity checks. |
| [Radial response](verify_radial_response.py) | [radial-response.json](results/radial-response.json) | 45 radial, primitive, horizon, Frobenius and subtraction checks. |

The total of 262 includes different kinds of evidence: exact differential
identities, controls, bookkeeping identities and consistency checks. It is not
262 independent proofs. [Verification coverage](docs/verification.md) explains
which claims each method supports.

The records are immutable checkpoints unless a scientific correction requires
a reviewed replacement. Their `not_established` statements describe the scope
of that individual calculation when written. For example, the baseline record
predates the mixed solution. Current status is in [CLAIMS.md](CLAIMS.md).

## Reproduction

With Python 3.11 and [pinned dependencies](requirements.txt), run:

```sh
.venv/bin/python verify_reproduction.py
.venv/bin/python verify_formal_transcription.py
```

The wrapper compares complete fresh outputs, serialized bytes, script hashes
and dependency versions. It also checks local Markdown file targets. The
default command writes nothing. `--report tmp/reproduction.json` saves a separate
execution receipt; it cannot overwrite expected scientific records. See
[CONTRIBUTING.md](CONTRIBUTING.md) before regenerating an expected record.

[results/reproduction.json](results/reproduction.json) records the interpreter,
platform, package versions, input hashes, comparisons and execution time.
Earlier receipts remain in Git history. The operating system and Python build
are not frozen; the actual Python patch version is recorded. Publication checks
also confirmed that changed expected results, changed calculation scripts and
attempts to overwrite an expected record with a receipt are rejected.

The [Lean project](formal/README.md) has a separate pinned toolchain and dependency
manifest. It checks selected statements from the radial calculation, including
their derivative and domain assumptions. The [CI workflow](.github/workflows/verify.yml)
runs symbolic reproduction and formal verification separately. A transcription
check compares the three explicit formal rational functions with the reproduced
radial record. CI does not
certify the encoding of the full Einstein problem or the unformalized analytic
arguments.

## Sources and attribution

[sources.json](provenance/sources.json) records primary-source versions,
inspection scope and available download hashes. The
[literature audit](docs/literature-audit.md) distinguishes published papers,
preprints and abstract-only screening. The governing exact metric family comes
from the cited literature; differentiating it does not transfer authorship of
that family to this project.

The published Gounis–Kehagias–Riotto PDF was retrieved again and its SHA-256
matched `58d49474ca3438ce77fa3c9dc87002cb930c48710bbccfb246bebb3df65cd1d6`.
Selected rendered pages were checked against extracted formulas. The published
version includes a mixed-quadrupole discussion absent from arXiv v1. Downloaded
papers and page images are temporary references and are not distributed here.

Original code and documentation use the [MIT license](LICENSE). Papers and
dependencies retain their own rights. [AUTHORS.md](AUTHORS.md) records authorship,
contact and assistance disclosure; [CITATION.cff](CITATION.cff) identifies this
working collection. No repository DOI or peer review is claimed.
