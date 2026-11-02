"""Authenticate currently present original afrr logs without executing a replay."""
from datetime import datetime, timezone
import json
from pathlib import Path

from review_record_tools_004 import OUT, R, Evidence, rows, sha


def main(ev):
    map_path = OUT / "afrr-20261031T233750162131Z/inputs.json"
    previous_map = json.loads(ev.capture(map_path))
    retained = ev.retained_map(
        map_path, "00e25bf0757561eab6b8f36eed90b35a8a947e2df558de5acdc6f747fe1d49b8"
    )
    for path in (OUT / "AFRR_REVIEW_006.md", OUT / "AFREP_REVIEW_011.md",
                 OUT / "REPEAT_NARRATIVE_REVIEW_012.md"):
        ev.capture(path)
    records = rows(retained(R / "afrr/results.jsonl"))
    ev.check(len(records) == 20, "Twenty original afrr records")
    source_path = Path("bot_research/harness/tournament.py")
    source = ev.capture(source_path)
    ev.capture("bot_research/experiments/economy/run_tourn.sh")
    source_old_pin = previous_map["inputs"].get(str(source_path))
    if source_old_pin:
        ev.check(source_old_pin["sha256"] == sha(source), "Tournament source matches006 captured bytes")
    parsed, log_report = 0, []
    for line, record in enumerate(records, 1):
        path = record.get("log")
        ev.check(bool(path), "Original result contains log path " + str(line))
        if not path:
            continue
        p = Path(path)
        present = p.is_file()
        ev.check(present, "Original log currently exists " + str(line))
        if not present:
            log_report.append({"result_line": line, "path": path, "currently_exists": False})
            continue
        stat = p.stat()
        raw = ev.capture(p)
        stream = rows(raw)
        index = {(entry["round"], entry["player"]): entry for entry in stream}
        expected = {(turn, side) for turn in range(record["rounds"] + 1) for side in (0, 1)}
        ev.check(len(stream) == len(index) == len(expected) and set(index) == expected,
                 "Complete unique round/seat structure " + str(line))
        for (turn, side), entry in index.items():
            ev.check(entry["schema_version"] == 1
                     and entry["snapshot"]["name"] == record["spec_a" if side == 0 else "spec_b"],
                     "Log schema and player binding " + str(line))
            if turn == 0:
                ev.check(entry["match"]["research_specs"] == [record["spec_a"], record["spec_b"]]
                         and entry["match"]["research_scenario"] is None
                         and entry["match"]["research_metadata"] == record["metadata"],
                         "Initial log/result metadata " + str(line))
            if turn == record["rounds"]:
                for key in ("hp", "gold", "n_factories", "n_turrets", "n_walls", "length_path"):
                    ev.check(entry["snapshot"][key] == record["players"][side][key],
                             "Terminal log/result " + str(line) + "/" + key)
        ev.check(p.read_bytes() == raw, "Log bytes stable across current capture " + str(line))
        parsed += len(stream)
        log_report.append({
            "result_line": line, "path": path, "currently_exists": True,
            "sha256": sha(raw), "bytes": len(raw), "log_rows": len(stream),
            "candidate_won": record["winner"] == record["candidate_side"],
            "candidate_side": record["candidate_side"],
            "filesystem_mtime_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            "mtime_scope": "Observed metadata only; not proof of past presence or past-byte identity",
        })
    text = source.decode()
    source_checks = {
        "single_standard_scenario_in_all_records": all(row.get("scenario") is None for row in records),
        "first_of_pair_assigned_by_first_scenario":
            '"first_of_pair": scenario == scenarios[0]' in text,
        "losses_deletes_win_only_if_not_first":
            'keep == "losses" and cand_won and not task.get("first_of_pair")' in text,
    }
    ev.check(all(source_checks.values()), "Inspected retention predicates")
    return {
        "audit_completed_without_findings": not ev.problems,
        "original_records": len(records), "logs": log_report, "total_parsed_log_rows": parsed,
        "currently_present_logs": sum(row["currently_exists"] for row in log_report),
        "winning_logs": sum(row.get("candidate_won", False) for row in log_report),
        "source_retention_checks": source_checks,
        "tournament_source_sha256": sha(source),
        "tournament_source_in_previous006_input_map": source_old_pin,
        "prior006_history_log_input_keys":
            [key for key in previous_map["inputs"] if "/afrr/logs/" in key],
        "previous_scope": (
            "006 captured the afrr result table and console completion log, not original game logs. "
            "Its repeat comparisons concerned outcome, margin and rounds and did not establish log absence. "
            "011 authenticated the two afrep histories.012 additionally authenticated original afrr game9."
        ),
        "retention_explanation": (
            "The source marks both seats first_of_pair whenever their scenario is the first scenario. "
            "All afrr records use its sole standard scenario, so the losses-mode deletion predicate "
            "does not delete any of these winning logs. The default shell value alone cannot infer "
            "the launch environment, but no such inference is needed to explain retention."
        ),
        "scope_limitation": (
            "Current retained-byte log existence, source and metadata authentication only. "
            "No backdated assertion of006 log examination, continuous presence, Engine replay, "
            "policy regeneration or complete-history transfer to other campaigns."
        ),
    }


if __name__ == "__main__":
    evidence = Evidence("original-repeat-logs", __file__)
    try:
        result = main(evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"audit_completed_without_findings": False, "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        key: result.get(key) for key in (
            "currently_present_logs", "winning_logs", "total_parsed_log_rows",
            "prior006_history_log_input_keys", "source_retention_checks")
    }, indent=2))
