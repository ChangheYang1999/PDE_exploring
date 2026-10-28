"""Exact original-k arithmetic and symbolic normal-family identities."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
raw=np.load(source,allow_pickle=False);k=F.from_float(float(raw['k']))
assert k==F(1615536043799051,9007199254740992)
ell=1/k;A=2*ell-1;D=4*ell-1;Sig=A+D;delta=F(9,5);s0=F(41,20);sigma=F(25,4)
mx=Sig*(F(3,2)-s0)+delta*A;my=Sig*(sigma-F(1,2))-delta*D;l2=delta*D-2*Sig
assert mx==(3*ell-7)/10 and my==(273*ell-97)/10 and l2==(11-24*ell)/5
assert max(-mx,-my,l2)==-mx and mx>0 and delta*D-Sig>0
As,Ds,S,dd,ix,lam,x=s.symbols('A D Sigma delta ixi lambda x')
q=-As+S*x;beta=1+((dd+ix)*As+lam)/S;alpha=((dd+ix)*Ds-lam)/S;a=beta-1
assert s.expand((3*q-1+S*(1-3*x)).subs(S,3*As+1))==0
assert s.simplify((a+alpha-dd-ix).subs(S,As+Ds))==0
hom=s.expand(S*(a*(1-x)-alpha*x)+(dd+ix)*q-lam)
assert s.simplify(hom.subs(S,As+Ds))==0
# Source-side and vertical-side exact Euler conjugation coefficients.
assert s.simplify((3+dd+ix)*q-1-lam+S*((1-x)*beta-x*(2+alpha))) .subs(Ds,2*As+1).subs(S,3*As+1).simplify()==0

def encl(v,digits=14):
 scale=10**digits;lo=(v.numerator*scale)//v.denominator;hi=lo+1
 assert F(lo,scale)<=v<F(hi,scale)
 def dec(n):return ('-' if n<0 else '')+str(abs(n)//scale)+'.'+str(abs(n)%scale).zfill(digits)
 return {'exact':str(v),'lower':str(F(lo,scale)),'upper':str(F(hi,scale)),'decimal_lower':dec(lo),'decimal_upper':dec(hi)}
vals={'k':k,'ell':ell,'m_x':mx,'m_y':my,'lambda_2':l2,'Lambda_0':-mx,'trace_resonance':delta*D,'first_derivative_resonance':delta*D-Sig,'far_threshold':-1-ell/2}
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','original_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'values':{name:encl(v) for name,v in vals.items()},'symbolic_checks':['factor identity','homogeneous exponent sum','homogeneous cofactor equation','homogeneous bulk equation'],'scope':'fixed xi; no uniform large-frequency estimate'}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
