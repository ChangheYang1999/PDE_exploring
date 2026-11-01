"""Record the final manual reread of the central mathematical proof chain."""
from pathlib import Path
import json, sys
sys.dont_write_bytecode = True
from certificate_admission import stamp, ref, next_entry
from reconstruct_text_delta import reconstruct
base = Path('research/301_final_claim_audit')
paths = [
 'research/01_recurrence/PROOF.md',
 'research/06_conditional_convergence/PROOF.md',
 'research/13_lead_theory_audit/PROOF.md',
 'research/14_analytic_data/PROOF.md',
 'research/15_conditional_divergence/PROOF.md',
 'research/31_prime_denominator_obstruction/PROOF.md',
 'research/32_constructive_divergence/PROOF.md',
 'research/42_real_profile_prime_obstruction/PROOF.md',
 'research/43_peer_review_closure/PROOF.md',
 'research/76_error_level_majorant/PROOF.md',
 'research/108_exterior_existence_audit/PROOF.md',
 'research/109_exterior_potential_reconstruction/PROOF.md',
 'research/110_fixed_order_exterior_existence/PROOF.md',
 'research/297_asymptotic_growth_discontinuity/PROOF.md',
]
for p in paths: assert Path(p).is_file(), p
ledger, text = next_entry(657)
now = stamp()
review = f'''# Final reread of the central mathematical chain

Recorded {now}. This is a manual mathematical review of the exact files hashed in admission_V657.json. The proofs themselves remain in their topic folders. This review introduces no new theorem and does not replay their numerical certificates.

## Convergence and potential

The density-to-stream formula has both neighboring Fourier channels, with opposite signs in its reduced form. The nonlinear sum is over ordered pairs; inserting a factor of one half would change the stationary equation. The radial coefficient is (n-1)(c-1), with the sign obtained by moving the linear stationary contribution to the other side. The independent Cartesian derivation and the polar formula agree.

The scalar normalization Y_n = n ||f_n|| / d_n leaves a factor 1/d_n at the root of every interaction tree. The continued-fraction argument controls products of these factors, rather than replacing each by a polynomial loss. In the compressed forest of marked vertices, the terminal and unary charges use disjoint sets of leaves; the number of branching vertices is no greater than the number of terminal vertices. Thus the bound 2n/q_k is valid. The constant-alpha factor has n-1 copies, while the error-level exponential has exponent 2n E. This gives the prefactor alpha/(4K) and also bounds the one-leaf case.

The potential inversion has a downward triangular density-to-Laplacian step followed by the angular Laplacian inverse. For late orders its norm is at most C_chi ||f_n||/d_n, with finite C_chi at the fixed irrational parameter. It does not introduce another exponential small-divisor loss. The finitely many earlier inverses are nonsingular. Angular bandwidth and radial degrees grow linearly with n, so each fixed Cartesian derivative costs only a polynomial factor. The strict exterior margin absorbs it. Four potential derivatives suffice for the displayed stationary equation; the theorem supplies every fixed derivative. Weighted uniform convergence does not assert bounded unweighted density at infinity.

The analytic-data proof uses a strictly smaller target strip. Its derivative estimate handles the zero-order Nagumo exponent by a limit, and the finitely many early potential inverses use a polynomial Fourier loss absorbed by a strip decrease. Its parameter result is continuity and a common radius on compact Brjuno sublevel sets. It is not continuity of the actual limsup growth constant on an unrestricted interval. The large-c radius-128 family retains the integer hypothesis N >= 16.

## Obstruction and divergence

At the first incompatible stream resonance, the density of that same order is still regular. The next density order has a nonzero simple pole because its highest output harmonic has coefficient proportional to (L+gamma) times the nonzero highest input coefficient. There is only one ordered pair using the singular stream at that order. Thus no unexamined cancellation is needed in the Baire argument.

The prime obstruction first applies to rational finite profiles, with finitely many input primes excluded. The arbitrary-real extension uses a finitely generated coefficient algebra and preserves the nonzero first harmonic under a suitable finite-field specialization. It proves density of incompatible rational parameters for each fixed finite real profile with a nonzero first harmonic; it supplies no uniform quantitative lower bound for arbitrary real coefficients. The earlier conditional statement in topic 15 is closed for this class by topics 31, 42 and 43.

The dense-G_delta divergence conclusion and full-measure Brjuno convergence conclusion refer to different notions of typicality and are compatible. The growth constant is finite at every Brjuno point and infinite on the proved dense set. Its resulting discontinuity at Brjuno points does not conflict with the restricted parameter continuity theorem. No assertion of necessity of the Brjuno condition is obtained.

## A fixed finite truncation

The corrected exterior-existence construction fixes N, a weight and a regularity order before choosing the radius. Its weighted Poisson multiplier excludes its stated indicial weights. The transport energy identity has the helpful outward boundary sign, while the damping is 1-c beta > 0. The nonlinear contraction estimates the coefficient difference in L2 and the differentiated iterate in Linfinity. It does not make the false infinite-volume Linfinity-to-L2 inference rejected in the earlier draft.

The Sobolev limit uses k >= 4. Uniqueness is in the specified auxiliary half-cylinder equation with fixed cutoff and all chosen constants; it is not uniqueness among arbitrary exterior solutions. The common-potential reconstruction and pressure period argument preserve the reflection symmetries. None of these arguments constructs one fixed-radius smooth solution with every finite truncation as its asymptotic expansion, proves summability of a divergent canonical series, or proves a whole-plane canonical stationary extension.

## Verdict

CONFIRMED for the central convergence, obstruction, divergence and fixed-truncation proof chains with the hypotheses just stated. No new mathematical defect was found in this reread. The source proofs and their earlier repairs remain the complete arguments; this record identifies the delicate steps checked again. No new whole-report reading or fresh arithmetic replay is claimed.
'''
review_path = base/'sources/final_critical_chain_review_V657.md'
review_path.write_text(review)
protocol = '''\n## Final critical-chain reread protocol\n\nRead the complete current proofs of the recurrence, conditional reconstruction, Brjuno and analytic-data convergence, first-pole and prime obstruction, constructive divergence, error-level majorant, fixed-truncation existence and its repaired draft, common potential, and growth discontinuity. Check the derivative, arithmetic, uniqueness and parameter-topology hypotheses against the final theorem statements. Record a digest for each reviewed text and distinguish a manual reread from a new numerical replay. The conclusion is limited to those arguments and their exact hypotheses.\n'''
with (base/'PROOF.md').open('a') as f: f.write(protocol + f'\nCompleted {now}, V657. The fourteen proof texts pass the recorded final critical-chain review. No new mathematical defect was found; no new theorem or numerical certificate is introduced.\n')
proof = base/'sources/PROOF_at_V657.md'
proof.write_bytes((base/'PROOF.md').read_bytes())
algorithm = base/'sources/admit_final_critical_chain_review.py'
algorithm.write_bytes(Path(__file__).read_bytes())
snapshot = base/'verification/post_freeze_20261031T235941Z/theory.json'
assert reconstruct(snapshot) == Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md').read_bytes()
result = ('Fourteen complete proof texts were reread, including the recurrence, Brjuno tree estimate, analytic-data extension, potential inverse, prime obstruction and Baire argument, constructive divergence, sharper error-level constant, growth discontinuity, and the corrected fixed-truncation exterior construction. The strict derivative margin, smaller-strip topology, first-harmonic restriction, integer large-c parameter and auxiliary uniqueness class are preserved. No new mathematical defect was found. The lead theory remains identical to the reviewed 23:59:41Z snapshot.')
scope = 'CONFIRMED for this manual mathematical review with the exact hypotheses of the retained proofs. No fresh numerical replay, new theorem or cover-to-cover assembled-report reading is claimed.'
p = base/'verification/admission_V657.json'
p.write_text(json.dumps(dict(at=now,entry=657,verdict='CONFIRMED',review_kind='manual mathematical reread, not a numerical replay',reviewed_proofs=[ref(p) for p in paths],review=ref(review_path),proof=ref(proof),algorithm=ref(algorithm),theory_snapshot=ref(snapshot),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text + f'\n## V657 | {now} | Final reread of the central mathematical chain\n\n**Claim.** The central proof chains retain their stated mathematical hypotheses and conclusions.\n\n**Method.** Complete manual reread of fourteen proof texts, with a written account of the delicate estimates and scope restrictions; compare the lead theory by exact reconstruction.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
n = Path('NOTES_FOR_TEAM.md')
n.write_text(f'## {now} VERIFIER -> LEAD: V657 final critical-chain reread passes\n\n{result}\n\n{scope}\n\nThe numerics lane has already posted its final summary at 23:03Z, with subsequent corrections through 23:37Z. No new computation or report change is requested. I will check any final editorial changes against the retained report snapshot before cutoff.\n\n' + n.read_text())
with Path('WORKLOG.md').open('a') as f: f.write(f'\n{now}: V657 records the final manual critical-chain reread of fourteen proof texts. No new defect found; no arithmetic replay claimed.\n')
print(now, result)
