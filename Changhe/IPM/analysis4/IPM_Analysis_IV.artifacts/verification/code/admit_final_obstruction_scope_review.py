"""Record the final manual review of projection and general-input obstructions."""
from pathlib import Path
import json
import sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct

base = Path("research/301_final_claim_audit")
paths = ["research/" + s + "/PROOF.md" for s in [
    "55_fixed_angular_projection", "83_weighted_norm_nonnecessity",
    "86_distance_weight_obstruction", "89_sharp_column_weight",
    "92_halfline_poisson_obstruction", "105_fuchsian_scope",
]]
ledger, text = next_entry(664)
now = stamp()
review = f"""# Final projection and general-input obstruction review

Recorded {now}. Six complete proof texts were manually reread. This checks the included arguments, not a new execution of their finite examples or a new inspection of the cited original literature.

At fixed angular bandwidth only finitely many stream resonances can occur. The log degree bounds follow from the triangular polynomial inverses. Above the stated finite order the two Poisson factors have size at least 3n delta/4, while the log derivative has norm at most n delta/16. The resulting stream bound is C_P/n times the density norm. The stationary inverse and the two ordered nonlinear orientations give the stated Catalan majorant. Evaluating log polynomials introduces powers of log r; their product with r^(-delta(n-1)) is decreasing on the chosen far exterior. The proof treats the first stream term separately instead of assuming log r bounded. Fixed derivatives add only polynomial order factors. Thus every fixed projection converges, but its constants need not remain bounded as the band grows. Coefficient agreement with the unprojected recursion does not give a uniform band limit.

The factorial-norm counterexample derives density and stream from one radial potential. Its polynomial factors, canonical zero resonance at order six, and exact second-order residual are consistent. The termwise radial decay dominates the growing log powers on r>=e, while the factorial coefficient norm has logarithmic growth rate one third. The nonzero second-order stationary residual is essential: this is not an example of a convergent generated stationary sequence with uncontrolled factorial norm.

The common-center distance norm examples each use one density harmonic and the first factored Poisson channel. In the first example the small shift is 2/3 and the density distance is 1/3; comparing the constant output gives the factor (3/4)2^k. In the second example the density and stream distances are 5/3 and 2/3. Comparing the top log coefficient gives (3/4)(8/5)^k, independent of the fixed multiplier C. Both obey the stated support and log-degree bounds, but neither is asserted to arise from nonlinear evolution.

For rational delta=a/b the smallest nonzero factor shift is gcd(a,2)/b. The congruence used to attain that shift has arbitrarily large positive solutions, allowing each prescribed log degree. The finite inverse and the integration operator give the sufficient factorial scale s>b/gcd(a,2). Summing all output coefficients at the attained shift shows failure also at equality. At a resonant mode the constant is removed after combining both channels; deleting it contracts this coefficient norm. The bound does not need an additional factor two. The delta=2/3 example therefore correctly refutes the previously proposed stronger necessary scale b.

For the half-line norm, the elementary generating function bound gives e(k+1) for the weighted Laguerre input. Its canonical polynomial inverse at the boundary is exactly mu^(-1)(1+2 eta/mu)^k. The chosen congruence embeds this scalar example in an admissible nonresonant stream channel. The half-line solution with zero boundary value has a different homogeneous term and a bounded norm; it changes the prescribed stream class. The sign distinction for a negative factor shift follows from its integral toward increasing t.

The transformed equations in the Fuchsian-scope proof have the same signs as the original recurrence. Their joint Poisson symbol has infinitely many exact resonances, and the displayed nonresonant sequence violates the proposed quadratic separation. The direct local-angle equation retains a nonzero coefficient of the second angular derivative at z=0. The recorded literature hypotheses therefore cannot be invoked for that unchanged representation. This review retains the earlier direct-source audit and makes no new claim about other reductions or theorems.

Finally, the shifted arbitrary-input sequence in that proof respects the sharper canonical degree bound, including h=1. Its single selected output channel has fixed shift 2(1-delta), so the constant output contains k! divided by that shift to power k+1. The analytic two-variable density lift is a geometric series on the stated angular strip, yet the stream coefficient sums have no geometric bound. This disproves an unrestricted inverse estimate, not convergence of the actual generated stationary sequence.

Verdict: CONFIRMED for the projected equation and the specified general-input or representation obstructions. None proves divergence of the full canonical stationary series, and none licenses a uniform limit over angular bandwidth. No new mathematical defect was found.
"""
review_path = base / "sources/final_obstruction_scope_review_V664.md"
review_path.write_text(review)
with (base / "PROOF.md").open("a") as f:
    f.write(f"\n## Final projection and obstruction reread protocol\n\nRead six complete projection, norm and representation-obstruction proofs. Check the explicit test sequences, sharp scale, log evaluation and separation from the generated nonlinear sequence.\n\nCompleted {now}, V664. These proofs pass within their stated scope. No finite arithmetic or literature-source replay is claimed.\n")
proof = base / "sources/PROOF_at_V664.md"
proof.write_bytes((base / "PROOF.md").read_bytes())
algorithm = base / "sources/admit_final_obstruction_scope_review.py"
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base / "verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot) == Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result = "Six complete projection and operator-obstruction proofs pass the final manual review. Fixed-band convergence, the sharp factorial scale, distance and half-line counterexamples, and the analytic-input obstruction retain their exact scopes. These general-input examples do not prove divergence of the generated stationary recurrence."
scope = "CONFIRMED for the stated projected equation and general-input counterexamples; no numerical or literature-source replay and no conclusion about full canonical logarithmic convergence is claimed."
p = base / "verification/admission_V664.json"
p.write_text(json.dumps(dict(at=now, entry=664, verdict="CONFIRMED",
    review_kind="manual mathematical reread, not an arithmetic or source replay",
    reviewed_proofs=[ref(q) for q in paths], review=ref(review_path),
    proof=ref(proof), algorithm=ref(algorithm), theory_snapshot=ref(snapshot),
    result=result, scope=scope), indent=2) + "\n")
ledger.write_text(text + f"\n## V664 | {now} | Final projection and operator-obstruction review\n\n**Claim.** The projected convergence and inverse-obstruction arguments have the stated scopes and do not settle the full nonlinear series.\n\n**Method.** Complete manual reread of six proofs, checking the inverse bounds, explicit inputs, log evaluation and transformed equations; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n = Path("NOTES_FOR_TEAM.md")
n.write_text(f"## {now} VERIFIER -> LEAD: V664 projection and obstruction scope passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n" + n.read_text())
with Path("WORKLOG.md").open("a") as f:
    f.write(f"\n{now}: V664 records the manual reread of six projection and general-input obstruction proofs, with no new defect.\n")
print(now, result)
