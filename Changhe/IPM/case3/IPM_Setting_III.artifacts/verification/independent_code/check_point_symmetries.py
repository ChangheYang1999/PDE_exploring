"""Exact jet substitutions for finite symmetries, independent of prolongation code."""
from fractions import Fraction as F
from datetime import datetime,timezone
from pathlib import Path
import json
checks=[]
for ell in [F(3,2),F(2),F(11,3)]:
 for alpha,beta in [(F(2),F(2)),(F(2),F(-2)),(F(-2),F(2)),(F(-2),F(-2)),(F(1,3),F(1,3))]:
  x,y,u=F(2,5),F(-3,7),F(5,11);p,q=F(7,3),F(-2,9);a,b=F(4,7),F(-5,8);vxx,vyy=F(11,13),F(-7,17);d1,d2=F(2,3),F(-4,5)
  before=(ell*x-b)*p+(ell*y+a)*q-u
  E=vxx+vyy+p
  z1,z2=alpha*x+d1,beta*y+d2
  up=beta*u;ux=beta/alpha*p;uy=q
  vx=beta*a-ell*d2;vy=alpha*b+ell*d1
  vxxp=beta/alpha*vxx;vyyp=alpha/beta*vyy
  after=(ell*z1-vy)*ux+(ell*z2+vx)*uy-up
  Ep=vxxp+vyyp+ux
  assert after==beta*before and Ep==beta/alpha*E
  wrong=(ell*z1-alpha*b)*ux+(ell*z2+beta*a)*uy-up
  assert wrong!=beta*before
  checks.append({'ell':str(ell),'alpha':str(alpha),'beta':str(beta),'transport_covariance':True,'poisson_covariance':True,'omitting_translation_compensation_fails':True})
p=Path('research/point_symmetries/verification/exact_jet_substitutions.json')
p.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'method':'Exact Fraction finite-transformation substitution on arbitrary off-equation jets; necessity is the separate written proof','checks':checks},indent=2)+'\n')
print(len(checks),'exact finite-point jet substitutions passed')
