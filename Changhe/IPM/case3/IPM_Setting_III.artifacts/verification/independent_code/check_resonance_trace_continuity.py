#!/usr/bin/env python3
"""Exact bounds supporting the trace-continuity proof, not a profile test."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
start=time.monotonic();out=Path('research/resonance_trace_continuity/verification');counts={}
assert(out/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
def ck(b,g):
 counts[g]=counts.get(g,0)+1
 if not b:raise AssertionError(g)
for row in json.loads((out/'manifest.json').read_text())['files']:
 ck(hashlib.sha256(Path(row['frozen']).read_bytes()).hexdigest()==row['sha256'],'frozen_hash')
evidence=json.loads((out/'PURE150_EXACT.json').read_text());rows=[]
for ell,K,M in ((F(3),5,2),(F(5,2),9,4)):
 p=1/ell;delta=1-p;s=[p-i*delta for i in range(K+1)];B=[];L=[];neigh=[]
 for i in range(K):
  q=abs(s[i]+1)
  lo=2*(q.numerator//(2*q.denominator));candidates=sorted(set(m for m in (lo,lo+2,2) if m>=2))
  ck(all(F(m)!=q for m in candidates),'no_resonant_neighbor')
  bi=max((F(m)+q)/abs(F(m)-q) for m in candidates);li=bi*((F(3,2)**K)+1)/2
  B.append(bi);L.append(li);neigh.append(candidates)
  for m in range(2,102,2):
   ck((F(m)+q)/abs(F(m)-q)<=bi,'global_ratio_finite_support')
   for mm in (m+2,m+10):
    if q<m:ck((F(m)+q)/(F(m)-q)>=(F(mm)+q)/(F(mm)-q),'ratio_monotone_above')
    elif mm<q:ck((F(m)+q)/(q-m)<=(F(mm)+q)/(q-mm),'ratio_monotone_below')
  for n in range(1,82,2):
   for j in range(K+1):
    column=F()
    for m,src in ((n+1,(s[i]-n)/2),(n-1,(s[i]+n)/2)):
     if m==0:continue
     den=m*m-(s[i]+1)**2;ck(den!=0,'column_nonresonant')
     column+=F(1+m,1+n)**j*(m+q)*abs(src/den)
    ck(column<=li,'exact_velocity_column_bound')
 C=[F(1)]
 for k in range(1,K+1):
  val=sum((L[i]*(abs(s[k-1-i])+1)*C[i]*C[k-1-i] for i in range(k)),F())/(ell*k*delta)
  C.append(val);ck(val>0,'positive_majorant')
  factor=F()
  for i in range(k):
   j=k-1-i;ck(i+1+j+1==k+1,'difference_degree_count')
   ck(K-k<=K-i and K-k+1<=K-j,'available_angular_derivatives')
   factor+=L[i]*(abs(s[j])+1)*C[i]*C[j]*(i+j+2)/(ell*k*delta)
  ck(factor==(k+1)*C[k],'difference_majorant_exact')
  pure=next(c for c in evidence['cases'] if F(c['ell'])==ell)['density_coefficients_at_A1'][k]
  norm=sum(((1+int(n))**(K-k)*abs(F(v)) for n,v in pure['sine'].items()),F())
  ck(norm<=C[k]*F(2**K)**(k+1),'actual_pure_cascade_bound')
 g0=F(next(c for c in evidence['cases'] if F(c['ell'])==ell)['g_star_at_A1'])
 radius=min(F(1),abs(g0)/(2*M*(K+1)*C[K]*(2**K+1)**K))
 ck(0<radius<=1,'positive_radius')
 for A in (F(-7,3),F(-1),F(1,5),F(1),F(9,2)):
  d=radius*abs(A);R=(2**K+1)*abs(A)
  bound=M*(K+1)*C[K]*R**K*d
  ck(bound<=abs(g0)*abs(A)**(K+1)/2,'persistence_half_margin')
  ck(g0*A**(K+1)!=0,'pure_nonzero_amplitude')
 # Critical coefficient extraction and first density log transport.
 ck(s[K]==-M-1 and (s[K]-(M-1))/2==-M and (s[K]+M+1)/2==0,'critical_coordinate_formula')
 ck(ell*((p-M-2)-p)==-ell*(M+2),'density_log_divisor')
 rows.append(dict(ell=str(ell),K=K,M=M,s=[str(v) for v in s],B=[str(v) for v in B],L=[str(v) for v in L],neighbor_modes=neigh,C=[str(v) for v in C],g0=str(g0),epsilon0=str(radius),epsilon0_float_orientation_only=float(radius),majorant_CK_float_orientation_only=float(C[K])))
# Direct finite trig multiplication confirms the norm normalization/constants.
def put(d,n,v,sine):
 if sine and n==0:return
 if n<0:n=-n;v=-v if sine else v
 d[n]=d.get(n,F())+v
for sample in range(24):
 a={n:F((-1)**(n+sample)*(n+1),sample+n+2) for n in range(1,8,2)}
 b={m:F((-1)**(m//2+sample)*(m+2),sample+m+3) for m in range(0,9,2)}
 product={}
 for n,v in a.items():
  for m,w in b.items():put(product,n+m,v*w/2,True);put(product,n-m,v*w/2,True)
 for j in range(10):
  norm=lambda d:sum(((1+n)**j*abs(v) for n,v in d.items()),F())
  ck(norm(product)<=norm(a)*norm(b),'actual_sine_cosine_product_norm')
  ck(sum(((1+n)**j*n*abs(v) for n,v in a.items()),F())<=sum(((1+n)**(j+1)*abs(v) for n,v in a.items()),F()),'derivative_norm')
res=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='PASS',checks=sum(counts.values()),counts=counts,proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=rows,scope='Conservative strong Fourier norm bound; no candidate tail has been certified')
(out/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
for r in rows:print(json.dumps({k:v for k,v in r.items() if k not in ('C','L','s')},indent=2))
