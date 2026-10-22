"""Exact source expansion and horizontal offset certificate, packet136.

No fitting modules or NUM code are imported. Rational monomial differentiation,
polynomial products, finite primitives, and sparse algebraic certificates.
"""
from fractions import Fraction as Q
from math import factorial,lcm,comb
from pathlib import Path
import json,hashlib

def add(*pieces):
 out={}
 for scalar,terms in pieces:
  for key,value in terms.items():out[key]=out.get(key,Q(0))+scalar*value
 return {key:value for key,value in out.items()if value}

def deriv(terms,axis,s):
 out={}
 for (a,b,ns,nc),v in terms.items():
  ab=[a,b];n=ab[axis]
  if n:
   low=ab.copy();low[axis]-=1;key=(*low,ns,nc);out[key]=out.get(key,Q(0))+v*n
  ab[axis]+=1;key=(*ab,ns,nc-2);out[key]=out.get(key,Q(0))+v*(ns*s+nc)
 return {k:v for k,v in out.items()if v}

def multiply(A,B):
 out={}
 for a,va in A.items():
  for b,vb in B.items():
   k=tuple(x+y for x,y in zip(a,b));out[k]=out.get(k,Q(0))+va*vb
 return {k:v for k,v in out.items()if v}

def chebyshev(n,offset=0,scale=1):
 a=[1]
 if n==0:return a
 b=[offset,scale]
 for _ in range(1,n):
  c=[0]*(len(b)+1)
  for j,v in enumerate(b):c[j]+=2*offset*v;c[j+1]+=2*scale*v
  for j,v in enumerate(a):c[j]-=v
  a,b=b,c
 return b

