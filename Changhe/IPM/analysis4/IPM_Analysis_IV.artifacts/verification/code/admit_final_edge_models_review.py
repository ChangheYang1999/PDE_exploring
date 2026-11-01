"""Record the completed manual finite-edge proof review."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "103_edge_top_chain", "106_edge_convergence",
    "107_log_free_edge_criterion", "111_finite_edge_gevrey",
    "112_edge_top_comparison", "113_edge_top_radii",
    "114_edge_top_polynomial_rate", "116_edge_radius_approach",
    "117_edge_top_constant",
]]
ledger, text = next_entry(669)
now = stamp()
review = base / "sources/final_edge_models_review_V669.md"
review.write_text(review.read_text().replace(
    "Nine complete proof texts", f"Recorded {now}. Nine complete proof texts", 1))
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final finite-edge proof reread\n\nRead nine complete proofs covering edge convergence, Gevrey bounds, highest-mode comparisons, exact radii and asymptotic constants. Completed {now}, V669. Their arguments pass with the stated previously certified inputs. This does not add an arithmetic replay or establish convergence of the unrestricted canonical rational logarithmic series.\n")
proof = base / "sources/PROOF_at_V669.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_edge_models_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Nine complete finite-edge proofs pass the final mathematical review. Geometric and positive-Gevrey bounds remain distinct; highest-mode radii are not equated with full-norm radii; the central-pair factor 1/2 is retained; and every fixed-cutoff conclusion remains separate from the unrestricted recurrence."
scope = "CONFIRMED within the exact hypotheses and previously admitted arithmetic inputs; no new arithmetic replay or unrestricted-series convergence conclusion is claimed."
p = base / "verification/admission_V669.json"
p.write_text(json.dumps(dict(at=now, entry=669, verdict="CONFIRMED",
    review_kind="manual mathematical reread",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V669 | {now} | Final finite-edge proof review\n\n**Claim.** The edge convergence, Gevrey and highest-mode hierarchy results have their stated conclusions and limits.\n\n**Method.** Complete manual reread of nine proofs; check inverse estimates, factorial costs, positive comparisons, moving-radius tails, stochastic contraction and the central-pair normalization; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V669 finite-edge reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V669 records the manual reread of nine finite-edge proofs, with no new defect.\n")
print(now, result)
