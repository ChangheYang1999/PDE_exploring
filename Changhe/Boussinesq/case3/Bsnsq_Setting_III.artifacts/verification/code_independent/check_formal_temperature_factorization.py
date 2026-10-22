#!/usr/bin/env python3
"""Independent sparse bivariate Fraction algebra on own P324 data; no teammate code."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import json,hashlib,time,argparse
pa=argparse.ArgumentParser();pa.add_argument('--rmax',type=int,default=8);pa.add_argument('--qmax',type=int,default=16);pa.add_argument('--tag',default='n8w160');pa.add_argument('--out',default='n8_r8q16');args=pa.parse_args()
P=Path('research/331_formal_temperature_factorization');V=P/'verification';start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def ck(name,test,detail=None):
 checks.append(dict(name=name,passed=bool(test),detail=detail))
 if not test:print('FAIL',name,detail,flush=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class Ring:
 def __init__(self,N,M):self.N,self.M=N,M
 def clean(self,p):return{(i,j):Q(v)for(i,j),v in p.items()if v and 0<=i<=self.N and 0<=j<=self.M}
 def add(self,*polys):
  z={}
  for p in polys:
   for a,v in p.items():z[a]=z.get(a,0)+v
  return self.clean(z)
 def scale(self,p,c):return self.clean({a:v*c for a,v in p.items()})
 def mul(self,a,b):
  z={}
  for(i,j),v in a.items():
   for(k,l),w in b.items():
    if i+k<=self.N and j+l<=self.M:
     t=(i+k,j+l);z[t]=z.get(t,0)+v*w
  return self.clean(z)
 def power(self,a,n):
  z={(0,0):Q(1)}
  while n:
   if n%2:z=self.mul(z,a)
   n//=2
   if n:a=self.mul(a,a)
  return z
 def diff(self,p,axis):
  z={}
  for(i,j),v in p.items():
   if axis==0 and i:z[i-1,j]=i*v
   if axis==1 and j:z[i,j-1]=j*v
  return self.clean(z)
 def shift(self,p,i,j):return self.clean({(a+i,b+j):v for(a,b),v in p.items()})
 def root(self,p,alpha):
  assert p.get((0,0),0)==1
  u=self.add(p,{(0,0):Q(-1)});z={(0,0):Q(1)};term=dict(z);c=Q(1)
  for n in range(1,self.N+self.M+1):
   term=self.mul(term,u);c=c*(alpha-n+1)/n;z=self.add(z,self.scale(term,c))
   if not term:break
  return z
 def compose(self,p,h):
  # Finite binomial substitution s=q+h(r); h has zero constant.
  assert h.get((0,0),0)==0 and all(j==0 for i,j in h)
  hp=[{(0,0):Q(1)}]
  for n in range(self.N):hp.append(self.mul(hp[-1],h))
  out={}
  for(i,d),v in p.items():
   if i>self.N:continue
   for j in range(max(0,d-self.N+i),min(d,self.M)+1):
    for(a,b),w in hp[d-j].items():
     if i+a<=self.N:
      t=(i+a,j);out[t]=out.get(t,0)+v*comb(d,j)*w
  return self.clean(out)
 def atqzero(self,p):return{a:v for a,v in p.items()if a[1]==0}

def graph(A,P,N):
 g=Ring(N,0);h={}
 for m in range(1,N+1):
  a=g.compose(A,h);p=g.compose(P,h);res=g.add(p,g.scale(g.mul(g.shift(a,1,0),g.diff(h,0)),-1));h[m,0]=res.get((m,0),0)/Q(10*m+1)
 return g.clean(h)
def serial(p):return{str(i)+','+str(j):str(v)for(i,j),v in sorted(p.items())}
fr=json.loads((V/'proof_freeze_v5.json').read_text());ck('proof_precedes',datetime.fromisoformat(fr['utc'])<datetime.fromisoformat(start));ck('proof_hash',sha(P/'PROOF.md')==fr['sha256'])
for p,h in fr['dependency_sha256'].items():ck('dependency_'+p,sha(Path(p))==h)
N,M=args.rmax,args.qmax;assert M>=12
rawpath=Path('research/324_nonlinear_formal_jet_checks/verification')/(args.tag+'_coefficients.json');raw=json.loads(rawpath.read_text());R=Ring(N,M);srcS=N+M+2
coverage=[]
def load(group,indices,shift=0):
 z={}
 for i in indices:
  d=raw[group][str(i)];ck(group+'_'+str(i)+'_coverage',d['known_high']>=srcS+1,{'known_high':d['known_high'],'needed':srcS+1});coverage.append([group,i,d['known_high'],srcS+1])
  for e,v in d['coefficients'].items():
   j=int(e)
   if j<=srcS+1:z[i+shift,j]=Q(v)
 return z
v=load('v',range(N+1));F=load('theta',range(1,N+2),-1)
A={(0,0):Q(8)}
for(i,j),c in v.items():
 if j:A[i,j-1]=A.get((i,j-1),0)+2*j*c/Q(2*i+1)
P0={a:-c for a,c in v.items()};C=2*F.get((0,10),0);k=P0.get((1,0),0)
meta_path=rawpath.with_name(args.tag+'.json');meta=json.loads(meta_path.read_text());decl=meta['parameters']
ck('declared_C_k',C==Q(str(decl['C'])) and k==Q(str(decl['k'])))
B={j:c for(i,j),c in v.items()if i==0};ck('exact_base_B',B=={1:Q(1),2:k,13:-C*k/260})
ck('k_matches_B_and_v1',B.get(2,0)==-v.get((1,0),0)==k)
ck('C_nonzero',C!=0);ck('A_constant',A.get((0,0))==10);ck('P_linear',P0.get((0,1))==-1 and P0.get((0,0),0)==0);ck('F_axis_leading',all(F.get((0,j),0)==0 for j in range(10)))
h=graph(A,P0,N);ck('h_linear',h.get((1,0),0)==k/11)
a=R.compose(A,h);p=R.compose(P0,h);f=R.compose(F,h);e=R.add(p,R.scale(R.mul(R.shift(a,1,0),R.diff(h,0)),-1))
ck('graph_residual_q0_exact',not R.atqzero(e));ck('q_vector_linear',e.get((0,1))==-1)
for j in range(10):ck('f_divisible_q10_coefficient_'+str(j),all(f.get((i,j),0)==0 for i in range(N+1)))
# V preserves the rectangular ideal because its components are divisible by r and q.
thermal=R.add(R.mul(R.shift(a,1,0),R.diff(f,0)),R.mul(e,R.diff(f,1)),R.mul(a,f));ck('consistency_thermal_equation_rectangle',not thermal,serial(thermal)if thermal else None)
S=Ring(N,M-10);K=S.clean({(i,j-10):c for(i,j),c in f.items()if j>=10});U=S.scale(K,2/C);L=S.root(U,Q(1,10));ck('root_constant',L.get((0,0))==1);ck('unit_tenth_power',S.power(L,10)==U)
Z=R.shift(L,0,1);low=Ring(N,M-9);az=low.clean(a);ez=low.clean(e);zr=low.clean(Z)
zeq=low.add(low.mul(low.shift(az,1,0),low.diff(zr,0)),low.mul(ez,low.diff(zr,1)),low.scale(low.mul(az,zr),Q(1,10)))
ck('Z_transport_rectangle',not zeq,serial(zeq)if zeq else None)
ck('consistency_factorization_rectangle',R.scale(R.power(Z,10),C/2)==f)
# Deliberately wrong q graph must fail; noninvariant thermal perturbations must be detected.
hwrong=R.add(h,{(1,0):Q(1,100)});ww=R.add(R.compose(P0,hwrong),R.scale(R.mul(R.shift(R.compose(A,hwrong),1,0),R.diff(hwrong,0)),-1));ck('negative_wrong_graph_detected',bool(R.atqzero(ww)))
for j in [0,3,9]:
 bad=R.add(f,{(0,j):Q(1)});res=R.add(R.mul(R.shift(a,1,0),R.diff(bad,0)),R.mul(e,R.diff(bad,1)),R.mul(a,bad));ck('negative_noninvariant_q'+str(j),res.get((0,j),0)==10-j and bool(res));ck('negative_divisibility_q'+str(j),any(bad.get((i,j),0)!=0 for i in range(N+1)))
# Deeper source perturbations test sensitivity beyond the linear smoke controls.
Fbad=dict(F);Fbad[2,12]=Fbad.get((2,12),0)+Q(7,13);fbad=R.compose(Fbad,h)
ck('deep_theta3_s12_divisibility_detected',any(fbad.get((i,j),0) for i in range(N+1) for j in range(10)))
Abad=dict(A);Pbad=dict(P0);Abad[3,2]=Abad.get((3,2),0)+Q(6,13);Pbad[3,3]=Pbad.get((3,3),0)-Q(7,13)
ab=R.compose(Abad,h);pb=R.compose(Pbad,h);eb=R.add(pb,R.scale(R.mul(R.shift(ab,1,0),R.diff(h,0)),-1))
rb=R.add(R.mul(R.shift(ab,1,0),R.diff(f,0)),R.mul(eb,R.diff(f,1)),R.mul(ab,f))
ck('deep_v3_s3_thermal_detected',bool(rb))
Aw={(0,0):Q(8)}
for(i,j),c in v.items():
 if j:Aw[i,j-1]=Aw.get((i,j-1),0)+2*j*c/Q(2*i+1 if i==0 else 2*i+3)
aw=R.compose(Aw,h);ew=R.add(p,R.scale(R.mul(R.shift(aw,1,0),R.diff(h,0)),-1))
rw=R.add(R.mul(R.shift(aw,1,0),R.diff(f,0)),R.mul(ew,R.diff(f,1)),R.mul(aw,f))
ck('wrong_thermal_weight_detected',bool(rw))
# Manufactured nonlinear example uses a prescribed Z=q(1+r+q/3), A=10+r+q^2.
# Define e from VZ=-AZ/10; the inverse of Z_q is a unit in the quotient.
T=Ring(4,15);aa={(0,0):Q(10),(1,0):Q(1),(0,2):Q(1)};zz={(0,1):Q(1),(1,1):Q(1),(0,2):Q(1,3)}
num=T.add(T.scale(T.mul(aa,zz),Q(-1,10)),T.scale(T.mul(T.shift(aa,1,0),T.diff(zz,0)),-1));dz=T.diff(zz,1);ee=T.mul(num,T.root(dz,Q(-1)));ff=T.scale(T.power(zz,10),Q(-3,4));rr=T.add(T.mul(T.shift(aa,1,0),T.diff(ff,0)),T.mul(ee,T.diff(ff,1)),T.mul(aa,ff))
# Manufacture in q coordinates, whose e has q factor; no lost-edge derivative inputs are used.
ck('manufactured_q_factor',not T.atqzero(ee));ck('consistency_manufactured_transport',not rr);ck('manufactured_not_linear',any(i+j>1 for i,j in ee))
rootring=Ring(4,5);uu=rootring.scale(rootring.clean({(i,j-10):c for(i,j),c in ff.items()if j>=10}),Q(-4,3));ll=rootring.root(uu,Q(1,10));ck('manufactured_root_recovers_prescribed_unit',ll=={(0,0):Q(1),(1,0):Q(1),(0,1):Q(1,3)})
res={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(x['passed']for x in checks),'total':len(checks),'checks':checks,'code_sha256':sha(Path(__file__)),'input_sha256':sha(rawpath),'metadata_sha256':sha(meta_path),'input':str(rawpath),'C':str(C),'k':str(k),'rmax':N,'qmax_F':M,'qmax_Z':M-9,'source_s_needed':srcS+1,'coverage':coverage,'h':serial(h),'Z_in_graph_coordinates':serial(Z),'scope':'Exact rational arithmetic on P324 stated-exact jets within recorded coverage. Thermal/factorization/manufactured transport are consistency controls; simple negatives are smoke tests. No convergence, actual graph or profile claim.'}
(V/(args.out+'.json')).write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items()if k not in ['checks','h','Z_in_graph_coordinates','coverage']},indent=2),flush=True);print('h',serial(h),flush=True);raise SystemExit(0 if all(x['passed']for x in checks)else 1)
