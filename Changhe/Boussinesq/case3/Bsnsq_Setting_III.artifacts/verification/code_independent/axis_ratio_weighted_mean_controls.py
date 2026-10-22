"""Exact independent P259 identities and controls; no lead/NUM code."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/259_axis_ratio_weighted_mean/verification');tic=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks=[]
def eq(n,e):
 z=s.factor(s.cancel(s.expand(e)));checks.append({'name':n,'passed':z==0,'difference':str(z)})
def pos(n,e):
 n0,d0=s.fraction(s.cancel(e.subs(beta,2+z)));pn=s.Poly(n0,z);pd=s.Poly(d0,z);a=pn.all_coeffs();b=pd.all_coeffs();checks.append({'name':n,'passed':bool(all(t>=0 for t in a+b)and any(t>0 for t in a)and any(t>0 for t in b)),'positive_parameter':'z=beta-2','numerator':str(pn.as_expr()),'denominator':str(pd.as_expr())})
y=s.symbols('y',positive=True);beta=s.symbols('beta',positive=True);A,c2=s.symbols('A c2',real=True);z=s.symbols('z',positive=True)
d=(3*beta+2)/2;h=(beta+6)/2;gamma=s.Rational(1,2)+1/beta;k0=1+h/d;eps=(beta-2)/(128*beta*(1+beta))
b=s.Function('b')(y);R=s.Function('R')(y);rho=s.Function('rho')(y);I=s.Function('I')(y);J=s.Function('J')(y);v=s.Function('v')(y);eta=s.Function('eta')(y);M=s.Function('M')(y);N=s.Function('N')(y)
eq('3d_minus_h',3*d-h-4*beta)
eq('M_log_derivative',(4*(d-s.diff(b,y))-k0*d)/b-4*(beta-s.diff(b,y))/b)
eq('M_central_power',4*gamma-k0*(gamma+1))
eq('N_central_power',gamma-k0*(gamma+1)+1+h/beta)
eq('positive_mean_growth_power',2-2*gamma-(1-2/beta))
eq('R_positive_power',1-h/d-(beta-2)/d)
for name,expr in [('eps_positive',eps),('mu_integrable',1/beta-2*eps),('Meta_integrable',1/beta-(6+k0)*eps),('N_integrable',h/beta-(1+k0)*eps),('contradiction_power_positive',1-2/beta-2*eps)]:pos(name,expr)
# Differentiate the scaled J directly; remove J' and use exact algebraic v.
JJ=s.diff(J*R**(-h/d),y).subs({s.diff(J,y):rho*I,s.diff(R,y):rho})
vsub=(c2+A/8*(d*R*I-h*J))/rho**3
expr=JJ-8/(A*d)*rho*R**(-1-h/d)*(rho**3*vsub-c2)
eq('J_scaled_identity',s.powsimp(expr,force=False))
# This elementary product rule remains true even for arbitrarily large b''.
prod=s.diff(M*(s.diff(b,y)-beta),y).subs(s.diff(M,y),4*M*(beta-s.diff(b,y))/b)
eq('weighted_square_identity',prod-M*s.diff(b,y,2)+4*M*(s.diff(b,y)-beta)**2/b)
first=-M*s.diff(b,y,2)-M*eta-2*c2*N
energy=first+prod
eq('S_energy_identity',energy+4*M*(s.diff(b,y)-beta)**2/b+M*eta+2*c2*N)
eq('positive_mean_division_power',s.powsimp(R**(1-h/d)/(rho**4*R**(-1-h/d))-R**2/rho**4,force=False))
eq('positive_mean_b_form',(R**2/rho**4-b**2/(d**2*rho**2)).subs(b,d*R/rho))
# Exact integrating factor in terms of R, a useful independent check of the estimates.
a=beta/(2*d)
eq('mu_R_log_derivative',a*rho/R-beta/(2*b).subs(b,d*R/rho))
eq('mu_R_growth_power',a*(gamma+1)-s.Rational(1,2))
eq('mu_source_integrability_power',(a-1)*(gamma+1)+1+1/beta)
# Reflection test uses independent polynomial rho,I, and their integrated products.
u=s.symbols('u',real=True);rm=1+u**2;im=1-2*u+3*u**2;Rm=s.integrate(rm,(u,0,y));Jm=s.integrate(rm*im,(u,0,y));rnew=rm.subs(u,-u);inew=-im.subs(u,-u);Rn=s.integrate(rnew,(u,0,y));Jn=s.integrate(rnew*inew,(u,0,y))
eq('reflection_R',Rn+Rm.subs(y,-y));eq('reflection_J',Jn-Jm.subs(y,-y));eq('reflection_signed_mean',-A*Jn/Rn-A*Jm.subs(y,-y)/Rm.subs(y,-y));eq('reflection_signed_ratio',-A*inew-A*im.subs(u,-u))
# Independent rational b,M pairs, including oscillatory curvature represented by a polynomial.
# Set b to a positive monomial: the M ODE then integrates exactly.
for bv in[s.Rational(5,2),s.Integer(3),s.Integer(6)]:
 for coeff in[s.Rational(1,2),s.Integer(1),s.Integer(2)]:
  bm=coeff*y;Mm=y**(4*(bv-coeff)/coeff);test=s.diff(Mm*(s.diff(bm,y)-bv),y)-Mm*s.diff(bm,y,2)+4*Mm*(s.diff(bm,y)-bv)**2/bm
  eq(f'manufactured_energy_beta{bv}_bcoef{coeff}',s.powsimp(test,force=False))
# An explicitly oscillatory smooth b with b/y->beta can have unbounded b'.
# This is a kinematic control only, not an axis-system solution with prescribed I.
bm=3*y+s.sin(y**3)/y
expr=(s.diff(bm,y)-3)-(3*y*s.cos(y**3)-s.sin(y**3)/y**2)
eq('wild_derivative_control',expr)
# Curvature energy is nonnegative on a positive b without estimating b'.
P,B=s.symbols('P B',positive=True);D=s.symbols('D',real=True)
eq('square_nonnegative_form',4*P*D**2/B-(2*s.sqrt(P/B)*D)**2)
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tic,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Exact identities, rational inequalities, reflection and kinematic controls. The analytic contradiction and integrability arguments are supplied in PROOF.md; no global B2 manufacture is claimed.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print([c for c in checks if not c['passed']])
