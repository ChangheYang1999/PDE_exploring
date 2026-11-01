"""Record the completed manual reconstruction and quantitative-scope review."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "197_high_harmonic_tuning", "198_odd_period_high_harmonic_support",
    "201_spectral_gap_response", "203_generic_lattice_obstruction",
    "246_support_boundary_scope", "229_eleven_lattice_stability",
    "231_extremal_single_harmonics", "216_repeated_near_resonant_poles",
    "218_all_order_near_resonant_poles",
]]
ledger, text = next_entry(668)
now = stamp()
review = base / "sources/final_support_poles_review_V668.md"
review.write_text(review.read_text().replace(
    "Nine complete proof texts", f"Recorded {now}. Nine complete proof texts", 1))
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final support and parameter-pole reread\n\nRead nine complete proofs covering response support, actual and generic obstructions, lattice stability and parameter poles. Completed {now}, V668. Their arguments pass with the stated previously certified arithmetic inputs. No arithmetic replay or fixed-displacement asymptotic claim is added.\n")
proof = base / "sources/PROOF_at_V668.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_support_poles_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Nine complete support, tuning-failure, lattice-stability and parameter-pole proofs pass the final mathematical review. Support inclusion is not mistaken for noncancellation; the genericity and neighborhood scopes are retained; the pole hierarchy remains a fixed-order meromorphic result."
scope = "CONFIRMED within the exact hypotheses and previously admitted arithmetic inputs; no new arithmetic replay or fixed-displacement convergence conclusion is claimed."
p = base / "verification/admission_V668.json"
p.write_text(json.dumps(dict(at=now, entry=668, verdict="CONFIRMED",
    review_kind="manual mathematical reread",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V668 | {now} | Final support and parameter-pole review\n\n**Claim.** The support, lattice and near-resonant results have their stated conclusions and limits.\n\n**Method.** Complete manual reread of nine proofs; check signed sumsets, affine index bounds, witness genericity, uniform response neighborhoods and Laurent pole propagation; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V668 support and parameter-pole reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V668 records the manual reread of nine support and parameter-pole proofs, with no new defect.\n")
print(now, result)
