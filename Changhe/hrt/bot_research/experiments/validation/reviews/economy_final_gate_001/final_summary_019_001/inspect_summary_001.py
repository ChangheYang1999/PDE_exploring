"""Bounded source and retained-record review. Standard library only."""
from pathlib import Path
import collections
import datetime
import gzip
import hashlib
import json

B = Path("bot_research/experiments/validation/reviews/economy_final_gate_001")
OUT = B / "final_summary_019_001"
F = Path("bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001")
PINS = {}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def relative(path):
    path = Path(path)
    path = (path if path.is_absolute() else Path.cwd() / path).relative_to(Path.cwd())
    if ".." in path.parts:
        raise ValueError("Path leaves project")
    return path


def capture(path, raw=None):
    path = relative(path)
    raw = path.read_bytes() if raw is None else raw
    digest = sha(raw)
    target = OUT / "inputs" / (digest + ".gz")
    if not target.exists():
        with target.open("xb") as stream:
            stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    packed = target.read_bytes()
    if gzip.decompress(packed) != raw:
        raise ValueError("Archive mismatch")
    pin = {"sha256": digest, "bytes": len(raw), "gzip_sha256": sha(packed),
           "snapshot": str(target), "captured_utc": now()}
    key = str(path)
    if key in PINS and PINS[key]["sha256"] != digest:
        raise ValueError("Different bytes under one logical key")
    PINS[key] = pin
    return raw


def pinned_json(path, digest):
    raw = capture(path)
    if sha(raw) != digest:
        raise ValueError("Sealed receipt mismatch: " + str(path))
    return json.loads(raw)


def write(name, value):
    raw = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    if str(Path.cwd()).encode() in raw:
        raise ValueError("Absolute project path in metadata")
    with (OUT / name).open("xb") as stream:
        stream.write(raw)
    return sha(raw)


