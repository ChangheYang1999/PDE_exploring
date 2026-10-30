"""Independent Fourier Gram and Cartesian-gradient compression audit."""
from pathlib import Path
from hashlib import sha256
from math import factorial
from functools import lru_cache
from datetime import datetime,timezone
import json,sys,time
from flint import arb,ctx,fmpq as Q,fmpq_mat
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/parity_reference_audit';SRC=BASE/'source'
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,pshift,ar

def H(p):return sha256(p.read_bytes()).hexdigest()
def add(*args):
 out={}
 for p in args:
  for k,v in p.items():out[k]=out.get(k,Q(0))+v
 return {k:v for k,v in out.items() if v}
def scale(p,v):return {k:x*v for k,x in p.items() if x*v}
def mul(p,q):
 out={}
 for k,v in p.items():
  for j,w in q.items():out[k+j]=out.get(k+j,Q(0))+v*w
 return {k:v for k,v in out.items() if v}
def derivative(p):return {k+1:-k*v for k,v in p.items() if k*v}
def times_t(p):return add({k-1:v for k,v in p.items()},scale(p,-1))
def fn(n):
 out={}
 for k in range(n//2+1):
  p=Q(2*n-2*k+1,2)
  out[p]=Q((-1)**(n+k)*factorial(n)*factorial(2*n-2*k),2**n*factorial(k)*factorial(n-k)*factorial(n-2*k))
 return out

def main():
 start=time.monotonic();ctx.prec=1024
 name=sys.argv[1];dim=12
 assert name in ['d2','C1-N1-005-d2w-j7-x3','C1-N1-007-d2w-j7-e2bal']
 canonical=ROOT/f'research/candidate_audits/data/{name}/canonical.json' if name.startswith('C1-N1-') else ROOT/'research/refit_audit/data/d2_canonical.json'
 energy=ROOT/f'research/background_sobolev/verification/{name}.json'
 peerfile=SRC/f'T4_{name}_d{dim}.json';peer=json.loads(peerfile.read_text())
 maps={f'data/{name}_canonical.json':canonical,f'data/{name}_HS.json':SRC/f'{name}_HS.json','code/check.py':SRC/'T4_check.py','PROOF.md':SRC/'T4_PROOF.md','weak_probe_audit/code/reproduce.py':SRC/'T4_fields.py'}
 for p,digest in peer['inputs'].items():assert H(maps[p])==digest,(p,H(maps[p]),digest)
 model=Radial(canonical)
 fields={tag:{j:pshift(P,2) for (j,n),P in getattr(model,attr).items() if n==freq} for tag,attr,freq in [('a2','rx',2),('b0','ry',0),('b2','ry',2)]}
 @lru_cache(None)
 def moment(field,k,with_t):
  out=Q(0);m0=2 if with_t else 1
  for j,P in fields[field].items():
   q=k+(j+1)*model.delta/2-(2 if with_t else 1);assert q>0
   beta=Q(1)/q if m0==1 else Q(1)/(q*(q+1))
   for l,coefficient in enumerate(P):
    out+=coefficient*beta
    beta*=Q(l+m0)/(q+l+m0)
  return out
 fs=[fn(n) for n in range(dim+1)]
 ds=[derivative(f) for f in fs];dds=[derivative(f) for f in ds]
 hs=[scale(add(ds[n],times_t(dds[n])),-4) for n in range(dim)]
 G=[[Q((-1)**(i+j)*factorial(i+j+3),2**(i+j+3)) for j in range(dim)] for i in range(dim)]
 B=[[Q(0) for j in range(dim)] for i in range(dim)]
 for i in range(dim):
  for j in range(i+1):
   A=add(scale(add(mul(hs[i],dds[j]),mul(hs[j],dds[i])),-2),scale(mul(ds[i+1],ds[j+1]),-4))
   D=add(mul(hs[i],ds[j]),mul(hs[j],ds[i]))
   val=sum((v*(moment('a2',k,True)-moment('b2',k,True)-2*moment('b0',k,True))/4 for k,v in A.items()),Q(0))
   val+=sum((v*moment('b0',k,False) for k,v in D.items()),Q(0))
   B[i][j]=B[j][i]=val
   assert val==Q(peer['B_over_pi'][i][j]),('B',i,j)
   assert G[i][j]==Q(peer['G_over_pi'][i][j]),('G',i,j)
 print('all exact matrix entries agree',time.monotonic()-start,flush=True)
 L=[[Q(i==j) for j in range(dim)] for i in range(dim)];pivots=[]
 for i in range(dim):
  p=G[i][i]-sum((L[i][k]**2*pivots[k] for k in range(i)),Q(0));assert p>0;pivots.append(p)
  assert p==Q(peer['gram_ldl_pivots'][i])
  for j in range(i+1,dim):L[j][i]=(G[j][i]-sum((L[j][k]*L[i][k]*pivots[k] for k in range(i)),Q(0)))/p
 ens=json.loads(energy.read_text())['norms']
 Ex=Q(ens['D_rho_x']['unweighted_rational_sum']);Ey=Q(ens['D_rho_y']['unweighted_rational_sum'])
 kappa2=((arb(2).log()-Q(1,2))*ar(Ex)+(3*arb(2).log()-2)*ar(Ey))/32
 assert kappa2.sqrt().overlaps(arb(peer['full_kappa']))
 rows=[]
 for old in peer['rows']:
  d=old['dimension'];g=fmpq_mat([r[:d] for r in G[:d]]);b=fmpq_mat([r[:d] for r in B[:d]])
  m=g.inv()*b;T=sum((m[i,j]*m[j,i] for i in range(d) for j in range(d)),Q(0))
  assert T==Q(old['captured_HS_energy_exact']) and T>=0 and kappa2>ar(T)
  bound=(kappa2-ar(T)).sqrt();budget=ar(model.c-1)-bound
  checks={key:bool(value.overlaps(arb(old[key]))) for key,value in [('captured_HS_energy',ar(T)),('remaining_S1_HS_upper',bound),('theta_budget_for_beta2',budget)]}
  assert all(checks.values())
  rows.append({'dimension':d,'captured_exact':str(T),'remaining_S1_HS_upper':bound.str(85),'theta_budget_for_beta2':budget.str(85),'peer_overlaps':checks})
  print('dimension',d,'bound',bound.str(25),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':ctx.prec,'method':'Fourier Gram formula; explicit Legendre Poisson derivatives; direct Cartesian rho-gradient angular integrals, without density integration by parts.','dimension':dim,'all_matrix_entries_equal':True,'all_LDL_pivots_positive':True,'G_over_pi':[[str(q) for q in r] for r in G],'B_over_pi':[[str(q) for q in r] for r in B],'rows':rows,'code_sha256':H(Path(__file__)),'proof_sha256':H(BASE/'PROOF.md'),'inputs':{str(p.relative_to(ROOT)):H(p) for p in [canonical,energy,peerfile,*maps.values(),ROOT/'research/radial_fourier/code/radial.py']},'elapsed_seconds':time.monotonic()-start,'status':'Arithmetic and finite compression CONFIRMED; low-generator and candidate theta hypotheses remain separate.'}
 target=BASE/f'verification/{name}_d{dim}.json';assert not target.exists();target.write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
