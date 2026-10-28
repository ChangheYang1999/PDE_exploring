"""Exact compactified tensor coefficients; Arb continuum bounds, no sampling acceptance."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import json,sys,time
from flint import arb,arb_mat,ctx
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'02_energy/verification'))
from compact_matrix import A,add,derivative,chebyshev,encode
import compact_certificate as cc

def plus(*terms):
 out={}
 for scale,p in terms:
  for key,v in p.items():out[key]=out.get(key,Q(0))+scale*v
 return {k:v for k,v in out.items() if v}

def mul(p,q):
 out={}
 for (i,j),v in p.items():
  for (a,b),c in q.items():out[i+a,j+b]=out.get((i+a,j+b),Q(0))+v*c
 return {k:v for k,v in out.items() if v}

def oddpoly(n,kind):
 assert n%2 and n>0;m=(n-1)//2
 seq=[[Q(1)],[Q(1 if kind=='s' else -1),Q(2)]]
 while len(seq)<=m:
  z=[Q(0)]*(len(seq[-1])+1)
  for i,c in enumerate(seq[-1]):z[i+1]+=2*c
  for i,c in enumerate(seq[-2]):z[i]-=c
  seq.append(z)
 return seq[m]

def construct():
 s=json.loads((BASE/'source_audit/state131_exact.json').read_text());gamma=1/Q(s['exact_parameters']['cl']);delta=1-gamma
 P={};kinds={}
 for order in (5,6):
  for nx in range(order+1):
   label=f'd{order}_{nx}';axes='x'*nx+'y'*(order-nx);kind='s' if (order-nx)%2 else 'c'
   kinds[label]=('sin' if kind=='s' else 'cos') if order==5 else ('sin2' if kind=='s' else 'one')
   for branch in range(4):
    trig={};p=(3+gamma-branch*delta)/2
    for (j,m,k),v in zip(s['canonical_order'],s['canonical_coefficients']):
     if j!=branch:continue
     tt={('c',2*m,0):Q(v)}
     for di,axis in enumerate(axes):tt=derivative(tt,p,k,di,axis)
     for (ki,n,l),v in tt.items():add(trig,ki,n,k-3+l,v)
    assert all(l>=0 for ki,n,l in trig),(order,nx,min(l for ki,n,l in trig))
    poly={}
    for (ki,n,l),v in trig.items():
     assert ki==kind
     C=oddpoly(n,ki) if order==5 else (chebyshev(n//2-1,'U') if ki=='s' else chebyshev(n//2))
     for zi,a in enumerate(C):poly[l,zi]=poly.get((l,zi),Q(0))+v*a
    P[label,branch]={k:v for k,v in poly.items() if v}
 old=json.loads((BASE/'02_energy/verification/state131_auxiliary_polynomials.json').read_text())
 for j in range(4):
  def oldp(label):return {(i,k):Q(v) for i,k,v in old['polynomials'][f'{label}_{j}']}
  P['rx',j]=plus((-1,oldp('chi31')),(-1,oldp('chi13')))
  P['ry',j]=plus((-1,oldp('chi22')),(-1,oldp('chi04')))
  for i in range(3):P[f'r2_{i}',j]=plus((-1,P[f'd5_{i+2}',j]),(-1,P[f'd5_{i}',j]));kinds[f'r2_{i}']='cos' if i%2 else 'sin'
  for i in range(4):P[f'r3_{i}',j]=plus((-1,P[f'd6_{i+2}',j]),(-1,P[f'd6_{i}',j]));kinds[f'r3_{i}']='sin2' if i%2 else 'one'
  for u in range(2):
   for i in range(3):
    key=f'u2_{u}_{i}';source=f'd5_{i+1+u}';P[key,j]=plus(((-1 if u==0 else 1),P[source,j]));kinds[key]=kinds[source]
  q={(0,0):Q(1),(1,0):Q(3)};zp={(0,0):Q(1),(0,1):Q(1)};zm={(0,0):Q(1),(0,1):Q(-1)};t={(1,0):Q(1)}
  P['kb_xx',j]=plus((1,mul(q,P['r2_2',j])),(Q(32,5),mul(zp,P['rx',j])))
  P['kb_yx',j]=plus((1,mul(q,P['r2_1',j])),(Q(32,5),mul(zm,P['rx',j])))
  P['kb_xy',j]=plus((1,mul(q,P['r2_1',j])),(Q(32,5),P['ry',j]))
  P['kb_yy',j]=plus((1,mul(q,P['r2_0',j])),(Q(32,5),P['ry',j]))
  for k in ('xx','yx','xy','yy'):kinds['kb_'+k]='sin' if k in ('xx','yy') else 'cos'
  P['scalar',j]=plus((Q(-128,25),mul(mul(t,{(0,0):Q(1),(0,2):Q(-1)}),P['rx',j])),(1,mul(plus((Q(-32,5),q),(Q(128,25),mul(t,zp))),P['ry',j])),(Q(-16,5),mul(mul(mul(t,zp),q),P['r2_1',j])),(Q(16,5),mul(mul(mul(t,zm),q),P['r2_2',j])))
 kinds['scalar']='one'
 for key in list(P):
  if key[0].startswith('d'):del P[key]
 kinds={k:v for k,v in kinds.items() if not k.startswith('d')};kinds['rx']='sin2';kinds['ry']='one'
 return s,delta,P,kinds

TARGETS={'rho2':Q(3),'rho2_weighted':Q(8),'rho3_weighted':Q(32),'u2_weighted':Q(3),'omega_rho2':Q(8),'omega_rho3':Q(10),'omega_u2':Q(3),'kb':Q(28),'scalar':Q(40)}

def make_blocks(P,nt,nz):
 tt=cc.transforms(nt);zz=cc.transforms(nz,Q(-1),Q(1)).transpose();B={}
 for key,poly in P.items():
  M=arb_mat(nt+1,nz+1)
  for (i,j),v in poly.items():M[i,j]=A(v)
  B[key]=tt*M*zz
 return B

def bound(B,tl,th,zl,zh,delta,kinds):
 wl=(1-A(th))**(A(delta)/2);wu=(1-A(tl))**(A(delta)/2);W=cc.wcoeff(wl,wu)
 ab={}
 for label,kind in kinds.items():
  if label in ('rx','ry'):continue
  lo,hi=cc.hull((W*arb_mat([B[label,j].entries() for j in range(4)])).entries());v=abs(lo).max(abs(hi))
  if kind=='sin':v*=A((1-zl)/2).sqrt()
  elif kind=='cos':v*=A((1+zh)/2).sqrt()
  elif kind=='sin2':v*=arb(1) if zl<=0<=zh else A(1-min(abs(zl),abs(zh))**2).sqrt()
  ab[label]=v
 def norm(labels):return sum((m*ab[k]**2 for k,m in labels),arb(0)).sqrt()
 r2=norm([(f'r2_{i}',comb(2,i)) for i in range(3)])
 r3=norm([(f'r3_{i}',comb(3,i)) for i in range(4)])
 u2=norm([(f'u2_{u}_{i}',comb(2,i)) for u in range(2) for i in range(3)])
 sqrt_t=A(th).sqrt();sqrt_ot=A(1-tl).sqrt()
 common=sqrt_t*A(1-tl)**A(Q(1,10))*A(1+3*th)**A(Q(2,5))
 return {'rho2':sqrt_t*sqrt_ot*r2,'rho2_weighted':sqrt_t*r2,'rho3_weighted':r3,'u2_weighted':sqrt_t*u2,'omega_rho2':common*r2,'omega_rho3':A(1-tl)**A(Q(3,5))*A(1+3*th)**A(Q(2,5))*r3,'omega_u2':common*u2,'kb':sqrt_t*A(1-tl)**A(Q(1,10))*A(1+3*tl)**A(Q(-3,5))*norm([('kb_'+k,1) for k in ('xx','yx','xy','yy')]),'scalar':A(Q(1,2))*A(1-tl)**A(Q(1,5))*A(1+3*tl)**A(Q(-6,5))*ab['scalar']}

def run():
 ctx.prec=320;start=time.monotonic();dest=HERE/'sharp_coefficient_polynomials.json'
 if dest.exists():
  raw=json.loads(dest.read_text());s=json.loads((BASE/'source_audit/state131_exact.json').read_text());assert raw['source_sha256']==s['canonical_serialization_sha256'];delta=Q(raw['delta']);P={(k.rsplit('_',1)[0],int(k.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for k,vals in raw['polynomials'].items()};kinds=raw['kinds']
 else:
  s,delta,P,kinds=construct();dest.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':s['canonical_serialization_sha256'],'delta':str(delta),'kinds':kinds,'polynomials':{f'{k}_{j}':encode(v) for (k,j),v in P.items()}},indent=2)+'\n')
 nt=max(i for p in P.values() for i,j in p);nz=max(j for p in P.values() for i,j in p);B=make_blocks(P,nt,nz);Lt,Rt=cc.split_matrices(nt);Lz,Rz=cc.split_matrices(nz)
 print('constructed',nt,nz,'seconds',time.monotonic()-start,flush=True)
 stack=[(B,Q(0),Q(1),Q(-1),Q(1),'')];good=[];bad=[];n=0
 while stack and time.monotonic()-start<470:
  b,tl,th,zl,zh,path=stack.pop();n+=1;v=bound(b,tl,th,zl,zh,delta,kinds)
  if all(v[k].is_finite() and v[k]<=A(tar) for k,tar in TARGETS.items()):good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'upper':{k:x.str(50) for k,x in v.items()}})
  elif len(path)>=42:bad.append({'path':path,'upper':{k:x.str(30) for k,x in v.items()}})
  else:
   # Keep balanced refinement for compact, auditable partitions.
   axis='t' if path.lower().count('t')<=path.lower().count('z')+2 else 'z'
   left,right=cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
   if axis=='t':
    mid=(tl+th)/2;children=[(left,tl,mid,zl,zh,path+'t'),(right,mid,th,zl,zh,path+'T')]
   else:
    mid=(zl+zh)/2;children=[(left,tl,th,zl,mid,path+'z'),(right,tl,th,mid,zh,path+'Z')]
   stack.extend(reversed(children))
  if n%100==0:print(n,'good',len(good),'bad',len(bad),'pending',len(stack),'seconds',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','source_sha256':s['canonical_serialization_sha256'],'precision_bits':ctx.prec,'nt':nt,'nz':nz,'targets':{k:str(v) for k,v in TARGETS.items()},'accepted':good,'failed':bad,'pending':[x[-1] for x in stack],'elapsed_seconds':time.monotonic()-start}
 (HERE/'sharp_coefficient_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(good),len(bad),len(stack),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
