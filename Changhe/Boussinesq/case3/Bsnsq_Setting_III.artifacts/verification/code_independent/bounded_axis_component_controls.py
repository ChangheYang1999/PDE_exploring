"""Independent exact algebra for P273. No fitting-lane imports or numerical PDE claims."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,time,hashlib
start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
root=Path('research/273_bounded_axis_component');out=root/'verification/controls.json'
x,y=s.symbols('x y',real=True);B=s.symbols('beta',positive=True);A=s.symbols('A',nonzero=True,real=True)
d=(3*B+2)/2;k=(B+6)/2;c=7*B+2
b,T,e,v,D=[s.Function(n)(y) for n in ('b','T','eta','v','D')]
records=[]
def ck(name,expr,expected=0):
    error=s.factor(s.simplify(expr-expected));ok=error==0
    records.append({'name':name,'passed':ok,'error':str(error)})
def truth(name,val): records.append({'name':name,'passed':bool(val)})
TH=T*x*x/2+D*x**4/24
W1=(2*B-s.diff(b,y))*x-s.diff(v,y)*x**3/3
W2=b+v*x*x
OM=(-s.diff(b,y,2)-2*v)*x-s.diff(v,y,2)*x**3/3
TT=s.expand(W1*s.diff(TH,x)+W2*s.diff(TH,y)-(B-2)*TH)
OO=s.expand(W1*s.diff(OM,x)+W2*s.diff(OM,y)+OM-s.diff(TH,x))
ck('divergence',s.diff(W1,x)+s.diff(W2,y),2*B)
ck('negative curl',s.diff(W1,y)-s.diff(W2,x),OM)
ck('thermal x2 factorial',2*TT.coeff(x,2),b*s.diff(T,y)+(3*B+2-2*s.diff(b,y))*T)
ck('thermal x4 factorial',24*TT.coeff(x,4),b*s.diff(D,y)+(7*B+2-4*s.diff(b,y))*D-8*s.diff(v,y)*T+12*v*s.diff(T,y))
eta=-s.diff(b,y,2)-2*v
ck('vorticity x coefficient',OO.coeff(x,1),b*s.diff(eta,y)+(2*B+1-s.diff(b,y))*eta-T)
for name,f,sgn in [('W1',W1,-1),('W2',W2,1),('Theta',TH,1),('Omega',OM,-1)]:ck(name+' x parity',f.subs(x,-x),sgn*f)
core={b:d*y,T:A,D:0,v:-A/B}
for name,f,expected in [('W1',W1,(B-2)*x/2),('W2',W2,d*y-A*x*x/B),('Theta',TH,A*x*x/2),('Omega',OM,2*A*x/B)]:
    ck('core '+name,f.subs(core).doit(),expected)
ck('core full thermal PDE',TT.subs(core).doit())
ck('core full vorticity PDE',OO.subs(core).doit())
ck('origin normalization a0',s.diff(TH,x,2).subs(core).doit().subs(x,0)/2,A/2)
ck('origin vorticity normalization',s.diff(OM,x).subs(core).doit().subs(x,0),2*A/B)
ck('nonlinear relative vertical velocity',W2.subs(core).doit().subs(y,0),-A*x*x/B)
rho=s.Function('rho')(y);r=s.Function('r')(y);I=s.Function('I')(y);G=s.Function('G')(y);R=s.Function('R')(y)
rhop=(d-s.diff(b,y))*rho/b
ck('rho b derivative',s.diff(rho*b,y).subs(s.diff(rho,y),rhop),d*rho)
ck('T2 after rho equation',(b*s.diff(A/rho**2,y)+(3*B+2-2*s.diff(b,y))*A/rho**2).subs(s.diff(rho,y),rhop))
expr=b*s.diff(r/rho,y)+(2*B+1-s.diff(b,y))*r/rho-A/rho**2
ck('eta equation after r equation',expr.subs(s.diff(rho,y),rhop).subs(s.diff(r,y),(A/rho-B*r/2)/b))
ck('d-kappa',d-k,B-2)
phi=s.Function('phi')(y);al=B/(2*d)
rexpr=A/d*R**(-al)*phi
ck('integral formula for r', s.powsimp((b*s.diff(rexpr,y)+B*rexpr/2-A/rho).subs({s.diff(R,y):rho,s.diff(phi,y):R**(al-1),b:d*R/rho}).subs(R,s.Symbol('Rpos',positive=True)),force=True))
ck('core r integral coefficient',A/(d*al),2*A/B)
ck('alpha d',al*d,B/2)
ck('tail integral exponential gap',d-B/2,B+1)
ck('eta exponential rate',d+B/2,2*B+1)
original=s.diff(rho**3*v,y)-A/s.Integer(8)*(b*rho*s.diff(I,y)+(d-k)*rho*I)
original=original.subs(s.diff(rho,y),rhop)
physical=b*s.diff(A**2*I/rho**4,y)+(7*B+2-4*s.diff(b,y))*A**2*I/rho**4-8*s.diff(v,y)*A/rho**2+12*v*s.diff(A/rho**2,y)
physical=physical.subs(s.diff(rho,y),rhop)
ck('integrated fourth jet multiplier',-original*8*(A/rho**2)/rho**3,physical)
q=s.symbols('tau',positive=True);Cr=s.symbols('C_rho',positive=True)
rt=Cr*q**2*s.exp(d*q);Rt=Cr/d*s.exp(d*q);Tt=A/Cr**2/q**4*s.exp(-2*d*q)
et=s.Function('eta_endpoint')(q)
for side in (1,-1):
    by=side/q**2
    dy=lambda f:side*q*q*s.diff(f,q)
    ck(f'endpoint{side} bprime',dy(by),-2/q)
    ck(f'endpoint{side} bsecond',dy(dy(by)),2*side)
    ck(f'endpoint{side} transport derivative',by*dy(s.Function('f')(q)),s.diff(s.Function('f')(q),q))
    ck(f'endpoint{side} rho equation',by*dy(rt),(d-dy(by))*rt)
    ck(f'endpoint{side} R derivative',dy(side*Rt),rt)
    ck(f'endpoint{side} rho b',rt*by,d*side*Rt)
    ck(f'endpoint{side} thermal ODE',by*dy(Tt)+(3*B+2-2*dy(by))*Tt)
    ve=-side-et/2
    F=8*dy(ve)*Tt-12*ve*dy(Tt)
    ck(f'endpoint{side} force main', (F/Tt).subs({et:0,s.diff(et,q):0}),-24*d*q*q-48*q)
    remainder=side*(-4*q*q*s.diff(et,q)-24*q*et-12*d*q*q*et)
    ck(f'endpoint{side} force remainder',F/Tt+24*d*q*q+48*q,remainder)
    K=s.Function('K')(q)
    eq=s.diff(Tt*K,q)+(c+8/q)*Tt*K
    ck(f'endpoint{side} K equation',eq/Tt,s.diff(K,q)+(4*B+4/q)*K)
ck('positive D exponential gap',c-2*d,4*B)
ck('D integrating factor derivative',s.diff(q**8*s.exp(c*q),q)/(q**8*s.exp(c*q)),c+8/q)
ck('K integrating factor derivative',s.diff(q**4*s.exp(4*B*q),q)/(q**4*s.exp(4*B*q)),4*B+4/q)
ck('K leading coefficient',-24*d/(4*B),-6*d/B)
ck('A I identity',A*(Tt*s.Function('K')(q))/Tt**2,rt**2*s.Function('K')(q))
# Finite exact instances test the derivative mechanism; the proof treats every order.
for order in range(1,7):
    f=Tt
    for _ in range(order): f=s.diff(f,q)*q*q
    ratio=s.simplify(f/Tt)
    truth('flat thermal derivative polynomial '+str(order),s.denom(s.factor(ratio))==1 or s.Poly(ratio,q) is not None)
for name,expr in [('c-2d',c-2*d),('d-beta/2',d-B/2),('2d',2*d),('2beta+1',2*B+1)]:
    truth(name+' positive for beta>=2',s.ask(s.Q.positive(expr)))
proof=root/'PROOF.md';initial=json.loads((root/'verification/proof_written.json').read_text())
truth('informal proof predates controls',initial['utc']<utc)
truth('exact derivative multiplier recorded','by 8T/rho^3' in proof.read_text())
result={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'passed':sum(z['passed'] for z in records),'total':len(records),'checks':records,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Exact algebra and source provenance. No numerical/full-plane existence assertion.'}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('started_utc','ended_utc','elapsed_seconds','passed','total')},indent=2))
for z in records:
    if not z['passed']: print(z)
raise SystemExit(0 if all(z['passed'] for z in records) else 1)
