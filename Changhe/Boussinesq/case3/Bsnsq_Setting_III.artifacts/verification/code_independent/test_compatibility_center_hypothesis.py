"""Independent exact controls for packet170; no fitting-lane imports."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys, time
import sympy as s
started=time.monotonic(); x,y,b,c,q=s.symbols('x y beta c q', real=True); k=b-2
rows=[]
def eq(label,a,z=0):
    r=s.factor(a-z)
    rows.append({'label':label,'passed':r==0,'residual':str(r)})
    if r!=0: raise AssertionError((label,r))
def calc(psi):
    ux=-s.diff(psi,y); uy=s.diff(psi,x)
    w1=b*x+ux-ux.subs({x:0,y:0}); w2=b*y+uy-uy.subs({x:0,y:0})
    adv=lambda f: s.expand(w1*s.diff(f,x)+w2*s.diff(f,y))
    om=-s.diff(psi,x,2)-s.diff(psi,y,2); F=adv(om)+om
    J=s.diff(w2,x); D=(k-s.diff(w1,x))*F-adv(F)
    Z=s.expand(w1*F*J+w2*D)
    E=s.expand(J*s.diff(Z,y)-Z*s.diff(J,y)-k*D*J)
    th=s.integrate(F,x); th=s.expand(th-th.subs(x,0))
    t=s.expand(adv(th)-k*th)
    return dict(psi=psi,w1=w1,w2=w2,om=om,F=F,J=J,D=D,Z=Z,E=E,th=th,t=t)
a=calc(c*x*y-q*x**3/6)
expected={'om':q*x,'w1':(b-c)*x,'w2':(b+c)*y-q*x*x/2,
 'F':q*(b-c+1)*x,'th':q*(b-c+1)*x*x/2,
 't':q*(b-c+1)*(b+2-2*c)*x*x/2,
 'E':q*q*(c+2)*(b-c+1)*(b+2-2*c)*x*x}
for name,val in expected.items(): eq('symbolic family '+name,a[name],val)
eq('boundary E zero',a['E'].subs(c,-2))
eq('boundary thermal residual',a['t'].subs(c,-2),q*(b+3)*(b+6)*x*x/2)
eq('normalized family thermal zero',a['t'].subs(c,1+b/2))
eq('normalized family center q=4a/b',4*s.expand(a['th']/x**2).subs(c,1+b/2),b*q)
# Mixed x,y terms and a nonzero vertical observer velocity exercise cancellations
# missing from the univariate boundary family. These tests use E directly from Z.
polys=[3*x+2*x*y-s.Rational(2,3)*x**3,
 2*x+3*x*y-x**3/6+s.Rational(2,5)*x*y*y+x**3*y/7,
 -x+4*x*y+x**3/3+x*y**3/5-x**5/11+x**3*y*y/13]
for i,psi in enumerate(polys):
    v=calc(psi); w1,w2,F,J,D,Z,E,th,t=[v[n] for n in ['w1','w2','F','J','D','Z','E','th','t']]
    eq(f'mixed{i} divergence',s.diff(w1,x)+s.diff(w2,y),2*b)
    eq(f'mixed{i} primitive derivative',s.diff(th,x),F)
    eq(f'mixed{i} first identity',s.diff(t,x),J*s.diff(th,y)-D)
    eq(f'mixed{i} corrected second identity',k*J*th,Z-J*t+w2*s.diff(t,x))
    rhs=J**2*s.diff(t,y)-J*w2*s.diff(t,x,y)+(w2*s.diff(J,y)+J*(k-s.diff(w2,y)))*s.diff(t,x)
    eq(f'mixed{i} compatibility identity',E,rhs)
    mu=s.cancel(s.diff(t,x)/J); nu=t-w2*mu
    eq(f'mixed{i} quotient identity x',s.diff(nu,x),-w2*s.diff(mu,x))
    eq(f'mixed{i} quotient identity y',E,J**2*(s.diff(nu,y)+k*mu))
    eq(f'mixed{i} axis t',t.subs(x,0))
    eq(f'mixed{i} parity t',t.subs(x,-x),t)
# Explicit negative control: the sign in the first proof draft fails here.
bad=s.expand((a['Z']-a['J']*a['t']-a['w2']*s.diff(a['t'],x)-k*a['J']*a['th']).subs({b:3,c:0,q:2,x:1,y:1}))
assert bad!=0
# The spectral boundary cannot use the bounded-ODE exclusion: v=k*y allows f=1.
eq('singular ODE boundary bounded mode',(k*y)*s.diff(s.Integer(1),y)+(k-k)*s.Integer(1))
delta=s.symbols('delta',positive=True)
eq('linear singular ODE indicial exponent',delta*(k/delta-1)+delta-k)
out={'utc':datetime.now(timezone.utc).isoformat(),'method':'exact SymPy polynomial differentiation, direct E from Z, no numerical fitting code',
 'controls':rows,'negative_controls':[{'label':'original minus sign rejected','residual':str(bad),'passed':True}],
 'all_passed':all(r['passed'] for r in rows),'elapsed_seconds':time.monotonic()-started,
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path(sys.argv[1]); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_passed':out['all_passed'],'exact_controls':len(rows),'negative_controls':1,'elapsed_seconds':out['elapsed_seconds']},indent=2))
