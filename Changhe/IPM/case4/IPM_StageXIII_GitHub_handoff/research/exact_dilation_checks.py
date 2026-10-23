"""Exact function dilation checks; no refit, optimization or candidate export."""
import argparse
import json
import math
import os
import time
from pathlib import Path

from absolute_common import ROOT,BASE,OUT,A_REF,np,read,atomic,npz,digest,provenance
from absolute_fields import prepare_candidate,fields,residual,exact_dilation_fields


def terms(cl,ff,x,y,stable=True):
    wx=cl*x-ff['psiy'];wy=cl*y+ff['psix']
    q=ff['q'] if stable else cl-1+ff['ratio']
    a=wx*ff['fx'];b=wy*ff['fy'];c=q*ff['f']
    return a+b+c,np.abs(a)+np.abs(b)+np.abs(c)


def location(values,x,y):
    i=int(np.argmax(np.abs(values)))
    return {'value':float(np.abs(values[i])),'signed_value':float(values[i]),
        'point':[float(x[i]),float(y[i])],'radius':float(np.hypot(x[i],y[i])),
        'point_index':i}


def run(args):
    output=OUT/(args.label+'.json');artifact=OUT/(args.label+'.npz')
    if output.exists() or artifact.exists():raise ValueError('Refusing to overwrite dilation diagnostics')
    began=time.time();factors=[1.,2.,16.,256.,1024.]
    radii=np.asarray([1e-8,1e-4,.01,.019,.02,.021,.03,.5,1.,8.,64.,256.,8192.])
    angles=np.asarray([0.,1e-9,.17,.63,np.pi/2-1e-9,np.pi/2])
    xx,yy=np.meshgrid(radii,angles,indexing='ij')
    xvalues=xx*np.cos(yy);yvalues=xx*np.sin(yy)
    xvalues[:,-1]=0.;yvalues[:,0]=0.
    x=np.r_[0.,xvalues.ravel()];y=np.r_[0.,yvalues.ravel()]
    rad=np.hypot(x,y);eps=np.finfo(float).eps;rows={}
    arrays={'x':x,'y':y,'radii':radii,'angles':angles,'factors':np.asarray(factors)}
    index=read(ROOT/'inputs/candidates.json')
    result={'schema':'absolute_loss_exact_function_dilation_v1','completed':False,
        'a_ref':A_REF,'factors':factors,'predetermined_radii':radii.tolist(),
        'predetermined_angles':angles.tolist(),'points':len(x),
        'spatial_dilation_is_exact_function_evaluation_at_X_over_lambda':True,
        'old_basis_refit_performed':False,'candidate_exported':False,'optimization_performed':False,
        'finite_domain_integral_invariance_claimed':False,
        'covariance_tolerance':{'absolute_Rf_per_a_ref':1e-10,'additional_term_sum_epsilon_factor':128},
        'candidates':rows}
    atomic(output,result)
    for name in index['candidates']:
        path=ROOT/'inputs'/(name+'.json');case=read(path)
        prepared=prepare_candidate(case,'center_chart');cl=float(prepared['parameters'][0])
        center=fields(prepared,[0.],[0.]);a0=float(center['f'][0]);records=[]
        for factor in factors:
            bx,by=x/factor,y/factor
            reference_fields=fields(prepared,bx,by)
            reference_rf=residual(prepared,bx,by)
            scaled=exact_dilation_fields(prepared,x,y,factor)
            assembled,term_sum=terms(cl,scaled,x,y,True)
            physical_assembled,physical_terms=terms(cl,scaled,x,y,False)
            drift_x=cl*x-scaled['psiy'];drift_y=cl*y+scaled['psix']
            rho=y*scaled['f'];rho_x=y*scaled['fx'];rho_y=scaled['f']+y*scaled['fy']
            direct_rrho=drift_x*rho_x+drift_y*rho_y-rho
            covariance=assembled-reference_rf
            physical_covariance=physical_assembled-reference_rf
            density_covariance=direct_rrho-factor*(by*reference_rf)
            scaled_density_error=np.divide(density_covariance,rad,out=np.zeros_like(rad),where=rad>0)
            identity_error=direct_rrho-y*assembled
            scale_checks={}
            for key,multiplier in [('f',1.),('fx',1/factor),('fy',1/factor),
                                   ('psi',factor*factor),('psix',factor),('psiy',factor),('ratio',1.),('q',1.)]:
                expected=multiplier*reference_fields[key]
                difference=scaled[key]-expected
                scale_checks[key]={'max_abs_error':float(np.max(abs(difference))),
                    'max_field':float(np.max(abs(expected)))}
            rho_law=rho-factor*(by*reference_fields['f'])
            term_bound=1e-10*A_REF+128*eps*(term_sum+np.abs(reference_rf))
            physical_bound=1e-10*A_REF+128*eps*(physical_terms+np.abs(reference_rf))
            rho_term=(abs(drift_x*rho_x)+abs(drift_y*rho_y)+abs(rho))
            rho_bound=(1e-10*A_REF*rad+128*eps*(rho_term+np.abs(factor*by*reference_rf)))
            stable_pass=bool(np.all(np.abs(covariance)<=term_bound))
            physical_pass=bool(np.all(np.abs(physical_covariance)<=physical_bound))
            density_pass=bool(np.all(np.abs(density_covariance)<=rho_bound))
            record={'lambda':factor,'cl':cl,'a0':a0,
                'cl_and_a0_unchanged':True,'field_scaling_checks':scale_checks,
                'rho_lambda_equals_lambda_rho_X_over_lambda_max_abs_error':float(np.max(abs(rho_law))),
                'Rf_recomputed_from_scaled_fields':True,
                'stable_center_Rf_covariance_abs_error':location(covariance,x,y),
                'physical_formula_Rf_covariance_abs_error':location(physical_covariance,x,y),
                'stable_center_Rf_covariance_per_a_ref':float(np.max(abs(covariance))/A_REF),
                'physical_formula_Rf_covariance_per_a_ref':float(np.max(abs(physical_covariance))/A_REF),
                'density_covariance_abs_error':location(density_covariance,x,y),
                'density_covariance_error_divided_by_r_a_ref':float(np.max(abs(scaled_density_error))/A_REF),
                'direct_density_equals_y_Rf_abs_error':location(identity_error,x,y),
                'reference_Rf_max':float(np.max(abs(reference_rf))),
                'max_term_roundoff_bound':float(np.max(term_bound)),
                'stable_center_covariance_passed':stable_pass,
                'direct_physical_covariance_passed':physical_pass,
                'direct_density_covariance_passed':density_pass,
                'roundoff_interpretation':'Absolute errors are meaningful near canceled Taylor jets; relative error against a near-zero residual is not used as a pass criterion.'}
            records.append(record)
            stem=name+'_lambda_'+str(int(factor))
            arrays[stem+'_reference_Rf']=reference_rf;arrays[stem+'_assembled_Rf']=assembled
            arrays[stem+'_physical_Rf']=physical_assembled;arrays[stem+'_direct_Rrho']=direct_rrho
        rows[name]={'candidate_path':str(path),'candidate_sha256':digest(path),
            'interpretation':'center_chart with unrounded analytic potential and explicit center c0',
            'center_metadata':prepared['center_metadata'],'checks':records,
            'passed':bool(all(r['stable_center_covariance_passed'] and r['direct_physical_covariance_passed'] and r['direct_density_covariance_passed'] for r in records))}
        atomic(output,result)

    # This deliberately uses the frozen historical native residual path and
    # its fixed X-grid denominator. It is not the new unrounded absolute loss.
    from stage12_model import total_fields_saved,residual_from_fields
    from stage12_common import e,objectives
    os.environ['IPM_WORK_DIR']=str(ROOT)
    original=read(ROOT/'inputs/stage11.json');problem=e.GridProblem(97)
    p=np.r_[original['cl'],original['coefficients'][1:]]
    old_records=[]
    for factor in factors:
        ff=total_fields_saved(original,problem.x/factor,problem.y/factor)
        for key,multiplier in [('fx',1/factor),('fy',1/factor),('psi',factor*factor),('psix',factor),('psiy',factor)]:
            ff[key]=ff[key]*multiplier
        value=residual_from_fields(p,ff,problem.x,problem.y,problem.root)
        objective=objectives(value,97)
        old_records.append({'lambda':factor,**objective,
            'old_native_stabilized_fixed_domain_objective':True,
            'exact_dilation_evaluation_no_refit':True})
        arrays['historical_J97_lambda_'+str(int(factor))+'_residual']=value
    result['historical_StageXI_fixed_domain_J97_under_exact_dilation']=old_records
    result['historical_StageXI_lambda1_archived_objective']=original['objectives']
    result['historical_lambda1_J_difference']=old_records[0]['J_joint']-original['objectives']['J_joint']
    result['historical_and_absolute_arithmetic_are_separate']=True
    result['function_covariance_is_not_a_fixed_truncated_integral_invariance_test']=True
    result['source_sha256']={name:digest(ROOT/name) for name in ['exact_dilation_checks.py','absolute_fields.py','highprecision_origin.py']}
    result['base_manifest_sha256']=digest(ROOT/'provenance/base_manifest.json')
    result['candidate_index_sha256']=digest(ROOT/'inputs/candidates.json')
    result['environment']=provenance();result['elapsed_seconds']=time.time()-began
    result['completed']=True;result['passed']=bool(all(row['passed'] for row in rows.values()))
    npz(artifact,**arrays);result['arrays_path']=str(artifact);result['arrays_sha256']=digest(artifact)
    atomic(output,result)
    print(json.dumps({'path':str(output),'passed':result['passed'],
        'historical_J97':{str(int(r['lambda'])):r['J_joint'] for r in old_records},
        'elapsed_seconds':result['elapsed_seconds']}),flush=True)
    if not result['passed']:raise SystemExit(2)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label',default='exact_dilation_checks')
    args=parser.parse_args()
    if '/' in args.label or '\\' in args.label:parser.error('Simple output label required')
    run(args)


if __name__=='__main__':main()
