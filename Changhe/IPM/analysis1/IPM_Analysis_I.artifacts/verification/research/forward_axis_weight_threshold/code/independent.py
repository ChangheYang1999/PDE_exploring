from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,json,hashlib
sys.dont_write_bytecode=True
from flint import fmpq
import sympy as s
R=Path(__file__).resolve().parents[3];D=R/'research/forward_axis_weight_threshold';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
start=now();p=load(E/'check.json');assert p['code_sha256']==sha(D/'code/check.py') and p['proof_sha256']==sha(D/'PROOF.md')
for n,h in p['parent_files'].items():assert sha(R/n)==h,n
j=R/'data_exact/modal_v2.json';assert sha(j)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
h=load(j)['scalars_hex']['k'];sign=-1 if h[0]=='-' else 1;h=h.lstrip('+-');mant,ex=h.split('p');ip,fp=mant[2:].split('.');k=sign*fmpq(int(ip+fp,16))*fmpq(2)**(int(ex)-4*len(fp))
A=(2-k)/k;Dval=(4-k)/k;b0=(1+k)/k
th=(Dval*fmpq(153,50)-b0)/A;phi=(Dval*fmpq(307,100)-b0)/A
vals={'k':k,'A':A,'D':Dval,'b0':b0,'theta_153_over_50':th,'phi_307_over_100':phi,'quadrant_counterexample_delta':fmpq(5,2)*A,'quadrant_counterexample_inverse_norm':2/(5*A),'Y_counterexample_delta_minus':A*fmpq(1,2)-fmpq(3,2)}
for n,v in vals.items():assert F(str(v))==F(p['exact'][n]),n
assert all(vals[n]>0 for n in ['A','D','quadrant_counterexample_delta','quadrant_counterexample_inverse_norm','Y_counterexample_delta_minus'])
lo,hi=map(F,p['theta_strict_window']);assert lo<F(str(th))<hi
Av,t,a=s.symbols('A t a',real=True);Dv=2*Av+1;bv=(Av+3)/2
DY=Dv*(t-s.Rational(1,2))-Av*(a-s.Rational(1,2))-1;DZ=Dv*t-Av*a-bv
identities=[s.factor(DY-DZ),s.factor(Av*(s.Rational(1,2)+(Dv*(t-s.Rational(1,2))-1)/Av-s.Rational(5,2))-Dv*(t-s.Rational(3,2))),s.factor(DZ.subs({t:s.Rational(3,2),a:0})-s.Rational(5,2)*Av),s.factor(-Av*(a-s.Rational(1,2))-1-Dv/2-(-Av*a-bv))]
assert identities==[0]*4
# Quantifier direction: strict midpoint construction if t<3/2.
threshold=s.factor((Dv*t-bv)/Av);mid=(threshold+s.Rational(5,2))/2
assert s.simplify(mid-threshold-Dv*(s.Rational(3,2)-t)/(2*Av))==0
assert s.simplify(s.Rational(5,2)-mid-Dv*(s.Rational(3,2)-t)/(2*Av))==0
# Physical group conjugation and Euler-derivative shifts, exact symbolic test on arbitrary powers.
u,v,nu,nv,c=s.symbols('u v nu nv c',real=True);G=s.exp(nu*u+nv*v);H=s.exp((a-s.Rational(1,2))*u+(t-s.Rational(1,2))*v)*G
trans=s.simplify(s.exp(-(a-s.Rational(1,2))*u-(t-s.Rational(1,2))*v)*(-Av*s.diff(H,u)+Dv*s.diff(H,v)-H)/G)
assert s.simplify(trans-(-Av*nu+Dv*nv+DZ))==0
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_INTEGER_HEX_FMPQ_AND_SYMBOLIC_GENERAL_THRESHOLDS','code_sha256':sha(Path(__file__)),'check_sha256':sha(E/'check.json'),'parent_pin_count':len(p['parent_files']),'exact_values_compared':len(vals),'general_symbolic_identities':4,'strict_midpoint_quantifier_identities':2,'group_conjugation_power_identity':True,'theta_strict_window':p['theta_strict_window'],'PDE_endpoint':'UNRESOLVED'}
with (E/'independent.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
