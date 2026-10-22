"""Independent sparse rational algebra for packet144; no numerics-lane code.
The proof precedes these finite controls. Sparse polynomial arithmetic uses
fractions.Fraction; only three generic parameter identities use SymPy.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time,datetime
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as S
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
checks=[]
def add(*terms):
 out={}
 for p in terms:
  for key,v in p.items():out[key]=out.get(key,F(0))+v
 return {key:v for key,v in out.items() if v}
def scale(p,a):return {k:v*a for k,v in p.items() if v*a}
def diff(p,j):
 out={}
 for k,v in p.items():
  if k[j]:
   new=list(k);new[j]-=1;out[tuple(new)]=v*k[j]
 return out
def shift(p,i,j):return {(k[0]+i,k[1]+j):v for k,v in p.items()}
def lap(p):return add(diff(diff(p,0),0),diff(diff(p,1),1))
def operator(beta,a):
 q=4*a/beta;lam1=(beta-2)/2;lam2=1+3*beta/2
 def adv(p):return add(scale(shift(diff(p,0),1,0),lam1),scale(shift(diff(p,1),0,1),lam2),scale(shift(diff(p,1),2,0),-q/2))
 def ls(p):
  ap=add(scale(adv(p),-1),scale(p,1-2*beta));z=lap(ap);dy=diff(p,1)
  return add(adv(z),scale(z,4*beta),scale(adv(dy),-q),scale(dy,-4*beta*q),scale(shift(diff(dy,0),1,0),-2*a))
 return ls

def rank_exact(rows):
 if not rows:return 0
 a=[list(row) for row in rows];m=len(a);n=len(a[0]);rank=0
 for col in range(n):
  pivot=next((i for i in range(rank,m) if a[i][col]),None)
  if pivot is None:continue
  a[rank],a[pivot]=a[pivot],a[rank];v=a[rank][col]
  a[rank]=[z/v for z in a[rank]]
  for i in range(rank+1,m):
   if a[i][col]:
    c=a[i][col];a[i]=[z-c*w for z,w in zip(a[i],a[rank])]
  rank+=1
  if rank==m:break
 return rank

def basis(k):return [(2*i+1,j) for i in range(k+1) for j in range(k+1-i)] if k>=0 else []
matrices=[]
for beta in [F(2),F(9,4),F(7,2)]:
 for a in [F(1),F(-1)]:
  ls=operator(beta,a);q=4*a/beta;c=3*(7*beta-8)*(9*beta-2)/(q*(17*beta-4))
  tests=[('x3',ls({(3,0):F(1)}),{(1,0):F(3,2)*(8-7*beta)*(9*beta-2)}),('xy',ls({(1,1):F(1)}),{(1,0):q*(17*beta-4)/2}),('p3',ls({(3,0):F(1),(1,1):c}),{}),('affine_x',ls({(1,0):F(1)}),{}),('affine_y',ls({(0,1):F(1)}),{})]
  for name,left,right in tests:checks.append({'name':f'{name}_beta{beta}_a{a}','pass':left==right})
  for k in range(9):
   src=basis(k);target=basis(k-1);cols=[ls({m:F(1)}) for m in src]
   lowering=all(set(p).issubset(target) for p in cols)
   matrix=[[p.get(m,F(0)) for p in cols] for m in target];rank=rank_exact(matrix);nullity=len(src)-rank
   matrices.append({'beta':str(beta),'a':str(a),'k':k,'domain_dimension':len(src),'target_dimension':len(target),'rank_exact':rank,'nullity':nullity,'claimed_lower_bound':k+1,'weighted_lowering':lowering,'pass':lowering and nullity>=k+1})
# Generic parameter identities separately from the sparse rational code.
x,y,b,a=S.symbols('x y beta a');q=4*a/b
adv=lambda p:(b-2)*x*S.diff(p,x)/2+((1+3*b/2)*y-q*x*x/2)*S.diff(p,y)
lapS=lambda p:S.diff(p,x,2)+S.diff(p,y,2)
ls=lambda p:adv(lapS(-adv(p)+(1-2*b)*p))+4*b*lapS(-adv(p)+(1-2*b)*p)-q*(adv(S.diff(p,y))+4*b*S.diff(p,y))-2*a*x*S.diff(p,x,y)
c=3*(7*b-8)*(9*b-2)/(q*(17*b-4))
for name,z in [('generic_x3',ls(x**3)-S.Rational(3,2)*(8-7*b)*(9*b-2)*x),('generic_xy',ls(x*y)-q*(17*b-4)*x/2),('generic_p3',ls(x**3+c*x*y))]:checks.append({'name':name,'pass':S.cancel(z)==0})
# Finite smoothness manufactured controls: C7 polynomial bumps, sufficient for
# these integrations; the analytical counterexample permits C-infinity bumps.
numeric=[]
for beta,a in [(2.,1.),(2.25,-1.),(3.5,1.)]:
 q=4*a/beta;c=3*(7*beta-8)*(9*beta-2)/(q*(17*beta-4))
 for n in [16,24,36]:
  nodes,w=leggauss(n);radius=.4;rr=radius*(nodes+1)/2;wr=radius*w/2;angles=2*np.pi*(np.arange(64)+.37)/64
  rad,ang=np.meshgrid(rr,angles,indexing='ij');weights=wr[:,None]*rad*(2*np.pi/64)
  affine=np.zeros(3);moment=0.;massx2=0.
  for sign in [1.,-1.]:
   xx=sign*1.2+rad*np.cos(ang);yy=.35+rad*np.sin(ang)
   rho=(1-rad**2/radius**2)**8;rho_y=-16*(yy-.35)/radius**2*(1-rad**2/radius**2)**7;f=xx*rho_y
   for i,p in enumerate([np.ones_like(xx),xx,yy]):affine[i]+=float(np.sum(weights*p*f))
   moment+=float(np.sum(weights*(xx**3+c*xx*yy)*f));massx2+=float(np.sum(weights*xx**2*rho))
  expected=-c*massx2;err=abs(moment-expected)
  numeric.append({'beta':beta,'a':a,'radial_order':n,'angles':64,'affine_moments':affine.tolist(),'p3_moment_direct':moment,'p3_moment_predicted':expected,'error':err,'pass':max(abs(affine))<2e-13 and err<2e-12 and abs(moment)>.01})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'algebraic_controls':checks,'exact_fraction_matrix_controls':matrices,'manufactured_counterexample_controls':numeric,'all_pass':all(z['pass'] for z in checks+matrices+numeric),'scope':'Finite exact instances and nonrigorous quadrature controls. All-k dimension bound is proved in PROOF.md. Observed ranks do not establish equality of the general kernel bound or a full cokernel.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_pass':result['all_pass'],'algebra_count':len(checks),'matrix_count':len(matrices),'counterexample_count':len(numeric),'elapsed_seconds':result['elapsed_seconds'],'max_counterexample_error':max(z['error'] for z in numeric)},indent=2))
if not result['all_pass']:raise SystemExit(1)
