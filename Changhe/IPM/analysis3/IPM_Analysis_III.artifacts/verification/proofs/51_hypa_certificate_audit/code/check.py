"""Small independent exact tests for certificate arithmetic and identities."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as s
from flint import arb,ctx
P=Path(__file__).resolve().parents[1]
LANE=P.parents[1]
ctx.prec=256;ctx.threads=1
x=s.symbols('x', real=True)
# x=sin(theta), z=cos(theta)^2=1-x^2.
# cos(2n theta)=(-1)^n T_(2n)(x).
identities=[]
for n in range(1,20):
    u=s.chebyshevu(n-1,x)
    identity=(-1)**n*(s.chebyshevt(2*n,x)-1)+2*(-1)**n*(1-x*x)*u*u
    assert s.expand(identity)==0
    # tan(theta)sin(2n theta)=(-1)^(n+1)x U_(2n-1)(x).
    gn=2*(-1)**n*sum(((s.chebyshevu(j-2,x)**2 if j>=2 else 0)+s.chebyshevu(j-1,x)**2 for j in range(1,n+1)),s.Integer(0))
    identity=(-1)**(n+1)*(x*s.chebyshevu(2*n-1,x)-2*n)-(1-x*x)*gn
    assert s.expand(identity)==0
    identities.append(n)
# Exact upper endpoint becomes smaller after a plain float conversion.
endpoint=arb(2)**(-1200)
float_endpoint=float(endpoint.upper())
radius_ball=arb(0,float_endpoint)
assert float_endpoint==0.0 and not radius_ball.contains(endpoint)
# Floating multiplication is not a directed upper bound.
b=math.nextafter(1.0,math.inf)
assert Q(b*b)<Q(b)**2
# Failed endpoint cells are excluded by the snapshot's finite filtering.
DD2=np.array([1.0,np.inf]);DP2=np.array([2.0,3.0])
left=[i for i in range(2) if np.isfinite(DD2[i])]
assert left==[0] and float(np.nanmax(DD2[left]))==1.0
# Cell crossing zero: e^(-2t)|a0| can be strictly smaller than |a0| at t>0,
# so a crossing cell must contribute to both weighted and unweighted maxima.
crossing={'t_left':-1,'t_right':1,'a0':'exp(2*t)','weighted_sup':1,'unweighted_sup':'exp(2)>1'}
# Source near resonance for the inner B_27 correction.
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
f=np.load(source,allow_pickle=False)
bi=Q(float(f['bi']));lam=bi+4-2*27
assert lam>0 and lam<Q(1,10**11)
log2growth=7*math.log2(1/float(lam))
out={'date_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'symbolic_identity_modes':identities,'float_endpoint_counterexample':{'exact':'2^-1200','rounded':float_endpoint,'radius_contains_exact':False},
 'float_square_counterexample':{'input':b.hex(),'rounded_square':str(Q(b*b)),'exact_square':str(Q(b)**2)},
 'coverage_counterexample':{'DD2':['1','infinity'],'included_cells':left,'reported_max':1},'crossing_cell_counterexample':crossing,
 'inner_B27_near_resonance':{'lambda_exact':str(lam),'lambda_float':float(lam),'seventh_inverse_power_log2':log2growth,'interpretation':'Diagnostic conditioning, not a proved bound on final interval widths'},
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'snapshot_sha256':hashlib.sha256((P/'evidence/hypA_snapshot.py').read_bytes()).hexdigest(),
 'scope':'The identities are confirmed; the snapshot is not a sound certificate until rounding and coverage defects are repaired.'}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
