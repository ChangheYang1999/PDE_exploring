"""Independent P275 exact identities and scalar geometry diagnostics, not a B2 solver."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math,time
import sympy as s
root=Path('research/275_curvature_spikes_axis_limits');vdir=root/'verification';tick=time.monotonic();utc=datetime.now(timezone.utc).isoformat();cs=[]
def ck(name,e,want=0):
 err=s.simplify(e-want);cs.append({'name':name,'passed':err==0,'error':str(err)})
def tr(name,value):cs.append({'name':name,'passed':bool(value)})
beta=s.symbols('beta',positive=True);A=s.symbols('A',positive=True);delta=s.symbols('delta',positive=True);ell=s.symbols('ell',positive=True);Y=s.symbols('Y',positive=True);q=s.symbols('q',positive=True);N=s.symbols('N',integer=True,positive=True)
d=(3*beta+2)/2;k=(beta+6)/2;gamma=s.Rational(1,2)+1/beta;m=1-2/beta;p=d/beta;qp=k/beta
c=(d-beta)*(1-q)/q**N
ck('geometric mass',c*q**N/(1-q),d-beta)
ck('positive d-beta',d-beta,beta/2+1)
w=Y**(1-delta)/s.log(Y)**ell;an=s.Symbol('c',positive=True)*Y**(-delta)
ck('relative width',w/Y,Y**(-delta)/s.log(Y)**ell)
ck('curvature amplitude',an/w,s.Symbol('c',positive=True)/Y*s.log(Y)**ell)
for order in range(1,6):
 ck('derivative power '+str(order),-delta-order*(1-delta),-order+(order-1)*delta)
 ck('derivative amplitude '+str(order),s.powsimp((an/w**order).subs(s.log(Y),s.Symbol('LogY',positive=True)),force=True),s.Symbol('c',positive=True)*Y**(-delta-order*(1-delta))*s.Symbol('LogY',positive=True)**(order*ell))
for name,e in [('rho power',p-1-gamma),('P power',3*gamma-1-qp),('I power',qp-1-gamma+m),('quartic d-k',d-k-beta+2),('r tail integrand',s.Rational(1,2)-1-gamma+1+1/beta),('eta exponent',-s.Rational(1,2)-gamma+1+1/beta),('rho inverse faster',3*gamma-(1+1/beta)-(s.Rational(1,2)+2/beta)),('r alpha integrand',(beta/(2*d)-1)*p+1+1/beta)]:ck(name,e)
y=s.symbols('y',positive=True);b=s.Function('b')(y);rho=s.Function('rho')(y);r=s.Function('r')(y);R=s.Function('R')(y);vv=s.Function('v')(y);G=s.Function('G')(y);h=s.Function('h')(y);Phi=s.Function('Phi')(y);eta=r/rho
rhop=(d-s.diff(b,y))*rho/b;rp=(A/rho-beta*r/2)/b
ck('rho b ODE',s.diff(rho*b,y).subs(s.diff(rho,y),rhop),d*rho)
T=A/rho**2
ck('thermal x2', (b*s.diff(T,y)+(3*beta+2-2*s.diff(b,y))*T).subs(s.diff(rho,y),rhop))
ck('vorticity x1',(b*s.diff(eta,y)+(2*beta+1-s.diff(b,y))*eta-T).subs({s.diff(rho,y):rhop,s.diff(r,y):rp}))
P=rho**3/(b*h);f=eta-2*A/(beta*rho**3)
forcing=8/A*(rho**3*(-s.diff(b,y,2)-eta)/2+A/beta)
ck('Phi derivative',forcing/(b*h),-4/A*P*(s.diff(b,y,2)+f))
I=s.diff(h*Phi,y)/rho
ck('I extraction',I.subs(s.diff(h,y),k*h/b),h/(b*rho)*(k*Phi+b*s.diff(Phi,y)))
I2=(I.subs(s.diff(h,y),k*h/b)).subs(s.diff(Phi,y),-4/A*P*(s.diff(b,y,2)+f))
ck('full critical extraction',y**m*I2,y**m*h/(b*rho)*(k*Phi-4/A*b*P*(s.diff(b,y,2)+f)))
# Direct Cartesian factorial and curl controls for the three physical jet equations.
x=s.symbols('x',real=True);TT=s.Function('Tphysical')(y);DD=s.Function('Dphysical')(y);vp=s.Function('vphysical')(y)
Th=TT*x*x/2+DD*x**4/24
WW1=(2*beta-s.diff(b,y))*x-s.diff(vp,y)*x**3/3;WW2=b+vp*x*x
RTh=s.expand(WW1*s.diff(Th,x)+WW2*s.diff(Th,y)-(beta-2)*Th)
ck('Cartesian thermal fourth factorial',24*RTh.coeff(x,4),b*s.diff(DD,y)+(7*beta+2-4*s.diff(b,y))*DD-8*s.diff(vp,y)*TT+12*vp*s.diff(TT,y))
ck('Cartesian divergence',s.diff(WW1,x)+s.diff(WW2,y),2*beta)
ck('Cartesian negative curl',s.diff(WW1,y)-s.diff(WW2,x),(-s.diff(b,y,2)-2*vp)*x-s.diff(vp,y,2)*x**3/3)
# Taylor's exact integral identity underlying redundancy of j1.
ss,hh=s.symbols('ss hh',positive=True)
for nn in range(0,7):
 gg=y**nn
 ck('Taylor integral polynomial control '+str(nn),gg.subs(y,y+hh)-gg-hh*s.diff(gg,y)-s.integrate((hh-ss)*s.diff(gg,y,2).subs(y,y+ss),(ss,0,hh)))
# The global theorem uses arbitrary smooth g, as proved by integral remainder.
# Explicit smooth-cutoff derivative at a valid interior point.
z=s.symbols('z',real=True);chi=1/(1+s.exp(1/z-1/(1-z)))
ck('cutoff midpoint',chi.subs(z,s.Rational(1,2)),s.Rational(1,2))
ck('cutoff positive midpoint derivative',s.diff(chi,z).subs(z,s.Rational(1,2)),2)
ck('beta2 critical exponent',m.subs(beta,2))
ck('beta2 d',d.subs(beta,2),4);ck('beta2 kappa',k.subs(beta,2),4)
# These arithmetic sample diagnostics supplement the analytic infinite-sequence argument.
diags=[]
for bv,dv in [(2.0,0.5),(3.0,1/3),(10.0,0.1),(2.0,0.9),(3.0,0.75)]:
 ev=2.0;nv=8;dv0=(3*bv+2)/2;cc=(dv0-bv)*(1-2**(-dv))*2**(nv*dv)
 sample=[]
 for nn in (nv,nv+8,nv+24,nv+56):
  yy=2.0**nn;ww=yy**(1-dv)/math.log(yy)**ev;anv=cc*yy**(-dv);yp=yy+ww/2
  curve=yp*anv/ww*2;rat=curve/math.log(yy)**ev
  sample.append({'n':nn,'width_ratio':ww/yy,'peak_over_logell':rat,'limiting_coefficient':2*cc,'curvature_bound_violation_ratio':curve*yp**dv})
  tr(f'geometry beta{bv} delta{dv} n{nn}',ww<=yy/4 and yy+ww<1.5*yy<2*yy)
  tr(f'exact peak identity beta{bv} delta{dv} n{nn}',abs(rat/(2*cc)-(1+ww/(2*yy)))<1e-13)
 tr(f'peak coefficient improves beta{bv} delta{dv}',abs(sample[-1]['peak_over_logell']/(2*cc)-1)<abs(sample[0]['peak_over_logell']/(2*cc)-1))
 diags.append({'beta':bv,'delta':dv,'ell':ev,'N':nv,'samples':sample})
pb=json.loads((vdir/'proof_before_checks.json').read_text());tr('proof before controls',pb['utc']<utc);tr('proof unchanged',pb['proof_sha256']==hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest());tr('source full answer retained',(vdir/'A158_answer.md').exists())
result={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in cs),'total':len(cs),'checks':cs,'geometry_diagnostics':diags,'scope':'Exact algebra and finite arithmetic diagnostics only. Analytic proof treats smooth joining, all derivatives and infinite limits; no full B2 profile asserted.'}
(vdir/'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({key:result[key]for key in ('started_utc','ended_utc','elapsed_seconds','passed','total')},indent=2));print([z for z in cs if not z['passed']]);raise SystemExit(0 if all(c['passed']for c in cs) else 1)
