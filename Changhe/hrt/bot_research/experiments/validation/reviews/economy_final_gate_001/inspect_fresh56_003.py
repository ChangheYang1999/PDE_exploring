"""Read completed fresh56 evidence, without importing project code.

This supplementary review does not rerun sweep reductions or inspect partial
follow-up outcomes. All input bytes used for reductions are retained losslessly.
"""
import ast
import collections
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import random
import re

OUT = Path("bot_research/experiments/validation/reviews/economy_final_gate_001")
E = Path("bot_research/experiments/economy")
R = Path("bot_research/runs/economy")


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


started = now()
phase = OUT / ("fresh56-" + started.replace(":", "").replace("-", "").replace(".", ""))
phase.mkdir(exist_ok=False)
objects = OUT / "inputs"
pins, captured, problems = {}, {}, []


def capture(path):
    path = Path(path)
    project_root = Path.cwd()
    path = (path if path.is_absolute() else project_root / path).relative_to(project_root)
    if ".." in path.parts:
        raise ValueError("Input path leaves the project root")
    key = str(path)
    if key not in captured:
        when = now()
        raw = path.read_bytes()
        digest = sha(raw)
        target = objects / (digest + ".gz")
        if not target.exists():
            target.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
        packed = target.read_bytes()
        if gzip.decompress(packed) != raw:
            raise ValueError("Snapshot mismatch: " + key)
        pins[key] = {
            "captured_utc": when, "sha256": digest, "bytes": len(raw),
            "snapshot": str(target), "gzip_sha256": sha(packed),
        }
        captured[key] = raw
    return captured[key]


def check(condition, message):
    if not condition:
        problems.append(message)


def text(path):
    return capture(path).decode()


def specs_file(path):
    return [s.strip() for s in text(path).splitlines() if s.strip() and not s.startswith("#")]


def rows_file(path):
    rows, bad = [], []
    for i, line in enumerate(capture(path).splitlines(), 1):
        try:
            rows.append(json.loads(line))
        except Exception as error:
            bad.append({"line": i, "error": type(error).__name__})
    return rows, bad


def normalize(row):
    side = row["candidate_side"]
    candidate = row["spec_a"] if side == 0 else row["spec_b"]
    opponent = row["spec_b"] if side == 0 else row["spec_a"]
    key = (opponent, row.get("scenario"), side)
    if row.get("error"):
        return candidate, key, None
    score = 1.0 if row["winner"] == side else .5 if row["winner"] is None else 0.0
    margin = row["hp_diff_a"] * (1 if side == 0 else -1)
    return candidate, key, (score, margin, row["rounds"])


def wdl(values):
    scores = [value[0] for value in values]
    return [scores.count(score) for score in (1.0, .5, 0.0)]


def bootstrap(keys, a, b):
    opponents = sorted({key[0] for key in keys})
    by = collections.defaultdict(list)
    for key in sorted(keys):
        by[key[0]].append(a[key][0] - b[key][0])
    mean = sum(sum(by[opponent]) for opponent in opponents) / len(keys)
    rng = random.Random(1)
    samples = []
    for _ in range(4000):
        sample = [rng.choice(opponents) for _ in opponents]
        samples.append(sum(sum(by[o]) for o in sample) / sum(len(by[o]) for o in sample))
    samples.sort()
    return {
        "mean": mean, "lo": samples[100], "hi": samples[3899],
        "opponents": len(opponents), "conditions": len(keys),
        "resamples": 4000, "seed": 1, "sorted_indices": [100, 3899],
    }


for path in (
    OUT / "INTERIM_REVIEW.md", OUT / "interim_manifest.json",
    OUT / "CHRONOLOGY_CLARIFICATION_001.md",
    OUT / "chronology_clarification_manifest_001.json",
    E / "dec22.py", E / "pooltab.py", E / "run_tourn.sh",
    Path("bot_research/harness/match.py"),
    Path("bot_research/harness/tournament.py"),
    R / "dec22.out", Path(__file__),
):
    capture(path)
notes = text("bot_research/notes/economy.md")
(phase / "notes-from-18.22.md").write_text(notes[notes.index("### 18.22"):])
candidate_specs = {tag: text(E / "specs" / (tag + ".spec")).strip()
                   for tag in ("af5", "g1", "v29", "g1f")}
