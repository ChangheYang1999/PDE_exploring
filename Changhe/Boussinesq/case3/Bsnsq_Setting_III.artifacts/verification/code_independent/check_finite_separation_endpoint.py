"""Independent exact controls for P199. No numerical-lane implementation imported."""
from pathlib import Path
from datetime import datetime, timezone
import json, time
import sympy as S
root=Path('research/199_finite_separation_outgoing_endpoint/verification')
t0=time.monotonic(); checks=[]
def zero(name, expr):
    if isinstance(expr,S.MatrixBase): ok=all(S.simplify(v)==0 for v in expr)
    else: ok=S.simplify(expr)==0
    assert ok, (name,expr)
    checks.append(name)
s,z,a,r=S.symbols('s z a r',real=True)
rho=S.symbols('rho',positive=True)
alpha,xi,eta,omega=S.symbols('alpha xi eta omega',real=True)
phi=S.symbols('phi',real=True)
e=S.Matrix([S.cos(phi),S.sin(phi)]); n=S.Matrix([-S.sin(phi),S.cos(phi)])
R=rho*e; A=alpha*rho*e-n/rho
zero('positive area orientation',S.det(S.Matrix.hstack(A,R))-1)
zero('tangential dot product',A.dot(R)-alpha*rho**2)
P=S.Matrix([[xi-alpha*eta,eta/rho,0],[-eta/rho**3,xi-alpha*eta,0],[0,2*eta/rho**2,eta]])
zero('full principal determinant',P.det()-eta*((xi-alpha*eta)**2+eta**2/rho**4))
zero('characteristic conormal',P.det().subs({xi:1,eta:0}))
B=S.Matrix([[alpha,-1/rho],[1/rho**3,alpha]])
for sign in [-1,1]: zero('complex speed '+str(sign),(B-(alpha+sign*S.I/rho**2)*S.eye(2)).det())
# Physical curl differentiated in Cartesian coordinates, through independent Jacobian inversion.
chart_rows=[]
for kappa in [S.Rational(1,5),S.Rational(2,5),S.Rational(-3,7)]:
    v=r+a*a+a**3/3
    X=S.Matrix([a+kappa*v*v,v]); Aa=X.diff(a); Rr=X.diff(r); J=S.Matrix.hstack(Aa,Rr)
    zero('shear area '+str(kappa),J.det()-1)
    q=S.expand(Rr.dot(Rr)); al=S.cancel(Aa.dot(Rr)/q)
    phia=S.cancel(S.det(S.Matrix.hstack(Rr,Rr.diff(a)))/q)
    phir=S.cancel(S.det(S.Matrix.hstack(Rr,Rr.diff(r)))/q)
    physical_DW=(4*r*Rr).jacobian([a,r])*J.inv()
    om=S.expand(physical_DW[0,1]-physical_DW[1,0])
    zero('physical divergence '+str(kappa),S.trace(physical_DW)-4)
    zero('one form curl '+str(kappa),om-4*S.diff(r*Aa.dot(Rr),r)+4*r*S.diff(q,a))
    zero('compatibility rho '+str(kappa),q.diff(a)/2-q*al.diff(r)-al*q.diff(r)/2-phir)
    zero('compatibility angle '+str(kappa),phia-al*phir-q.diff(r)/(2*q*q))
    zero('curl eliminated '+str(kappa),om-4*al*q+4*r*al.diff(r)*q+8*r*phir)
    zero('final rho equation '+str(kappa),q.diff(a)/2-al*q.diff(r)/2+phir-al*q/r+om/(4*r))
    zero('final alpha equation '+str(kappa),al.diff(r)-al/r+2*phir/q+om/(4*r*q))
    for rr in [S.Rational(-3,4),S.Rational(2,3)]:
        aa=S.Rational(1,7); qq=q.subs({a:aa,r:rr})
        assert qq>0
        chart_rows.append({'kappa':str(kappa),'a':str(aa),'r':str(rr),'rho_squared':str(qq),'omega':str(om.subs({a:aa,r:rr}))})
