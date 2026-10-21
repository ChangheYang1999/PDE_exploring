from fractions import Fraction as Q
from itertools import product
from math import factorial, comb
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time

ROOT=Path(__file__).resolve().parents[1]
J=75
MAX_N=4

def add(a,b,c=Q(1)):
 out=a.copy()
 for j,v in b.items():
  out[j]=out.get(j,Q(0))+c*v
  if not out[j]: del out[j]
 return out

def diff(a): return {j-1:j*v for j,v in a.items() if j}
def rad(a,p): return {j:(p-j)*v for j,v in a.items() if (p-j)*v}
def trunc(a,limit=J): return {j:v for j,v in a.items() if j<=limit and v}
def times(a,b):
 out={}
 for j,v in a.items():
  for k,w in b.items():
   if j+k<=J: out[j+k]=out.get(j+k,Q(0))+v*w
 return {j:v for j,v in out.items() if v}
def norm(a,k): return sum((abs(v)*k**j for j,v in a.items()),Q(0))
def source_norm(a,k): return sum((abs(v)*k**j/j for j,v in a.items()),Q(0))
def rise(x,n):
 ans=Q(1)
 for i in range(n): ans*=x+i
 return ans

def indices(d,N):
 for a in product(range(N+1),repeat=d):
  if sum(a)==N: yield a

def invert(A,b,ms,Cs,a,H):
 N=sum(a);res=1+sum(ai*(mi-1) for ai,mi in zip(a,ms));p=1+Q(res-1)*(1-1/A)
 f={};u={};v={};compat=[]
 for j in range(1,J+1,2):
  c=A*p-1-(A-1)*j
  rhs=H.get(j,Q(0))-2*b*(A-1)*v.get(j,Q(0))
  if c: fj=rhs/c
  else:
   assert j==res and rhs==0,(a,j,rhs)
   fj=Cs[a.index(1)] if N==1 else Q(0)
   compat.append(j)
  if fj: f[j]=fj
  uj=(j-p)*(v.get(j,Q(0))+fj)/(j+1)
  if uj:u[j+1]=uj
  vj=(p-j-1)*uj/(j+2)
  if vj:v[j+2]=vj
 # Check all three equations through their valid truncation order directly.
 transport=add({j:(A*p-1+(1-A)*j)*x for j,x in f.items()},v,2*b*(A-1))
 assert not trunc(add(transport,H,-1)),('transport',a)
 assert not trunc(add(diff(v),rad(u,p),-1),J+1),('divergence',a)
 curl=add({j:(j-p)*x for j,x in v.items()},diff(u),-1)
 assert not trunc(add(curl,rad(f,p),-1)),('curl',a)
 return {'f':f,'u':u,'v':v,'p':p,'res':res,'M':res+2*(N-1),'compat':compat}

def axis_terms(modes,j):
 out={}
 for v in modes.values():
  c=v['f'].get(j,Q(0))
  if c:out[v['p']-j]=out.get(v['p']-j,Q(0))+c
 return {p:c for p,c in out.items() if c}

