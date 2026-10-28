import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import sympy as s
from flint import arb,ctx
P=Path(__file__).resolve().parents[1];LANE=P.parents[1]
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
f=np.load(source,allow_pickle=False)
k=Q(float(f['k']));ell=1/k;c=3*ell-1;A=2*ell-1;D=4*ell-1
a=Q(17,4);eta=Q(5,4)
k0=1+ell+a*A;kinf=1+ell-eta*ell/2
assert k0>0 and kinf>0 and D>0 and ell>0
assert k0==Q(19,2)*ell-Q(13,4) and kinf==1+Q(3,8)*ell
L,z=s.symbols('L z',real=True)
AA=2*L-1;DD=4*L-1;aa=s.Rational(17,4)
q=-AA*z+DD*(1-z);tang=(AA+DD)*(1-z)
assert s.expand(1+L-aa*q+aa*tang-(1+L+aa*AA))==0
assert s.expand(-2*AA+DD-1)==0
assert s.expand(q-DD+(AA+DD)*z)==0
r,x,y,H,cc=s.symbols('r x y H cc',positive=True)
psi=cc*x*y-x*y*(x*x+y*y)/6+4*H*x*y*(x*x-y*y)
flead=-s.diff(psi,x,2)-s.diff(psi,y,2)
assert s.expand(flead-2*x*y)==0
vals={}
for bits in (256,512):
 ctx.prec=bits;ctx.threads=1
 def ball(q):return arb(q.numerator)/q.denominator
 res={'kappa_origin':ball(k0),'kappa_infinity':ball(kinf),'axis_D':ball(D),'axis_ell':ball(ell),'minus_limit_a1':ball(-2*c)}
 if vals:
  assert all(res[name].overlaps(vals[name]) for name in res)
 vals=res
out={'date_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'exact':{'kappa_origin':str(k0),'kappa_infinity':str(kinf),'axis_D':str(D),'axis_ell':str(ell),'limit_a1':str(-2*c)},
 'balls':{name:v.str(70) for name,v in vals.items()},'precisions_bits':[256,512],
 'symbolic_checks':['origin energy coefficient is angle-independent','origin p constant vanishes','q-d quotient is -(A+D)','quartic stream has -Laplacian 2xy'],
 'scope':'Endpoint constants and symbolic identities only. No explicit asymptotic cutoffs or global margin.',
 'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest()}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