fresh5 = specs_file(E / "opp_fresh5.txt")
fresh6 = specs_file(E / "opp_fresh6.txt")
fresh56 = specs_file(E / "opp_fresh56.txt")
frr1 = specs_file(E / "opp_frr1.txt")
pools = json.loads(capture(E / "opp_fresh56_pools.json"))
for name in ("opp_fresh5_pools.json", "opp_fresh6_pools.json"):
    capture(E / name)
check(len(fresh5) == 27 and len(fresh6) == 16, "Fresh list lengths")
check(fresh56 == fresh5 + fresh6 and len(set(fresh56)) == 43,
      "Fresh56 exact concatenation and uniqueness")
check(set(pools) == set(fresh56), "Fresh56 pool map keys")
check(all(len(set(pools[o]) & {"LEAD", "W1_FORTRESS", "W3_COUNTERS"}) == 1
          for o in fresh56), "Disjoint primary family assignment")
check(all(("NOT_BUILT_AGAINST" in pools[o]) ==
          bool(set(pools[o]) & {"LEAD", "W1_FORTRESS"}) for o in fresh56),
      "Provenance complement assignment")

allrows, run_status = {}, {}
for run in ("fresh5a", "fresh6", "afq56"):
    path = R / run / "results.jsonl"
    rows, bad = rows_file(path)
    allrows[run] = rows
    summary = R / run / "summary.md"
    log = R / (run + ".log")
    summary_exists, log_exists = summary.exists(), log.exists()
    if summary_exists:
        capture(summary)
    log_text = text(log) if log_exists else ""
    completions = re.findall(r"done in ([0-9.]+)s; summary at ([^\n]+)", log_text)
    check(not bad, run + " JSON syntax")
    check(summary_exists and len(completions) == 1, run + " completion evidence")
    run_status[run] = {
        "rows": len(rows), "json_errors": bad,
        "summary_exists": summary_exists, "completion_lines": completions,
        "harness_errors": sum(bool(r.get("error")) for r in rows),
        "bot_errors": sum(sum(len(p["bot_errors"]) for p in r.get("players", []))
                          for r in rows),
        "rejected_actions": sum(sum(p["n_rejected"] for p in r.get("players", []))
                                for r in rows),
        "source_changed": sum(bool(r.get("source_changed")) for r in rows),
        "scenario_errors": sum(sum(len(e) for e in r.get("scenario_errors", []))
                               for r in rows),
    }
    check(not any(run_status[run][key] for key in
                  ("harness_errors", "bot_errors", "rejected_actions",
                   "source_changed", "scenario_errors")), run + " reported errors")

# These three unfinished runs are retained only as dated status, not strength data.
for run, expected in (("afg5", 514), ("bvf", 86), ("afrr", 20)):
    observed = now()
    path = R / run / "results.jsonl"
    exists = path.exists()
    rows, bad = rows_file(path) if exists else ([], [])
    summary, log = R / run / "summary.md", R / (run + ".log")
    summary_exists = summary.exists()
    if summary_exists:
        capture(summary)
    log_text = text(log) if log.exists() else ""
    run_status[run] = {
        "observed_utc": observed, "results_exist": exists, "rows": len(rows),
        "expected": expected, "json_errors": bad, "summary_exists": summary_exists,
        "completion_line": "done in " in log_text,
        "scope": "Status only; no outcome reduction or recommendation inference",
    }

tables = {tag: {} for tag in ("af5", "g1", "v29")}
refs = {tag: {} for tag in tables}
duplicates, source_claims = [], collections.defaultdict(set)
entry_claims, version_claims = collections.defaultdict(set), collections.defaultdict(set)
metadata_issues = []
for run, rows in allrows.items():
    expected_tags = ("af5",) if run == "afq56" else ("g1", "v29", "g1f") if run == "fresh6" else ("g1", "v29")
    opponents = fresh56 if run == "afq56" else fresh6 if run == "fresh6" else fresh5
    expected_keys = {(o, None, side) for o in opponents for side in (0, 1)}
    by_tag = {tag: [] for tag in expected_tags}
    for line, row in enumerate(rows, 1):
        candidate, key, value = normalize(row)
        matches = [tag for tag in expected_tags if candidate == candidate_specs[tag]]
        check(len(matches) == 1, f"{run}:{line} exact candidate spec")
        if len(matches) != 1 or value is None:
            continue
        tag = matches[0]
        by_tag[tag].append(key)
        side = key[2]
        if not (side in (0, 1) and row["winner"] in (0, 1, None)
                and row["hp_a"] - row["hp_b"] == row["hp_diff_a"]
                and row["metadata"]["candidate_side"] == side
                and row["metadata"]["pair"] == row["pair"]
                and row.get("experiment") == run):
            metadata_issues.append([run, line])
        if tag in tables:
            if key in tables[tag]:
                duplicates.append({"tag": tag, "condition": list(key),
                                   "first": refs[tag][key], "second": [run, line]})
            else:
                tables[tag][key] = value
                refs[tag][key] = {"run": run, "line": line}
        for path, digest in row.get("sources", {}).items():
            source_claims[path].add(digest)
        for suffix in ("a", "b"):
            module = row["spec_" + suffix].split(":")[0]
            entry_claims[module].add(row["hash_" + suffix])
            version_claims[module].add(row["version_" + suffix])
    for tag, actual in by_tag.items():
        check(len(actual) == len(expected_keys) and set(actual) == expected_keys,
              run + " exact complete condition set for " + tag)
    run_status[run]["expected_rows"] = len(expected_keys) * len(expected_tags)
