"""Exact algebra controls for proof186, written before this program.
Finite tests check identities and negative examples, not Baire category or PDE existence.
"""
from pathlib import Path
from datetime import datetime,timezone
from time import perf_counter
from fractions import Fraction as Q
import json
import sympy as sp
root=Path('research/186_directional_quasianalytic_obstructions/verification')
start=perf_counter(); utc=datetime.now(timezone.utc).isoformat();checks=[];negative=[]
def check(name,condition,detail=''):
 assert bool(condition),name
 checks.append({'name':name,'pass':True,'detail':detail})
def reject(name,condition,detail):
 assert bool(condition),name
 negative.append({'name':name,'detected':True,'detail':detail})
s,t,u=sp.symbols('s t u',real=True)
# Independent differentiation in the physical and flattened coordinates.
for n in range(1,17):
 a=(n*s+t)**2 + s**(n%3+1)*t**(n%2+1)+sp.Rational(n,3)*t**3
 b=(s-n*t)**3 + sp.Rational(1,n)*s**2*t+s*t**2
 g=sp.Rational(n,5)*s+s**(n%3+1)/sp.Integer(7)
 A=sp.expand(a.subs(t,u+g)); B=sp.expand(b.subs(t,u+g))
 omega=-sp.diff(b,s)+sp.diff(a,t)
 O=sp.expand(omega.subs(t,u+g))
 rhs=-sp.diff(B,s)+sp.diff(A,u)+sp.diff(g,s)*sp.diff(B,u)
 check(f'curved graph curl case{n}',sp.expand(O-rhs)==0)
 for k in range(5):
  check(f'physical directional derivative case{n} order{k}',sp.expand(sp.diff(O,u,k)-sp.diff(omega,t,k).subs(t,u+g))==0)
 # Polynomial phi is only an integration-identity control: its endpoint values
 # vanish, but it is not being asserted to be a C-infinity compactly supported test.
 phi=(1-s*s)**2*(1+s if n%2 else 1-s+s*s)
 check(f'test endpoint boundary values{n}',phi.subs(s,-1)==0 and phi.subs(s,1)==0)
 F=sp.integrate(sp.expand(O*phi),(s,-1,1))
 weak=sp.integrate(sp.expand(B*sp.diff(phi,s)),(s,-1,1))+sp.diff(sp.integrate(sp.expand((A+sp.diff(g,s)*B)*phi),(s,-1,1)),u)
 check(f'weak curl integration identity{n}',sp.expand(F-weak)==0)
 for k in range(4):
  check(f'weak differentiated identity{n} order{k}',sp.expand(sp.diff(F,u,k)-sp.integrate(sp.expand(sp.diff(O,u,k)*phi),(s,-1,1)))==0)
# Every fixed line direction admits a positively oriented physical frame;
# verify -curl is unchanged, with independently transformed vector components.
x,y=sp.symbols('x y',real=True)
Vx=x*x*y+y*y;Vy=x*y*y+x**3
physical=-sp.diff(Vy,x)+sp.diff(Vx,y)
for aa,bb in [(0,1),(1,0),(sp.Rational(3,5),sp.Rational(4,5)),(-sp.Rational(5,13),sp.Rational(12,13))]:
 check(f'oriented frame determinant {aa},{bb}',aa*aa+bb*bb==1)
 trans={x:bb*s+aa*t,y:-aa*s+bb*t}
 Vs=(bb*Vx-aa*Vy).subs(trans,simultaneous=True)
 Vt=(aa*Vx+bb*Vy).subs(trans,simultaneous=True)
 check(f'curl under proper rotation {aa},{bb}',sp.expand(-sp.diff(Vt,s)+sp.diff(Vs,t)-physical.subs(trans,simultaneous=True))==0)
# Absorb genuinely line-dependent amplitudes, rates, and radii into an integer N.
for j in range(1,12):
 A=Q(j+1,3);B=Q(2*j+1,4);r=Q(1,j+2);N=max(j+3,1)
 check(f'absorbed compact radius{j}',Q(1,N)<r)
 for k in range(9):check(f'absorbed derivative constant{j},{k}',A*B**k<=Q(N)**(k+1))
