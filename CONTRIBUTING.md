# Contributing

The objective is a proof or a consistently matched counterexample in a precisely
defined nonlinear Kerr tidal sector. Do not assume vanishing. Begin with
[research-context.md](research-context.md), [CLAIMS.md](CLAIMS.md), and
[the verification map](docs/verification.md).

State conventions, units, boundary conditions, expansion orders, and source
versions. Distinguish an exact identity, a conditional argument, a published
result, and a conjecture. A decaying coordinate term is not automatically a Love
coefficient, and an absent homogeneous seed is not a matched-response proof.

Before committing changes, use Python 3.11 and the pinned dependencies:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/python verify_reproduction.py
.venv/bin/python verify_formal_transcription.py
git diff --check
```

The reproduction command reruns all six symbolic calculations and compares their
complete outputs with the saved JSON, including script hashes. It never updates
those expected records. If an intentional scientific change invalidates them,
explain the change, preserve its predecessor in Git, review the new calculation,
and only then regenerate the relevant JSON with the original script's `--write`.
Update the claim and provenance records as appropriate. Do not change expected
values simply to make a failed check pass.

When changing formal statements or their dependencies, run the
[Lean build and axiom audit](formal/README.md). Review the theorem statement
against the mathematical note as well as checking that the proof compiles.

Use the published Gounis--Kehagias--Riotto paper for its equation numbers. Record
primary sources and actual version status; no DOI, priority, or peer-review claim
may be invented. Preserve third-party rights under their original licenses.

The sibling recoil repository and its manuscript are a separate project. Do not
edit them as part of this investigation. Synced parent-project `sources/` files
are read-only. Keep public cross-project links portable and preferably pinned.

No new-theorem manuscript is justified by the present checks. Any eventual
manuscript should use two-column APS/PRD REVTeX, standard typography and citations,
no watermark, and claims supported by the evidence. Compile and visually inspect
it before publication.
