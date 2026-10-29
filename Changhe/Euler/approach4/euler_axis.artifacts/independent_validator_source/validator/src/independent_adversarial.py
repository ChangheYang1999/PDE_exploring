"""Untouched quasi-random grids and searches for local reduced-residual peaks."""
from __future__ import annotations
import numpy as np
from scipy.stats import qmc
from scipy.optimize import minimize
from independent_tail_audit import scalar_cancellation
from independent_precision import compare_precision
from independent_pressure import GreenPoisson,DirectNewtonPressure
from independent_stagnation import stagnation_audit


def adversarial_audit(field,*,seed=828718,sample_power=12,log_radius_bounds=(-9.,9.),starts=8):
    lower,upper=map(float,log_radius_bounds)
    points=qmc.Sobol(d=2,scramble=True,seed=seed).random_base2(sample_power)
    logR=lower+(upper-lower)*points[:,0]
    mu=2*points[:,1]-1
    R=np.exp(logR);r=R*np.sqrt(1-mu*mu);z=R*mu
    red=field.reduced(r,z)
    def balanced(values,terms):
        # A fixed denominator is used for peak searches so optimizer-dependent
        # denominator enlargement cannot lower the selected objective.
        scale=float(np.sqrt(np.mean(np.sum(terms*terms,axis=-1))))
        return np.abs(values)/scale if scale else np.abs(values),scale
    records=[];worst_points=[]
    for name in ['q','eta']:
        metric,scale=balanced(red[name],red[name+'_terms'])
        ranked=np.argsort(-metric)[:starts]
        def objective(x):
            lr,m=x;radius=np.exp(lr)
            rr=radius*np.sqrt(max(0.,1-m*m));zz=radius*m
            value=float(field.reduced(rr,zz)[name])
            return -(value/scale)**2 if scale else -value*value
        peaks=[]
        for k in ranked:
            result=minimize(objective,[logR[k],mu[k]],method='L-BFGS-B',bounds=[(lower,upper),(-1.,1.)],
                            options={'maxiter':120,'ftol':1e-13,'gtol':1e-9,'maxls':30})
            radius=float(np.exp(result.x[0]));m=float(result.x[1]);rr=radius*np.sqrt(max(0.,1-m*m));zz=radius*m
            value=float(field.reduced(rr,zz)[name])
            peaks.append({'r':rr,'z':zz,'R':radius,'residual':value,'fixed_scale_relative':abs(value)/scale if scale else None,
                          'search_success':bool(result.success),'search_message':str(result.message),
                          'at_radial_search_boundary':bool(abs(result.x[0]-lower)<1e-5 or abs(result.x[0]-upper)<1e-5)})
        peaks.sort(key=lambda d:-abs(d['residual']))
        records.append({'equation':name,'fixed_term_scale':scale,'holdout_rms':float(np.sqrt(np.mean(red[name]**2))),
                        'holdout_max':float(np.max(np.abs(red[name]))),'peaks':peaks})
        if peaks:worst_points.append([peaks[0]['r'],0.,peaks[0]['z']])
    # Independent pressure resolution study at fixed, generally off-grid points.
    pressure_points=np.array([[0.,0.],[0.,.731],[.317,-.419],[1.73,.29],[7.1,-3.3]])
    pressure_records=[]
    for level,config in [('coarse',(12,32,20)),('medium',(24,64,36)),('fine',(40,100,56))]:
        ell,na,nr=config
        solver=GreenPoisson(field.source,decay_power=2*field.alpha,lmax=ell,nangle=na,nradial=nr)
        p,g=solver.evaluate(pressure_points[:,0],pressure_points[:,1])
        pressure_records.append({'level':level,'lmax':ell,'nangle':na,'nradial':nr,'pressure':p.tolist(),'gradient':g.tolist()})
    direct=DirectNewtonPressure(field.source,decay_power=2*field.alpha,nradial=96,nangle=96)
    gradient_checks=[]
    for r0,z0 in pressure_points[:3]:
        gradient_checks.append({'r':float(r0),'z':float(z0),'direct_pressure':direct.evaluate(r0,z0),
                                'direct_gradient_steps':direct.finite_difference_gradient(r0,z0)})
    precision=compare_precision(field,worst_points+[[0.,0.,0.]],dps=70)
    sample_points=np.stack((r,np.zeros_like(r),z),axis=-1)
    cancellation={name:scalar_cancellation(scalar,r*r,z) for name,scalar in [('phi',field.phi),('q',field.q)]}
    return {'seed':seed,'sample_count':len(r),'log_radius_bounds':[lower,upper],'peak_searches':records,
            'pressure_points_r_z':pressure_points.tolist(),'pressure_refinements':pressure_records,
            'direct_pressure_gradient_checks':gradient_checks,'high_precision_points':precision,
            'basis_cancellation':cancellation,'stagnation':stagnation_audit(field),
            'scope':'Finite searches can expose defects; absence of a found peak does not prove a global residual bound.'}
