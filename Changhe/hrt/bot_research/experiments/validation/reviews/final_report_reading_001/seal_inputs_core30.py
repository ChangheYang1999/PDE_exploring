"""Bind this source-only report review to its previously copied inputs.

Standard-library byte reads only. This is not a policy, replay or strength check.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path.cwd()
OUT = ROOT / "bot_research/experiments/validation/reviews/final_report_reading_001"
RETAINED = OUT / "inputs/retained"
EXPECTED = {
    "bot_research/experiments/validation/reviews/economy_final_gate_001/AFRR_REVIEW_006.md": "23ed39dbe088ea004071f48823ac8ac99c84d1dc381307af245e7d72492a2227",
    "bot_research/experiments/validation/reviews/economy_final_gate_001/AFREP_REVIEW_011.md": "c6d87049b258edf61556a4c52efcdb97bbf82c697105b9da91eff9d1c1c619de",
    "bot_research/experiments/validation/reviews/economy_final_gate_001/FINAL_GATE_REVIEW_008.md": "e87d01a4a1c74a81d8c4ff356880f6767b19d0e20c1dfa8ca1cd36f67f15e19c",
    "bot_research/experiments/validation/reviews/economy_final_gate_001/root_afrr_afrep_review_001.json": "39be0a1627df819dfd83a06d78d97692a858627de3312e35754b300b2f1e131b",
    "bot_research/experiments/validation/reviews/economy_final_gate_001/root_gate_review_008.json": "a2e397edcdda875d58dbac67f2c5edabc2eccd15f04bae1d70257fac7283fb87",
    "bot_research/runs/economy/afrep/logs/20261031T233734-00001--make-free_fallback=-zero--foreign_attack_from=11-doom=-next-vs--make_best_v9e-std.jsonl": "546fb4af3079ed296cdcc36c0613161c8a206f619be1fbdf918c10bb62adcd77",
    "bot_research/runs/economy/afrep/logs/20261031T233734-00002--make_best_v9e-vs--make-free_fallback=-zero--foreign_attack_from=11-doom=-next-std.jsonl": "514c2c0a6b3ad8c0b50324ed868d8aab61762b01be464bbff2c8fd9deba81d5b",
}
SNAPSHOTS = {
    "REPORT.snapshot-001.md": "d25446a51868de63d9c81f54d5dd30f42adce120c0d03fc8379f0c6971160751",
    "REPORT.snapshot-002.md": "07fb468ee52d797e6e1e8f0bf4442fa604853591dde17dbd01fb62eebce4cc8c",
    "REPORT.snapshot-003.md": "476c8d5d9d00b858636e81c60f04f5601dd415289ed8895af6db99d1c5dd853d",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identify(path: Path) -> dict:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size}


def main() -> None:
    if os.sched_getaffinity(0) != {30} or os.getpriority(os.PRIO_PROCESS, 0) != 19:
        raise RuntimeError("Expected one permitted core 30 at nice 19")
    if not sys.dont_write_bytecode or os.environ.get("PYTHONDONTWRITEBYTECODE") != "1":
        raise RuntimeError("Bytecode must remain disabled")
    if os.environ.get("TMPDIR") != str(ROOT / "bot_research/tmp"):
        raise RuntimeError("Unexpected research scratch setting")
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise RuntimeError("Thread settings must all be one")
    destination = OUT / "INPUT_BINDINGS.json"
    if destination.exists():
        raise RuntimeError("Preserve existing receipt; use a separately named amendment")
    began = dt.datetime.now(dt.timezone.utc).isoformat()
    inputs = []
    for path in sorted(p for p in RETAINED.rglob("*") if p.is_file()):
        original = path.relative_to(RETAINED).as_posix()
        record = identify(path)
        record["source_path"] = original
        current = ROOT / original
        record["current_sha256_at_receipt"] = sha(current) if current.is_file() else None
        record["archive_equals_current_at_receipt"] = record["sha256"] == record["current_sha256_at_receipt"]
        if original in EXPECTED:
            record["known_earlier_pin_sha256"] = EXPECTED[original]
            if record["sha256"] != EXPECTED[original]:
                raise RuntimeError("Earlier receipt identity differs: " + original)
        inputs.append(record)
    seen = {record["source_path"] for record in inputs}
    if not set(EXPECTED).issubset(seen):
        raise RuntimeError("A previously pinned required archive is missing")
    for name, expected in SNAPSHOTS.items():
        path = OUT / "inputs" / name
        record = identify(path)
        if record["sha256"] != expected:
            raise RuntimeError("Preserved report snapshot differs: " + name)
        record["source_path"] = "bot_research/reports/REPORT.md"
        record["historical_snapshot"] = True
        inputs.append(record)
    notes = identify(OUT / "inputs/NOTES_FOR_TEAM.snapshot-001.md")
    notes["source_path"] = "../hrt-lead/NOTES_FOR_TEAM.md"
    inputs.append(notes)
    review = OUT / "REVIEW.md"
    if sha(review) != "b62205f58a74058e646754add79f00ecc58cdff96c7b467fa19a9da5aa9f998d":
        raise RuntimeError("The sent review bytes changed")
    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", review.read_text())
    missing = [link for link in links if not (review.parent / link.split("#", 1)[0]).exists()]
    if missing:
        raise RuntimeError("Unresolved review links: " + repr(missing))
    receipt = {
        "schema": "report_reading_input_binding_001",
        "began_at": began,
        "completed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_model": "GPT-6 Astra",
        "opus_collaboration": "Separate lead and economy lane notes; no substituted model label",
        "scope": "Posthoc source-only publication review, conditional on retained bytes",
        "policy_constructor_engine_game_replay_test_calls": 0,
        "new_numerical_strength_reduction": False,
        "review": identify(review),
        "binding_script": identify(Path(__file__).resolve()),
        "inputs": inputs,
        "input_count": len(inputs),
        "earlier_pin_comparisons": len(EXPECTED),
        "all_earlier_pin_comparisons_pass": True,
        "review_local_links": links,
        "all_review_local_links_resolve": True,
        "provenance_limits": [
            "Copied inputs are retained observations, not continuous source monitoring.",
            "Earlier review pins establish the stated earlier byte identities only.",
            "Mutable current report and notes may differ after their archived snapshots.",
            "No new replay, fresh policy audit, full runtime-data closure or erased-attempt audit was performed.",
        ],
    }
    payload = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if any(chr(34) + "/" + name + "/" in payload for name in ("mnt", "home", "efs", "tmp")):
        raise RuntimeError("A forbidden absolute local path would be published")
    with destination.open("x", encoding="utf-8") as stream:
        stream.write(payload)
    print(json.dumps({"receipt": destination.relative_to(ROOT).as_posix(), "sha256": sha(destination), "inputs": len(inputs)}))


if __name__ == "__main__":
    main()
