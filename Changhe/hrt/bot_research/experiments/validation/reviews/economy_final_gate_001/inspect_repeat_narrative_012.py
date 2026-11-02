"""Review retained repeat logs and the dated economy18.34 prose, without replay."""
import gzip
import json
from pathlib import Path

from review_record_tools_004 import OUT, R, Evidence, rows, sha


def main(ev):
    capture = json.loads(ev.capture(OUT / "repeat_notes_capture_012.json"))
    packed = ev.capture(capture["snapshot"])
    notes = gzip.decompress(packed)
    ev.check(sha(packed) == capture["gzip_sha256"]
             and sha(notes) == capture["sha256"]
             and len(notes) == capture["bytes"], "Dated notes archive identity")
    text = notes.decode()
    section = text[text.index("### 18.34"):]
    ev.write("reviewed_section.json", {
        "source_path": capture["path"], "source_sha256": capture["sha256"],
        "source_observed_utc": capture["observed_utc"], "text": section,
    })
    old = ev.retained_map(
        OUT / "afrr-20261031T233750162131Z/inputs.json",
        "00e25bf0757561eab6b8f36eed90b35a8a947e2df558de5acdc6f747fe1d49b8",
    )
    repeat = ev.retained_map(
        OUT / "afrep-20261031T234033189508Z/inputs.json",
        "0ba2effbde74fd5b016995da2b772f060be88bb2b6e77233f3e8b8deff3ca5dd",
    )
    original = rows(old(R / "afrr/results.jsonl"))
    repeated = rows(repeat(R / "afrep/results.jsonl"))
    lead_path = Path("bot_research/runs/lead/frr1/results.jsonl")
    lead = rows(ev.capture(lead_path))
    afrr, afrep, g1 = original[8], repeated[0], lead[11]
    af5_spec = afrr["spec_a"]
    best_spec = "bot_research.experiments.lead.frozen.best_v9e:@make"
    ev.check(afrr["candidate_side"] == afrep["candidate_side"] == 0
             and af5_spec == afrep["spec_a"] and afrr["spec_b"] == afrep["spec_b"] == best_spec,
             "Both af5 seat-zero repeat controls")
    ev.check(g1["spec_a"] == af5_spec.replace("attack_from=5", "attack_from=7")
             and g1["spec_b"] == best_spec, "Exact frr1 g1 control specs")
    selected = {"afrr": afrr, "afrep": afrep, "g1": g1}
    logs, indexes, identities = {}, {}, {}
    for label, record in selected.items():
        raw = repeat(record["log"]) if label == "afrep" else ev.capture(record["log"])
        stream = rows(raw)
        ev.check(len(stream) == 102, "Full 102-line retained log " + label)
        index = {(entry["round"], entry["player"]): entry for entry in stream}
        ev.check(len(index) == 102
                 and set(index) == {(turn, side) for turn in range(51) for side in (0, 1)},
                 "Unique complete log rounds " + label)
        for (turn, side), entry in index.items():
            ev.check(entry["snapshot"]["name"] == record["spec_a" if side == 0 else "spec_b"],
                     "Log name and record binding " + label)
            if turn == 0:
                ev.check(entry["match"]["research_specs"] == [record["spec_a"], record["spec_b"]]
                         and entry["match"]["research_scenario"] is None
                         and entry["match"]["research_metadata"] == record["metadata"],
                         "Initial log metadata binding " + label)
            if turn == 50:
                for key in ("hp", "gold", "n_factories", "n_turrets", "n_walls", "length_path"):
                    ev.check(entry["snapshot"][key] == record["players"][side][key],
                             "Terminal log and result " + label + "/" + key)
        logs[label], indexes[label] = stream, index
        identities[label] = {"path": record["log"], "sha256": sha(raw), "rows": len(stream)}

    def public(entry):
        snapshot = {key: value for key, value in entry["snapshot"].items() if key != "name"}
        return {"round": entry["round"], "player": entry["player"],
                "event": entry["event"], "snapshot": snapshot}

    repetition = [{
        "round": key[0], "player": key[1],
        "event_equal": indexes["afrr"][key]["event"] == indexes["afrep"][key]["event"],
        "snapshot_equal": indexes["afrr"][key]["snapshot"] == indexes["afrep"][key]["snapshot"],
    } for key in sorted(indexes["afrr"])]
    opening = [{
        "round": turn, "player": side,
        "events_and_name_normalized_snapshots_equal":
            public(indexes["afrr"][turn, side]) == public(indexes["g1"][turn, side]),
    } for turn in range(5) for side in (0, 1)]
    chronology = {}
    for label, index in indexes.items():
        chronology[label] = [{
            "round": turn,
            "hp": [index[turn, side]["snapshot"]["hp"] for side in (0, 1)],
            "actions": [[event["action"] for event in index[turn, side]["event"]
                         if event["kind"] == "action"] for side in (0, 1)],
            "combat": [[event for event in index[turn, side]["event"]
                        if event["kind"] == "combat"] for side in (0, 1)],
        } for turn in range(1, 11)]
    max_line, max_row = max(enumerate(original, 1),
                           key=lambda item: item[1]["decide_max_seconds"][item[1]["candidate_side"]])
    actual_max = max_row["decide_max_seconds"][max_row["candidate_side"]]
    sources = ev.source_checks(list(selected.values()))
    return {
        "audit_completed_without_findings": not ev.problems,
        "dated_notes_source": capture,
        "narrative_issue": {
            "quoted_runtime_sentence_fragment": "largest decide call of af5 0.8 s",
            "fragment_present_in_archived_notes": "largest decide call of af5 0.8 s" in section,
            "actual_max_af5_elapsed_wall_seconds": actual_max,
            "result_path": str(R / "afrr/results.jsonl"),
            "result_line": max_line, "candidate_side": max_row["candidate_side"],
            "both_physical_seat_maxima": max_row["decide_max_seconds"],
            "claim_matches_records": actual_max <= 0.8,
        },
        "retained_log_identities": identities,
        "afrr_afrep_comparisons": repetition,
        "all_102_events_and_snapshots_equal":
            all(row["event_equal"] and row["snapshot_equal"] for row in repetition),
        "af5_g1_first_four_rounds": opening,
        "all_first_four_events_and_name_normalized_snapshots_equal":
            all(row["events_and_name_normalized_snapshots_equal"] for row in opening),
        "first_ten_round_chronology": chronology,
        "sources": sources,
        "claim_scope": (
            "Retained JSON event/snapshot comparisons and receipt-bound source identities only; "
            "no Engine replay, policy regeneration, private-decision or causal load inference. "
            "The 0.8 s statement is compared to rounded elapsed wall measurements."
        ),
    }


if __name__ == "__main__":
    evidence = Evidence("repeat-narrative", __file__)
    try:
        result = main(evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"audit_completed_without_findings": False, "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        key: result.get(key) for key in (
            "narrative_issue", "all_102_events_and_snapshots_equal",
            "all_first_four_events_and_name_normalized_snapshots_equal")
    }, indent=2))
