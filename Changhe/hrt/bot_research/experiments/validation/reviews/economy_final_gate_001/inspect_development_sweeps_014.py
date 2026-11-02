"""Read completed or explicitly stopped afs4/afs3 development sweeps.

This module imports only the retained standard-library review helper. It never
imports, constructs or calls project policies or the Engine. No new game runs.
"""
import argparse
import collections
import json
from pathlib import Path
import re
import sys

from review_record_tools_004 import (
    E, R, OUT, Evidence, bootstrap, error_counts, normalize, now, relative,
    row_metadata_ok, rows, sha, specs, wdl,
)


def review(ev, run, stopped_evidence=None, afs4_input_map=None, afs4_input_map_sha=None,
           afs4_inspection_sha=None):
    tag = {"afs4": "af4", "afs3": "af3"}[run]
    old = ev.retained_map(
        OUT / "inspection-20261031T225610458161Z/inputs.json",
        "bc062c3fe55a54245fd583a21c0a37b60b23332b8c9c1aa25df6564d82fcffc0",
    )
    gate = ev.retained_map(
        OUT / "final-gate-20261031T233546260787Z/inputs.json",
        "31523d876f0443867d30fcbfab3620d77e9577811db92c207cab324d373c7b15",
    )
    gate_raw = ev.capture(OUT / "final-gate-20261031T233546260787Z/inspection.json")
    ev.check(sha(gate_raw) == "3c06e23be7a4944fd25b3a8b20c2820fbd1c3c4c826ebe69ac4f155979473c6e",
             "Completed gate008 receipt identity")
    gate_result = json.loads(gate_raw)
    ev.check(gate_result["audit_completed_without_findings"] and not gate_result["problems"],
             "Gate008 baseline validation succeeded")
    for path in (
        OUT / "FINAL_GATE_REVIEW_008.md", OUT / "CHRONOLOGY_CLARIFICATION_001.md",
        E / "pooltab.py", E / "run_tourn.sh",
    ):
        ev.capture(path)
    notes = ev.capture("bot_research/notes/economy.md").decode()
    ev.write("reviewed_notes.json", {"from_section": "18.31",
                                   "text": notes[notes.index("### 18.31"):]})
    candidate_specs = {name: old(E / "specs" / (name + ".spec")).decode().strip()
                       for name in ("af5", "af6", "g1", "v29")}
    candidate_specs[tag] = ev.capture(E / "specs" / (tag + ".spec")).decode().strip()
    ev.check(candidate_specs[tag] == candidate_specs["v29"] + "&attack_from=" + tag[-1],
             "Exact new candidate differs from V29 spec only by explicit attack_from")
    sweep = specs(old(E / "opp_afsweep.txt"))
    ev.check(ev.capture(E / "opp_afsweep.txt") == old(E / "opp_afsweep.txt"),
             "Current declared sweep list matches frozen selection list")
    pools = json.loads(old(E / "opp_afsweep_pools.json"))
    ev.check(len(sweep) == len(set(sweep)) == 145, "145 unique sweep opponent specs")
    ev.check(sum(map(len, pools.values())) == 145
             and {opponent for values in pools.values() for opponent in values} == set(sweep),
             "Disjoint145-spec descriptive pool partition")
    expected = {(opponent, None, side) for opponent in sweep for side in (0, 1)}
    path = R / run / "results.jsonl"
    if not path.exists():
        return {"status": "WAITING_FOR_RESULTS", "run": run, "numerical_reduction_performed": False}
    raw = ev.capture(path)
    current = rows(raw)
    summary = path.parent / "summary.md"
    if summary.exists():
        ev.capture(summary)
    log_path = R / (run + ".log")
    console = ev.capture(log_path).decode() if log_path.exists() else ""
    completions = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", console)
    actual = [normalize(row)[1] for row in current
              if normalize(row)[0] == candidate_specs[tag]]
    complete = (len(current) == len(actual) == len(expected) and set(actual) == expected
                and summary.exists() and len(completions) == 1)
    stop = None
    if stopped_evidence is not None:
        p = relative(stopped_evidence)
        stop = {"path": str(p), "sha256": sha(ev.capture(p)),
                "scope": "Explicit supplied stop evidence, not inferred from elapsed time"}
    status = {
        "observed_utc": now(), "rows": len(current), "expected_conditions": 290,
        "summary_exists": summary.exists(), "completion_lines": completions,
        "complete_condition_and_completion_evidence": complete, "stopped_evidence": stop,
    }
    if not complete and stop is None:
        return {"status": "WAITING_FOR_COMPLETION_OR_EXPLICIT_STOP", "run": run,
                "campaign_status": status, "numerical_reduction_performed": False,
                "H18_31b_candidate_component": None}
    tables = {name: {} for name in candidate_specs}
    refs = {name: {} for name in candidate_specs}
    selected_records, cache = [], {}

    def include(name, record, reference):
        candidate, key, value = normalize(record)
        ev.check(candidate == candidate_specs[name] and key in expected
                 and key not in tables[name] and value is not None,
                 "Exact unique candidate/condition " + name + "/" + str(reference))
        ev.check(row_metadata_ok(record), "Record metadata " + name + "/" + str(reference))
        selected_records.append(record)
        if value is not None:
            tables[name][key], refs[name][key] = value, reference
        return key, value

    gate_joins = [row for row in gate_result["joined_conditions"]
                  if (row["opponent"], row["scenario"], row["candidate_side"]) in expected]
    ev.check(len(gate_joins) == 290, "Exactly290 frozen gate joins in the sweep")
    for joined in gate_joins:
        key = (joined["opponent"], joined["scenario"], joined["candidate_side"])
        for name in ("af5", "g1", "v29"):
            ref = joined["refs"][name]
            baseline_path = R / ref["run"] / "results.jsonl"
            if str(baseline_path) not in cache:
                cache[str(baseline_path)] = rows(gate(baseline_path))
            record = cache[str(baseline_path)][ref["line"] - 1]
            found, value = include(name, record, {"path": str(baseline_path), "line": ref["line"]})
            ev.check(found == key and list(value) == joined["values"][name],
                     "Frozen raw baseline agrees with gate008 join " + name)
    for line, record in enumerate(rows(old(R / "afs6/results.jsonl")), 1):
        include("af6", record, {"path": str(R / "afs6/results.jsonl"), "line": line})
        ev.check(record.get("experiment") == "afs6", "af6 campaign metadata")
    if run == "afs3":
        if any(value is None for value in
               (afs4_input_map, afs4_input_map_sha, afs4_inspection_sha)):
            raise ValueError("afs3 requires the explicitly pinned completed afs4 input map and receipt")
        af4_map = relative(afs4_input_map)
        af4 = ev.retained_map(af4_map, afs4_input_map_sha)
        af4_receipt_raw = ev.capture(af4_map.parent / "inspection.json")
        ev.check(sha(af4_receipt_raw) == afs4_inspection_sha,
                 "Explicit af4 inspection receipt identity")
        af4_receipt = json.loads(af4_receipt_raw)
        ev.check(af4_receipt["run"] == "afs4"
                 and af4_receipt["audit_completed_without_findings"]
                 and af4_receipt["campaign_status"]["complete_condition_and_completion_evidence"],
                 "Completed af4 control receipt")
        candidate_specs["af4"] = af4(E / "specs/af4.spec").decode().strip()
        ev.check(candidate_specs["af4"] == candidate_specs["v29"] + "&attack_from=4",
                 "Exact retained af4 specification")
        tables["af4"], refs["af4"] = {}, {}
        for line, record in enumerate(rows(af4(R / "afs4/results.jsonl")), 1):
            include("af4", record, {"path": str(R / "afs4/results.jsonl"), "line": line})
            ev.check(record.get("experiment") == "afs4", "Retained af4 campaign metadata")
    for line, record in enumerate(current, 1):
        include(tag, record, {"path": str(path), "line": line})
        ev.check(record.get("experiment") == run, "New campaign metadata " + str(line))
    ev.check(all(set(table) == expected for name, table in tables.items() if name != tag),
             "Full exact290-condition coverage for every baseline")
    if complete:
        ev.check(set(tables[tag]) == expected, "Full exact290-condition new campaign")
    ev.check(set(tables[tag]) <= expected, "No outside condition in current campaign")
    covered = set(tables[tag]) & expected
    errors = error_counts(selected_records)
    ev.check(not any(errors.values()), "Reported errors, rejection or source changes")
    source_report = ev.source_checks(selected_records)
    pairs = {}
    for name in tables:
        if name == tag:
            continue
        pairs[name] = {
            "better_wdl": sum(tables[tag][key][0] > tables[name][key][0] for key in covered),
            "worse_wdl": sum(tables[tag][key][0] < tables[name][key][0] for key in covered),
            "equal_wdl": sum(tables[tag][key][0] == tables[name][key][0] for key in covered),
            "equal_wdl_hp_rounds": sum(tables[tag][key] == tables[name][key] for key in covered),
            "interval": bootstrap(covered, tables[tag], tables[name]) if covered else None,
        }
    pool_tables = {
        pool: {
            "specs": len(values), "expected_conditions": 2 * len(values),
            "covered_conditions": len(covered & {(o, None, side) for o in values for side in (0, 1)}),
            "wdl": {name: wdl(table, covered & {(o, None, side) for o in values for side in (0, 1)})
                    for name, table in tables.items()},
        } for pool, values in pools.items()
    }
    strike_keys = covered & {(o, None, side) for o in pools["strike1"] for side in (0, 1)}
    strike_interval = bootstrap(strike_keys, tables[tag], tables["af5"]) if strike_keys else None
    seat_differences = [{
        "opponent": opponent, "seat0": list(tables[tag][opponent, None, 0]),
        "seat1": list(tables[tag][opponent, None, 1]),
    } for opponent in sweep if all((opponent, None, side) in covered for side in (0, 1))
        and tables[tag][opponent, None, 0] != tables[tag][opponent, None, 1]]
    maximum = max(enumerate(current, 1),
                  key=lambda item: item[1]["decide_max_seconds"][item[1]["candidate_side"]],
                  default=None)
    stamps = sorted({match.group(1) for row in current if row.get("log")
                     for match in [re.search(r"/(\d{8}T\d{6})-", row["log"])] if match})
    stable = path.read_bytes() == raw
    ev.check(stable, "Current campaign bytes changed during review")
    valid = not ev.problems
    new_wdl = wdl(tables[tag], covered)
    combined = None
    if complete and valid and run == "afs3":
        combined = new_wdl[0] < 264 and wdl(tables["af4"], expected)[0] < 264
    return {
        "status": "COMPLETED_DEVELOPMENT_SWEEP" if complete and valid else
                  "EXPLICITLY_STOPPED_PARTIAL_DEVELOPMENT_SWEEP" if stop and valid else "AUDIT_FINDINGS",
        "run": run, "candidate": tag, "audit_completed_without_findings": valid,
        "numerical_reduction_performed": True, "campaign_status": status,
        "specs": candidate_specs, "exact_sweep_specs": sweep,
        "selected_candidate_baseline_records": len(selected_records),
        "covered_conditions": len(covered),
        "covered_complete_seat_pairs": sum(all((opponent, None, side) in covered
                                              for side in (0, 1)) for opponent in sweep),
        "wdl": {name: wdl(table, covered) for name, table in tables.items()},
        "pool_tables": pool_tables, "paired_comparisons": pairs,
        "strike1_candidate_minus_af5_interval": strike_interval,
        "paired_seat_value_differences": seat_differences,
        "joined_conditions": [{
            "opponent": key[0], "scenario": key[1], "candidate_side": key[2],
            "values": {name: list(table[key]) for name, table in tables.items()},
            "refs": {name: refs[name][key] for name in tables},
        } for key in sorted(covered)],
        "errors": errors, "sources": source_report,
        "H18_31b_candidate_component": new_wdl[0] < 264 if complete and valid else None,
        "H18_31b_combined_af4_and_af3": combined,
        "verified_partial_refutation_by_at_least264_wins": new_wdl[0] >= 264 if valid else None,
        "max_candidate_call": {
            "line": maximum[0], "candidate_side": maximum[1]["candidate_side"],
            "seconds": maximum[1]["decide_max_seconds"][maximum[1]["candidate_side"]],
            "condition": list(normalize(maximum[1])[1]),
        } if maximum else None,
        "retained_log_name_campaign_stamps": stamps,
        "time_scope": "Rounded elapsed wall call and console campaign durations; path timestamps are retained labels, not continuous runtime monitoring or causal load identification",
        "bootstrap_scope": "Declared pooltab.py descriptive paired score bootstrap: W=1,D=0.5,L=0; exact opponent-spec clusters preserve observed seat rows, including both seats for every spec in a complete sweep;4000 resamples,Random(1),sorted samples100 and3899. A stopped partial sweep uses only its observed conditions. Sweep selection and correlated parameter families preclude an unrestricted fresh-population inference.",
        "selection_scope": "Development only on145 specs selected for V29/g1 disagreement. No held-out af4/af3 check; neither changes the selected af5 gate, its separate95percent prediction or installation.",
        "final_result_bytes_unchanged": stable,
        "python_version": sys.version,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", choices=("afs4", "afs3"), required=True)
    parser.add_argument("--stopped-evidence")
    parser.add_argument("--afs4-input-map")
    parser.add_argument("--afs4-input-map-sha")
    parser.add_argument("--afs4-inspection-sha")
    args = parser.parse_args()
    evidence = Evidence("development-" + args.run, __file__)
    try:
        for arg in (args.stopped_evidence, args.afs4_input_map):
            if arg is not None:
                relative(arg)
        evidence.write("invocation.json", {"reader": str(relative(__file__)),
                                          "reader_sha256": sha(Path(__file__).read_bytes()),
                                          "arguments": vars(args)})
        result = review(evidence, args.run, args.stopped_evidence,
                        args.afs4_input_map, args.afs4_input_map_sha,
                        args.afs4_inspection_sha)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "run": args.run,
                  "H18_31b_candidate_component": None, "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        key: result.get(key) for key in (
            "status", "run", "campaign_status", "wdl", "paired_comparisons",
            "strike1_candidate_minus_af5_interval", "H18_31b_candidate_component",
            "H18_31b_combined_af4_and_af3", "max_candidate_call")
    }, indent=2))
