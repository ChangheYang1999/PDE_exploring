#!/usr/bin/env python3
"""Replay the scalar CORE verifier without touching its original output."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "operator_theory/verify_nonlinear_core_scalar.py"
ORIGINAL = HERE / "operator_theory/nonlinear_core_scalar_result.json"
OUT = HERE / "root_nonlinear_core_replay"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    before = {str(p.relative_to(HERE)): sha(p) for p in (SOURCE, ORIGINAL)}
    raw = SOURCE.read_text()
    virtual = OUT / SOURCE.name
    exec(compile(raw, str(virtual), "exec"),
         {"__name__": "__main__", "__file__": str(virtual)})
    replay = OUT / ORIGINAL.name
    expected = json.loads(ORIGINAL.read_text())
    observed = json.loads(replay.read_text())
    assert expected == observed
    assert observed["status"] == "NONLINEAR_CORE_SCALAR_CONTINUUM_PASS"
    assert observed["intervals"] == 3210
    assert observed["target"] == "53/50"
    assert before == {str(p.relative_to(HERE)): sha(p) for p in (SOURCE, ORIGINAL)}
    result = {
        "status": "ROOT_NONLINEAR_CORE_REPLAY_PASS",
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "source_and_result_sha256": before,
        "replay_result_sha256": sha(replay),
        "replay_result_relative_path": str(replay.relative_to(HERE)),
        "scalar_results_identical": True,
        "original_files_unchanged": True,
        "program_sha256": sha(Path(__file__)),
        "scope": "Fresh replay and provenance of the complete scalar continuum verifier; no stationary existence claim.",
    }
    (HERE / "ROOT_NONLINEAR_CORE_REPLAY.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
