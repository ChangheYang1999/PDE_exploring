"""Protected-file manifest check and detection of files outside bot_research/.

Usage (from the project root):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m bot_research.harness.integrity [--json OUT]

The check never modifies any file. It reports, relative to the manifest
bot_research/protected_files.sha256.json:
  missing   manifest entries absent from the working copy,
  changed   entries whose SHA-256 differs,
  extra     files outside bot_research/ (and outside .venv/) not in the manifest.
It also compares the result with the recorded starting baseline
(bot_research/reports/integrity_baseline.json) when that file exists.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "bot_research" / "protected_files.sha256.json"
BASELINE = ROOT / "bot_research" / "reports" / "integrity_baseline.json"
EXCLUDED_TOP = {"bot_research", ".venv"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def project_files() -> list[str]:
    files = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_TOP:
            continue
        if path.is_file() or path.is_symlink():
            files.append(rel.as_posix())
    return sorted(files)


def check() -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    present = project_files()
    present_set = set(present)
    missing = sorted(name for name in manifest if name not in present_set and not (ROOT / name).exists())
    changed = sorted(name for name in manifest if (ROOT / name).is_file() and sha256(ROOT / name) != manifest[name])
    extra = sorted(name for name in present if name not in manifest)
    hashes = {name: sha256(ROOT / name) for name in present}
    missing_games = [m for m in missing if m.startswith("data/games/")]
    return {
        "manifest_entries": len(manifest),
        "files_outside_bot_research": len(present),
        "missing_count": len(missing),
        "missing_data_games_count": len(missing_games),
        "missing_other": [m for m in missing if not m.startswith("data/games/")],
        "changed": changed,
        "extra_outside_bot_research": extra,
        "current_hashes": hashes,
    }


def compare_with_baseline(result: dict) -> dict:
    if not BASELINE.exists():
        return {"baseline": "absent"}
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    diffs = {}
    for key in ("missing_count", "missing_other", "changed", "extra_outside_bot_research", "current_hashes"):
        if base.get(key) != result.get(key):
            diffs[key] = {"baseline": base.get(key), "now": result.get(key)}
    return {"baseline": "present", "identical_to_baseline": not diffs, "differences": diffs}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", help="write the full result to this path (inside bot_research/)")
    parser.add_argument("--write-baseline", action="store_true", help="record the starting baseline (first shift only)")
    args = parser.parse_args(argv)
    result = check()
    if args.write_baseline:
        if BASELINE.exists():
            print("baseline already exists; not overwritten", file=sys.stderr)
            return 2
        BASELINE.parent.mkdir(parents=True, exist_ok=True)
        BASELINE.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    comparison = compare_with_baseline(result)
    summary = {k: v for k, v in result.items() if k != "current_hashes"}
    summary["baseline_comparison"] = comparison
    print(json.dumps(summary, indent=1, sort_keys=True))
    if args.json:
        Path(args.json).write_text(json.dumps({**result, "baseline_comparison": comparison}, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
