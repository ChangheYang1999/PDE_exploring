"""Independent identities and discriminating manufactured tests for result76."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
import mpmath as mp
x,y,m,e,A=s.symbols('x y m e A',real=True)
r2=x*x+y*y;f=y*r2**(1-m)
checks={
 'elliptic_laplacian':s.diff(f,x,2)+s.diff(f,y,2)-4*(m-1)*(m-2)*y*r2**(-m),
 'elliptic_xx':s.diff(f,x,2)-2*(m-1)*y*r2**(-m)*(2*m*x*x/r2-1),
}
# Manufactured divergence-constant source flow. It satisfies the transport
# equation for y*q(y), but no canonical IPM elliptic relation is claimed.
g=e*y*y/(1+y*y);wx=x*(A-g-y*s.diff(g,y));wy=y*(1+g)
logq=-e*s.log(1+(1+e)*y*y)/(2*(1+e))
checks['manufactured_divergence']=s.diff(wx,x)+s.diff(wy,y)-A-1
checks['manufactured_transport']=wy*(1/y+s.diff(logq,y))-1
checks['trajectory_primitive']=s.diff(-logq,y)-g/wy
for name,expr in checks.items():
 assert s.simplify(s.factor(expr))==0,name
mp.mp.dps=65
orbit=[]
for eps in [mp.mpf('0.2'),mp.mpf('-0.2')]:
 for Y in [mp.mpf('.01'),mp.mpf('1'),mp.mpf('10')]:
  integral=mp.quad(lambda z:eps*z/(1+(1+eps)*z*z),[0,Y])
  q=(1+(1+eps)*Y*Y)**(-eps/(2*(1+eps)))
  err=abs(mp.exp(-integral)-q);assert err<mp.mpf('1e-60')
  assert (q<1) if eps>0 else (q>1)
  orbit.append(dict(epsilon=str(eps),y=str(Y),integral=mp.nstr(integral,40),q=mp.nstr(q,40),error=mp.nstr(err,8)))
# H=y exp(-1/r^2)*(1-r^2)/(1+r^2) has a positive flat inner
# defect and a negative outer tail. It is not a profile. Substitution u=1/r^2
# turns the moments into gamma-weighted integrals, avoiding a reused r-grid.
concentration=[];previous=mp.inf
for mm in [6,10,20,40,80]:
 density=lambda u:u**(mm-3)*mp.exp(-u)/mp.gamma(mm-2)
 signed=lambda u:density(u)*(u-1)/(u+1)
 inner=mp.quad(signed,[4,max(5,mm-3),mp.inf])
 outer=mp.quad(lambda u:abs(signed(u)),[0,1,4])
 full=mp.quad(signed,[0,1,4,max(5,mm-3),mp.inf])
 ratio=outer/inner
 assert inner>0 and full>0 and ratio<previous
 assert abs(full-inner)<=outer*(1+mp.mpf('1e-50'))+mp.mpf('1e-60')
 previous=ratio
 concentration.append(dict(m=mm,inner=mp.nstr(inner,40),signed_total=mp.nstr(full,40),outer_absolute=mp.nstr(outer,40),m_outer_over_inner=mp.nstr(mm*ratio,40)))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',exact_identities=list(checks),manufactured_orbits=orbit,signed_tail_concentration=concentration,
 scope='Exact cutoff multiplier and manufactured divergence/transport identities;65-digit orbit quadrature and flat sign-changing moment concentration. Manufactured fields are not asserted to satisfy both IPM equations. The continuum theorem is proved in PROOF.md.')
p=Path('research/local_flat_sign_and_trajectories/verification/checks.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
