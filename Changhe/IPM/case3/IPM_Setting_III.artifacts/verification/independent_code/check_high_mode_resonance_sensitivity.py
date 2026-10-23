#!/usr/bin/env python3
"""Own exact two-algebra high-mode test, with no external code imports."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,resource
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(40,40))
start=time.monotonic();out=Path('research/high_mode_resonance_sensitivity/verification');counts={}
assert(out/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
def ck(b,g):
 counts[g]=counts.get(g,0)+1
 if not b:raise AssertionError(g)
def clean(a):return{k:v for k,v in a.items() if v}
def accum(a,k,v):a[k]=a.get(k,F())+v
def add(a,b):
 r=dict(a)
 for k,v in b.items():accum(r,k,v)
 return clean(r)
def scl(a,c):return clean({k:v*c for k,v in a.items()})
def sineput(a,e,n,v):
 if n and e<=2:accum(a,(e,abs(n)),v if n>0 else -v)
def rdx(a,s):
 r={}
 for (e,n),v in a.items():
  sineput(r,e,n+1,v*(s-n)/2);sineput(r,e,n-1,v*(s+n)/2)
 return clean(r)
def rB(h,a,si,sj):
 r={}
 for (e,m),v in h.items():
  for (f,n),w in a.items():
   if e+f>2:continue
   sineput(r,e+f,n+m,v*w*((si+1)*n-m*sj)/2)
   sineput(r,e+f,n-m,-v*w*((si+1)*n+m*sj)/2)
 return clean(r)
def toC(a):
 r={}
 for (e,n),v in a.items():r[e,n]=-v/2;r[e,-n]=v/2
 return clean(r)
# Separately expressed Cartesian derivatives and epsilon-Laurent convolution.
def derivative(a,q,axis):
 r={}
 for (e,n),v in a.items():
  if axis==0:shifts=((1,q-n),(-1,q+n))
  else:shifts=((1,n-q),(-1,n+q))
  for dn,f in shifts:accum(r,(e,n+dn),v*f/2)
 return clean(r)
def conv(a,b):
 r={}
 for (e,n),v in a.items():
  for (f,m),w in b.items():
   if e+f<=2:accum(r,(e+f,n+m),v*w)
 return clean(r)
def cB(h,a,si,sj):
 return add(conv(derivative(h,si+1,1),derivative(a,sj,0)),scl(conv(derivative(h,si+1,0),derivative(a,sj,1)),-1))
def inverse(g,s):
 r={}
 for (e,n),v in g.items():
  den=n*n-(s+1)**2
  ck(bool(den),'nonzero_inverse_denominator')
  r[e,n]=v/den
 return clean(r)
def ser(a):return{f'{e},{n}':str(v) for (e,n),v in sorted(a.items())}
for row in json.loads((out/'manifest.json').read_text())['files']:
 ck(hashlib.sha256(Path(row['frozen']).read_bytes()).hexdigest()==row['sha256'],'frozen_hash')
external=json.loads((out/'external_values.json').read_text());pure=json.loads((out/'PURE150_EXACT.json').read_text())
results=[]
for ell,K,M in ((F(3),5,2),(F(5,2),9,4)):
 N=101;p=1/ell;delta=1-p;s=[p-k*delta for k in range(K+1)]
 rp=[{(0,1):F(1),(1,N):F(1)}];cp=[{(0,1):F(-1,2),(0,-1):F(1,2),(1,N):F(-1,2),(1,-N):F(1,2)}];rh=[];ch=[];steps=[]
 for k in range(K+1):
  if k:
   r={};c={}
   for i in range(k):
    j=k-1-i;r=add(r,rB(rh[i],rp[j],s[i],s[j]));c=add(c,cB(ch[i],cp[j],s[i],s[j]))
   rp.append(scl(r,1/(ell*k*delta)));cp.append(scl(c,1/(ell*k*delta)))
  ck(toC(rp[k])==cp[k],'density_two_algebras')
  for (e,n) in rp[k]:
   ck(n>0 and n%2==1 and 0<=e<=2,'density_parity')
   ck(any(abs(n-a*N)<=2*k+1-e for a in range(-e,e+1,2)),'frequency_bound_density')
  rg=rdx(rp[k],s[k]);cg=derivative(cp[k],s[k],0)
  ck(toC(rg)==cg,'source_two_algebras')
  for (e,n) in rg:
   ck(any(abs(n-a*N)<=2*k+2-e for a in range(-e,e+1,2)),'frequency_bound_source')
  if k<K:
   rh.append(inverse(rg,s[k]));ch.append(inverse(cg,s[k]));ck(toC(rh[k])==ch[k],'stream_two_algebras')
   q=s[k]+1;neg_lap=add(scl(derivative(derivative(ch[k],q,0),q-1,0),-1),derivative(derivative(ch[k],q,1),q-1,1))
   ck(neg_lap==cg,'Cartesian_Poisson')
  steps.append(dict(k=k,s=str(s[k]),density=ser(rp[k]),source=ser(rg),stream=ser(rh[k]) if k<K else None))
 g=[rg.get((e,M),F()) for e in range(3)]
 match=next(row for row in external if F(row['ell'])==ell)
 ck([str(v) for v in g]==match['g_epsilon_coefficients_through_degree_2'],'external_exact_rationals')
 ck(str(g[0])==next(row for row in pure['cases'] if F(row['ell'])==ell)['g_star_at_A1'],'pure_constant')
 ck(g[1]==0 and g[2]!=0,'linear_zero_quadratic_nonzero')
 prime=1000003;ck(g[2].denominator%prime!=0,'modular_denominator')
 residue=(g[2].numerator%prime)*pow(g[2].denominator,-1,prime)%prime
 ck(residue==match['epsilon_squared_residue_mod_1000003'],'modular_residue')
 ck(N>4*K+4,'stable_frequency_range')
 results.append(dict(ell=str(ell),K=K,M=M,N=N,g_epsilon=[str(v) for v in g],quadratic_residue=residue,steps=steps))
res=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='PASS',checks=sum(counts.values()),counts=counts,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=results,scope='Exact finite coefficient functional; no trace-realization or profile assertion')
(out/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
for row in results:print(json.dumps({k:v for k,v in row.items() if k!='steps'},indent=2))
