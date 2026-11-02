"""Independent archived-record recount, without project imports or policy execution."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import gzip
import hashlib
import json

BASE = Path("bot_research/experiments/validation/reviews/economy_final_gate_001")
PHASE = BASE / "final-gate-20261031T233546260787Z"

def digest(data):
    return hashlib.sha256(data).hexdigest()

started = datetime.now(timezone.utc).isoformat()
raw_receipt = (PHASE / "inspection.json").read_bytes()
raw_manifest = (PHASE / "inputs.json").read_bytes()
assert digest(raw_receipt) == "3c06e23be7a4944fd25b3a8b20c2820fbd1c3c4c826ebe69ac4f155979473c6e"
assert digest(raw_manifest) == "31523d876f0443867d30fcbfab3620d77e9577811db92c207cab324d373c7b15"
result = json.loads(raw_receipt)
manifest = json.loads(raw_manifest)
assert result["status"] == "COMPLETE_GATE_REVIEW" and not result["problems"]
raw = {}
for name, pin in manifest["inputs"].items():
    assert not Path(name).is_absolute() and ".." not in Path(name).parts
    packed = Path(pin["snapshot"]).read_bytes()
    assert digest(packed) == pin["gzip_sha256"], name
    data = gzip.decompress(packed)
    assert digest(data) == pin["sha256"] and len(data) == pin["bytes"], name
    raw[name] = data
assert len(raw) == 351
cache = {}

def row_at(path, line):
    if path not in cache:
        cache[path] = [json.loads(line) for line in raw[path].splitlines()]
    return cache[path][line - 1]

def normalize(row):
    side = row["candidate_side"]
    assert side in (0, 1) and row["winner"] in (None, 0, 1)
    assert row["hp_a"] - row["hp_b"] == row["hp_diff_a"]
    assert not row.get("error") and not row.get("source_changed")
    assert not any(row.get("scenario_errors", []))
    assert all(not p["bot_errors"] and p["n_rejected"] == 0 for p in row["players"])
    candidate = row["spec_a" if side == 0 else "spec_b"]
    opponent = row["spec_b" if side == 0 else "spec_a"]
    outcome = 0.5 if row["winner"] is None else float(row["winner"] == side)
    value = [outcome, row["hp_diff_a"] * (1 if side == 0 else -1), row["rounds"]]
    return candidate, (opponent, row.get("scenario"), side), value

tables = {tag: {} for tag in result["specs"]}
refs_checked = 0
pool_memberships = {}
for item in result["joined_conditions"]:
    key = (item["opponent"], item["scenario"], item["candidate_side"])
    assert key not in pool_memberships
    pool_memberships[key] = set(item["pool_memberships"])
    for tag, ref in item["refs"].items():
        path = "bot_research/runs/economy/" + ref["run"] + "/results.jsonl"
        candidate, observed_key, value = normalize(row_at(path, ref["line"]))
        assert candidate == result["specs"][tag] and observed_key == key
        assert value == item["values"][tag]
        tables[tag][key] = value
        refs_checked += 1
assert len(pool_memberships) == 804 and refs_checked == 2412
assert len({key[0] for key in pool_memberships}) == 402
assert Counter(map(len, pool_memberships.values())) == {1: 770, 2: 26, 3: 8}

baseline = {}
base_specs = Counter()
pool_keys = {}
for pool, refs in result["base_membership_refs"].items():
    keys = set()
    for item in refs:
        key = tuple(item["condition"])
        ref = item["ref"]
        candidate, observed_key, value = normalize(row_at(ref["path"], ref["line"]))
        assert key == observed_key and key not in keys and pool in pool_memberships[key]
        keys.add(key)
        if key in baseline:
            assert baseline[key] == value
        baseline[key] = value
        base_specs[candidate] += 1
    pool_keys[pool] = keys
assert len(pool_keys) == 14 and sum(map(len, pool_keys.values())) == 846
assert set(baseline) == set(pool_memberships)
assert set().union(*pool_keys.values()) == set(pool_memberships)

def wdl(table, keys):
    counts = Counter(table[key][0] for key in keys)
    return [counts[1.0], counts[0.5], counts[0.0]]

pool_tables = {}
for pool, keys in pool_keys.items():
    expected = result["pool_tables"][pool]
    calculated = {tag: wdl(table, keys) for tag, table in tables.items()}
    assert calculated == expected["wdl"]
    delta = calculated["af5"][0] - calculated["g1"][0]
    assert delta == expected["af5_minus_g1_wins"] and delta >= -2
    pool_tables[pool] = {"conditions": len(keys), "wdl": calculated,
                         "retained_R13_baseline_wdl": wdl(baseline, keys),
                         "af5_minus_g1_wins": delta}
unique = {tag: wdl(table, pool_memberships) for tag, table in tables.items()}
assert unique == result["unique_gate"]["wdl"]
assert unique == {"af5": [764, 2, 38], "g1": [726, 16, 62], "v29": [546, 14, 244]}
remaining = {tuple(key) for key in result["remaining_gate"]["conditions"]}
assert len(remaining) == 514
assert all(tables["g1"][key][0] == tables["v29"][key][0] for key in remaining)
changed = sorted(key for key in remaining if tables["af5"][key][0] != tables["g1"][key][0])
assert [list(key) for key in changed] == result["agreement_prediction"]["changed_conditions"]
assert len(changed) == 2 and result["agreement_prediction"]["passes"]
assert all(tables["af5"][key][0] == 1 and tables["g1"][key][0] == 0 for key in changed)
assert all(table[(opponent, None, 0)] == table[(opponent, None, 1)]
           for table in tables.values() for opponent in {key[0] for key in table})
# A retained older parameterized baseline is not silently relabeled as a current policy.
base_unique = wdl(baseline, pool_memberships)
assert base_unique == [504, 64, 236]
memberships = {tag: [sum(pool["wdl"][tag][i] for pool in pool_tables.values()) for i in range(3)]
               for tag in tables}
assert memberships == {"af5": [804, 2, 40], "g1": [764, 16, 66], "v29": [584, 18, 244]}
source_path = BASE / "inspect_final_gate_008.py"
assert digest(source_path.read_bytes()) == "71fe3cd8fd091258241af833217dce1293d19d861e1aad2db282af03750bfd19"
output = {
    "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
    "verdict": "CONFIRMED for archived finite counts and the declared standard-start gate",
    "scope": "Independent source/archive/result recount; no policy, engine, game, replay or test execution",
    "root_reader": str(Path(__file__).relative_to(Path.cwd())),
    "root_reader_sha256": digest(Path(__file__).read_bytes()),
    "review_sha256": digest(raw_receipt), "input_manifest_sha256": digest(raw_manifest),
    "archive_inputs_verified": len(raw), "raw_candidate_baseline_joins_verified": refs_checked,
    "base_membership_rows_verified": sum(map(len, pool_keys.values())),
    "denominators": result["denominators"], "unique_wdl": unique,
    "pool_membership_wdl": memberships, "retained_R13_base_unique_wdl": base_unique,
    "retained_R13_base_specs_by_membership": dict(base_specs), "pool_tables": pool_tables,
    "agreement_conditions": 514, "agreement_differences": len(changed),
    "standard_start_gate": result["recommendation"],
    "caveats": ["The 290 sweep conditions informed af5 selection; 514 remainder and 86 fresh56 conditions have separate roles.",
                 "The retained R13 comparison mixes explicitly parameterized predecessor baseline rows; this recount does not prove clone equivalence.",
                 "WDL agreement does not mean equal HP margins or equal histories.",
                 "The scenario check and post-selection round robins are separate evidence."]
}
out = BASE / "root_gate_review_008.json"
assert not out.exists()
out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({"receipt": str(out), "sha256": digest(out.read_bytes()),
                  "finished_utc": output["finished_utc"], "unique_wdl": unique,
                  "verdict": output["verdict"]}, indent=2))
