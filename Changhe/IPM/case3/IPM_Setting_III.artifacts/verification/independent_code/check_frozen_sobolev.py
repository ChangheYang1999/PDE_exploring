"""Exact Gaussian moment tests of the frozen Sobolev integration by parts."""
from fractions import Fraction as F
from math import comb,prod
from pathlib import Path
from datetime import datetime,timezone
import json

def moment(i,j,a,b):
 return F(prod(range(1,2*i,2)),1)/(4*a)**i*F(prod(range(1,2*j,2)),1)/(4*b)**j

def integral(s,ix,iy,a,b):
 return sum(F(comb(s,k))*moment(k+ix,s-k+iy,a,b) for k in range(s+1))

checks=[]
for A,a0 in [(F(2),F(7,2)),(F(5),F(20)),(F(3,2),F(-4))]:
 for a,b in [(F(1,2),F(1)),(F(2),F(1,3))]:
  for s in (1,2,3,5):
   mass=integral(s,0,1,a,b)
   horizontal=integral(s-1,1,1,a,b)
   vertical=integral(s-1,0,2,a,b)
   # Direct differentiated transform of hhat = i*zeta*exp(-a*xi^2-b*zeta^2).
   direct=2*A*a*integral(s,1,1,a,b)+2*b*integral(s,0,2,a,b)-(A+3)*mass-a0*horizontal
   identity=s*(A*horizontal+vertical)-(A+3)/2*mass-a0*horizontal
   pointwise_omission=s*(A*horizontal+vertical)-(1+a0*horizontal/mass)*mass
   assert direct==identity and direct!=pointwise_omission
   checks.append({'A':str(A),'a0':str(a0),'gaussian_alpha':str(a),'gaussian_beta':str(b),'s':s,'direct_over_gaussian_base':str(direct),'identity_equal':True,'omitting_volume_factor_fails':True})
p=Path('research/frozen_sobolev/verification/exact_gaussian_moments.json')
p.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'method':'Exact Fraction Gaussian moments after direct Fourier differentiation; Gaussian base pi/(2*sqrt(alpha*beta)) cancels','checks':checks},indent=2)+'\n')
print(len(checks),'exact frozen Sobolev examples and negative controls passed')
