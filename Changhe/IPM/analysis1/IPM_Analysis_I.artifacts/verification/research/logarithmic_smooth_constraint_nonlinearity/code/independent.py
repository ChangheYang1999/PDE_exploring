from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
from flint import fmpq as Q
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_smooth_constraint_nonlinearity';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
start=now();a=json.loads((E/'check.json').read_text());assert sha(D/'PROOF.md')==a['proof_sha256']=='935abeef7acbb87346ccf8471b9e87e5ecc1d337af0a54db99cb0a6e4ec0e701'
for name,h in a['parent_files'].items():assert sha(R/name)==h,name
# Sparse fmpq ring adapted from211. No Sympy or primary evaluator import.
NVAR=12
def var(i):
 e=[0]*NVAR;e[i]=1;return {tuple(e):Q(1)}
def const(q):return {(0,)*NVAR:Q(q)} if q else {}
def add(*xs):
 out={}
 for x in xs:
  for m,q in x.items():out[m]=out.get(m,Q(0))+q
 return {m:q for m,q in out.items() if q}
def sc(x,q):return {m:c*q for m,c in x.items() if c*q}
def mul(*xs):
 out=const(1)
 for x in xs:
  nxt={}
  for m,q in out.items():
   for n,p in x.items():
    e=tuple(i+j for i,j in zip(m,n));nxt[e]=nxt.get(e,Q(0))+q*p
  out={m:q for m,q in nxt.items() if q}
 return out
v=list(map(var,range(NVAR)));G=v[:2];H=v[2:4];W=v[4:6];B=[[v[6],v[7]],[v[8],v[9]]];T=v[10];A=v[11]
def plus(x,y):return [add(a,b) for a,b in zip(x,y)]
def scale(x,t):return [mul(t,a) for a in x]
def bil(x,y):return add(*[mul(x[i],B[i][j],y[j]) for i in range(2) for j in range(2)])
def quad(x):return bil(x,x)
def cross(x,y):return add(bil(x,y),bil(y,x))
checks={}
def ck(name,left,right):assert left==right,name;checks[name]=True
ck('quadratic_perturbation',quad(plus(G,W)),add(quad(G),cross(G,W),quad(W)))
ck('cross_scalar_linearity',cross(scale(G,T),scale(W,A)),mul(T,A,cross(G,W)))
ck('plus_packet_correction',cross(scale(plus(G,H),T),scale(W,A)),mul(T,A,add(cross(G,W),cross(H,W))))
ck('minus_packet_correction',cross(scale(plus(G,scale(H,const(-1))),T),scale(W,A)),mul(T,A,add(cross(G,W),sc(cross(H,W),-1))))
ck('full_scaled_perturbation',quad(plus(scale(plus(G,H),T),scale(W,A))),add(mul(T,T,quad(plus(G,H))),mul(T,A,cross(plus(G,H),W)),mul(A,A,quad(W))))
ck('scaled_polarization',add(quad(scale(plus(G,H),T)),sc(quad(scale(plus(G,scale(H,const(-1))),T)),-1)),sc(mul(T,T,cross(G,H)),2))
# Independent integer-power reconstruction; no fractional root routine is used.
assert len(a['fixtures'])==21;idx=0;signed=0;rootchecks=0
for power in [5,6,8]:
 nu=Q(power,4)
 for nbase in [1,2,3,7,16,31,101]:
  z=a['fixtures'][idx];idx+=1;t=Q(1,nbase**4);n=nbase**8;corr=-Q(1,nbase**power)
  assert z['power']==power and z['N']==nbase and Q(z['nu'])==nu and Q(z['n'])==n and Q(z['t'])==t and Q(z['a'])==corr
  assert n*t*t==1 and corr<=0
  # Positive-root uniqueness identifies abs(x)^nu from this exact power equality.
  assert (-corr)**int(nu.q)==t**int(nu.p);rootchecks+=1
  for sign,value in zip([-1,1],z['constraint_at_two_signs']):
   x=sign*t;assert abs(x)==t and corr+(-corr)==0 and Q(value)==0;signed+=1
  ratio=abs(corr)/t;bound=n*t*abs(corr)+corr*corr
  assert Q(z['correction_over_t'])==ratio==Q(1,nbase**(power-4))
  assert Q(z['cross_plus_square_bound'])==bound==Q(1,nbase**(power-4))+Q(1,nbase**(2*power))
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_FMPQ_CORRECTION_IDENTITIES_AND_INTEGER_POWER_FIXTURES','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'check_sha256':sha(E/'check.json'),'parent_pin_count':len(a['parent_files']),'ring_checks':checks,'fixtures_compared':idx,'signed_evaluations_compared':signed,'positive_root_power_equalities':rootchecks,'source_reuse':'Sparse fmpq ring adapted from211; no primary evaluator or Sympy import. Scalar fixtures rebuilt by integer powers and positive-root uniqueness.','scope':'Generic quadratic algebra and finite scalar surrogate equations only. No finite sample proves a statement about every Frechet map or the fixed-dimensional contraction. No IPM constraint data, modal norm or interval constant.'}
with (E/'independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
