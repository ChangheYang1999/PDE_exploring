#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from scipy.special import beta as beta_function
from independent_fields import PotentialField,ScalarExpansion,manufactured_power,manufactured_gaussian
from independent_global_diagnostics import (swirl_maximum,bernoulli_balance,velocity_tail_split,
    energy_finite_part,energy_finite_part_beta,helicity_finite_part,eta_norm_identity,virial_identity)
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)
def main():
    start=time.time();exception=None
    try:
        zero=ScalarExpansion([])
        for i,(terms,point) in enumerate([([(1.,0,0,1.)],(0.,0.)),([(1.,1,0,1.)],(1.,0.))]):
            field=PotentialField(ScalarExpansion([(.5,0,1,0.)]),ScalarExpansion(terms,kernel='gaussian'),.57)
            row=swirl_maximum(field);b=row['best']
            check(f'q_maximum_location_{i}',np.hypot(b['r']-point[0],b['z']-point[1]),2e-7,row)
            check(f'q_maximum_strain_{i}',b['absolute_swirl_maximum_defect'],1e-15)
            check(f'q_maximum_gradient_{i}',b['gradient_norm'],2e-8)
        xyz=np.random.default_rng(85721).normal(size=(51,3));r=np.hypot(xyz[:,0],xyz[:,1]);z=xyz[:,2]
        P=xyz[:,0]**2+xyz[:,1]**2-2*z*z+.3*z
        gp=np.stack((2*xyz[:,0],2*xyz[:,1],-4*z+.3),axis=-1)
        for k,field in enumerate([manufactured_power(.55),manufactured_power(.72),manufactured_gaussian()]):
            row=bernoulli_balance(field,xyz,P,gp)
            check(f'Bernoulli_algebra_{k}',np.max(np.abs(row['algebraic_error'])),2e-13)
            def H(points):
                U=field.cartesian(points);c=field.c_l
                pres=points[:,0]**2+points[:,1]**2-2*points[:,2]**2+.3*points[:,2]
                return np.sum(U*U,axis=-1)/2+pres+c*np.sum(points*U,axis=-1)+c*(2*c-1)*np.sum(points*points,axis=-1)/2
            h=2e-4;fd=np.empty_like(xyz)
            for j in range(3):
                step=np.zeros_like(xyz);step[:,j]=h
                fd[:,j]=(H(xyz-2*step)-8*H(xyz-step)+8*H(xyz+step)-H(xyz+2*step))/(12*h)
            check(f'Bernoulli_gradient_FD_{k}',np.max(np.abs(fd-row['gradient_H'])),2e-10)
        for c in [.51,.55,.595]:
            field=manufactured_power(c);R=np.geomspace(.03,1e7,30);mu=np.linspace(-.98,.97,30)
            rr=R*np.sqrt(1-mu*mu);zz=R*mu
            (u0,j0,o0),(du,dj,do)=velocity_tail_split(field,rr,zz)
            uv,jv=field.cartesian(np.stack((rr,np.zeros_like(rr),zz),axis=-1),True)
            check(f'velocity_split_{c}',np.max(np.abs(u0+du-uv)/(1+np.abs(uv))),4e-13)
            check(f'Jacobian_split_{c}',np.max(np.abs(j0+dj-jv)/(1+np.abs(jv))),2e-11)
            row=energy_finite_part(field,nradial=64,nangle=64,residual_check=True)
            refined=energy_finite_part(field,nradial=96,nangle=80,split_radius=2.)
            check(f'energy_residual_integral_{c}',abs(row['residual_identity_error'])/(1+abs(row['integrals']['energy_finite_part'])),2e-9,row)
            check(f'energy_refinement_{c}',abs(row['integrals']['energy_finite_part']-refined['integrals']['energy_finite_part'])/(1+abs(refined['integrals']['energy_finite_part'])),2e-9)
            kappa=.71;pure=PotentialField(zero,ScalarExpansion([(kappa,0,0,(field.alpha+1)/2)]),c)
            exact=-(4*np.pi/3)*kappa*kappa*(field.alpha+1)/(3-2*field.alpha)*beta_function(2.5,field.alpha-.5)
            result=energy_finite_part(pure)
            check(f'energy_exact_beta_{c}',abs(result['integrals']['energy_finite_part']-exact)/abs(exact),2e-9)
            scaled=energy_finite_part(field.dilate(1.73))
            check(f'energy_beta_reference_{c}',abs(energy_finite_part_beta(field)['energy_finite_part']-row['integrals']['energy_finite_part'])/(1+abs(row['integrals']['energy_finite_part'])),2e-10)
            check(f'energy_dilation_{c}',abs(scaled['integrals']['energy_finite_part']-1.73**5*row['integrals']['energy_finite_part'])/(1+abs(scaled['integrals']['energy_finite_part'])),3e-11)
        for c in [.51,.55,.595]:
            base=manufactured_power(c);alpha=base.alpha
            corrected=PotentialField(ScalarExpansion([*base.phi.terms,(.04,0,1,alpha+1)]),
                                     ScalarExpansion([*base.q.terms,(.03,0,0,alpha+1)]),c)
            exact=energy_finite_part_beta(corrected)['energy_finite_part']
            row=energy_finite_part(corrected,nradial=96)
            check(f'energy_noninteger_correction_{c}',abs(row['integrals']['energy_finite_part']-exact)/(1+abs(exact)),2e-10)
        a=.37;b=.71;c=.56
        gaussian=PotentialField(ScalarExpansion([(a,0,0,1.)],kernel='gaussian'),ScalarExpansion([(b,0,0,1.)],kernel='gaussian'),c)
        h=helicity_finite_part(gaussian,nradial=96)
        exact_h=5*a*b*(np.pi/2)**1.5
        check('helicity_exact_Gaussian',abs(h['integrals']['helicity_finite_part']-exact_h)/abs(exact_h),2e-10,h)
        pure=PotentialField(zero,gaussian.q,c)
        e=energy_finite_part(pure,nradial=96)
        exact_e=b*b*np.pi**1.5/(2*2**2.5)
        check('energy_exact_Gaussian',abs(e['integrals']['energy_finite_part']-exact_e)/exact_e,2e-10)
        v=virial_identity(pure,nradial=96)
        exact_l2=2*exact_e*(pure.alpha**2-3*pure.alpha+19/4)
        check('virial_exact_Gaussian',abs(v['integrals']['L_squared']-exact_l2)/exact_l2,2e-10,v)
        check('virial_swirl_orthogonality',abs(v['integrals']['N_dot_L']),1e-14)
        for i,field in enumerate([gaussian,manufactured_power(.53),manufactured_power(.66)]):
            row=eta_norm_identity(field,nradial=96,nangle=80)
            scale=1+abs(row['integrals']['eta_squared'])
            check(f'eta_integral_identity_{i}',abs(row['algebraic_integral_error'])/scale,2e-9,row)
            if i==0:
                exact_eta=35*a*a*(np.pi/2)**2.5
                check('eta_exact_Gaussian',abs(row['integrals']['eta_squared']-exact_eta)/exact_eta,2e-10)
        invalid=PotentialField(ScalarExpansion([(.3,0,0,.1)]),gaussian.q,.55)
        rejected=False
        try:energy_finite_part(invalid)
        except ValueError:rejected=True
        check('reject_invalid_energy_tail',not rejected,0.)
        rejected=False
        try:energy_finite_part(manufactured_power(.6))
        except ValueError:rejected=True
        check('reject_critical_energy_subtraction',not rejected,0.)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_global_diagnostics.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/global_diagnostic_tests.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
