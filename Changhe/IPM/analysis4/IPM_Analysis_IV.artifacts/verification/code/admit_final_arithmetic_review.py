"""Record a manual check of arithmetic and generic-data divergence quantifiers."""
from pathlib import Path
import json, sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct
base = Path("research/301_final_claim_audit")
paths = ["research/"+s+"/PROOF.md" for s in [
 "18_liouville_convergence", "37_generic_analytic_data",
 "46_quantitative_divergence", "49_algebraic_quantitative_divergence",
 "52_metric_amplitude_divergence", "80_compatibility_size_criterion"]]
ledger, text = next_entry(660)
now = stamp()
review = f"""# Final arithmetic and generic-data quantifier review

Recorded {now}. Six complete proof texts were read and checked. This is a manual argument review, not a numerical replay or a new claim about the arithmetic boundary of convergence.

The explicit continued-fraction construction in topic 18 makes log(q_(k+1))/q_k summable while violating every polynomial Diophantine bound. Grouping q_(N+r) >= 2^floor(r/2) q_N gives the two stated elementary geometric sums. The convergent error is smaller than 1/(q_k q_(k+1)); multiplication by two preserves the Liouville conclusion after reduction because denominators remain at least q_k/2. The finite-prefix cylinder argument gives density. This establishes convergent Liouville parameters, not convergence at every Liouville parameter.

For generic analytic leading data, each fixed-order coefficient is a continuous homogeneous polynomial into a smaller strip and hence into C^0. A compatibility polynomial is nonzero on the single-sine direction, so its zero set has empty interior. Countably many rational centers give a residual set of data. At a fixed divergent parameter, the Banach-valued Chebyshev estimate on a line segment transfers one divergent datum to a residual set of data. This second argument proves no full-measure statement. The distinct quantifiers in parameter and data are retained.

The rational-profile common denominator counts internal nodes and selected velocity subtrees by disjoint leaf sets of a fixed mass. The factor 4a at an internal node accounts for the stream and trigonometric halves after the stream numerator p cancels the radial denominator p. The product over both stream channels is an allowed overestimate. Reversing the divisor sum gives S_p <= (pi^2/12)p^2 + (p/2)(1+log p); multiplying by the two logarithmic powers of p yields B pi^2/6. The remaining factors are lower order on the p^2 log p scale.

On the complex disk of radius 1/(4p^2), each nonresonant linear stream divisor stays at least 3/(4p) from zero. The resonant boundary divisor has modulus 1/(4p), so the common 4p stream bound covers that boundary too. Only the order-p stream can have a pole in the order-(p+1) density recurrence. Multiplication by the parameter displacement removes the simple pole, and Cauchy gives the stated remainder. Compact localization precedes using a center-independent stationary-inverse bound. Topic 80 explicitly retains this localization; its historical unlocalized version is not approved.

For number-field input, a common integer makes the coefficients integral. The nonzero algebraic-integer norm and bounds on the other conjugates cost the field-degree factor d in the leading height exponent. The finite set of exceptional primes is harmless along infinitely many distinct prime approximants. Nonzero real scalar multiplication preserves divergence by order-n homogeneity; no claim about arbitrary transcendental coefficient vectors follows from this height argument.

For a fixed analytic higher-mode profile and variable first amplitude x, the compatibility polynomial has degree p and the single-sine compatibility as leading coefficient. If its value is smaller than that coefficient times r^p, one complex root lies within r; intersecting with the real line is covered by an interval centered at the real part of that root. At most p roots for each of fewer than p numerators give p^2 intervals. Their p^(-eta p) radii have summable s-powers for every s>0. The countable union over eta=1/m, together with x=0, therefore has Hausdorff dimension zero and is independent of delta and tau.

The residue amplitude at frequency 2j+1 contains only the first input mode and mode 4j+1. Analytic decay makes the latter negligible for each fixed nonzero x as j tends to infinity. The shrinking-strip remainder remains exp(O(p log p)), below the pole term p^(epsilon p^2). Choosing eta so that pi^2/3+2eta<tau proves the stated simultaneous threshold. It does not prove necessity of the Brjuno condition or divergence at all non-Brjuno parameters.

Verdict: CONFIRMED with the exact input classes, strict thresholds, localization and quantifiers in the six retained proofs. No new mathematical defect was found. The numerical tables and earlier finite tests have not been rerun.
"""
review_path = base/"sources/final_arithmetic_review_V660.md"
review_path.write_text(review)
with (base/"PROOF.md").open("a") as f:
 f.write(f"\n## Final arithmetic-boundary reread protocol\n\nCheck complete proofs of convergent Liouville examples, generic analytic data, rational and algebraic height bounds, the metric first-amplitude theorem and the localized actual-compatibility criterion. Verify denominator counts, the compact pole disk, the root-cover estimate and all exceptional-set quantifiers.\n\nCompleted {now}, V660. Six complete proof texts pass with no new mathematical defect. No numerical replay or characterization of the full arithmetic boundary is claimed.\n")
proof=base/"sources/PROOF_at_V660.md";proof.write_bytes((base/"PROOF.md").read_bytes())
algorithm=base/"sources/admit_final_arithmetic_review.py";algorithm.write_bytes(Path(__file__).read_bytes())
snapshot=base/"verification/post_freeze_20261031T235941Z/theory.json"
assert reconstruct(snapshot)==Path("../a4-lead/FARFIELD_CONVERGENCE_THEORY.md").read_bytes()
result="Six complete arithmetic and generic-data proofs pass the final manual review. The denominator-height constant, localized simple-pole remainder, number-field degree, root-cover Hausdorff bound and exceptional-set quantifiers are consistent. Convergent Liouville examples and sufficient divergent approximation classes remain distinct; necessity of Brjuno remains open."
scope="CONFIRMED under the exact hypotheses of the retained proofs; no new arithmetic replay or full characterization of convergence is claimed."
p=base/"verification/admission_V660.json"
p.write_text(json.dumps(dict(at=now,entry=660,verdict="CONFIRMED",review_kind="manual mathematical reread, not a numerical replay",reviewed_proofs=[ref(p) for p in paths],review=ref(review_path),proof=ref(proof),algorithm=ref(algorithm),theory_snapshot=ref(snapshot),result=result,scope=scope),indent=2)+"\n")
ledger.write_text(text+f"\n## V660 | {now} | Final arithmetic and generic-data quantifier review\n\n**Claim.** The arithmetic sufficient conditions and generic-data conclusions have the stated constants and quantifiers.\n\n**Method.** Complete manual reread of six proof texts; check the elementary denominator, complex-disk, norm and small-value-set arguments; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n")
n=Path("NOTES_FOR_TEAM.md");n.write_text(f"## {now} VERIFIER -> LEAD: V660 arithmetic and generic-data reread passes\n\n{result}\n\nNo report correction is requested. The theory remains identical to the reviewed 23:59:41Z snapshot.\n\n"+n.read_text())
with Path("WORKLOG.md").open("a") as f:f.write(f"\n{now}: V660 records the manual reread of six arithmetic and generic-data proofs, with no new defect and no numerical replay.\n")
print(now,result)
