#!/usr/bin/env python3
"""Audit a completed Mac Pro reproduction without importing numerical code.

Read-only except for the explicitly selected JSON output. This is a full-suite
gate, not an optimizer or a replacement for the supplied numerical verifier.
"""
import argparse
from collections import Counter
import datetime
import hashlib
import json
import math
from pathlib import Path
import platform
import struct
import sys
import time

sys.dont_write_bytecode = True

PROVENANCE = ("verifier_sha256", "portable_source_sha256", "python", "numpy",
              "scipy", "hostname", "threadpools")
STEPS = [.004, .002]
THRESHOLD = 1e-5


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(case):
    return hashlib.sha256(struct.pack("<25d", case["cl"], *case["coefficients"])).hexdigest()


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def blas_signature(pools):
    keys = ("user_api", "internal_api", "filepath", "version", "threading_layer", "architecture")
    return sorted([{k: row.get(k) for k in keys} for row in pools], key=lambda row: str(row["filepath"]))


class Audit:
    def __init__(self):
        self.checks = []

    def check(self, name, passed, **details):
        self.checks.append({"name": name, "passed": bool(passed), **details})

    def load(self, path, name=None):
        try:
            return read(path)
        except (OSError, ValueError) as exc:
            self.check(name or str(path), False, error=str(exc))
            return None


