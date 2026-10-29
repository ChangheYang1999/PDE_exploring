#!/usr/bin/env python3
from pathlib import Path
import datetime,json,time,hashlib
import numpy as np
import sympy as sp
import torch
from independent_farfield import angular_data,evaluate_vector,pad
from independent_fields import manufactured_power
from independent_pressure import GreenPoisson

ROOT=Path(__file__).resolve().parents[1]
checks=[]

def check(name,error,tol,detail=None):
    row={'name':name,'error':float(error),'tolerance':tol,'passed':bool(np.isfinite(error) and error<=tol)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)


def symbolic():
    a,x=sp.symbols('alpha mu',real=True)
    A=sp.Rational(2,5)-x/3+x*x/7-x**3/11
    B=sp.Rational(3,7)+x/5-x*x/13
    S=1-x*x
    FR=2*x*A-S*sp.diff(A,x);C=(a-2)*A;Fz=x*FR-S*C
    NR=-a*FR**2-S*C*sp.diff(FR,x)-S*(C*C+B*B)
    V=(1-a)*FR*C+x*C*C-S*C*sp.diff(C,x)-x*B*B
    f=(1-2*a)*NR-sp.diff(S*V,x)
    mean=lambda expr:sp.integrate(sp.expand(expr),(x,-1,1))/2
    identities={
        'monopole_factor':sp.factor(mean(f)-(1-2*a)*mean(NR)),
        'dipole_factor':sp.factor(3*mean(x*f)-2*(1-a)*(3*mean(x*NR)-3*mean(FR*Fz))),
        'leading_divergence':sp.factor((2-a)*FR-sp.diff(S*C,x)),
    }
    for name,value in identities.items():check('symbolic_'+name,0 if value==0 else 1,0,str(value))
    return {name:str(value) for name,value in identities.items()}


def cartesian_ad():
    torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
    A=np.array([.4,-1/3,1/7,-1/11]);B=np.array([3/7,1/5,-1/13])
    points=np.array([[.4,.3,.8],[1.1,-.7,-.4],[.2,.5,-1.3]])
    Rnp=np.linalg.norm(points,axis=1);mu=points[:,2]/Rnp
    for a in [.34,.5,.77,1.]:
        xyz=torch.tensor(points,requires_grad=True);x,y,z=xyz.unbind(-1)
        s=x*x+y*y;R=torch.sqrt(s+z*z);m=z/R
        phi=R**(-a)*sum(float(v)*m**i for i,v in enumerate(A))
        q=R**(-a-1)*sum(float(v)*m**i for i,v in enumerate(B))
        ps=torch.autograd.grad(phi.sum(),s,create_graph=True,retain_graph=True)[0]
        pz=torch.autograd.grad(phi.sum(),z,create_graph=True,retain_graph=True)[0]
        U=torch.stack((-x*pz-y*q,-y*pz+x*q,2*phi+2*s*ps),dim=-1)
        J=torch.stack([torch.autograd.grad(U[:,i].sum(),xyz,create_graph=True,retain_graph=True)[0] for i in range(3)],dim=1)
        N=(J@U[...,None])[...,0].detach().numpy()
        U=U.detach().numpy()
        er=points/Rnp[:,None]
        rho=np.linalg.norm(points[:,:2],axis=1)
        eaz=np.stack((-points[:,1]/rho,points[:,0]/rho,np.zeros_like(rho)),axis=-1)
        eth=np.cross(eaz,er)
        frame=np.stack((er,eth,eaz),axis=1)
        Fsphere=np.einsum('nij,nj->ni',frame,U)*Rnp[:,None]**a
        Nsphere=np.einsum('nij,nj->ni',frame,N)*Rnp[:,None]**(2*a+1)
        data=angular_data(a,A,B)
        check(f'cartesian_F_alpha{a}',np.max(np.abs(Fsphere-evaluate_vector(data,mu,'F'))),3e-14)
        check(f'cartesian_N_alpha{a}',np.max(np.abs(Nsphere-evaluate_vector(data,mu,'N'))),5e-14)
        check(f'pressure_angular_alpha{a}',np.max(np.abs(data['eigenvalues']*data['Qmode']-data['fmode'])),2e-13)
        check(f'correction_divergence_alpha{a}',np.max(np.abs(data['divergence'].coef)),2e-13)


def global_matching():
    # These are smooth manufactured fields, not Euler candidates. Their
    # pressure nevertheless has the predicted leading angular coefficients.
    for a in [.5,.8,1.]:
        field=manufactured_power(1/(1+a))
        data=angular_data(a,[.42,-.23,-.04],[.34,.19,.13])
        errors=[]
        radii=[16.,64.,256.,1024.]
        inv=GreenPoisson(field.source,decay_power=2*a,lmax=14,nangle=40,nradial=40)
        for R in radii:
            p,_=inv.radial(R)
            expected=pad(data['Qmode'],len(p))
            errors.append(float(np.max(np.abs(R**(2*a)*p-expected))))
        check(f'global_pressure_tail_alpha{a}',errors[-1],8e-4,{'radii':radii,'max_coefficient_errors':errors})
        check(f'global_pressure_improves_alpha{a}',max(errors[k+1]/errors[k] for k in [0,1,2]),.75)


def main():
    start=time.time();exception=None;identities={}
    try:
        identities=symbolic();cartesian_ad();global_matching()
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_farfield.py',ROOT/'src/independent_fields.py',ROOT/'src/independent_pressure.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'checks':checks,'symbolic_identities':identities,'exception':exception,
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/farfield_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
