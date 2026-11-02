"""Read the completed 120-condition scnaf5 control, never execute policies.

This is separate from the standard-start gate. A documented stopped run may be
reviewed as partial; matching observed rows never establishes all120 equality.
"""
import argparse
import json
from pathlib import Path
import re

from review_record_tools_004 import (
    E, R, OUT, Evidence, error_counts, normalize, now, relative, row_metadata_ok,
    rows, sha, specs, wdl,
)

SCENARIOS = (
    "mirror:51:2", "asym:52:2", "mirror:53:3", "asym:54:3", "asym:55:2", "mirror:56:3",
    "mirror:61:2", "asym:62:2", "mirror:63:3", "asym:64:3", "asym:65:2", "mirror:66:3",
)
OPPONENTS = (
    'bot_research.bots.counters.pool:@archetype?name="eco6_t5"',
    "bot_research.bots.economy.frozen.lead_best_b.best:@make",
    "bot_research.bots.economy.frozen.lead_best_a.best:@make",
    "bot_research.bots.economy.frozen.v2.econ:@make?late_round=6&phi=0.0",
    "bot_research.bots.economy.frozen.lead_v4.v4:@make",
)


def main(ev, stopped_evidence):
    prior = ev.retained_map(
        OUT / "fresh56-20261031T231428944261Z/inputs_relative_003.json",
        "e0ad62776109588ee5b2b1c5149553fc8467f9263780997cc8602cebbead1e27",
    )
    candidate_specs = {tag: prior(E / "specs" / (tag + ".spec")).decode().strip()
                       for tag in ("af5", "g1", "v29")}
    for path in (OUT / "FRESH56_REVIEW_003.md",
                 OUT / "CHRONOLOGY_CLARIFICATION_001.md",
                 E / "run_tourn.sh", E / "pair_diff.py",
                 Path("bot_research/harness/scenarios.py")):
        ev.capture(path)
    notes = ev.capture("bot_research/notes/economy.md").decode()
    (ev.phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
    opponents = specs(ev.capture(E / "opp_clockfree5.txt"))
    ev.check(tuple(opponents) == OPPONENTS, "Exact ordered five-opponent control")
    heldout3 = specs(ev.capture(E / "opp_heldout3.txt"))
    ev.check(set(opponents) <= set(heldout3), "Five specs belong to held-out3 opponent list")
    expected = {(opponent, scenario, side) for opponent in opponents
                for scenario in SCENARIOS for side in (0, 1)}
    path = R / "scnaf5/results.jsonl"
    if not path.exists():
        return {"status": "WAITING_FOR_SCNAF5", "numerical_reduction_performed": False,
                "H18_31a": None, "observed_utc": now()}
    raw = ev.capture(path)
    current = rows(raw)
    summary = R / "scnaf5/summary.md"
    if summary.exists():
        ev.capture(summary)
    log_path = R / "scnaf5.log"
    log = ev.capture(log_path).decode() if log_path.exists() else ""
    completions = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", log)
    actual = [normalize(row)[1] for row in current
              if normalize(row)[0] == candidate_specs["af5"]]
    complete = (len(current) == len(actual) == len(expected) and set(actual) == expected
                and summary.exists() and len(completions) == 1)
    stop = None
    if stopped_evidence:
        p = relative(stopped_evidence)
        stop = {"path": str(p), "sha256": sha(ev.capture(p)),
                "scope": "Caller-supplied explicit stop evidence, not inferred from time"}
    status = {"observed_utc": now(), "rows": len(current), "expected": 120,
              "summary_exists": summary.exists(), "completion_lines": completions,
              "complete_condition_and_completion_evidence": complete, "stopped_evidence": stop}
    if not complete and stop is None:
        return {"status": "WAITING_FOR_COMPLETION_OR_EXPLICIT_STOP",
                "scnaf5": status, "numerical_reduction_performed": False, "H18_31a": None}
    tables = {tag: {} for tag in candidate_specs}
    refs = {tag: {} for tag in candidate_specs}
    selected_rows, run_status = [], {}
    for run, tag, scenarios in (
        ("hs3", "v29", set(SCENARIOS[:6])),
        ("hs4", "v29", set(SCENARIOS[6:])),
        ("hs34g1", "g1", set(SCENARIOS)),
        ("scnaf5", "af5", set(SCENARIOS)),
    ):
        records = current if run == "scnaf5" else rows(ev.capture(R / run / "results.jsonl"))
        if run != "scnaf5":
            ev.capture(R / run / "summary.md")
        matches = []
        for line, row in enumerate(records, 1):
            candidate, key, value = normalize(row)
            if candidate != candidate_specs[tag] or key[0] not in opponents:
                if run == "scnaf5":
                    ev.check(False, f"Unexpected scnaf5 candidate/opponent {line}")
                continue
            matches.append(key)
            selected_rows.append(row)
            ev.check(key in expected and key[1] in scenarios and key not in tables[tag],
                     f"Expected unique scenario key {run}:{line}")
            ev.check(value is not None and row_metadata_ok(row)
                     and row.get("experiment") == run, f"Scenario metadata {run}:{line}")
            if value is not None:
                tables[tag][key], refs[tag][key] = value, {"run": run, "line": line}
        target = {(o, scenario, side) for o in opponents for scenario in scenarios
                  for side in (0, 1)}
        if run != "scnaf5" or complete:
            ev.check(len(matches) == len(target) and set(matches) == target,
                     "Complete matching baseline/candidate subset " + run)
        run_status[run] = {"all_rows_in_file": len(records),
                           "matching_control_rows": len(matches),
                           "expected_control_rows": len(target)}
    errors = error_counts(selected_rows)
    ev.check(not any(errors.values()), "Selected scenario rows report errors")
    ev.check(all(set(tables[tag]) == expected for tag in ("g1", "v29")),
             "Full two-baseline 120-condition coverage")
    source_checks = ev.source_checks(selected_rows)
    covered = expected & set(tables["af5"]) & set(tables["g1"]) & set(tables["v29"])
    joined = [{
        "opponent": key[0], "scenario": key[1], "candidate_side": key[2],
        "values": {tag: list(values[key]) for tag, values in tables.items()},
        "refs": {tag: refs[tag][key] for tag in tables},
        "af5_matches_v29": tables["af5"][key] == tables["v29"][key],
        "g1_matches_v29": tables["g1"][key] == tables["v29"][key],
    } for key in sorted(covered)]
    differences = [row for row in joined if not row["af5_matches_v29"]]
    baseline_differences = [{
        "condition": list(key), "g1": list(tables["g1"][key]), "v29": list(tables["v29"][key]),
    } for key in sorted(expected) if tables["g1"][key] != tables["v29"][key]]
    by_scenario = {scenario: {
        "expected_conditions": 10,
        "covered_conditions": sum(key[1] == scenario for key in covered),
        "wdl": {tag: wdl(values, {key for key in covered if key[1] == scenario})
                for tag, values in tables.items()},
        "af5_value_differences": sum(row["scenario"] == scenario for row in differences),
    } for scenario in SCENARIOS}
    stable = path.read_bytes() == raw
    ev.check(stable, "scnaf5 bytes changed during review")
    valid = not ev.problems
    observed_refutation = bool(differences) if valid else None
    hypothesis = not differences if complete and valid else None
    maxima = max(enumerate(current, 1),
                 key=lambda item: item[1]["decide_max_seconds"][item[1]["candidate_side"]],
                 default=None)
    return {
        "status": "COMPLETE_SCENARIO_REVIEW" if complete and valid else
                  "EXPLICITLY_STOPPED_PARTIAL_SCENARIO_REVIEW" if stop and valid else "AUDIT_FINDINGS",
        "audit_completed_without_findings": valid, "numerical_reduction_performed": True,
        "scnaf5": status, "specs": candidate_specs, "opponents": opponents,
        "scenarios": list(SCENARIOS), "run_subsets": run_status, "errors": errors,
        "joined_conditions": joined, "covered_conditions": len(covered),
        "differences": differences, "g1_v29_baseline_differences": baseline_differences,
        "wdl": {tag: wdl(values, covered) for tag, values in tables.items()},
        "by_scenario": by_scenario, "sources": source_checks,
        "H18_31a": hypothesis, "verified_observed_counterexample": observed_refutation,
        "equality_scope": "Equality means recorded winner, normalized HP margin and round count only; no claim of complete action-history equality or arbitrary scenario transfer",
        "recommendation_scope": (
            "The stated scenario condition restricts any af5 recommendation to standard starts"
            if observed_refutation else
            "All declared120 finite scenario comparisons match; no unrestricted scenario or runtime guarantee"
            if hypothesis is True else
            "Incomplete or unauthenticated evidence leaves all120 equality OPEN"
        ),
        "clock_free_list_label": "The exact five-spec list and recorded source identities are checked; the list label does not establish a universal absence of time dependence in all surrounding runtime behavior",
        "max_recorded_af5_call": {
            "seconds": maxima[1]["decide_max_seconds"][maxima[1]["candidate_side"]],
            "line": maxima[0], "condition": list(normalize(maxima[1])[1]),
            "clock": "Rounded elapsed wall time, not CPU time or a three-second guarantee",
        } if maxima is not None else None,
        "standard_gate_separation": "This control adds a scenario-scope qualification; afs4/afs3 development outcomes do not retune or replace the fixed af5 gate",
        "final_scnaf5_bytes_unchanged": stable,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stopped-evidence")
    args = parser.parse_args()
    evidence = Evidence("scenario-control", __file__)
    try:
        result = main(evidence, args.stopped_evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "H18_31a": None,
                  "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        "status": result.get("status"), "scnaf5": result.get("scnaf5"),
        "H18_31a": result.get("H18_31a"), "wdl": result.get("wdl"),
        "difference_count": len(result.get("differences", [])),
        "baseline_difference_count": len(result.get("g1_v29_baseline_differences", [])),
        "recommendation_scope": result.get("recommendation_scope"),
    }, indent=2))
