"""Record the completed manual reconstruction and quantitative-scope review."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "168_certified_initial_majorants", "170_tuned_top_mode_obstruction",
    "184_explicit_prefix_tail_bounds", "187_sharp_prefix_tail_bounds",
    "79_realized_loss_criterion", "82_weighted_loss_criterion",
    "88_plain_stream_criterion", "104_divisor_localized_criterion",
]]
ledger, text = next_entry(667)
now = stamp()
review = base / "sources/final_majorant_criteria_review_V667.md"
review.write_text(review.read_text().replace(
    "Eight complete proof texts", f"Recorded {now}. Eight complete proof texts", 1))
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final majorant and conditional-criterion reread\n\nRead eight complete proofs covering prefix supersolutions, sharp tails, necessary radii and realized-loss criteria. Completed {now}, V667. No new mathematical defect was found. Conditional all-order assumptions remain unproved for the canonical logarithmic sequence. Earlier numerical certificates were not rerun.\n")
proof = base / "sources/PROOF_at_V667.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_majorant_criteria_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Eight complete proofs pass the final majorant and conditional-criterion review. Prefix bounds, residue tails, abstract-budget optimality, top-mode independence, stationary inverses and localized Poisson estimates retain their stated scopes."
scope = "CONFIRMED under the stated hypotheses; no new numerical replay or unconditional canonical-log convergence follows."
p = base / "verification/admission_V667.json"
p.write_text(json.dumps(dict(at=now, entry=667, verdict="CONFIRMED",
    review_kind="manual mathematical reread",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V667 | {now} | Final majorant and conditional-criterion review\n\n**Claim.** Prefix and tail estimates are valid, and realized-loss criteria retain their all-order hypotheses.\n\n**Method.** Complete manual reread of eight proofs; check triangular domination, residue starting indices, discrete maxima, top-mode propagation, degree bounds and both Poisson incidences; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V667 majorant and conditional-criterion reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V667 records the manual reread of eight majorant and conditional-criterion proofs, with no new defect.\n")
print(now, result)
