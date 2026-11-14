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
| [verify_reproduction.py](verify_reproduction.py) | Read-only comparison of fresh complete outputs, pinned package versions, and script/result hashes; also checks local Markdown file targets. |
| [reproduction.json](results/reproduction.json) | Fresh execution receipt with actual time, interpreter, platform, package versions, input hashes, and comparisons. |

Run with Python 3.11:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/python verify_reproduction.py
```

The default command never writes results. To retain a new execution receipt,
use `--report tmp/reproduction.json`. This option cannot target either expected
scientific record. The two original scripts' `--write` options deliberately
regenerate expected records and should be used only for a reviewed scientific
change, as described in [CONTRIBUTING.md](CONTRIBUTING.md).

The CI workflow installs the same pinned SymPy and mpmath versions in a fresh
Python 3.11 environment, checks dependencies, reruns both calculations, checks
local file links, and uploads its execution receipt. Actions are pinned to
verified commit SHAs. The receipt records the actual Python patch version;
the entire operating system and Python build are not frozen. Dependency pins
support reproducibility and are not a claim that those releases are the newest.

Publication validation also confirmed, in a temporary copy, that a changed expected result, a changed calculation script, and an attempt to overwrite an expected record with an execution receipt are rejected.

CI reports numerical/algebraic execution status. It does not review the
conditional asymptotic proof, validate global boundary conditions, or perform
EFT matching. The 16 Ricci components are checked after imposing the declared
local vacuum relations; they do not establish an arbitrary full metric as vacuum.

## Literature and rights

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
