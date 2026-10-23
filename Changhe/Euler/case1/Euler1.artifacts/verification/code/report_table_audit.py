"""Check displayed report tables against frozen evidence, without model execution."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGIONS = {
    "R < 0.25": "shell_0_0.25", "0.25 < R < 1": "shell_0.25_1",
    "1 < R < 2": "shell_1_2", "2 < R < 4": "shell_2_4",
    "4 < R < 8": "shell_4_8", "8 < R < 16": "shell_8_16",
    "16 < R < 32": "shell_16_32", "32 < R < 64": "shell_32_64",
    "core grid": "cartesian_grid_core", "axis": "axis_line",
}


def displayed_number(text):
    value = Decimal(text.replace(" x 10^", "e").strip())
    half_unit = Decimal(10) ** value.as_tuple().exponent / 2
    return float(value), float(half_unit)


def audit(report_path, frozen_path):
    raw = report_path.read_bytes()
    aggregate = json.loads(frozen_path.read_text())
    selected_path = ROOT / aggregate["selected_primary"]["audit_evidence"]
    selected = json.loads(selected_path.read_text())
    best = {(x["feature"], x["c_l"]): x for x in aggregate["best_by_representation_exponent"]}
    checks = []
    counts = dict(regional_rows=0, best_rows=0, final_time_rows=0)

    def compare(where, label, shown, actual):
        value, tolerance = displayed_number(shown)
        checks.append(dict(location=where, field=label, displayed=shown,
                           actual=actual, rounding_tolerance=tolerance,
                           verdict="CONFIRMED" if abs(value-actual) <= tolerance + 1e-16 else "REFUTED"))

    def exact(where, label, shown, actual):
        checks.append(dict(location=where, field=label, displayed=shown, actual=actual,
                           verdict="CONFIRMED" if shown == actual else "REFUTED"))

    for line in raw.decode().splitlines():
        if not line.startswith("|"):
            continue
        cells = [x.strip() for x in line.strip("|").split("|")]
        if len(cells) == 8 and cells[0] in REGIONS:
            name = REGIONS[cells[0]]
            region = selected["regions"][name]
            mom = region["momentum"]
            values = [mom["relative_rms"], mom["absolute"]["rms"], mom["absolute"]["q999"],
                      mom["absolute"]["sampled_max"], region["vorticity"]["relative_rms"],
                      region["pressure_poisson"]["relative_rms"], region["divergence"]["relative_rms"]]
            labels = ["eps_m", "Rm RMS", "Rm q999", "Rm max", "eps_omega", "eps_P", "eps_div"]
            for label, shown, actual in zip(labels, cells[1:], values):
                compare(name, label, shown, actual)
            counts["regional_rows"] += 1
        elif len(cells) == 5 and (cells[0] in ("first", "second") or cells[0].startswith("first (pilot")):
            feature = "dir_log" if cells[0].startswith("first") else "dir_tau"
            c = float(cells[1].split()[0])
            item = best[(feature, c)]
            where = f"{feature} c={c}"
            exact(where, "saved step", int(cells[2]), item["saved_step"])
            match = re.fullmatch(r"([^ (]+) \((.*)\)", cells[3])
            if not match:
                raise ValueError(f"Unrecognized momentum cell: {cells[3]}")
            compare(where, "eps_m", match.group(1), item["worst_eps_m"])
            exact(where, "worst region", REGIONS[match.group(2)], item["worst_region"])
            compare(where, "tail nonlinear ratio", cells[4], item["tail_nonlinear_relative"])
            counts["best_rows"] += 1
        elif len(cells) == 4 and "(final)" in cells[0]:
            exact("final time row", "training records", int(cells[1]), aggregate["ledger"]["records"])
            for cell, key in zip(cells[2:], ["credited_elapsed_union_bounds", "combined_with_validation"]):
                lower, upper = map(float, cell.split(" to "))
                actual = aggregate["ledger"][key]
                checks.append(dict(location="final time row", field=key, displayed=[lower, upper],
                                   actual=[actual["lower_hours"], actual["upper_hours"]],
                                   verdict="CONFIRMED" if lower <= actual["lower_hours"] and upper >= actual["upper_hours"] else "REFUTED"))
            counts["final_time_rows"] += 1
    for key, expected in [("regional_rows", 10), ("best_rows", 12), ("final_time_rows", 1)]:
        exact("table coverage", key, counts[key], expected)
    return dict(date_utc=datetime.now(timezone.utc).isoformat(), report_sha256=hashlib.sha256(raw).hexdigest(),
                report=str(report_path), frozen_numeric_audit=str(frozen_path),
                frozen_numeric_audit_sha256=hashlib.sha256(frozen_path.read_bytes()).hexdigest(),
                selected_evidence=str(selected_path.relative_to(ROOT)),
                selected_evidence_sha256=hashlib.sha256(selected_path.read_bytes()).hexdigest(),
                counts=counts, checks=checks, verdict="CONFIRMED" if all(x["verdict"] == "CONFIRMED" for x in checks) else "REFUTED",
                scope="Displayed-table arithmetic only. Source, method, scope and prose require a separate complete human/model audit.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--frozen", type=Path, default=ROOT/"final_snapshot/20261023T075719Z/NUMERIC_AUDIT.json")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT):
        raise ValueError("Output must remain inside the verifier lane")
    result = audit(args.report.resolve(), args.frozen.resolve())
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(dict(verdict=result["verdict"], counts=result["counts"],
                          checks=len(result["checks"]), report_sha256=result["report_sha256"])))
    return 0 if result["verdict"] == "CONFIRMED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
