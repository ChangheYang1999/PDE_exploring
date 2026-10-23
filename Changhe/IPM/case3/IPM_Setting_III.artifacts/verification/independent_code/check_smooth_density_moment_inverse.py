"""Independent manufactured comparisons for the density-moment inverse."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb
import argparse,hashlib,json,time
import numpy as np
import mpmath as mp
from smooth_basis import SmoothBasis
from smooth_density_moment_inverse import DensityMomentInverse as BaseInverse,power_rule
ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['quick','full'],default='quick');ap.add_argument('--composite',action='store_true');args=ap.parse_args()
def DensityMomentInverse(basis,order):
 return BaseInverse(basis,order,composite=args.composite)
prefix='COMPOSITE_'if args.composite else ''
start=time.monotonic();checks=[]
root=Path('research/smooth_density_moment_inverse/verification');root.mkdir(parents=True,exist_ok=True)
def record(name,error,tolerance,**data):
 row=dict(test=name,error=float(error),tolerance=float(tolerance),**data)
 if not error<=tolerance:
  (root/(prefix+args.phase+'_FAIL.json')).write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),status='FAIL',row=row,previous_checks=checks),indent=2)+'\n')
  raise AssertionError(row)
 checks.append(row)
def cheb_poly(n):
 a=[F(1)];b=[F(0),F(1)]
 if n==0:return a
 for _ in range(1,n):
  c=[F(0)]+[2*v for v in b]
  for k,v in enumerate(a):c[k]-=v
  a,b=b,c
 return b
def exact_I(n,b,w):
 out=F(0)
 for d,co in enumerate(cheb_poly(n)):
  for k in range(d+1):out+=co*comb(d,k)*(-2*w)**k/(b+k+1)
 return out
from numpy.polynomial.chebyshev import chebvander
for b in [F(0),F(3,2),F(11,3),F(100)]:
 nodes,weights=power_rule(12,float(b))
 for w in [F(1,7),F(3,4),F(1)]:
  values=weights@chebvander(1.-2.*float(w)*nodes,10)
  for n,value in enumerate(values):record('finite polynomial upper moment',abs(value-float(exact_I(n,b,w))),2e-13,degree=n,b=str(b),w=str(w))
mp.mp.dps=70
for p in [F(1,3),F(2,5),F(9,10)]:
 b=SmoothBasis(0,1,float(p),1.25);inv=DensityMomentInverse(b,192)
 for qs in ['1e-7','.1','.9','1','3','20','1000','1e40']:
  q=mp.mpf(qs);alpha=(1-mp.mpf(p.numerator)/p.denominator)/2
  if q<mp.mpf('1e-4'):
   exact=mp.hyp2f1(alpha,2,3,-q*q)/4
  else:
   exact=(((1+q*q)**(2-alpha)-1)/(2-alpha)-((1+q*q)**(1-alpha)-1)/(1-alpha))/(2*q**4)
  got=inv.lower(2,0,float(q)*b.L)[0]
  error=abs(got-float(exact))/max(abs(float(exact)),1e-300)
  record('radial closed lower primitive',error,2e-10,p=str(p),q=qs)
# A basis change of length is the physical dilation, preserving U/r.
for q in [.013,.3,2.,30.]:
 a=SmoothBasis(5,4,.4,.7);b=SmoothBasis(5,4,.4,2.3)
 ai=DensityMomentInverse(a,128);bi=DensityMomentInverse(b,128)
 av=ai.modal_rows(q*a.L);bv=bi.modal_rows(q*b.L)
 record('canonical modal dilation',max(np.max(abs(x-y))for x,y in zip(av,bv)),2e-14,q=q)
if args.phase=='full':
 from smooth_mp_primitives import SmoothMP
 from kernel_basis import KernelBasis
 from direct_inverse import Quadrature
 def enc(f):
  f=F(f);return dict(numerator=str(f.numerator),denominator=str(f.denominator))
 coeff=[[F((-1)**(k+j)*(k+2*j+1),(k+2)*(j+3))for j in range(7)]for k in range(5)]
 data=dict(alpha=enc(F(3,10)),length=enc(F(5,4)),cl=enc(F(5,2)),chebyshev_coefficients=[[enc(v)for v in row]for row in coeff])
 model=SmoothMP(data,65);b=SmoothBasis(6,5,.4,1.25);co=np.array([[float(v)for v in row]for row in coeff]).reshape(-1)
 rows=[]
 for rs in ['1e-8','.025','.4','1.25','3','11','1000','1e20']:
  r=float(rs);theta=.37
  with mp.workdps(model.working_digits):
   th=mp.mpf(str(theta));rr=mp.mpf(rs)
   reference=model.stream_velocity(rr*mp.cos(th),rr*mp.sin(th))
  ref=np.array([float(reference[0])/(r*r),float(reference[1])/r,float(reference[2])/r])
  previous=None
  for order in [64,128,256]:
   inv=DensityMomentInverse(b,order)
   out=inv.stream_velocity_at_radius(r,[theta]);got=np.array([out[0][0]@co/(r*r),out[1][0]@co/r,out[2][0]@co/r])
   err=np.max(abs(got-ref))/max(np.max(abs(ref)),1e-30)
   rows.append(dict(radius=rs,order=order,relative_error=float(err),change=None if previous is None else float(np.max(abs(got-previous)))))
   previous=got
   if order==256:record('nonradial separate source primitive',err,2e-8,radius=rs)
 # Separately implemented Cartesian integral, no radial mode differentiation.
 q=Quadrature(40,256,144,4.,b.L,b.p,16*b.L,1/(1-b.p));cart=KernelBasis(b,q)
 inv=DensityMomentInverse(b,256)
 for x,y in [(.3,.7),(1.5,.4),(2.,3.),(11.,7.)]:
  got=inv.velocity_matrix(x,y)@co;ref=cart.velocity_matrix(x,y)@co
  record('independent Cartesian singular integral',np.max(abs(got-ref))/max(1.,np.max(abs(ref))),2e-8,x=x,y=y)
 # Center strain and exact parity zeros with a fresh non-constrained vector.
 c=float(model.c)
 for r in [1e-4,1e-5]:
  got=(inv.velocity_matrix(0.,r)@co)[1]/r
  record('canonical strain from velocity limit',abs(got-c),1e-5,radius=r,strain_reference=c)
 for x,y in [(0.,1.),(1.,0.),(0.,0.)]:
  got=inv.velocity_matrix(x,y)@co
  record('exact symmetry velocity zeros',max(abs(got[0])if x==0 else 0.,abs(got[1])if y==0 else 0.),0.,x=x,y=y)
 (root/(prefix+'FULL_CONVERGENCE.json')).write_text(json.dumps(rows,indent=2)+'\n')
result=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='PASS',phase=args.phase,composite=args.composite,count=len(checks),checks=checks,
 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inverse_sha256=hashlib.sha256(Path('independent_code/smooth_density_moment_inverse.py').read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((root.parent/'PROOF.md').read_bytes()).hexdigest(),scope='Manufactured empirical comparisons; no interval quadrature error bound and no profile claim.')
(root/(prefix+args.phase.upper()+'_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['utc','elapsed_seconds','status','phase','count']}))
