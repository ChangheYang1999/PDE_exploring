#!/usr/bin/env python3
"""Independent exact local algebra and Gaussian reflected-moment quadrature."""
from pathlib import Path
from datetime import datetime,timezone
import time
import numpy as np
import sympy as S
from scipy.special import roots_legendre
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]

def reflected_gaussian_integral(target,n):
    """Positive-z source integral of (z-target) rho^-5 r^3 eta.

    Target-centered coordinates cancel the apparent kernel singularity.
    eta=z*(14-4*(r*r+z*z))*exp(-r*r-z*z).
    """
    g,weights=roots_legendre(n);total=0.
    intervals=[(0.,abs(target)),(abs(target),12.)]
    for lo,hi in intervals:
        if hi<=lo:continue
        rho=lo+(g+1)*(hi-lo)/2;rw=weights*(hi-lo)/2
        lower=np.maximum(-1.,-target/rho)
        active=lower<1
        rho=rho[active];rw=rw[active];lower=lower[active]
        mu=lower[:,None]+(g[None,:]+1)*(1-lower[:,None])/2
        mw=weights[None,:]*(1-lower[:,None])/2
        z=target+rho[:,None]*mu
        radius2=rho[:,None]**2+target**2+2*target*rho[:,None]*mu
        eta=z*(14-4*radius2)*np.exp(-radius2)
        total+=np.sum(rw[:,None]*mw*mu*(1-mu*mu)*eta)
    return float(total)

