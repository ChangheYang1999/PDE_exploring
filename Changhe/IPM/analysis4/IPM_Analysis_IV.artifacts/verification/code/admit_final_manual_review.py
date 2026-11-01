"""Retain a completed manual review with immutable inputs and a dated ledger."""
from pathlib import Path
import argparse
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

ap = argparse.ArgumentParser()
ap.add_argument("configuration")
args = ap.parse_args()
config = json.loads(Path(args.configuration).read_text())
entry = config["entry"]
base = Path("research/301_final_claim_audit")
ledger, text = next_entry(entry)
now = stamp()
review = Path(config["review"])
assert review.is_file()
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## {config['title']}\n\nCompleted {now}, V{entry}. "
            f"{config['result']} {config['scope']}\n")
proof = base / f"sources/PROOF_at_V{entry}.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / f"sources/admit_final_manual_review_at_V{entry}.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
p = base / f"verification/admission_V{entry}.json"
p.write_text(json.dumps(dict(at=now, entry=entry, verdict="CONFIRMED",
    review_kind="manual mathematical reread",
    reviewed_proofs=[ref(q) for q in config["paths"]], review=ref(review),
    proof=ref(proof), algorithm=ref(algorithm), configuration=ref(args.configuration),
    theory_snapshot=ref(snapshot), result=config["result"], scope=config["scope"]),
    indent=2) + "\n")
ledger.write_text(text + f"\n## V{entry} | {now} | {config['title']}\n\n"
    f"**Claim.** {config['claim']}\n\n**Method.** {config['method']}\n\n"
    f"**Result.** {config['result']}\n\n**Verdict: {config['scope']}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V{entry} {config['title']}\n\n"
    f"{config['result']}\n\nNo report correction is requested. The theory remains "
    "identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V{entry}, {config['title']}. {config['result']}\n")
print(now, entry, config["result"])
