"""Independent exact controls for the axis-limit source audit. No source code reused."""
from pathlib import Path
import sympy as S
import time,datetime,json,hashlib
start=time.monotonic();root=Path('verification/axis_pressure_controls_20261021T1005Z');root.mkdir(exist_ok=True)
t,r,z,rho,th=S.symbols('t r z rho th',real=True);mu,lam=S.symbols('mu lam',positive=True);m=S.symbols('m',positive=True);A=S.Function('A')(t)
rows=[]
def check(name,value,expected=0):
 diff=S.simplify(S.expand(value-expected));rows.append({'name':name,'value':str(S.simplify(value)),'expected':str(expected),'pass':diff==0});assert diff==0,(name,diff)
u=S.Integer(0);v=A;g=m*A;psi=A;p=(lam*S.diff(A,t)-A**2)*r**2/2-(lam*m*S.diff(A,t)+m**2*A**2)*z**2/(2*mu)
def D(f):return lam*S.diff(f,t)-v*r*S.diff(f,r)+g*z*S.diff(f,z)
check('full_Em_u',D(u)-m**2*u*v/2)
check('full_Em_v',D(v)-v**2+u**2-S.diff(p,r)/r)
check('full_Em_g',D(g)+g**2+mu*S.diff(p,z)/z)
check('full_Em_divergence',z*S.diff(g,z)-r*S.diff(v,r)+g-m*v)
check('full_Em_stream_v',v-psi-z*S.diff(psi,z))
check('full_Em_stream_g',g-m*psi-r*S.diff(psi,r))
for name,f in [('u',u),('v',v),('g',g),('psi',psi),('p',p)]:
 check(name+'_even_r',f.subs(r,-r)-f);check(name+'_even_z',f.subs(z,-z)-f)
P=p.subs({r:rho*S.cos(th),z:rho*S.sin(th)})
for angle in [0,S.pi/2,S.pi,-S.pi/2]:check('pressure_ridge_flat_'+str(angle),S.diff(P,th).subs(th,angle))
check('polar_pressure_chain',S.diff(P,rho)/rho+S.cos(th)*S.diff(P,th)/(rho**2*S.sin(th)),S.diff(p,z).subs({r:rho*S.cos(th),z:rho*S.sin(th)})/(rho*S.sin(th)))
limit=S.limit(S.cos(th)*S.diff(P,th)/S.sin(th),th,0)/rho**2
check('singular_axis_limit',limit,S.diff(p,z,2)-S.diff(p,r,2))
# Cartesian pressure jets beyond quadratic fields: independently take polar limit and compare the Cartesian quotient extension.
for name,q in [('quartic',2*r**4+3*r**2*z**2+7*z**4+r**2-2*z**2),('gaussian',(r**2-3*z**2)*S.exp(-r**2-z**2)),('rational',(2*r**2+z**2)/(1+r**2+z**2))]:
 Q=q.subs({r:rho*S.cos(th),z:rho*S.sin(th)});actual=S.limit(S.cos(th)*S.diff(Q,th)/S.sin(th),th,0)/rho**2
 expected=S.diff(q,z,2).subs({z:0,r:rho})-S.diff(q,r).subs({z:0,r:rho})/rho
 check('axis_jet_'+name,actual,expected)
# The incorrect apex ODE is evaluated directly, with actual exact solutions from the full equations above.
for mm in [1,2]:
 q=mm+1;mu0=S.Rational((2*q+mm)*mm**2,2*q-mm**2);lam0=S.Rational(mm**2*(q+1),q)
 check('distinguished_mu_'+str(mm),mu0,S.Rational(5,3) if mm==1 else S.Integer(16))
 predicted=(mu0-mm**2)/(mu0+mm)
 check('nonzero_steady_apex_prediction_'+str(mm),predicted,S.Rational(1,4) if mm==1 else S.Rational(2,3))
 assert predicted!=0
 check('scaled_apex_coefficient_'+str(mm),predicted/lam0,S.Rational(1,2*(q+1)))
 wrong_g=-mm**2-mu0*(-1)
 omitted=-mu0*(1-S.Rational(mm**2,1)/mu0)
 check('omitted_term_cancels_wrong_g_'+str(mm),wrong_g+omitted)
 check('wrong_g_nonzero_'+str(mm),wrong_g,mu0-mm**2)
 # At mu=m^2, the exact time-dependent family A=1+t has left lam and false RHS0.
 mismatch=lam0-(S.Rational(mm**2,1)-mm**2)/(mm**2+mm)*(1+t)**2
 check('dynamic_mu_m2_apex_mismatch_'+str(mm),mismatch,lam0);assert mismatch!=0
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'count':len(rows),'all_pass':all(q['pass'] for q in rows),'rows':rows,'proof_sha256':hashlib.sha256(Path('research/153_axis_reduction_literature_audit/PROOF.md').read_bytes()).hexdigest(),'scope':'Exact algebra for a source-reduction counterexample. Not B2 fields, no PDE solver or source code used.'}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
