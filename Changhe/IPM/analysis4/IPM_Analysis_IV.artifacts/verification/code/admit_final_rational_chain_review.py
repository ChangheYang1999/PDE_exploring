"""Record a manual reread of the rational-series convergence proof chain."""
from pathlib import Path
import json, sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct
base = Path('research/301_final_claim_audit')
paths = [
 'research/131_general_odd_period_majorant/PROOF.md',
 'research/132_general_period_potential/PROOF.md',
 'research/134_general_component_radius/PROOF.md',
 'research/144_general_rational_response_limit/PROOF.md',
 'research/145_general_rational_convergence/PROOF.md',
 'research/169_sharp_rational_poisson/PROOF.md',
 'research/171_resonance_block_majorant/PROOF.md',
 'research/172_certified_prefix_majorant/PROOF.md',
 'research/175_integer_period_prefix/PROOF.md',
 'research/188_finite_prefix_stationary_residual/PROOF.md',
 'research/223_tail_response_radii/PROOF.md',
 'research/226_integer_period_tail_radii/PROOF.md',
 'research/296_primary_weight_amplitude/PROOF.md',
]
for p in paths: assert Path(p).is_file(), p
ledger, text = next_entry(658)
now = stamp()
review = f'''# Final reread of rational convergence and finite residuals

Recorded {now}. This is a manual mathematical review of the thirteen proof texts hashed in admission_V658.json. It introduces no new theorem and does not replay the numerical certificates or recompute the algebraic response bounds.

## Initialization and response

For delta = 2/Q the first positive stream resonance is at order 2Q. There is no free H_Q, and the majorant must retain this zero. For delta = 2h/Q with coprime h >= 2 and Q > 2h, the first stream resonance is Q and its free H_Q is retained. In either case the first compatibility condition must hold before subsequent tuning begins. A positive uniform response bound is a further hypothesis, not a consequence of first compatibility.

In the Q-step response calculation, a product involving two copies of the new free harmonic cannot reach the next resonance: its earliest density order is 2n+1 > n+Q for n >= Q. The remaining dependence is affine. The limiting positive Fourier carrier includes the factor of two converting a positive complex Fourier coefficient into a sine coefficient. Each intermediate denominator is nonzero for 1 <= s < Q by coprimality. The limiting response and its finite exceptions must both be controlled; a nonzero limit alone does not exclude an earlier zero response.

## Majorant and period blocks

The restricted lookahead density pairs have both indices at least the lookahead step, so their indices do not exceed the already constructed base order. The restricted harmonic pairs use a density index at least Q+1, hence an earlier harmonic. The ordered low-index density pairs contribute the factor 2L. These restrictions make the scalar construction triangular even though it looks ahead to the next resonance.

The period-block projection uses w = z^Q and the residue Q for positive multiples of Q. Its first unknown density term is order 2Q, not Q. The factors w and w^2 in tail products follow from their total degree. The constant-level dependence is ordered as the lookahead components, then the harmonic component, then increasing density residues. Its affine matrix is strictly lower triangular; no contraction estimate on that matrix is assumed. Multiplication by its finite nonnegative inverse leaves a remainder with positive w degree.

A nonnegative supersolution box bounds monotone formal iteration at the stated positive w. Coefficientwise stabilization and monotone convergence then prove convergence of the majorant. Failure of a chosen box has no converse meaning. Each derivative costs only a fixed polynomial in the order, absorbed by a strict increase of the exterior radius. The physical radius associated with w0 is w0^(-1/(2h)), and the amplitude factor is |epsilon|^(Q/(2h)).

The sharp rational Poisson constant applies to the particular inverse after the entire resonant output is removed. The independent free harmonic must then be added separately. Applying the reduced two-channel expression inside a resonant output without that deletion would be invalid. The two-channel extremum and the separate first-sine channel produce the stated uniform bound.

## Certified prefixes and tails

A supplied prefix bound needs to enclose the true tuned coefficient; it need not satisfy the artificial scalar majorant recurrence. The prefix ends at N = MQ. Its last free harmonic H_N is still unknown and belongs to the tail. For h = 1 the initialization requires M >= 2 and the absent H_Q remains zero. The ordinary density inequality is applied only at orders at least N+1, which justifies its sharpened N-dependent constant. The ratio n/(n+Q) in the tuning estimate may be discarded upwards since it is at most one.

The prefix residue equations contain every known-known, known-tail and tail-tail product with its appropriate power of w. The harmonic products are ordered; the density cross terms carry their factor two. The same triangular affine argument applies. Tail-only response certificates begin at the first unknown tuning index. Earlier tuning divisions are justified by their own prefix certificates. An interval in the compactified response variable can be discarded only after proving it contains no permitted integer index; the limiting point at zero remains part of the tail argument. A finite failure of this test does not imply a true response zero.

## Common potential and residual

For h = 1 the only exceptional logarithmic potential corrections are at Q and 2Q. At Q, r^2 log r and r^2 log r cos(2 theta) supply the two missing density modes; their mixed derivatives give the stated pure stream modes. At 2Q, log r adjusts the resonant stream without changing density. At late orders the density primitive, Laplace inverse and harmonic adjustment preserve the same geometric base. For general coprime h >= 2 the exceptional orders are restricted as in topic 145. The conclusion is an exterior common potential, not a whole-plane stationary extension.

The finite residual contains exactly the ordered nonlinear pairs with total order J+1 through 2J, since the linear and nonlinear terms cancel through J. The Euler and angular derivative multipliers are |p_n|^a and (Bn)^b, and division by the leading density weight gives z^(n-1). Every coefficient of the bound is nonnegative, giving a uniform exterior estimate. A prefix ending with an untuned H_N cannot be used at J = N without separately bounding that harmonic. Residual smallness alone proves neither an infinite series nor an error bound to one.

For the leading radial weight, amplitude restoration carries |epsilon|/z times the normalized density or stream tail expression, as specified in topic 296. It is not permissible to omit that factor when epsilon differs from one. No unit-amplitude certificate changes under this correction.

## Verdict

CONFIRMED for the rational majorants, prefix-to-tail argument, potential reconstruction and finite residual estimate under the exact hypotheses in the source proofs. No new mathematical defect was found. Their exact numerical inputs and certified radii retain the scopes of their earlier receipts. This is a final argument review, not a new arithmetic replay or a complete reread of the assembled report.
'''
review_path = base/'sources/final_rational_chain_review_V658.md'
review_path.write_text(review)
protocol = '''\n## Final rational-chain reread protocol\n\nRead the complete current proofs of rational tuning, response limits, component and resonance-block majorants, certified prefixes, tail-only response bounds, sharp particular Poisson inversion, common potential, finite residuals and amplitude restoration. Check the first resonance separately for h=1 and h>=2, all total-order shifts and factors of two, triangularity at zero, nonnegative supersolution convergence, last-prefix-harmonic treatment and strict exterior derivative margin. Preserve the distinction between proof review and a fresh numerical replay.\n'''
with (base/'PROOF.md').open('a') as f:
 f.write(protocol + f'\nCompleted {now}, V658. All thirteen reviewed proof texts pass. No new mathematical defect was found; no new theorem or numerical certificate is introduced.\n')