def summarize(args):
    audit = Audit()
    run = args.run_dir.resolve()
    migration = run / "migration_preparation"
    records = run / "deployment_records"
    reference = args.reference_dir.resolve() if args.reference_dir else None
    results = migration / "reproduction/results"
    source = migration / "portable/stage10_completion"
    session_dir = run / "resource_session"
    candidates = audit.load(results / "candidates_macpro.json", "candidate result present")
    summary = audit.load(results / "stationarity_summary_macpro.json", "full stationarity summary present")
    directions = [audit.load(results / ("stationarity_direction_%02d.json" % i),
                             "fresh stationarity direction %02d present" % i) for i in range(22)]
    session = audit.load(session_dir / "session.json", "fresh session present")
    policy = audit.load(session_dir / "policy.json", "session policy present")
    baseline = audit.load(session_dir / "session_baseline.json", "fresh baseline present")
    native = audit.load(records / "native_environment.json", "native environment capture present")
    hardware = audit.load(records / "hardware_inventory.json", "hardware inventory present")
    benchmark_root = reference / "migration_preparation" if reference else migration
    archived_candidates = audit.load(benchmark_root / "reproduction/results/candidates.json", "archived candidate benchmark present")
    package = audit.load(migration / "inventories/package_sha256.json", "archive manifest present")
    archive_stationarity = audit.load(source / "reference_results/final_stationarity_scale4.json",
                                     "archived stationarity benchmark present")

    if session and policy and baseline:
        audit.check("session policy hash unchanged", digest(session_dir / "policy.json") == session.get("policy_sha256"))
        audit.check("fresh baseline hash unchanged", digest(session_dir / "session_baseline.json") == session.get("baseline_sha256"))
        audit.check("session baseline describes macOS", baseline.get("platform") == "Darwin")
        audit.check("session hostname is current host", session.get("hostname") == platform.node())
        initial = audit.load(session_dir / "initial_assessment.json", "initial resource assessment present")
        if initial:
            audit.check("initial resource assessment passes", initial.get("stop") is False)

    # Bind all immutable numerical sources, grids, saved vectors and stationarity
    # data to the original archive manifest, including inputs not hashed by the
    # supplied verifier's top-level result.
    immutable = []
    if package:
        for name, expected in package.get("files", {}).items():
            relative = Path(name)
            if (str(relative).startswith("migration_preparation/portable/") or
                    str(relative).startswith("migration_preparation/hardware/") or
                    name == "migration_preparation/reproduction/verify_candidates.py"):
                path = run / relative
                okay = path.is_file() and path.stat().st_size == expected.get("bytes") and digest(path) == expected.get("sha256")
                immutable.append({"path": name, "passed": okay})
        audit.check("all archived portable sources and numerical inputs unchanged", bool(immutable) and all(row["passed"] for row in immutable),
                    checked_files=len(immutable), errors=[row["path"] for row in immutable if not row["passed"]])
        code_names = {p.name for p in source.glob("*.py")}
        archived_names = {Path(name).name for name in package.get("files", {})
                          if Path(name).parent.as_posix() == "migration_preparation/portable/stage10_completion" and name.endswith(".py")}
        audit.check("portable module set is unchanged", code_names == archived_names)

    preservation = {}
    for phase in ("before", "after"):
        data = audit.load(records / ("verification_%s.json" % phase), "reference integrity %s present" % phase)
        preservation[phase] = data
        if data:
            for kind in ("package", "history"):
                item = data.get(kind, {})
                audit.check("reference %s integrity %s passes" % (kind, phase),
                            item.get("passed") is True and not item.get("errors"), checked_files=item.get("checked_files"))
    frozen_path = records / "active_frozen_integrity.json"
    frozen = audit.load(frozen_path, "active frozen integrity present")
    if frozen:
        audit.check("active immutable files unchanged after execution", frozen.get("passed") is True and not frozen.get("errors"),
                    checked_files=frozen.get("files"))
    if reference:
        audit.check("reference and active workspaces are distinct", reference != run and reference not in run.parents and run not in reference.parents)
        reference_manifest = reference / "migration_preparation/inventories/package_sha256.json"
        audit.check("reference archive manifest matches active manifest", reference_manifest.is_file() and digest(reference_manifest) == digest(migration / "inventories/package_sha256.json"))

    numerical_checks = candidates.get("checks", []) if candidates else []
    discrepancies = []
    if candidates and archived_candidates:
        expected_checks = archived_candidates.get("checks", [])
        names = [row.get("name") for row in numerical_checks]
        audit.check("all three saved profiles present", set(candidates.get("cases", {})) == {"final", "five", "original"})
        audit.check("all 221 candidate checks match archived order and identities", len(numerical_checks) == 221 and
                    names == [row.get("name") for row in expected_checks])
        errors = []
        for index, row in enumerate(numerical_checks):
            expected = expected_checks[index] if index < len(expected_checks) else {}
            actual, target, limit = row.get("actual"), row.get("expected"), row.get("tolerance")
            okay = (all(finite(value) for value in (actual, target, limit)) and limit >= 0 and
                    row.get("name") == expected.get("name") and target == expected.get("expected") and limit == expected.get("tolerance"))
            difference = abs(actual-target) if okay else None
            okay = okay and difference <= limit and row.get("passed") is True and row.get("absolute_difference") == difference
            if not okay:
                errors.append(row)
            discrepancies.append({**row, "fraction_of_tolerance": difference / limit if okay and limit else (0. if okay else None)})
        audit.check("221 candidate comparisons independently satisfy archived tolerances", not errors and len(numerical_checks) == 221,
                    errors=errors)
        audit.check("candidate overall verdict passes", candidates.get("passed") is True)
        audit.check("saved coefficients directly evaluated", candidates.get("original_coefficients_not_re_solved") is True)
        audit.check("documented tolerances unchanged", candidates.get("tolerances") == archived_candidates.get("tolerances"))
        for label, case in candidates.get("cases", {}).items():
            input_path = source / ("inputs/start_original.json" if label == "original" else "reference_results/%s.json" % label)
            original = audit.load(input_path, "saved input %s present" % label)
            if original:
                audit.check("%s current input hash and exact coefficient identity" % label,
                            case.get("input_sha256") == digest(input_path) and case.get("physical_vector_sha256") == fingerprint(original) and
                            case.get("coefficients") == original.get("coefficients") and case.get("cl") == original.get("cl"))

    present = [("candidates", candidates), ("stationarity-summary", summary)] + [("stationarity-%02d" % i, d) for i, d in enumerate(directions)]
    current_verifier = digest(migration / "reproduction/verify_candidates.py") if (migration / "reproduction/verify_candidates.py").is_file() else None
    current_source = {p.name: digest(p) for p in source.glob("*.py")}
    provenance = {k: candidates.get(k) for k in PROVENANCE} if candidates else {}
    for label, record in present:
        if not record:
            continue
        audit.check("%s code and environment provenance matches candidates" % label,
                    {k: record.get(k) for k in PROVENANCE} == provenance and
                    record.get("verifier_sha256") == current_verifier and record.get("portable_source_sha256") == current_source)
        audit.check("%s freshly generated after session initialization" % label,
                    bool(session) and finite(record.get("generated_utc_epoch")) and record["generated_utc_epoch"] > session.get("initialized_time", math.inf))
        audit.check("%s uses native environment and this host" % label,
                    record.get("executable") == str(run / "native_venv/bin/python") and record.get("hostname") == platform.node())
        audit.check("%s is read-only numerical verification" % label, record.get("no_optimization") is True)
        audit.check("%s numerical thread pools limited to one" % label,
                    bool(record.get("threadpools")) and all(pool.get("num_threads") == 1 for pool in record["threadpools"]))

    norms = []
    direction_errors = []
    final_fingerprint = candidates.get("cases", {}).get("final", {}).get("physical_vector_sha256") if candidates else None
    for index, record in enumerate(directions):
        if not record:
            continue
        rows = record.get("rows", [])
        okay = (record.get("direction") == index and record.get("physical_vector_sha256") == final_fingerprint and
                record.get("passed") is True and [row.get("physical_step") for row in rows] == STEPS and
                all(finite(row.get(k)) for row in rows for k in ("FD_gradient", "FD_gradient_over_rnorm", "relative_J_error")))
        if not okay:
            direction_errors.append(index)
    complete_directions = all(directions) and not direction_errors
    audit.check("22 fresh direction identities, both steps and finite derivatives", complete_directions,
                errors=direction_errors, present=sum(record is not None for record in directions))
    if complete_directions:
        norms = [math.hypot(*(record["rows"][i]["FD_gradient_over_rnorm"] for record in directions)) for i in range(2)]
        audit.check("both freshly recomputed full stationarity norms satisfy 1e-5", max(norms) <= THRESHOLD,
                    FD_relative=norms, threshold=THRESHOLD)
    if summary:
        audit.check("stationarity summary binds all directions to matching provenance", summary.get("directions") == 22 and
                    summary.get("physical_FD_steps") == STEPS and summary.get("physical_vector_sha256") == final_fingerprint and
                    summary.get("direction_run_provenance") == provenance)
        reported = summary.get("FD_relative", [])
        audit.check("stationarity summary norms independently reassemble", len(norms) == 2 and len(reported) == 2 and
                    all(finite(v) and abs(v-n) <= 1e-18 for v, n in zip(reported, norms)))
        audit.check("fresh full stationarity established at unchanged threshold", summary.get("threshold") == THRESHOLD and
                    summary.get("passed") is True and summary.get("fresh_full_stationarity_established") is True)

    if hardware and native and candidates:
        physical_arch = hardware.get("native_architecture")
        audit.check("native macOS interpreter matches physical CPU architecture", physical_arch in ("x86_64", "arm64") and
                    native.get("system") == "Darwin" and native.get("machine") == physical_arch and physical_arch in candidates.get("platform", "") and
                    platform.machine() == physical_arch)
        audit.check("recorded numerical environment matches executed environment", native.get("executable") == candidates.get("executable") and
                    native.get("python", "").startswith(candidates.get("python", "MISSING")) and
                    native.get("packages", {}).get("numpy") == candidates.get("numpy") and
                    native.get("packages", {}).get("scipy") == candidates.get("scipy") and
                    blas_signature(native.get("threadpools", [])) == blas_signature(candidates.get("threadpools", [])))
        audit.check("native environment dependency check passes", native.get("pip_check", {}).get("returncode") == 0)

    guard_results = []
    samples = []
    for path in sorted((session_dir / "runs").glob("*/result.json")):
        record = audit.load(path)
        if not record:
            continue
        guard_results.append(record)
        audit.check("guard run %s completed successfully" % path.parent.name,
                    record.get("success") is True and record.get("worker_started") is True and record.get("returncode") == 0 and
                    not record.get("stop_reasons") and record.get("session_id") == (session or {}).get("session_id") and
                    (path.parent / "worker.log").is_file())
        env = record.get("controlled_environment", {})
        vars_ = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS", "GOTO_NUM_THREADS")
        audit.check("guard run %s uses controlled session and threads" % path.parent.name,
                    all(env.get(key) == "1" for key in vars_) and env.get("IPM_RESOURCE_SESSION") == str(session_dir) and
                    env.get("IPM_RESOURCE_RUN") == str(path.parent))
        try:
            telemetry = [json.loads(line) for line in (path.parent / "resources.jsonl").read_text().splitlines() if line.strip()]
            samples.extend(telemetry)
            audit.check("guard run %s telemetry has no stop" % path.parent.name,
                        bool(telemetry) and all(row.get("decision", {}).get("stop") is False for row in telemetry))
        except (OSError, ValueError) as exc:
            audit.check("guard run %s telemetry readable" % path.parent.name, False, error=str(exc))
    audit.check("at least 24 completed supervised jobs", len(guard_results) >= 24, jobs=len(guard_results))
    for label, record in present:
        if not record:
            continue
        matches = []
        for job in guard_results:
            command = job.get("command", [])
            mode = "stationarity" if label.startswith("stationarity-") and label != "stationarity-summary" else label
            if str(migration / "reproduction/verify_candidates.py") not in command or mode not in command:
                continue
            if mode == "stationarity":
                if "--direction" not in command or command[command.index("--direction")+1] != str(record.get("direction")):
                    continue
            epoch = record.get("generated_utc_epoch")
            if finite(epoch) and job.get("started_time", math.inf) <= epoch <= job.get("finished_time", -math.inf):
                matches.append(job.get("run_id"))
        audit.check("%s result was generated by a successful supervised job" % label, len(matches) == 1, matching_run_ids=matches)
    try:
        ledger = [json.loads(line) for line in (session_dir / "session_ledger.jsonl").read_text().splitlines() if line.strip()]
        audit.check("guard ledger completely accounts for completed jobs", Counter(row.get("run_id") for row in ledger) == Counter(row.get("run_id") for row in guard_results) and
                    all(row.get("returncode") == 0 and not row.get("stop_reasons") for row in ledger))
    except (OSError, ValueError) as exc:
        ledger = []
        audit.check("guard session ledger readable", False, error=str(exc))
    audit.check("fresh resource session has no holds", not (session_dir / "ACTIVE_HOLD.json").exists() and not list((session_dir / "holds").glob("*.json")))

    benchmarks = {}
    if candidates and archived_candidates:
        for label, case in candidates.get("cases", {}).items():
            old = archived_candidates.get("cases", {}).get(label, {})
            row = {"cl": case.get("cl"), "a0": case.get("a0"), "physical_vector_sha256": case.get("physical_vector_sha256"),
                   "J97": case.get("objectives", {}).get("97", {}).get("J_joint"),
                   "archived_J97": old.get("objectives", {}).get("97", {}).get("J_joint"),
                   "objectives": case.get("objectives"), "independent_physical_residuals": case.get("validation"),
                   "Taylor": case.get("high_precision_independent_Taylor"), "canonical_Poisson_inverse": case.get("canonical_full_plane_inverse")}
            if finite(row["J97"]) and finite(row["archived_J97"]):
                row["J97_minus_archived_reproduction"] = row["J97"] - row["archived_J97"]
            benchmarks[label] = row
    snapshots = [row.get("snapshot", {}) for row in samples]
    def extrema(key, function):
        values = [row[key] for row in snapshots if finite(row.get(key))]
        return function(values) if values else None
    failed = [row for row in audit.checks if not row["passed"]]
    direction_error_rows = [
        {"direction": record.get("direction"),
         "physical_steps": [row.get("physical_step") for row in record.get("rows", [])],
         "relative_J_errors": [row.get("relative_J_error") for row in record.get("rows", [])],
         "FD_gradient_over_rnorm": [row.get("FD_gradient_over_rnorm") for row in record.get("rows", [])]}
        for record in directions if record]
    relative_errors = [row["relative_J_error"] for record in directions if record
                       for row in record.get("rows", []) if finite(row.get("relative_J_error"))]
    errors_by_step = [{"physical_step": step,
                       "maximum_relative_J_error": max((row["relative_J_error"] for record in directions if record
                                                        for row in record.get("rows", [])
                                                        if row.get("physical_step") == step and finite(row.get("relative_J_error"))),
                                                       default=None)} for step in STEPS]
    report = {
        "schema": 1, "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "run_dir": str(run), "reference_dir": str(reference) if reference else None,
        "status": "passed" if not failed else "failed", "passed": not failed,
        "full_suite_gate_passed": not failed, "no_optimization": True,
        "counts": {"candidate_profiles": len((candidates or {}).get("cases", {})), "candidate_checks": len(numerical_checks),
                   "passing_candidate_checks": sum(row.get("passed") is True for row in numerical_checks),
                   "fresh_stationarity_directions": sum(record is not None for record in directions),
                   "supervised_jobs": len(guard_results), "telemetry_samples": len(samples),
                   "gate_checks": len(audit.checks), "gate_failures": len(failed)},
        "hardware": hardware, "fresh_resource_baseline": baseline, "resource_policy": policy,
        "actual_environment": {"native_capture": native, "executed_provenance": provenance,
                               "executed_platform": (candidates or {}).get("platform"), "executable": (candidates or {}).get("executable")},
        "benchmarks": benchmarks,
        "stationarity": {"physical_FD_steps": STEPS, "fresh_FD_relative": norms, "threshold": THRESHOLD,
                         "max_relative_J_error": max(relative_errors, default=None),
                         "maximum_relative_J_error_by_physical_step": errors_by_step,
                         "step_to_step_norm_difference": abs(norms[0]-norms[1]) if len(norms) == 2 else None,
                         "direction_relative_errors": direction_error_rows,
                         "archived_FD_relative": (archive_stationarity or {}).get("FD_relative"),
                         "fresh_minus_archived_FD_relative": [a-b for a,b in zip(norms, (archive_stationarity or {}).get("FD_relative", []))],
                         "archived_hybrid_relative": (archive_stationarity or {}).get("hybrid_relative"),
                         "reassembled_hybrid_relative": (candidates or {}).get("cases", {}).get("final", {}).get("preserved_stationarity", {}).get("hybrid_relative_reassembled")},
        "numerical_discrepancies": sorted(discrepancies, key=lambda row: row.get("fraction_of_tolerance") or 0, reverse=True),
        "resources": {"total_supervised_wall_seconds": sum(row.get("wall_seconds", 0) for row in guard_results),
                      "maximum_process_family_RSS_MiB": max((row.get("peak_family_rss_mib", 0) for row in guard_results), default=None),
                      "minimum_available_RAM_MiB": extrema("available_mib", min), "minimum_disk_free_GiB": extrema("disk_free_gib", min),
                      "maximum_swap_used_MiB": extrema("swap_used_mib", max),
                      "jobs": [{k: row.get(k) for k in ("run_id", "command", "returncode", "success", "wall_seconds", "peak_family_rss_mib", "stop_reasons")} for row in guard_results]},
        "preservation": preservation, "active_frozen_integrity": frozen,
        "gate_checks": audit.checks, "verification_failures": failed,
    }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--reference-dir", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--require-passed", action="store_true", help="Return nonzero unless every full-suite gate check passes")
    args = parser.parse_args()
    output, run = args.output.resolve(), args.run_dir.resolve()
    if run not in output.parents or run / "migration_preparation" in output.parents:
        parser.error("output must be inside the separate run workspace and outside migration_preparation")
    try:
        report = summarize(args)
    except (OSError, ValueError, TypeError, KeyError, IndexError) as exc:
        report = {"schema": 1, "status": "failed", "passed": False, "full_suite_gate_passed": False,
                  "no_optimization": True, "run_dir": str(run),
                  "verification_failures": [{"name": "summary inputs are valid", "passed": False, "error": "%s: %s" % (type(exc).__name__, exc)}]}
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".partial")
    temporary.write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n")
    temporary.replace(output)
    print(json.dumps({"passed": report["passed"], "output": str(output), "counts": report.get("counts"),
                      "verification_failures": report["verification_failures"]}, indent=2))
    return 1 if args.require_passed and not report["passed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