check(not duplicates, "Unexpected duplicate joined conditions")
check(not metadata_issues, "Result metadata or HP arithmetic")
fresh_keys = {(o, None, side) for o in fresh56 for side in (0, 1)}
check(all(set(table) == fresh_keys for table in tables.values()), "Complete three-way join")

family_tables = {}
for family in sorted({p for values in pools.values() for p in values}) + ["ALL", "fresh5", "fresh6"]:
    selected = fresh56 if family == "ALL" else fresh5 if family == "fresh5" else fresh6 if family == "fresh6" else [o for o in fresh56 if family in pools[o]]
    keys = {(o, None, side) for o in selected for side in (0, 1)}
    if not all(keys <= set(table) for table in tables.values()):
        continue
    family_tables[family] = {
        "opponents": len(selected), "conditions": len(keys),
        "wdl": {tag: wdl(table[key] for key in keys) for tag, table in tables.items()},
        "paired": {"af5-" + tag: bootstrap(keys, tables["af5"], tables[tag])
                   for tag in ("g1", "v29")},
    }
paired_disagreements = {
    tag: [o for o in fresh56 if table.get((o, None, 0)) != table.get((o, None, 1))]
    for tag, table in tables.items()
}
joined = []
for key in sorted(fresh_keys):
    joined.append({"opponent": key[0], "scenario": key[1], "candidate_side": key[2],
                   "values": {tag: list(table[key]) for tag, table in tables.items()},
                   "refs": {tag: refs[tag][key] for tag in tables}})
changed = [row for row in joined if row["values"]["af5"][0] != row["values"]["g1"][0]]
losses = [row for row in joined if row["values"]["af5"][0] == 0]

versions = {}


def module_file(name):
    path = Path(*name.split("."))
    for candidate in (path.with_suffix(".py"), path / "__init__.py"):
        if candidate.is_file():
            return candidate
    return None


def version(module):
    if module in versions:
        return versions[module]
    seen, todo = {}, [module]
    while todo:
        name = todo.pop()
        if name in seen or not name.startswith("bot_research"):
            continue
        path = module_file(name)
        if path is None:
            continue
        seen[name] = path
        parts = name.split(".")
        todo.extend(".".join(parts[:i]) for i in range(1, len(parts)))
        package = name if path.name == "__init__.py" else ".".join(parts[:-1])
        for node in ast.walk(ast.parse(capture(path))):
            if isinstance(node, ast.Import):
                todo.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    parts = package.split(".")
                    parts = parts[:len(parts) - (node.level - 1)]
                    target = ".".join(parts + ([node.module] if node.module else []))
                else:
                    target = node.module or ""
                todo.append(target)
                todo.extend(target + "." + alias.name for alias in node.names)
    files = set(seen.values()) | set(Path("bot_research/harness").glob("*.py"))
    digest = hashlib.sha256()
    for path in sorted(files):
        digest.update((str(path) + "\0" + sha(capture(path)) + "\n").encode())
    result = {"digest": digest.hexdigest(), "paths": [str(path) for path in sorted(files)]}
    versions[module] = result
    return result


loaded_checks = []
for path, recorded in sorted(source_claims.items()):
    current = sha(capture(path))
    loaded_checks.append({"path": path, "recorded": sorted(recorded),
                          "current": current, "matches": recorded == {current}})