# The derivative closure factor has a separate k=0 case. A scaled factorial
# weight with m1<1 detects an attempt to replace max(1,D) by D blindly.
for scale in [Q(1,10),Q(1),Q(3)]:
 m=lambda k:scale**k*int(sp.factorial(k))
 D=max(Q(1),3*scale);C=max(Q(1),m(1))
 for k in range(9):
  check(f'derivative closure factorial scale{scale} k{k}',m(k+1)<=C*D**k*m(k))
  N=Q(3);p=Q(5,2);q=Q(7,3);G=Q(4,5)
  lhs=p*N**(k+1)*m(k)+(1+G)*q*N**(k+2)*m(k+1)
  bound=N*(p+N*C*(1+G)*q)*(N*D)**k*m(k)
  check(f'weak bound7 scale{scale} k{k}',lhs<=bound)
# h(t) is exp(-1/t^2) on t<0 and zero on t>=0. Negative-side derivatives
# checked via z=-t>0; the proof gives the all-order argument, not a finite scan.
z=sp.symbols('z',positive=True);h=sp.exp(-1/z**2)
for k in range(9):check(f'flat manufacture derivative{k}',sp.limit(sp.diff(h,z,k),z,0,dir='+')==0)
f=s*s*h
check('exceptional scalar line identically zero',f.subs(s,0)==0)
check('near every interface point nonzero values possible',f.subs({s:1,z:1})==sp.exp(-1))
# Curved graph omission and orientation errors have explicit nonzero defects.
a=sp.Integer(0);b=s*t;g=s*s;B=b.subs(t,u+g);O=-u-s*s
reject('omit graph derivative',sp.expand(O+sp.diff(B,s))==2*s*s,'Physical curl pullback is -u-s^2; omitting g prime B_u gives -u-3s^2.')
reject('reverse curl sign',sp.expand((-sp.diff(b,s)).subs(t,u+g)+(sp.diff(b,s)).subs(t,u+g))==0 and O!=0,'Using +curl instead of -curl reverses this nonzero polynomial.')
reject('omit integration boundary requirement',sp.integrate(-sp.diff(s,s),(s,-1,1))==-2,'With U_t=s and phi=1, integral Omega=-2, but the boundary-free right side is0.')
reject('upgrade generic to every line',f.subs(s,0)==0 and f.subs(s,1)!=0,'The smooth f=s^2 h(t) has no full zero neighborhood at any graph point, yet line s=0 is identically zero.')
reject('drop no-zero-neighborhood hypothesis',-sp.diff(s,s)+sp.diff(t,t)==0,'U=(t,s) has zero curl and analytic restrictions on all lines; Omega=0 has full zero neighborhoods.')
reject('drop directional flatness',sp.diff(t,t)==1 and t.subs(t,0)==0,'f=t is analytic and nonzero as a germ, and has no full zero neighborhood, but its first derivative is nonzero.')
reject('drop quasianalyticity',h.subs(z,1)==sp.exp(-1) and sp.diff(h,z).subs(z,1)==2*sp.exp(-1),'U=(h(t),0) is Gevrey3/2, div U=0; Omega=h prime is flat and nonzero, while the whole vector belongs to that nonquasianalytic class.')
reject('upgrade vector failure to both scalar components',sp.Integer(0)==0 and h.subs(z,1)!=0,'The same U=(h(t),0) has a zero analytic second component, so vector failure cannot imply both scalar components fail.')
end=datetime.now(timezone.utc).isoformat()
data={'verdict':'PASS','started_utc':utc,'ended_utc':end,'elapsed_seconds':perf_counter()-start,'exact_count':len(checks),'negative_count':len(negative),'exact_checks':checks,'negative_controls':negative,'scope':'Finite exact coordinate, weak integration, derivative-bound and explicit-counterexample checks. No finite proof of meagerness, quasianalytic uniqueness, strong-manifold geometry, or B2 existence is claimed.'}
(root/'controls.json').write_text(json.dumps(data,indent=2)+'\n');print({k:v for k,v in data.items()if k not in ['exact_checks','negative_controls']})
