"""Independent Laurent-polynomial audit of beta2 scattering identities."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,time
start=time.monotonic();z=s.symbols('z',nonzero=True);I=s.I
co=lambda n:(z**n+z**(-n))/2
si=lambda n:(z**n-z**(-n))/(2*I)
def D(f):return s.expand(I*z*s.diff(f,z))
def mean(f):return s.expand(f).coeff(z,0)
P=s.Rational(5,9)*co(1)-s.Rational(3,11)*si(2)+s.Rational(2,13)*co(5)+s.Rational(1,7)*si(6)
h=co(1)**2*(1+s.Rational(2,9)*si(1)+s.Rational(3,10)*si(1)**2)
a=s.expand(D(D(P))+s.Rational(9,4)*P)
b=s.expand(-s.Rational(3,2)*P*D(a)-s.Rational(1,2)*D(P)*a+si(1)*D(h))
b1=s.simplify(2*mean(b*co(1)))
Q=s.expand(sum(b.coeff(z,n)*z**n/(1-n*n) for n in range(-20,21) if abs(n)!=1))
B1=D(Q)*co(1)+(Q+b1*co(1)/2)*si(1)
B2=D(Q)*si(1)-(Q+b1*co(1)/2)*co(1)
U1=D(P)*co(1)+s.Rational(3,2)*P*si(1)
U2=D(P)*si(1)-s.Rational(3,2)*P*co(1)
checks={'resonance':s.simplify(mean(b*co(1))-mean(si(1)*(2*D(P)**2-s.Rational(3,2)*P**2))+mean(h*co(2))),
'first_sine_zero':s.simplify(mean(b*si(1))),
'nonresonant_poisson':s.simplify(D(D(Q))+Q-b+b1*co(1)),
'angular_B_horizontal_mean':s.simplify(mean(B1)),
'angular_B_vertical_mean':s.simplify(mean(B2)+b1/4),
'leading_horizontal_mean':s.simplify(mean(U1)),
'leading_vertical_mean':s.simplify(mean(U2)+2*mean(a*co(1)))}
assert all(v==0 for v in checks.values()),checks
out={'utc':datetime.now(timezone.utc).isoformat(),'method':'independent exact Laurent polynomial differentiation and constant-term integration','zeros':{k:str(v) for k,v in checks.items()},'b1_test_value':str(b1),'elapsed_seconds':time.monotonic()-start,'verdict':'PASSED'}
Path('research/54_beta2_scattering_identities/verification/algebra.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
