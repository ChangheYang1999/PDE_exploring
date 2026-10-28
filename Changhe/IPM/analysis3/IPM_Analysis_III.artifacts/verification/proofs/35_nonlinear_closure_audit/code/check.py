from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json
import numpy as np
P=Path(__file__).resolve().parents[1]
R=P.parents[1]
s=R/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
with np.load(s,allow_pickle=False) as z:
    k=Q(float(z['k']));a=Q(float(z['Aout'][-1,0]));tp=Q(float(z['knots'][-1]));M=int(z['M'])
assert 0<k<Q(5,16) and M==260 and a!=0
n=2*(M-1)+3
assert n==521
# Exact highest sine-mode coefficient, omitting the positive common exponential factor.
A=a/8
p=(k-n)*A/(2*((n+1)**2-(k+1)**2))
assert p==-A/(2*(n+k+2))
c=(-k*(n+1)+(k+1)*n)*p*A/2
assert c==-(n-k)*A*A/(4*(n+k+2)) and c<0
for q in [k-Q(1,100),k+Q(1,100)]:
    assert 0<q<Q(5,16)
    assert 2*max(q,k)-1 > q+k-1
    assert 2*max(q,k)-1 < -Q(3,8)
    assert q+2*k-2 < 2*max(q,k)-1
# Algebra of the augmented scalar row: 3+k^2 cKP = k(3/k+k cKP).
for cp in [Q(0),Q(1,8),Q(71,1000)]:
    d=3/k+k*cp
    assert 3+k*k*cp==k*d
out={
 'date':datetime.now(timezone.utc).isoformat(), 'result':'PASS',
 'source':str(s.relative_to(R)), 'source_sha256':hashlib.sha256(s.read_bytes()).hexdigest(),
 'highest_density_frequency':n, 'highest_interaction_frequency':2*n+1,
 'Aout_259_0':str(a), 'theta_coefficient_before_exp':str(A),
 'positive_exponential_factor':'exp((3-k)t_plus)', 't_plus':str(tp),
 'nonzero_interaction_coefficient_before_exp_squared':str(c),
 'radial_membership_condition':'max(q,k)<5/16',
 'lead_snapshot_sha256':hashlib.sha256((P/'evidence/lead_snapshot.md').read_bytes()).hexdigest(),
 'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest()
}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
