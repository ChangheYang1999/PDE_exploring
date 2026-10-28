from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
import numpy as np
from flint import arb,ctx
ctx.prec=384;ctx.threads=1
P=Path(__file__).resolve().parents[1];ROOT=P.parents[1]
def aa(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def beta(x,y):return x.gamma()*y.gamma()/(x+y).gamma()
def txt(x):return x.str(100)
source=ROOT/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
with np.load(source,allow_pickle=False) as f:
 kq=Q(float(f['k']));tpq=Q(float(f['knots'][-1]));ac=[Q(float(f['Aout'][m,0])) for m in range(4)]
k=aa(kq);ell=1/k;A=2*ell-1;D=4*ell-1;b0=ell+1
knots=list(map(Q,['0','1.5','1.75','3','4','5','6','7','8','9','10']))
slopes=[Q(n,16) for n in [4,17,28,27,25,18,4,-10,-17,-19,-20]]
mu=Q(0);I=arb(0);pieces=[]
for i,(left,right) in enumerate(zip(knots,knots[1:])):
 rate=Q(4)+slopes[i];width=right-left
 value=aa(-4*left-mu).exp()*(1-aa(-rate*width).exp())/aa(rate)
 I+=value;pieces.append({'left':str(left),'right':str(right),'mu_left':str(mu),'slope':str(slopes[i]),'integral':txt(value)})
 mu+=slopes[i]*width
value=aa(-4*knots[-1]-mu).exp()/aa(4+slopes[-1]);I+=value
Cfar=(I/arb.pi()).sqrt()
repair=ROOT/'proofs/04_modal_scalar/evidence/recomputed.json'
z=arb(json.loads(repair.read_text())['normalization_correction_z']['ball'])
s3overpi=(sum((aa(v)*aa(w) for v,w in zip(ac,[Q(1,4),Q(1,8),Q(-1,8),Q(-1,8)])),arb(0))+z/4)*((3-k)*aa(tpq)).exp()
assert s3overpi>arb('37.63077494715565') and s3overpi<arb('37.63077494715567')
kpcbound=s3overpi/(1-k)**2
assert k*kpcbound<3*ell
results=[]
for aq,bq in [(Q(7,2),Q(6,5)),(Q(17,4),Q(0))]:
 a=aa(aq);b=aa(bq);sigma=a+b-4;kap=b0+a*A-b*D
 Cr2=2*(9*beta(a+aa(Q(1,2)),b+aa(Q(3,2)))-24*beta(a+aa(Q(1,2)),b+aa(Q(5,2)))+16*beta(a+aa(Q(1,2)),b+aa(Q(7,2))))/(arb.pi()**2*(2*a+2*b-4))
 Cr=Cr2.sqrt();Cv=1/(8*(sigma*(sigma+1)*(sigma+2)).sqrt());Cang=(2*beta((9-2*a)/2,(3-2*b)/2)).sqrt()
 CF=Cr/kap;Cg=Cv/D+Cr*(A+D)*Cang/(D*kap);Cc=(CF*CF+Cg*Cg).sqrt();Ccap=(aa(Q(1,64))+Cv*Cv+Cr2+Cfar*Cfar).sqrt()
 results.append({'a':str(aq),'b':str(bq),'kappa':txt(kap),'C_R':txt(Cr),'C_v':txt(Cv),'C_ang':txt(Cang),'C_F':txt(CF),'C_gamma':txt(Cg),'C_c0':txt(Cc),'C_cap':txt(Ccap)})
 if aq==Q(7,2):
  assert CF<arb('0.0027316') and Cg<arb('0.0136875') and Cc<arb('0.013958')
  assert Ccap<arb('0.312093') and Ccap<arb('0.31210')
 assert Cc<arb('0.017231')
assert Cfar<arb('0.273629')
result={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','k_exact':str(kq),'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'s3_over_pi':txt(s3overpi),'k_cKP_bound_for_cutoff_after_R1':txt(k*kpcbound),'three_ell':txt(3*ell),'repair_evidence_sha256':hashlib.sha256(repair.read_bytes()).hexdigest(),'I':txt(I),'C_far':txt(Cfar),'general_far_bound':txt((1/(arb.pi()*aa(Q(11,4)))).sqrt()),'intervals':pieces,'tail':txt(value),'constants':results,'lead_snapshot_sha256':hashlib.sha256((P/'evidence/lead_snapshot.md').read_bytes()).hexdigest()}
if (P/'PROOF.md').exists():result['proof_sha256']=hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest()
(P/'evidence/check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