# Analytic vector functions with dependencies invisible to low-order jets.
Ts=[S.Matrix([1,0]),S.Matrix([0,z**7]),S.Matrix([z**11,z**13]),S.Matrix([S.sin(z)-z+z**3/6,S.cos(z)-1+z*z/2])]
rank_rows=[]
for M in [0,3,4,7,10,11,13]:
    Qall=S.Matrix([[T[c].diff(z,j).subs(z,0) for T in Ts] for c in [0,1] for j in range(M+1)])
    rank_rows.append({'maximum_jet_order':M,'rank':Qall.rank()})
assert rank_rows[-1]['rank']==4 and rank_rows[-3]['rank']==3
selected=[(0,0),(1,7),(0,11),(1,4)]
Q=S.Matrix([[T[c].diff(z,j).subs(z,0) for T in Ts] for c,j in selected]); assert Q.det()!=0
bs=S.Matrix(S.symbols('b0:4')); h=S.symbols('arbitrary_h')
W=sum((Ts[j]*bs[j] for j in range(4)),S.zeros(2,1))
Wbad=(bs[0]-h)*Ts[0]+(bs[1]-h)*Ts[1]+bs[2]*Ts[2]+bs[3]*Ts[3]+h*(Ts[0]+Ts[1])
zero('arbitrary coefficient cancellation',Wbad-W)
jets=S.Matrix([W[c].diff(z,j).subs(z,0) for c,j in selected])
zero('finite jet coefficient recovery',Q.inv()*jets-bs)
# Independent complex polynomial tests of both CR signs, trace conversion and recovery.
w=s+S.I*z
for degree in [2,3,5,9]:
    G=S.expand(w**degree+(2+S.I)*w**(degree+2))
    Ws=S.re(G).expand(complex=True); Wz=4*z-S.im(G).expand(complex=True)
    zero('CR divergence degree'+str(degree),S.diff(Ws,s)+S.diff(Wz,z)-4)
    zero('CR curl degree'+str(degree),S.diff(Wz,s)-S.diff(Ws,z))
    zero('complex recovery degree'+str(degree),Ws-S.I*Wz+4*S.I*z-G)
    trace=G.subs(s,0); zz=S.symbols('zz')
    zero('complexified trace sign degree'+str(degree),trace.subs(z,zz).subs(zz,-S.I*w)-G)
    for component in [Ws,Wz]:
        assert component.subs({s:0,z:0})==0
    zero('endpoint derivative degree'+str(degree),S.Matrix([Ws,Wz]).jacobian([s,z]).subs({s:0,z:0})-S.diag(0,4))
# The integral operator is algebraically zeroth order on its input, with correct ODE.
u=S.symbols('u',positive=True); g=sum(S.Rational(j+1,j+2)*r**j for j in range(13))
Ag=sum(S.Rational(j+1,j+2)*r**j/(4*j+1) for j in range(13))
zero('bounded transport integral ODE',4*r*S.diff(Ag,r)+Ag-g)
for rr in [S.Rational(-2,3),S.Rational(3,5)]:
    direct=sum(S.Rational(j+1,j+2)*rr**j*S.integrate(u**(S.Rational(-3,4)+j),(u,0,1))/4 for j in range(13))
    zero('integral both signs '+str(rr),direct-Ag.subs(r,rr))
# Concrete domain correction: sigma may be negative under all listed graph-jet conditions.
sigma=-z*z; kval=s*s
zero('graph composition order4',sigma.subs(z,kval)+s**4)
for zz in [S.Rational(1,10),S.Rational(-1,20)]:
    ss=-zz*zz/2
    assert ss<0 and sigma.subs(z,zz)<ss
    checks.append('raw set includes negative s '+str(zz))
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'exact_checks_count':len(checks),'exact_checks':checks,'finite_jet_ranks':rank_rows,'jet_evaluation_determinant':str(Q.det()),'area_chart_samples':chart_rows,'all_passed':True,'scope':'Finite exact controls of signs, chart formulas, jet recovery, trace continuation algebra, integral ODE, and domain counterexample. The functional theorem rests on PROOF.md, not these tests. No endpoint or general solvability follows.'}
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['utc','elapsed_seconds','exact_checks_count','finite_jet_ranks','all_passed']},indent=2))
