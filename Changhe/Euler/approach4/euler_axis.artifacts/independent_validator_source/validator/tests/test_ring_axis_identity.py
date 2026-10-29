#!/usr/bin/env python3
"""Independent symbolic and high-precision checks of the outgoing axis identity."""
from pathlib import Path
import time
import sympy as sp
import mpmath as mp
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[]
    def check(name,error,tol=0):
        e=float(abs(error))
        if e>tol:raise AssertionError((name,e,tol))
        rows.append(dict(name=name,error=e,tolerance=float(tol)))
    c,w,wp,Q,J=sp.symbols('c w wp Q J',nonzero=True)
    delta=1+c;lam=1+4*c;kap=1+7*c;a=2*c-1
    qp=(2*wp-lam)*Q/w;jp=(2*Q*qp-(kap-2*wp)*J)/w;Y=w*J/Q**2
    yp=wp*J/Q**2+w*jp/Q**2-2*w*J*qp/Q**3
    check('Y exact identity',sp.simplify(w*yp+(wp-delta)*Y-4*wp+2*lam))
    check('shifted Y constant',sp.expand(4*delta-2*lam+2*a))
    check('origin eta divisor',sp.expand(lam+kap-2*lam-3*c))
    s=sp.symbols('s');f,fp,g,gp,h,hp,q2,q2p,q0,q0p,e0,e0p,e1,e1p=sp.symbols('f fp g gp h hp q2 q2p q0 q0p e0 e0p e1 e1p')
    # Independent expansion, with q0=eta0=eta_s=0 already established.
    ws=2*s*(c-(wp-c)/2-s*gp-s*s*hp);wz=w+4*s*g+6*s*s*h
    q=s*Q+s*s*q2;qz=s*sp.Symbol('Qp')+s*s*q2p
    eta=s*s*J;etaz=s*s*sp.Symbol('Jp')
    rq=sp.expand((1-2*((wp-c)/2+s*gp+s*s*hp))*q+ws*sp.diff(q,s)+wz*qz)
    re=sp.expand(delta*eta+ws*sp.diff(eta,s)+wz*etaz-2*q*qz)
    check('coefficient s in q',sp.simplify(rq.coeff(s,1)-(w*sp.Symbol('Qp')+(lam-2*wp)*Q)))
    check('coefficient s2 in eta',sp.simplify(re.coeff(s,2)-(w*sp.Symbol('Jp')+(kap-2*wp)*J-2*Q*sp.Symbol('Qp'))))
    mp.mp.dps=60
    for cs in ['0.505','0.56','0.60','0.6666666666666666666666666666666666666666666666667','0.72','0.74']:
        cc=mp.mpf(cs);ll=1+4*cc;dd=1+cc;aa=2*cc-1;tt=cc/ll;hh=(ll-cc)/(2*cc*ll)
        A=(1-dd/ll)/2;B=1/(2*cc);I0=mp.beta(A,B)/(2*tt**A);Inorm=tt**(dd*hh)*I0
        def ww(z):return z*(ll+cc*z*z)/(1+z*z)
        def tau0(z):return mp.log(z)/ll+hh*mp.log1p(tt*z*z)
        def qq(z):return ww(z)**2/ll**2*mp.exp(-ll*tau0(z))
        def partial(z):return mp.betainc(A,B,0,tt*z*z/(1+tt*z*z))/(2*tt**A)
        def yy(z):return 4-2*aa*partial(z)/(ww(z)*mp.exp(-dd*tau0(z)))
        def jj(z):return yy(z)*qq(z)**2/ww(z)
        for zs in ['0.001','0.03','0.3','1','3','10','100']:
            z=mp.mpf(zs);wv=ww(z);d=mp.diff(ww,z);qv=qq(z);qv1=mp.diff(qq,z);jv=jj(z);jv1=mp.diff(jj,z)
            check(f'{cs} {zs} q ODE',(wv*qv1-(2*d-ll)*qv)/(1+abs(qv)),mp.mpf('1e-48'))
            check(f'{cs} {zs} eta ODE',(wv*jv1+(1+7*cc-2*d)*jv-2*qv*qv1)/(1+abs(jv)),mp.mpf('1e-48'))
        # Singular endpoint removed by z=t^(1/(1-delta/lambda)).
        exponent=1/(1-dd/ll)
        direct=mp.quad(lambda t:mp.exp(-dd*tau0(t**exponent))*exponent*t**(exponent-1),[0,mp.mpf('.1'),1])
        check(f'{cs} incomplete beta vs quadrature',(partial(mp.mpf(1))-direct)/direct,mp.mpf('1e-40'))
        z=mp.mpf('1e-7')
        check(f'{cs} origin Q',qq(z)/z-1,mp.mpf('1e-12'))
        check(f'{cs} origin J',jj(z)/z-2/(3*cc),mp.mpf('1e-12'))
        b1=tt**(-(1-cc)/(2*cc));d2=-2*aa*b1*b1*Inorm/(cc*cc);z=mp.mpf('1e9')
        check(f'{cs} far Q',qq(z)*z**(2+1/cc)/b1-1,mp.mpf('1e-14'))
        check(f'{cs} far J',jj(z)*z**(5+1/cc)/d2-1,mp.mpf('1e-10'))
        if not (jj(mp.mpf('1e-3'))>0 and jj(z)<0):raise AssertionError('sign reversal')
        rows.append(dict(name=f'{cs} sign reversal',B1=str(b1),D2=str(d2),I=str(Inorm)))
    atomic_json(ROOT/'results/ring_axis_identity_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
