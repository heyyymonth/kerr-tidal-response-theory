"""Compare the explicit Lean rational functions with the saved radial calculation.

This is a transcription check, not a proof checker. Lean proves the identities;
verify_reproduction.py separately regenerates the scientific record.
"""

import json
from pathlib import Path
import re

import sympy as sp


ROOT = Path(__file__).resolve().parent
DECLARATIONS = {
    "solution2": "radial_solution",
    "source2": "radial_source",
    "primitive2": "source_only_primitive",
}


def check_transcription(lean_text, sector):
    x = sp.Symbol("x")
    for declaration, field in DECLARATIONS.items():
        pattern = rf"def {declaration}\s*:\s*Fraction\s*:=\s*⟨([^,]+),([^⟩]+)⟩"
        matches = re.findall(pattern, lean_text)
        if len(matches) != 1:
            raise ValueError(f"Expected one explicit Fraction definition: {declaration}")
        parts = []
        for expression in matches[0]:
            if not re.fullmatch(r"[0-9X+*^()\s-]+", expression):
                raise ValueError(f"Unsupported polynomial syntax in {declaration}")
            parts.append(sp.sympify(expression.replace("^", "**"), locals={"X": x}))
        numerator, denominator = parts
        if denominator == 0:
            raise ValueError(f"Zero denominator in {declaration}")
        expected = sp.sympify(sector[field], locals={"x": x})
        if sp.cancel(numerator / denominator - expected) != 0:
            raise ValueError(f"Lean {declaration} differs from saved {field}")
    return len(DECLARATIONS)


if __name__ == "__main__":
    source = (ROOT / "formal/KerrRadial/Rational.lean").read_text()
    record = json.loads((ROOT / "results/radial-response.json").read_text())
    count = check_transcription(source, record["sectors"]["2"])
    print(f"Verified {count} Lean rational definitions against the saved radial record.")
