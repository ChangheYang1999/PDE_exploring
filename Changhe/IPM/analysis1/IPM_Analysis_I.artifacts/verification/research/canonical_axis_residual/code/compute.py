from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial as fac,comb
import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import sys,json,hashlib,time
sys.dont_write_bytecode=True
import numpy as np
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/canonical_axis_residual';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ball(x):return {'display':x.str(55),'lo':str(dy(x.lower())),'hi':str(dy(x.upper()))}
def add(a,b):
 c=a.copy()
 for i,v in b.items():c[i]=c.get(i,F(0))+v
 return {i:v for i,v in c.items() if v}
def mul(a,b):
 c={}
 for i,u in a.items():
  for j,v in b.items():k=tuple(x+y for x,y in zip(i,j));c[k]=c.get(k,F(0))+u*v
 return {i:v for i,v in c.items() if v}
def scale(a,v):return {i:z*v for i,z in a.items() if z*v}
def derivative(a,k):
 c={}
 for i,v in a.items():
  if i[k]:j=list(i);j[k]-=1;c[tuple(j)]=v*i[k]
 return c
def var(j,n=6):k=[0]*n;k[j]=1;return {tuple(k):F(1)}
def powp(a,n):
 b={(0,)*len(next(iter(a))):F(1)}
 for j in range(n):b=mul(b,a)
 return b
def serial(p):return {','.join(map(str,i)):str(z) for i,z in sorted(p.items())}
start=now();timer=time.monotonic();pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['proof_sha256']
parent='research/axis_compatibility_moment_domain/evidence/verdict.json';assert sha(R/parent)=='c4a19ffedeaa50097a2a441ec447a8e65196c0f2388825eb36190be43a6906a8';pv=load(R/parent)
for n,h in pv['files'].items():assert sha(R/n)==h,n
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874';raw=np.load(npz,allow_pickle=False)
f=lambda v:F.from_float(float(v));k,bi,bo=(f(raw[n].item()) for n in ['k','bi','bo']);assert 0<k<F(1,2) and bi>4 and bo>4
knots=list(map(f,raw['knots']));nb=raw['S'].shape[1];assert raw['S'].shape==(260,1565) and raw['D'].shape==(260,7) and raw['Aout'].shape==(260,10) and len(knots)==nb+8 and int(raw['p'])==7
assert knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8 and all(knots[i]<knots[i+1] for i in range(7,nb))
meta=load(R/'data_exact/modal_v2.json');assert sha(R/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
jl=meta['outer_jl'];assert len(jl)==10 and all(type(j)==type(l)==int and min(j,l)>=0 for j,l in jl)
alpha=[k-3-j*(1-k)-2*l for j,l in jl];assert all(q<0 for q in alpha)
w={1:F(1),2:F(1),3:F(-1),4:F(-1)}
def project(name):return [sum((c*f(raw[name][m,j]) for m,c in w.items()),F(0)) for j in range(raw[name].shape[1])]
S,DD,AA=(project(n) for n in ['S','D','Aout'])
# Exact Cox basis polynomial in z=t-left endpoint, only on the first and last span.
def padd(a,b):
 q=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):q[i]+=v
 for i,v in enumerate(b):q[i]+=v
 return q
def plin(a,c,d):
 q=[F(0)]*(len(a)+1)
 for i,v in enumerate(a):q[i]+=c*v;q[i+1]+=d*v
 return q
def endpoint(span,right):
 left=knots[span];basis={span:[F(1)]}
 for degree in range(1,8):
  out={}
  for i in range(span-degree,span+1):
   v=[]
   if i in basis and knots[i+degree]!=knots[i]:v=padd(v,plin(basis[i],(left-knots[i])/(knots[i+degree]-knots[i]),1/(knots[i+degree]-knots[i])))
   if i+1 in basis and knots[i+degree+1]!=knots[i+1]:v=padd(v,plin(basis[i+1],(knots[i+degree+1]-left)/(knots[i+degree+1]-knots[i+1]),-1/(knots[i+degree+1]-knots[i+1])))
   out[i]=v
  basis=out
 part=[sum((basis[i][j] for i in basis),F(0)) for j in range(8)];assert part==[F(1)]+[F(0)]*7
 co=[sum((S[i]*basis[i][j] for i in basis),F(0)) for j in range(8)];x=knots[span+1]-left if right else F(0)
 return [sum((co[j]*F(fac(j),fac(j-n))*x**(j-n) for j in range(n,8)),F(0)) for n in range(7)]
ji=endpoint(7,False);jo=endpoint(nb-1,True)
pi=[sum((DD[j]*(2*j+2)**n for j in range(7)),F(0)) for n in range(7)];po=[sum((AA[j]*alpha[j]**n for j in range(10)),F(0)) for n in range(7)]
def join(J,P,b):
 out=[sum(((-b)**(i-j)*(J[j]-P[j])/fac(i-j)/fac(j) for j in range(i+1)),F(0)) for i in range(7)]
 for n in range(7):assert P[n]+sum((out[j]*F(fac(n),fac(n-j))*b**(n-j) for j in range(n+1)),F(0))==J[n]
 return out
