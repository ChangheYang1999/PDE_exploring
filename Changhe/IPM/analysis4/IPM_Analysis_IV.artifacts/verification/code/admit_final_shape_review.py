"""Record the completed manual nontermination and shape review."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "05_no_termination", "26_analytic_nontermination",
    "34_logarithmic_nontermination", "51_shear_approximants",
    "54_leading_velocity_optimum", "210_three_fifths_profile_geometry",
    "214_three_fifths_interior_maximum",
]]
ledger, text = next_entry(665)
now = stamp()
review = base / "sources/final_shape_review_V665.md"
review.write_text(review.read_text().replace(
    "Seven complete proof texts", f"Recorded {now}. Seven complete proof texts", 1))
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final nontermination and shape reread protocol\n\nRead seven complete proofs and the corresponding nontermination and leading-velocity report passages. Check the analytic vanishing orders, least radial exponent, weighted norm equality cases and axis-uniform shape estimates.\n\nCompleted {now}, V665. The arguments and inspected report passages pass. Earlier exact numerical certificates were not rerun.\n")
proof = base / "sources/PROOF_at_V665.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_shape_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Seven complete nontermination, leading-velocity and profile-geometry proofs pass the final manual review. The inspected report passages preserve analyticity, the specified polar Wiener norm and the sufficiently large exterior. The shape estimates control both axes and distinguish the two monotone branches from the two interior-maximum branches."
scope = "CONFIRMED within the exact hypotheses; no new numerical replay, full-series growth optimum or sharp shape radius is claimed."
p = base / "verification/admission_V665.json"
p.write_text(json.dumps(dict(at=now, entry=665, verdict="CONFIRMED",
    review_kind="manual mathematical and selected report-passage reread",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    report_passages=["7.4", "8.2", "8.3", "Proposition 8.4"],
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V665 | {now} | Final nontermination and profile-shape review\n\n**Claim.** The nontermination and shape results retain their regularity, norm and exterior-domain qualifications.\n\n**Method.** Complete manual reread of seven proofs and selected report passages; check vanishing-order parity, least exponents, norm equality and axis-uniform estimates; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V665 nontermination and shape reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V665 records the manual reread of seven nontermination and shape proofs and selected report passages, with no new defect.\n")
print(now, result)
