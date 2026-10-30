from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial,comb
from functools import lru_cache
import json,sys,time,runpy
from flint import fmpq as Q,fmpq_mat,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
start=time.monotonic();base=Path(__file__).resolve().parents[1];parent=base.parent
name=sys.argv[1];N=int(sys.argv[2]);M=int(sys.argv[3]);assert 1<=N<=12 and 0<=M<=12
helper=parent/'weak_probe_audit/code/reproduce.py';lib=runpy.run_path(str(helper));ar=lib['ar']
src=parent/'parity_hs_budget/data'/f'{name}_canonical.json';hsfile=parent/'parity_hs_budget/data'/f'{name}_HS.json'
c,delta,rho,_=lib['fields'](json.loads(src.read_text()))
def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,Q(0))+v
 return clean(out)
def scale(p,a):return clean({k:v*a for k,v in p.items()})
def mul(p,q):
 out={}
 for (i,j,k),v in p.items():
  for (ii,jj,kk),w in q.items():
   key=i+ii,j+jj,k+kk;out[key]=out.get(key,Q(0))+v*w
 return clean(out)
def der(p,axis):
 out={}
 for (i,j,k),v in p.items():
  degree=[i,j][axis]
  if degree:
   key=(i-1,j,k) if axis==0 else (i,j-1,k);out[key]=out.get(key,Q(0))+degree*v
  key=(i+1,j,k+1) if axis==0 else (i,j+1,k+1);out[key]=out.get(key,Q(0))-2*k*v
 return clean(out)
def dr(p):return {k+1:-k*v for k,v in p.items()}
def radd(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,Q(0))+v
 return clean(out)
terms={(0,Q(1,2)):Q(1)};fs=[]
for n in range(N+1):
 f={}
 for (k,p),v in terms.items():f[p]=f.get(p,Q(0))+v
 fs.append(clean(f));new={}
 for (k,p),v in terms.items():
  if k:new[k-1,p]=new.get((k-1,p),Q(0))+k*v
  new[k+1,p+1]=new.get((k+1,p+1),Q(0))-2*p*v
 terms=clean(new)
