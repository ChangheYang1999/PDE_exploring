"""All-column whole-axis gradient blocks and independent refined-rule probes.

Diagnostic only: every feasible coefficient is retained, no optimizer runs,
and no derivative PASS establishes stationarity. Run through launch.py after
selecting an immutable accepted endpoint and allowing its campaign to stop.
"""
import argparse
import json
from pathlib import Path
import time

from absolute_common import ROOT,OUT,A_REF,np,read,atomic,npz,digest,array_hash,provenance
from absolute_model_v2 import AbsoluteLossProblem
from absolute_chart_v2 import AbsoluteC5ChartV2
from absolute_chart import hp_report
from stage13_model_v3 import CachedAbsoluteProblem,original_namespace_identity_record
from stage13_integration_v3 import EpochIntegrator
from stage13_solver import DenseTrustModel
from stage13_campaign_v3 import numerical_sources
from threadpoolctl import threadpool_limits


BLOCKS=('origin','middle','infinity')
DIRECTION_NAMES=('leading_gradient','complete_cl_feasible','complete_core_extra_mixed','weakest_positive_singular')


def relative(delta,reference):
    return float(np.linalg.norm(delta)/max(np.linalg.norm(reference),1e-300))


def summary(matrix,r,block_ids):
    block_vectors=np.asarray([matrix[block_ids==i].T@r[block_ids==i] for i in range(3)])
    full=matrix.T@r;assembled=np.sum(block_vectors,axis=0)
    rows={name:{'nodes':int(np.count_nonzero(block_ids==i)),
        'gradient_components':block_vectors[i].tolist(),'gradient_norm':float(np.linalg.norm(block_vectors[i])),
        'J_abs_contribution':float(r[block_ids==i]@r[block_ids==i]/2)} for i,name in enumerate(BLOCKS)}
    return {'gradient_components':full.tolist(),'gradient_norm':float(np.linalg.norm(full)),
        'gradient_max_abs':float(np.max(abs(full))),
        'gradient_blocks':rows,'block_sum_vs_direct_gradient_norm_difference':float(np.linalg.norm(assembled-full)),
        'block_cancellation_ratio':float(np.sum(np.linalg.norm(block_vectors,axis=1))/max(np.linalg.norm(full),1e-300)),
        'J_abs_mesh':float(r@r/2)},block_vectors


def new_array_path(path):
    if path.exists() or path.with_name(path.name+'.partial').exists():
        return path.with_name(path.stem+'_preserved_orphan_retry_'+str(time.time_ns())+path.suffix)
    return path


def normalize_physical(direction,tangent,scales):
    v=np.asarray(direction,dtype=float).copy()
    raw=np.r_[tangent@(scales[:19]*v[:19]),scales[19:]*v[19:]]
    length=float(np.linalg.norm(raw))
    if not np.isfinite(length) or length==0:raise ValueError('Representative direction has zero or unresolved physical length')
    return v/length,raw/length,length