start=time.monotonic()
out={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'angular_cutoff':J,'max_total_amplitude_degree':MAX_N,'cases':[]}
cases=[([3,5,7],Q(3),Q(7,4),[Q(1),Q(-2),Q(3)]),([3,5,7],Q(4,3),Q(3),[Q(1),Q(2),Q(-3)]),([3,5,7],Q(2),Q(1,2),[Q(0),Q(1),Q(2)]),([3,7,11,13],Q(7,4),Q(50),[Q(1,2),Q(-1),Q(0),Q(2)]),([5,9],Q(10),Q(2),[Q(-2),Q(3)]),([3,5,7],Q(5,4),Q(1),[Q(0),Q(0),Q(0)])]
for ms,A,b,Cs in cases:
 k=Q(1,4) if b<15 else Q(1,16)
 B=k*k/(1-k*k);L=Q(2*max(ms)+1,2)/((A-1)*(1-b*B));K=(2*max(ms)+1)*k/((A-1)*(1-k*k)*(1-b*B))
 abar=sum(abs(C)*k**m for C,m in zip(Cs,ms))/(1-max(Q(1),b)*k*k)
 assert (1+b)*k*k<1
 modes={};degree_norms={};rows=[]
 for N in range(1,MAX_N+1):
  for a in indices(len(ms),N):
   H={};conv=Q(0)
   if N>=2:
    for u,x in modes.items():
     v=tuple(ai-ui for ai,ui in zip(a,u))
     if min(v)<0 or not sum(v) or v not in modes:continue
     z=modes[v]
     assert sum(u)+sum(v)==N
     H=add(H,times(x['u'],rad(z['f'],z['p'])))
     H=add(H,times(x['v'],diff(z['f'])),-1)
     conv+=norm(x['f'],k)*norm(z['f'],k)
   z=invert(A,b,ms,Cs,a,H);modes[a]=z
   for tag,order in [('f',z['M']),('u',z['M']+1),('v',z['M']+2)]:
    assert not z[tag] or min(z[tag])>=order,(a,tag,order,min(z[tag]))
   fn=norm(z['f'],k)
   assert norm(z['u'],k)<=k/(1-k*k)*fn
   assert norm(z['v'],k)<=B*fn
   if N==1:
    i=a.index(1);m=ms[i];q=Q(m-1)/A
    for j in range(m,J+1,2):
     ell=(j-m)//2
     exact=Cs[i]*(-1)**ell*rise(b,ell)*rise(q,2*ell)*Q(factorial(m),factorial(ell)*factorial(j))
     assert z['f'].get(j,Q(0))==exact
   else:
    hn=source_norm(H,k)
    assert hn<=2*k/(1-k*k)*conv
    assert fn<=L*hn and fn<=K*conv
   rows.append({'multiindex':a,'radial_degree':str(z['p']),'resonance':z['res'],'minimum_order':z['M'],'actual_orders':[min(z[t]) if z[t] else None for t in ['f','u','v']],'density_norm':float(fn)})
  degree_norms[N]=sum(norm(z['f'],k) for a,z in modes.items() if sum(a)==N)
  assert degree_norms[N]<=Q(comb(2*(N-1),N-1),N)*K**(N-1)*degree_norms[1]**N
 assert degree_norms[1]<=abar
 traces={}
 if ms==[3,5,7]:
  lam=2/A;C3,C5,C7=Cs
  expected={3:{-lam:C3},5:{-lam-2:-b*lam*(lam+1)*C3/20,-2*lam:C5},7:{-lam-4:b*(b+1)*rise(lam,4)*C3/1680,-2*lam-2:-b*(2*lam)*(2*lam+1)*C5/42-lam*(3-2*lam)*C3*C3/(40*(A-1)),-3*lam:C7}}
  for j,e in expected.items():
   e={p:c for p,c in e.items() if c}
   actual=axis_terms(modes,j)
   assert actual==e,(A,b,Cs,j,actual,e)
   traces[j]={str(p):str(c) for p,c in actual.items()}
 # Radial collisions are recorded, not excluded.
 collisions={}
 for a,z in modes.items():collisions.setdefault(str(z['p']),[]).append(a)
 collisions={p:aa for p,aa in collisions.items() if len(aa)>1}
 row={'m':ms,'A':str(A),'b':str(b),'C':list(map(str,Cs)),'kappa':str(k),'K':str(K),'a_bar':str(abar),'degree_norms':{N:float(x) for N,x in degree_norms.items()},'traces':traces,'radial_collisions':collisions,'multiindices':rows}
 out['cases'].append(row)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',ms,'A',A,'b',b,'C',Cs,'multiindices',len(rows),'collisions',len(collisions),flush=True)
out['complete']=True;out['seconds']=time.monotonic()-start;out['exact_multiindex_cases']=sum(len(x['multiindices']) for x in out['cases'])
(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL',out['exact_multiindex_cases'],'EXACT CASES PASS',out['seconds'],flush=True)
