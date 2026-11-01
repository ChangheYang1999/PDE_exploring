"""Check final proof-reading coverage and the last editorial report changes."""
from pathlib import Path
from hashlib import sha256
import difflib
import gzip
import json
import re
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

entry = 674
base = Path("research/301_final_claim_audit")
ledger, text = next_entry(entry)
now = stamp()
map_snapshot = base / "sources/FINAL_CLAIM_MAP_at_V674.md"
map_snapshot.write_bytes(Path("FINAL_CLAIM_MAP.md").read_bytes())
mapped = set(re.findall(r"\]\((research/[^)]+/PROOF\.md)\)", map_snapshot.read_text()))
seen = {}
receipts = []
for n in range(657, 674):
    p = base / f"verification/admission_V{n}.json"
    d = json.loads(p.read_text())
    assert d["entry"] == n
    receipts.append(ref(p))
    for item in d["reviewed_proofs"]:
        assert sha256(Path(item["path"]).read_bytes()).hexdigest() == item["sha256"]
        assert item["path"] not in seen or seen[item["path"]] == item["sha256"]
        seen[item["path"]] = item["sha256"]
assert len(mapped) == 135 and len(seen) == 142 and not mapped - seen.keys()
old = base / "verification/post_freeze_20261031T235941Z"
new = base / "verification/post_freeze_20261101T003558Z"
changes = []
for name, live in [("summary", "FINAL_SUMMARY.md"), ("theory", "FARFIELD_CONVERGENCE_THEORY.md"), ("report", "FINAL_REPORT.md")]:
    before = reconstruct(old / f"{name}.json")
    after = reconstruct(new / f"{name}.json")
    assert after == (Path("../a4-lead") / live).read_bytes()
    if name == "theory":
        assert before == after
    elif name == "summary":
        old_header = "Checkpoint version, 2026-10-31T23:53Z (run start 2026-10-31T01:57:42Z). This file is kept current at every checkpoint;\nthe final version will be stamped at the end of the run. Labels: PROVED (complete proof written and confirmed by the\n"
        new_header = "Final version, 2026-11-01T00:34Z (run start 2026-10-31T01:57:42Z; team stop 2026-11-01T00:57:42Z). Labels: PROVED (complete proof written and confirmed by the\n"
        assert before.count(old_header.encode()) == 1
        assert before.replace(old_header.encode(), new_header.encode()) == after
    else:
        old_header = b"Report version 2026-10-31T23:58Z."
        new_header = b"Report version 2026-11-01T00:34Z."
        assert before.count(old_header) == 1
        assert before.replace(old_header, new_header) == after
    diff = base / f"sources/final_stamp_{name}_V674.diff"
    diff.write_text("".join(difflib.unified_diff(before.decode().splitlines(keepends=True), after.decode().splitlines(keepends=True), fromfile="reviewed_235941", tofile="final_003558")))
    changes.append(dict(document=name, previous=ref(old/f"{name}.json"), current=ref(new/f"{name}.json"), diff=ref(diff), final_sha256=sha256(after).hexdigest(), final_line_count=len(after.splitlines()), changed=before != after))
numerics = []
old_num_report = Path("research/301_final_claim_audit/verification/20261031T221828Z/numerics_report.md")
old_num_lines = old_num_report.read_text().splitlines(keepends=True)
status_changes = []
for p in sorted(Path("research/307_final_numerical_summary/sources").glob("*repaired_V643.excerpts.json")):
    d = json.loads(p.read_text())
    raw = Path(d["source_path"]).read_bytes()
    actual = sha256(raw).hexdigest()
    if actual != d["source_sha256"]:
        assert Path(d["source_path"]).name == "FARFIELD_NUMERICAL_EXPERIMENTS.md"
        restored = raw.decode()
        for tag, expected_order in [("sqrt5_sin1_p1024", 700), ("c007_exact", 23), ("c007_arb512", 233)]:
            before = next(l for l in old_num_lines if l.startswith("| " + tag + " |"))
            after = next(l for l in restored.splitlines(keepends=True) if l.startswith("| " + tag + " |"))
            assert restored.count(after) == 1
            restored = restored.replace(after, before)
            log = Path("../a4-num/logs") / (tag + ".jsonl")
            log_raw = log.read_bytes()
            rows = [json.loads(l) for l in log_raw.decode().splitlines()]
            orders = [r["n"] for r in rows if isinstance(r.get("n"), int) and "K" in r]
            assert orders == list(range(1, expected_order + 1))
            packed = base / "sources" / (tag + "_at_V674.jsonl.gz")
            packed.write_bytes(gzip.compress(log_raw, mtime=0))
            assert gzip.decompress(packed.read_bytes()) == log_raw
            status_changes.append(dict(tag=tag, before=before, after=after, first_order=orders[0], final_order=orders[-1], order_count=len(orders), source_log_sha256=sha256(log_raw).hexdigest(), retained_log=ref(packed)))
        assert sha256(restored.encode()).hexdigest() == d["source_sha256"]
        current = base / "sources/FARFIELD_NUMERICAL_EXPERIMENTS_at_V674.md"
        current.write_bytes(raw)
        restored_file = base / "sources/numerics_restoration_V674.json"
        restored_file.write_text(json.dumps(dict(current=ref(current), restored_sha256=d["source_sha256"], substitutions=status_changes, scope="Replace each after line by its before line to recover exactly the source hash at V643."), indent=2)+"\n")
    numerics.append(dict(retained_excerpt=ref(p), source_path=d["source_path"], expected_sha256=d["source_sha256"], current_sha256=actual, unchanged=actual==d["source_sha256"]))
