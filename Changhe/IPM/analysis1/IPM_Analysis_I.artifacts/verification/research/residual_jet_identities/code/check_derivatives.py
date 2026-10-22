"""Exact differential algebra: source recurrences versus direct IPM derivatives."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import comb,factorial
import ast,hashlib,json,time,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_v22/source/src/cert_resid.py';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();source_sha='1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053';assert sha(S)==source_sha
t0=time.monotonic();tree=ast.parse(S.read_text());core=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_cell_core_deriv')
# Read the two actual cst expressions. Their small integer values happen to
# be exactly represented, which is checked independently for every split.
csts=[x for x in ast.walk(core) if isinstance(x,ast.Assign) and len(x.targets)==1 and ast.unparse(x.targets[0])=='cst'];assert len(csts)==2
csts=sorted(csts,key=lambda x:(x.lineno,x.col_offset));codes=[compile(ast.Expression(x.value),str(S),'eval') for x in csts]
class ExactMR:
 @staticmethod
 def exact(x):return F(x)
source_inner={};source_outer={};cst_checks=0
for i in range(5):
 for l in range(i+1):
  env={'__builtins__':{},'_comb':comb,'i':i,'l':l,'float':float,'MR':ExactMR}
  a=F(eval(codes[0],env));b=F(eval(codes[1],env))
  assert a==comb(i,l)*(-2)**(i-l) and b==comb(i,l)
  source_inner[i,l]=a;source_outer[i,l]=b;cst_checks+=2
# Linear combinations in A,B,g_0,..., or bilinear terms H*R_k, all carrying
# the common exponential e^-2t. Differentiation reduces the ODE immediately.
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v}
def sc(p,a):return {k:v*a for k,v in p.items() if v*a}
def dH(h,n):
 if h=='A':return {'A':-2*n,'g0':1}
 if h=='B':return {'B':2*n,'g0':-1}
 assert h.startswith('g');return {'g'+str(int(h[1:])+1):1}
def direct_D(p,n):
 out={}
 for (h,k),v in p.items():
  for key,w in { (h,k):-2,(h,k+1):1}.items():out[key]=out.get(key,0)+v*w
  for hh,w in dH(h,n).items():out[hh,k]=out.get((hh,k),0)+v*w
 return {k:v for k,v in out.items() if v}
def attach(p,k):return {(h,k):v for h,v in p.items()}
checks=0;coeffchecks=0;records=[];maxg=-1
for n in range(1,262):
 # First method: actual source ODE recurrences as exact smooth-function jets.
 A=[{'A':F(1)}];Bb=[{'B':F(1)}]
 for i in range(4):A.append(add(sc(A[-1],-2*n),{'g'+str(i):F(1)}));Bb.append(add(sc(Bb[-1],2*n),{'g'+str(i):F(-1)}))
 Ps=[];Qs=[]
 for i in range(5):
  p={};q={}
  for l in range(i+1):
   cst=source_inner[i,l];p=add(p,sc(add(A[l],Bb[l]),-cst));q=add(q,sc(add(Bb[l],sc(A[l],-1)),cst))
  Ps.append(p);Qs.append(q)
 # These are 4P/e^-2t and 4Q/e^-2t. w_j remains an arbitrary scalar;
 # comparing its coefficient is an identity for every j, not sampling j.
 rawR={('A',1):F(-1),('B',1):F(-1)};rawT={('B',0):F(1),('A',0):F(-1)}
 for i in range(5):
  srcR={};srcT={}
  for l in range(i+1):
   srcR=add(srcR,attach(sc(Ps[l],source_outer[i,l]),1+i-l));srcT=add(srcT,attach(sc(Qs[l],source_outer[i,l]),i-l))
  assert srcR==rawR,(n,i,'radial');assert srcT==rawT,(n,i,'tangent')
  checks+=2;coeffchecks+=len(set(srcR)|set(rawR))+len(set(srcT)|set(rawT))
  for h,k in set(srcR)|set(srcT):
   assert k<=i+1
   if h.startswith('g'):maxg=max(maxg,int(h[1:]));assert int(h[1:])<=i-1
  if n in [1,261]:records.append({'n':n,'order':i,'radial_terms':[[h,k,str(v)] for (h,k),v in sorted(srcR.items())],'tangent_per_w_terms':[[h,k,str(v)] for (h,k),v in sorted(srcT.items())]})
  rawR=direct_D(rawR,n);rawT=direct_D(rawT,n)
assert checks==2610 and maxg==3
# Independent exact monomial recurrence, symbolic beta and sigma.
# Keys(beta_power,sigma_power). A polynomial basis spans all degree<=7 input.
polychecks=polycoeffchecks=0
for d in range(8):
 p={(0,d):1}
 for i in range(14):
  closed={(i-k,d-k):comb(i,k)*factorial(d)//factorial(d-k) for k in range(min(i,d)+1)}
  assert p==closed,(d,i);polychecks+=1;polycoeffchecks+=len(p)
  nxt={}
  for (a,b),c in p.items():
   nxt[a+1,b]=nxt.get((a+1,b),0)+c
   if b:nxt[a,b-1]=nxt.get((a,b-1),0)+b*c
  p=nxt
assert polychecks==112
# Count full source derivative products: two scatters for each i,l.
scatters=2*sum(i+1 for i in range(5));assert scatters==30
# Two independent integer identities for the exact Poisson factor at every n.
pois=0
for n in range(1,262):
 # psi'=(A'+B')/(4n); g cancels and psi''=n(A+B)-g.
 psip=add(sc({'A':-2*n,'g0':1},F(1,4*n)),sc({'B':2*n,'g0':-1},F(1,4*n)))
 assert psip=={'A':F(-1,2),'B':F(1,2)}
 psipp={}
 for h,v in psip.items():psipp=add(psipp,sc(dH(h,n),v))
 assert psipp=={'A':F(n),'B':F(n),'g0':F(-1)}
 assert F(-n)*F(1,4*n)==F(-1,4);pois+=3
assert sha(S)==source_sha
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_EXACT_ODE_REDUCED_RESIDUAL_DERIVATIVES',all_n=261,derivative_orders=list(range(5)),radial_and_tangential_identities=checks,coefficient_equalities=coeffchecks,arbitrary_angular_weight='Coefficient of arbitrary scalar w_j compared exactly; applies to every j after source w_j linkage',source_constant_checks=cst_checks,source_cst_bindings=[{'line':x.lineno,'expression':ast.unparse(x.value)} for x in csts],poisson_scalar_identities=pois,maximum_g_derivative_used=maxg,maximum_R_derivative_used=5,monomial_basis_degree=7,exponential_polynomial_orders=list(range(14)),exponential_polynomial_cases=polychecks,exponential_polynomial_coefficient_equalities=polycoeffchecks,convolutions_per_parent=scatters,endpoint_examples=records,source_sha256=source_sha,code_sha256=sha(Path(__file__)),seconds=time.monotonic()-t0,scope='Free smooth-function differential algebra reduced by the ODE, exact source binomial constants, complete symbolic exponent/monomial basis. Not differentiation of numerical Taylor remainders. Remaining source structures and actual physical models require separate checks.')
(D/'evidence/derivatives.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],checks,polychecks,out['seconds'])
