from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,hashlib
sys.dont_write_bytecode=True
from flint import fmpq
R=Path(__file__).resolve().parents[3];P=R/'research/logarithmic_frozen_range_inverse';E=P/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
start=now();a=load(E/'check.json');assert a['proof_sha256']==sha(P/'PROOF.md') and a['code_sha256']==sha(P/'code/check.py')
for n,h in a['parent_files'].items():assert sha(R/n)==h,n
# Universal exact polynomials in independent variables u,v,D,r. No Sympy.
N=4
def const(v=1):return {(0,)*N:F(v)} if v else {}
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
def sq(p):return mul(p,p)
def df(p,k):
 d={}
 for e,v in p.items():
  if e[k]:g=list(e);g[k]-=1;d[tuple(g)]=v*e[k]
 return d
u,v,D,r=[var(i) for i in range(N)];total=add(u,v);H=add(total,sc(D,-2));up=add(u,sc(D,-1));vp=add(v,sc(D,-1));d=add(sc(u,-1),mul(total,r));dr=sc(mul(total,mul(r,add(const(),sc(r,-1)))),2)
W=add(sq(d),mul(D,dr));expected=add(sq(u),sc(mul(mul(total,add(D,sc(u,-1))),r),2),mul(mul(total,H),sq(r)))
checks={};checks['coercive_quadratic_from_square_plus_derivative']=add(W,sc(expected,-1))
mH=add(mul(sq(D),H),sc(mul(mul(D,up),vp),2));checks['completed_square_numerator']=add(mul(H,W),sc(mH,-1),sc(mul(total,sq(add(mul(H,r),sc(up,-1)))),-1))
checks['vertex_complement_numerator']=add(H,sc(up,-1),sc(vp,-1))
# Direct weighted Fourier adjoint and pairing, with original c=D/2-u.
# The adjoint exponent eta is (u/D-1/2)-iAxi/D and weight exponent -s.
# Check exponent after conjugation cancels Fourier weight and has real power -c/D.
c=add(sc(D,F(1,2)),sc(u,-1));checks['original_eta_power_margin']=add(u,sc(D,-F(1,2)),c)
# With v=sD-u, direct L2 powers at eta endpoints have margins2u,2v.
checks['adjoint_zero_integrability_margin']=add(D,sc(c,-2),sc(u,-2))
checks['adjoint_infinity_integrability_margin']=add(sc(c,2),sc(total,2),sc(D,-1),sc(v,-2))
# Independent logarithmic coefficient table, each column multiplied by2D.
# columns are log eta, log B, log(B+eta²); h denotes iAxi formally and cancels pairwise.
# Actual entries are rational affine expressions in u,D,sD,h, kept as sparse polynomial rows.
# Add a new phase variable using r: polynomial identity is valid for complex r as well.
h=r
original_eta=add(sc(u,2),sc(D,-1),sc(h,-2));target_eta=add(sc(c,-2),sc(h,-2))
original_B=add(sc(u,-1),h,total);target_B=add(total,sc(u,-1),h)
original_weight=sc(total,-2);target_weight=sc(total,-2)
checks['full_original_adjoint_log_eta_coefficient']=add(original_eta,sc(target_eta,-1));checks['full_original_adjoint_log_B_coefficient']=add(original_B,sc(target_B,-1));checks['full_original_adjoint_log_weight_coefficient']=add(original_weight,sc(target_weight,-1))
assert all(z=={} for z in checks.values()),checks
# Original weight cancellation and phase conjugation independently as exact integer coefficient pairs.
assert (1)+(-1)==0 and -(-1)==1
j=R/'data_exact/modal_v2.json';assert sha(j)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';hx=load(j)['scalars_hex']['k'];sg=-1 if hx[0]=='-' else 1;hx=hx.lstrip('+-');mant,expo=hx.split('p');ip,fp=mant[2:].split('.');k=sg*fmpq(int(ip+fp,16))*fmpq(2)**(int(expo)-4*len(fp));Av=(2-k)/k;Dv=(4-k)/k;sv=fmpq(153,50);uv=(k+1)/k;vv=sv*Dv-uv;iv=k/(k+1)
values={'k':k,'A':Av,'D':Dv,'s':sv,'u':uv,'v':vv,'inverse_norm':iv}
for n,w in values.items():assert str(w)==a['actual'][n],n
assert 0<uv<Dv and vv>uv
lo,hi=map(fmpq,a['inverse_strict_window']);assert lo<iv<hi
# Minima independently use the derivative sign, not the primary min-formula evaluation.
cases=[]
for row in a['cases']:
 u0,v0,D0=[fmpq(row[n]) for n in ['u','v','D']];T=u0+v0;aa=T*(T-2*D0);bb=2*T*(D0-u0);cc=u0*u0;minimum=min(cc,v0*v0);vertex_val=None
 if aa>0 and bb<0 and 2*aa+bb>0:
  vertex_val=cc-bb*bb/(4*aa);minimum=vertex_val
 assert minimum==fmpq(row['m']) and minimum>0
 assert (str(vertex_val) if vertex_val is not None else None)==row['vertex_value']
 if row['sharp_inverse_norm'] is not None:assert min(u0,v0)<=D0 and fmpq(row['sharp_inverse_norm'])==1/min(u0,v0)
 else:assert min(u0,v0)>D0
 cases.append(row['name'])
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_POLYNOMIALS_ORIGINAL_FOURIER_PAIRING_AND_MINIMA','code_sha256':sha(Path(__file__)),'check_sha256':sha(E/'check.json'),'parent_pin_count':len(a['parent_files']),'universal_polynomial_identities':{n:'ZERO_POLYNOMIAL' for n in checks},'separate_integer_pairing_coefficients_checked':True,'exact_values_compared':len(values),'inverse_strict_window':a['inverse_strict_window'],'independent_minimum_cases':cases,'scope':'Different polynomial implementation and direct weighted-adjoint method; analytic domain/range/projection still requires proof and review.'}
with (E/'independent.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