assert len(numerics) == 3 and len(status_changes) == 3
inventory = base / "verification/final_coverage_and_stamp_V674.json"
inventory.write_text(json.dumps(dict(at=now, mapped_count=len(mapped), reviewed_count=len(seen), mapped_proofs=sorted(mapped), reviewed_proofs=[dict(path=p, sha256=h) for p,h in sorted(seen.items())], extra_supporting_proofs=sorted(seen.keys()-mapped), missing=[], final_reports=changes, numerical_report_identities=numerics, numerical_status_changes=status_changes, numerical_restoration=ref(restored_file), all_checks_pass=True), indent=2) + "\n")
result = "The final reread covers all 135 distinct mapped proofs and seven additional supporting proofs, with every reread hash still matching. The final lead theory is unchanged; the summary and assembled report differ from the last reviewed versions only in their editorial version stamps. Two numerical report texts are byte-identical to their V643 source hashes. The experiments report differs only in three final-order status cells, which agree with the retained complete logs at orders 700, 23 and 233."
scope = "CONFIRMED for complete mapped-proof rereading coverage and these final text identities. This does not claim a new cover-to-cover reading of the assembled report or a new arithmetic replay."
with (base/"PROOF.md").open("a") as f:
    f.write(f"\n## Final proof coverage and report freeze\n\nCompleted {now}, V674. {result}\n\nThe finite check takes the set of distinct proof links in a frozen claim map and the union of proof references in V657 through V673. The first set is contained in the second, and the stored digest of every member equals its current digest. Reconstruction of the previous and final lead snapshots leaves only the two explicitly checked header substitutions; the theory substitution is empty. Two numerical texts match the full-source hashes retained with the V643 excerpts. Replacing the three changed status lines in the third text with their older versions exactly recovers its V643 hash. The three source logs contain uninterrupted computed-order rows from one through their stated final orders. This is a check of completion metadata, not a new coefficient certificate. These identities transfer the existing scoped reviews to the final texts; they introduce no new mathematical implication. {scope}\n")
proof = base/"sources/PROOF_at_V674.md"
proof.write_bytes((base/"PROOF.md").read_bytes())
algorithm = base/"sources/admit_final_freeze_at_V674.py"
algorithm.write_bytes(Path(__file__).read_bytes())
admission = base/"verification/admission_V674.json"
admission.write_text(json.dumps(dict(at=now,entry=entry,verdict="CONFIRMED",all_checks_pass=True,claim_map=ref(map_snapshot),manual_review_receipts=receipts,inventory=ref(inventory),proof=ref(proof),algorithm=ref(algorithm),result=result,scope=scope),indent=2)+"\n")
ledger.write_text(text+f"\n## V674 | {now} | Final mapped-proof coverage and report freeze\n\n**Claim.** The final mapped proofs are all covered by the completed manual reread, and the final report changes do not alter any mathematical or numerical claim.\n\n**Method.** Set inclusion and current digest checks for all 142 reread proofs; exact reconstruction and header-substitution checks for the three lead reports; two full-source identity checks and exact reconstruction of the third V643 numerical report from its three status changes; complete-order metadata checks in the retained logs.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {admission}.\n")
notes=Path("NOTES_FOR_TEAM.md")
notes.write_text(f"## {now} VERIFIER -> LEAD: V674 final mapped-proof coverage and freeze confirmed\n\n{result}\n\nNo report correction is requested. Final hashes: summary abd508a37708dc8c2327a50736ad25d3b560b79f28539002f7492a5427acef92; theory 6d9069c1ef647cc17bbef85cc44409b69f5c73e2bcddb228fad9fa3d09f3f248; assembled report 2bde22cb390a9d7b5f1efface0ce0cf6992e69ac91f387408d30625c707b77d1. The final summary now has 501 lines because the stamp replaces two lines with one; the historical 502-line reading count remains correct for its original snapshot.\n\n"+notes.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V674 final coverage and freeze. {result}\n")
print(now, result)
