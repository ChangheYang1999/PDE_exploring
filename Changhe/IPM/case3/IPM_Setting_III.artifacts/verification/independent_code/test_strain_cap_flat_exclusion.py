"""Independent symbolic and manufactured checks of the positive moments.

The analytic proof was written first. This does not use the reviewed checker.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json
import sympy as sp
import mpmath as mp

out=Path('research/strain_cap_flat_exclusion/verification');out.mkdir(parents=True,exist_ok=True)
x,y,m,ell=sp.symbols('x y m ell',real=True);s=x*x+y*y
w0=y*s**(1-m);w=y*s**(-m)
identities=[]
for name,expr in [
 ('laplacian_weight',sp.diff(w0,x,2)+sp.diff(w0,y,2)-4*(m-1)*(m-2)*w),
 ('horizontal_weight',sp.diff(w0,x,2)-2*(m-1)*w*(2*m*x*x/s-1))]:
 assert sp.simplify(expr)==0,name;identities.append(name)
# A separately chosen divergence-free polynomial velocity and scalar check the
# full transport integration by parts, including the sign of each drift term.
psi=x*y*(1+2*x*x-3*y*y+x*x*y*y);U=sp.Matrix([-sp.diff(psi,y),sp.diff(psi,x)])
W=sp.Matrix([ell*x+U[0],ell*y+U[1]]);H=y*(2+x*x+3*y*y+x**4)
V=(W.dot(sp.Matrix([sp.diff(H,x),sp.diff(H,y)]))-H)
fluxdiv=sp.diff(H*w*W[0],x)+sp.diff(H*w*W[1],y)
coefficient=2*m*(x*W[0]+y*W[1])/s-2*ell-W[1]/y-1
assert sp.simplify(sp.expand((V*w-fluxdiv-H*w*coefficient)/w))==0
identities.append('transport_density_with_boundary_divergence')
# Independent Cartesian differentiation of a nonradial potential.
f=sp.Function('f');a,eps=sp.symbols('a eps',real=True);K=y*(1+eps*x*x)*f(s)
HH=sp.diff(K,x,2)+sp.diff(K,y,2);VV=a*sp.diff(K,x,2)
assert sp.simplify(sp.diff(VV,x,2)+sp.diff(VV,y,2)-a*sp.diff(HH,x,2))==0
identities.append('nonradial_manufactured_Poisson')
# Rational explicit m choices, with both signs and wide parameter scales.
rational=[]
for l in [F(1001,1000),F(6,5),F(3,2),F(2),F(19),F(1000)]:
 for ab in [F(1,10**6),F(1,10),F(1),F(5),F(100),F(10**6)]:
  for sign in [-1,1]:
   q=3+2*l+(2*ab if sign>0 else ab)
   lower=2*q-4*l;upper=ab*(2*q-1)/(2*(q-2)) if sign>0 else ab/(2*(q-2))
   assert lower>upper
   rational.append(dict(ell=str(l),a=str(sign*ab),m=str(q),gap=str(lower-upper)))
# Smooth flat nonradial potentials K=y(1+eps*x^2)exp(-r^2-r^-2).
# H=Delta K, V=a K_xx satisfy the elliptic equation exactly. H need not
# have the profile sign, so this validates the moment identity only.
mp.mp.dps=65
rows=[]
for mm,ee,aa in [(mp.mpf('2.25'),mp.mpf('0.3'),mp.mpf('1.7')),
                 (mp.mpf('3'),mp.mpf('-0.2'),mp.mpf('-2')),
                 (mp.mpf('4.75'),mp.mpf('0.7'),mp.mpf('0.25')),
                 (mp.mpf('9'),mp.mpf('0.1'),mp.mpf('3'))]:
 def values(z):
  ss=mp.exp(2*z);ff=mp.exp(-ss-1/ss);fp=ff*(-1+1/ss**2);fpp=ff*((-1+1/ss**2)**2-2/ss**3)
  base=8*fp+4*ss*fpp
  ii=base+ee*(2*ff+4*ss*fp+ss**2*fpp)
  jj=aa*(2*fp+ss*fpp+ee*(2*ff+mp.mpf('2.5')*ss*fp+ss**2*fpp/2))
  tt=base/4+ee*(ff/2+2*ss*fp+ss**2*fpp/2)
  fac=mp.pi*mp.exp((4-2*mm)*z)
  return fac*ii,fac*jj,fac*tt
 previous=None
 for steps in [16,32]:
  cut=[-4+mp.mpf(8)*j/steps for j in range(steps+1)]
  I,J,T=[mp.quad(lambda z:values(z)[k],cut) for k in range(3)]
  rhs=aa*(2*mm*T-I)/(2*(mm-2))
  relative=abs(J-rhs)/(1+abs(J)+abs(rhs))
  assert relative<mp.mpf('1e-55'),(mm,relative)
  change=None if previous is None else max(abs(v-old)/(1+abs(v)) for v,old in zip((I,J,T),previous))
  if change is not None:assert change<mp.mpf('1e-55'),(mm,change)
  rows.append(dict(m=str(mm),epsilon=str(ee),a=str(aa),segments=steps,I=str(I),J=str(J),moment_rhs=str(rhs),
                   relative_identity_error=float(relative),refinement_change=None if change is None else float(change)))
  previous=(I,J,T)
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',exact_identities=identities,
            rational_contradictions=rational,manufactured_moments=rows,
            scope='Independent algebra and finite-annulus MP65 diagnostics on flat nonradial manufactured potentials. Full proof, positivity and tail limits are analytic, not numerical certificates. Extra global strain cap remains a hypothesis.')
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
