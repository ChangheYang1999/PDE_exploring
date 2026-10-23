#!/usr/bin/env python3
"""Supporting exact algebra for result162; the limiting proof is separate."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from math import comb,factorial
import hashlib,json,resource,time
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
t0=time.monotonic();out=Path('research/small_power_limit/verification');counts={}
assert (out/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
def ck(b,name):
 counts[name]=counts.get(name,0)+1
 if not b:raise AssertionError(name)
for row in json.loads((out/'manifest.json').read_text())['files']:
 ck(hashlib.sha256(Path(row['frozen']).read_bytes()).hexdigest()==row['sha256'],'frozen_input_hash')
rows=[]
for ell in (F(11,10),F(3,2),F(5,2),F(3),F(5),F(9)):
 p=1/ell;delta=1-p
 for eta in (F(1,10),F(1,2),F(9,10)):
  lam=p+eta*delta
  for beta in (F(1,1000),F(1,10),F(1),F(7,3)):
   alpha=-2-lam*beta
   ck(-2-beta<alpha<-2-p*beta,'power_strip')
   ck(alpha+beta+1==-1+beta*(1-lam)>-1,'origin_radial_exponent')
   ck(alpha+p*beta+1==-1-beta*(lam-p)<-1,'infinity_mass_exponent')
   ck(alpha+(beta+1)*p<-1,'infinity_velocity_integrability')
   ck(((2+alpha)*ell+beta)/(-alpha)==beta*(1-ell*lam)/(2+lam*beta),'exact_transport_prefactor')
   ck(1+beta*(1-lam)>-1 and -1-delta-beta*(lam-p)<-1,'dominated_remainder_exponents')
  for z_over_pi in (F(0),F(1,5),F(1),F(199,100)):
   # All quantities divided by pi; these are formal zero-set measures, not actual profiles.
   mass=2/(1-lam)+(2-z_over_pi)/(lam-p)
   predicted=(1-ell*lam)*mass/2
   ck(predicted==-(ell-1)/(1-lam)+ell*z_over_pi/2,'mass_to_velocity_limit')
   for k in (1-ell,F(-1,7),F(3,5)):
    direct=k/(1-lam)+ell*z_over_pi/2
    ck(direct-predicted==(k+ell-1)/(1-lam),'zero_set_correction_cancels')
   if eta==F(1,2):rows.append(dict(ell=str(ell),lambda_value=str(lam),z_over_pi=str(z_over_pi),mass_limit_over_pi=str(mass),velocity_limit_over_pi=str(predicted)))
 for r in (F(2),F(5),F(13)):
  for ur in (F(-1,3),F(0),F(3,4)):
   ck(ell*r+ur>0,'outward_manufactured_radial_speed')
   ck(1/(ell*r+ur)-p/r==-p*ur/(r*(ell*r+ur)),'scattering_multiplier_coefficient')
# Independent angular averages of homogeneous Cartesian harmonic velocities.
def clean(a):return {k:v for k,v in a.items() if v}
def add(*args):
 d={}
 for a in args:
  for k,v in a.items():d[k]=d.get(k,F())+v
 return clean(d)
def scale(a,c):return clean({k:v*c for k,v in a.items()})
def der(a,j):
 d={}
 for ij,v in a.items():
  if ij[j]:kk=list(ij);kk[j]-=1;d[tuple(kk)]=v*ij[j]
 return clean(d)
def mul(a,b):
 d={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():d[i+k,j+l]=d.get((i+k,j+l),F())+v*w
 return clean(d)
def avg(a):
 # Integral on unit circle divided by pi, computed through Cartesian beta integrals.
 return sum(v*F(2*factorial(i)*factorial(j),4**((i+j)//2)*factorial(i//2)*factorial(j//2)*factorial((i+j)//2)) for (i,j),v in a.items() if i%2==j%2==0)
def val(a,x,y):return sum(v*x**i*y**j for (i,j),v in a.items())
X={(1,0):F(1)};Y={(0,1):F(1)}
for trial in range(1,7):
 k=F(trial-4,trial+2);psi={(1,1):k,(3,1):F(trial,7),(1,3):F(-trial,11)}
 ux=scale(der(psi,1),-1);uy=der(psi,0);dot=add(mul(ux,X),mul(uy,Y))
 ck(add(der(ux,0),der(uy,1))=={},'Cartesian_divergence_zero')
 ck(avg(dot)==0,'circular_flux_cancellation')
 quad={ij:v for ij,v in dot.items() if sum(ij)==2}
 ck(quad==clean({(2,0):-k,(0,2):k}),'center_quadrupole_sign')
 for n in range(1,9):
  weight={(0,2*n):F(1)}
  direct=avg(mul(quad,weight));S=F(2*comb(2*n,n),4**n)
  ck(direct==k*F(n,n+1)*S,'weighted_quadrupole_angular_integral')
 rho={(0,1):F(2),(2,1):F(-1,3),(0,3):F(1,5)};rx=der(rho,0);ry=der(rho,1)
 for ell in (F(3,2),F(5,2)):
  wx=add(scale(X,ell),ux);wy=add(scale(Y,ell),uy)
  for x,y in ((F(2,3),F(3,4)),(F(-1,2),F(2,5))):
   rr=x*x+y*y;v=val(rho,x,y);wr=x*val(wx,x,y)+y*val(wy,x,y);ad=val(wx,x,y)*val(rx,x,y)+val(wy,x,y)*val(ry,x,y);E=ad-v
   for eps in (F(1,10),F(2,3)):
    # Exact coefficient of exp(-rho^2/eps^2) in the differentiated flux.
    lhs=2*ell/rr-2*wr/rr**2-2*v*ad/(eps*eps*rr)
    rhs=-2*val(dot,x,y)/rr**2-2*v*(v+E)/(eps*eps*rr)
    ck(lhs==rhs,'regularized_zero_set_flux_with_residual_retained')
res=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=sum(counts.values()),counts=counts,elapsed_seconds=time.monotonic()-t0,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sample_exact_limits=rows,scope='Finite algebra and local polynomial manufactures only. No numerical or formal certification of improper integrals; no actual profiles or positive-measure zero traces constructed.')
(out/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='sample_exact_limits'},indent=2))