def analytic_phase(folder,seed,p,extra,integrator,scales,args,saved_checkpoint_residual):
    record_path=folder/'analytic.json'
    if record_path.exists():
        record=read(record_path)
        if not record.get('completed') or digest(record['arrays_path'])!=record['arrays_sha256']:
            raise ValueError('Saved complete analytic gradient artifact changed')
        with np.load(record['arrays_path'],allow_pickle=False) as values:
            arrays={name:values[name].copy() for name in values.files}
        return record,arrays
    chart=AbsoluteC5ChartV2(p);tangent=chart.base_tangent
    train=CachedAbsoluteProblem(seed,integrator.mesh,A_REF,workers=args.workers,block_size=args.block_size)
    r=train.fun(p,extra);raw=train.jacobian(p,extra)
    training_unscaled=np.column_stack((raw[:,:24]@tangent,raw[:,24:]));matrix=training_unscaled*scales
    train.clear_cache();del train,raw
    reproducibility=float(np.linalg.norm(r-saved_checkpoint_residual))
    restore_tolerance=64*np.finfo(float).eps*max(np.linalg.norm(r),np.linalg.norm(saved_checkpoint_residual),1e-300)
    if reproducibility>restore_tolerance:raise ValueError('Accepted endpoint residual did not reproduce at64-epsilon relative tolerance')
    fine=CachedAbsoluteProblem(seed,integrator.refined_mesh,A_REF,workers=args.workers,block_size=args.block_size)
    fr=fine.fun(p,extra);fraw=fine.jacobian(p,extra)
    fine_unscaled=np.column_stack((fraw[:,:24]@tangent,fraw[:,24:]));fine_matrix=fine_unscaled*scales
    fine.clear_cache();del fine,fraw
    if matrix.shape[1]!=19+len(extra) or fine_matrix.shape[1]!=19+len(extra):
        raise ValueError('Every original and added feasible direction is required')
    training,train_blocks=summary(matrix,r,integrator.training_blocks)
    refined,fine_blocks=summary(fine_matrix,fr,integrator.refined_blocks)
    raw_training,raw_train_blocks=summary(training_unscaled,r,integrator.training_blocks)
    raw_refined,raw_fine_blocks=summary(fine_unscaled,fr,integrator.refined_blocks)
    model=DenseTrustModel(matrix,r);fmodel=DenseTrustModel(fine_matrix,fr)
    positives=np.flatnonzero(model.s>0)
    if not len(positives):raise ValueError('No positive singular direction is resolved; diagnose the complete matrix')
    gradient=model.gradient
    leading=-gradient.copy();fallback=False
    if np.linalg.norm(leading)==0:leading=model.vt[0].copy();fallback=True
    cl=np.r_[tangent[0]*scales[:19],np.zeros(len(extra))]
    mixed=np.random.default_rng(130013).normal(size=19+len(extra))
    weak=model.vt[positives[-1]].copy()
    seeds=(leading,cl,mixed,weak);directions=[];physical=[];metadata=[]
    for name,value in zip(DIRECTION_NAMES,seeds):
        v,raw,length=normalize_physical(value,tangent,scales)
        directions.append(v);physical.append(raw)
        metadata.append({'name':name,'coordinate_components':v.tolist(),'linearized_full_physical_components':raw.tolist(),
            'linearized_full_physical_norm':float(np.linalg.norm(raw)),
            'unscaled_selection_physical_norm':length,'complete_cl_component':float(raw[0]),
            'largest_singular_fallback_because_gradient_exact_zero':bool(fallback and name=='leading_gradient'),
            'weakest_direction_uses_smallest_exactly_positive_singular_pair_without_threshold':name=='weakest_positive_singular'})
    directions=np.asarray(directions);physical=np.asarray(physical)
    direct=AbsoluteLossProblem(seed,integrator.refined_mesh,A_REF,block_size=args.block_size)
    original=direct.fun(p,extra);original_difference=relative(original-fr,fr)
    total_delta=np.asarray(refined['gradient_components'])-np.asarray(training['gradient_components'])
    blocks_delta=fine_blocks-train_blocks
    record={'schema':'stage13_all_column_three_block_analytic_gradient_v3_origin20_private_scalar_exp','completed':True,
        'all_columns':19+len(extra),'all19_original_core_directions_retained':True,'all_extra_coefficients_retained':len(extra),
        'training':training,'refined':refined,'raw_training':raw_training,'raw_refined':raw_refined,
        'coordinate_metric':'training/refined gradients use all19+K feasible endpoint tangent columns multiplied by the unchanged positive campaign column scales; raw_training/raw_refined use the same full feasible tangent without those scales.',
        'training_spectrum':model.stationarity(),'refined_spectrum':fmodel.stationarity(),
        'full_singular_spectra_retained':True,'normal_equations_used':False,'weak_directions_deleted':False,
        'gradient_convergence':{'total_gradient_difference_norm':float(np.linalg.norm(total_delta)),
            'total_gradient_relative_difference':float(np.linalg.norm(total_delta)/max(np.linalg.norm(model.gradient),np.linalg.norm(fmodel.gradient),1e-300)),
            'total_relative_agreement_1e_3':bool(np.linalg.norm(total_delta)<1e-3*max(np.linalg.norm(model.gradient),np.linalg.norm(fmodel.gradient),1e-300)),
            'sum_block_gradient_difference_norms':float(np.sum(np.linalg.norm(blocks_delta,axis=1))),
            'by_block':{name:{'gradient_difference_components':blocks_delta[i].tolist(),
                'gradient_difference_norm':float(np.linalg.norm(blocks_delta[i])),
                'relative_to_larger_block_gradient':float(np.linalg.norm(blocks_delta[i])/max(np.linalg.norm(train_blocks[i]),np.linalg.norm(fine_blocks[i]),1e-300))} for i,name in enumerate(BLOCKS)},
            'rigorous_gradient_error_bound':False,'stationarity_accepted':False},
        'representative_directions':metadata,
        'direction_selection':{'leading_gradient':'Negative complete training-rule scaled feasible gradient, normalized to unit linearized full physical parameter length. If exactly zero at working precision, explicitly recorded largest-right-singular-vector fallback.',
            'complete_cl_feasible':'Completecl row of the full scaled feasible tangent, with no discarded core/extra direction.',
            'complete_core_extra_mixed':'Fixed seed130013 Gaussian vector in every one of the19+K coordinates, normalized in linearized full physical parameters.',
            'weakest_positive_singular':'Last exactly positive singular pair of the full training scaled feasible Jacobian; no numerical rank threshold.'},
        'endpoint_restore':{'difference_norm':reproducibility,'tolerance':float(restore_tolerance),'passed':True},
        'independent_fine_residual_comparison':{'reference':'Original stateless AbsoluteLossProblem, independent of the cached analytic-Jacobian provider',
            'relative_difference':original_difference,'threshold':5e-9,'passed':bool(original_difference<5e-9)},
        'training_feasible_matrix_sha256':array_hash(matrix),'refined_feasible_matrix_sha256':array_hash(fine_matrix),
        'stationarity_accepted':False}
    arrays={'p':p,'extra':extra,'core_tangent':tangent,'column_scales':scales,
        'training_residual':r,'refined_residual':fr,'original_refined_residual':original,
        'scaled_block_gradients_training':train_blocks,'scaled_block_gradients_refined':fine_blocks,
        'raw_block_gradients_training':raw_train_blocks,'raw_block_gradients_refined':raw_fine_blocks,
        'training_singular_values':model.s,'refined_singular_values':fmodel.s,
        'training_right_singular_vectors':model.vt,'refined_right_singular_vectors':fmodel.vt,
        'directions':directions,'physical_directions':physical,
        'analytic_training_directional_derivatives':matrix@directions.T,
        'analytic_refined_directional_derivatives':fine_matrix@directions.T}
    array_path=new_array_path(folder/'analytic.npz');npz(array_path,**arrays)
    record.update(arrays_path=str(array_path),arrays_sha256=digest(array_path));atomic(record_path,record)
    return record,arrays


