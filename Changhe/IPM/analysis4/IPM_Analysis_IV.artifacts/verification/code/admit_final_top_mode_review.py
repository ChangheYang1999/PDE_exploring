"""Record the manual final review of the highest-mode radius obstruction."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "38_extreme_fourier_mode",
    "115_top_coefficient_asymptotic",
    "118_critical_derivative_obstruction",
]]
ledger, text = next_entry(662)
now = stamp()
review = f"""# Final highest-mode and boundary-derivative review

Recorded {now}. Three complete proof texts were manually reread. This is a review of the exact arguments and their scope, not a replay of the finite beta-integral or coefficient certificates.

Write B=L+1, eta=B-delta and d=delta/(1-delta). The highest density and stream frequencies at order n are Bn-1 and Bn. The top Poisson coefficient is -A_n/[2(eta n+2)]. Substitution into the ordered nonlinear product gives (A_i A_j/4)[1-2Bj/(eta i+2)], with the same signs and halves as the full recurrence. No lower input pair can reach that frequency. A resonant homogeneous stream has frequency n delta-2, strictly below Bn, so it cannot change the top recurrence or introduce a logarithm into that coefficient.

After the alternating amplitude normalization, pairing i,j makes the kernel positive. Subtracting 2n/(eta n+4) from j/(eta i+2)+i/(eta j+2) gives the positive numerator eta(eta n+2)(i-j)^2 over the common denominator. The remaining strict inequality is (B+delta)n>4; it also holds at B=2,n=2. Therefore every normalized h_n is positive.

The generating equations, the substitution w=1/(1-v), the integrating factor x^a(1-x)^b, and the initial normalization give z=4d[a Beta_x(a,b)]^(1/a). The real inverse is analytic below x=1. Positivity rules out a smaller convergence radius by the elementary nonnegative-series argument stated in the proof. Its derivative is unbounded at x=1 because b>1, so the radius is exactly R_H. This first argument gives the radius and boundary value but does not alone give a coefficient asymptotic.

The later asymptotic proof supplies the required complex step. Absolute convergence on the closed disk follows from positivity and the finite endpoint sums. On any other boundary point, equality in the triangle inequality for J would require the positive coefficients of indices one and two to have the same phase. Hence |v|<1 there, and the holomorphic differential system extends the solution. The terminal integral equation and uniqueness match this continuation to the interior one. Compact collars away from R_H combine with the local inverse near R_H into a dented disk.

Near the positive endpoint, the analytic inverse of u Phi(u)^(1/b) gives H=4d-4d C(1-z/R_H)^nu+O((1-z/R_H)^(2nu)), with nu=1/b in (1/2,1). The local remainder is controlled on the dented disk. The displayed contour uses rays with positive real displacement from R_H; their exponential factor bounds the integral by R_H^(-n)n^(-1-2nu). The binomial coefficient and gamma recurrence give the positive leading constant 4d C nu/Gamma(1-nu). Thus the asserted constant-factor asymptotic and consecutive ratio limit follow. No unproved real-axis transfer step is used.

At the physical radius r_*=(|alpha|/R_H)^(1/delta), extracting the top Fourier coefficient gives density derivative norms bounded below by a positive constant times n^(k-1-nu). The stream has one extra factor of order n^(-1). Therefore the sum of first density derivative norms and second stream derivative norms diverges; the individual second density and third stream derivative norms grow. These conclusions distinguish failure of absolute summability from failure of the term-to-zero condition. They do not exclude conditional convergence of the first density derivative series or differentiability obtained by another method. The angular-strip factor changes the critical radius by exp(B sigma/delta), with the density's exp(-sigma) factor independent of n.

Verdict: CONFIRMED for the exact highest-mode radius, its coefficient asymptotic, and the stated necessary derivative-radius bounds. They are upper bounds on the full convergence radius and necessary physical-radius conditions, not a theorem that the full series converges at or above those bounds. No new mathematical defect was found.
"""
review_path = base / "sources/final_top_mode_review_V662.md"
review_path.write_text(review)
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final highest-mode reread protocol\n\nRead the complete highest-frequency recurrence, complex coefficient asymptotic and critical derivative obstruction. Check every sign and half, positivity, the complex continuation step and the distinction between necessary and sufficient radii.\n\nCompleted {now}, V662. Three complete proof texts pass with no new mathematical defect. No new numerical replay or full-series radius equality is claimed.\n")
proof = base / "sources/PROOF_at_V662.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_top_mode_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Three complete highest-mode proofs pass the final manual review. The closed scalar recurrence, exact beta-integral radius, complex coefficient asymptotic and derivative obstruction are consistent. These give necessary physical-radius conditions; they do not identify the full-series convergence boundary."
scope = "CONFIRMED under the exact finite-support and prescribed-channel hypotheses; no new numerical replay or full-series radius equality is claimed."
p = base / "verification/admission_V662.json"
p.write_text(json.dumps(dict(at=now, entry=662, verdict="CONFIRMED",
    review_kind="manual mathematical reread, not a numerical replay",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review_path),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V662 | {now} | Final highest-mode radius and derivative review\n\n**Claim.** The exact highest-mode radius and its boundary derivative obstructions have the stated constants and scope.\n\n**Method.** Complete manual reread of three proof texts, checking the scalar recurrence, positivity, complex continuation, coefficient extraction and derivative norm lower bounds; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V662 highest-mode reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V662 records the manual reread of three highest-mode proofs, with no new defect and no numerical replay.\n")
print(now, result)
