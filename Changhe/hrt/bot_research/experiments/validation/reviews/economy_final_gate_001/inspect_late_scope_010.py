"""Bind the late notes and partition retained gate memberships by sampling stage."""
import json

from review_record_tools_004 import OUT, R, Evidence, normalize, rows, sha


def main(ev):
    raw = ev.capture(OUT / "final-gate-20261031T233546260787Z/inspection.json")
    ev.check(sha(raw) == "3c06e23be7a4944fd25b3a8b20c2820fbd1c3c4c826ebe69ac4f155979473c6e",
             "Completed final gate receipt identity")
    gate = json.loads(raw)
    read = ev.retained_map(
        OUT / "final-gate-20261031T233546260787Z/inputs.json",
        "31523d876f0443867d30fcbfab3620d77e9577811db92c207cab324d373c7b15",
    )
    base_raw = ev.capture(OUT / "historical-base-20261031T233659004971Z/inspection.json")
    ev.check(sha(base_raw) == "35e23b3fb1a0dfa03fc8df5ae2264c86ce7f68a0f05d4c9e0d4ab27a8403375a",
             "Verified historical base receipt identity")
    base_receipt = json.loads(base_raw)
    ev.check(not gate["problems"] and not base_receipt["problems"], "Prior audits passed")
    ev.capture(OUT / "FINAL_GATE_REVIEW_008.md")
    ev.capture(OUT / "afrr-20261031T233750162131Z/inspection.json")
    notes = ev.capture("bot_research/notes/economy.md").decode()
    (ev.phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
    joined = {(row["opponent"], row["scenario"], row["candidate_side"]): row
              for row in gate["joined_conditions"]}
    stages = {
        stage: {"memberships": 0, "keys": set(), "wdl": {tag: [0, 0, 0]
                                                       for tag in ("af5", "g1", "v29", "base")}}
        for stage in ("afs5", "afg5")
    }
    cache = {}
    for pool, references in gate["base_membership_refs"].items():
        for item in references:
            key, ref = tuple(item["condition"]), item["ref"]
            if ref["path"] not in cache:
                cache[ref["path"]] = rows(read(ref["path"]))
            candidate, actual, value = normalize(cache[ref["path"]][ref["line"] - 1])
            ev.check(actual == key and value is not None, "Retained base condition")
            row = joined[key]
            stage = row["refs"]["af5"]["run"]
            ev.check(stage in stages, "Declared af5 stage")
            summary = stages[stage]
            summary["memberships"] += 1
            summary["keys"].add(key)
            for tag, score in dict(
                {tag: row["values"][tag][0] for tag in ("af5", "g1", "v29")},
                base=value[0],
            ).items():
                summary["wdl"][tag][(1.0, .5, 0.0).index(score)] += 1
    output = {}
    for stage, row in stages.items():
        output[stage] = {
            "memberships": row["memberships"], "unique_conditions": len(row["keys"]),
            "exact_specs": len({key[0] for key in row["keys"]}), "wdl": row["wdl"],
        }
    ev.check(output["afs5"]["memberships"] == 296 and output["afg5"]["memberships"] == 550,
             "296 development and 550 post-selection memberships")
    status = {}
    for name, expected in (("afrep", 2), ("scnaf5", 120)):
        path = R / name / "results.jsonl"
        captured = ev.capture(path) if path.exists() else b""
        summary = path.parent / "summary.md"
        if summary.exists():
            ev.capture(summary)
        status[name] = {
            "rows": len(captured.splitlines()), "expected_rows": expected,
            "summary_exists": summary.exists(),
            "scope": "Dated status only; no numerical outcome reduction in this receipt",
        }
    return {
        "status": "SCOPE_REDUCTION_VERIFIED" if not ev.problems else "AUDIT_FINDINGS",
        "sampling_stage_partition": output, "later_run_status": status,
        "gate_scope": "The full gate remains selection-conditioned; 550 post-selection pool memberships represent 514 distinct conditions, and 296 sweep memberships represent 290 distinct conditions.",
        "afrep_scope": "The 18.33 prediction follows exposed afrr outcomes and is a reproduction prediction. A discrepancy alone does not isolate load as a cause.",
        "base_identity_scope": base_receipt["identity_scope"],
    }


if __name__ == "__main__":
    evidence = Evidence("late-scope", __file__)
    try:
        result = main(evidence)
    except Exception as error:
        evidence.check(False, type(error).__name__ + ": " + str(error))
        result = {"status": "INCOMPLETE_REVIEW", "error_type": type(error).__name__}
    print(json.dumps(evidence.seal(result) | {
        "status": result.get("status"), "partition": result.get("sampling_stage_partition"),
        "later_run_status": result.get("later_run_status"),
    }, indent=2))