Ei=join(ji,pi,bi);Eo=join(jo,po,-bo)
Ii=sum((DD[j]/(2*j+2)+Ei[j]*(-1)**j*fac(j)/bi**(j+1) for j in range(7)),F(0))
Im=sum((S[j]*(knots[j+8]-knots[j])/8 for j in range(nb)),F(0))
Io=sum((AA[j]/(-alpha[j]) for j in range(10)),F(0))+sum((Eo[j]*fac(j)/bo**(j+1) for j in range(7)),F(0));I=Ii+Im+Io
Braw=sum(((-1)**m*f(raw['D'][m,0]) for m in range(260)),F(0));B=aa(Braw)*(-2*aa(knots[0])).exp();ell=1/k;beta=4*ell-1;H4=I/16-F(1,64);Ac=-F(1,6)-4*H4;Q=2*aa(beta)*B-5*aa(Ac)
assert (Q-(2*aa(beta)*B+aa(F(25,48)+5*I/4))).contains(0)
# Independent exact angular sign selection in sine coefficients.
proj={}
for m in range(260):
 c=F(0)
 for base in [1,3]:
  for n in [base+2*m,base-2*m]:
   if abs(n)==5:c+=F(1 if n>0 else -1,8)
 if c:proj[m]=c
assert proj=={1:F(1,8),2:F(1,8),3:F(-1,8),4:F(-1,8)}
# Jet calculation uses divergence-free velocity and generic B,A,ell,sigma.
x,y,L,sigma,Bv,Av=[var(j) for j in range(6)];one={(0,)*6:F(1)}
rho=mul(powp(x,2),add(y,mul(Bv,powp(y,3))))
uy=add(mul(sigma,y),mul(Av,powp(y,3)));ux=scale(mul(x,add(sigma,scale(mul(Av,powp(y,2)),3))),-1)
assert add(derivative(ux,0),derivative(uy,1))=={}
res=add(add(mul(add(mul(L,x),ux),derivative(rho,0)),mul(add(mul(L,y),uy),derivative(rho,1))),scale(rho,-1))
axis={i:z for i,z in scale(derivative(derivative(res,0),0),F(1,2)).items() if i[0]==0}
# Substitute sigma=3ell-1 by polynomial expansion.
sub={}
for i,z in axis.items():
 base={tuple(0 if j==3 else v for j,v in enumerate(i)):z}
 sub=add(sub,mul(base,powp(add(scale(L,3),scale(one,-1)),i[3])))
low={i:z for i,z in sub.items() if i[1]<=3}
want=mul(powp(y,3),add(mul(add(scale(L,8),scale(one,-2)),Bv),scale(Av,-5)))
assert low==want
assert -F(1,2)*F(1,4)*F(1,8)==-F(1,64)
lo,hi=dy(Q.lower()),dy(Q.upper());assert lo*hi>0
# A strict rational decimal window, chosen by exact arithmetic from this first enclosure.
scale10=10**12
while (lo*scale10).__floor__()==0 or (hi*scale10).__ceil__()==0:scale10*=10
wlo=F((lo*scale10).__floor__()-1,scale10);whi=F((hi*scale10).__ceil__()+1,scale10);assert wlo<lo<=hi<whi and wlo*whi>0
out={'start_utc':start,'utc':now(),'seconds':time.monotonic()-timer,'status':'PASS_EXACT_AXIS_COEFFICIENT_AND_ARB512_NONZERO_REQUIRES_INDEPENDENT_CHECK','code_sha256':sha(Path(__file__)),'proof_sha256':sha(D/'PROOF.md'),'parent_path':parent,'parent_sha256':sha(R/parent),'parent_files':pv['files'],'parent_pin_count':len(pv['files']),'NPZ_sha256':sha(npz),'exact':{n:str(v) for n,v in {'k':k,'a':knots[0],'bi':bi,'bo':bo,'Braw':Braw,'I_inner':Ii,'I_middle':Im,'I_outer':Io,'I':I,'H4':H4,'A':Ac,'beta':beta}.items()},'jets_inner':list(map(str,ji)),'jets_outer':list(map(str,jo)),'joins_inner':list(map(str,Ei)),'joins_outer':list(map(str,Eo)),'exact_join_equations':14,'spline_spans':nb-7,'angular_projection':{str(m):str(z) for m,z in proj.items()},'axis_polynomial_after_normalization':serial(low),'origin_quartic_correction':'-1/64','balls':{'B':ball(B),'Q':ball(Q)},'Q_strict_window':[str(wlo),str(whi)],'Q_sign':'POSITIVE' if lo>0 else 'NEGATIVE','scope':'Actual exact normalized trial coefficient. Finite arithmetic plus PROOF.md gives Y nonmembership if independently verified; not a PDE endpoint.'}
(E/'compute.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ['utc','seconds','status','Q_strict_window','Q_sign']}));print('B',out['balls']['B']['display']);print('Q',out['balls']['Q']['display'])
