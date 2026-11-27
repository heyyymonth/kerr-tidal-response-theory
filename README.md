# Kerr Tidal Response Theory

Classical general relativity · Rotating black holes · Nonlinear tidal response

**Contributed by Hemanth.**

Venkata Hemanth Athota · Independent researcher · Working research notes

[![Research verification](https://github.com/heyyymonth/kerr-tidal-response-theory/actions/workflows/verify.yml/badge.svg)](https://github.com/heyyymonth/kerr-tidal-response-theory/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project studies stationary, axisymmetric perturbations of a Kerr black
hole. The mathematical problem is to construct interacting tidal fields,
establish regularity, and define a response coefficient when the perturbation
equation itself has a nonlinear source. The physical interpretation asks which
part of the deformed geometry can be attributed to the black hole's response.

The first calculation couples quadrupolar and hexadecapolar seed fields through
second order in spin. It gives regular mixed fields for explicit boundary data
and a quadrupolar connection coefficient whose value depends on the chosen
subtraction. An independently matched physical Love coefficient remains open.

## Results

The [linear](docs/linear-construction.md) and
[mixed](docs/mixed-construction.md) constructions give explicit Ernst
potentials satisfying their perturbative equations. Local metric regularity
uses a known distorted-Kerr family. The uniqueness argument assumes finitely
many angular modes, complete exterior data, fixed gauge and rod conventions,
and a common smooth horizon chart. The prescribed growing fields include
spin-linked odd sectors; their identification with purely electric physical
tides has not been established.

The [radial reduction](docs/radial-response.md) compares two references
constructed from the source. Writing the connection coefficient as
$b=b_0+\chi^2 b_2+\cdots$ gives:

| Reference convention | $b_0$ | $b_2$ |
|---|---:|---:|
| Primitive with zero finite part at infinity | $0$ | $-16172/218295$ |
| Formal Frobenius reference with two specified coefficients set to zero | $0$ | $-17760/218295$ |

The change is in the definition of the coefficient; the regular metric stays
the same. Homogeneous-solution calibration and a static zero therefore do not
fix an absolute sourced response. The next mathematical problem is to classify
the remaining freedom and identify quantities independent of it, or supply a
further criterion that selects a reference.

An earlier [horizon-curvature calculation](mixed-horizon.md) reconstructs a
local obstruction to a singular decaying seed in a restricted vacuum family.
That obstruction does not determine the regular solution driven by interacting
fields. A vanishing response would also allow tidal deformation of the horizon.

## Reading guide

| Note | Content |
|---|---|
| [Ernst equation](docs/ernst-equation.md) | Conventions, static seeds and mixed source equation. |
| [Linear construction](docs/linear-construction.md) | Driver fields, boundary data, regularity and restricted uniqueness. |
| [Mixed construction](docs/mixed-construction.md) | Driven interaction through spin squared. |
| [Radial response](docs/radial-response.md) | Source subtraction, connection coefficient and its ambiguity. |
| [Response definition](docs/response-definition.md) | Tensor structures and the combination accessible in alignment. |
| [Regularity and matching](docs/regularity-and-matching.md) | Physical interpretation and remaining matching obligations. |
| [Claims and evidence](CLAIMS.md) | Results, assumptions and limits. |
| [Verification](docs/verification.md) | Symbolic checks, Lean proofs and unformalized steps. |

[Research history](research-context.md) explains the choice of problem and
approaches set aside. [Research state](NEW_CHAT_HANDOFF.md) records the current
checkpoint. The [literature audit](docs/literature-audit.md) distinguishes
published results, preprints and the scope of each source inspection.

## Reproduction

Use Python 3.11 and the pinned dependencies:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/python verify_reproduction.py
.venv/bin/python verify_formal_transcription.py
```

This reruns six calculations, compares their complete outputs and hashes with
the saved records, and checks local Markdown file links. It does not rewrite
expected results. See [provenance](PROVENANCE.md), the
[execution receipt](results/reproduction.json) and the
[CI workflow](.github/workflows/verify.yml).

The [Lean project](formal/README.md) checks selected radial statements with a
proof kernel. Its theorem statements and assumptions are listed separately
from the symbolic checks; it does not formalize the entire Kerr construction.

## Attribution

Use [CITATION.cff](CITATION.cff) or [CITATION.bib](CITATION.bib) with the exact
Git revision, and cite the [primary papers](references.bib) for their results.
These are working notes, not a peer-reviewed manuscript. Original code and
documentation use the [MIT license](LICENSE). Contact and assistance disclosure
are in [AUTHORS.md](AUTHORS.md).