entry_checks = []
for module, recorded in sorted(entry_claims.items()):
    path = module_file(module)
    current = sha(capture(path)) if path else None
    closure = version(module)
    entry_checks.append({"module": module, "entry_path": str(path),
                         "entry_recorded": sorted(recorded), "entry_current": current,
                         "entry_matches": recorded == {current},
                         "version_recorded": sorted(version_claims[module]),
                         "version_current": closure["digest"],
                         "version_matches": version_claims[module] == {closure["digest"]}})
check(all(row["matches"] for row in loaded_checks), "Loaded source hash mismatch")
check(all(row["entry_matches"] and row["version_matches"] for row in entry_checks),
      "Entry or static closure hash mismatch")

old_input_path = OUT / "inspection-20261031T225610458161Z/inputs.json"
old_inputs = json.loads(capture(old_input_path))["inputs"]
old_afq = old_inputs[str(R / "afq56/results.jsonl")]
old_packed = capture(old_afq["snapshot"])
check(sha(old_packed) == old_afq["gzip_sha256"], "Prior afq56 compressed identity")
old_raw = gzip.decompress(old_packed)
check(sha(old_raw) == old_afq["sha256"], "Prior afq56 raw identity")
check(capture(R / "afq56/results.jsonl").startswith(old_raw), "Prior afq56 prefix retained")
old_rows = [json.loads(line) for line in old_raw.splitlines()]
overlap = sorted(set(frr1) & set(fresh56))
overlap_rows = [row for row in joined if row["opponent"] in overlap]
prior_overlap = [{"line": i, "opponent": normalize(row)[1][0],
                  "candidate_side": row["candidate_side"]}
                 for i, row in enumerate(old_rows, 1) if normalize(row)[1][0] in overlap]
maxima = {}
for tag in tables:
    candidates = [(run, line, row) for run, rows in allrows.items()
                  for line, row in enumerate(rows, 1)
                  if normalize(row)[0] == candidate_specs[tag]]
    run, line, row = max(candidates, key=lambda item: item[2]["decide_max_seconds"][item[2]["candidate_side"]])
    maxima[tag] = {
        "seconds": row["decide_max_seconds"][row["candidate_side"]],
        "opponent": normalize(row)[1][0], "side": row["candidate_side"],
        "run": run, "line": line,
        "clock": "Recorded rounded time.perf_counter elapsed wall time per call",
    }

afq_complete = (len(allrows["afq56"]) == 86 and not problems)
condition = family_tables.get("ALL", {}).get("paired", {}).get("af5-g1")
result = {
    "started_utc": started, "finished_utc": now(), "reviewer": "GPT-6 Astra",
    "scope": "Supplementary source/result review; no policy, constructor, Engine, game, replay or test calls",
    "problems": problems, "metadata_issues": metadata_issues,
    "specs": candidate_specs, "runs": run_status, "join_duplicates": duplicates,
    "joined_conditions": joined, "family_tables": family_tables,
    "paired_outcome_margin_round_disagreements": paired_disagreements,
    "changed_af5_g1": changed, "af5_losses": losses,
    "max_recorded_candidate_call": maxima,
    "gate_18_22": {
        "completed_afq56_verified": afq_complete,
        "criterion": "Upper endpoint of declared paired cluster-bootstrap interval at least zero",
        "passes": condition["hi"] >= 0 if afq_complete and condition else None,
        "interval": condition,
    },
    "recommendation_18_26": "OPEN; no completion or pool-gate inference from partial afg5",
    "afrr_overlap": {
        "specs": overlap, "spec_count": len(overlap), "condition_count": 2 * len(overlap),
        "afq_rows": overlap_rows, "present_in_prior_22_56_snapshot": prior_overlap,
        "chronology_scope": "Row order and fixed prior snapshot establish retained availability only, not full researcher knowledge or independently timestamped creation history",
    },
    "sources": {"loaded": loaded_checks, "entries": entry_checks, "static_closures": versions},
}
(phase / "inspection.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
(phase / "inputs.json").write_text(json.dumps({
    "written_utc": now(), "inputs": pins, "inspector_sha256": sha(capture(Path(__file__))),
}, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "folder": str(phase), "finished_utc": result["finished_utc"], "problems": problems,
    "families": family_tables, "maxima": maxima, "gate_18_22": result["gate_18_22"],
    "source_counts": {"loaded": len(loaded_checks), "entries": len(entry_checks)},
    "partial_status": {run: run_status[run] for run in ("afg5", "bvf", "afrr")},
    "afrr_overlap_specs": overlap,
    "inspection_sha256": sha((phase / "inspection.json").read_bytes()),
    "inputs_sha256": sha((phase / "inputs.json").read_bytes()),
}, indent=2))