def probe(folder,model,chart,p,extra,scales,direction,h,factor,args):
    tag='h_'+format(h,'.12g').replace('.','p')+'_factor_'+str(int(factor)).replace('-','minus')
    path=folder/'probes'/(tag+'.json');path.parent.mkdir(exist_ok=True)
    delta=factor*h*scales*direction
    pp=chart.lift_delta(delta[:19]);ee=extra+delta[19:];hp=hp_report(pp)
    if hp['max_abs']>=1e-10 or not hp['physical_bounds'] or abs(hp['a0'])<=1e-12:
        raise ValueError('Independent refined-grid feasible probe fails unchanged C5/admissibility')
    if path.exists():
        record=read(path)
        if not record.get('completed') or record['p']!=pp.tolist() or record['extra_sha256']!=array_hash(ee):
            raise ValueError('Saved independent probe belongs to different physical coefficients')
        if digest(record['arrays_path'])!=record['arrays_sha256']:raise ValueError('Saved independent probe arrays changed')
        with np.load(record['arrays_path'],allow_pickle=False) as data:
            if not np.array_equal(data['p'],pp) or not np.array_equal(data['extra'],ee):
                raise ValueError('Independent probe parameter arrays changed')
            rr=data['residual'].copy()
        return {**record,'record_path':str(path),'record_sha256':digest(path)},rr
    began=time.time();rr=model.fun(pp,ee)
    arrays=new_array_path(path.with_suffix('.npz'));npz(arrays,p=pp,extra=ee,residual=rr)
    lift_info=(chart.last_diagnostics if np.any(delta[:19]) else
        {'version':chart.version,'zero_core_coordinate_step':True,'core_endpoint_preserved_bitwise':True,'independent_HP':hp})
    record={'completed':True,'h':h,'factor':factor,'p':pp.tolist(),'extra_sha256':array_hash(ee),
        'linearized_physical_parameter_step':factor*h,'actual_full_physical_displacement_norm':float(np.linalg.norm(np.r_[pp-p,ee-extra])),
        'five_Taylor':hp,'chart_lift':lift_info,'independent_value_provider':'Original stateless AbsoluteLossProblem on the independently refined whole-axis rule',
        'arrays_path':str(arrays),'arrays_sha256':digest(arrays),'residual_sha256':array_hash(rr),'seconds':time.time()-began}
    atomic(path,record);return {**record,'record_path':str(path),'record_sha256':digest(path)},rr


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--campaign',type=Path,required=True);parser.add_argument('--label',required=True)
    parser.add_argument('--workers',type=int,default=4);parser.add_argument('--physical-step',type=float,default=2e-4)
    parser.add_argument('--block-size',type=int,default=1024);parser.add_argument('--resume',action='store_true')
    args=parser.parse_args()
    if not args.label or any(char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for char in args.label):parser.error('Simple label required')
    if not np.isfinite(args.physical_step) or args.physical_step<=0 or args.workers<1 or args.block_size<1:parser.error('Positive finite probe step and worker/block settings required')
    began=time.time();campaign=args.campaign.resolve();state=read(campaign/'state.json')
    identity_at_start=original_namespace_identity_record()
    if not identity_at_start['passed']:raise ValueError('Old independent field namespace changed')
    seed=read(state['parent_candidate_path']);p=np.asarray(state['p'],dtype=float);extra=np.asarray(state['extra'],dtype=float)
    if state['source_sha256']!=numerical_sources():raise ValueError('Campaign numerical source closure changed')
    for path_key,hash_key in (('candidate_path','candidate_sha256'),('arrays_path','arrays_sha256'),('epoch_path','epoch_sha256'),('coordinate_map_path','coordinate_map_sha256'),('parent_candidate_path','parent_candidate_sha256')):
        if digest(state[path_key])!=state[hash_key]:raise ValueError('Accepted endpoint artifact changed: '+path_key)
    integrator=EpochIntegrator(seed,Path(state['epoch_path']));integrator.require_qualified(state['epoch_anchor_candidate'],args.workers)
    with np.load(state['arrays_path'],allow_pickle=False) as values:
        if not np.array_equal(values['p'],p) or not np.array_equal(values['extra'],extra):raise ValueError('Checkpoint physical arrays do not match campaign')
        saved_r=values['residual'].copy()
    with np.load(state['coordinate_map_path'],allow_pickle=False) as values:scales=values['column_scales'].copy()
    dimension=19+len(extra)
    if scales.shape!=(dimension,) or np.any(scales<=0) or not np.all(np.isfinite(scales)):raise ValueError('All181-or-larger positive coordinate scales must be retained')
    folder=OUT/'gradient_refinement_v3'/args.label
    binding={'candidate_sha256':state['candidate_sha256'],'arrays_sha256':state['arrays_sha256'],
        'epoch_sha256':state['epoch_sha256'],'coordinate_map_sha256':state['coordinate_map_sha256'],
        'candidate_path':state['candidate_path'],'campaign_path':str(campaign),'dimension':dimension,
        'training_mesh_sha256':integrator.mesh.fingerprint,'refined_mesh_sha256':integrator.refined_mesh.fingerprint,
        'mesh_file_sha256':{key:row['sha256'] for key,row in integrator.record['meshes'].items()},
        'physical_step':args.physical_step,'workers':args.workers,'block_size':args.block_size,
        'source_sha256':{**numerical_sources(),'stage13_gradient_refinement_v3.py':digest(Path(__file__)),
            'base/spectral_basis.py':digest(ROOT/'base/spectral_basis.py')},
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'production_cached_provider':'stage13_model_v3.CachedAbsoluteProblem',
        'independent_refined_value_provider':'Unchanged absolute_model_v2.AbsoluteLossProblem'}
    if folder.exists():
        if not args.resume:raise ValueError('Existing diagnostic requires explicit --resume')
        if read(folder/'binding.json')!=binding:raise ValueError('Endpoint, mesh, coordinate, source or probe settings changed')
        if (folder/'checks.json').exists():raise ValueError('Completed refinement diagnostics are immutable; use a fresh label')
    else:folder.mkdir(parents=True);atomic(folder/'binding.json',binding)
    with threadpool_limits(limits=args.workers,user_api='blas'):
        analytic,arrays=analytic_phase(folder,seed,p,extra,integrator,scales,args,saved_r)
        if not np.array_equal(arrays['p'],p) or not np.array_equal(arrays['extra'],extra) or not np.array_equal(arrays['column_scales'],scales):
            raise ValueError('Saved analytic phase belongs to another endpoint or coordinate map')
        chart=AbsoluteC5ChartV2(p)
        if not np.array_equal(chart.base_tangent,arrays['core_tangent']):raise ValueError('The complete feasible tangent did not restore bit for bit')
        original=AbsoluteLossProblem(seed,integrator.refined_mesh,A_REF,block_size=args.block_size)
        rows=[]
        for index,name in enumerate(DIRECTION_NAMES):
            directory=folder/name;directory.mkdir(exist_ok=True);record_path=directory/'checks.json'
            if record_path.exists():
                row=read(record_path)
                if digest(row['arrays_path'])!=row['arrays_sha256']:raise ValueError('Completed direction derivative arrays changed')
                rows.append(row);continue
            direction=arrays['directions'][index];expected=arrays['analytic_refined_directional_derivatives'][:,index]
            steps=[];derivatives=[];all_probes=[]
            for h in (args.physical_step,args.physical_step/2):
                values=[];records=[]
                for factor in (-2.,-1.,1.,2.):
                    record,value=probe(directory,original,chart,p,extra,scales,direction,h,factor,args)
                    values.append(value);records.append(record)
                derivative=(values[0]-8*values[1]+8*values[2]-values[3])/(12*h)
                derivatives.append(derivative);all_probes.append(records)
                block_gradient_components={}
                for block_id,block_name in enumerate(BLOCKS):
                    use=integrator.refined_blocks==block_id
                    block_gradient_components[block_name]={'FD_residual_direction_dot':float(arrays['original_refined_residual'][use]@derivative[use]),
                        'analytic_residual_direction_dot':float(arrays['refined_residual'][use]@expected[use])}
                steps.append({'physical_parameter_step':h,'FD_analytic_relative_disagreement':relative(derivative-expected,expected),
                    'FD_derivative_norm':float(np.linalg.norm(derivative)),'analytic_derivative_norm':float(np.linalg.norm(expected)),
                    'FD_directional_gradient':float(arrays['original_refined_residual']@derivative),
                    'analytic_directional_gradient':float(arrays['refined_residual']@expected),
                    'directional_gradient_abs_disagreement':abs(float(arrays['original_refined_residual']@derivative-arrays['refined_residual']@expected)),
                    'by_block_directional_gradients':block_gradient_components,
                    'maximum_probe_five_Taylor_defect':max(record['five_Taylor']['max_abs'] for record in records)})
            difference=relative(derivatives[0]-derivatives[1],derivatives[1])
            path=new_array_path(directory/'derivatives.npz');npz(path,derivative_h=derivatives[0],derivative_half_h=derivatives[1],
                analytic_refined_derivative=expected,analytic_training_derivative=arrays['analytic_training_directional_derivatives'][:,index],
                coordinate_direction=direction,linearized_physical_direction=arrays['physical_directions'][index])
            row={'name':name,'completed':True,'direction_metadata':analytic['representative_directions'][index],
                'steps':steps,'two_step_derivative_relative_disagreement':difference,
                'two_step_directional_gradient_abs_disagreement':abs(steps[0]['FD_directional_gradient']-steps[1]['FD_directional_gradient']),
                'passed':bool(all(step['FD_analytic_relative_disagreement']<1e-3 for step in steps) and difference<1e-3),
                'probe_records':all_probes,'arrays_path':str(path),'arrays_sha256':digest(path),
                'passed_scope':'Representative derivative agreement only; neither a small directional gradient nor a PASS establishes full stationarity.'}
            atomic(record_path,row);rows.append(row)
            atomic(folder/'progress.json',{'completed_directions':len(rows),'required_representative_directions':4,
                'all_analytic_columns':dimension,'completed':False,'failed_directions':[item['name'] for item in rows if not item['passed']]})
            print(json.dumps({'direction':name,'passed':row['passed'],'completed_directions':len(rows)}),flush=True)
    identity_at_finish=original_namespace_identity_record()
    current=read(campaign/'state.json')
    unchanged=all(current.get(key)==state.get(key) for key in ('candidate_sha256','arrays_sha256','epoch_sha256','coordinate_map_sha256','accepted'))
    result={'schema':'stage13_three_block_gradient_refinement_v3_origin20_private_scalar_exp','completed':True,
        'passed':bool(unchanged and identity_at_finish['passed'] and analytic['independent_fine_residual_comparison']['passed'] and all(row['passed'] for row in rows)),
        'passed_scope':'Endpoint artifact restoration, independent refined residual provider agreement, and four representative two-step derivative checks. Gradient quadrature convergence is reported separately and stationarity is never accepted automatically.',
        'endpoint_binding':binding,'candidate_unchanged_during_diagnostic':unchanged,'dimension':dimension,
        'production_origin_order':20,'all_raw_origin_derivative_order':20,'physical_model_or_objective_changed':False,
        'all_19_core_and_every_extra_column_retained':True,'normal_equations_used':False,'weak_directions_deleted':False,
        'analytic_record_path':str(folder/'analytic.json'),'analytic_record_sha256':digest(folder/'analytic.json'),
        'analytic_arrays_path':analytic['arrays_path'],'analytic_arrays_sha256':analytic['arrays_sha256'],
        'analytic':analytic,'gradient_convergence':analytic['gradient_convergence'],'representative_directions':rows,
        'direction_records':[{'name':name,'path':str(folder/name/'checks.json'),
            'sha256':digest(folder/name/'checks.json'),'passed':read(folder/name/'checks.json')['passed']} for name in DIRECTION_NAMES],
        'stationarity_accepted':False,'rigorous_error_certificate':False,
        'stationarity_status':'Pending interpretation of full gradients, block cancellation, refined quadrature differences, independent FD probes and weak-direction precision.',
        'optimization_performed':False,'elapsed_seconds':time.time()-began,'environment':provenance(),
        'production_cached_provider':'stage13_model_v3.CachedAbsoluteProblem',
        'independent_refined_value_provider':'Unchanged absolute_model_v2.AbsoluteLossProblem',
        'original_namespace_identity_at_start':identity_at_start,
        'original_namespace_identity_at_finish':identity_at_finish}
    atomic(folder/'checks.json',result);atomic(folder/'progress.json',{'completed_directions':4,'all_analytic_columns':dimension,'completed':True,'passed':result['passed']})
    print(json.dumps({'path':str(folder/'checks.json'),'completed':True,'passed':result['passed'],'stationarity_accepted':False}),flush=True)
    if not result['passed']:raise SystemExit(2)


if __name__=='__main__':main()
