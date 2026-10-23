"""Supervised qualification and BLAS benchmark of the actual absolute model.

No solver step is promoted and no optimization is launched. The root launches
this worker after choosing the candidate and complete whole-axis training rule.
"""
import argparse
import gc
import time
from pathlib import Path
from absolute_common import ROOT,OUT,A_REF,np,read,atomic,npz,digest,array_hash,provenance
from absolute_model_v2 import AbsoluteLossProblem,FrozenLogMesh
from absolute_chart_v2 import AbsoluteC5ChartV2
from absolute_chart import hp_report
from stage13_model_v3 import CachedAbsoluteProblem,original_namespace_identity_record


def rel(actual,reference):
    return float(np.linalg.norm(actual-reference)/max(np.linalg.norm(reference),1e-300))


def timed(call):
    began=time.perf_counter();value=call()
    return value,time.perf_counter()-began


def main(args):
    if sorted(args.workers)!=[1,4,8] or args.block_size<1:
        raise ValueError('Fresh V3 qualification requires actual worker settings1/4/8 and positive blocks')
    directory=args.output.resolve()
    if directory.exists():raise ValueError('Model qualification output exists; choose a fresh label')
    directory.mkdir(parents=True)
    case=read(args.candidate);mesh=FrozenLogMesh.load(args.mesh)
    report={'schema':'stage13_actual_model_cache_benchmark_v3_origin20_private_scalar_exp','candidate_path':str(args.candidate.resolve()),
        'candidate_sha256':digest(args.candidate),'mesh_path':str(args.mesh.resolve()),'mesh_sha256':mesh.fingerprint,
        'a_ref':A_REF,'center_convention':'center_chart','production_origin_order':20,'all_raw_origin_derivative_order':20,'physical_model_or_objective_changed':False,'optimization_performed':False,
        'source_sha256':{name:digest(ROOT/name) for name in ('stage13_model.py','stage13_model_v2.py','stage13_model_v3.py','stage13_stable_exp.py','stage13_model_benchmark_v3.py','base/spectral_basis.py',
            'absolute_model.py','absolute_model_v2.py','absolute_fields.py','absolute_fields_v2.py','highprecision_origin.py','absolute_chart.py','absolute_chart_v2.py')},
        'thresholds':{'reference_residual_relative':5e-9,'reference_jacobian_relative':5e-11,
            'raw_FD_relative':3e-5,'feasible_FD_relative':1e-3,'adjoint_scaled':1e-12},
        'benchmarks':[],'raw_checks':[],'feasible_checks':[],'operator_checks':[],
        'completed':False,'passed':False,'environment':provenance(),
        'original_namespace_identity_at_start':original_namespace_identity_record(),
        'independent_stateless_provider':'Unchanged absolute_model_v2 / absolute_fields_v2',
        'selected_runtime_workers':4,'runtime_selection_reason':'Explicit conservative runtime setting4; all1/4/8 timings reported separately.'}
    output=directory/'checks.json';atomic(output,report)
    baseline=AbsoluteLossProblem(case,mesh,A_REF,block_size=args.block_size)
    p,extra=baseline.p.copy(),baseline.extra.copy()
    rr,reference_fun_seconds=timed(lambda:baseline.fun(p,extra))
    JJ,reference_jac_seconds=timed(lambda:baseline.jacobian(p,extra))
    report.update(raw_physical_columns=baseline.physical_columns,feasible_columns=baseline.physical_columns-5,
        all_19_original_core_directions_retained=True,all_additional_coefficients_retained=True,
        full_cl_derivative_included=True,reference_objective=float(rr@rr/2),
        reference_fun_seconds=reference_fun_seconds,reference_jac_seconds=reference_jac_seconds,
        p=p.tolist(),extra_sha256=array_hash(extra),all_extra_coefficients_directly_FD_checked=True)
    reference_file=directory/'reference.npz';npz(reference_file,residual=rr,raw_jacobian=JJ,p=p,extra=extra)
    report.update(reference_arrays_path=str(reference_file),reference_arrays_sha256=digest(reference_file))
    atomic(output,report)
    for workers in args.workers:
        model=CachedAbsoluteProblem(case,mesh,A_REF,block_size=args.block_size,workers=workers)
        r,first_seconds=timed(lambda:model.fun(p,extra))
        J,jac_seconds=timed(lambda:model.jacobian(p,extra))
        _,cached_fun_seconds=timed(lambda:model.fun(p,extra))
        _,cached_jac_seconds=timed(lambda:model.jacobian(p,extra))
        # A genuine coefficient-only trial reuses an exact cl basis, without
        # accepting a stale residual/Jacobian at different coefficients.
        trial_extra=extra.copy()
        if len(extra):trial_extra[len(extra)//2]+=1e-6
        else:raise ValueError('The Stage XIII benchmark expects added modes')
        _,trial_fun_seconds=timed(lambda:model.fun(p,trial_extra))
        _,trial_jac_seconds=timed(lambda:model.jacobian(p,trial_extra))
        # Reject-and-return must restore the higher-order derivative cache as
        # well as the residual. Exercise A -> changed-cl B -> original A.
        trial_p=p.copy();trial_p[0]+=1e-7*max(1.,abs(p[0]))
        model.fun(trial_p,trial_extra);model.jacobian(trial_p,trial_extra)
        restored_r=model.fun(p,extra);restored_J=model.jacobian(p,extra)
        cycle_r_error=rel(restored_r,r);cycle_J_error=rel(restored_J,J)
        cycle_norm=float(np.linalg.norm(restored_r-r))
        cycle_64eps=64*np.finfo(float).eps*max(np.linalg.norm(restored_r),np.linalg.norm(r),1e-300)
        row={'BLAS_threads':workers,'cold_fun_seconds':first_seconds,'following_jacobian_seconds':jac_seconds,
            'duplicate_fun_seconds':cached_fun_seconds,'duplicate_jacobian_seconds':cached_jac_seconds,
            'same_cl_coefficient_trial_fun_seconds':trial_fun_seconds,
            'same_cl_coefficient_trial_jacobian_seconds':trial_jac_seconds,
            'reference_residual_relative_error':rel(r,rr),'reference_jacobian_relative_error':rel(J,JJ),
            'reference_residual_max_abs_error':float(np.max(abs(r-rr))),
            'reference_jacobian_max_abs_error':float(np.max(abs(J-JJ))),
            'objective':float(r@r/2),'cache':model.cache_record(),
            'rejected_trial_return_cycle':{'changed_cl_and_extra_trial_was_not_promoted':True,
                'restored_residual_relative_difference':cycle_r_error,
                'restored_Jacobian_relative_difference':cycle_J_error,
                'restored_residual_difference_norm':cycle_norm,
                'original_64epsilon_threshold':float(cycle_64eps),
                'within_original_64epsilon_threshold':bool(cycle_norm<=cycle_64eps)},
            'passed':bool(rel(r,rr)<5e-9 and rel(J,JJ)<5e-11 and cycle_r_error<5e-9 and cycle_J_error<5e-11 and cycle_norm<=cycle_64eps)}
        if workers==4:
            cached_path=directory/'cached_workers4.npz';npz(cached_path,residual=r,raw_jacobian=J,p=p,extra=extra)
            row.update(cached_arrays_path=str(cached_path),cached_arrays_sha256=digest(cached_path))
            report.update(production_arrays_path=str(cached_path),production_arrays_sha256=digest(cached_path))
        report['benchmarks'].append(row);atomic(output,report)
        model.clear_cache();del model,r,J;gc.collect()

    # Independently evaluate the ORIGINAL stateless provider again after all
    # private cached providers. Identity sentinels establish no mutation; value
    # differences retain the original stateless tolerances (not cached replay).
    after_r=baseline.fun(p,extra);after_J=baseline.jacobian(p,extra)
    unchanged_path=directory/'original_stateless_after_private_cache.npz'
    npz(unchanged_path,residual=after_r,raw_jacobian=after_J,p=p,extra=extra)
    unchanged={'identity':original_namespace_identity_record(),
        'residual_relative_difference':rel(after_r,rr),'raw_jacobian_relative_difference':rel(after_J,JJ),
        'residual_bitwise_equal':bool(np.array_equal(after_r,rr)),
        'raw_jacobian_bitwise_equal':bool(np.array_equal(after_J,JJ)),
        'artifact_path':str(unchanged_path),'artifact_sha256':digest(unchanged_path),
        'same_original_stateless_source_and_functions':True,
        'passed':bool(original_namespace_identity_record()['passed'] and rel(after_r,rr)<5e-9 and rel(after_J,JJ)<5e-11)}
    report['old_independent_provider_after_private_evaluations']=unchanged
    del after_r,after_J;gc.collect();atomic(output,report)

    # Derivative checks use explicit radii on both sides of the origin branch,
    # exact axes, near axes, and independent large-radius sites. This is a
    # derivative test, not a quadrature-accuracy claim.
    radii=np.asarray([.001,.005,.01,.015,.019,.02,.021,.03,.1,.5,1.,2.,8.,64.,256.,1024.,8192.,1e8])
    angles=np.r_[0.,1e-8,np.linspace(.01,np.pi/2-.01,15),np.pi/2-1e-8,np.pi/2]
    ss,tt=np.meshgrid(np.log(radii),angles,indexing='ij')
    derivative_mesh=FrozenLogMesh(ss.ravel(),tt.ravel(),np.ones(ss.size),'stage13_derivative_switch_axes_far_probe')
    model=CachedAbsoluteProblem(case,derivative_mesh,A_REF,block_size=args.block_size,workers=1)
    r=model.fun(p,extra);J=model.jacobian(p,extra)
    saved={'residual':r,'raw_jacobian':J,'p':p,'extra':extra,'s':derivative_mesh.s,'theta':derivative_mesh.theta}
    rng=np.random.default_rng(131301)
    for index in range(model.physical_columns):
        direction=np.zeros(model.physical_columns);direction[index]=1
        analytic=J[:,index];steps=[]
        # Unit coefficients are not all the same scale; the cl and core probes
        # use the same relative physical steps as earlier validated tests.
        magnitude=max(1.,abs(p[index])) if index<24 else max(1.,abs(extra[index-24]))
        for h in (2e-5*magnitude,1e-5*magnitude):
            values=[model.fun(p+factor*h*direction[:24],extra+factor*h*direction[24:]) for factor in (2,1,-1,-2)]
            fd=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h)
            steps.append({'step':h,'relative_error':rel(fd,analytic),
                'max_abs_error':float(np.max(abs(fd-analytic)))})
        row={'direction':'core_'+str(index) if index<24 else 'extra_'+str(index-24),
            'steps':steps,'passed':bool(all(item['relative_error']<3e-5 for item in steps))}
        report['raw_checks'].append(row);atomic(output,report)
    chart=AbsoluteC5ChartV2(p);T=chart.base_tangent
    reduced=np.column_stack((J[:,:24]@T,J[:,24:]))
    saved.update(core_tangent=T,feasible_jacobian=reduced)
    directions=[]
    for index in range(19):
        direction=np.zeros(19+len(extra));direction[index]=1
        directions.append(('feasible_core_'+str(index),direction))
    for index in range(4):
        direction=rng.normal(size=19+len(extra));direction/=np.linalg.norm(direction)
        directions.append(('feasible_mixed_'+str(index),direction))
    for name,direction in directions:
        scale=max(np.linalg.norm(np.r_[T@direction[:19],direction[19:]]),1e-300)
        direction=direction/scale;analytic=reduced@direction;steps=[]
        for h in (2e-4,1e-4):
            values=[];defects=[]
            for factor in (2,1,-1,-2):
                pp=chart.lift_delta(factor*h*direction[:19]);defects.append(hp_report(pp)['max_abs'])
                values.append(model.fun(pp,extra+factor*h*direction[19:]))
            fd=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h)
            steps.append({'physical_parameter_step':h,'relative_error':rel(fd,analytic),
                'max_abs_error':float(np.max(abs(fd-analytic))),'maximum_HP_defect':max(defects)})
        report['feasible_checks'].append({'direction':name,'steps':steps,
            'passed':bool(all(item['relative_error']<1e-3 and item['maximum_HP_defect']<1e-10 for item in steps))})
        atomic(output,report)
    for index in range(3):
        v=rng.normal(size=reduced.shape[1]);w=rng.normal(size=reduced.shape[0]);
        jv=reduced@v;jtw=reduced.T@w
        left=float(w@jv);right=float(v@jtw)
        error=abs(left-right)/max(np.linalg.norm(w)*np.linalg.norm(jv),np.linalg.norm(v)*np.linalg.norm(jtw),1e-300)
        report['operator_checks'].append({'index':index,'adjoint_scaled_error':float(error),'passed':bool(error<1e-12)})
    final_file=directory/'derivatives.npz';npz(final_file,**saved)
    report.update(derivative_arrays_path=str(final_file),derivative_arrays_sha256=digest(final_file),
        derivative_mesh=derivative_mesh.record(),base_independent_HP=hp_report(p),
        full_cl_tested=True,all_19_feasible_core_directly_FD_checked=True,
        completed=True,selected_fastest_workers=min(report['benchmarks'],key=lambda item:item['cold_fun_seconds']+item['following_jacobian_seconds'])['BLAS_threads'])
    report['original_namespace_identity_at_finish']=original_namespace_identity_record()
    report['passed']=bool(all(row['passed'] for key in ('benchmarks','raw_checks','feasible_checks','operator_checks') for row in report[key])
        and unchanged['passed'] and report['original_namespace_identity_at_finish']['passed'])
    atomic(output,report)
    if not report['passed']:raise SystemExit(2)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--mesh',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=OUT/'model_benchmark_v3')
    parser.add_argument('--workers',type=int,nargs='+',default=[1,4,8])
    parser.add_argument('--block-size',type=int,default=1024)
    main(parser.parse_args())
