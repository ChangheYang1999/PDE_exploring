#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
import sympy as sp
import torch
from independent_second_order import second_forcing
from independent_farfield import asymptotic_fixture
from independent_pressure import GreenPoisson
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def symbolic():
    x=sp.symbols('mu');a=sp.Rational(2,3);s=1-x*x
    A=sp.Rational(21,50)-sp.Rational(23,100)*x-sp.Rational(1,25)*x*x
    B=sp.Rational(17,50)+sp.Rational(19,100)*x+sp.Rational(13,100)*x*x
    fr=2*x*A-s*sp.diff(A,x);c=(a-2)*A
    def conv(F,G,beta):
        f,c,b=F;g,d,h=G
        return [-beta*f*g-s*c*sp.diff(g,x)-s*(c*d+b*h),
                -beta*f*d+c*(x*d-s*sp.diff(d,x))+c*g-x*b*h,
                -beta*f*h+c*(x*h-s*sp.diff(h,x))+b*g+x*b*d]
    F=[fr,c,B];N=conv(F,F,a)
    src=sp.expand((1-2*a)*N[0]-sp.diff(s*N[1],x))
    degree=sp.degree(src,x)
    modes=[sp.factor(sp.Rational(2*l+1,2)*sp.integrate(src*sp.legendre(l,x),(x,-1,1))) for l in range(degree+1)]
    Q=sum(modes[l]/(l*(l+1)-2*a*(2*a-1))*sp.legendre(l,x) for l in range(len(modes)))
    G=[N[0]-2*a*Q,N[1]-sp.diff(Q,x),N[2]]
    N2=[sp.expand(u+v) for u,v in zip(conv(F,G,2*a+1),conv(G,F,a))]
    src2=sp.expand(-3*a*N2[0]-sp.diff(s*N2[1],x))
    f2=sp.factor(sp.Rational(5,2)*sp.integrate(src2*sp.legendre(2,x),(x,-1,1)))
    data=second_forcing(float(a),[.42,-.23,-.04],[.34,.19,.13])
    check('nonzero_second_quadrupole_exact',0 if f2!=0 else 1,0,{'source_coefficient':str(f2),'pressure_log_coefficient':str(f2/5)})
    check('second_quadrupole_exact_vs_float',abs(float(f2)-data['source_legendre'][2]),1e-12)
    return str(f2)


def cartesian():
    torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
    points=np.array([[.4,.3,.8],[1.1,-.7,-.4],[.2,.5,-1.3]])
    Rnp=np.linalg.norm(points,axis=1);mu=points[:,2]/Rnp
    for a in [.5,2/3,1.]:
        data=second_forcing(a,[.42,-.23,-.04],[.34,.19,.13]);first=data['first']
        xyz=torch.tensor(points,requires_grad=True);x,y,z=xyz.unbind(-1)
        s=x*x+y*y;R=torch.sqrt(s+z*z);m=z/R
        def scalar(poly,beta):return R**(-beta)*sum(float(v)*m**i for i,v in enumerate(poly.coef))
        def vel(A,B,beta):
            phi=scalar(A,beta);q=scalar(B,beta+1)
            ps=torch.autograd.grad(phi.sum(),s,create_graph=True,retain_graph=True)[0]
            pz=torch.autograd.grad(phi.sum(),z,create_graph=True,retain_graph=True)[0]
            return torch.stack((-x*pz-y*q,-y*pz+x*q,2*phi+2*s*ps),dim=-1)
        F=vel(first['A'],first['B'],a);G=vel(first['A1'],first['B1'],2*a+1)
        def jac(v):return torch.stack([torch.autograd.grad(v[:,i].sum(),xyz,create_graph=True,retain_graph=True)[0] for i in range(3)],dim=1)
        cross=(jac(F)@G[...,None]+jac(G)@F[...,None])[...,0].detach().numpy()
        er=points/Rnp[:,None];rho=np.linalg.norm(points[:,:2],axis=1)
        az=np.stack((-points[:,1]/rho,points[:,0]/rho,np.zeros_like(rho)),axis=-1);polar=np.cross(az,er)
        frame=np.stack((er,polar,az),axis=1)
        actual=np.einsum('nij,nj->ni',frame,cross)*Rnp[:,None]**(3*a+2)
        expected=np.stack((data['N'][0](mu),np.sqrt(1-mu*mu)*data['N'][1](mu),np.sqrt(1-mu*mu)*data['N'][2](mu)),axis=-1)
        check(f'cross_advection_cartesian_alpha{a}',np.max(np.abs(actual-expected)),2e-13)


def global_log():
    a=2/3;field,first=asymptotic_fixture(a,True,True)
    data=second_forcing(a,first['A'],first['B']);expected=data['resonant_log_coefficients'][2]
    radii=np.array([32.,128.,512.,2048.,8192.])
    psolver=GreenPoisson(field.source,decay_power=2*a,lmax=28,nangle=64,nradial=56)
    rem=np.array([R**3*(psolver.radial(R)[0][2]-R**(-2*a)*first['Qmode'][2]) for R in radii])
    slopes=np.diff(rem)/np.diff(np.log(radii))
    check('global_pressure_quadrupole_log_slope',abs(slopes[-1]-expected),2e-5,
          {'radii':radii.tolist(),'scaled_remainders':rem.tolist(),'log_slopes':slopes.tolist(),'expected':expected})


def main():
    start=time.time();exception=None
    try:symbolic();cartesian();global_log()
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_second_order.py',ROOT/'src/independent_farfield.py',ROOT/'src/independent_pressure.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'checks':checks,'exception':exception,
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/second_order_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
