"""Read completed afg5 plus frozen afs5 and baseline records. No project imports.

Default refuses a partial numerical reduction. After an explicitly documented
stop, --stopped-evidence RELATIVE_FILE permits a clearly partial covered-set
reduction; it never converts the 514-condition prediction into a completed test.
"""
import argparse
import ast
import collections
import json
from pathlib import Path
import re

from review_record_tools_004 import (
    E, R, OUT, Evidence, error_counts, normalize, now, relative, row_metadata_ok,
    rows, sha, specs, wdl,
)


def source_literals(raw):
    """Read the static string/list definitions; never execute the source."""
    env = {}

    def literal(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return env[node.id]
        if isinstance(node, ast.List):
            return [literal(value) for value in node.elts]
        if isinstance(node, ast.Tuple):
            return tuple(literal(value) for value in node.elts)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return literal(node.left) + literal(node.right)
        raise ValueError("Unsupported source literal")
    for node in ast.parse(raw).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in {"L", "T", "E", "GATE", "RUNS"}:
                env[target.id] = literal(node.value)
    return env


def main(ev, stopped_evidence):
    ev.capture(OUT / "inspect_final_gate_005.py")
    ev.capture(OUT / "final-gate-20261031T233508049026Z/inspection.json")
    ev.capture(OUT / "final-gate-20261031T233508049026Z/inputs.json")
    old = ev.retained_map(
        OUT / "inspection-20261031T225610458161Z/inputs.json",
        "bc062c3fe55a54245fd583a21c0a37b60b23332b8c9c1aa25df6564d82fcffc0",
    )
    old_keys = json.loads(ev.capture(
        OUT / "inspection-20261031T225610458161Z/inputs.json"))["inputs"]
    fresh = ev.retained_map(
        OUT / "fresh56-20261031T231428944261Z/inputs_relative_003.json",
        "e0ad62776109588ee5b2b1c5149553fc8467f9263780997cc8602cebbead1e27",
    )
    for path in (
        OUT / "INTERIM_REVIEW.md", OUT / "interim_manifest.json",
        OUT / "CHRONOLOGY_CLARIFICATION_001.md",
        OUT / "chronology_clarification_manifest_001.json",
        OUT / "FRESH56_REVIEW_003.md", OUT / "fresh56_review_manifest_003.json",
        E / "dec22.py", E / "run_tourn.sh",
    ):
        ev.capture(path)
    notes = ev.capture("bot_research/notes/economy.md").decode()
    (ev.phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
    candidate_specs = {tag: old(E / "specs" / (tag + ".spec")).decode().strip()
                       for tag in ("af5", "g1", "v29")}
    sweep, agree = (specs(old(E / ("opp_" + name + ".txt")))
                    for name in ("afsweep", "afagree"))
    sweep_pools = json.loads(old(E / "opp_afsweep_pools.json"))
    ev.check(len(sweep) == len(set(sweep)) == 145, "145 unique sweep specs")
    ev.check(len(agree) == len(set(agree)) == 257, "257 unique remaining specs")
    ev.check(not set(sweep) & set(agree), "Sweep and remainder are disjoint")
    sweep_keys = {(o, None, side) for o in sweep for side in (0, 1)}
    agree_keys = {(o, None, side) for o in agree for side in (0, 1)}

    raw = ev.capture(R / "afg5/results.jsonl")
    current_rows = rows(raw)
    summary = R / "afg5/summary.md"
    if summary.exists():
        ev.capture(summary)
    log = ev.capture(R / "afg5.log").decode()
    completions = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", log)
    actual_keys = [normalize(row)[1] for row in current_rows
                   if normalize(row)[0] == candidate_specs["af5"]]
    complete = (len(current_rows) == len(actual_keys) == len(agree_keys)
                and set(actual_keys) == agree_keys
                and summary.exists() and len(completions) == 1)
    stop = None
    if stopped_evidence:
        path = relative(stopped_evidence)
        stop = {"path": str(path), "sha256": sha(ev.capture(path)),
                "scope": "Caller-supplied explicit stop evidence; reviewed by the author, not inferred from elapsed time"}
    status = {"rows": len(current_rows), "expected": 514, "summary_exists": summary.exists(),
              "completion_lines": completions, "complete_condition_and_completion_evidence": complete,
              "stopped_evidence": stop, "observed_utc": now()}
    if not complete and stop is None:
        return {"status": "WAITING_FOR_COMPLETION_OR_EXPLICIT_STOP",
                "afg5": status, "numerical_reduction_performed": False,
                "recommendation": None, "agreement_prediction": None}

    gate_source = old(E / "gate_vs_base.py")
    current_gate_source = Path(E / "gate_vs_base.py").read_bytes()
    ev.check(current_gate_source == gate_source, "Gate source unchanged from frozen interim")
    definitions = source_literals(gate_source)
    gate = definitions["GATE"]
    ev.check(len(gate) == 14, "Fourteen named gate pools")
    pool_keys, membership_refs, base_conflicts = {}, {}, []
    for name, path, substring, expected in gate:
        records = rows(old(path))
        table, refs = {}, {}
        for line, row in enumerate(records, 1):
            candidate, key, value = normalize(row)
            if substring not in candidate or "catch_up_share=1.0" in candidate or value is None:
                continue
            if key in table and table[key] != value:
                base_conflicts.append({"pool": name, "condition": list(key),
                                       "first": refs[key], "second_line": line})
            table[key] = value
            refs[key] = {"path": path, "line": line}
        ev.check(len(table) == expected, "Pool membership count " + name)
        pool_keys[name] = set(table)
        membership_refs[name] = refs
    union = set().union(*pool_keys.values())
    ev.check(not base_conflicts, "Conflicting duplicate base membership records")
    ev.check(union == sweep_keys | agree_keys, "Gate equals sweep plus remainder")
    ev.check(len(union) == 804 and len({key[0] for key in union}) == 402,
             "804 unique conditions and 402 exact specs")
    ev.check(sum(map(len, pool_keys.values())) == 846, "846 pool memberships")
    ev.check(all(key[1] is None and key[2] in (0, 1) for key in union),
             "Only standard scenario and both physical seats")
    ev.check({o for values in sweep_pools.values() for o in values} == set(sweep),
             "Frozen sweep pool mapping")

    tables = {tag: {} for tag in candidate_specs}
    refs = {tag: {} for tag in candidate_specs}
    duplicates, conflicts, baseline_rows, baseline_runs = [], [], [], {}
    # Every run named by the reviewed economy gate reducer is inspected. Only
    # exact g1/V29 candidates on the gate union contribute baseline values.
    for run in definitions["RUNS"]:
        path = R / run / "results.jsonl"
        if run in ("afs5", "afg5", "afs6", "afq56"):
            continue
        if str(path) in old_keys:
            records = rows(old(path))
            provenance = "Frozen interim input bytes"
        elif path.exists():
            records = rows(ev.capture(path))
            provenance = "Captured current bytes for an additional named baseline run"
        else:
            baseline_runs[run] = {"present": False, "matching_gate_rows": 0}
            continue
        matched = 0
        for line, row in enumerate(records, 1):
            candidate, key, value = normalize(row)
            tags = [tag for tag in ("g1", "v29") if candidate == candidate_specs[tag]]
            if not tags or key not in union:
                continue
            tag = tags[0]
            matched += 1
            baseline_rows.append(row)
            ev.check(value is not None and row_metadata_ok(row),
                     f"Baseline metadata {run}:{line}")
            if value is None:
                continue
            ref = {"run": run, "line": line}
            if key in tables[tag]:
                record = {"tag": tag, "condition": list(key), "first": refs[tag][key],
                          "second": ref, "first_value": list(tables[tag][key]),
                          "second_value": list(value)}
                (duplicates if tables[tag][key] == value else conflicts).append(record)
            else:
                tables[tag][key], refs[tag][key] = value, ref
        baseline_runs[run] = {"present": True, "matching_gate_rows": matched,
                              "source": provenance}
    ev.check(not conflicts, "Conflicting baseline observations")
    ev.check(all(set(tables[tag]) == union for tag in ("g1", "v29")),
             "Full g1/V29 baseline coverage")
    shared_baseline_diff = [list(key) for key in sorted(agree_keys)
                            if key not in tables["g1"] or key not in tables["v29"]
                            or tables["g1"][key][0] != tables["v29"][key][0]]
    ev.check(not shared_baseline_diff, "All 514 remainder baseline WDL values agree")

    candidate_rows, candidate_status = [], {}
    for run, expected, records in (
        ("afs5", sweep_keys, rows(old(R / "afs5/results.jsonl"))),
        ("afg5", agree_keys, current_rows),
    ):
        keys = []
        candidate_rows.extend(records)
        for line, row in enumerate(records, 1):
            candidate, key, value = normalize(row)
            ev.check(candidate == candidate_specs["af5"], "Exact af5 spec " + run)
            ev.check(value is not None and row_metadata_ok(row)
                     and row.get("experiment") == run, f"Candidate metadata {run}:{line}")
            ev.check(key in expected and key not in tables["af5"],
                     f"Candidate unexpected or duplicate condition {run}:{line}")
            if value is not None:
                tables["af5"][key] = value
                refs["af5"][key] = {"run": run, "line": line}
                keys.append(key)
        errors = error_counts(records)
        ev.check(not any(errors.values()), "Candidate reported errors " + run)
        ev.check(len(keys) == len(set(keys)), "Candidate uniqueness " + run)
        if run == "afs5" or complete:
            ev.check(set(keys) == expected and len(records) == len(expected),
                     "Complete candidate condition coverage " + run)
        candidate_status[run] = {"rows": len(records), "successful_unique_conditions": len(set(keys)),
                                 "expected": len(expected), "errors": errors}
    ev.check(not any(error_counts(baseline_rows).values()), "Baseline reported errors")
    covered = union & set(tables["af5"])
    ev.check(sweep_keys <= covered, "Complete frozen sweep contribution")
    if complete:
        ev.check(covered == union, "Full final gate coverage")

    def table(keys):
        selected = set(keys) & covered & set(tables["g1"]) & set(tables["v29"])
        return {
            "expected_conditions": len(keys), "covered_conditions": len(selected),
            "covered_specs": len({key[0] for key in selected}),
            "wdl": {tag: wdl(values, selected) for tag, values in tables.items()},
            "af5_minus_g1_wins": wdl(tables["af5"], selected)[0] - wdl(tables["g1"], selected)[0],
            "paired_counts_to_g1": {
                "better": sum(tables["af5"][key][0] > tables["g1"][key][0] for key in selected),
                "worse": sum(tables["af5"][key][0] < tables["g1"][key][0] for key in selected),
                "same_outcome": sum(tables["af5"][key][0] == tables["g1"][key][0] for key in selected),
                "same_outcome_other_margin": sum(tables["af5"][key][0] == tables["g1"][key][0]
                                                 and tables["af5"][key][1] != tables["g1"][key][1]
                                                 for key in selected),
            },
            "conditions": [list(key) for key in sorted(selected)],
        }
    pool_tables = {pool: table(keys) for pool, keys in pool_keys.items()}
    unique_table = table(union)
    remaining_table = table(agree_keys)
    unique_membership = collections.Counter(key for values in pool_keys.values() for key in values)
    joined = [{
        "opponent": key[0], "scenario": key[1], "candidate_side": key[2],
        "pool_memberships": [pool for pool, values in pool_keys.items() if key in values],
        "values": {tag: list(values[key]) for tag, values in tables.items()},
        "refs": {tag: refs[tag][key] for tag in tables},
    } for key in sorted(covered) if all(key in values for values in tables.values())]
    remaining_covered = agree_keys & covered
    changed = [list(key) for key in sorted(remaining_covered)
               if tables["af5"][key][0] != tables["g1"][key][0]]
    pairs = {tag: [opponent for opponent in sorted({key[0] for key in covered})
                   if (opponent, None, 0) in covered and (opponent, None, 1) in covered
                   and values[(opponent, None, 0)] != values[(opponent, None, 1)]]
             for tag, values in tables.items()}
    source_checks = ev.source_checks(candidate_rows + baseline_rows)
    fresh_result_path = OUT / "fresh56-20261031T231428944261Z/inspection.json"
    fresh_raw = ev.capture(fresh_result_path)
    ev.check(sha(fresh_raw) == "354dcf82b613116d5d7c6d97ece32071b660c773a0016be7c0d8d6a30e637e32",
             "Completed fresh56 numerical receipt identity")
    fresh_result = json.loads(fresh_raw)
    ev.check(not fresh_result["problems"]
             and fresh_result["gate_18_22"]["completed_afq56_verified"],
             "Completed fresh56 gate authenticated")
    # The archived result bytes and relative map are bound; no repeated fresh56
    # bootstrap or sweep-selection calculation is necessary for this extension.
    fresh(R / "afq56/results.jsonl")
    initial_path = OUT / "inspection-20261031T225610458161Z/inspection.json"
    initial_raw = ev.capture(initial_path)
    ev.check(sha(initial_raw) == "5cc12012e159a33e7f4fb3302ada1d6ec9ed70ba5dfe1610ca3749a7d71573da",
             "Frozen selection receipt identity")
    initial = json.loads(initial_raw)
    ev.check(initial["selection"]["choice"] == "af5", "Prior af5 selection")
    worst_delta = min(row["af5_minus_g1_wins"] for row in pool_tables.values())
    valid = not ev.problems
    gate_pass = worst_delta >= -2 if valid else None
    fresh_pass = fresh_result["gate_18_22"]["passes"] if valid else None
    max_row = max(enumerate(candidate_rows, 1),
                  key=lambda item: item[1]["decide_max_seconds"][item[1]["candidate_side"]])
    max_seconds = max_row[1]["decide_max_seconds"][max_row[1]["candidate_side"]]
    final_stable = (R / "afg5/results.jsonl").read_bytes() == raw
    ev.check(final_stable, "afg5 bytes changed during review")
    if not final_stable:
        valid = False
        gate_pass = fresh_pass = None
    return {
        "status": "COMPLETE_GATE_REVIEW" if complete and valid else
                  "EXPLICITLY_STOPPED_PARTIAL_COVERAGE" if stop and valid else "AUDIT_FINDINGS",
        "audit_completed_without_findings": valid,
        "numerical_reduction_performed": True, "afg5": status,
        "specs": candidate_specs, "candidate_runs": candidate_status,
        "baseline_runs": baseline_runs, "baseline_duplicate_rows": duplicates,
        "baseline_conflicts": conflicts, "base_membership_conflicts": base_conflicts,
        "base_membership_refs": {pool: [{"condition": list(key), "ref": refs[key]}
                                      for key in sorted(refs)]
                                 for pool, refs in membership_refs.items()},
        "denominators": {
            "sweep_specs": len(sweep), "remaining_specs": len(agree),
            "unique_gate_specs": len({key[0] for key in union}),
            "unique_gate_conditions": len(union),
            "pool_membership_conditions": sum(map(len, pool_keys.values())),
            "excess_pool_memberships": sum(map(len, pool_keys.values())) - len(union),
            "multiplicity_histogram": dict(collections.Counter(unique_membership.values())),
            "covered_unique_conditions": len(covered),
            "covered_pool_memberships": sum(len(values & covered) for values in pool_keys.values()),
        },
        "pool_tables": pool_tables, "unique_gate": unique_table,
        "remaining_gate": remaining_table, "joined_conditions": joined,
        "paired_outcome_margin_round_disagreements": pairs,
        "remaining_baseline_outcome_disagreements": shared_baseline_diff,
        "agreement_prediction": {
            "criterion": "At least 95 percent of all 514 remainder conditions agree in WDL with the common g1/V29 outcome",
            "observed_conditions": len(remaining_covered), "changed_outcomes": len(changed),
            "changed_conditions": changed, "minimum_agreements_if_complete": 489,
            "maximum_differences_if_complete": 25,
            "passes": len(changed) <= 25 if complete and valid else None,
            "scope": "Separate prediction; not a recommendation gate; incomplete coverage leaves it OPEN",
        },
        "recommendation": {
            "gate_18_22": fresh_pass, "gate_18_26": gate_pass,
            "criterion_18_26": "On each named R13 pool within jointly covered conditions, af5 has at most two fewer wins than g1",
            "worst_pool_win_delta": worst_delta,
            "qualifies_under_stated_rule": bool(fresh_pass and gate_pass) if valid else None,
            "coverage": "All 804 exact conditions" if complete else "Explicitly stopped covered subset only",
            "scope": "Selection-conditioned R13 gate plus separate43-spec fresh56 condition; no unconditional deployment, runtime or global-strength conclusion",
        },
        "sources": source_checks,
        "max_recorded_af5_call_seconds": max_seconds,
        "max_call_row": {"combined_afs5_then_afg5_line": max_row[0],
                         "run": max_row[1].get("experiment"),
                         "condition": list(normalize(max_row[1])[1]),
                         "clock": "Rounded elapsed wall seconds, not CPU time or a three-second guarantee"},
        "reader_amendment": {
            "supersedes_reader": "inspect_final_gate_005.py",
            "prior_reader_sha256": "86807838829d57fa68f93d8436b5047c6233eb94ea78def9d331eea62205fc32",
            "prior_incomplete_result_sha256": "3c46d67f51c56a3d0148f990fa2798358f6c21766f076462e759aef5551da65f",
            "change": "Exclude afq56 from the exact g1/V29 baseline scan, alongside afs5/afg5/afs6; afq56 contains af5 records only and is authenticated separately through the completed fresh56 map",
            "reason": "The frozen partial afq56 input and completed afq56 input share a logical path and the archive helper correctly refused to replace one version silently",
            "scope": "No gate, selection, source identity, candidate record or numerical criterion changed; prior incomplete receipt and all archives retained"
        },
        "chronology": "Frozen selection and clarification preserved; no stronger tie-break ordering inferred. Agreement pre-statement and recommendation gate are distinct.",
        "other_experiments": "afrr repeat review and scnaf5 scenario control remain separate; afs4/afs3 are development and do not retune this af5 gate",
        "final_afg5_bytes_unchanged": final_stable,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stopped-evidence")
    args = parser.parse_args()
    evidence = Evidence("final-gate", __file__)
    try:
        result = main(evidence, args.stopped_evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "recommendation": None,
                  "agreement_prediction": None, "error_type": type(error).__name__}
    receipt = evidence.seal(result)
    print(json.dumps(receipt | {
        "status": result.get("status"),
        "denominators": result.get("denominators"),
        "recommendation": result.get("recommendation"),
        "agreement_prediction": result.get("agreement_prediction"),
        "pool_wdl": {pool: {"conditions": row["covered_conditions"], "wdl": row["wdl"],
                             "af5_minus_g1_wins": row["af5_minus_g1_wins"]}
                     for pool, row in result.get("pool_tables", {}).items()},
    }, indent=2))
