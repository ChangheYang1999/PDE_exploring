#!/usr/bin/env python3
"""Finite-search and global-integral diagnostics for a saved approximation."""
from pathlib import Path
import argparse,datetime,time
import numpy as np
from scipy.special import roots_legendre
from independent_artifacts import sha256,source_identity,verify_source_identity,atomic_json
from independent_fields import PotentialField
from independent_geometry import reporting_gauge
from independent_pressure import GreenPoisson
from independent_global_diagnostics import (swirl_maximum,bernoulli_balance,energy_finite_part,
    energy_finite_part_beta,helicity_finite_part,eta_norm_identity,virial_identity,tail_compatibility)
from independent_weighted_identities import weighted_circulation_suite
from independent_stagnation import stagnation_audit
from independent_axis_moments import axis_moments
ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('--output',required=True,type=Path)
    p.add_argument('--nradial',type=int,default=64);p.add_argument('--nangle',type=int,default=64)
    a=p.parse_args();out=a.output.resolve();start=time.perf_counter()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside verifier lane')
    if out.exists():raise FileExistsError('preserving existing global diagnostic record')
    identity=source_identity(ROOT,__file__);before=sha256(a.candidate)
    field,gauge=reporting_gauge(PotentialField.load(a.candidate))
    result={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_sha256':before,
            'candidate_path':str(a.candidate.resolve()),'source_sha256':identity,'gauge':gauge,'c_l':field.c_l,'alpha':field.alpha,
            'swirl_maximum':swirl_maximum(field),'tail_compatibility':tail_compatibility(field)}
    parameters={'nradial':a.nradial,'nangle':a.nangle}
    result['weighted_circulation']=weighted_circulation_suite(field,**parameters)
    result['stagnation']=stagnation_audit(field,search_radius=16*max(field.phi.length,field.q.length))
    result['axis_moments']=[]
    for root in result['stagnation']['roots']:
        if root['kind']!='axis':continue
        first=axis_moments(field,root['z'])
        second=axis_moments(field,root['z'],nradial=56,nangle=80,cutoff_factor=16)
        result['axis_moments'].append({'root':root,'levels':[first,second]})
    allowed=result['tail_compatibility']['sufficient_basis_test_passed']
    for name,function,lower,upper in [('energy_finite_part',energy_finite_part,.5,.6),
                                      ('helicity_finite_part',helicity_finite_part,.5,.75),
                                      ('eta_norm',eta_norm_identity,.5,2/3),('virial',virial_identity,.5,.75)]:
        if allowed and lower<field.c_l<upper:
            first=function(field,**parameters)
            second=function(field,nradial=max(a.nradial+16,int(a.nradial*1.5)),nangle=max(a.nangle+16,int(a.nangle*1.25)),
                            split_radius=2*max(field.phi.length,field.q.length))
            result[name]={'status':'EVALUATED','levels':[first,second]}
        else:result[name]={'status':'NOT_APPLICABLE','reason':'Exponent or sufficient differentiated-tail hypotheses not met.'}
    if result['energy_finite_part']['status']=='EVALUATED':
        result['energy_finite_part']['independent_beta_reference']=energy_finite_part_beta(field)
    pressure=GreenPoisson(field.source,decay_power=2*field.alpha,lmax=20,nangle=48,nradial=28,scale=field.phi.length)
    R=max(field.phi.length,field.q.length)*np.array([.125,.5,1.,2.,8.,32.]);mu,_=roots_legendre(32)
    r=R[:,None]*np.sqrt(1-mu*mu);z=R[:,None]*mu
    xyz=np.stack((r,np.zeros_like(r),z),axis=-1);P,gp=pressure.on_spheres(R,mu)
    gradients=np.stack((gp[...,0],np.zeros_like(r),gp[...,1]),axis=-1)
    bern=bernoulli_balance(field,xyz,P,gradients)
    result['Bernoulli']={key:value.tolist() for key,value in bern.items()}
    result['Bernoulli'].update(r=r.tolist(),z=z.tolist(),maximum_algebraic_error=float(np.max(np.abs(bern['algebraic_error']))),
                              maximum_Euler_defect=float(np.max(np.abs(bern['Euler_defect']))))
    if sha256(a.candidate)!=before:raise RuntimeError('candidate changed during validation')
    verify_source_identity(ROOT,identity)
    result.update(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,
                  scope='Additional necessary-condition diagnostics and implementation identities. Finite searches and quadrature are not certified global bounds. This file does not assign label A or B.')
    atomic_json(out,result)
    print({'output':str(out),'elapsed_seconds':result['elapsed_seconds'],'maximum_q':result['swirl_maximum']['best']},flush=True)
if __name__=='__main__':main()