proof = base/'sources/PROOF_at_V658.md'
proof.write_bytes((base/'PROOF.md').read_bytes())
algorithm = base/'sources/admit_final_rational_chain_review.py'
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base/'verification/post_freeze_20261031T235941Z/theory.json'
assert reconstruct(snapshot) == Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md').read_bytes()
result = ('Thirteen complete proof texts were reread. The two first-resonance initializations, affine Q-step tuning, ordered factors and period shifts, triangular supersolution argument, certified prefix and tail hypotheses, particular Poisson inverse, exceptional potential logarithms, finite residual and amplitude factors all retain their stated scope. No new mathematical defect was found. The lead theory remains identical to the reviewed 23:59:41Z snapshot.')
scope = 'CONFIRMED for this manual mathematical review under the exact hypotheses of the retained proofs. No fresh numerical replay, new theorem or complete assembled-report reread is claimed.'
p = base/'verification/admission_V658.json'
p.write_text(json.dumps(dict(at=now,entry=658,verdict='CONFIRMED',review_kind='manual mathematical reread, not a numerical replay',reviewed_proofs=[ref(p) for p in paths],review=ref(review_path),proof=ref(proof),algorithm=ref(algorithm),theory_snapshot=ref(snapshot),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text + f'\n## V658 | {now} | Final reread of rational convergence and finite residuals\n\n**Claim.** The rational majorants and their prefix, potential and residual consequences retain their stated hypotheses and conclusions.\n\n**Method.** Complete manual reread of thirteen proof texts, with a written account of initialization, factors, index shifts, supersolution convergence and scope; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
n = Path('NOTES_FOR_TEAM.md')
n.write_text(f'## {now} VERIFIER -> LEAD: V658 final rational-chain reread passes\n\n{result}\n\n{scope}\n\nNo report correction or new computation is requested. Both the irrational and rational central proof chains have now received the additional final reread recorded in V657/V658.\n\n' + n.read_text())
with Path('WORKLOG.md').open('a') as f:
 f.write(f'\n{now}: V658 records the final manual rational-chain reread of thirteen proof texts. No new defect found; no arithmetic replay claimed.\n')
print(now, result)
