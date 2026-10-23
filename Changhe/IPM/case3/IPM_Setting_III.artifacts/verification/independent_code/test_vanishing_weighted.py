"""Independent symbolic strain and radial/angle weighted manufactured checks."""
import json, math
from pathlib import Path
from datetime import datetime, timezone
import sympy as sp
import numpy as np
import mpmath as mp

out=Path('research/vanishing_weighted_limit/verification/checks.json')
x,y,t,a,D,e=sp.symbols('x y t a D e', real=True)
f=sp.Function('f')(t);b=sp.Function('b')(t)
Dx=lambda v:sp.diff(v,x)+2*x*sp.diff(v,t)
Dy=lambda v:sp.diff(v,y)+2*y*sp.diff(v,t)
psi=-a*x*y*b
u1=-Dy(psi);u2=Dx(psi)
reductions={sp.diff(b,t,2):sp.diff(f,t)/(2*t)-6*(f-4*b)/(4*t*t),sp.diff(b,t):(f-4*b)/(2*t)}
def reduced(v):return sp.factor(v.subs(reductions,simultaneous=True))
def zero(name,v):
    z=sp.factor(v.subs(t,x*x+y*y))
    assert z==0,(name,z)
    checks.append(name)
checks=[]
K=2*f+2*t*sp.diff(f,t);L=2*t*sp.diff(f,t)-6*f+24*b
zero('Cartesian S11 equals fourth-angle expression',reduced(Dx(u1))-a*(K-L*(x**4-6*x*x*y*y+y**4)/t**2)/8)
zero('Cartesian S12 equals fourth-angle expression',reduced((Dy(u1)+Dx(u2))/2)+a*L*x*y*(x*x-y*y)/(2*t**2))
zero('Cartesian divergence vanishes',Dx(u1)+Dy(u2))
zero('Poisson equation',reduced(-Dx(Dx(psi))-Dy(Dy(psi)))-Dx(a*y*f))
zero('Radial velocity compression',reduced(x*u1+y*u2)-a*(x*x-y*y)*b)
rho=a*y*f
R=(1+D)*(x*Dx(rho)+y*Dy(rho))+u1*Dx(rho)+u2*Dy(rho)-rho
R=reduced(R).subs(sp.diff(f,t),-e*f/(2*(1+t))).subs(a,4*D)
expected=4*D**2*y*f*(1/(1+t)-4*b-4*x*x/t*(f-4*b)-4*e*(x*x-y*y)*b/(1+t))
zero('Direct transport residual', (R-expected).subs(e,D/(1+D)))
B0=1/(1+t)+(-4+4*e)*b-4*e*b/(1+t)
B2=-8*sp.diff(b,t)-8*e*b/(1+t)
zero('Smooth residual bracket',reduced(B0+x*x*B2)-(1/(1+t)-4*b-4*x*x/t*(f-4*b)-4*e*(x*x-y*y)*b/(1+t)))
th=sp.symbols('theta',real=True)
for k,expected_ang in [(0,sp.pi),(1,sp.pi/4),(2,sp.pi/8)]:
    actual=sp.integrate(sp.sin(th)**2*sp.cos(th)**(2*k),(th,0,2*sp.pi))
    assert sp.simplify(actual-expected_ang)==0
    checks.append('Exact angular moment '+str(k))
mp.mp.dps=60
I=mp.quad(lambda z:mp.log1p(z)**2/z**2,[0,1,mp.inf])
assert abs(I-mp.pi**2/3)<mp.mpf('1e-55')
exact_norms={'G_squared':'2*pi^3/3','J_squared':'8*pi','ratio_limit':'2*sqrt(3)/pi','log_radial_integral_mp60':str(I)}

