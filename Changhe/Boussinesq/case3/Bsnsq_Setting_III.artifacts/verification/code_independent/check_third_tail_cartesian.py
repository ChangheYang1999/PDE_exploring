"""Exact Cartesian differentiation checks of packet 90. No numerics-lane imports."""
from pathlib import Path
from datetime import datetime, timezone
import json, time
import sympy as S

root = Path("research/90_third_terms_and_constant_velocity/verification")
start = time.monotonic()
x,y,R,z = S.symbols("x y R z", nonzero=True)
I = S.I

def dx(q):
    return S.expand(S.diff(q,x) + x/R*S.diff(q,R))
def dy(q):
    return S.expand(S.diff(q,y) + y/R*S.diff(q,R))
def dot(u,q):
    return S.expand(u[0]*dx(q)+u[1]*dy(q))
def velocity(p):
    return (-dy(p),dx(p))
def curl(p):
    return S.expand(-dx(dx(p))-dy(dy(p)))
def circle(q):
    return S.expand(q.subs(R,1).subs({x:(z+1/z)/2,y:(z-1/z)/(2*I)}, simultaneous=True))
def diff_angle(q):
    return S.expand(I*z*S.diff(q,z))
def invert(q,k):
    out=0
    for term in S.Add.make_args(S.expand(q)):
        n=int(term.as_powers_dict().get(z,0))
        out += term/(n*n-k*k)
    return S.expand(out)
def cart_stream(f,k):
    out=0
    for term in S.Add.make_args(S.expand(f)):
        n=int(term.as_powers_dict().get(z,0))
        c=term/z**n
        out += c*R**(k-abs(n))*(x+I*y if n>=0 else x-I*y)**abs(n)
    return S.expand(out)
def is_zero(q):
    return S.expand(q)==0

cases=[]
for beta in [S.Rational(5,2),S.Rational(7,3),S.Rational(8,3),S.Rational(4)]:
    s=1/beta;m=1-2*s;k0=2-s;k1=2-2*s
    psi0=S.expand(R**k0*(x/R+S.Rational(4,7)*x*y/R**2+S.Rational(1,11)*(4*x**3/R**3-3*x/R)))
    th0=S.expand(R**m*x*x/R**2*(1+y/(5*R)+y*y/(13*R**2)))
    om0=curl(psi0);u0=velocity(psi0)
    om1=S.expand(dot(u0,om0)-dx(th0));th1=dot(u0,th0)
    A0,A1,H0,H1=map(circle,[om0,om1,th0,th1])
    F0=circle(psi0);F1=invert(A1,k1)
    psi1=cart_stream(F1,k1);u1=velocity(psi1)
    om2=S.expand((dot(u0,om1)+dot(u1,om0)-dx(th1))/2)
    th2=S.expand((dot(u0,th1)+dot(u1,th0))/2)
    ca=(z+1/z)/2;sa=(z-1/z)/(2*I)
    a2formula=S.expand((k0*F0*diff_angle(A1)+2*s*diff_angle(F0)*A1+k1*F1*diff_angle(A0)+s*diff_angle(F1)*A0-(m-s)*ca*H1+sa*diff_angle(H1))/2)
    h2formula=S.expand((k0*F0*diff_angle(H1)-(m-s)*diff_angle(F0)*H1+k1*F1*diff_angle(H0)-m*diff_angle(F1)*H0)/2)
    checks={
        "source0_poisson":is_zero(A0+diff_angle(diff_angle(F0))+k0*k0*F0),
        "source1_poisson":is_zero(circle(curl(psi1))-A1),
        "third_vorticity_cartesian_vs_angular":is_zero(circle(om2)-a2formula),
        "third_temperature_cartesian_vs_angular":is_zero(circle(th2)-h2formula),
        "negative_curl_sign":is_zero(circle(dy(u0[0])-dx(u0[1])-om0)),
        "divergence_zero":is_zero(circle(dx(u0[0])+dy(u0[1]))),
    }
    # The C correction is checked against the Euler profile operators in Cartesian form.
    C=S.Rational(-7,11)
    omC=S.expand(C*dy(om0)/beta);thC=S.expand(C*dy(th0)/beta)
    checks["C_vorticity_profile_balance"]=is_zero(circle(beta*(x*dx(omC)+y*dy(omC))+omC+C*dy(om0)))
    checks["C_temperature_profile_balance"]=is_zero(circle(beta*(x*dx(thC)+y*dy(thC))-(beta-2)*thC+C*dy(th0)))
    for name,q,deg in [("third_vorticity",om2,-3*s),("third_temperature",th2,m-2*s)]:
        checks[name+"_homogeneity"]=is_zero(circle(x*dx(q)+y*dy(q)-deg*q))
    vals={name:str(S.expand(q.subs({x:S.Rational(3,5),y:S.Rational(4,5),R:1}, simultaneous=True))) for name,q in [("omega2",om2),("theta2",th2),("omegaC",omC),("thetaC",thC)]}
    case={"beta":str(beta),"checks":checks,"witness_circle_3_5_4_5":vals,"all_pass":all(checks.values())}
    cases.append(case)
    print("beta",beta,"checks",len(checks),"all_pass",case["all_pass"],flush=True)
result={"timestamp_utc":datetime.now(timezone.utc).isoformat(),"method":"Exact rational SymPy algebra; independent total Cartesian derivatives with R=sqrt(x^2+y^2), compared after exact Laurent substitution on the circle.","cases":cases,"all_pass":all(c["all_pass"] for c in cases),"elapsed_seconds":time.monotonic()-start,"scope":"Manufactured angular data and algebraic identities only; these data are not exact global B2 profiles. No convergence or interval proof supplied by this check."}
root.joinpath("cartesian_exact_checks.json").write_text(json.dumps(result,indent=2)+"\n")
assert result["all_pass"]
print("elapsed_seconds",result["elapsed_seconds"],flush=True)
