from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
x,r,beta,A=s.symbols('x r beta A',positive=True);f=s.Function('f');t=s.log(r/x);gam=7+beta;v=x**gam*f(t)
expected=x**(gam-2)*(gam*(gam-1)*f(t)-(2*gam-1)*s.Subs(s.Derivative(f(s.Symbol('t')),s.Symbol('t')),s.Symbol('t'),t)+s.Subs(s.Derivative(f(s.Symbol('t')),s.Symbol('t'),2),s.Symbol('t'),t))
# Derive with a separate formal coordinate rather than depend on Subs simplification.
u=s.symbols('u');P0=f(u);P1=gam*P0-s.diff(P0,u);P2=(gam-1)*P1-s.diff(P1,u)
r0=s.simplify(s.diff(v,x,2)-x**(gam-2)*P2.subs(u,t));assert r0==0
G=s.Function('G')(x);aa=s.Function('a')(x);Q=aa/G**3;F=-aa*s.diff(G,x)+s.diff(aa,x)*G/3;r1=s.simplify(F-G**4*s.diff(Q,x)/3);assert r1==0
k=(1-beta)*(6+beta)*(7+beta)/(6*A);r2=s.simplify(((beta-1)*A**(1-beta)/3)*(-A**(beta-2)/2)*gam*(gam-1)-k);assert r2==0
# Uniform cutoff derivatives: C_i control is independent of N because d/dt acts on two fixed translates.
# If chi(t)+chi(1-t)=1, each end integral is 1/2 exactly, so the normalized plateau integral is 1+1/N.
Ns=[3,10,30,100,300];rows=[{'N':N,'leading_log_integral_exact':str(1+s.Rational(1,N)),'critical_norm_prefactor_exact':str(s.Rational(1,N))} for N in Ns]
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'Exact identities supporting the informal proof. Does not numerically evaluate the nonlinear B functional.','second_derivative_residual':str(r0),'forcing_Q_residual':str(r1),'kappa_residual':str(r2),'kappa_A4_exact':str(k.subs({A:4,beta:s.Rational(1,2)})),'kappa_A10_150725':str(k.subs({A:s.Rational('10.150725'),beta:2/s.Rational('10.150725')}).evalf(25)),'leading_sequence':rows}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('EXACT_CRITICAL_NORM_IDENTITIES_PASS')
