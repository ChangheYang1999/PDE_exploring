"""Independent scalar integration of the S0 cutoff tails from the original NPZ."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import importlib.util,json,hashlib,math
import numpy as np
from flint import arb,ctx
P=Path(__file__).resolve().parents[1];LANE=P.parents[1]
spec=importlib.util.spec_from_file_location('own_scalar',LANE/'proofs/04_modal_scalar/code/recompute.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
ctx.prec=512;ctx.threads=1
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
raw=np.load(source,allow_pickle=False)
sha=hashlib.sha256(source.read_bytes()).hexdigest();assert sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
knots=list(map(m.rat,raw['knots']));k=m.rat(raw['k']);tp=knots[-1];nb=len(knots)-8
coef=[Q(i>=nb-10) for i in range(nb)]
spans=[i for i in range(7,len(knots)-8) if knots[i]<knots[i+1] and i>=nb-10]
assert len(spans)==10
z=arb(json.loads((LANE/'proofs/04_modal_scalar/evidence/recomputed.json').read_text())['normalization_correction_z']['ball'])
A=[m.aa(m.rat(raw['Aout'][i,0]))+(z if i==0 else 0) for i in range(5)]
B=[A[1]/2,A[0]+A[2]/2,(A[1]+A[3])/2,(A[2]+A[4])/2]
w=[Q(1,4),Q(1,8),Q(-1,8),Q(-1,8)]
CA=sum((m.aa(wi)*Ai for wi,Ai in zip(w,A)),arb(0))
CB=sum((m.aa(wi)*Bi for wi,Bi in zip(w,B)),arb(0))

def moments(z,N):
 out=[arb(0) for i in range(9)];term=arb(1)
 for n in range(N):
  for i in range(9):out[i]+=term/(i+n+1)
  term*=z/(n+1)
 az=arb(abs(z).upper());tail=az.exp()*az**N/math.factorial(N)
 return [v+arb(0,(tail/(N+i+1)).upper()) for i,v in enumerate(out)]

def calc(N):
 i0=arb(0);i1=arb(0)
 for i in spans:
  width=knots[i+1]-knots[i];tau=knots[i]-tp
  poly=m.deboor_poly(knots,coef,7,i)
  ms=moments(m.aa((k-1)*width),N)
  fac=m.aa(width)*m.aa((k-1)*tau).exp()
  i0+=fac*sum((m.aa(c)*ms[j] for j,c in enumerate(poly)),arb(0))
  i1+=fac*sum((m.aa(c)*(m.aa(tau)*ms[j]+m.aa(width)*ms[j+1]) for j,c in enumerate(poly)),arb(0))
 i0+=1/m.aa(1-k);i1+=1/m.aa((1-k)**2)
 fac=m.aa(2*tp).exp()
 cp=fac*CA*i0;ck=fac*CA*i1;ct=fac*CB*i0
 return {'I0':i0,'I1':i1,'cPhi':cp,'cKP_shifted':ck,'cTAU':ct,'cKP_logr':ck+m.aa(tp)*cp,'border_d_shifted':3/m.aa(k)+m.aa(k)*ck}
res=calc(80);alt=calc(128)
for name in res:assert res[name].overlaps(alt[name])
meta=json.loads((LANE.parent/'s2-num/work/runs/S0_M4_s60_o12/meta.json').read_text())
def ball4(v):
 a,e,r,s=map(int,v);return arb(a)*arb(2)**e+arb(0,(arb(r)*arb(2)**s).upper())
for name,key in [('cKP_shifted','cKP'),('cTAU','cTAU')]:
 assert res[name].overlaps(ball4(meta[key])),(name,res[name],ball4(meta[key]))
assert res['cKP_shifted']>0 and res['cTAU']>0
# Compare with the unshifted nonnegative-log convention, keeping the two distinct.
assert res['cKP_logr']>res['cKP_shifted']
assert res['border_d_shifted']>3/m.aa(k)
def record(x):
 def q(v):
  a,e=v.man_exp();return str(Q(int(a))*Q(2)**int(e))
 return {'ball':x.str(65),'lower_exact':q(x.lower()),'upper_exact':q(x.upper())}
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','input':str(source),'input_sha256':sha,'precision_bits':512,
 'method':'own exact rational de Boor, 80/128-term exponential moments with analytic remainder; exact outer half-line moments',
 'cutoff_spans':len(spans),'cutoff_start_exact':str(knots[spans[0]]),'tp_exact':str(tp),'results':{n:record(x) for n,x in res.items()},
 'numerics_comparison':'both independently integrated scalar balls overlap the original S0 meta balls',
 'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'evidence/recomputed.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
