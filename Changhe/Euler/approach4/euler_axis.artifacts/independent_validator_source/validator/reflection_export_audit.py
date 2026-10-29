#!/usr/bin/env python3
"""Check the documented reflection mask without changing active evaluators."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import signal
import subprocess
import sys
import time
from normalize_column_masks import normalize

ROOT = Path(__file__).resolve().parent


def main():
    pid = int(sys.argv[1])
    process = Path("/proc") / str(pid)
    if Path(os.readlink(process / "cwd")).resolve() != ROOT.parent:
        raise RuntimeError("Unexpected worker directory")
    if b"piecewise_pressure_audit.py" not in (process / "cmdline").read_bytes():
        raise RuntimeError("Unexpected worker")
    out = ROOT / "results/reflection_l0_mask_audit"
    out.mkdir()
    native = ROOT / "external_exports/T1_reflection_L0_20261029T013412.291018Z"
    expanded = ROOT / "external_exports/T1_reflection_L0_expanded_20261029T0136Z"
    record = {"started_utc": datetime.now(timezone.utc).isoformat(), "paused_pid": pid,
              "runs": []}
    start = time.perf_counter()
    os.kill(pid, signal.SIGSTOP)
    try:
        for _ in range(100):
            if "T (stopped)" in (process / "status").read_text():
                break
            time.sleep(.01)
        else:
            raise RuntimeError("Worker did not stop")
        record["normalization"] = normalize(native, expanded)
        for kind, script, inputs in [
            ("preflight", "export_preflight.py", [str(expanded)]),
            ("interfaces", "piecewise_interface_audit.py", [str(expanded / "coeffs.npz")]),
            ("structure", "piecewise_structure_audit.py", [str(expanded / "coeffs.npz")]),
            ("tail", "coefficient_tail_audit.py", [str(expanded / "coeffs.npz")]),
        ]:
            begin = time.perf_counter()
            with (out / f"{kind}.log").open("w") as log:
                proc = subprocess.run(
                    [sys.executable, str(ROOT / script), *inputs,
                     "--output", str(out / f"{kind}.json")],
                    stdout=log, stderr=subprocess.STDOUT, timeout=45)
            row = {"kind": kind, "returncode": proc.returncode,
                   "wall_seconds": time.perf_counter() - begin}
            record["runs"].append(row)
            print(json.dumps(row), flush=True)
            if proc.returncode:
                raise RuntimeError(f"{kind} failed; inspect retained log")
    finally:
        os.kill(pid, signal.SIGCONT)
        record["resumed_utc"] = datetime.now(timezone.utc).isoformat()
        record["pause_wall_seconds"] = time.perf_counter() - start
        (out / "resource_pause.json").write_text(json.dumps(record, indent=2) + "\n")


if __name__ == "__main__":
    main()
