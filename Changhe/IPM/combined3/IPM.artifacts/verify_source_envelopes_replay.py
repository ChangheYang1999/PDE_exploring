#!/usr/bin/env python3
"""Reassemble every saved source envelope and both exact endpoint regions."""
import hashlib
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "certify_source_envelopes.py"
INPUT = HERE / "source_envelopes_v01"
OUTPUT = HERE / "root_source_envelopes_replay"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    OUTPUT.mkdir(exist_ok=True)
    paths = [INPUT / "configuration.json", *sorted(INPUT.glob("chunk_*.json"))]
    original_result = INPUT / "result.json"
    bindings = {str(p.relative_to(HERE)): sha(p)
                for p in [SOURCE, original_result, *paths]}
    for path in paths:
        target = OUTPUT / path.name
        if target.exists():
            assert sha(target) == sha(path)
        else:
            target.write_bytes(path.read_bytes())
    spec = importlib.util.spec_from_file_location("independent_source_envelope_replay", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.assemble(OUTPUT)
    actual = json.loads(original_result.read_text())
    replay_path = OUTPUT / "result.json"
    replay = json.loads(replay_path.read_text())
    for data in (actual, replay):
        data.pop("finished_utc")
    assert actual == replay
    assert actual["status"] == "CERTIFIED_RADIAL_NEAR_SOURCE_ENVELOPES"
    for name, digest in bindings.items():
        assert sha(HERE / name) == digest
    out = {
        "status": "ROOT_SOURCE_ENVELOPE_REPLAY_PASS",
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "input_sha256": bindings,
        "replay_result_sha256": sha(replay_path),
        "program_sha256": sha(Path(__file__)),
        "all_assembly_values_identical": True,
        "original_files_unchanged": True,
        "scope": "Complete599-panel source envelope assembly and exact origin/far replay only; no existence claim.",
    }
    (HERE / "ROOT_SOURCE_ENVELOPE_REPLAY.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "input_sha256"}, indent=2))


if __name__ == "__main__":
    main()
