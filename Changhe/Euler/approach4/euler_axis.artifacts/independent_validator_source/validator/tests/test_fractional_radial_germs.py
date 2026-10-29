"""Exact checks of local annular fields and formal radial recurrences."""
from pathlib import Path
import datetime, json, time
import sympy as S
from independent_artifacts import atomic_json, sha256
ROOT=Path(__file__).resolve().parents[1]


def main():
    start=time.perf_counter();rows=[]
    def exact(name,value):
        value=S.factor(value)
        if value!=0:raise AssertionError((name,value))
        rows.append({'name':name,'passed':True,'remainder':'0'})
    c,nu,j,p,rho=S.symbols('c nu j p rho',positive=True)
    delta=1+c;a=2*c-1;Lam=3*c+2*nu
    relation=2*(p-1)+(3*c*p-a)/nu
    exact('general saddle indicial relation',(-nu*rho+Lam*p+1-2*(c+nu)).subs(rho,relation))
    exact('simple odd saddle exponent',relation.subs(p,1)-delta/nu)
    n=S.symbols('n',integer=True,nonnegative=True);P=2*j+1
    D=a+2*nu-2*nu*n*P
    exact('eta divisor at first higher order',D.subs(n,1).subs(nu,delta/(2*j))+3)
    tau=(delta+Lam)/(2*nu);s,z,ell,s0=S.symbols('s z ell s0',positive=True)
    phi_h=-z*s**(tau+1)/(4*(tau+1)*(tau+2))
    exact('homogeneous eta radial inverse',-4*s*S.diff(phi_h,s,2)-8*S.diff(phi_h,s)-z*s**tau)
    # Direct finite-order coupled solves. New f is obtained from eta, then a from q.
    x=S.symbols('x',positive=True)
    for cv,jv in [(S.Rational(3,5),S.Rational(3,4)),(S.Rational(17,25),S.Rational(4,5)),(S.Rational(37,50),S.Rational(3,2))]:
        dv=1+cv;nv=dv/(2*jv);pv=2*jv+1;av=S.Rational(3,2)
        F=cv+nv;A=S.Integer(1)
        coeffs=[]
        for order in range(3):
            fnew=S.symbols('fnew');Ftrial=F+fnew*x**(order+1)
            H=-4*pv*((pv+1)*S.diff(Ftrial,x)+pv*x*S.diff(Ftrial,x,2))
            eta=2*(cv-Ftrial)*((pv-1)*H+pv*x*S.diff(H,x))+(1+2*cv+2*Ftrial+2*pv*x*S.diff(Ftrial,x))*H-2*av**2*A**2
            solved=S.solve(S.expand(eta).coeff(x,order),fnew)
            if len(solved)!=1:raise AssertionError('eta recurrence nonunique')
            F=S.expand(Ftrial.subs(fnew,solved[0]));coeffs.append(str(solved[0]))
            anew=S.symbols('anew');Atrial=A+anew*x**(order+1)
            rq=2*(cv-F)*(jv*Atrial+pv*x*S.diff(Atrial,x))+(dv+2*pv*x*S.diff(F,x))*Atrial
            solved_a=S.solve(S.expand(rq).coeff(x,order+1),anew)
            if len(solved_a)!=1:raise AssertionError('q recurrence nonunique')
            A=S.expand(Atrial.subs(anew,solved_a[0]))
        H=-4*pv*((pv+1)*S.diff(F,x)+pv*x*S.diff(F,x,2))
        re=2*(cv-F)*((pv-1)*H+pv*x*S.diff(H,x))+(1+2*cv+2*F+2*pv*x*S.diff(F,x))*H-2*av**2*A**2
        rq=2*(cv-F)*(jv*A+pv*x*S.diff(A,x))+(dv+2*pv*x*S.diff(F,x))*A
        for order in range(3):
            exact(f'coupled eta c={cv} j={jv} order={order}',S.expand(re).coeff(x,order))
            exact(f'coupled q c={cv} j={jv} order={order}',S.expand(rq).coeff(x,order))
        rows.append({'name':f'formal coefficients c={cv} j={jv}','passed':True,'f_coefficients':coeffs})
    d=c-ell/2;b=ell*s0/2;phi=z*(d+b/s)
    hs=2*s*(c-S.diff(phi,z));w=c*z+2*phi+2*s*S.diff(phi,s)
    exact('annular radial drift',hs-ell*(s-s0))
    exact('annular axial drift',w-(3*c-ell)*z)
    exact('annular elliptic identity',4*s*S.diff(phi,s,2)+8*S.diff(phi,s)+S.diff(phi,z,2))
    G=S.Function('G')(s);q=G/s
    rq=q+hs*S.diff(q,s)-2*S.diff(phi,z)*q
    exact('annular q versus circulation',rq-(ell*(s-s0)*S.diff(G,s)-a*G)/s)
    C=S.symbols('C')
    for sign in [1,-1]:
        gg=C*(sign*(s-s0))**p
        exact(f'annular circulation branch {sign}',ell*(s-s0)*S.diff(gg,s)-ell*p*gg)
    r=S.symbols('r',positive=True);gg=S.Function('Gamma')(r)
    ur=-d*r-b/r;uz=2*d*z;ut=gg/r;wr=c*r+ur;wz=c*z+uz
    mr=(1-c)*ur+wr*S.diff(ur,r)-ut**2/r
    mz=(1-c)*uz+wz*S.diff(uz,z)
    exact('annular radial primitive',mr-((d*d-d)*r+a*b/r-(b*b+gg*gg)/r**3))
    exact('annular axial primitive',mz-2*d*(1+2*d)*z)
    Pr=(d-d*d)*r-a*b/r+(b*b+gg*gg)/r**3;Pz=-2*d*(1+2*d)*z
    exact('annular radial pressure cancellation',mr+Pr)
    exact('annular axial pressure cancellation',mz+Pz)
    mt=(1-c)*ut+wr*S.diff(ut,r)+ur*ut/r
    exact('annular swirl cancellation',mt-(wr*S.diff(gg,r)-a*gg)/r)
    # Vertical odd background and leading eta coefficient.
    bs=3*c-ell;F0=(ell-c)/2+bs/(2*s);ph0=z*F0
    exact('vertical background radial drift',2*s*(c-S.diff(ph0,z))-bs*(s-1))
    exact('vertical background axial drift',c*z+2*ph0+2*s*S.diff(ph0,s)-ell*z)
    exact('vertical background elliptic',4*s*S.diff(ph0,s,2)+8*S.diff(ph0,s)+S.diff(ph0,z,2))
    E=S.Function('E')(s);ph1=-E*z**(2*p+1)/(2*p*(2*p+1))
    exact('leading odd potential coefficient',-S.diff(ph1,z,2)-E*z**(2*p-1))
    record={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_passed':True,'case_count':len(rows),
            'rows':rows,'wall_seconds':time.perf_counter()-start,
            'source_sha256':sha256(Path(__file__)),'proof_sha256':sha256(ROOT.parent/'research/fractional_radial_germs/PROOF.md')}
    atomic_json(ROOT/'results/fractional_radial_germ_tests.json',record)
    atomic_json(ROOT.parent/'research/fractional_radial_germs/verification/tests.json',record)
    print(json.dumps({'all_passed':True,'case_count':len(rows),'wall_seconds':record['wall_seconds']}))


if __name__=='__main__':main()
