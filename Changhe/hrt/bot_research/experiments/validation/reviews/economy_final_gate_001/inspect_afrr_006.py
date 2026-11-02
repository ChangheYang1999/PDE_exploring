"""Review completed afrr and frozen fresh56 repeats; no project imports/calls.

Partial records are status-only unless an explicit retained stop record is
supplied. Partial hypotheses then remain OPEN, even when observed rows disagree.
"""
import argparse
import ast
import gzip
import json
from pathlib import Path
import re

from review_record_tools_004 import (
    E, R, OUT, Evidence, error_counts, normalize, now, relative, row_metadata_ok,
    rows, sha, specs, wdl,
)


def main(ev, stopped_evidence):
    prior = ev.retained_map(
        OUT / "fresh56-20261031T231428944261Z/inputs_relative_003.json",
        "e0ad62776109588ee5b2b1c5149553fc8467f9263780997cc8602cebbead1e27",
    )
    for path in (
        OUT / "FRESH56_REVIEW_003.md", OUT / "fresh56_review_manifest_003.json",
        OUT / "CHRONOLOGY_CLARIFICATION_001.md",
        OUT / "chronology_clarification_manifest_001.json",
        OUT / "fresh56-20261031T231428944261Z/scope_supplement.json",
        E / "run_tourn.sh",
    ):
        ev.capture(path)
    notes = ev.capture("bot_research/notes/economy.md").decode()
    (ev.phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
    candidate = prior(E / "specs/af5.spec").decode().strip()
    opponents = specs(prior(E / "opp_frr1.txt"))
    fresh = specs(prior(E / "opp_fresh56.txt"))
    ev.check(len(opponents) == len(set(opponents)) == 10, "Ten exact afrr specs")
    ev.check(Path(E / "opp_frr1.txt").read_bytes() == prior(E / "opp_frr1.txt"),
             "Current afrr list matches retained pre-statement")
    expected = {(o, None, side) for o in opponents for side in (0, 1)}
    raw = ev.capture(R / "afrr/results.jsonl")
    records = rows(raw)
    summary = R / "afrr/summary.md"
    if summary.exists():
        ev.capture(summary)
    log = ev.capture(R / "afrr.log").decode()
    completions = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", log)
    keys = [normalize(row)[1] for row in records if normalize(row)[0] == candidate]
    complete = (len(records) == len(keys) == len(expected) and set(keys) == expected
                and summary.exists() and len(completions) == 1)
    stop = None
    if stopped_evidence:
        path = relative(stopped_evidence)
        stop = {"path": str(path), "sha256": sha(ev.capture(path)),
                "scope": "Caller-supplied explicit stop evidence, not inferred from clock time"}
    status = {"observed_utc": now(), "rows": len(records), "expected": 20,
              "summary_exists": summary.exists(), "completion_lines": completions,
              "complete_condition_and_completion_evidence": complete, "stopped_evidence": stop}
    if not complete and stop is None:
        return {"status": "WAITING_FOR_COMPLETION_OR_EXPLICIT_STOP", "afrr": status,
                "numerical_reduction_performed": False, "hypotheses": None}
    table, refs = {}, {}
    for line, row in enumerate(records, 1):
        actual_candidate, key, value = normalize(row)
        ev.check(actual_candidate == candidate and key in expected and key not in table,
                 f"Exact candidate/unique expected condition {line}")
        ev.check(value is not None and row_metadata_ok(row)
                 and row.get("experiment") == "afrr", f"afrr metadata {line}")
        if value is not None:
            table[key], refs[key] = value, {"run": "afrr", "line": line}
    errors = error_counts(records)
    ev.check(not any(errors.values()), "afrr reported errors")
    afq = rows(prior(R / "afq56/results.jsonl"))
    afq_table, afq_refs = {}, {}
    for line, row in enumerate(afq, 1):
        actual_candidate, key, value = normalize(row)
        ev.check(actual_candidate == candidate and value is not None
                 and row_metadata_ok(row), "Prior afq56 metadata")
        ev.check(key not in afq_table, "Prior afq56 uniqueness")
        afq_table[key], afq_refs[key] = value, {"run": "afq56", "line": line}
    ev.check(len(afq) == 86 and set(afq_table) ==
             {(o, None, side) for o in fresh for side in (0, 1)}, "Prior afq56 complete")
    overlap = sorted(set(opponents) & set(fresh))
    ev.check(len(overlap) == 4, "Four exact afrr/fresh56 overlapping specs")
    repeated = []
    for opponent in overlap:
        for side in (0, 1):
            key = (opponent, None, side)
            repeated.append({
                "opponent": opponent, "candidate_side": side,
                "afq56": list(afq_table[key]), "afq56_ref": afq_refs[key],
                "afrr": list(table[key]) if key in table else None,
                "afrr_ref": refs.get(key),
                "same_outcome": table[key][0] == afq_table[key][0] if key in table else None,
                "same_outcome_margin_round": table[key] == afq_table[key] if key in table else None,
            })

    guard_path = Path("bot_research/bots/counters/early_wall_guard.py")
    guard_raw = prior(guard_path)
    ev.check(guard_path.read_bytes() == guard_raw, "Current guard source identity")
    tree = ast.parse(guard_raw)
    guard = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                 and node.name == "EarlyWallGuard")
    constructor = next(node for node in guard.body if isinstance(node, ast.FunctionDef)
                       and node.name == "__init__")
    default_map = dict(zip([arg.arg for arg in constructor.args.args][-len(constructor.args.defaults):],
                           [ast.literal_eval(value) for value in constructor.args.defaults]))
    make = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                and node.name == "make")
    returned = make.body[0].value if len(make.body) == 1 and isinstance(make.body[0], ast.Return) else None
    forwards = (isinstance(returned, ast.Attribute) and returned.attr == "decide"
                and isinstance(returned.value, ast.Call)
                and isinstance(returned.value.func, ast.Name)
                and returned.value.func.id == "EarlyWallGuard"
                and not returned.value.args and len(returned.value.keywords) == 1
                and returned.value.keywords[0].arg is None
                and isinstance(returned.value.keywords[0].value, ast.Name)
                and returned.value.keywords[0].value.id == make.args.kwarg.arg)
    ev.check(default_map.get("witness") == "guard00" and forwards,
             "guard00 default and kwargs-forwarding source premise")
    default_guard = "bot_research.bots.counters.early_wall_guard:@make"
    explicit_guard = default_guard + '?witness="guard00"'
    ev.check(default_guard in fresh and explicit_guard in opponents,
             "Guard exact specs establish different strings")
    alias_repeats = []
    for side in (0, 1):
        key, old_key = (explicit_guard, None, side), (default_guard, None, side)
        alias_repeats.append({
            "candidate_side": side, "prior_spec": default_guard, "new_spec": explicit_guard,
            "afq56": list(afq_table[old_key]), "afq56_ref": afq_refs[old_key],
            "afrr": list(table[key]) if key in table else None, "afrr_ref": refs.get(key),
            "same_outcome_margin_round": table[key] == afq_table[old_key] if key in table else None,
        })
    # Read the original partial object's bytes in place. Its original input map
    # binds the existing gzip object; no second copy or conflicting logical key.
    old_map_path = OUT / "inspection-20261031T225610458161Z/inputs.json"
    old_map_raw = ev.capture(old_map_path)
    ev.check(sha(old_map_raw) == "bc062c3fe55a54245fd583a21c0a37b60b23332b8c9c1aa25df6564d82fcffc0",
             "Prior partial input map identity")
    old_map = json.loads(old_map_raw)["inputs"]
    old_afq_pin = old_map[str(R / "afq56/results.jsonl")]
    packed = relative(old_afq_pin["snapshot"]).read_bytes()
    old_afq_raw = gzip.decompress(packed)
    ev.check(sha(packed) == old_afq_pin["gzip_sha256"]
             and sha(old_afq_raw) == old_afq_pin["sha256"]
             and len(old_afq_raw) == old_afq_pin["bytes"], "Prior partial archive verified")
    ev.check(prior(R / "afq56/results.jsonl").startswith(old_afq_raw),
             "Completed afq56 extends prior partial bytes")
    earlier_overlap = [{
        "line": line, "opponent": normalize(row)[1][0],
        "candidate_side": row["candidate_side"],
    } for line, row in enumerate(rows(old_afq_raw), 1) if normalize(row)[1][0] in overlap]
    gate_overlaps = {}
    for name in ("afsweep", "afagree"):
        pin = old_map[str(E / ("opp_" + name + ".txt"))]
        packed_list = relative(pin["snapshot"]).read_bytes()
        list_raw = gzip.decompress(packed_list)
        ev.check(sha(packed_list) == pin["gzip_sha256"]
                 and sha(list_raw) == pin["sha256"] and len(list_raw) == pin["bytes"],
                 "Frozen gate spec list " + name)
        gate_overlaps[name] = sorted(set(opponents) & set(specs(list_raw)))

    labels = ("guard00", "v41", "V29", "g1", "best_v9e", "AS1C",
              "best_v9f", "af2g", "v30", "threat_defender")
    by_label = dict(zip(labels, opponents))
    # These positions are authenticated by the exact frozen ten-spec input hash.
    ev.check(sha(prior(E / "opp_frr1.txt")) ==
             "3f7fb39b079a6e79eda9de459ae63e22602af3a0f6782cfad07d62615ae4b1d1",
             "Frozen ten-spec order identity")
    predictions = {}
    for label in ("best_v9e", "best_v9f", "af2g", "v30", "AS1C", "threat_defender"):
        observations = []
        for side in (0, 1):
            key = (by_label[label], None, side)
            value = table.get(key)
            matches = (value[0] == 1 if label == "threat_defender"
                       else value[0] == 0 and -20 <= value[1] <= -5 and value[2] == 50
                       ) if value is not None else None
            observations.append({"candidate_side": side, "value": list(value) if value else None,
                                 "matches_prediction": matches})
        predictions[label] = observations
    sources = ev.source_checks(records)
    stable = (R / "afrr/results.jsonl").read_bytes() == raw
    ev.check(stable, "afrr bytes changed during review")
    valid = not ev.problems
    prediction_a = all(row["matches_prediction"] for label in
                       ("best_v9e", "best_v9f", "af2g", "v30", "AS1C")
                       for row in predictions[label])
    prediction_b = all(row["matches_prediction"] for row in predictions["threat_defender"])
    per_opponent = [{
        "label": label, "opponent": opponent,
        "observations": [{"candidate_side": side,
                           "value": list(table[(opponent, None, side)])
                           if (opponent, None, side) in table else None,
                           "ref": refs.get((opponent, None, side))}
                          for side in (0, 1)],
    } for label, opponent in by_label.items()]
    maxima = max(enumerate(records, 1),
                 key=lambda item: item[1]["decide_max_seconds"][item[1]["candidate_side"]])
    max_row = maxima[1]
    return {
        "status": "COMPLETE_AFRR_REVIEW" if complete and valid else
                  "EXPLICITLY_STOPPED_PARTIAL_AFRR" if stop and valid else "AUDIT_FINDINGS",
        "audit_completed_without_findings": valid, "numerical_reduction_performed": True,
        "afrr": status, "candidate_spec": candidate, "errors": errors,
        "wdl": wdl(table, table), "per_opponent": per_opponent,
        "paired_outcome_margin_round_disagreements": [
            o for o in opponents if (o, None, 0) in table and (o, None, 1) in table
            and table[(o, None, 0)] != table[(o, None, 1)]],
        "exact_fresh56_repeats": repeated,
        "exact_repeat_count": {"specs": len(overlap), "conditions": 2 * len(overlap),
                               "same_complete_value": sum(row["same_outcome_margin_round"] is True
                                                          for row in repeated)},
        "source_parameter_alias": {
            "default_guard00_verified": default_map.get("witness") == "guard00",
            "make_forwards_kwargs_verified": forwards,
            "source_sha256": sha(guard_raw), "comparisons": alias_repeats,
            "scope": "Same source configuration, distinct exact spec strings and possible raw player names. No exhaustive semantic deduplication or deadline-independent whole-history equality claimed.",
        },
        "gate_exact_spec_overlaps": gate_overlaps,
        "hypotheses": {
            "H18_28a_on_completed_afrr": prediction_a if complete and valid else None,
            "H18_28b_on_completed_afrr": prediction_b if complete and valid else None,
            "per_condition": predictions,
            "historical_H18_28a": "Already refuted by the earlier completed afq56 af2g wins; afrr does not erase the earlier observation",
            "freshness": "Four exact fresh56 specs already played; default/explicit guard00 supplies a fifth source-configuration alias. Within H18.28a only default best_v9e and best_v9f are new exact targets here.",
        },
        "chronology": {
            "prior_partial_input_map": str(old_map_path),
            "prior_partial_afq56_archive": old_afq_pin,
            "prior_partial_archive_verified": True,
            "overlap_rows_present_in_prior_snapshot": earlier_overlap,
            "scope": "Pre-statement before afq56 completion is not proof it preceded all overlap observations. Data availability does not independently establish researcher knowledge. Preserve the earlier tie-break clarification.",
        },
        "repeat_scope": "Repeated observations are not independent strength samples. A discrepancy alone does not establish a causal load effect.",
        "sources": sources,
        "max_recorded_af5_call": {
            "seconds": max_row["decide_max_seconds"][max_row["candidate_side"]],
            "line": maxima[0], "condition": list(normalize(max_row)[1]),
            "clock": "Rounded elapsed wall seconds, not CPU or a three-second guarantee",
        },
        "recommendation_scope": "afrr is a separate descriptive/prediction/repeat review and does not alter the fixed af5 gate",
        "final_afrr_bytes_unchanged": stable,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stopped-evidence")
    args = parser.parse_args()
    evidence = Evidence("afrr", __file__)
    try:
        result = main(evidence, args.stopped_evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "hypotheses": None,
                  "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        "status": result.get("status"), "wdl": result.get("wdl"),
        "per_opponent": result.get("per_opponent"),
        "hypotheses": result.get("hypotheses"),
        "exact_repeat_count": result.get("exact_repeat_count"),
        "paired_disagreements": result.get("paired_outcome_margin_round_disagreements"),
    }, indent=2))
