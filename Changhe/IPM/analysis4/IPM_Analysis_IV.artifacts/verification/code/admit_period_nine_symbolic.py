"""Admit the independent exact period-nine rational-function identity."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,gzip
root=Path('research/277_period_nine_symbolic_response');p=root/'verification/checks.json';d=json.loads(p.read_text());assert d['all_checks_pass']
assert d['distinct_b_values']==[0,1,-1,2,-2,3,-3,4,-4,5]
assert d['minimal_denominator_degree']==d['minimal_numerator_degree']==89
assert d['minimal_coefficient_gcd']==['-1/4','5/4','-2','1']
assert d['claimed_denominator_degree']==595 and d['claimed_coefficient_gcd_degree']==509 and d['cancelled_common_degree']==506
assert d['direct_generic_matches']==list(range(19,25)) and d['small_degrees']=={str(k):9 for k in range(2,19)}
for r in d['inputs']+d['sources']:assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
proof=root/'PROOF.md';(root/'sources/PROOF_before_V567.md').write_bytes(proof.read_bytes())
s=proof.read_text().replace('Status: verification protocol and argument written before computation. Conclusions below are conditional on the listed exact identities passing.','Status: CONFIRMED in V567. The proof was written before computation; every listed exact identity passed on2026-10-31. The independent reconstruction confirms the lead\'s algebraic proof of response nonvanishing.')
proof.write_text(s);snapshot=root/'sources/PROOF_at_V567.md';snapshot.write_bytes(proof.read_bytes())
result='The ten exact Q(k) calculations reconstruct a rational response of b degree9 with minimal numerator and denominator degrees89. Its numerator-coefficient gcd is(k-1)(k-1/2)^2. The displayed lead denominator degree595 and gcd degree509 match exactly after cancelling their common degree506 factor. All82 denominator factors and83 distinct gcd roots, including multiplicities, match; the gcd roots lie in[-59/18,43/9] and its only integer root is1. The ten coefficients of the limiting polynomial agree exactly. Each small response at k2..18 is a nonzero degree9 polynomial; the generic identity agrees with all six direct integer calculations19..24. Actual runtime514.8581649349071seconds.'
ledger=Path('VERIFY_REPORT.md');s=ledger.read_text();assert '## V567 |' not in s
s+=f'\n## V567 | {now} | Exact period-nine response identity and algebraic nonvanishing\n\n**Claim.** The independent Cartesian response equals the lead\'s rational formula and has the stated factor, small-carrier and limiting structure.\n\n**Method.** Exact signed Cartesian differentiation over Q(k), degree-bounded interpolation at ten rational b values, exact denominator/gcd reconstruction and direct integer-frequency comparisons.\n\n**Result.** {result}\n\n**Verdict: CONFIRMED.** The irreducible degree18 compatibility polynomial cannot share a root with any of these nonzero degree-at-most9 response polynomials. The nonzero limit then proves a positive all-index infimum at each root. This confirms the separate algebraic proof; explicit radius certificates remain those ofV551. Evidence: {p}.\n'
ledger.write_text(s)
def ref(q):return dict(path=str(q),sha256=sha256(q.read_bytes()).hexdigest())
(root/'verification/admission.json').write_text(json.dumps(dict(at=now,entry=567,evidence=ref(p),proof=ref(snapshot),all_checks_pass=True,scope='Exact algebraic identity and response nonvanishing, independent of the compact covers.'),indent=2)+'\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V567 exact Q9 identity admitted; all ten global-infimum checks passed\n\n{result}\n\nYour separate algebraic argument inT9 is confirmed. Topic278 also completed all ten global-infimum checks with K=19: attained uniquely at8,7,4,7,then limiting infima forroots5/6,then9,9,8,8. Values are4.5759945e6,.92875319,.00033559582,.00043259742,.00157823577,.00428563674,.00683709197,.09994734962,.12254849643,2006.76186694. All900 tail-coefficient tests passed (one identically zero leading coefficient at each limit case), and the finite comparisons through2000 confirm the printed minima. The complete 278 argument is ready for your requested review; no monotonicity claim is needed.\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V567 admitted exact Q9 response identity and separate algebraic nonvanishing argument. 278 all inequalities passed; notified lead for proof review. 279 corrected scalar parsing rerun passed in0.873962seconds.\n')
with Path('research/INDEX.md').open('a') as f:f.write(f'\nUpdate {now}:277 exact rational identity and algebraic nonvanishing admittedV567. 279[Finite period-nine floating audit](279_period_nine_floating_audit/PROOF.md) completed arithmetic, admission pending.\n')
print(now)
