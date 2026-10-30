"""Exact weighted-membership cutoff from an independently confirmed rounded sector."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import time
from flint import arb, fmpq as Q, ctx

R=Path(__file__).resolve().parents[3]
B=R/'research/rounded_weighted_membership'
def H(p):return sha256(p.read_bytes()).hexdigest()
def ar(q):return arb(int(q.numerator))/arb(int(q.denominator))
t0=time.monotonic();ctx.prec=512
p=R/'research/rounding_realization/verification/C1-N1-007-d2w-j7-e2bal.json'
d=json.loads(p.read_text())
assert d['canonical_source_sha256']=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
assert d['realized_canonical_sha256']=='3e8a0d9b2bf4349978e2e3c5d25cc79c1905729279e7b2c84508f3d1ebb1e369'
assert d['stored_binary64_matches_correct_rounding']
c=Q(4076476460239181,2251799813685248)
alpha=2/c-1;critical=alpha+1
lead=d['leading_nonzero_forbidden_sector']
assert lead['h']==1 and lead['q']==0 and Q(lead['exponent'])==alpha
assert 0<alpha<1 and not lead['rounded_exact_zero']
preceding=next(x for x in d['forbidden_sectors'] if (x['h'],x['q'])==(0,0))
assert preceding['rounded_exact_zero']
A=arb(lead['rounded_full_circle_norm']);assert A>0
B_lower=ar(1-alpha**2)*A;assert B_lower>0
paths=[p,Path(__file__),B/'PROOF.md',
 R/'research/rounding_realization/PROOF.md',
 R/'research/rounding_realization/peer_review/T4/results.json',
 R/'research/rounding_realization/peer_review/T4/PROOF.md']
output={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'binary64 coefficient realization of C1-N1-007-d2w-j7-e2bal',
 'precision_bits':ctx.prec,'alpha_exact':str(alpha),'alpha':ar(alpha).str(90),
 'critical_a_exact':str(critical),'critical_a':ar(critical).str(90),
 'leading_residual_angular_norm':A.str(90),'leading_laplacian_angular_norm_lower':B_lower.str(90),
 'weights':{str(Q(k,4)):('INFINITE' if Q(k,4)<=critical else 'FINITE') for k in range(7)},
 'inputs':{str(x.relative_to(R)):H(x) for x in paths},
 'elapsed_seconds':time.monotonic()-t0,
 'status':'N4-origin analytic consequence, OPEN independent review; exact published candidate excluded from this claim'}
out=B/'verification/candidate007.json';assert not out.exists();out.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
