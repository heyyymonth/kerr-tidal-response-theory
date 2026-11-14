"""Recompute both scientific records without rewriting the expected evidence.

Optionally write a separate execution receipt. This verifies declared algebra
and record integrity, not the unresolved Kerr boundary conditions or matching.
"""

import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import platform
import re
import time
from urllib.parse import unquote, urlsplit

import verify_baseline
import verify_mixed_horizon


ROOT = Path(__file__).resolve().parent
CALCULATIONS = (
    (verify_baseline, "results/baseline.json", 32, 0),
    (verify_mixed_horizon, "results/mixed-horizon.json", 18, 16),
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_links(pending_report=None):
    """Check local file targets in the collection's Markdown, not remote URLs."""
    checked = 0
    for document in sorted(ROOT.rglob("*.md")):
        parts = document.relative_to(ROOT).parts
        if any(part.startswith(".") or part in {"tmp", "__pycache__"} for part in parts):
            continue
        for target in re.findall(r"\]\(([^\s)]+)\)", document.read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (document.parent / unquote(url.path)).resolve()
            if not path.is_relative_to(ROOT):
                raise ValueError(f"Nonportable local link in {document.name}: {target}")
            if not path.is_file() and path != pending_report:
                raise ValueError(f"Missing local link in {document.name}: {target}")
            checked += 1
    return checked


def run(report_path=None):
    packages = {}
    for requirement in (ROOT / "requirements.txt").read_text().splitlines():
        requirement = requirement.strip()
        if not requirement or requirement.startswith("#"):
            continue
        if not re.fullmatch(r"[A-Za-z0-9_.-]+==[A-Za-z0-9_.+-]+", requirement):
            raise ValueError(f"Expected an exact dependency pin: {requirement}")
        package, expected = requirement.split("==")
        installed = version(package)
        if installed != expected:
            raise ValueError(f"{package}: installed {installed}, expected {expected}")
        packages[package] = installed

    inputs = ["requirements.txt", "verify_reproduction.py"]
    comparisons = []
    for module, filename, expected_count, expected_ricci in CALCULATIONS:
        script = Path(module.__file__).resolve()
        saved_bytes = (ROOT / filename).read_bytes()
        saved = json.loads(saved_bytes)
        if saved["script_sha256"] != sha256(script):
            raise ValueError(f"{filename}: script hash no longer matches the saved evidence")
        started = time.monotonic()
        actual = module.run()
        if actual != saved:
            differing = sorted(key for key in actual.keys() | saved.keys() if actual.get(key) != saved.get(key))
            raise ValueError(f"{filename}: fresh result differs in {differing}")
        if (json.dumps(actual, indent=2) + "\n").encode() != saved_bytes:
            raise ValueError(f"{filename}: serialized output differs from the saved bytes")
        if actual["checks_passed"] != expected_count or len(actual["checks"]) != expected_count:
            raise ValueError(f"{filename}: unexpected number of checks")
        if any(check["status"] != "verified" for check in actual["checks"]):
            raise ValueError(f"{filename}: an unverified check remains")
        if actual.get("vacuum_ricci_components_checked", 0) != expected_ricci:
            raise ValueError(f"{filename}: unexpected Ricci-component count")
        comparisons.append({
            "record": filename,
            "checks_passed": expected_count,
            "vacuum_ricci_components_checked": expected_ricci,
            "complete_output_matches_saved_record": True,
            "serialized_output_matches_saved_bytes": True,
            "elapsed_seconds": round(time.monotonic() - started, 3),
        })
        inputs.extend([script.relative_to(ROOT).as_posix(), filename])
        print(f"{filename}: {expected_count} checks, {expected_ricci} Ricci components; exact saved-record match.", flush=True)

    link_count = local_links(report_path)
    report = {
        "schema_version": 1,
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_level": "reproduction of declared symbolic identities and saved evidence; no matched Love coefficient",
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "packages": packages,
        "inputs_sha256": {name: sha256(ROOT / name) for name in inputs},
        "comparisons": comparisons,
        "local_markdown_file_links_checked": link_count,
        "expected_scientific_records_rewritten": False,
    }
    if os.environ.get("GITHUB_SHA"):
        report["github_commit"] = os.environ["GITHUB_SHA"]
        report["github_run_id"] = os.environ.get("GITHUB_RUN_ID")
    print(f"Reproduced 32 baseline + 18 curvature checks and 16 Ricci components; {link_count} local file links valid.")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Write a separate execution receipt; never the expected scientific records.")
    args = parser.parse_args()
    target = args.report.resolve() if args.report else None
    protected = {ROOT / name for _, name, _, _ in CALCULATIONS}
    protected.update(ROOT / name for name in ("verify_baseline.py", "verify_mixed_horizon.py", "verify_reproduction.py", "requirements.txt"))
    if target in protected:
        parser.error("--report cannot overwrite a calculation input or expected scientific record")
    result = run(target)
    if target:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(result, indent=2) + "\n")
        print(f"Execution receipt written to {target.name}.")
