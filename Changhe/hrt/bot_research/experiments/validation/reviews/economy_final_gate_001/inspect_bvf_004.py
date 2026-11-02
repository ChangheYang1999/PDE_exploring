"""Review completed bvf against the sealed fresh56 records; no project imports."""
import json
from pathlib import Path
import re
from review_record_tools_004 import (
    E, R, OUT, Evidence, bootstrap, error_counts, normalize, now, row_metadata_ok,
    rows, sha, specs, wdl,
)

ev = Evidence("bvf", __file__)
prior = ev.retained_map(
    OUT / "fresh56-20261031T231428944261Z/inputs_relative_003.json",
    "e0ad62776109588ee5b2b1c5149553fc8467f9263780997cc8602cebbead1e27",
)
for path in (
    OUT / "FRESH56_REVIEW_003.md", OUT / "fresh56_review_manifest_003.json",
    OUT / "CHRONOLOGY_CLARIFICATION_001.md",
    E / "pooltab.py", E / "run_tourn.sh",
    Path("bot_research/harness/match.py"),
    Path("bot_research/harness/tournament.py"),
):
    ev.capture(path)
notes = ev.capture("bot_research/notes/economy.md").decode()
(ev.phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
fresh = specs(prior(E / "opp_fresh56.txt"))
fresh5, fresh6 = (specs(prior(E / ("opp_" + name + ".txt")))
                  for name in ("fresh5", "fresh6"))
pools = json.loads(prior(E / "opp_fresh56_pools.json"))
ev.check(len(fresh) == len(set(fresh)) == 43 and fresh == fresh5 + fresh6,
         "Exact 43-spec fresh56 concatenation")
ev.check(set(pools) == set(fresh), "Pool map coverage")
for path in (E / "opp_fresh56.txt", E / "opp_fresh56_pools.json"):
    ev.check(Path(path).read_bytes() == prior(path), "Current list/pool identity " + str(path))
candidate_specs = {tag: prior(E / "specs" / (tag + ".spec")).decode().strip()
                   for tag in ("af5", "g1", "v29")}
candidate_specs["best_v9e"] = "bot_research.experiments.lead.frozen.best_v9e:@make"
tables = {tag: {} for tag in candidate_specs}
refs = {tag: {} for tag in candidate_specs}
allrows = {}
for run, tags in (("afq56", ("af5",)), ("fresh5a", ("g1", "v29")),
                  ("fresh6", ("g1", "v29"))):
    records = rows(prior(R / run / "results.jsonl"))
    allrows[run] = records
    for line, row in enumerate(records, 1):
        candidate, key, value = normalize(row)
        for tag in tags:
            if candidate == candidate_specs[tag]:
                ev.check(value is not None and row_metadata_ok(row),
                         f"Retained metadata {run}:{line}")
                ev.check(key not in tables[tag], "Duplicate retained condition " + tag)
                tables[tag][key] = value
                refs[tag][key] = {"run": run, "line": line}

bvf = rows(ev.capture(R / "bvf/results.jsonl"))
allrows["bvf"] = bvf
summary = R / "bvf/summary.md"
summary_exists = summary.exists()
if summary_exists:
    ev.capture(summary)
log = ev.capture(R / "bvf.log").decode()
completions = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", log)
errors = error_counts(bvf)
ev.check(summary_exists and len(completions) == 1, "bvf completion evidence")
ev.check(not any(errors.values()), "bvf reported errors")
for line, row in enumerate(bvf, 1):
    candidate, key, value = normalize(row)
    ev.check(candidate == candidate_specs["best_v9e"], "Exact bvf candidate")
    ev.check(value is not None and row_metadata_ok(row)
             and row.get("experiment") == "bvf", f"bvf metadata {line}")
    ev.check(key not in tables["best_v9e"], "Duplicate bvf condition")
    tables["best_v9e"][key] = value
    refs["best_v9e"][key] = {"run": "bvf", "line": line}
keys = {(opponent, None, side) for opponent in fresh for side in (0, 1)}
ev.check(len(bvf) == 86, "bvf row count")
ev.check(all(set(table) == keys for table in tables.values()), "Exact four-way condition join")
ev.check(all(len(set(pools[o]) & {"LEAD", "W1_FORTRESS", "W3_COUNTERS"}) == 1
             for o in fresh), "Disjoint family assignment")
ev.check(all(("NOT_BUILT_AGAINST" in pools[o]) ==
             bool(set(pools[o]) & {"LEAD", "W1_FORTRESS"}) for o in fresh),
         "LEAD_PLUS_FORTRESS provenance union")
family_tables = {}
for family in ("ALL", "LEAD", "W1_FORTRESS", "W3_COUNTERS",
               "LEAD_PLUS_FORTRESS", "fresh5", "fresh6"):
    if family == "ALL":
        selected = fresh
    elif family == "fresh5":
        selected = fresh5
    elif family == "fresh6":
        selected = fresh6
    elif family == "LEAD_PLUS_FORTRESS":
        selected = [o for o in fresh if set(pools[o]) & {"LEAD", "W1_FORTRESS"}]
    else:
        selected = [o for o in fresh if family in pools[o]]
    selected_keys = {(o, None, side) for o in selected for side in (0, 1)}
    if not all(selected_keys <= set(table) for table in tables.values()):
        continue
    family_tables[family] = {
        "opponents": len(selected), "conditions": len(selected_keys),
        "wdl": {tag: wdl(table, selected_keys) for tag, table in tables.items()},
        "paired": {tag + "-best_v9e": bootstrap(selected_keys, tables[tag],
                                               tables["best_v9e"])
                   for tag in ("af5", "g1", "v29")},
    }
source_checks = ev.source_checks(bvf)
joined = [{"opponent": key[0], "scenario": key[1], "candidate_side": key[2],
           "values": {tag: list(table[key]) for tag, table in tables.items()},
           "refs": {tag: refs[tag][key] for tag in tables}} for key in sorted(keys)]
paired = {tag: [o for o in fresh if table[(o, None, 0)] != table[(o, None, 1)]]
          for tag, table in tables.items()}
maxima = {}
for which in ("candidate", "opponent", "either"):
    possibilities = []
    for line, row in enumerate(bvf, 1):
        sides = (row["candidate_side"],) if which == "candidate" else (
            1 - row["candidate_side"],) if which == "opponent" else (0, 1)
        possibilities.extend((row["decide_max_seconds"][side], line, side, row)
                             for side in sides)
    seconds, line, side, row = max(possibilities, key=lambda x: x[0])
    maxima[which] = {"seconds": seconds, "line": line, "physical_side": side,
                     "spec": row["spec_a"] if side == 0 else row["spec_b"],
                     "candidate_side": row["candidate_side"],
                     "clock": "Recorded rounded time.perf_counter elapsed wall seconds"}

partial = {}
for run, expected in (("afg5", 514), ("afrr", 20)):
    path, summary = R / run / "results.jsonl", R / run / "summary.md"
    raw = path.read_bytes() if path.exists() else b""
    partial[run] = {"observed_utc": now(), "rows": len(raw.splitlines()),
                    "expected": expected, "results_sha256_at_observation": sha(raw),
                    "summary_exists": summary.exists(),
                    "scope": "Status-only byte/count observation, no outcome reduction; raw partial bytes not duplicated"}
valid = not ev.problems
interval = family_tables["ALL"]["paired"]["g1-best_v9e"]
result = {
    "audit_completed_without_findings": valid,
    "specs": candidate_specs, "joined_conditions": joined, "family_tables": family_tables,
    "bvf": {"rows": len(bvf), "summary_exists": summary_exists,
            "completion_lines": completions, "errors": errors,
            "complete_exact_condition_set": valid},
    "paired_outcome_margin_round_disagreements": paired,
    "bvf_losses": [row for row in joined if row["values"]["best_v9e"][0] == 0],
    "max_recorded_call": maxima, "sources": source_checks,
    "H18_20": {"criterion": "g1 minus best_v9e paired interval upper endpoint >= 0",
               "not_falsified_on_this_list": interval["hi"] >= 0 if valid else None,
               "interval": interval, "superiority_not_established": interval["lo"] <= 0},
    "af5_vs_best_v9e_scope": "Descriptive comparison; no prospective prediction stated",
    "family_scope": "LEAD_PLUS_FORTRESS is non-W3 provenance, not proof of development against neither bot or an unbiased opponent sample",
    "followup_status_only": partial,
    "af5_recommendation": "OPEN until completed or explicitly stopped afg5 covered-pool reduction; H18.20 is a separate comparison",
    "chronology": "Prior clarification retained: rule/code reportedly preceded first partial-row test; independent stronger ordering not established. Existing afrr overlap availability does not establish researcher knowledge; a repeat discrepancy alone does not establish a causal load effect.",
}
print(json.dumps(ev.seal(result) | {"families": family_tables, "maxima": maxima,
                                   "partial": partial}, indent=2))
