"""Global weighted D3 velocity and D4 density bounds from exact compactification."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import json,time
from flint import arb,ctx
import sharp_coefficients as sc
from sharp_coefficients import A,add,derivative,chebyshev,encode,plus
HERE=Path(__file__).resolve().parent
TARGETS={'omega_u3':Q(10),'omega_rho4':Q(128)}

def construct():
 s=json.loads((sc.BASE/'source_audit/state131_exact.json').read_text());gamma=1/Q(s['exact_parameters']['cl']);delta=1-gamma
 P={};kinds={}
 for order in (6,7):
  for nx in range(order+1):
   label=f'd{order}_{nx}';axes='x'*nx+'y'*(order-nx);kind='s' if (order-nx)%2 else 'c'
   kinds[label]=('sin' if kind=='s' else 'cos') if order==7 else ('sin2' if kind=='s' else 'one')
   for branch in range(4):
    trig={};p=(3+gamma-branch*delta)/2
    for (j,m,k),v in zip(s['canonical_order'],s['canonical_coefficients']):
     if j!=branch:continue
     tt={('c',2*m,0):Q(v)}
     for di,axis in enumerate(axes):tt=derivative(tt,p,k,di,axis)
     for (ki,n,l),v in tt.items():add(trig,ki,n,k-(4 if order==7 else 3)+l,v)
    assert all(l>=0 for ki,n,l in trig),(order,nx,min(l for ki,n,l in trig))
    poly={}
    for (ki,n,l),v in trig.items():
     assert ki==kind
     C=sc.oddpoly(n,ki) if order==7 else (chebyshev(n//2-1,'U') if ki=='s' else chebyshev(n//2))
     for zi,a in enumerate(C):poly[l,zi]=poly.get((l,zi),Q(0))+v*a
    P[label,branch]={k:v for k,v in poly.items() if v}
 for j in range(4):
  for i in range(5):
   key=f'r4_{i}';P[key,j]=plus((-1,P[f'd7_{i+2}',j]),(-1,P[f'd7_{i}',j]));kinds[key]='cos' if i%2 else 'sin'
  for u in range(2):
   for i in range(4):
    key=f'u3_{u}_{i}';source=f'd6_{i+1+u}';P[key,j]=plus(((-1 if u==0 else 1),P[source,j]));kinds[key]=kinds[source]
 for key in list(P):
  if key[0].startswith('d'):del P[key]
 kinds={k:v for k,v in kinds.items() if not k.startswith('d')}
 return s,delta,P,kinds

def bound(B,tl,th,zl,zh,delta,kinds):
 wl=(1-A(th))**(A(delta)/2);wu=(1-A(tl))**(A(delta)/2);W=sc.cc.wcoeff(wl,wu);ab={}
 for label,kind in kinds.items():
  lo,hi=sc.cc.hull((W*sc.arb_mat([B[label,j].entries() for j in range(4)])).entries());v=abs(lo).max(abs(hi))
  if kind=='sin':v*=A((1-zl)/2).sqrt()
  elif kind=='cos':v*=A((1+zh)/2).sqrt()
  elif kind=='sin2':v*=arb(1) if zl<=0<=zh else A(1-min(abs(zl),abs(zh))**2).sqrt()
  ab[label]=v
 u3=sum((comb(3,i)*ab[f'u3_{u}_{i}']**2 for u in range(2) for i in range(4)),arb(0)).sqrt()
 r4=sum((comb(4,i)*ab[f'r4_{i}']**2 for i in range(5)),arb(0)).sqrt()
 return {'omega_u3':A(1-tl)**A(Q(3,5))*A(1+3*th)**A(Q(2,5))*u3,'omega_rho4':A(th).sqrt()*A(1-tl)**A(Q(11,10))*A(1+3*th)**A(Q(2,5))*r4}

def run():
 ctx.prec=320;start=time.monotonic();dest=HERE/'extra_coefficient_polynomials.json'
 if dest.exists():
  raw=json.loads(dest.read_text());s=json.loads((sc.BASE/'source_audit/state131_exact.json').read_text());assert raw['source_sha256']==s['canonical_serialization_sha256'];delta=Q(raw['delta']);P={(k.rsplit('_',1)[0],int(k.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for k,vals in raw['polynomials'].items()};kinds=raw['kinds']
 else:
  s,delta,P,kinds=construct();dest.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':s['canonical_serialization_sha256'],'delta':str(delta),'kinds':kinds,'polynomials':{f'{k}_{j}':encode(v) for (k,j),v in P.items()}},indent=2)+'\n')
 nt=max(i for p in P.values() for i,j in p);nz=max(j for p in P.values() for i,j in p);B=sc.make_blocks(P,nt,nz);Lt,Rt=sc.cc.split_matrices(nt);Lz,Rz=sc.cc.split_matrices(nz)
 print('constructed',nt,nz,'seconds',time.monotonic()-start,flush=True)
 stack=[(B,Q(0),Q(1),Q(-1),Q(1),'')];good=[];bad=[];n=0
 while stack and time.monotonic()-start<470:
  b,tl,th,zl,zh,path=stack.pop();n+=1;v=bound(b,tl,th,zl,zh,delta,kinds)
  if all(v[k].is_finite() and v[k]<=A(tar) for k,tar in TARGETS.items()):good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'upper':{k:x.str(50) for k,x in v.items()}})
  elif len(path)>=42:bad.append({'path':path,'upper':{k:x.str(30) for k,x in v.items()}})
  else:
   axis='t' if path.lower().count('t')<=path.lower().count('z')+2 else 'z';left,right=sc.cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
   if axis=='t':
    mid=(tl+th)/2;stack.extend([(right,mid,th,zl,zh,path+'T'),(left,tl,mid,zl,zh,path+'t')])
   else:
    mid=(zl+zh)/2;stack.extend([(right,tl,th,mid,zh,path+'Z'),(left,tl,th,zl,mid,path+'z')])
  if n%100==0:print(n,'good',len(good),'bad',len(bad),'pending',len(stack),'seconds',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','source_sha256':s['canonical_serialization_sha256'],'precision_bits':ctx.prec,'nt':nt,'nz':nz,'targets':{k:str(v) for k,v in TARGETS.items()},'accepted':good,'failed':bad,'pending':[x[-1] for x in stack],'elapsed_seconds':time.monotonic()-start}
 (HERE/'extra_coefficient_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(good),len(bad),len(stack),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
