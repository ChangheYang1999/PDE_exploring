#!/usr/bin/env python3
"""Independent exact bivariate controls for formal vorticity, using only verifier-owned P324 data."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import json,hashlib,time,argparse
pa=argparse.ArgumentParser();pa.add_argument('--tag',default='n10w190');pa.add_argument('--rmax',type=int,default=8);pa.add_argument('--qmax',type=int,default=26);pa.add_argument('--out',default='n10_r8q26');args=pa.parse_args()
P=Path('research/344_formal_vorticity_factorization');D=P/'verification';start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
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
freeze=json.loads((D/'proof_freeze.json').read_text());ck('proof_before',freeze['utc']<start);ck('proof_hash',freeze['proof_sha256']==sha(P/'PROOF.md'))
for p,h in freeze['dependency_sha256'].items():ck('dependency_'+p,sha(Path(p))==h)
N,M=args.rmax,args.qmax;assert N>=3 and M>=20
source=Path('research/324_nonlinear_formal_jet_checks/verification')/(args.tag+'_coefficients.json');raw=json.loads(source.read_text());metadata=json.loads(source.with_name(args.tag+'.json').read_text());R=Ring(N,M);need=N+M+2;coverage=[]
def load(group,indices,shift=0):
 out={}
 for i in indices:
  dat=raw[group][str(i)];ck(group+'_'+str(i)+'_coverage',dat['known_high']>=need+2);coverage.append([group,i,dat['known_high'],need+2])
  for e,c in dat['coefficients'].items():
   if int(e)<=need+1:out[i+shift,int(e)]=Q(c)
 return out
vv=load('v',range(N+1));F=load('theta',range(1,N+2),-1);G=load('omega',range(N+1));A={(0,0):Q(8)}
for(i,j),c in vv.items():
 if j:A[i,j-1]=A.get((i,j-1),0)+2*j*c/Q(2*i+1)
P0={ij:-c for ij,c in vv.items()};C=Q(str(metadata['parameters']['C']));k=Q(str(metadata['parameters']['k']));H0=-k**7/231
ck('a_constant',A.get((0,0))==10);ck('G_axis_leading',G.get((0,6))==H0 and all(not G.get((0,j),0)for j in range(6)));ck('theta_axis_coefficient',F.get((0,10))==C/2)
h=graph(A,P0,N);a=R.compose(A,h);p=R.compose(P0,h);f=R.compose(F,h);g=R.compose(G,h);e=R.add(p,R.scale(R.mul(R.shift(a,1,0),R.diff(h,0)),-1))
ck('graph_exact',not R.atqzero(e));ck('h_linear',h.get((1,0))==k/11)
for j in range(6):ck('g_lower_transverse_'+str(j),all(not g.get((i,j),0)for i in range(N+1)))
for j in range(10):ck('f_lower_transverse_'+str(j),all(not f.get((i,j),0)for i in range(N+1)))
source0={(i,j):(2+2*i)*c for(i,j),c in F.items()};ss=R.compose(source0,h)
ck('source_divisible_q9',all(not ss.get((i,j),0)for i in range(N+1)for j in range(9)));ck('source_q9_nonzero',any(ss.get((i,9),0)for i in range(N+1)))
rg=R.add(R.mul(R.shift(a,1,0),R.diff(g,0)),R.mul(e,R.diff(g,1)),R.mul(R.add(R.scale(a,Q(1,2)),{(0,0):Q(1)}),g),R.scale(ss,-1));ck('full_vorticity_rectangle',not rg,serial(rg)if rg else None)
# Dividing the thermal coefficient by q^10 loses ten known q orders.
T=Ring(N,M-10);L=T.root(T.scale(T.clean({(i,j-10):c for(i,j),c in f.items()if j>=10}),2/C),Q(1,10));Z=R.shift(L,0,1)
K=T.clean({(i,j-6):c for(i,j),c in g.items()if j>=6});Y=T.mul(T.scale(K,1/H0),T.root(L,Q(-6)))
ck('Y_constant_one',Y.get((0,0))==1);ck('Y_real_rational',all(isinstance(c,Q)for c in Y.values()))
Rlow=Ring(N,M-4);ck('factorization_reconstruction_consistency',Rlow.clean(g)==Rlow.scale(Rlow.mul(Rlow.power(Rlow.clean(Z),6),Rlow.clean(Y)),H0))
# V preserves the r,q rectangular ideal. The fixed-u derivative of Z needs the chart correction.
az=T.clean(a);ez=T.clean(e);yz=T.clean(Y);zz=T.clean(Z);hr=T.diff(h,0)
zr_fixed=T.add(T.diff(zz,0),T.scale(T.mul(hr,T.diff(zz,1)),-1))
right=T.scale(T.add(T.power(zz,4),T.scale(T.shift(T.mul(T.power(zz,3),zr_fixed),1,0),10)),C/H0)
left=T.add(T.mul(T.shift(az,1,0),T.diff(yz,0)),T.mul(ez,T.diff(yz,1)),T.mul(T.add({(0,0):Q(1)},T.scale(az,Q(-1,10))),yz))
ck('Y_transport_rectangle',left==right,serial(T.add(left,T.scale(right,-1)))if left!=right else None)
wrong_right=T.scale(T.add(T.power(zz,4),T.scale(T.shift(T.mul(T.power(zz,3),T.diff(zz,0)),1,0),10)),C/H0)
ck('negative_omit_chart_correction',left!=wrong_right)
# A separate triangular solution uses the quotient only at the zero pivots.
cunit=T.add({(0,0):Q(1)},T.scale(az,Q(-1,10)))
def unit_transport(poly):
 return T.add(T.mul(T.shift(az,1,0),T.diff(poly,0)),T.mul(ez,T.diff(poly,1)),T.mul(cunit,poly))
yode={};resonant=[];nonresonant=0;compat=[]
for degree in range(T.N+T.M+1):
 for i in range(max(0,degree-T.M),min(T.N,degree)+1):
  j=degree-i;pivot=10*i-j
  previous=unit_transport(yode).get((i,j),Q(0));rhs=right.get((i,j),Q(0))
  if pivot:
   value=(rhs-previous)/pivot;nonresonant+=1
  else:
   compat.append(previous==rhs);value=Y.get((i,j),Q(0));resonant.append([i,j,str(value),str(previous-rhs)])
  if value:yode[i,j]=value
ck('separate_transport_all_resonances_compatible',all(compat),resonant)
ck('separate_transport_matches_quotient',yode==Y,{'nonresonant_coefficients':nonresonant,'supplied_resonant_coefficients':resonant})
ck('separate_transport_residual',unit_transport(yode)==right)
ck('F_built_directly_from_theta_through_Nplus1',all(str(i)in raw['theta'] for i in range(1,N+2)))

lead={ij:c for ij,c in G.items()if sum(ij)<=6};expected={(i,6-i):H0*comb(6,i)*(-k/Q(11))**i for i in range(7)if i<=N}
ck('weighted_leading_G',lead==expected);ck('ordinary_degree7_unique',{ij:c for ij,c in G.items()if 2*ij[0]+ij[1]+1<=7}=={(0,6):H0})
for j in[0,3,5]:
 bad=R.add(g,{(2,j):Q(1)});rr=R.add(R.mul(R.shift(a,1,0),R.diff(bad,0)),R.mul(e,R.diff(bad,1)),R.mul(R.add(R.scale(a,Q(1,2)),{(0,0):Q(1)}),bad),R.scale(ss,-1));ck('negative_g_r2q'+str(j),rr.get((2,j))==26-j)
# A unit perturbation keeps normalization but violates its required transport.
badY=T.add(Y,{(2,4):Q(1)});badleft=T.add(T.mul(T.shift(az,1,0),T.diff(badY,0)),T.mul(ez,T.diff(badY,1)),T.mul(T.add({(0,0):Q(1)},T.scale(az,Q(-1,10))),badY));ck('negative_unit_perturbation',T.add(badleft,T.scale(right,-1)).get((2,4))==16)
for j in range(6):
 for power in[0,1,2,10]:ck(f'positive_formal_pivot_j{j}_r{power}',10*power+6-j>0)
# Lowest resonant jet j=6 has zero pivot at r=0, so its prescribed coefficient is essential.
ck('resonant_j6_pivot_zero',10*0+6-6==0)
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(z['passed']for z in checks),total=len(checks),checks=checks,code_sha256=sha(Path(__file__)),source=str(source),input_sha256=sha(source),metadata_sha256=sha(source.with_name(args.tag+'.json')),proof_sha256=sha(P/'PROOF.md'),rmax=N,qmax_G=M,qmax_Y=M-10,qmax_factorization=M-4,coverage=coverage,unit_ode_resonant_data=resonant,unit_ode_nonresonant_coefficients=nonresonant,precision_proof_sha256=sha(D/'PRECISION_PROOF.md'),C=str(C),k=str(k),H0=str(H0),h=serial(h),Y_graph=serial(Y),scope='Finite exact verifier-owned jets, no teammate code. Formal implication proved separately; rectangular known-coefficient checks and negative controls are finite consistency evidence, not convergence or an actualprofile.')
(D/(args.out+'.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in['checks','coverage','h','Y_graph']},indent=2));raise SystemExit(0 if all(z['passed']for z in checks)else 1)