def main():
    wall=time.perf_counter();cpu=time.process_time();rows=[]
    def exact(name,value):
        value=S.factor(value)
        if value!=0:raise AssertionError((name,value))
        rows.append(dict(name=name,passed=True,method='exact symbolic identity'))
    def near(name,value,tol):
        error=float(np.max(np.abs(value)))
        if not np.isfinite(error) or error>tol:raise AssertionError((name,error,tol))
        rows.append(dict(name=name,passed=True,error=error,tolerance=tol))
    z,s,c,k,mu,K,Q=S.symbols('z s c k mu K Q',positive=True)
    delta=1+c;f=S.Function('f')(s);a=S.Function('A')(s);e=S.Function('E')(s)
    h=2*s*(c-f);b=c+2*f+2*s*S.diff(f,s)
    exact('equatorial ratio logarithmic derivative',(-(delta+(k-1)*b)+(1-2*f+k*b))/h-S.diff(f,s)/(c-f))
    ratio=K*(3*c+mu)/(mu*(c-f))
    exact('equatorial ratio at saddle',ratio.subs(f,-(c+mu)/2)-2*K/mu)
    exact('particular Poisson coefficient',-S.diff(-e*z**(k+1)/(k*(k+1)),z,2)-e*z**(k-1))
    exact('T3 indicial identity',(-mu*k+mu+delta).subs(mu,delta/(k-1)))
    nu,j=S.symbols('nu j',positive=True)
    exact('T2 indicial identity',(-2*nu*j+delta).subs(nu,delta/(2*j)))
    a1=-4*K*Q/(mu*k*(k+1));b1=-a1/(mu*k)
    a2=(a1*a1*k*(k+1)+4*Q*Q-4*K*Q*b1)/(mu*2*k*(2*k+1))
    exact('first eta coefficient',-mu*a1*k*(k+1)-4*K*Q)
    exact('first swirl correction',-mu*k*b1-a1)
    exact('second eta coefficient',-mu*a2*2*k*(2*k+1)+a1*a1*k*(k+1)+4*Q*Q-4*K*Q*b1)
    sub={c:S.Rational(3,5),k:S.Rational(5,2),mu:S.Rational(16,15),K:1,Q:1}
    exact('reported q coefficient',b1.subs(sub)-S.Rational(9,56))
    exact('reported first phi coefficient',a1.subs(sub)/2+S.Rational(3,14))
    exact('reported second phi coefficient',a2.subs(sub)/2-S.Rational(139,1792))
    # Check residuals through the stated orders without using the coefficient identities.
    for cv,kv in [(S.Rational(3,5),S.Rational(5,2)),(S.Rational(7,10),S.Rational(7,3)),(S.Rational(37,50),S.Integer(4))]:
        mv=(1+cv)/(kv-1);d=int(S.denom(kv));n=int(S.numer(kv));x=S.symbols('x',positive=True)
        values={c:cv,k:kv,mu:mv,K:S.Rational(3,2),Q:S.Rational(4,3)}
        av=a1.subs(values);bv=b1.subs(values);dv=a2.subs(values)
        ww=-mv*x**d+av*x**(n+d)+dv*x**(2*n+d)
        qq=values[Q]*x**n*(1+bv*x**n)
        def dz(v):return S.diff(v,x)/(d*x**(d-1))
        rq=S.expand(ww*dz(qq)-(dz(ww)-(1+cv))*qq)
        re=S.expand(ww*dz(dz(ww))+4*qq*(qq-values[K]))
        for order in [n,2*n]:
            exact(f'polynomial q residual c{cv} k{kv} power{order}',rq.coeff(x,order))
            exact(f'polynomial eta residual c{cv} k{kv} power{order}',re.coeff(x,order))
    # An axis-only counterexample to the unqualified finite-part assertion.
    kv=S.Rational(5,2);cv=S.Rational(3,5);mv=(1+cv)/(kv-1)
    qq=Q*z**kv;ww=-mv*z+mv*z**kv
    exact('axis-only swirl equation',ww*S.diff(qq,z)-(S.diff(ww,z)-(1+cv))*qq)
    et=2*qq*(qq-Q)/ww
    exact('axis-only eta equation',ww*S.diff(et,z)+(1+cv)*et-2*qq*S.diff(qq,z))
    exact('axis-only source derivative',S.diff(ww,z).subs(z,1)-(1+cv))
    exact('axis-only finite-part integrand',Q/qq-z**(-kv))
    # Pressure equivalence for arbitrary one-dimensional F and q, reduced only
    # by their actual ODEs. A direct Cartesian curl-free argument is unnecessary.
    F=S.Function('F')(z);q=S.Function('q')(z);w=c*z+2*F
    Cr=S.diff(F,z)-S.diff(F,z)**2+w*S.diff(F,z,2)+q*q
    exact('constant radial pressure derivative',S.diff(Cr,z)-((1+c)*S.diff(F,z,2)+w*S.diff(F,z,3)+2*q*S.diff(q,z)))
    exact('radial primitive cancellation',-S.diff(F,z)+S.diff(F,z)**2-w*S.diff(F,z,2)-q*q+Cr)
    exact('azimuthal primitive versus axis equation',(1-2*S.diff(F,z))*q+w*S.diff(q,z)-(w*S.diff(q,z)-(S.diff(w,z)-(1+c))*q))
    r,Z=S.symbols('r Z',positive=True)
    minus=(r*r+(z-Z)**2)**(-S.Rational(3,2));plus=(r*r+(z+Z)**2)**(-S.Rational(3,2))
    correct=(z-Z)*(r*r+(z-Z)**2)**(-S.Rational(5,2))+(z+Z)*(r*r+(z+Z)**2)**(-S.Rational(5,2))
    old=(z-Z)*(r*r+(z-Z)**2)**(-S.Rational(5,2))-(z+Z)*(r*r+(z+Z)**2)**(-S.Rational(5,2))
    exact('reflected target derivative plus sign',S.diff(minus-plus,Z)/3-correct)
    exact('old kernel exact discrepancy',correct-old-2*(z+Z)*(r*r+(z+Z)**2)**(-S.Rational(5,2)))
    exact('central kernel normalization',correct.subs(Z,0)-2*z*(r*r+z*z)**(-S.Rational(5,2)))
    quadratures=[]
    for target in [.5,1.,1.75]:
        records=[]
        expected=4/3*(1-2*target*target)*np.exp(-target*target)
        for nquad in [48,72,112]:
            Iplus=reflected_gaussian_integral(target,nquad);Iminus=reflected_gaussian_integral(-target,nquad)
            value=Iplus+Iminus;oldvalue=Iplus-Iminus
            near(f'Gaussian reflected moment Z{target} N{nquad}',value-expected,2e-11)
            records.append(dict(nquad=nquad,correct=value,old_wrong_kernel=oldvalue,expected=expected,error=value-expected))
        near(f'Gaussian moment refinement Z{target}',records[-1]['correct']-records[0]['correct'],2e-11)
        if abs(records[-1]['old_wrong_kernel']-expected)<1e-3:raise AssertionError('old kernel test not discriminating')
        quadratures.append(dict(target=target,records=records))
    record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,case_count=len(rows),rows=rows,quadratures=quadratures,
        wall_seconds=time.perf_counter()-wall,cpu_seconds=time.process_time()-cpu,
        source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in [Path(__file__),ROOT.parent/'research/finite_regularity/PROOF.md'] if p.is_relative_to(ROOT)})
    record['proof_sha256']=sha256(ROOT.parent/'research/finite_regularity/PROOF.md')
    atomic_json(ROOT/'results/finite_regularity_tests.json',record)
    atomic_json(ROOT.parent/'research/finite_regularity/verification/tests.json',record)
    print(dict(all_passed=True,case_count=len(rows),wall_seconds=record['wall_seconds'],cpu_seconds=record['cpu_seconds']),flush=True)
if __name__=='__main__':main()