def source_from_state(state):
 beta=Q(state['beta']);s=1/beta;psi={}
 for label,value in zip(state['labels'],state['C']):
  i,j,shift=label;v=Q(value)
  for ri,ci in enumerate(chebyshev(i,-1,2)):
   for aj,cj in enumerate(chebyshev(j)):
    if ci and cj:
     key=(1,aj,-ri-1,1-aj-shift);psi[key]=psi.get(key,Q(0))+v*ci*cj
 for row in state.get('extra_stream_terms',[]):
  key=(int(row['x_power']),int(row['y_power']),0,Q(row['R_power']))
  psi[key]=psi.get(key,Q(0))+Q(row['coefficient'])
 psi={k:v for k,v in psi.items()if v}
 px=deriv(psi,0,s);py=deriv(psi,1,s)
 at0=lambda f:sum(v for(a,b,ns,nc),v in f.items()if a==b==0)
 w1=add((beta,{(1,0,0,0):Q(1)}),(-1,py),(at0(py),{(0,0,0,0):Q(1)}))
 w2=add((beta,{(0,1,0,0):Q(1)}),(1,px),(-at0(px),{(0,0,0,0):Q(1)}))
 omega=add((-1,deriv(px,0,s)),(-1,deriv(py,1,s)))
 F=add((1,multiply(w1,deriv(omega,0,s))),(1,multiply(w2,deriv(omega,1,s))),(1,omega))
 rows=[]
 for(a,b,ns,nc),c in F.items():
  if a%2!=1:raise ValueError('source lost odd parity')
  q=(ns*s+nc)/2;degree=a+b+2*q
  if degree>=0:raise ValueError('termwise negative-degree hypothesis fails')
  rows.append((c,(a-1)//2,b,q))
 return rows

def finite_part_terms(rows):
 powers=[];logc=Q(0)
 for c,k,b,q in rows:
  if 2*k+1+b+2*q>=0:raise ValueError('negative degree required')
  den=Q(1)
  for ell in range(1,k+2):den*=q+ell
  if den:
   coefficient=c*((-1)**(k+1))*factorial(k)/(2*den)
   powers.append((coefficient,b,q+k+1))
  else:
   assert q==-k-1 and b==0
   logc-=c/2
 return powers,logc

def whole_offset_certificate(rows):
 powers,logc=finite_part_terms(rows);even={};odd={}
 for a,b,e in powers:
  h=b//2;terms=odd if b%2 else even
  for ell in range(h+1):
   exponent=e+ell;terms[exponent]=terms.get(exponent,Q(0))+a*comb(h,ell)*((-1)**(h-ell))
  if b==0:even[Q(0)]=even.get(Q(0),Q(0))-a
 even={k:v for k,v in even.items()if v};odd={k:v for k,v in odd.items()if v}
 return {'even_power_coefficients':{str(k):str(v)for k,v in sorted(even.items())},'odd_power_coefficients':{str(k):str(v)for k,v in sorted(odd.items())},'log_coefficient':str(logc),
  'verdict':'REFUTED_TRANSVERSE_GRADIENT'if even or odd or logc else'CONFIRMED_WHOLE_OFFSET_ZERO_ONLY',
  'method':'Even/odd decomposition and independence of finite real exponential sums; no transcendence theorem.'}

def offset_certificate(rows):
 powers,logc=finite_part_terms(rows);d=lcm(*(e.denominator for a,b,e in powers))if powers else 1
 poly={}
 for a,b,e in powers:
  quotient,residue=divmod(int(e*d),d);two=Q(2)**quotient
  poly[residue]=poly.get(residue,Q(0))+a*two
  if b==0:poly[0]=poly.get(0,Q(0))-a
 poly={k:v for k,v in poly.items()if v}
 if not logc:verdict='REFUTED_TRANSVERSE_GRADIENT'if poly else'CONFIRMED_H1_ZERO_ONLY'
 elif not poly:verdict='REFUTED_TRANSVERSE_GRADIENT'
 else:verdict='OPEN_MIXED_LOG_ALGEBRAIC'
 return {'root_degree':d,'reduced_polynomial':{str(k):str(v)for k,v in sorted(poly.items())},'log2_coefficient':str(logc),'source_monomials':len(rows),'verdict':verdict,
 'scope':'Exact H(1) of this rationally serialized primitive source. Conditional on the necessary critical transverse-gradient estimate. No nearby-profile bound.'}

def mp_offset(rows,y,dps=80):
 import mpmath as mp
 with mp.workdps(dps):
  rat=lambda q:mp.mpf(q.numerator)/q.denominator
  y=mp.mpf(str(y));A=1+y*y;powers,logc=finite_part_terms(rows)
  value=mp.fsum(rat(a)*(y**b*mp.power(A,rat(e))-(1 if b==0 else 0))for a,b,e in powers)+rat(logc)*mp.log(A)
  return mp.nstr(value,dps)

def mp_primitive(rows,x,y,dps=80):
 import mpmath as mp
 with mp.workdps(dps):
  rat=lambda q:mp.mpf(q.numerator)/q.denominator
  x=mp.mpf(str(x));y=mp.mpf(str(y));A=1+y*y;z=mp.log1p(x*x/A);values=[]
  for c,k,b,q in rows:
   subs=[]
   for ell in range(k+1):
    p=q+ell+1;L=mp.power(A,rat(p))*mp.expm1(rat(p)*z)/rat(p)if p else z
    subs.append(comb(k,ell)*(-A)**(k-ell)*L)
   values.append(rat(c)*y**b*mp.fsum(subs)/2)
  return mp.nstr(mp.fsum(values),dps)

if __name__=='__main__':
 import argparse,time
 from datetime import datetime,timezone
 ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--labels',nargs='*');args=ap.parse_args();out=args.root/'horizontal_offset_certificates';out.mkdir(exist_ok=True)
 paths=sorted(args.root.glob('*_state.json'))
 if args.labels:paths=[p for p in paths if any(p.stem.startswith(v)for v in args.labels)]
 summary={'status':'RUNNING','utc':datetime.now(timezone.utc).isoformat(),'states':[]};tic=time.perf_counter()
 for path in paths:
  t=time.perf_counter();rows=source_from_state(json.loads(path.read_text()));cert=offset_certificate(rows)
  cert['whole_function']=whole_offset_certificate(rows)
  cert.update(source=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),H1_80digits=mp_offset(rows,1,80),H1_120digits=mp_offset(rows,1,120),elapsed_seconds=time.perf_counter()-t)
  dest=out/(path.stem+'_offset.json');dest.write_text(json.dumps(cert,indent=2)+'\n')
  summary['states'].append({k:v for k,v in cert.items()if k not in ['reduced_polynomial','whole_function']}|{'whole_offset_verdict':cert['whole_function']['verdict']}|{'nonzero_reduced_coefficients':len(cert['reduced_polynomial'])})
  summary['elapsed_seconds']=time.perf_counter()-tic;(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(path.name,cert['verdict'],cert['H1_80digits'][:30],cert['elapsed_seconds'],flush=True)
 summary['status']='COMPLETE';summary['ended_utc']=datetime.now(timezone.utc).isoformat();(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
