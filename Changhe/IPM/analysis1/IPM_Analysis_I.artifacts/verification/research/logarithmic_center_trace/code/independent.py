from pathlib import Path
from math import comb
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq as Q
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_center_trace';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();primary=p.load(E/'check.json');p.rehash(primary['parent_files']);assert p.sha(D/'PROOF.md')==primary['proof_sha256']=='1520a97d475afcfd62a464c32d7549d299d2d33ddf3ef24776528006ecdd3f58'
raw=R/'data_exact/modal_v2.json';assert p.sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=p.load(raw)
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');whole,frac=m[2:].split('.');return Q(sign*int(whole+frac,16))*Q(2)**(int(e)-4*len(frac))
k=hx(raw['scalars_hex']['k']);AA=Q(2*k.q-k.p,k.p);DD=Q(4*k.q-k.p,k.p)
actual={'k':k,'A':AA,'D':DD,'D_minus_2A':DD-2*AA,'example_weight':Q(3,2),'example_decay_power':Q(5,2)-Q(3,2),'s':Q(153,50)};assert {n:str(v) for n,v in actual.items()}==primary['actual'] and AA>0
# Rational differential ring. Exponents correspond to u,y,delta,a,beta,A,D.
# Independent cutoff jets and eta jets are differentiated by the Leibniz rule.
def mon(powers=(0,)*7,jets=(),c=1):return {(tuple(powers),tuple(sorted(jets))):Q(c)} if c else {}
def var(i,n=1):
 v=[0]*7;v[i]=n;return mon(v)
def jet(name,i=0,j=0):return mon(jets=((name,i,j),))
def add(*parts):
 out={}
 for f in parts:
  for t,c in f.items():out[t]=out.get(t,Q(0))+c
 return {t:c for t,c in out.items() if c}
def scale(f,c):return {t:v*c for t,v in f.items() if v*c}
def mul(f,g):
 out={}
 for (a,j),c in f.items():
  for (b,jj),cc in g.items():
   t=(tuple(v+w for v,w in zip(a,b)),tuple(sorted(j+jj)));out[t]=out.get(t,Q(0))+c*cc
 return {t:c for t,c in out.items() if c}
def power(f,n):
 out=mon()
 for _ in range(n):out=mul(out,f)
 return out
def deriv(f,axis):
 out={}
 for (powers,jets),c in f.items():
  if powers[axis]:
   pp=list(powers);pp[axis]-=1;out=add(out,mon(pp,jets,c*powers[axis]))
  for at,(name,i,j) in enumerate(jets):
   if (name=='C' and axis==1) or (name in ['eta','W'] and axis==0 and name=='eta') or (name in ['W','Wa'] and axis==1):continue
   if name=='W':out=add(out,scale(mul(var(4),mon(powers,jets,c)),-1));continue
   if name=='Wa':out=add(out,mul(var(3),mul(var(0,-1),mon(powers,jets,c))));continue
   ij=[i,j];ij[axis]+=1;jj=list(jets);jj[at]=(name,*ij);out=add(out,mon(powers,jj,c))
 return out
def diff(f,axis,n=1):
 for _ in range(n):f=deriv(f,axis)
 return f
u,y,delta,a,beta,A,DDsym=[var(i) for i in range(7)];C,eta=jet('C'),jet('eta')
f=scale(mul(var(2,4),mul(var(0,4),mul(C,eta))),Q(-1,12))
def dx(f):return mul(var(2,-1),deriv(f,0))
h=scale(add(dx(dx(f)),diff(f,1,2)),-1);psi=dx(f);U1=scale(deriv(psi,1),-1);U2=dx(psi)
H2=mul(add(mul(var(0,2),C),scale(mul(var(0,3),jet('C',1)),Q(2,3)),scale(mul(var(0,4),jet('C',2)),Q(1,12))),eta)
H4=scale(mul(var(0,4),mul(C,jet('eta',0,2))),Q(1,12))
checks={}
def check(name,f,g=None):
 if g is None:g={}
 assert f==g,(name,f,g);checks[name]=True
check('physical_two_term_scaling',h,add(mul(var(2,2),H2),mul(var(2,4),H4)))
check('physical_Poisson_stream',add(dx(dx(psi)),diff(psi,1,2),dx(h)))
check('physical_divergence',add(dx(U1),deriv(U2,1)))
check('physical_curl',add(dx(U2),scale(deriv(U1,1),-1),dx(h)))
# Reflection signs include both polynomial powers and differentiated cutoff parity.
def reflect(f,axis):
 out={}
 for (powers,jets),c in f.items():
  exponent=powers[axis]
  for name,i,j in jets:exponent+=(i if axis==0 else 1+j) if name=='eta' else (i if axis==0 else j)
  out[(powers,jets)]=c*((-1)**exponent)
 return out
check('density_even_x',reflect(h,0),h);check('density_odd_y',reflect(h,1),scale(h,-1))
f0=scale(mul(var(0,4),y),Q(-1,12));h0=scale(add(diff(f0,0,2),diff(f0,1,2)),-1);check('center_density',h0,mul(var(0,2),y))
J=scale(diff(diff(h0,0,2),1),Q(1,2));check('center_J',J,mon())
strain=diff(diff(f0,0,2),1)
def at_origin(f):return {key:c for key,c in f.items() if key[0][0]==key[0][1]==0 and not key[1]}
check('center_strain',at_origin(strain))
Fz,W=jet('F'),jet('W');WF=mul(W,Fz)
conj=add(scale(mul(A,deriv(WF,0)),-1),mul(DDsym,mul(y,deriv(WF,1))),scale(WF,-1))
expected=mul(W,add(scale(mul(A,deriv(Fz,0)),-1),mul(DDsym,mul(y,deriv(Fz,1))),mul(add(mul(A,beta),mon(c=-1)),Fz)))
check('frozen_weight_conjugation',conj,expected)
# Euler powers via Leibniz vs the closed Stirling normal form.
St={(0,0):1}
for n in range(1,7):
 for j in range(n+1):St[n,j]=j*St.get((n-1,j),0)+St.get((n-1,j-1),0)
Wa,G=jet('Wa'),jet('G')
for n in range(1,7):
 left=mul(Wa,G)
 for _ in range(n):left=mul(u,deriv(left,0))
 right={}
 for ell in range(n+1):
  for j in range(ell+1):right=add(right,scale(mul(power(a,n-ell),mul(var(0,j),jet('G',j))),comb(n,ell)*St.get((ell,j),0)))
 check(f'closed_Euler_order{n}',left,mul(Wa,right))
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_FMPQ_DIFFERENTIAL_RING_CENTER_TRACE','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(primary['parent_files']),'exact_parameters_compared':len(actual),'ring_checks':checks,'center_J':'1','center_Sigma':'0','source_reuse':'Independent fmpq Leibniz differential ring and Stirling normal ordering; no NPZ, Sympy or primary code import.','scope':'Finite algebra and exact parameter instance only. Sobolev convergence, canonical uniqueness and nonclosability are analytic arguments.'};p.write(E/'independent.json',out);print(json.dumps(out))
