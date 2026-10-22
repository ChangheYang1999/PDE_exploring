"""Exact Cartesian checks of the beta-three resonance. Uses only verifier code."""
from pathlib import Path
from datetime import datetime, timezone
import json,time
# Load only definitions from the verifier's Cartesian checker, never its test runner.
namespace={}
source=Path("code_independent/check_third_tail_cartesian.py").read_text().split("cases=[]",1)[0]
exec(compile(source,"own_cartesian_definitions","exec"),namespace)
S=namespace["S"]
x,y,R,z=[namespace[n] for n in ["x","y","R","z"]]
dx,dy,dot,velocity,curl,circle,invert,cart_stream,is_zero=[namespace[n] for n in ["dx","dy","dot","velocity","curl","circle","invert","cart_stream","is_zero"]]
start=time.monotonic();beta=S.Rational(3);s=S.Rational(1,3);m=s;k0=2-s;k1=2-2*s
rows=[]
for name,F0cart,H0cart in [
    ("one_mode",x/R,x*x/R**2),
    ("mixed_modes",x/R+S.Rational(4,7)*x*y/R**2+S.Rational(1,11)*(4*x**3/R**3-3*x/R),x*x/R**2*(1+y/(5*R)+y*y/(13*R**2))),
    ("mixed_zero_temperature",x/R+S.Rational(4,7)*x*y/R**2+S.Rational(1,11)*(4*x**3/R**3-3*x/R),S.Integer(0))
]:
    psi0=S.expand(R**k0*F0cart);th0=S.expand(R**m*H0cart);om0=curl(psi0);u0=velocity(psi0)
    om1=S.expand(dot(u0,om0)-dx(th0));th1=dot(u0,th0)
    A1=circle(om1);F1=invert(A1,k1);psi1=cart_stream(F1,k1);u1=velocity(psi1)
    om2=S.expand((dot(u0,om1)+dot(u1,om0)-dx(th1))/2)
    th2=S.expand((dot(u0,th1)+dot(u1,th0))/2)
    A2=circle(om2)
    alpha=S.expand(A2).coeff(z,1)+S.expand(A2).coeff(z,-1)
    cosine=(z+1/z)/2
    g=invert(S.expand(A2-alpha*cosine),S.Integer(1))
    assert not g.has(S.zoo)
    psi2=S.expand(cart_stream(g,S.Integer(1))-alpha*x*S.log(R)/2+S.Rational(7,11)*x)
    w2=velocity(psi2)
    Qom=S.expand(dot(w2,om0)+dot(u1,om1)+dot(u0,om2)-dx(th2))
    Qth=S.expand(dot(w2,th0)+dot(u1,th1)+dot(u0,th2))
    om3=S.expand(Qom/3-alpha*dy(om0)/6);th3=S.expand(Qth/3-alpha*dy(th0)/6)
    # Test log identities on two exact radii, retaining algebraic log constants.
    checks={
        "resonant_negative_curl":is_zero(circle(curl(psi2)-om2)),
        "first_sine_zero":is_zero(S.expand(A2).coeff(z,1)-S.expand(A2).coeff(z,-1)),
        "mean_zero":is_zero(S.expand(A2).coeff(z,0)),
        "velocity_divergence_zero":is_zero(circle(dx(w2[0])+dy(w2[1]))),
    }
    for nm,q,Q,shift in [("omega",om3,Qom,S.Integer(1)),("theta",th3,Qth,S.Integer(-1))]:
        residual=S.expand(3*(x*dx(q)+y*dy(q))+shift*q+Q)
        checks[nm+"_profile_balance_r1"]=is_zero(circle(residual))
        checks[nm+"_profile_balance_r2"]=is_zero(S.expand(residual.subs({x:2*(z+1/z)/2,y:2*(z-1/z)/(2*S.I),R:2},simultaneous=True)))
        expected=S.expand(-alpha*dy(om0 if nm=="omega" else th0)/6)
        logcoef=S.expand(q).coeff(S.log(R),1)
        checks[nm+"_log_coefficient"]=is_zero(circle(logcoef-expected))
    rows.append({'name':name,'alpha_exact':str(alpha),'checks':checks,'all_pass':all(checks.values())})
    print(name,'alpha',alpha,'all_pass',rows[-1]['all_pass'],flush=True)
result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'rows':rows,'all_pass':all(row['all_pass'] for row in rows),'scope':'Exact finite-order Cartesian identities on manufactured angular data, not global B2 solutions. The zero-temperature row tests the algebra only and does not satisfy profile nontriviality.'}
Path('research/91_beta_three_logarithmic_tail/verification/exact_cartesian_checks.json').write_text(json.dumps(result,indent=2)+'\n')
assert result['all_pass']
print('elapsed',result['elapsed_seconds'],flush=True)
