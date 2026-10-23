"""Prepare and check a three-block absolute-loss residual mesh; never optimize."""
import argparse
import math
import os
from pathlib import Path
import time

from absolute_common import ROOT,OUT,A_REF,np,read,load_case,atomic,npz,digest,provenance
from absolute_model import AbsoluteLossProblem,FrozenLogMesh,array_hash
from whole_axis_mesh import build_whole_axis_mesh


def check_spot_derivatives(case,mesh,block_ids,block_size):
    # All three transformed regions are represented. These are tests of the
    # complete analytic field chain, not a replacement integration mesh.
    chosen=[]
    for block in range(3):
        available=np.flatnonzero(block_ids==block)
        positions=np.unique(np.linspace(0,len(available)-1,12).astype(int))
        chosen.extend(available[positions])
    chosen=np.asarray(chosen,dtype=int)
    spots=FrozenLogMesh(mesh.s[chosen],mesh.theta[chosen],mesh.weights[chosen],'three_block_derivative_spots')
    problem=AbsoluteLossProblem(case,spots,A_REF,block_size=block_size)
    J=problem.jacobian();p,extra=problem.p,problem.extra
    rng=np.random.default_rng(120119);directions=[]
    cl=np.zeros(problem.physical_columns);cl[0]=1;directions.append(('complete_cl',cl))
    for i in range(2):
        v=rng.normal(size=problem.physical_columns);v/=np.linalg.norm(v)
        directions.append(('physical_mixed_'+str(i),v))
    rows=[];arrays={'selected_indices':chosen,'raw_jacobian':J,'selected_block_ids':block_ids[chosen]}
    for name,v in directions:
        analytic=J@v;checks=[]
        for h in (2e-5,1e-5):
            probes=[problem.fun(p+k*h*v[:24],extra+k*h*v[24:]) for k in (2,1,-1,-2)]
            fd=(-probes[0]+8*probes[1]-8*probes[2]+probes[3])/(12*h)
            difference=fd-analytic
            perblock={}
            for block,label in [(0,'origin'),(1,'middle'),(2,'infinity')]:
                select=block_ids[chosen]==block
                perblock[label]={'relative_error':float(np.linalg.norm(difference[select])/max(np.linalg.norm(analytic[select]),1e-300)),
                    'weighted_absolute_error_norm':float(np.linalg.norm(difference[select])),
                    'analytic_weighted_norm':float(np.linalg.norm(analytic[select]))}
            relative=float(np.linalg.norm(difference)/max(np.linalg.norm(analytic),1e-300))
            checks.append({'step':h,'relative_error':relative,
                'weighted_absolute_error_norm':float(np.linalg.norm(difference)),
                'blocks':perblock,'passed':bool(relative<1e-4)})
            arrays[name+'_fd_'+str(h)]=fd
        rows.append({'direction':name,'input_sha256':array_hash(v),'steps':checks,
            'passed':bool(all(c['passed'] for c in checks))})
    return {'rows':rows,'passed':bool(all(row['passed'] for row in rows)),
        'threshold_overall_weighted_relative':1e-4,
        'extreme_tail_relative_error_is_reported_but_not_a_standalone_acceptance_criterion':True,
        'scope':'Complete raw cl and two fixed mixed physical directions at selected nodes from all three transformed blocks; no full-mesh Jacobian or optimizer run.'},arrays


