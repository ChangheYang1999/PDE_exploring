from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,runpy
from functools import lru_cache
from flint import fmpq as Q,fmpq_mat,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
start=time.monotonic();base=Path(__file__).resolve().parents[1]
helper=base.parent/'weak_probe_audit/code/reproduce.py'
lib=runpy.run_path(str(helper));fields=lib['fields'];ar=lib['ar']
name=sys.argv[1];dim=int(sys.argv[2]) if len(sys.argv)>2 else 12
src=base/'data'/f'{name}_canonical.json';hsfile=base/'data'/f'{name}_HS.json'
c,delta,rho,_=fields(json.loads(src.read_text()))
first=[((j+1)*delta/2,p) for (j,n),p in rho.items() if n==1]

def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,Q(0))+v
 return clean(out)
def scale(p,a):return clean({k:v*a for k,v in p.items()})
def mul(p,q):
 out={}
 for k,v in p.items():
  for l,w in q.items():out[k+l]=out.get(k+l,Q(0))+v*w
 return clean(out)
def dt(p):return {k+1:-k*v for k,v in p.items()}
def times_t(p):return add({k-1:v for k,v in p.items()},scale(p,-1))
terms={(0,Q(1,2)):Q(1)};fs=[]
for n in range(dim+1):
 f={}
 for (k,p),v in terms.items():f[p]=f.get(p,Q(0))+v
 fs.append(clean(f));new={}
 for (k,p),v in terms.items():
  if k:new[k-1,p]=new.get((k-1,p),Q(0))+k*v
  new[k+1,p+1]=new.get((k+1,p+1),Q(0))-2*p*v
 terms={k:v for k,v in new.items() if v}
hs=[scale(add(dt(f),times_t(dt(dt(f)))),-4) for f in fs[:dim]]
assert hs[0]=={Q(3,2):Q(-1),Q(5,2):Q(3)}
@lru_cache(None)
def moment(k):
 out=Q(0)
 for a,p in first:
  q=k+a-2;assert q>0
  beta=1/(q*(q+1))
  for l,v in enumerate(p):
   out+=v*beta
   beta*=Q(l+2)/(l+2+q)
 return out
G=[[Q(0) for j in range(dim)] for i in range(dim)]
B=[[Q(0) for j in range(dim)] for i in range(dim)]
constant_checks=0
for i in range(dim):
 for j in range(i+1):
  prod=mul(hs[i],hs[j]);assert all(k>1 for k in prod)
  gram=sum((v/(k-1) for k,v in prod.items()),Q(0))
  A=add(scale(add(mul(hs[i],dt(dt(fs[j]))),mul(hs[j],dt(dt(fs[i])))),-2),scale(mul(dt(fs[i+1]),dt(fs[j+1])),-4))
  D=add(mul(hs[i],dt(fs[j])),mul(hs[j],dt(fs[i])))
  C=add(A,scale(dt(D),2))
  assert all(k.denominator==1 and k>2 for k in C)
  assert sum((v/((k-2)*(k-1)) for k,v in C.items()),Q(0))==0
  constant_checks+=1
  if i==j==0:assert C=={Q(4):Q(-3),Q(5):Q(6)}
  val=-sum((v*moment(k) for k,v in C.items()),Q(0))/2
  G[i][j]=G[j][i]=gram;B[i][j]=B[j][i]=val
assert G[0][0]==Q(3,4)
# Independent exact LDL positivity check.
L=[[Q(i==j) for j in range(dim)] for i in range(dim)];D=[]
for i in range(dim):
 pivot=G[i][i]-sum((L[i][k]**2*D[k] for k in range(i)),Q(0));assert pivot>0;D.append(pivot)
 for j in range(i+1,dim):L[j][i]=(G[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),Q(0)))/pivot
old=json.loads(hsfile.read_text())
def energy(k):
 d=old['norms'][k]
 return Q(d.get('rational_energy_over_pi_half',d.get('unweighted_rational_sum')))
kappa2=((arb(2).log()-arb(1)/2)*ar(energy('D_rho_x'))+(3*arb(2).log()-2)*ar(energy('D_rho_y')))/32
rows=[]
for d in sorted(set([1,2,4,8,dim])):
 if d>dim:continue
 gm=fmpq_mat([r[:d] for r in G[:d]]);bm=fmpq_mat([r[:d] for r in B[:d]])
 m=gm.inv()*bm;t=sum((m[i,j]*m[j,i] for i in range(d) for j in range(d)),Q(0));assert t>=0
 rem=kappa2-ar(t);assert rem>0
 bound=rem.sqrt();budget=ar(c-1)-bound
 rows.append({'dimension':d,'captured_HS_energy_exact':str(t),'captured_HS_energy':ar(t).str(75),'remaining_S1_HS_upper':bound.str(75),'theta_budget_for_beta2':budget.str(75)})
 print(name,'dim',d,'captured',ar(t).str(16),'remaining',bound.str(20),'theta budget',budget.str(20),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':ctx.prec,'dimension':dim,'first_density_modes':len(first),'all_constant_background_checks':constant_checks,'gram_ldl_pivots':[str(x) for x in D],'G_over_pi':[[str(x) for x in r] for r in G],'B_over_pi':[[str(x) for x in r] for r in B],'radial_q0':ar(B[0][0]/G[0][0]).str(80),'full_kappa':kappa2.sqrt().str(80),'rows':rows,'inputs':{str(p.relative_to(base)) if p.is_relative_to(base) else str(p.relative_to(base.parent)):sha256(p.read_bytes()).hexdigest() for p in [src,hsfile,Path(__file__),base/'PROOF.md',helper]},'elapsed_seconds':time.monotonic()-start,'status':'New theorem and arithmetic pending independent review'}
path=base/'verification'/f'{name}_d{dim}.json';assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n')
print('seconds',out['elapsed_seconds'],flush=True)
