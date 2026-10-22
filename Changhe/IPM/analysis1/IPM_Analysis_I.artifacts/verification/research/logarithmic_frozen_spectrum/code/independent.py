from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,hashlib
sys.dont_write_bytecode=True
from flint import fmpq
R=Path(__file__).resolve().parents[3];P=R/'research/logarithmic_frozen_spectrum';E=P/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
start=now();a=load(E/'check.json');assert a['proof_sha256']==sha(P/'PROOF.md') and a['code_sha256']==sha(P/'code/check.py')
for n,h in a['parent_files'].items():assert sha(R/n)==h,n
# No Sympy: universal exact polynomial dictionaries in c,D,s,q,h.
# h represents the imaginary frequency i*A*xi algebraically; identities are polynomials over Q and hold for complex h.
N=5
def one(v=1):return {(0,)*N:F(v)} if v else {}
def var(i):e=[0]*N;e[i]=1;return {tuple(e):F(1)}
def add(*ps):
 d={}
 for p in ps:
  for e,v in p.items():d[e]=d.get(e,F(0))+v
 return {e:v for e,v in d.items() if v}
def sc(p,k):return {e:v*k for e,v in p.items() if v*k}
def mul(p,q):
 d={}
 for e,u in p.items():
  for f,v in q.items():g=tuple(x+y for x,y in zip(e,f));d[g]=d.get(g,F(0))+u*v
 return {e:v for e,v in d.items() if v}
def df(p,k):
 d={}
 for e,v in p.items():
  if e[k]:g=list(e);g[k]-=1;d[tuple(g)]=v*e[k]
 return d
c,D,s,q,h=[var(i) for i in range(N)];den=add(one(),q);dm=add(c,sc(D,-F(1,2)));dp=add(dm,mul(s,D));pot=add(mul(dm,den),mul(mul(s,D),q));checks={}
# Conjugation of eta*d_eta, after multiplying by1+q. Jacobian givesD/2, Fourier phase cancels h.
chain=add(mul(add(c,sc(D,-1),sc(h,-1)),den),mul(D,add(sc(den,F(1,2)),mul(s,q))),mul(h,den))
checks['full_conjugation_numerator']=add(chain,sc(pot,-1))
# Direct original Fourier weighted adjoint; no use of the unitary potential in this independent derivation.
adj_log_deriv_D=add(mul(add(sc(c,-1),sc(h,-1)),den),sc(mul(mul(s,D),q),-2))
adj_coefficient=add(mul(add(c,h),den),sc(mul(mul(s,D),q),2))
checks['direct_weighted_adjoint_ODE']=add(adj_log_deriv_D,adj_coefficient)
# For the original Fourier kernel eta^((c-D-h)/D), the two L2 power-integrability margins.
checks['kernel_zero_margin']=add(add(sc(c,2),sc(D,-1)),sc(dm,-2))
checks['kernel_infinity_margin']=add(add(D,sc(c,-2),sc(mul(s,D),-2)),sc(dp,2))
# Adjoint eta^(-(c+h)/D)*(1+xi²+eta²)^(-s); norm includes one positive Sobolev weight.
checks['adjoint_zero_margin']=add(add(D,sc(c,-2)),sc(dm,2))
checks['adjoint_infinity_margin']=add(add(sc(c,2),sc(mul(s,D),2),sc(D,-1)),sc(dp,-2))
# Differentiate d(q)=pot/(1+q), with partial_tau=2q partial_q.
der_num=sc(mul(q,add(mul(df(pot,3),den),sc(pot,-1))),2)
checks['potential_derivative_numerator']=add(der_num,sc(mul(mul(s,D),q),-2))
checks['right_tail_numerator']=add(mul(dp,den),sc(pot,-1),sc(mul(s,D),-1))
checks['left_tail_numerator']=add(pot,sc(mul(dm,den),-1),sc(mul(mul(s,D),q),-1))
# Rational positive remainders for1/(1+q)<=1/q andq/(1+q)<=q, q>0.
checks['right_tail_inequality_positive_remainder']=add(den,sc(q,-1),one(-1))
checks['left_tail_inequality_positive_remainder']=add(mul(q,den),sc(q,-1),sc(mul(q,q),-1))
# Gauge byexp(-i Im(lambda)tau/D) contributes+h, canceling the imaginary shift-h.
checks['spectral_phase_cancellation']=add(h,sc(h,-1))
assert all(v=={} for v in checks.values()),checks
# Independent manual exact hexadecimal k, never using npz or binary floating point.
j=R/'data_exact/modal_v2.json';assert sha(j)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';hx=load(j)['scalars_hex']['k'];sgn=-1 if hx[0]=='-' else 1;hx=hx.lstrip('+-');mant,expo=hx.split('p');ip,fp=mant[2:].split('.');k=sgn*fmpq(int(ip+fp,16))*fmpq(2)**(int(expo)-4*len(fp));Av=(2-k)/k;Dv=(4-k)/k;bv=1+1/k
exact={'k':k,'A':Av,'D':Dv,'b0':bv}
for n,v in exact.items():assert F(str(v))==F(a['exact'][n]),n
assert 0<k<fmpq(1,2) and Av>3
casechecks=[]
for row in a['cases']:
 aa=fmpq(row['a']);ss=fmpq(row['s']);cv=-Av*aa+Av/2-1;dminus=cv-Dv/2;dplus=cv+Dv*(ss-fmpq(1,2))
 assert str(dminus)==row['d_minus'] and str(dplus)==row['d_plus']
 if row['classification']=='forward':assert dplus<0 and dminus<=dplus;iv=-1/dplus
 elif row['classification']=='backward':assert dplus>=dminus>0;iv=1/dminus
 elif row['classification']=='interior_infinite_cokernel':assert dminus<0<dplus;iv=None
 elif row['classification']=='right_endpoint':assert dminus<0 and dplus==0;iv=None
 elif row['classification']=='collapsed_endpoint':assert ss==0 and dminus==dplus==0;iv=None
 else:raise AssertionError(row['classification'])
 assert (str(iv) if iv is not None else None)==row['inverse_norm'];casechecks.append(row['classification'])
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_GENERAL_POLYNOMIALS_DIRECT_FOURIER_ADJOINT_AND_EXACT_PARAMETERS','code_sha256':sha(Path(__file__)),'check_sha256':sha(E/'check.json'),'parent_pin_count':len(a['parent_files']),'universal_polynomial_identities':{n:'ZERO_POLYNOMIAL' for n in checks},'independent_adjoint_method':'Original Fourier weighted adjoint and both endpoint power-integrability margins, separately from the unitary reduction. Infinite-dimensional realization remains analytic proof.','exact_scalar_values_compared':4,'exact_parameter_cases_checked':casechecks,'scope':'Exact identities and scalar examples do not by themselves prove any spectrum or PDE claim.'}
with (E/'independent.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