def main():
    started = now()
    (OUT / "inputs").mkdir(exist_ok=True)
    capture(__file__)
    notes = capture("bot_research/notes/economy.md").decode()
    entry = notes[notes.index("## Entry 19 "):]
    write("entry19_snapshot.json", {"captured_utc": now(), "text": entry})
    gate = pinned_json(B / "final-gate-20261031T233546260787Z/inspection.json",
                       "3c06e23be7a4944fd25b3a8b20c2820fbd1c3c4c826ebe69ac4f155979473c6e")
    gate_map = pinned_json(B / "final-gate-20261031T233546260787Z/inputs.json",
                           "31523d876f0443867d30fcbfab3620d77e9577811db92c207cab324d373c7b15")
    afrr = pinned_json(B / "afrr-20261031T233750162131Z/inspection.json",
                      "6659ba2e0bb9a8c7ac693b1898099a34b9c9d2899f66cb57deb1d63e9112aa43")
    afrep = pinned_json(B / "afrep-20261031T234033189508Z/inspection.json",
                       "89af3548237a33784b3fdfb8499d33b940804194dafc05cf9ce2937b647fc9e8")
    bvf = pinned_json(B / "bvf-20261031T232428135728Z/inspection.json",
                     "71ecca24d07f1787a8bd081bc49c61589efa5eb0df6ffe76da2954f7a80ca3a9")
    scenario = pinned_json(B / "scenario-control-20261031T234828252397Z/inspection.json",
                          "746dd4d3a8a0b0710114692f4a0fe824444c4c8af0f9e61234aaf5f2749dddec")
    frr = pinned_json(F / "record_audit_final_001.json",
                     "518a8593bea8e590ecfdec22ee5e4fc1bfa7d720e3b67aeed9fe7db0a05febc7")
    pinned_json(F / "root_review_002.json",
                "2494c99caf1970368b043be9cd89f72679d8a002f15866a6ce3109ea1753e5b0")
    for path in (
        B / "AFRR_REVIEW_006.md", B / "AFREP_REVIEW_011.md",
        B / "BVF_REVIEW_004.md", B / "FINAL_GATE_REVIEW_008.md",
        B / "CHRONOLOGY_CLARIFICATION_001.md", B / "SCENARIO_REVIEW_007.md",
        B / "AFS4_DEVELOPMENT_REVIEW_014.md", B / "AFS3_DEVELOPMENT_REVIEW_015.md",
        F / "foreign_attack_control_flow_001/REVIEW.md",
        F / "root_foreign_gate_review_001.json",
        F / "hp_erratum_001/ERRATUM.md",
    ):
        capture(path)
    joined = gate["joined_conditions"]
    worse = [row for row in joined if row["values"]["af5"][0] < row["values"]["g1"][0]]
    cache = {}
    checked = 0
    for joined_row in worse:
        for tag in ("af5", "g1"):
            ref = joined_row["refs"][tag]
            path = Path("bot_research/runs/economy") / ref["run"] / "results.jsonl"
            key = str(path)
            if key not in cache:
                pin = gate_map["inputs"][key]
                packed = relative(pin["snapshot"]).read_bytes()
                raw = gzip.decompress(packed)
                if (sha(packed), sha(raw), len(raw)) != (
                        pin["gzip_sha256"], pin["sha256"], pin["bytes"]):
                    raise ValueError("Original raw row archive mismatch")
                cache[key] = [json.loads(line) for line in capture(path, raw).splitlines()]
            row = cache[key][ref["line"] - 1]
            side = row["candidate_side"]
            candidate = row["spec_a"] if side == 0 else row["spec_b"]
            opponent = row["spec_b"] if side == 0 else row["spec_a"]
            score = .5 if row["winner"] is None else float(row["winner"] == side)
            value = [score, row["hp_diff_a"] * (1 if side == 0 else -1), row["rounds"]]
            if (candidate != gate["specs"][tag]
                    or (opponent, row.get("scenario"), side) !=
                    (joined_row["opponent"], joined_row["scenario"], joined_row["candidate_side"])
                    or value != joined_row["values"][tag]):
                raise ValueError("Raw row does not match sealed comparison")
            checked += 1
    excluded = {"GROWERS", "GUARDED_MAZE", "HANDOFF", "f5t"}
    ten = [row for row in joined if set(row["pool_memberships"]) - excluded]
    result = {
        "started_utc": started, "finished_utc": now(), "reviewer": "GPT-6 Astra",
        "scope": "Bounded supplementary source/JSON review; no policy imports, constructors, decisions, games, Engine, replay or test calls",
        "gate_denominators": gate["denominators"],
        "ten_pool_subset": {"memberships": sum(len(set(x["pool_memberships"]) - excluded) for x in ten),
                            "unique_conditions": len(ten),
                            "unique_specs": len({x["opponent"] for x in ten}),
                            "excluded_pools": sorted(excluded)},
        "af5_worse_g1": {"unique_conditions": len(worse),
                        "memberships": sum(len(x["pool_memberships"]) for x in worse),
                        "raw_candidate_baseline_rows_authenticated": checked,
                        "conditions": worse},
        "afrr_exact_fresh56_repeat_count": afrr["exact_repeat_count"],
        "afrr_source_alias": afrr["source_parameter_alias"],
        "afrr_chronology": afrr["chronology"],
        "afrep_scope": {k: afrep[k] for k in ("causal_scope", "recommendation_scope", "log_scope")},
        "bvf_family_scope": bvf["family_scope"],
        "scenario_equality_scope": scenario["equality_scope"],
        "scenario_H18_31a": scenario["H18_31a"],
        "frr7_comparisons": {
            k: {field: value for field, value in row.items() if field != "conditions"}
            for k, row in frr["matched_comparisons"].items() if k in
            ("scripted_AF5_vs_G1", "scripted_AF5_vs_V29")},
        "limits": "Previously sealed review receipts are authenticated and quoted, not rerun. Only the16 raw rows supporting the eight af5/g1 regressions are newly rejoined here. Full historical archive graphs, old theorem claims and runtime causal counterfactuals are not re-audited.",
    }
    inspection = write("inspection.json", result)
    for pin in PINS.values():
        packed = relative(pin["snapshot"]).read_bytes()
        raw = gzip.decompress(packed)
        if (sha(packed), sha(raw), len(raw)) != (pin["gzip_sha256"], pin["sha256"], pin["bytes"]):
            raise ValueError("Final archive verification failed")
    inputs = write("inputs.json", {"written_utc": now(), "inputs": PINS,
                                  "all_archives_verified": len(PINS),
                                  "relative_input_keys_verified": all(not Path(k).is_absolute() for k in PINS)})
    print(json.dumps({"inspection_sha256": inspection, "inputs_sha256": inputs,
                      "archives": len(PINS), "af5_worse_g1": len(worse)}, indent=2))


if __name__ == "__main__":
    main()
