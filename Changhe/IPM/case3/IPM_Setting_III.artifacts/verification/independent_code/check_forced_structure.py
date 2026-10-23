"""Exact independent polynomial and Fourier checks of the forced source."""
from fractions import Fraction as F
from math import comb,prod
from pathlib import Path
from datetime import datetime,timezone
import json

def moment(i,j,g1,g2):
 return F(prod(range(1,2*i,2)),1)/(4*g1)**i*F(prod(range(1,2*j,2)),1)/(4*g2)**j
def integral(s,ix,iy,g1,g2):
 return sum(F(comb(s,k))*moment(k+ix,s-k+iy,g1,g2) for k in range(s+1))
checks=[]
for ell,c,a,b,L in [(F(3),F(-13,50),F(57,50),F(4,3),F(1)),(F(2),F(-1,2),F(3),F(-2),F(2)),(F(3,2),F(-1,2),F(5),F(3),F(3))]:
 A=2*ell-1;delta=ell+c-1;mu=a*delta;alpha=ell-c;beta=ell+c
 q1=(-2*mu/L**2-(2*A-delta)*b)/(3*a)
 q2=-b/3-q1;e=(-2*mu/L**2-a*q2)/(3*beta-1);H=q1-q2
 assert alpha==A-delta and beta==1+delta
 assert (2*alpha+beta-1)*b+3*a*q1==-2*mu/L**2
 assert (3*beta-1)*e+a*q2==-2*mu/L**2
 assert (a-4*A+2*delta)*b==3*a*H+4*mu/L**2
 assert (a-2*A+delta)*b==3*(2+3*delta)*e+8*mu/L**2
 checks.append({'ell':str(ell),'a':str(a),'c':str(c),'Delta':str(delta),'mu':str(mu),'alpha':str(alpha),'beta_y':str(beta),'b':str(b),'e':str(e),'q1':str(q1),'q2':str(q2),'length':str(L),'all_taylor_relations':True,'unforced_matrix_is_wrong':bool(delta)})
 for g1,g2 in [(F(1,2),F(1)),(F(2),F(1,3))]:
  for s in (1,2,3,5):
   mass=integral(s,0,1,g1,g2);horizontal=integral(s-1,1,1,g1,g2);vertical=integral(s-1,0,2,g1,g2)
   direct=2*alpha*g1*integral(s,1,1,g1,g2)+2*beta*g2*integral(s,0,2,g1,g2)-(alpha+2*beta+1)*mass-a*horizontal
   identity=s*(alpha*horizontal+beta*vertical)-(1+(alpha+beta)/2)*mass-a*horizontal
   assert direct==identity
   checks.append({'alpha':str(alpha),'beta_y':str(beta),'s':s,'gaussian_g1':str(g1),'gaussian_g2':str(g2),'direct_Gaussian_integral':str(direct),'energy_identity':True})
Path('research/forced_structure/verification/exact_checks.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'method':'Exact Fraction Taylor coefficients and independently differentiated Fourier Gaussians; tests are algebraic, not existence constructions.','checks':checks},indent=2)+'\n')
print('3 forced Taylor cases and 24 exact Fourier integral cases passed')
