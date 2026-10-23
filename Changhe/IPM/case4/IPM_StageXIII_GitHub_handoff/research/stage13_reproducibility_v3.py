"""Diagnose unchanged-endpoint residual reproducibility without changing gates.

Use launch.py. Three fresh cached4 evaluations retain all vectors and comparisons. The
unchanged stateless reference is freshly tested by the full model benchmark;
previous stateless replay controls remain archived provenance. This worker never
relaxes a tolerance, publishes a passed epoch, modifies a candidate, or starts
an optimizer. Its64-epsilon comparisons are diagnostic observations only.
"""
import argparse
from pathlib import Path
import time

from absolute_common import ROOT,OUT,A_REF,np,read,atomic,npz,digest,array_hash,provenance
from absolute_model import FrozenLogMesh
from stage13_model_v3 import CachedAbsoluteProblem,original_namespace_identity_record,_EXP
from stage13_integration_v3 import EpochIntegrator,_evaluate,integration_sources
from stage13_campaign import numerical_sources
from threadpoolctl import threadpool_limits,threadpool_info


def compare(a,b,mesh):
    delta=np.asarray(a)-np.asarray(b);index=int(np.argmax(abs(delta)))
    difference=float(np.linalg.norm(delta));anorm=float(np.linalg.norm(a));bnorm=float(np.linalg.norm(b))
    existing=64*np.finfo(float).eps*max(anorm,bnorm,1e-300)
    radius=float(np.exp(mesh.s[index]));angle=float(mesh.theta[index])
    return {'bitwise_equal':bool(np.array_equal(a,b)),'difference_norm':difference,
        'difference_max_abs':float(abs(delta[index])),'relative_difference_norm':difference/max(anorm,bnorm,1e-300),
        'norm_a':anorm,'norm_b':bnorm,'J_abs_a':float(np.asarray(a)@a/2),'J_abs_b':float(np.asarray(b)@b/2),
        'existing_64epsilon_threshold':float(existing),'difference_divided_by_existing_threshold':difference/existing,
        'within_existing_64epsilon_threshold':bool(difference<=existing),
        'maximum_difference_location':{'index':index,'log_radius':float(mesh.s[index]),'theta':angle,'radius':radius,
            'xy':[radius*float(np.cos(angle)),radius*float(np.sin(angle))]},
        'quantity':'Weighted absolute-loss residual vector, including the fixed sqrt(2w/(pi*a_ref^2)) factor',
        'tolerance_was_changed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start',type=Path,required=True)
    parser.add_argument('--epoch-design',type=Path,default=ROOT/'integration_epochs/epoch0003_v3_w4/epoch_design.json')
    parser.add_argument('--initial-npz',type=Path,default=ROOT/'integration_epochs/epoch0003_v3_w4/endpoint_initial.npz')
    parser.add_argument('--benchmark-checks',type=Path,default=OUT/'model_benchmark_v3/checks.json')
    parser.add_argument('--label',required=True);parser.add_argument('--workers',type=int,nargs='+',default=[4])
    parser.add_argument('--methods',nargs='+',choices=('cached','stateless'),default=['cached'])
    parser.add_argument('--repeats',type=int,default=3);parser.add_argument('--block-size',type=int,default=1024)
    args=parser.parse_args()
    if not args.label or any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for char in args.label):parser.error('Simple fresh label required')
    if args.repeats<2 or args.repeats>8 or args.block_size<1 or any(value<1 for value in args.workers):parser.error('Two to eight repeats and positive worker/block counts required')
    if len(set(args.workers))!=len(args.workers) or len(set(args.methods))!=len(args.methods):parser.error('Do not repeat methods or worker settings')
    folder=OUT/'reproducibility'/args.label
    if folder.exists():raise ValueError('Reproducibility output exists; preserve it and choose a fresh label')
    folder.mkdir(parents=True)
    began=time.time();case=read(args.start);p=np.asarray(case.get('core_parameters',[case['cl']]+case['coefficients'][1:]),dtype=float)
    extra=np.asarray(case.get('extra_coefficients',[]),dtype=float)
    integrator=EpochIntegrator(case,args.epoch_design);mesh=integrator.mesh
    with np.load(args.initial_npz,allow_pickle=False) as arrays:
        initial=arrays['residual'].copy();ip=arrays['p'].copy();ie=arrays['extra'].copy()
    benchmark=read(args.benchmark_checks)
    if benchmark.get('schema')!='stage13_actual_model_cache_benchmark_v3_origin20_private_scalar_exp' or not benchmark.get('completed') or not benchmark.get('passed'):
        raise ValueError('A completed passed fresh V3 full benchmark is required')
    if not benchmark.get('old_independent_provider_after_private_evaluations',{}).get('passed'):
        raise ValueError('Benchmark must retain the old stateless before/after namespace and numerical control')
    reference_path=Path(benchmark['reference_arrays_path'])
    if digest(reference_path)!=benchmark['reference_arrays_sha256']:raise ValueError('Benchmark reference arrays changed')
    with np.load(reference_path,allow_pickle=False) as arrays:
        reference=arrays['residual'].copy();bp=arrays['p'].copy();be=arrays['extra'].copy()
    if initial.shape!=(mesh.size,) or reference.shape!=initial.shape or benchmark['mesh_sha256']!=mesh.fingerprint:
        raise ValueError('Saved initial and benchmark residuals must use this exact training rule')
    sources={**numerical_sources(),**integration_sources(),'stage13_reproducibility_v3.py':digest(Path(__file__)),
        'stage13_model_v3.py':digest(ROOT/'stage13_model_v3.py'),'stage13_stable_exp.py':digest(ROOT/'stage13_stable_exp.py')}
    inputs={str(path.resolve()):digest(path) for path in (args.start,args.epoch_design,args.initial_npz,args.benchmark_checks,reference_path)}
    record={'schema':'stage13_unchanged_endpoint_reproducibility_diagnostic_v3_origin20_private_scalar_exp','label':args.label,
        'completed':False,'diagnostic_not_epoch_qualification':True,'optimization_performed':False,
        'tolerance_relaxation_performed':False,'passed_epoch_written':False,
        'production_origin_order':20,'all_raw_origin_derivative_order':20,'physical_model_or_objective_changed':False,'a_ref':A_REF,'candidate_path':str(args.start.resolve()),'candidate_sha256':digest(args.start),
        'input_sha256':inputs,'source_sha256':sources,'integration_source_sha256':integration_sources(),
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'training_mesh':mesh.record(),'workers':args.workers,'methods':args.methods,'fresh_repeats_per_method_and_workers':args.repeats,
        'fresh_cached_instance_for_each_repeat':True,'block_size':args.block_size,
        'exact_input_scalar_exp_LRU_cleared_before_each_cached_repeat':True,
        'cache_counters_or_resource_ledgers_reset':False,
        'initial_npz_path':str(args.initial_npz.resolve()),'benchmark_reference_path':str(reference_path),
        'parameter_bitwise_comparisons':{'input_p_equals_initial':bool(np.array_equal(p,ip)),
            'input_extra_equals_initial':bool(np.array_equal(extra,ie)),
            'input_p_equals_benchmark':bool(np.array_equal(p,bp)),
            'input_extra_equals_benchmark':bool(np.array_equal(extra,be)),
            'p_sha256':array_hash(p),'extra_sha256':array_hash(extra),
            'initial_p_sha256':array_hash(ip),'initial_extra_sha256':array_hash(ie),
            'benchmark_p_sha256':array_hash(bp),'benchmark_extra_sha256':array_hash(be)},
        'initial_vs_benchmark':compare(initial,reference,mesh),'runs':[],'pairwise_comparisons':[],
        'environment_at_start':provenance(),
        'selected_runtime_workers':4,'baseline_cached_residual_is_V3':True,
        'independent_stateless_provider':'Unchanged absolute_model_v2 / absolute_fields_v2',
        'stateless_control_provenance':{'fresh_full_benchmark_checks_path':str(args.benchmark_checks.resolve()),
            'fresh_full_benchmark_checks_sha256':digest(args.benchmark_checks),
            'before_and_after_old_provider_control':benchmark['old_independent_provider_after_private_evaluations'],
            'previous_V2_replay_controls':'Archived provenance only; not relabeled as fresh V3 runs'},
        'original_namespace_identity_at_start':original_namespace_identity_record()}
    output=folder/'checks.json';atomic(output,record)
    if not all(record['parameter_bitwise_comparisons'][name] for name in ('input_p_equals_initial','input_extra_equals_initial','input_p_equals_benchmark','input_extra_equals_benchmark')):
        record.update(completed=True,diagnosis='Physical parameter vectors are not identical; no repeat runs launched.')
        atomic(output,record);raise SystemExit(2)
    arrays_path=folder/'references.npz';npz(arrays_path,p=p,extra=extra,initial=initial,benchmark=reference,s=mesh.s,theta=mesh.theta,weights=mesh.weights)
    record.update(reference_artifact_path=str(arrays_path),reference_artifact_sha256=digest(arrays_path));atomic(output,record)
    vectors=[]
    for workers in args.workers:
        for method in args.methods:
            for repeat in range(args.repeats):
                label=method+'_workers'+str(workers)+'_repeat'+str(repeat+1);start=time.time()
                with threadpool_limits(limits=workers,user_api='blas'):
                    before=threadpool_info();environment=provenance()
                    identity_before=original_namespace_identity_record()
                    if not identity_before['passed']:raise RuntimeError('Original stateless namespace identity changed')
                    if method=='stateless':
                        _,rr=_evaluate(case,p,extra,mesh,workers,block_size=args.block_size)
                        duplicate=None;cache=None;exp_cache_clear=None
                    else:
                        before_clear=_EXP.metadata();counters={key:before_clear[key] for key in ('calls','hits','misses','evictions','peak_entries')}
                        _EXP.cache.clear();after_clear=_EXP.metadata()
                        if after_clear['current_entries']!=0 or any(after_clear[key]!=value for key,value in counters.items()):
                            raise RuntimeError('Pure LRU clear changed counters or retained old scalar values')
                        exp_cache_clear={'performed':True,'before':before_clear,'after':after_clear,
                            'counters_reset':False,'resource_ledgers_reset':False}
                        model=CachedAbsoluteProblem(case,mesh,A_REF,workers=workers,block_size=args.block_size)
                        rr=model.fun(p,extra);duplicate=model.fun(p,extra);cache=model.cache_record();model.clear_cache();del model
                    after=threadpool_info();identity_after=original_namespace_identity_record()
                    if not identity_after['passed']:raise RuntimeError('Original stateless namespace identity changed')
                path=folder/(label+'.npz')
                arrays={'p':p,'extra':extra,'residual':rr,'difference_from_initial':rr-initial,'difference_from_benchmark':rr-reference}
                if duplicate is not None:arrays['duplicate_cached_residual']=duplicate
                npz(path,**arrays)
                row={'label':label,'method':method,'workers':workers,'repeat':repeat+1,'fresh_instance':True,
                    'seconds':time.time()-start,'threadpools_inside_context_before':before,'threadpools_inside_context_after':after,
                    'environment_inside_context':environment,'cache':cache,'scalar_exp_LRU_clear_before_cold_instance':exp_cache_clear,
                    'original_namespace_identity_before':identity_before,'original_namespace_identity_after':identity_after,
                    'comparison_to_initial':compare(rr,initial,mesh),'comparison_to_benchmark':compare(rr,reference,mesh),
                    'duplicate_cache_control':compare(rr,duplicate,mesh) if duplicate is not None else None,
                    'artifact_path':str(path),'artifact_sha256':digest(path),'residual_sha256':array_hash(rr)}
                record['runs'].append(row);vectors.append((label,workers,method,rr));atomic(output,record)
                print(__import__('json').dumps({'run':label,'difference_to_initial':row['comparison_to_initial']['difference_norm'],
                    'ratio_to_existing_64eps':row['comparison_to_initial']['difference_divided_by_existing_threshold']}),flush=True)
    for index,(label_a,workers_a,method_a,a) in enumerate(vectors):
        for label_b,workers_b,method_b,b in vectors[index+1:]:
            record['pairwise_comparisons'].append({'a':label_a,'b':label_b,
                'same_workers':workers_a==workers_b,'same_provider':method_a==method_b,'comparison':compare(a,b,mesh)})
    record['within_provider_and_workers_summary']=[]
    for workers in args.workers:
        for method in args.methods:
            selected=[row for row in record['pairwise_comparisons'] if row['same_workers'] and row['same_provider']
                and row['a'].startswith(method+'_workers'+str(workers)+'_')]
            record['within_provider_and_workers_summary'].append({'workers':workers,'method':method,
                'all_bitwise_equal':all(row['comparison']['bitwise_equal'] for row in selected),
                'maximum_repeat_difference_norm':max(row['comparison']['difference_norm'] for row in selected),
                'maximum_repeat_difference_to_existing_64eps_ratio':max(row['comparison']['difference_divided_by_existing_threshold'] for row in selected)})
    record.update(completed=True,elapsed_seconds=time.time()-began,
        candidate_and_input_files_unchanged=all(Path(path).is_file() and digest(path)==sha for path,sha in inputs.items()),
        physical_parameter_arrays_unchanged=bool(np.array_equal(p,ip) and np.array_equal(extra,ie)),
        numerical_sources_unchanged=all(digest(ROOT/name)==sha for name,sha in sources.items()),
        diagnosis='Recorded repeat, provider and BLAS-setting differences. No numerical reproducibility tolerance or qualification status has been changed.',
        environment_at_finish=provenance(),original_namespace_identity_at_finish=original_namespace_identity_record())
    atomic(output,record)
    print(__import__('json').dumps({'path':str(output),'completed':True,'tolerance_relaxation_performed':False,
        'passed_epoch_written':False,'candidate_unchanged':record['candidate_and_input_files_unchanged']}),flush=True)
    if not record['candidate_and_input_files_unchanged'] or not record['physical_parameter_arrays_unchanged'] or not record['numerical_sources_unchanged'] or not record['original_namespace_identity_at_finish']['passed']:
        raise SystemExit(2)


if __name__=='__main__':main()
