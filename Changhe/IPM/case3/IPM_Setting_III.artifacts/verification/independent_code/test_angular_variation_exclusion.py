"""Independent exact and MP checks for result80. No producer or lead code."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
import mpmath as mp

x,y,t,B,A,n=s.symbols('x y t B A n',real=True)
th=s.symbols('th',real=True)
w=s.cos(th)*s.sin(th)**3;k=s.sin(th)**2*(4*s.sin(th)**2-3)
checks=[]
def zero(name,z):
    v=s.trigsimp(s.factor(z));assert v==0,(name,v);checks.append(name)
zero('angular integration by parts',s.diff(w,th)+k)
zero('kernel mean',s.integrate(k,(th,0,s.pi/2)))
zero('kernel positive mass',s.integrate(k,(th,s.pi/3,s.pi/2))-3*s.sqrt(3)/16)
zero('radial boundary angular factor',s.integrate(s.cos(th)**2*s.sin(th)**2,(th,0,s.pi/2))-s.pi/16)
zero('epsilon angular factor',s.integrate(s.cos(th)**2*s.sin(th)**4,(th,0,s.pi/2))-s.pi/32)
zero('slope threshold value',s.Rational(1,4)-(A-1)/(4*A)-1/(4*A))
zero('degree threshold value',s.Rational(1,4)-(A-1)/(2*(n-1)*A)-((n-3)*A+2)/(4*(n-1)*A))
frac=1/((B**2-1)**2*(1+t**2))+1/((B**2-1)*(1+t**2)**2)-B**2/((B**2-1)**2*(1+B**2*t**2))
zero('Gaussian partial fractions',frac-t**2/((1+t**2)**2*(1+B**2*t**2)))
zero('Gaussian integrated rational function',s.pi/(2*(B**2-1)**2)+s.pi/(4*(B**2-1))-B*s.pi/(2*(B**2-1)**2)-s.pi/(4*(1+B)**2))

# At a=e_K only the highest coefficient survives. Verify all equations
# for many degrees and several rational A without parameter division.
recurrence_checks=0
for K in range(1,26):
 nn=2*K+1
 for AA in [s.Rational(3,2),s.Rational(2),s.Rational(9),s.Rational(37),s.Rational(101,3)]:
  aa=(nn-1)*AA;cc=[s.Integer(0)]*K+[s.Integer(1)]
  for j in range(K):
   ej=nn-1+2*j*(AA-1);ek=nn-1+2*(j+1)*(AA-1)
   assert (nn-2*j)*(nn-2*j-1)*ej*cc[j]+(2*j+2)*(2*j+1)*(ek-aa)*cc[j+1]==0
   recurrence_checks+=1

jets=[]
for label,ell,aa,H,phi in [
 ('cubic',s.Integer(2),s.Integer(13),x*x*y+s.Rational(7,6)*y**3,2*x**3*y+s.Rational(7,3)*x*y**3),
 ('quintic',s.Integer(19),s.Integer(2),x**4*y-s.Rational(73,19)*x*x*y**3+s.Rational(2701,380)*y**5,s.Rational(148,5)*x**5*y-s.Rational(292,3)*x**3*y**3+s.Rational(2701,95)*x*y**5)]:
 AA=2*ell-1;D=ell-1;V=s.diff(phi,x);v=(-s.diff(phi,y),V)
 zero(label+' leading transport',AA*x*s.diff(H,x)+y*s.diff(H,y)-H-V)
 zero(label+' Poisson',s.diff(phi,x,2)+s.diff(phi,y,2)-aa*s.diff(H,x))
 rho=aa*(y-H);psi=-D*x*y+phi
 W=(ell*x-s.diff(psi,y),ell*y+s.diff(psi,x))
 R=s.expand(W[0]*s.diff(rho,x)+W[1]*s.diff(rho,y)-rho)
 zero(label+' nonlinear residual identity',R+aa*(v[0]*s.diff(H,x)+v[1]*s.diff(H,y)))
 assert R!=0
 pol=s.Poly(R,x,y);deg=pol.total_degree();assert {sum(p) for p,c in pol.terms()}=={deg}
 jets.append(dict(name=label,degree=deg,residual=str(R),residual_at_1_1=str(R.subs({x:1,y:1}))))
 if label=='cubic':
  angular_op=-y*s.diff(1-H/y,x)+x*s.diff(1-H/y,y)
  zero('cubic angular derivative',angular_op+x*y/3)
 else:
  Hy=s.diff(H,y)
  zero('quintic diagonal vertical strain',s.diff(V,y).subs({x:t,y:t})+s.Rational(11131,19)*t**4)
  zero('quintic discriminant',s.Rational(219,19)**2-4*s.Rational(2701,76)+s.Rational(3358,361))
  zero('quintic squared gradient identity',(s.diff(rho,x)**2+s.diff(rho,y)**2)/aa**2-(1-2*Hy+s.diff(H,x)**2+Hy**2))

mp.mp.dps=70
rows=[]
for beta in [mp.mpf(1),mp.mpf(2),mp.mpf(9),mp.mpf(100),mp.mpf('10000')]:
 b=mp.sqrt(beta)
 angular=mp.quad(lambda z:mp.cos(z)**2*mp.sin(z)**2/(mp.cos(z)**2+beta*mp.sin(z)**2),[0,mp.pi/4,mp.pi/2])
 err=abs(angular-mp.pi/(4*(1+b)**2));assert err<mp.mpf('1e-62'),(beta,err)
 # Integrate the negative angular variation after exact positive radial integration.
 N=mp.quad(lambda z:(beta-1)*mp.cos(z)**2*mp.sin(z)**4/(mp.cos(z)**2+beta*mp.sin(z)**2),[0,mp.pi/4,mp.pi/2])
 target=mp.pi/4*(mp.mpf(1)/4-1/(1+b)**2)
 assert abs(N-target)<mp.mpf('1e-62'),(beta,N,target)
 rows.append(dict(test='gaussian',beta=str(beta),center_per_a=str(-4*angular/mp.pi),center_error=str(err),N=str(N),N_error=str(abs(N-target))))
for ell in [mp.mpf('1.001'),mp.mpf('1.1'),mp.mpf('2'),mp.mpf('5'),mp.mpf('19')]:
 AA=2*ell-1;D=ell-1;eps=1/(2*AA)
 J=mp.quad(lambda z:mp.exp(-z)/(1+z),[0,1,mp.inf])
 N=eps*mp.pi*J/32
 # A separate source-derivative expression, not the angular identity under test.
 c_per_a= -mp.mpf(1)/4+eps/8*mp.quad(lambda z:mp.exp(-z)*z*((1+z)**-1+(1+z)**-2),[0,1,mp.inf])
 aeps=D/(mp.mpf(1)/4-4*N/mp.pi)
 assert abs(c_per_a+mp.mpf(1)/4-4*N/mp.pi)<mp.mpf('1e-64')
 assert 0<N<mp.pi/(64*AA) and 0<aeps<2*AA
 defect=6*(1+eps)-(aeps-2*AA);assert defect>0
 rows.append(dict(test='q_epsilon',ell=str(ell),N=str(N),N_bound=str(mp.pi/(64*AA)),a=str(aeps),center_per_a=str(c_per_a),canonical_error=str(abs(aeps*c_per_a+D)),cubic_defect=str(defect)))

out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',exact_checks=checks,recurrence_checks=recurrence_checks,polynomial_nonprofiles=jets,mp_dps=mp.mp.dps,quadrature_rows=rows,scope='Independent algebra and high precision quadrature support the standalone conditional proof. They do not certify a profile or replace its global hypotheses.')
p=Path('research/angular_variation_exclusion/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(utc=out['utc'],status=out['status'],exact_checks=len(checks),recurrence_checks=recurrence_checks,quadrature_rows=len(rows)),indent=2))
