"""Run the prepared local checks sequentially after the existing audit exits."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import sys
import time

sys.dont_write_bytecode = True


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def active(pid):
    status = Path("/proc") / str(pid) / "status"
    if not status.exists():
        return False
    for line in status.read_text().splitlines():
        if line.startswith("State:"):
            return line.split()[1] != "Z"
    return False


def main():
    out = Path("artifacts/storage/shift2_final_queue.json")
    records = []
    start = time.monotonic()
    while active(3718523):
        if time.monotonic() - start > 900:
            raise RuntimeError("The preceding audit did not exit within 900 seconds.")
        time.sleep(5)
    checks = json.loads(
        Path("research/166_edge30_later_order/verification/checks.json").read_text()
    )
    assert checks["all_cartesian_checks_pass"]
    jobs = [
        (
            ["code/period_four_prefix_radii.py"],
            "research/178_period_four_prefix_radii/verification/producer.log",
        ),
        (
            ["code/longer_four_ninths_prefixes.py"],
            "research/179_longer_four_ninths_prefixes/verification/producer.log",
        ),
        (
            ["code/period_five_numerical_audit.py", "--roots", "6"],
            "research/180_period_five_numerical_audit/verification/producer.log",
        ),
    ]
    for arguments, log_name in jobs:
        began = time.monotonic()
        row = {"arguments": arguments, "started_at_utc": stamp(), "log": log_name}
        with Path(log_name).open("w") as log:
            child = subprocess.Popen(
                [sys.executable, "-u", *arguments],
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=subprocess.STDOUT,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            row["pid"] = child.pid
            records.append(row)
            out.write_text(json.dumps({"jobs": records}, indent=2) + "\n")
            status = child.wait()
        row.update(
            ended_at_utc=stamp(),
            actual_elapsed_s=time.monotonic() - began,
            exit_status=status,
        )
        out.write_text(json.dumps({"jobs": records}, indent=2) + "\n")
        if status:
            raise RuntimeError(f"Prepared job failed: {arguments[0]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(
            json.dumps(
                {
                    "checked_at_utc": stamp(),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            ),
            flush=True,
        )
        raise SystemExit(1)