def run(args):
    began=time.time();directory=OUT/'whole_axis_preparation'/args.label
    if directory.exists():raise ValueError('Refusing to overwrite a prepared mesh')
    candidate_path=ROOT/'inputs'/(args.case+'.json');case=load_case(args.case)
    integral_path=OUT/'integrals'/(args.case+'.json');integral=read(integral_path)
    if (not integral.get('numerical_error_checks_passed') or not integral.get('finite_whole_axis')
        or integral.get('dilation')!=1. or integral.get('center_convention')!='center_chart'
        or integral.get('candidate_sha256')!=digest(candidate_path) or integral.get('a_ref')!=A_REF):
        raise ValueError('A matching candidate whole-radius integration record is required')
    origin_radius=integral['origin']['radius'];S=integral['final_quadrature']['s_max']
    coarse,coarse_meta,coarse_blocks=build_whole_axis_mesh(origin_radius,S,24,16,64,96,name=args.label+'_coarse')
    fine,fine_meta,fine_blocks=build_whole_axis_mesh(origin_radius,S,48,32,128,128,name=args.label+'_refined')
    directory.mkdir(parents=True)
    coarse_path=directory/'mesh_coarse.npz';fine_path=directory/'mesh_refined.npz'
    npz(coarse_path,s=coarse.s,theta=coarse.theta,weights=coarse.weights,block_ids=coarse_blocks)
    npz(fine_path,s=fine.s,theta=fine.theta,weights=fine.weights,block_ids=fine_blocks)
    problem=AbsoluteLossProblem(case,coarse,A_REF,block_size=args.block_size)
    fine_problem=AbsoluteLossProblem(case,fine,A_REF,block_size=args.block_size)
    r=problem.fun();rf=fine_problem.fun();jc=float(r@r/2);jf=float(rf@rf/2)
    blocks={}
    for i,label in [(0,'origin'),(1,'middle'),(2,'infinity')]:
        a=r[coarse_blocks==i];b=rf[fine_blocks==i]
        blocks[label]={'coarse_J':float(a@a/2),'refined_J':float(b@b/2),
            'refinement_difference':float(abs(a@a-b@b)/2)}
    mesh_error=math.fsum(x['refinement_difference'] for x in blocks.values())
    value=integral['J_abs_estimate'];floor=128*np.finfo(float).eps*max(abs(value),abs(jf),1e-300)
    combined_error=integral['total_error_diagnostic']+mesh_error+floor
    difference=abs(jf-value);comparison_passed=bool(difference<=combined_error)
    derivatives,derivative_arrays=check_spot_derivatives(case,coarse,coarse_blocks,args.block_size)
    derivative_path=directory/'derivative_spots.npz';npz(derivative_path,**derivative_arrays)
    residual_path=directory/'residuals.npz';npz(residual_path,coarse=r,refined=rf)
    result={'schema':'absolute_loss_whole_axis_preparation_v1','case':args.case,'label':args.label,
        'candidate_path':str(candidate_path),'candidate_sha256':digest(candidate_path),
        'validated_integral_path':str(integral_path),'validated_integral_sha256':digest(integral_path),
        'a_ref':A_REF,'center_convention':'center_chart',
        'coarse_mesh':coarse_meta,'refined_mesh':fine_meta,
        'coarse_mesh_path':str(coarse_path),'coarse_mesh_file_sha256':digest(coarse_path),
        'refined_mesh_path':str(fine_path),'refined_mesh_file_sha256':digest(fine_path),
        'coarse_halfnorm_J_abs':jc,'refined_halfnorm_J_abs':jf,
        'validated_J_abs':value,'difference_from_validated':difference,
        'transformed_block_contributions':blocks,'mesh_refinement_error_diagnostic':mesh_error,
        'validated_integral_error_diagnostic':integral['total_error_diagnostic'],
        'combined_comparison_diagnostic':combined_error,'comparison_passed':comparison_passed,
        'whole_axis_domain_covered_by_transformations':True,
        'whole_axis_qualified':False,'neighborhood_validated':False,
        'future_optimization_gate_open':False,'rigorous_error_certificate':False,
        'optimization_performed':False,'candidate_modified':False,
        'no_external_value_only_tail_correction':True,
        'complete_cl_and_mixed_derivatives':derivatives,
        'derivative_arrays_path':str(derivative_path),'derivative_arrays_sha256':digest(derivative_path),
        'residual_arrays_path':str(residual_path),'residual_arrays_sha256':digest(residual_path),
        'source_sha256':{name:digest(ROOT/name) for name in ['prepare_whole_axis.py','whole_axis_mesh.py','absolute_model.py','absolute_fields.py','highprecision_origin.py']},
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'environment':provenance(),'elapsed_seconds':time.time()-began,
        'limitation':'All three transformed integrals are represented by positive fixed quadrature weights. Refinement and endpoint tests are numerical diagnostics, not an exact invariant finite rule, rigorous integral enclosure or uniform trust-neighborhood qualification.',
        'completed':True,'passed':bool(comparison_passed and derivatives['passed'])}
    atomic(directory/'preparation.json',result)
    print(__import__('json').dumps({'path':str(directory/'preparation.json'),'passed':result['passed'],
        'coarse_J':jc,'refined_J':jf,'difference':difference,'combined_error':combined_error,
        'derivatives_passed':derivatives['passed'],'elapsed_seconds':result['elapsed_seconds']}),flush=True)
    if not result['passed']:raise SystemExit(2)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,choices=['stage11','combined','local','global'])
    parser.add_argument('--label',required=True)
    parser.add_argument('--block-size',type=int,default=1024)
    args=parser.parse_args()
    if '/' in args.label or '\\' in args.label:parser.error('Simple label required')
    run(args)


if __name__=='__main__':main()
