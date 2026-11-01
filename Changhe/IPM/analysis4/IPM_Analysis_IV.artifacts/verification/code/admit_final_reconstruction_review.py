"""Record the completed manual reconstruction and quantitative-scope review."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "07_diophantine_convergence", "09_relative_stability",
    "22_rational_finite_bound", "30_report_transcription",
    "39_potential_double_log", "119_tuned_rational_series",
    "121_tuned_potential_series",
]]
ledger, text = next_entry(666)
now = stamp()
review = base / "sources/final_reconstruction_review_V666.md"
review.write_text(review.read_text().replace(
    "Seven complete proof texts", f"Recorded {now}. Seven complete proof texts", 1))
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final reconstruction and quantitative-scope reread\n\nRead seven complete proofs covering the Diophantine packing estimate, relative stability, finite rational residual, historical transcription corrections and compatible potential reconstruction. Completed {now}, V666. No new mathematical defect was found. Earlier numerical certificates were not rerun.\n")
proof = base / "sources/PROOF_at_V666.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_reconstruction_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Seven complete proofs pass the final reconstruction and quantitative-scope review. The tree packing constants, relative parameter class, finite rational stopping order, tuned majorant Jacobian and exceptional potential logarithms have the stated scopes. Historical transcription corrections remain historical."
scope = "CONFIRMED within the exact hypotheses; no new arithmetic replay, global extension, rational convergence at the stored parameter or optimal radius is claimed."
p = base / "verification/admission_V666.json"
p.write_text(json.dumps(dict(at=now, entry=666, verdict="CONFIRMED",
    review_kind="manual mathematical reread",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V666 | {now} | Final reconstruction and quantitative-scope review\n\n**Claim.** The quantitative bounds and potential reconstruction retain their exact parameter, order and logarithmic qualifications.\n\n**Method.** Complete manual reread of seven proofs; check tree charges, compact-parameter continuity, residual indexing, affine tuning and exceptional potential channels; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V666 reconstruction and quantitative-scope reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V666 records the manual reread of seven reconstruction and quantitative-scope proofs, with no new defect.\n")
print(now, result)
