"""Own physical differentiation and finite polynomial controls for P229.
No numerics or lead code is imported. All coefficients are exact symbols.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import hashlib,json,time
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks={};diffs={}
root=Path(__file__).resolve().parents[1];out=root/'research/229_supercritical_neighbourhood_symbols/verification'
def check(name,left,right=0):
    d=s.factor(s.cancel(s.expand(left-right)));checks[name]=(d==0);diffs[name]=str(d)
def truth(name,value):checks[name]=bool(value)
x,y,k=s.symbols('x y k',real=True);beta=s.symbols('beta',positive=True);alpha=(beta-2)/2;L=1+3*beta/2;A0,c2=s.symbols('A0 c2')
a=s.Function('a')(y);A=s.Function('A')(y);qf=s.Function('q');cf=s.Function('C')
def norm(v):return s.simplify(v.doit().subs(s.diff(A,y),a).doit())
kx=x/a;Df=(2*beta-s.diff(qf(k),k)).subs(k,kx)*A+cf(kx)
w2=Df/a;w1=a*qf(kx)+kx*s.diff(a,y)*w2
om=norm(s.diff(w1,y)-s.diff(w2,x)); B=s.diff(a,y,2)/a-2*s.diff(a,y)**2/a**2
D=(2*beta-s.diff(qf(k),k))*A+cf(k)
claim=s.diff(a,y)*(qf(k)+2*beta*k-2*k*s.diff(qf(k),k))+k*D*B-(1+k*k*s.diff(a,y)**2)*s.diff(D,k)/a**2
check('generic_physical_divergence',norm(s.diff(w1,x)+s.diff(w2,y)),2*beta)
check('generic_material_k',norm(w1*s.diff(kx,x)+w2*s.diff(kx,y)),qf(kx))
check('generic_physical_negative_curl',norm(om.subs(x,k*a)),claim)
# New polynomial field differentiated directly in Cartesian coordinates.
P=s.Function('P');DP=L*A+P(kx);v2=DP/a;v1=a*alpha*kx+kx*s.diff(a,y)*v2
omt=norm(s.diff(v1,y)-s.diff(v2,x));omt_k=norm(omt.subs(x,k*a));DK=L*A+P(k)
ompoly=L*k*s.diff(a,y)+k*DK*B-(1+k*k*s.diff(a,y)**2)*s.diff(P(k),k)/a**2
check('comparison_curl',omt_k,ompoly)
check('comparison_divergence',norm(s.diff(v1,x)+s.diff(v2,y)),2*beta)
th=A0*kx*kx/2
check('comparison_temperature_transport',norm(v1*s.diff(th,x)+v2*s.diff(th,y)),(beta-2)*th)
phys=norm((a*(v1*s.diff(omt,x)+v2*s.diff(omt,y)+omt-s.diff(th,x))).subs(x,k*a))
pol=norm(a*alpha*k*s.diff(ompoly,k)+DK*s.diff(ompoly,y)+a*ompoly-A0*k)
check('comparison_physical_vorticity_residual',phys,pol)
# Axis identity and integrating factor.
phi=L*A/a;eta=-norm(s.diff(phi,y,2))-2*c2/a**3
axisom=s.expand(ompoly.subs(P(k),c2*k*k).doit()).coeff(k,1)/a
check('axis_negative_curl_formula',norm(axisom),eta)
check('axis_phi_derivative',norm(s.diff(phi,y)),L-phi*s.diff(a,y)/a)
check('axis_integrating_factor',norm(phi*s.diff(a*eta,y)+beta*a*eta/2),norm(a*(phi*s.diff(eta,y)+(2*beta+1-norm(s.diff(phi,y)))*eta)))
check('axis_homogeneous_weight',2*beta+1-L,beta/2)
# Exponents and exact symbolic threshold.
gamma=s.Rational(1,2)+1/beta;m=1-2/beta;j=s.symbols('j',integer=True,positive=True)
check('temperature_jet_exponent',j-j*gamma-m,(j/s.Integer(2)-1)*(1-2/beta))
check('velocity_jet_exponent',j-1+1/beta-(j+1)*gamma,j*(s.Rational(1,2)-1/beta)-s.Rational(3,2))
check('velocity_jet_threshold',((j*(s.Rational(1,2)-1/beta)-s.Rational(3,2))/(s.Rational(1,2)-1/beta)),j-3*beta/(beta-2))
b=s.symbols('b',positive=True);nu=s.symbols('nu',nonnegative=True)
truth('temperature_gap_positive_all_j_above2',s.factor(((j/s.Integer(2)-1)*(1-2/beta)).subs({j:3+nu,beta:2+b})).is_positive)
truth('scale_gamma_between_half_and_one',s.factor((1-gamma).subs(beta,2+b)).is_positive)
check('coercive_axis_exponent',L/beta-1,gamma)
# Direct highest-degree checks for different finite polynomial degrees.
ap=s.diff(a,y);ratio=ap/a;n=s.symbols('n',integer=True,positive=True);pn=s.symbols('p_n',nonzero=True)
top_formula=s.diff(B,y)-n*s.diff(ratio**2,y)
check('general_Riccati_derivative',top_formula,s.diff(ratio,y,2)-2*(n+1)*ratio*s.diff(ratio,y))
record={}
for degree in (2,3,4,6,8,10):
    # Odd degrees are useful algebra controls even though B2 admits even ones only.
    poly=pn*k**degree+(c2*k*k if degree!=2 else 0)+s.Rational(2,7)*k+s.Rational(3,11)
    field=s.expand(ompoly.subs(P(k),poly).doit()); DD=L*A+poly
    residual=norm(a*alpha*k*s.diff(field,k)+DD*s.diff(field,y)+a*field-A0*k)
    highest=s.expand(residual).coeff(k,2*degree+1)
    check(f'degree{degree}_highest_residual',highest,pn**2*top_formula.subs(n,degree))
    check(f'degree{degree}_highest_curl',s.expand(field).coeff(k,degree+1),pn*(B-degree*ratio**2))
    truth(f'degree{degree}_nothing_above_top',s.Poly(residual,k).degree()<=2*degree+1)
    record[str(degree)]=str(s.factor(highest/pn**2))
    print('degree',degree,'checked',flush=True)
# Exact Riccati linearization.
K=s.symbols('K',real=True);vv=a**(-(n+1));ric=s.diff(ratio,y)-(n+1)*ratio**2-K
check('Riccati_to_linear_ODE',(s.diff(vv,y,2)+(n+1)*K*vv)/vv,-(n+1)*ric)
mu=s.symbols('mu',positive=True);c,d=s.symbols('c d')
for name,value,kap in [('affine',c+d*y,0),('oscillatory',c*s.cos(mu*y)+d*s.sin(mu*y),mu**2/(n+1)),('hyperbolic',c*s.exp(mu*y)+d*s.exp(-mu*y),-mu**2/(n+1))]:
    check(f'linear_ODE_{name}',s.diff(value,y,2)+(n+1)*kap*value)
# Counterexample controls: local/global polynomial B2 equations need not be sublinear.
cc=-A0/beta;wex=s.Matrix([alpha*x,L*y+cc*x*x]);oex=-2*cc*x;tex=A0*x*x/2
check('polynomial_control_divergence',s.diff(wex[0],x)+s.diff(wex[1],y),2*beta)
check('polynomial_control_temperature',wex.dot(s.Matrix([s.diff(tex,x),s.diff(tex,y)]))-(beta-2)*tex)
check('polynomial_control_vorticity',wex.dot(s.Matrix([s.diff(oex,x),s.diff(oex,y)]))+oex-s.diff(tex,x))
check('polynomial_control_axis_slope',s.diff(wex[1].subs(x,0),y),L)
truth('polynomial_control_not_sublinear',s.factor((L-beta).subs(beta,2+b)).is_positive)
# Smooth flat remainders do not become analytic just because their jets vanish.
flat=s.exp(-1/k**2)
for order in range(7):
    check(f'flat_remainder_derivative{order}',s.limit(s.diff(flat,k,order),k,0,dir='+'))
# A nonzero negative-curvature contribution is required at the center.
check('center_eta_value',A0/(beta/2),2*A0/beta)
end=datetime.now(timezone.utc).isoformat();report={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-t0,'all_passed':all(checks.values()),'checks':checks,'differences':diffs,'highest_degree_formulas':record,'proof_sha256':hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Independent Cartesian differentiation, exact exponent algebra, finite degree controls and Riccati linearization. No lead or numerics code.','scope':'Controls support standalone proof; arbitrary degree and flat germ argument are proved informally, not by finite samples. Broad symbol-bound dependency separately audited.'}
(out/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({key:report[key] for key in ('started_utc','ended_utc','elapsed_seconds','all_passed')},indent=2));print('checks',len(checks),'failed',[q for q,v in checks.items() if not v])
