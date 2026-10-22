"""Own packet126 exact Cartesian tests, rational certificates and full inverse.

No lead or NUM code is read, imported or executed. The analytic proof precedes
this implementation. Numerical controls do not replace its global inequalities.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from time import monotonic
from math import factorial
import json,hashlib
import numpy as np
import sympy as sp
import mpmath as mp
import exact_bivariate as P
from cartesian_inverse import CartesianInverse,InverseSettings
root=Path('research/126_arbitrary_disk_anisotropic_realization/verification')
start=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','cases':[],'inverse':[],'compact_C3':[]}
x,y,L,e,h,p,B=sp.symbols('x y L e h p B',positive=True)
S=L*L+x*x+e*(y-h)**2;psi=-B*x*S**p
omega=-sp.diff(psi,x,2)-sp.diff(psi,y,2)
br=(3+e)*L*L+(1+2*p+e)*x*x+e*(3+(2*p-1)*e)*(y-h)**2
assert sp.simplify(omega-2*B*p*x*S**(p-2)*br)==0
out['general_anisotropic_Laplacian_identity']=True
# Independent rational bivariate expansion; no center moment identities.
def base(beta,q,ellL,N=8):
    beta,q,ellL=map(Q,(beta,q,ellL));cc=1+beta/2;pp=(beta-1)/(2*beta)
    kap=9*cc*cc/(beta*q*q);eta=kap/(ellL*ellL);dd=6*cc/q
    S0=(1+beta)*ellL*ellL;ell=-q*S0/(6*pp)
    assert 0<eta<=1
    T={(2,0):1/S0,(0,1):-dd/S0,(0,2):eta/S0}
    ps=P.scale(P.mul({(1,0):Q(1)},P.unit_power(T,pp,N),N),ell)
    ps.pop((1,0),None)
    pars=dict(beta=str(beta),q=str(q),a0=str(q*beta/4),L=str(ellL),eta=str(eta),
              h=str(dd/(2*eta)),S0=str(S0),p=str(pp),ell=str(ell),kappa=str(kap))
    return ps,pars

def elimination(beta,ps):
    N=8;W=(P.add({(1,0):beta},P.scale(P.diff(ps,1),-1)),P.add({(0,1):beta},P.diff(ps,0)))
    om=P.scale(P.lap(ps),-1);kk=beta-2
    f=P.add(P.dot_grad(W,om,N),om);j=P.diff(W[1],0)
    d=P.add(P.mul(P.add({(0,0):kk},P.scale(P.diff(W[0],0),-1)),f,N),P.scale(P.dot_grad(W,f,N),-1))
    z=P.add(P.mul(P.mul(W[0],f,N),j,N),P.mul(W[1],d,N))
    E=P.add(P.mul(j,P.diff(z,1),N),P.scale(P.mul(z,P.diff(j,1),N),-1),P.scale(P.mul(d,j,N),-kk))
    return E

for bs,qs,ls in [('4','1','6'),('9','1/2','20'),('3','2','3'),('5/2','3/7','20')]:
    beta,q,ll=map(Q,(bs,qs,ls));ps,pa=base(beta,q,ll);cc=1+beta/2;eta=Q(pa['eta']);mu=1+3*beta/2
    oo=P.scale(P.lap(ps),-1)
    assert ps[(1,1)]==cc and ps[(3,0)]==-q/6 and ps.get((1,2),0)==0
    assert oo[(1,0)]==q
    qp=cc*(3*(beta+1)+2*eta)/(beta*(beta+1)*ll*ll)
    assert oo[(1,1)]==qp>0
    ecoef=q*(2*beta+4)*mu*(2*beta+1)*qp
    E=elimination(beta,ps);assert E.get((2,1))==ecoef>0
    cert={'parameters':pa,'psi':P.serialize(ps),'Omega':P.serialize(oo),
          'E_through_degree3':P.serialize(P.trunc(E,3)),'qprime':str(qp),'E_x2y':str(ecoef)}
    path=root/f'base_b{bs.replace("/","_")}_L{ls}_certificate.json'
    path.write_text(json.dumps(cert,indent=2)+'\n');loaded=json.loads(path.read_text())
    # Separate Cartesian SymPy implementation differentiates exact serialized polynomials.
    sx,sy=sp.symbols('sx sy');ss=sum(sp.Rational(t['coefficient'])*sx**t['x_power']*sy**t['y_power']for t in loaded['psi'])
    beta_s=sp.Rational(bs);om=-sp.diff(ss,sx,2)-sp.diff(ss,sy,2)
    assert sp.diff(om,sx,sy).subs({sx:0,sy:0})==sp.Rational(loaded['qprime'])
    trunc=lambda t:sum(v*sx**ij[0]*sy**ij[1]for ij,v in sp.Poly(sp.expand(t),sx,sy).terms()if sum(ij)<=5)
    w1=beta_s*sx-sp.diff(ss,sy);w2=beta_s*sy+sp.diff(ss,sx);kk=beta_s-2
    f=trunc(w1*sp.diff(om,sx)+w2*sp.diff(om,sy)+om);j=sp.diff(w2,sx)
    d=trunc((kk-sp.diff(w1,sx))*f-w1*sp.diff(f,sx)-w2*sp.diff(f,sy))
    z=trunc(w1*f*j+w2*d);ee=trunc(j*sp.diff(z,sy)-z*sp.diff(j,sy)-kk*d*j)
    assert sp.Poly(ee,sx,sy).coeff_monomial(sx*sx*sy)==sp.Rational(loaded['E_x2y'])
    out['cases'].append({'parameters':pa,'qprime':str(qp),'E_x2y':str(ecoef),
        'exact_Cartesian_rational_agreement':True,'certificate':str(path),
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    print('exact case',bs,qs,ls,'E',ecoef,flush=True)
# General polynomial orbit, PDE and source condition, independently differentiated.
b,q,x0,y0,t=sp.symbols('beta q x0 y0 t',positive=True)
lam=(b-2)/2;mu=1+3*b/2;cc=1+b/2;kk=q/(2*(mu-2*lam))
xt=sp.exp(-lam*t)*x0;yt=sp.exp(-mu*t)*y0+kk*x0*x0*(sp.exp(-2*lam*t)-sp.exp(-mu*t))
assert sp.simplify(sp.diff(xt,t)+lam*xt)==0
assert sp.simplify(sp.diff(yt,t)+mu*yt-q*xt*xt/2)==0
spx,spy=sp.symbols('spx spy');ps=cc*spx*spy-q*spx**3/6;th=q*b*spx*spx/4
om=-sp.diff(ps,spx,2)-sp.diff(ps,spy,2);wx=b*spx-sp.diff(ps,spy);wy=b*spy+sp.diff(ps,spx)
assert sp.expand(wx*sp.diff(th,spx)+wy*sp.diff(th,spy)-(b-2)*th)==0
assert sp.expand(wx*sp.diff(om,spx)+wy*sp.diff(om,spy)+om-sp.diff(th,spx))==0
out['symbolic_polynomial_PDE_and_backward_orbit']=True
# Fixed-ball derivative comparison in a stable elementary expression, against
# the proven bound D_M/L^2. Sampled values are lower estimates of suprema only.
mp.mp.dps=50
for beta,q in [(mp.mpf(4),mp.mpf(1)),(mp.mpf('2.5'),mp.mpf('0.5'))]:
    cc=1+beta/2;pp=(beta-1)/(2*beta);kap=9*cc*cc/(beta*q*q);dd=6*cc/q;M=mp.mpf(2);H=M+1;C0=2+dd
    DM=q/6*(kap*H**3+2*C0**2*H**5/(1+beta))
    for ll in [mp.mpf(16),mp.mpf(32),mp.mpf(64)]:
        eta=kap/(ll*ll);S0=(1+beta)*ll*ll;ell=-q*S0/(6*pp)
        def err(xx,yy):
            T=xx*xx-dd*yy+eta*yy*yy
            return ell*xx*mp.expm1(pp*mp.log1p(T/S0))-(cc*xx*yy-q*xx**3/6)
        maximum=[]
        pts=[(mp.mpf('0.3'),mp.mpf('-0.7')),(mp.mpf('1.2'),mp.mpf('.8')),(mp.mpf('-1.1'),mp.mpf('-1.3')),(mp.mpf(0),mp.mpf('1.9'))]
        for i in range(4):
            for j in range(4-i):maximum.append(max(abs(mp.diff(err,pt,(i,j)))for pt in pts)/factorial(i)/factorial(j))
        sampled=sum(maximum);assert sampled<DM/(ll*ll)
        out['compact_C3'].append({'beta':str(beta),'q':str(q),'L':str(ll),'sampled_norm':float(sampled),
            'L2_times_sampled_norm':float(ll*ll*sampled),'proven_bound':float(DM/(ll*ll)),
            'points':[[float(a),float(b)]for a,b in pts],'precision_digits':50,
            'scope':'sampled derivative control; uniform bound proved analytically'})
# A separately implemented full-plane Duffy inverse applied to the analytic
# vorticity, compared with the exact relative stream velocity on three domains.
beta,q,ll=4.,1.,6.;cc=1+beta/2;pp=(beta-1)/(2*beta);eta=9*cc*cc/(beta*q*q*ll*ll)
hh=3*cc/(q*eta);S0=(1+beta)*ll*ll;ell=-q*S0/(6*pp)
def omega(xs,ys):
    st=ll*ll+xs*xs+eta*(ys-hh)**2;v=st/S0
    br=(3+eta)*ll*ll+(1+2*pp+eta)*xs*xs+eta*(3+(2*pp-1)*eta)*(ys-hh)**2
    return q/(3*S0)*xs*v**(pp-2)*br
pts=np.array([[0.,0.],[.25,-.4],[1.2,.7],[-1.,2.],[0.,-2.]])
xv,yv=pts[:,0],pts[:,1];z=(xv*xv-6*cc/q*yv+eta*yv*yv)/S0
u1=q/3*eta*xv*(yv-hh)*(1+z)**(pp-1)
u2=ell*np.expm1(pp*np.log1p(z))-q/3*xv*xv*(1+z)**(pp-1)
expected=np.column_stack([u1,u2])
for radius,order in [(8.,24),(14.,40),(22.,56)]:
    inv=CartesianInverse(omega,InverseSettings(radius=radius,core_radial_order=12,
        core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/beta))
    got=inv.relative(pts);error=float(np.max(abs(got-expected)))
    out['inverse'].append({'square_radius':radius,'angular_exterior_order':order,'maximum_absolute_error':error,'values':got.tolist()})
    print('inverse',radius,error,flush=True)
assert out['inverse'][-1]['maximum_absolute_error']<2e-7
out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-start,
    code_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),Path('code_independent/exact_bivariate.py'),Path('code_independent/cartesian_inverse.py')]})
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