def harmonic(f,m,kind):
 for _ in range(m):f=dr(f)
 out={}
 for k in range(m+1):
  if kind=='cos' and k%2==0:sgn=(-1)**(k//2)
  elif kind=='sin' and k%2:sgn=(-1)**((k-1)//2)
  else:continue
  for p,v in f.items():out[m-k,k,p]=2**m*comb(m,k)*sgn*v
 return clean(out)
@lru_cache(None)
def angle0(i,j):
 if i%2 or j%2:return Q(0)
 a,b=i//2,j//2
 return Q(2*factorial(i)*factorial(j),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))
@lru_cache(None)
def anglen(i,j,n):return sum(((-1)**k*comb(n,2*k+1)*angle0(i+n-2*k-1,j+2*k+1) for k in range((n+1)//2)),Q(0))
@lru_cache(None)
def beta(m,q):
 assert m>=1 and q>0
 out=1/q
 for k in range(1,m):out*=Q(k)/(q+k)
 return out
@lru_cache(None)
def plain(i,j,p):
 a=angle0(i,j)
 if not a:return Q(0)
 d=(i+j)//2;return a*beta(d+1,p-d-1)/2
def plain_integral(poly):return sum((v*plain(*k) for k,v in poly.items()),Q(0))
@lru_cache(None)
def radial_density(n,d,p):
 out=Q(0)
 for (j,nn),poly in rho.items():
  if nn!=n:continue
  q=p+(j+1)*delta/2-d-1;assert q>0
  bv=beta(d+1,q)
  for l,v in enumerate(poly):
   out+=v*bv;bv*=Q(d+l+1)/(q+d+l+1)
 return out
@lru_cache(None)
def density(i,j,p):
 assert (i+j)%2==1
 d=(i+j+1)//2;out=Q(0)
 for n in range(1,i+j+1,2):
  a=anglen(i,j,n)
  if a:out+=a*radial_density(n,d,p)/2
 return out
def density_integral(poly):return sum((v*density(*k) for k,v in poly.items()),Q(0))
blocks={'++':[],'-+':[],'--':[]}
for m in range(M+1):
 for kind in (['cos','sin'] if m and m%2==0 else ['cos']):
  parity=('--' if kind=='sin' else ('-+' if m%2 else '++'))
  for n in range(N):
   f=harmonic(fs[n],m,kind);nextf=harmonic(fs[n+1],m,kind)
   h=scale(add(der(der(f,0),0),der(der(f,1),1)),-1)
   u1=scale(der(der(f,0),1),-1);u2=der(der(f,0),0)
   v1=scale(der(nextf,0),-1);v2=scale(der(nextf,1),-1)
   blocks[parity].append({'label':[kind,m,n],'h':h,'u1':u1,'u2':u2,'v1':v1,'v2':v2})
old=json.loads(hsfile.read_text())
def energy(k):
 d=old['norms'][k];return Q(d.get('rational_energy_over_pi_half',d.get('unweighted_rational_sum')))
kappa2=((arb(2).log()-arb(1)/2)*ar(energy('D_rho_x'))+(3*arb(2).log()-2)*ar(energy('D_rho_y')))/32
radfile=parent/'parity_hs_budget/verification'/f'{name}_d12.json'
rad=json.loads(radfile.read_text()) if radfile.exists() else None
reports={};total=Q(0);checks=0;radial_checks=0
for parity,tests in blocks.items():
 size=len(tests)
 if not size:continue
 G=[[Q(0) for j in range(size)] for i in range(size)];B=[[Q(0) for j in range(size)] for i in range(size)]
 for i,ti in enumerate(tests):
  for j in range(i+1):
   tj=tests[j];gg=plain_integral(mul(ti['h'],tj['h']))
   if ti['label'][:2]!=tj['label'][:2]:assert gg==0
   A=scale(add(mul(ti['h'],tj['u1']),mul(tj['h'],ti['u1']),scale(mul(ti['v1'],tj['v2']),-1),scale(mul(ti['v2'],tj['v1']),-1)),Q(1,2))
   Bb=add(scale(add(mul(ti['h'],tj['u2']),mul(tj['h'],ti['u2'])),Q(1,2)),mul(ti['v1'],tj['v1']))
   C=scale(add(der(A,0),der(Bb,1)),-1)
   assert plain_integral({(u,v+1,p):q for (u,v,p),q in C.items()})==0;checks+=1
   bb=density_integral(C);G[i][j]=G[j][i]=gg;B[i][j]=B[j][i]=bb
   if rad is not None and ti['label'][1]==tj['label'][1]==0:
    ii,jj=ti['label'][2],tj['label'][2]
    assert gg==Q(rad['G_over_pi'][ii][jj]) and bb==Q(rad['B_over_pi'][ii][jj]);radial_checks+=2
  print('assembled',parity,i+1,'/',size,'seconds',time.monotonic()-start,flush=True)
 L=[[Q(i==j) for j in range(size)] for i in range(size)];D=[]
 for i in range(size):
  pivot=G[i][i]-sum((L[i][k]**2*D[k] for k in range(i)),Q(0));assert pivot>0;D.append(pivot)
  for j in range(i+1,size):L[j][i]=(G[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),Q(0)))/pivot
 mat=fmpq_mat(G).inv()*fmpq_mat(B);capture=sum((mat[i,j]*mat[j,i] for i in range(size) for j in range(size)),Q(0));assert capture>=0;total+=capture
 reports[parity]={'labels':[t['label'] for t in tests],'G_over_pi':[[str(x) for x in row] for row in G],'B_over_pi':[[str(x) for x in row] for row in B],'positive_LDL_pivots':[str(x) for x in D],'captured_exact':str(capture),'captured':ar(capture).str(80)}
 print('block',parity,'capture',ar(capture).str(24),flush=True)
remaining=kappa2-ar(total);assert remaining>0;bound=remaining.sqrt()
inputs=[src,hsfile,helper,Path(__file__),base/'PROOF.md']+([radfile] if rad is not None else [])
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'N':N,'M':M,'precision_bits':ctx.prec,'blocks':reports,'constant_gradient_checks':checks,'radial_comparison_checks':radial_checks,'total_captured_exact':str(total),'total_captured':ar(total).str(85),'full_kappa':kappa2.sqrt().str(85),'remaining_S1_HS_upper':bound.str(85),'theta_budget_for_beta2':(ar(c-1)-bound).str(85),'inputs':{str(p.relative_to(parent)):sha256(p.read_bytes()).hexdigest() for p in inputs},'elapsed_seconds':time.monotonic()-start,'status':'New theorem and arithmetic pending independent review'}
p=base/'verification'/f'{name}_n{N}_m{M}.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('TOTAL',ar(total).str(30),'remaining',bound.str(30),'theta budget',(ar(c-1)-bound).str(30),'seconds',out['elapsed_seconds'],flush=True)
