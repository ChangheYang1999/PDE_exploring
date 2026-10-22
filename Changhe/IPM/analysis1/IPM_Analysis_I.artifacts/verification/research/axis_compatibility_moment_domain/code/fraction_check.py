from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import json,sys,hashlib
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3];D=R/'research/axis_compatibility_moment_domain';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def clean(a):return {k:v for k,v in a.items() if v}
def add(a,b):
 z=a.copy()
 for k,v in b.items():z[k]=z.get(k,Q(0))+v
 return clean(z)
def scale(a,v):return clean({k:c*v for k,c in a.items()})
def mul(a,b):
 z={}
 for i,u in a.items():
  for j,v in b.items():k=tuple(x+y for x,y in zip(i,j));z[k]=z.get(k,Q(0))+u*v
 return clean(z)
def deriv(a,j):
 z={}
 for k,v in a.items():
  if k[j]:m=list(k);m[j]-=1;z[tuple(m)]=v*k[j]
 return clean(z)
def serial(a):return {','.join(map(str,k)):str(v) for k,v in sorted(a.items())}
def variable(j,n):k=[0]*n;k[j]=1;return {tuple(k):Q(1)}
def power(a,n):
 z={(0,)*len(next(iter(a))):Q(1)}
 for j in range(n):z=mul(z,a)
 return z
start=datetime.now(timezone.utc).isoformat();pf=load(E/'proof_first.json');assert sha(D/'PROOF.md')==pf['proof_sha256'];parent='research/axis_weighted_nonlocal_mapping/evidence/verdict.json';want='4153e615de63865350b7b06900ff47909b414bbaac7da36170c280c9b7abcf78';assert sha(R/parent)==want;v=load(R/parent)
for n,h in v['files'].items():assert sha(R/n)==h,n
x,y,b0,b1,u0,u1,c,vel2=[variable(j,8) for j in range(8)];rho=add(mul(power(x,2),add(b0,mul(y,b1))),mul(power(x,4),c));Ux=scale(mul(x,u1),-1);Uy=add(add(u0,mul(y,u1)),mul(power(x,2),vel2));assert add(deriv(Ux,0),deriv(Uy,1))=={}
g=add(mul(Ux,deriv(rho,0)),mul(Uy,deriv(rho,1)));gxx=scale(deriv(deriv(g,0),0),Q(1,2));axis={k:z for k,z in gxx.items() if k[0]==k[1]==0};expected=add(scale(mul(b0,u1),-2),mul(b1,u0));assert axis==expected
q,bp,w,wp=[variable(j,4) for j in range(4)];cleared=add(scale(mul(power(q,2),add(scale(mul(bp,w),Q(1,2)),mul(power(q,2),wp))),2),scale(mul(bp,mul(power(q,2),w)),-1));assert cleared==scale(mul(power(q,4),wp),2)
rows=[]
for j in range(1,25):
 n=2*j;psi={(n-l,l):Q(comb(n,l)*(-1)**((l-1)//2)) for l in range(1,n+1,2)};px=deriv(psi,0);a={k:z for k,z in px.items() if k[0]==0};want_axis={(0,n-1):Q(n*(-1)**(j-1))};assert a==want_axis;rows.append({'j':j,'n':n,'axis_coefficient':str(next(iter(a.values()))),'axis_degree':n-1})
X,Y=[variable(j,2) for j in range(2)];normpoly=power(add(power(X,2),power(Y,2)),3);derivpoly={(6-2*j,2*j):Q(1) for j in range(4)};upperdiff=add(normpoly,scale(derivpoly,-1));lowerdiff=add(scale(derivpoly,3),scale(normpoly,-1));assert all(z>=0 for p in [upperdiff,lowerdiff] for z in p.values())
t=Q(3,50);assert 3+t==Q(153,50) and 0<t<Q(1,2);exponents={'gagliardo_small':-2*t,'gagliardo_large':-1-2*t,'fourier_kernel_small':1-2*t};assert exponents['gagliardo_small']>-1 and exponents['gagliardo_large']<-1 and exponents['fourier_kernel_small']>-1
op1=mul({(2,0):Q(-1),(0,2):Q(-1)},{(1,0):Q(1)});op2=mul({(1,0):Q(1)},{(2,0):Q(-1),(0,2):Q(-1)});assert op1==op2=={(3,0):Q(-1),(1,2):Q(-1)}
for N in range(1,21):
 ns=list(range(2,2*N+3,2));ls=[2*j+3 for j in range(N+1)];assert len(ns)==len(ls)==N+1 and [n+1 for n in ns]==ls
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_AXIS_ODE_HARMONIC_SOBOLEV_AND_MOMENT_INDEX_ALGEBRA_REQUIRES_INDEPENDENT_CHECK','code_sha256':sha(Path(__file__)),'proof_sha256':sha(D/'PROOF.md'),'parent_path':parent,'parent_sha256':sha(R/parent),'parent_files':v['files'],'parent_status':v['status'],'parent_pin_count':len(v['files']),'axis_variables':['x','y','b0','b1','u0','u1','c','vel2'],'axis_coefficient':serial(axis),'integrating_factor_cleared':serial(cleared),'harmonic_axis_rows':rows,'sobolev_upper_difference':serial(upperdiff),'sobolev_lower_difference':serial(lowerdiff),'fractional_t_exact':str(t),'radial_exponents_exact':{n:str(z) for n,z in exponents.items()},'laplacian_derivative_operator':serial(op1),'finite_index_examples':20,'scope':'Finite algebra only. ODE uniqueness, analytic continuation, infinite codimension and embedding are proved analytically in PROOF.md.'}
with (E/'fraction.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','fractional_t_exact','radial_exponents_exact']}))