def scalar(tval,eta):
    nu=eta/2
    logp=mp.log1p(tval)
    fm1=mp.expm1(-nu*logp);fv=1+fm1
    if tval<mp.mpf('.04'):
        # Independent binomial integration of integral_0^1 u^3 f(ur)du.
        term=mp.mpf(1);hv=mp.mpf(1)/4
        for k in range(1,100):
            term*=-(nu+k-1)*tval/k
            inc=term/(2*(k+2));hv+=inc
            if abs(inc)<mp.mpf('1e-65'):break
    else:
        hv=(mp.expm1((2-nu)*logp)/(2-nu)-mp.expm1((1-nu)*logp)/(1-nu))/(2*tval*tval)
    hp=(fv-4*hv)/(2*tval)
    return fv,fm1,hv,hp

rows=[]
# Exact angular integration followed by independently implemented Gauss-Legendre
# integration on log-radius [-18,18], split into six intervals.
for n in (32,64,128):
    nodes,weights=np.polynomial.legendre.leggauss(n)
    for Dstr in ('1','.3','.1','.03','.01','.003','.001','.0003','.0001'):
        dv=mp.mpf(Dstr);eta=dv/(1+dv);gn=mp.mpf(0);fn=mp.mpf(0)
        for lo,hi in zip((-18,-12,-6,0,6,12),(-12,-6,0,6,12,18)):
            for nd,wt in zip(nodes,weights):
                log_r=mp.mpf(str((lo+hi)/2+(hi-lo)*nd/2));wgt=mp.mpf(str(wt*(hi-lo)/2))
                tv=mp.exp(2*log_r);fv,fm1,hv,hp=scalar(tv,eta)
                B0v=1/(1+tv)+(-4+4*eta)*hv-4*eta*hv/(1+tv)
                tB2=tv*(-8*hp-8*eta*hv/(1+tv))
                gn+=wgt*16*mp.pi/tv*(fm1/dv)**2
                fn+=wgt*16*mp.pi/tv*fv**2*(B0v*B0v+B0v*tB2/2+tB2*tB2/8)
        rows.append({'nodes_per_panel':n,'D':Dstr,'h_over_D2_norm_squared':str(gn),'F_over_D2_norm_squared':str(fn),'ratio':str(mp.sqrt(fn/gn))})
# These are convergence checks, never interval enclosures of the infinite integral.
for Dstr in ('1','.3','.1','.03','.01','.003','.001','.0003','.0001'):
    rr=[r for r in rows if r['D']==Dstr]
    rel=abs(mp.mpf(rr[-1]['ratio'])-mp.mpf(rr[-2]['ratio']))/mp.mpf(rr[-1]['ratio'])
    assert rel<mp.mpf('2e-10'),(Dstr,rel)
ratio=mp.mpf(rows[-1]['ratio']);limit=2*mp.sqrt(3)/mp.pi
assert abs(ratio-limit)<mp.mpf('.001')
# Additional global-strain formula samples are supporting diagnostics, not a proof.
strain=[]
for Dstr in ('1','.1','.001'):
    dv=mp.mpf(Dstr);eta=dv/(1+dv);ratios=[];lowestL=mp.inf
    for logr in np.linspace(-12,12,241):
        tv=mp.exp(2*mp.mpf(str(logr)));fv,_,hv,_=scalar(tv,eta)
        rf=-eta*tv/(1+tv)*fv
        Lv=rf-6*fv+24*hv;Kv=2*fv+rf
        lowestL=min(lowestL,Lv)
        sigma_over_D=(abs(Kv)+abs(Lv))/2
        assert Lv>=-mp.mpf('1e-45')
        assert sigma_over_D<=1+mp.mpf('1e-45')
        ratios.append(sigma_over_D)
    strain.append({'D':Dstr,'sampled_sigma_over_D_max':str(max(ratios)),'sampled_L_min':str(lowestL)})
payload={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'limiting_norms':exact_norms,'finite_D_rows':rows,'strain_samples':strain,'scope':'Analytic proof controls strain globally and establishes weighted dominated convergence. MP quadrature uses finite log-radius [-18,18]; its reported digits are supporting samples, not interval enclosures. No producer code or fitted velocity.'}
out.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'quadrature_rows':len(rows),'last_ratio':str(ratio),'limit':str(limit)}))
