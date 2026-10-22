from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import sys,json,hashlib
sys.dont_write_bytecode=True
import numpy as np
import sympy as s
R=Path(__file__).resolve().parents[3];P=R/'research/logarithmic_frozen_spectrum';E=P/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
start=now();pf=load(E/'proof_first.json');assert pf['proof_sha256']==sha(P/'PROOF.md')=='14827c0b6cf6ca602e73a8ac5ed29cea56040a10d02fac37787c44e41d7c9ada'
rel='research/forward_axis_weight_threshold/evidence/verdict.json';assert sha(R/rel)=='6525af41c5435d37868b79a8a0dd1532129685225c7d1b2b17a82838c9a547b2';parent=load(R/rel);pins=dict(parent['files']);pins[rel]=sha(R/rel)
for n,h in pins.items():assert sha(R/n)==h,n
# Arbitrary-parameter symbolic differential reconstruction.
A,D,c,d0,ss,xi,tau,t,q,r,u,v=s.symbols('A D c d0 s xi tau t q r u v',real=True);Dpos=s.symbols('Dp',positive=True);qp=s.symbols('qp',positive=True)
logW=tau/2+ss*s.log(1+s.exp(2*tau))/2
V=s.Function('V')(tau);inverse=s.exp(-s.I*A*xi*tau/D-logW)*V
conjugated=s.simplify(s.exp(s.I*A*xi*tau/D+logW)*(-D*s.diff(inverse,tau)+(c-D-s.I*A*xi)*inverse))
dtau=c-D/2+ss*D*s.exp(2*tau)/(1+s.exp(2*tau))
checks={}
checks['full_fourier_chain']=s.simplify(conjugated-(-D*s.diff(V,tau)+dtau*V))
logAmplitude=(c-D/2)*t+ss*(s.log(1+s.exp(2*tau))-s.log(1+s.exp(2*(tau-D*t))))/2
checks['group_amplitude_derivative']=s.simplify(s.diff(logAmplitude,t)-dtau.subs(tau,tau-D*t));checks['group_amplitude_at_zero']=s.simplify(logAmplitude.subs(t,0))
d=d0+ss*D*s.exp(2*tau)/(1+s.exp(2*tau));M=s.exp(d0*tau/D)*(1+s.exp(2*tau))**(ss/2);g=1/M
checks['kernel_ODE']=s.simplify(-D*s.diff(M,tau)+d*M);checks['adjoint_ODE']=s.simplify(D*s.diff(g,tau)+d*g)
checks['log_jacobian']=s.simplify(s.diff(s.sqrt(1+xi**2)*s.exp(tau),tau)-s.sqrt(1+xi**2)*s.exp(tau))
checks['potential_derivative']=s.simplify(s.diff(d,tau)-2*ss*D*s.exp(2*tau)/(1+s.exp(2*tau))**2)
dq=d0+ss*D*q/(1+q)
checks['right_tail']=s.factor((d0+ss*D-dq)*(1+q)-ss*D);checks['left_tail']=s.factor((dq-d0)*(1+q)-ss*D*q)
checks['right_exponential_bound']=s.factor(1/q-1/(1+q)-1/(q*(1+q)));checks['left_exponential_bound']=s.factor(q-q/(1+q)-q*q/(1+q))
H=s.Function('H')(tau);phase=s.exp(-s.I*v*tau/D)
checks['spectral_imaginary_gauge']=s.simplify((-D*s.diff(phase*H,tau)+(d-u-s.I*v)*phase*H)-phase*(-D*s.diff(H,tau)+(d-u)*H))
a,order=s.symbols('a order',real=True);Dm=2*A+1;b0=(A+3)/2
checks['actual_minus']=s.simplify(-A*(a-s.Rational(1,2))-1-Dm/2-(-A*a-b0))
checks['actual_plus']=s.simplify((-A*a-b0+Dm*order)- (Dm*(order-s.Rational(1,2))-A*(a-s.Rational(1,2))-1))
assert all(z==0 for z in checks.values()),checks
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as z:k=F.from_float(float(z['k'].item()))
Av=2/k-1;Dv=2*Av+1;bv=(Av+3)/2;assert 0<k<F(1,2) and Av>3
cases=[]
for aa,ssv,name in [(F(6),F(153,50),'forward'),(F(-1),F(153,50),'backward'),(F(0),F(153,50),'interior_infinite_cokernel'),(F(5,2),F(3,2),'right_endpoint'),(-bv/Av,F(0),'collapsed_endpoint')]:
 dm=-Av*aa-bv;dp=dm+Dv*ssv
 category='backward' if dm>0 else 'forward' if dp<0 else 'interior_infinite_cokernel' if dm<0<dp else 'right_endpoint' if dp==0 and dm<0 else 'collapsed_endpoint' if dm==dp==0 else 'UNEXPECTED'
 assert category==name
 inv=1/(-dp) if dp<0 else 1/dm if dm>0 else None
 cases.append({'a':str(aa),'s':str(ssv),'d_minus':str(dm),'d_plus':str(dp),'classification':category,'inverse_norm':str(inv) if inv is not None else None})
out={'start_utc':start,'utc':now(),'status':'PASS_GENERAL_SYMBOLIC_REDUCTION_AND_EXACT_PARAMETER_CASES_REQUIRES_INDEPENDENT_REVIEW','proof_sha256':sha(P/'PROOF.md'),'code_sha256':sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'parent_path':rel,'parent_sha256':sha(R/rel),'symbolic_identities':{n:str(v) for n,v in checks.items()},'exact':{'k':str(k),'A':str(Av),'D':str(Dv),'b0':str(bv)},'cases':cases,'scope':'Symbolic and exact scalar application; infinite-dimensional classification rests on standalone proof, not cases.'}
with (E/'check.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'parent_pin_count':len(pins),'symbolic_identity_count':len(checks),'cases':cases}))
