"""Read two completed afrep records and retained logs, with no policy or Engine calls."""
import json
from pathlib import Path
import re

from review_record_tools_004 import (
    OUT, R, E, Evidence, error_counts, normalize, row_metadata_ok, rows, sha, specs,
)


def main(ev):
    old_read = ev.retained_map(
        OUT / "afrr-20261031T233750162131Z/inputs.json",
        "00e25bf0757561eab6b8f36eed90b35a8a947e2df558de5acdc6f747fe1d49b8",
    )
    old_result = ev.capture(OUT / "afrr-20261031T233750162131Z/inspection.json")
    ev.check(sha(old_result) == "6659ba2e0bb9a8c7ac693b1898099a34b9c9d2899f66cb57deb1d63e9112aa43",
             "Completed afrr receipt identity")
    old = json.loads(old_result)
    ev.check(not old["problems"] and old["audit_completed_without_findings"], "afrr audit passed")
    candidate = old["candidate_spec"]
    opponent = "bot_research.experiments.lead.frozen.best_v9e:@make"
    ev.check(specs(ev.capture(E / "opp_bv9e.txt")) == [opponent], "Exact singleton opponent list")
    notes = ev.capture("bot_research/notes/economy.md").decode()
    (ev.phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
    path = R / "afrep/results.jsonl"
    if not path.exists():
        return {"status": "WAITING_FOR_AFREP", "numerical_reduction_performed": False}
    raw = ev.capture(path)
    records = rows(raw)
    summary = path.parent / "summary.md"
    if summary.exists():
        ev.capture(summary)
    logpath = R / "afrep.log"
    log = ev.capture(logpath).decode() if logpath.exists() else ""
    completion = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", log)
    actual = [normalize(row) for row in records]
    expected = {(opponent, None, side) for side in (0, 1)}
    complete = len(records) == 2 and {key for _, key, _ in actual} == expected
    complete = complete and summary.exists() and len(completion) == 1
    if not complete:
        return {"status": "WAITING_FOR_COMPLETED_AFREP", "rows": len(records),
                "summary_exists": summary.exists(), "completion_lines": completion,
                "numerical_reduction_performed": False, "H18_33": None}
    baseline = {}
    for row in rows(old_read(R / "afrr/results.jsonl")):
        tag, key, value = normalize(row)
        if tag == candidate and key in expected:
            ev.check(key not in baseline, "Unique original afrr control")
            baseline[key] = value
    ev.check(set(baseline) == expected, "Both exact afrr controls")
    errors = error_counts(records)
    ev.check(not any(errors.values()), "afrep reported errors")
    comparisons, log_summaries = [], []
    for line, row in enumerate(records, 1):
        tag, key, value = normalize(row)
        side = row["candidate_side"]
        ev.check(tag == candidate and value is not None and row_metadata_ok(row)
                 and row["experiment"] == "afrep", "Exact afrep metadata")
        comparisons.append({
            "candidate_side": side, "afrr": list(baseline[key]),
            "afrep": list(value), "same_outcome_margin_round": value == baseline[key],
            "matches_H18_33": value == (1.0, 410, 50),
            "afrep_line": line,
        })
        log_raw = ev.capture(row["log"])
        stream = rows(log_raw)
        snapshots, changes, actions = {}, [], []
        ev.check(len(stream) == 2 * (row["rounds"] + 1), "Exact retained log row count")
        for index, entry in enumerate(stream, 1):
            turn, player = entry["round"], entry["player"]
            ev.check(type(turn) is int and type(player) is int and player in (0, 1)
                     and 0 <= turn <= row["rounds"] and (turn, player) not in snapshots,
                     "Unique expected retained log round/seat")
            ev.check(entry["schema_version"] == 1
                     and entry["snapshot"]["name"] == row["spec_a" if player == 0 else "spec_b"],
                     "Retained log schema and player binding")
            snapshots[turn, player] = entry["snapshot"]
            role = "af5" if player == side else "best_v9e"
            if turn == 0:
                match = entry["match"]
                ev.check(match["research_specs"] == [row["spec_a"], row["spec_b"]]
                         and match["research_scenario"] is None
                         and match["research_metadata"] == row["metadata"],
                         "Initial log match binding")
                continue
            previous = snapshots[turn - 1, player]
            combat = [event for event in entry["event"] if event["kind"] == "combat"]
            ev.check(len(combat) == 1, "One recorded combat summary per round/player")
            combat = combat[0]
            if previous["hp"] != entry["snapshot"]["hp"] or combat["damage_dealt"] or combat["base_damage"]:
                changes.append({
                    "round": turn, "role": role, "player": player, "log_line": index,
                    "hp_before": previous["hp"], "hp_after": entry["snapshot"]["hp"],
                    "combat": combat,
                })
            for event in entry["event"]:
                if event["kind"] == "action":
                    ev.check(event["accepted"] is True, "No rejected action in retained log")
                    if event["action"]["op"] == "buy_minion":
                        actions.append({"round": turn, "role": role,
                                        "action": event["action"], "log_line": index})
        ev.check(set(snapshots) == {(turn, player) for turn in range(row["rounds"] + 1)
                                   for player in (0, 1)}, "Full retained snapshot coverage")
        terminal = []
        for player in (0, 1):
            last = snapshots[row["rounds"], player]
            for name in ("hp", "gold", "n_factories", "n_turrets", "n_walls", "length_path"):
                ev.check(last[name] == row["players"][player][name], "Log/result terminal " + name)
            ev.check(last["hp"] == row["hp_a" if player == 0 else "hp_b"],
                     "Final HP metadata binding")
            terminal.append({"role": "af5" if player == side else "best_v9e",
                             "snapshot": last})
        log_summaries.append({
            "candidate_side": side, "path": row["log"], "sha256": sha(log_raw),
            "rows": len(stream), "HP_or_combat_changes": changes,
            "minion_purchase_events": actions, "terminal": terminal,
        })
    source_report = ev.source_checks(records)
    ev.check(path.read_bytes() == raw, "Completed afrep bytes unchanged")
    valid = not ev.problems
    return {
        "status": "COMPLETE_AFREP_REVIEW" if valid else "AUDIT_FINDINGS",
        "audit_completed_without_findings": valid, "numerical_reduction_performed": True,
        "complete_records": len(records), "completion_lines": completion,
        "errors": errors, "comparisons": comparisons, "logs": log_summaries,
        "H18_33": all(item["matches_H18_33"] for item in comparisons) if valid else None,
        "sources": source_report,
        "recorded_max_af5_call_seconds": max(row["decide_max_seconds"][row["candidate_side"]]
                                           for row in records),
        "recorded_max_best_v9e_call_seconds": max(row["decide_max_seconds"][1-row["candidate_side"]]
                                                for row in records),
        "clock_scope": "Rounded elapsed wall time, not CPU time or a runtime bound",
        "log_scope": "Retained log structure, names/specs, terminal metadata and recorded HP/combat chronology only; no Engine replay, policy regeneration or private-decision explanation",
        "causal_scope": "This prediction follows exposed afrr outcomes. Reproduction is not fresh strength evidence, and a discrepancy alone would not establish load as a cause.",
        "recommendation_scope": "Separate repeat control; no retuning of the completed standard-start gate",
    }


if __name__ == "__main__":
    evidence = Evidence("afrep", __file__)
    try:
        result = main(evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "H18_33": None,
                  "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        "status": result.get("status"), "H18_33": result.get("H18_33"),
        "comparisons": result.get("comparisons"),
        "logs": [{key: row[key] for key in ("candidate_side", "rows", "HP_or_combat_changes")}
                 for row in result.get("logs", [])],
        "max_af5": result.get("recorded_max_af5_call_seconds"),
        "max_best_v9e": result.get("recorded_max_best_v9e_call_seconds"),
    }, indent=2))
