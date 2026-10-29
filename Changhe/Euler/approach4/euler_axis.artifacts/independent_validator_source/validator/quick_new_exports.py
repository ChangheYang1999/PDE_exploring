#!/usr/bin/env python3
"""Freeze-aware serial checks while pausing one of this lane's busy workers."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
EXPORTS = [
    ("ladder_l3sep", "T1_ladder_L3sep_20261029T013412.291018Z"),
    ("reflection_l0", "T1_reflection_L0_20261029T013412.291018Z"),
]


def main():
    pid = int(sys.argv[1])
    process = Path("/proc") / str(pid)
    if Path(os.readlink(process / "cwd")).resolve() != ROOT.parent:
        raise RuntimeError("Only this lane's worker may be paused")
    command = (process / "cmdline").read_bytes().replace(b"\0", b" ")
    if b"piecewise_pressure_audit.py" not in command:
        raise RuntimeError("Unexpected worker")
    output = ROOT / "results/new_exports_quick_20261029T0134Z"
    output.mkdir()
    start = time.perf_counter()
    record = {"started_utc": datetime.now(timezone.utc).isoformat(),
              "paused_pid": pid, "runs": [],
              "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    os.kill(pid, signal.SIGSTOP)
    try:
        for _ in range(100):
            if "T (stopped)" in (process / "status").read_text():
                break
            time.sleep(.01)
        else:
            raise RuntimeError("Pause not acknowledged")
        for name, directory in EXPORTS:
            export = ROOT / "external_exports" / directory
            tasks = [
                ("preflight", "export_preflight.py", [str(export)]),
                ("structure", "piecewise_structure_audit.py", [str(export / "coeffs.npz")]),
                ("interfaces", "piecewise_interface_audit.py", [str(export / "coeffs.npz")]),
                ("tail", "coefficient_tail_audit.py", [str(export / "coeffs.npz")]),
            ]
            for kind, script, arguments in tasks:
                destination = output / f"{name}_{kind}.json"
                command = [sys.executable, str(ROOT / script), *arguments,
                           "--output", str(destination)]
                begin = time.perf_counter()
                with (output / f"{name}_{kind}.log").open("w") as log:
                    completed = subprocess.run(command, stdout=log,
                                               stderr=subprocess.STDOUT, timeout=45)
                row = {"name": name, "kind": kind, "returncode": completed.returncode,
                       "wall_seconds": time.perf_counter() - begin}
                record["runs"].append(row)
                print(json.dumps(row), flush=True)
                if completed.returncode:
                    raise RuntimeError(f"Failed {name} {kind}; inspect retained output")
    finally:
        os.kill(pid, signal.SIGCONT)
        record["resumed_utc"] = datetime.now(timezone.utc).isoformat()
        record["pause_wall_seconds"] = time.perf_counter() - start
        (output / "resource_pause.json").write_text(json.dumps(record, indent=2) + "\n")


if __name__ == "__main__":
    main()
