"""Version 3 all-column absolute campaign with an immutable version 1 parent.

Every accepted candidate has an immutable snapshot and authoritative trial
commit. A time slice is never called convergence. All numerical work is launched
by the parent through the verified Mac Pro resource supervisor.
"""
import argparse
import json
import os
from pathlib import Path
import signal
import time

from absolute_common import ROOT,OUT,A_REF,np,read,atomic,npz,digest,array_hash,provenance
from absolute_chart_v2 import AbsoluteC5ChartV2
from absolute_chart import hp_report
from absolute_fields_v2 import prepare_candidate
from stage13_solver import DenseTrustModel

STOP=False


def request_stop(signum,frame):
    global STOP
    STOP=True


def append(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('a') as stream:
        stream.write(json.dumps(value,allow_nan=False)+'\n');stream.flush();os.fsync(stream.fileno())


def numerical_sources():
    # The copied legacy closure is immutable. Only actual new numerical
    # dependencies are added; unrelated future reports do not alter a resume.
    names=list(read(ROOT/'workspace.json')['source_python_sha256'])
    names+=['stage13_solver.py','stage13_campaign.py','stage13_model.py','stage13_integration.py',
        'absolute_fields_v2.py','absolute_model_v2.py','stage13_model_v2.py','stage13_integration_v2.py',
        'stage13_stable_exp.py','stage13_model_v3.py','stage13_integration_v3.py',
        'stage13_qualification_v3.py','stage13_model_benchmark_v3.py','stage13_qualification_review_v3.py',
        'stage13_reproducibility_v3.py','stage13_campaign_v3.py']
    return {name:digest(ROOT/name) for name in sorted(set(names))}


def parent_continuation(args):
    """Bind a stopped parent without modifying its state or source identities."""
    parent=args.parent_campaign.resolve();state_path=parent/'state.json'
    if parent==ROOT/'campaign'/args.label or ROOT/'campaign' not in parent.parents:
        raise ValueError('An independent stopped parent campaign inside this workspace is required')
    state=read(state_path)
    if state.get('status') in ('running','checkpointed_slice'):
        raise ValueError('The parent must be stopped for explicit diagnosis, rather than continuing concurrently')
    for name,sha in state['source_sha256'].items():
        if digest(ROOT/name)!=sha:raise ValueError('A frozen parent numerical source changed: '+name)
    for key,sha_key in [('candidate_path','candidate_sha256'),('arrays_path','arrays_sha256'),
            ('epoch_path','epoch_sha256'),('coordinate_map_path','coordinate_map_sha256'),
            ('parent_candidate_path','parent_candidate_sha256')]:
        if digest(state[key])!=state[sha_key]:raise ValueError('A parent incumbent artifact changed: '+key)
    if digest(args.start)!=state['candidate_sha256']:
        raise ValueError('Version 3 must start from the exact accepted parent snapshot JSON')
    seed=read(args.start)
    p=np.asarray(seed['core_parameters'],dtype=float);extra=np.asarray(seed['extra_coefficients'],dtype=float)
    if p.tobytes()!=np.asarray(state['p'],dtype=float).tobytes() or extra.tobytes()!=np.asarray(state['extra'],dtype=float).tobytes():
        raise ValueError('The independent core or extra parameters changed at the version boundary')
    with np.load(state['arrays_path'],allow_pickle=False) as arrays:
        if arrays['p'].tobytes()!=p.tobytes() or arrays['extra'].tobytes()!=extra.tobytes():
            raise ValueError('The parent serialized coefficient arrays differ from its accepted JSON')
    if seed['modes']!=state['modes'] or len(extra)!=state['expected_extra']:
        raise ValueError('The parent spectral modes or coefficient count changed')
    commits=[];accepted=0;incomplete_rejected_vectors=[]
    for index,path in enumerate(sorted((parent/'commits').glob('event_*.json')),1):
        value=read(path)
        if value['trial']['event_sequence']!=index or value['post_state']['events']!=index:
            raise ValueError('The parent immutable event sequence is incomplete')
        accepted+=int(bool(value['trial'].get('accepted')))
        if (not value['trial'].get('accepted') and value['trial'].get('trial_p')
                and not value['trial'].get('complete_trial_proposal')):
            incomplete_rejected_vectors.append(value['trial'].get('trial'))
        commits.append({'path':str(path),'sha256':digest(path),'accepted':bool(value['trial'].get('accepted'))})
    if len(commits)!=state['events'] or accepted!=state['accepted']:
        raise ValueError('The parent accepted/event counters differ from its immutable history')
    original_sources=read(ROOT/'workspace.json')['source_python_sha256']
    # This is a content check of all actually used original source names; its
    # historical reference-map values remain provenance rather than overrides.
    source_bindings={name:digest(ROOT/name) for name in original_sources}
    return {'schema':'stage13_exact_version_parent_v1','campaign_path':str(parent),
        'state_path':str(state_path),'state_sha256':digest(state_path),
        'candidate_path':state['candidate_path'],'candidate_sha256':state['candidate_sha256'],
        'arrays_path':state['arrays_path'],'arrays_sha256':state['arrays_sha256'],
        'epoch_path':state['epoch_path'],'epoch_sha256':state['epoch_sha256'],
        'coordinate_map_path':state['coordinate_map_path'],'coordinate_map_sha256':state['coordinate_map_sha256'],
        'source_sha256':state['source_sha256'],'copied_original_source_actual_sha256':source_bindings,
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'input_manifest_sha256':digest(ROOT/'inputs/candidates.json'),
        'commits':commits,'parent_status':state['status'],'parent_accepted':state['accepted'],
        'parent_trials':state['trials'],'parent_events':state['events'],
        'cumulative_parent_accepted':state.get('cumulative_parent_accepted',0)+state['accepted'],
        'cumulative_parent_trials':state.get('cumulative_parent_trials',0)+state['trials'],
        'parent_elapsed_worker_seconds':state.get('cumulative_parent_worker_seconds',0)+state.get('elapsed_worker_seconds',0),
        'parent_validation':state['validation'],'parent_objective':state['objective'],
        'p_sha256':array_hash(p),'extra_sha256':array_hash(extra),
        'original_core_extra_and_modes_bitwise_unchanged':True,
        'physical_candidate_reoptimized_or_refitted_at_transition':False,
        'parent_rejected_trials_without_saved_complete_vectors':incomplete_rejected_vectors,
        'parent_rejected_vector_limitation':'The historical records remain exactly as saved. A trial_p and extra SHA alone do not establish a recovered full rejected candidate; any reconstruction needs its own exact identity proof.',
        'old_history_or_counters_reset':False}


def verify_parent_continuation(binding):
    if digest(binding['state_path'])!=binding['state_sha256']:
        raise ValueError('The immutable stopped parent state changed')
    for key in ('candidate','arrays','epoch','coordinate_map'):
        if digest(binding[key+'_path'])!=binding[key+'_sha256']:
            raise ValueError('The stopped parent artifact changed: '+key)
    for item in binding['commits']:
        if digest(item['path'])!=item['sha256']:raise ValueError('A parent immutable event changed')
    for name,sha in binding['source_sha256'].items():
        if digest(ROOT/name)!=sha:raise ValueError('A parent numerical source changed: '+name)
    if digest(ROOT/'provenance/base_manifest.json')!=binding['base_manifest_sha256'] or digest(ROOT/'inputs/candidates.json')!=binding['input_manifest_sha256']:
        raise ValueError('The original dependency or input manifest changed')


class TrackedModel:
    def __init__(self,model,directory):
        self.model=model;self.path=directory/'numerical_calls.jsonl'
        self.fun_calls=self.jac_calls=0

    def _call(self,kind,p,extra):
        token=str(time.time_ns());began=time.time()
        append(self.path,{'event':'started','id':token,'kind':kind,'epoch':began,
            'p':np.asarray(p).tolist(),'extra_sha256':array_hash(extra)})
        value=getattr(self.model,kind)(p,extra)
        append(self.path,{'event':'completed','id':token,'kind':kind,'epoch':time.time(),
            'seconds':time.time()-began,'array_sha256':array_hash(value),
            'shape':list(value.shape)})
        if kind=='fun':self.fun_calls+=1
        else:self.jac_calls+=1
        return value

    def fun(self,p,extra):return self._call('fun',p,extra)
    def jacobian(self,p,extra):return self._call('jacobian',p,extra)


def export_candidate(seed,p,extra,state,label):
    case=json.loads(json.dumps(seed))
    model=prepare_candidate(seed,'center_chart',parameters=p,extra=extra)
    case['historical_parent_objectives']=seed.get('objectives')
    case.update(stage='XIII',label=label,cl=float(p[0]),core_parameters=p.tolist(),
        coefficients=model['coefficients'].tolist(),coefficients_decimal=model['center_metadata']['coefficients_decimal'],
        extra_coefficients=extra.tolist(),a0=hp_report(p)['a0'],core_HP_analytic_center=hp_report(p),
        feasible_variables=19+len(extra),independent_parameters=24+len(extra),
        center_coefficient_policy='Exact analytic center elimination; serialized c0 is a display/checkpoint approximation, never an independent coefficient.',
        objectives={'J_abs_mesh':state['objective'],'J_abs_independent':state['validation']['J_abs'],
            'integration_error_diagnostic':state['validation']['error_abs']},
        stage13_parent_candidate_sha256=state['parent_candidate_sha256'],
        stage13_source_sha256=state['source_sha256'],stage13_epoch_path=state['epoch_path'],
        stage13_epoch_sha256=state['epoch_sha256'],accepted_trials=state['accepted'],
        total_trials=state['trials'],no_weak_directions_removed=True,
        numerical_implementation_version=3,parent_campaign=state.get('parent_campaign'),
        cumulative_accepted_trials=state.get('cumulative_parent_accepted',0)+state['accepted'],
        cumulative_total_trials=state.get('cumulative_parent_trials',0)+state['trials'])
    return case


def snapshot(directory,state,seed,p,extra,r,tag):
    folder=directory/'snapshots';folder.mkdir(parents=True,exist_ok=True)
    candidate_path=folder/(tag+'.json');array_path=folder/(tag+'.npz')
    # A supervisor kill may occur after a complete snapshot but before its
    # authoritative event commit. Preserve that orphan and allocate a distinct
    # retry name; never overwrite it or prevent a valid incumbent from resuming.
    if candidate_path.exists() or array_path.exists():
        tag=tag+'_uncommitted_retry_'+str(time.time_ns())
        candidate_path=folder/(tag+'.json');array_path=folder/(tag+'.npz')
        if candidate_path.exists() or array_path.exists():raise ValueError('Immutable retry snapshot collision')
    npz(array_path,p=p,extra=extra,residual=r)
    case=export_candidate(seed,p,extra,state,tag)
    case['snapshot_arrays_path']=str(array_path);case['snapshot_arrays_sha256']=digest(array_path)
    atomic(candidate_path,case)
    return str(candidate_path),str(array_path)


def proposal_snapshot(directory,state,seed,p,extra,r,step,scales,report):
    """Persist the complete trial before validation; never edit this record."""
    folder=directory/'trial_proposals';folder.mkdir(parents=True,exist_ok=True)
    tag='trial_'+str(state['trials']).zfill(8)+'_'+str(time.time_ns())
    arrays=folder/(tag+'.npz');candidate_path=folder/(tag+'.candidate.json');record_path=folder/(tag+'.json')
    npz(arrays,p=p,extra=extra,residual=r,scaled_coordinate_step=step,
        physical_chart_coordinate_step=step*scales,column_scales=scales)
    unvalidated=json.loads(json.dumps(state));unvalidated.update(objective=float(r@r/2),
        validation={'J_abs':None,'error_abs':None})
    candidate=export_candidate(seed,p,extra,unvalidated,tag)
    candidate.update(candidate_role='unvalidated_trial_proposal_not_an_accepted_incumbent',
        trial_proposal_arrays_path=str(arrays),trial_proposal_arrays_sha256=digest(arrays),
        validation_status='pending independent whole-axis checks')
    atomic(candidate_path,candidate)
    record={'schema':'stage13_complete_unvalidated_trial_proposal_v3','trial':state['trials'],
        'status':'unvalidated','accepted_incumbent':False,'base_candidate_path':state['candidate_path'],
        'base_candidate_sha256':state['candidate_sha256'],'base_arrays_path':state['arrays_path'],
        'base_arrays_sha256':state['arrays_sha256'],'p_sha256':array_hash(p),'extra_sha256':array_hash(extra),
        'residual_sha256':array_hash(r),'mesh_J_abs':float(r@r/2),'five_Taylor':report,
        'arrays_path':str(arrays),'arrays_sha256':digest(arrays),
        'candidate_path':str(candidate_path),'candidate_sha256':digest(candidate_path),
        'source_sha256':state['source_sha256'],'epoch_path':state['epoch_path'],
        'epoch_sha256':state['epoch_sha256'],'coordinate_map_sha256':state['coordinate_map_sha256'],
        'created_epoch':time.time(),'outcome_is_separate_immutable_record':True}
    atomic(record_path,record)
    return {'record_path':str(record_path),'record_sha256':digest(record_path),
        'candidate_path':str(candidate_path),'candidate_sha256':digest(candidate_path),
        'arrays_path':str(arrays),'arrays_sha256':digest(arrays)}


def commit(directory,state,row):
    state['events']=state.get('events',0)+1
    row['event_sequence']=state['events']
    path=directory/'commits'/('event_'+str(state['events']).zfill(8)+'.json')
    if path.exists():raise ValueError('Immutable trial commit collision')
    atomic(path,{'trial':row,'post_state':state})
    atomic(directory/'state.json',state)
    append(directory/'trajectory.jsonl',row)


def make_model(seed,integrator,directory,args):
    from stage13_model_v3 import CachedAbsoluteProblem
    return TrackedModel(CachedAbsoluteProblem(seed,integrator.mesh,a_ref=A_REF,
        block_size=args.block_size,workers=args.workers),directory)


def map_and_model(model,p,extra,column_scales=None):
    chart=AbsoluteC5ChartV2(p);full=model.jacobian(p,extra)
    reduced=np.column_stack((full[:,:24]@chart.base_tangent,full[:,24:]))
    norms=np.linalg.norm(reduced,axis=0)
    if len(norms)!=19+len(extra) or not np.all(np.isfinite(norms)) or np.any(norms<=0):
        raise ValueError('An exact zero/nonfinite column requires diagnosis; no direction is discarded')
    scales=1/norms if column_scales is None else np.asarray(column_scales,dtype=float)
    if scales.shape!=norms.shape or np.any(scales<=0) or not np.all(np.isfinite(scales)):
        raise ValueError('Complete positive coordinate scales required')
    return chart,reduced*scales,scales


def feasible_trial(chart,p,extra,step,scales):
    physical=step*scales
    pp=chart.lift_delta(physical[:19]);ee=extra+physical[19:]
    report=hp_report(pp)
    if report['max_abs']>=1e-10 or not report['physical_bounds'] or abs(report['a0'])<=1e-12:
        raise ValueError('Proposed feasible trial fails unchanged physical C5/bounds')
    return pp,ee,report


def actual_matrix_kkt(A,r,step,subproblem):
    """Check the rotated SVD step with the original full Jacobian matrix."""
    mu=subproblem.get('lagrange_multiplier')
    if mu is None or not np.isfinite(mu):
        raise ValueError('Trust multiplier is not representable for independent KKT checking')
    response=A@step;gradient=A.T@r;response_gradient=A.T@response
    scale=max(np.linalg.norm(gradient),np.linalg.norm(response_gradient),
        mu*np.linalg.norm(step),1e-300)
    return float(np.linalg.norm(gradient+response_gradient+mu*step)/scale)


def verify_epoch_sources(integrator,args,seed):
    # The integrator owns the detailed representative-neighborhood, mesh,
    # endpoint, source and derivative preflight gate, and refuses stale proof.
    integrator.require_qualified(seed,workers=args.workers)
    mathematical_tests=read(OUT/'stage13_solver_tests.json')
    if not mathematical_tests.get('passed'):
        raise ValueError('The all-column trust solver mathematical tests have not passed')
    for name,sha in mathematical_tests['source_sha256'].items():
        if digest(ROOT/name)!=sha:
            raise ValueError('Trust solver arithmetic or its qualification tests changed: '+name)


def initialize(args,directory):
    from stage13_integration_v3 import EpochIntegrator
    parent=parent_continuation(args)
    seed=read(args.start);p=np.asarray(seed.get('core_parameters',[seed['cl']]+seed['coefficients'][1:]));extra=np.asarray(seed.get('extra_coefficients',[]))
    if len(extra)!=args.expected_extra or len(seed.get('modes',[]))!=len(extra):
        raise ValueError('The complete requested spectral space is required')
    integrator=EpochIntegrator(seed,args.epoch)
    verify_epoch_sources(integrator,args,seed)
    model=make_model(seed,integrator,directory,args);r=model.fun(p,extra)
    chart,A,scales=map_and_model(model,p,extra)
    npz(directory/'coordinate_map.npz',column_scales=scales,initial_core_tangent=chart.base_tangent)
    validation=integrator.validate(p,extra,coarse_r=r,predicted_reduction=None,reference=None)
    if not validation['accuracy_passed']:raise ValueError('Initial whole-axis validation failed')
    old=parent['parent_validation']
    delta=abs(validation['J_abs']-old['J_abs'])
    tolerance=validation['error_abs']+old['error_abs']+128*np.finfo(float).eps*max(validation['J_abs'],old['J_abs'],1e-300)
    if delta>tolerance:raise ValueError('The unchanged physical parent has incompatible old/new whole-axis values')
    atomic(directory/'parent_continuation.json',parent)
    state={'schema':'stage13_all_column_absolute_campaign_v3','label':args.label,
        'p':p.tolist(),'extra':extra.tolist(),'modes':seed['modes'],
        'parent_candidate_path':str(args.start.resolve()),'parent_candidate_sha256':digest(args.start),
        'source_sha256':numerical_sources(),'epoch_path':str(args.epoch.resolve()),'epoch_sha256':digest(args.epoch),
        'epoch_anchor_candidate':json.loads(json.dumps(seed)),
        'coordinate_map_path':str(directory/'coordinate_map.npz'),
        'coordinate_map_sha256':digest(directory/'coordinate_map.npz'),
        'expected_extra':args.expected_extra,'feasible_variables':19+len(extra),'workers':args.workers,
        'objective':float(r@r/2),'initial_objective':float(r@r/2),'validation':validation,
        'radius':float(args.initial_radius or .5*np.linalg.norm(r)),
        'accepted':0,'rejected':0,'trials':0,'events':0,'mesh_epochs':1,'slices':0,'consecutive_rejections':0,
        'elapsed_worker_seconds':0.,'started_epoch':time.time(),'last_epoch':time.time(),
        'status':'running','a_ref':A_REF,'resource_runs':[],
        'column_scale_policy':'All 19+K positive inverse initial column norms, fixed within the immutable mesh epoch; v2 chart reanchored after accepted physical steps.',
        'stationarity_independently_verified':False}
    state.update(numerical_implementation_version=3,parent_campaign=parent,
        parent_continuation_path=str(directory/'parent_continuation.json'),
        parent_continuation_sha256=digest(directory/'parent_continuation.json'),
        cumulative_parent_accepted=parent['cumulative_parent_accepted'],
        cumulative_parent_trials=parent['cumulative_parent_trials'],
        cumulative_parent_worker_seconds=parent['parent_elapsed_worker_seconds'],
        cumulative_accepted=parent['cumulative_parent_accepted'],cumulative_trials=parent['cumulative_parent_trials'])
    candidate_path,arrays_path=snapshot(directory,state,seed,p,extra,r,'initial')
    state.update(candidate_path=candidate_path,arrays_path=arrays_path,
        candidate_sha256=digest(candidate_path),arrays_sha256=digest(arrays_path))
    atomic(directory/'state.json',state)
    commit(directory,state,{'kind':'explicit_numerical_version_continuation','accepted':False,
        'old_campaign_path':parent['campaign_path'],'old_state_sha256':parent['state_sha256'],
        'parent_continuation_path':state['parent_continuation_path'],
        'parent_continuation_sha256':state['parent_continuation_sha256'],
        'old_accepted_preserved':parent['parent_accepted'],'new_local_accepted':0,
        'cumulative_accepted':state['cumulative_accepted'],'old_new_independent_loss_difference':delta,
        'combined_integration_error_tolerance':tolerance,
        'physical_core_extra_modes_unchanged':True,'optimization_or_candidate_refit_at_transition':False,
        'original_campaign_or_source_modified':False})
    return seed,state,integrator,model,r,scales,(chart,A)


def recover(args,directory):
    from stage13_integration_v3 import EpochIntegrator
    state=read(directory/'state.json');commits=sorted((directory/'commits').glob('event_*.json'))
    if state.get('numerical_implementation_version')!=3:
        raise ValueError('Version 3 resumes only its own independently initialized campaign')
    if str(args.parent_campaign.resolve())!=state['parent_campaign']['campaign_path']:
        raise ValueError('The version parent campaign changed')
    if digest(state['parent_continuation_path'])!=state['parent_continuation_sha256']:
        raise ValueError('The immutable parent continuation record changed')
    verify_parent_continuation(state['parent_campaign'])
    if commits:
        committed=read(commits[-1])['post_state']
        if committed['events']>state['events']:
            state=committed;atomic(directory/'state.json',state)
        elif committed['events']<state['events']:raise ValueError('State contains an uncommitted later event')
        else:
            for key in ['p','extra','objective','accepted','rejected','radius','epoch_sha256','epoch_anchor_candidate','coordinate_map_sha256','candidate_path','arrays_path','candidate_sha256','arrays_sha256']:
                if state[key]!=committed[key]:raise ValueError('State differs from authoritative complete commit: '+key)
    if state['source_sha256']!=numerical_sources():raise ValueError('Numerical sources changed; use a separately reviewed version')
    changed_epoch=state['epoch_sha256']!=digest(args.epoch) or str(args.epoch.resolve())!=state['epoch_path']
    if changed_epoch and not args.requalify_epoch:
        raise ValueError('Mesh epoch changed; explicit new epoch requalification is required')
    if state['parent_candidate_sha256']!=digest(args.start) or state['coordinate_map_sha256']!=digest(state['coordinate_map_path']):
        raise ValueError('Parent candidate or complete coordinate map changed')
    if state['candidate_sha256']!=digest(state['candidate_path']) or state['arrays_sha256']!=digest(state['arrays_path']):
        raise ValueError('Immutable accepted candidate or residual snapshot changed')
    if args.workers!=state['workers'] or args.expected_extra!=state['expected_extra']:raise ValueError('Worker count or approximation dimension changed')
    seed=read(args.start)
    if changed_epoch:
        return transition_epoch(args,directory,seed,state)
    integrator=EpochIntegrator(seed,args.epoch)
    verify_epoch_sources(integrator,args,state['epoch_anchor_candidate'])
    model=make_model(seed,integrator,directory,args)
    p,extra=np.asarray(state['p']),np.asarray(state['extra']);r=model.fun(p,extra)
    with np.load(state['arrays_path'],allow_pickle=False) as data:
        if not np.array_equal(data['p'],p) or not np.array_equal(data['extra'],extra):raise ValueError('Physical checkpoint arrays changed')
        difference=np.linalg.norm(r-data['residual'])
        tolerance=64*np.finfo(float).eps*max(np.linalg.norm(r),np.linalg.norm(data['residual']),1e-300)
        if difference>tolerance:raise ValueError('Exact endpoint residual did not reproduce within 64-epsilon relative tolerance')
    with np.load(state['coordinate_map_path'],allow_pickle=False) as data:scales=data['column_scales'].copy()
    append(directory/'continuations.jsonl',{'epoch':time.time(),'trials':state['trials'],
        'residual_difference_norm':float(difference),'tolerance':float(tolerance),
        'bitwise_residual_restored':bool(difference==0),'environment':provenance()})
    return seed,state,integrator,model,r,scales,None


def transition_epoch(args,directory,seed,state):
    """Requalify a finer immutable rule at the identical physical endpoint."""
    from stage13_integration_v3 import EpochIntegrator
    old=json.loads(json.dumps(state));p=np.asarray(state['p']);extra=np.asarray(state['extra'])
    current=export_candidate(seed,p,extra,state,'mesh_requalification_endpoint')
    integrator=EpochIntegrator(current,args.epoch);verify_epoch_sources(integrator,args,current)
    model=make_model(seed,integrator,directory,args);r=model.fun(p,extra)
    chart,A,scales=map_and_model(model,p,extra)
    validation=integrator.validate(p,extra,coarse_r=r,predicted_reduction=None,reference=None)
    if not validation['accuracy_passed']:raise ValueError('New mesh epoch failed independent accuracy checks')
    discrepancy=abs(validation['J_abs']-old['validation']['J_abs'])
    tolerance=validation['error_abs']+old['validation']['error_abs']+128*np.finfo(float).eps*max(validation['J_abs'],old['validation']['J_abs'],1e-300)
    if discrepancy>tolerance:raise ValueError('Unchanged endpoint independent whole-axis values disagree across mesh epochs')
    number=state.get('mesh_epochs',1)+1
    map_path=directory/('coordinate_map_epoch_'+str(number).zfill(4)+'.npz')
    if map_path.exists():raise ValueError('Immutable new mesh coordinate map collision')
    npz(map_path,column_scales=scales,initial_core_tangent=chart.base_tangent)
    state.update(epoch_path=str(args.epoch.resolve()),epoch_sha256=digest(args.epoch),
        epoch_anchor_candidate=current,
        coordinate_map_path=str(map_path),coordinate_map_sha256=digest(map_path),
        objective=float(r@r/2),validation=validation,mesh_epochs=number,
        radius=float(args.initial_radius or .5*np.linalg.norm(r)),
        consecutive_rejections=0,status='running')
    tag='mesh_epoch_'+str(number).zfill(4)+'_unchanged_endpoint'
    candidate_path,arrays_path=snapshot(directory,state,seed,p,extra,r,tag)
    state.update(candidate_path=candidate_path,arrays_path=arrays_path,
        candidate_sha256=digest(candidate_path),arrays_sha256=digest(arrays_path))
    row={'kind':'mesh_epoch_transition','trial':state['trials'],'accepted':False,
        'physical_endpoint_changed':False,'old_epoch_path':old['epoch_path'],'old_epoch_sha256':old['epoch_sha256'],
        'new_epoch_path':state['epoch_path'],'new_epoch_sha256':state['epoch_sha256'],
        'old_training_objective':old['objective'],'new_training_objective':state['objective'],
        'independent_value_difference':discrepancy,'combined_diagnostic_tolerance':tolerance,
        'accepted_count_unchanged':state['accepted']==old['accepted'],'old_state':old}
    commit(directory,state,row)
    return seed,state,integrator,model,r,scales,(chart,A)


def benchmark(directory,model,chart,A,r,p,extra,scales,radius,integrator):
    if (directory/'solver_benchmark.json').exists():return
    factors=DenseTrustModel(A,r);report,arrays=factors.compare_lsmr(radius)
    report['SVD']['actual_matrix_KKT_relative']=actual_matrix_kkt(A,r,arrays['svd_step'],report['SVD'])
    nonlinear={}
    for name in ('svd_step','lsmr_step'):
        step=arrays[name]
        try:
            pp,ee,hp=feasible_trial(chart,p,extra,step,scales)
            rr=model.fun(pp,ee);validation=integrator.validate(pp,ee,coarse_r=rr,predicted_reduction=None,reference=None)
            nonlinear[name]={'feasible':True,'mesh_J_abs':float(rr@rr/2),'independent':validation,
                'five_Taylor_max':hp['max_abs'],'physical_p':pp.tolist(),'extra_sha256':array_hash(ee),
                'promoted_as_candidate':False}
            arrays[name+'_nonlinear_residual']=rr
        except (ValueError,np.linalg.LinAlgError) as exc:
            nonlinear[name]={'feasible':False,'failure':str(exc),'promoted_as_candidate':False}
    report.update(nonlinear_trial_evaluations=nonlinear,nonlinear_trial_evaluations_pending=False,
        initial_objective=float(r@r/2),coordinate_map_sha256=digest(directory/'coordinate_map.npz'),
        environment=provenance())
    path=directory/'solver_benchmark.npz';npz(path,residual=r,matrix=A,column_scales=scales,core_tangent=chart.base_tangent,**arrays)
    report.update(arrays_path=str(path),arrays_sha256=digest(path))
    atomic(directory/'solver_benchmark.json',report)


def run(args):
    began=time.monotonic();deadline=began+args.seconds
    directory=ROOT/'campaign'/args.label
    if directory.exists():
        if not args.resume:raise ValueError('Existing campaign requires explicit --resume')
        seed,state,integrator,model,r,scales,prepared=recover(args,directory)
    else:
        if args.resume:raise ValueError('Cannot resume a nonexistent campaign')
        directory.mkdir(parents=True)
        seed,state,integrator,model,r,scales,prepared=initialize(args,directory)
    p,extra=np.asarray(state['p']),np.asarray(state['extra'])
    state['status']='running';state['slices']+=1
    state['resource_runs'].append(provenance())
    atomic(directory/'state.json',state)
    pending=None
    while not STOP and time.monotonic()<deadline:
        if pending is None:
            chart,A,_=map_and_model(model,p,extra,scales) if prepared is None else (*prepared,scales)
            prepared=None
            factors=DenseTrustModel(A,r);stationarity=factors.stationarity()
            atomic(directory/'latest_model.json',{'accepted':state['accepted'],'trials':state['trials'],
                'objective':state['objective'],'stationarity':stationarity,'chart':chart.geometry_diagnostics,
                'coordinate_map_sha256':state['coordinate_map_sha256'],'epoch_sha256':state['epoch_sha256']})
            if not (directory/'solver_benchmark.json').exists():
                benchmark(directory,model,chart,A,r,p,extra,scales,state['radius'],integrator)
            pending=(chart,A,factors,stationarity)
        chart,A,factors,stationarity=pending
        step,subproblem=factors.step(state['radius'])
        subproblem['actual_matrix_KKT_relative']=actual_matrix_kkt(A,r,step,subproblem)
        if subproblem['actual_matrix_KKT_relative']>1e-8:
            state['status']='full_matrix_trust_subproblem_inaccuracy_requires_diagnosis'
            atomic(directory/'subproblem_failure.json',{'accepted':state['accepted'],
                'trial':state['trials'],'subproblem':subproblem,'incumbent_preserved':True})
            break
        prediction=subproblem['actual_matrix_predicted_decrease']
        if not np.isfinite(prediction) or prediction<=128*np.finfo(float).eps*max(state['objective'],1e-300):
            state['status']='model_reduction_at_precision_floor';break
        state['trials']+=1
        state['cumulative_trials']=state['cumulative_parent_trials']+state['trials']
        row={'trial':state['trials'],'accepted_before':state['accepted'],'epoch':time.time(),
            'objective_before':state['objective'],'radius_before':state['radius'],
            'predicted_decrease':prediction,'subproblem':subproblem,'stationarity':stationarity,
            'mesh_epoch_sha256':state['epoch_sha256'],'coordinate_map_sha256':state['coordinate_map_sha256'],
            'accepted':False,'source_sha256':state['source_sha256']}
        try:
            pp,ee,hp=feasible_trial(chart,p,extra,step,scales)
            rr=model.fun(pp,ee);trial_objective=float(rr@rr/2)
            proposal=proposal_snapshot(directory,state,seed,pp,ee,rr,step,scales,hp)
            row['complete_trial_proposal']=proposal
            validation=integrator.validate(pp,ee,coarse_r=rr,predicted_reduction=prediction,reference=state['validation'])
            decrease=state['objective']-trial_objective;ratio=decrease/prediction
            independent_decrease=state['validation']['J_abs']-validation['J_abs']
            uncertainty=state['validation']['error_abs']+validation['error_abs']
            accuracy=bool(validation['accuracy_passed'] and not validation.get('requires_refinement',False)
                and uncertainty<=.05*prediction and independent_decrease>uncertainty)
            accepted=bool(decrease>128*np.finfo(float).eps*max(state['objective'],1e-300) and ratio>.1 and accuracy)
            row.update(objective_trial=trial_objective,actual_mesh_decrease=decrease,gain_ratio=ratio,
                independent_decrease=independent_decrease,integration_uncertainty=uncertainty,
                trial_validation=validation,five_Taylor_max=hp['max_abs'],
                trial_p=pp.tolist(),trial_extra_sha256=array_hash(ee),accepted=accepted)
            if not validation['accuracy_passed'] or validation.get('requires_refinement',False) or uncertainty>.05*prediction:
                row['stop_reason']='integration_uncertainty_requires_new_mesh_epoch'
                state['status']='needs_mesh_refinement'
            if ratio<.25:state['radius']*=.25
            elif ratio>.75 and np.linalg.norm(step)>.8*state['radius']:state['radius']*=2
            if accepted:
                # Serialize a prospective state before promoting any in-memory
                # incumbent. A failed snapshot leaves the previous physical
                # endpoint and its independently verified residual untouched.
                prospective=json.loads(json.dumps(state))
                prospective.update(p=pp.tolist(),extra=ee.tolist(),objective=trial_objective,validation=validation,
                    accepted=state['accepted']+1,consecutive_rejections=0,
                    cumulative_accepted=state['cumulative_parent_accepted']+state['accepted']+1)
                tag='accepted_'+str(prospective['accepted']).zfill(8)
                candidate_path,arrays_path=snapshot(directory,prospective,seed,pp,ee,rr,tag)
                prospective.update(candidate_path=candidate_path,arrays_path=arrays_path,
                    candidate_sha256=digest(candidate_path),arrays_sha256=digest(arrays_path))
                p,extra,r=pp,ee,rr
                state.update(prospective)
                pending=None
            else:
                state['rejected']+=1;state['consecutive_rejections']+=1
        except (ValueError,np.linalg.LinAlgError) as exc:
            row.update(failure=str(exc),accepted=False)
            state['radius']*=.25;state['rejected']+=1;state['consecutive_rejections']+=1
        if row.get('complete_trial_proposal'):
            outcome_path=Path(row['complete_trial_proposal']['record_path']).with_suffix('.outcome.json')
            if outcome_path.exists():raise ValueError('Immutable trial outcome collision')
            outcome={'schema':'stage13_trial_proposal_outcome_v3','trial':state['trials'],
                'proposal':row['complete_trial_proposal'],'accepted':row['accepted'],
                'status':'accepted' if row['accepted'] else ('validation_failed' if row.get('failure') else 'rejected'),
                'failure':row.get('failure'),'stop_reason':row.get('stop_reason'),
                'validation':row.get('trial_validation'),'incumbent_candidate_sha256':state['candidate_sha256'],
                'created_epoch':time.time()}
            atomic(outcome_path,outcome)
            row['complete_trial_outcome']={'path':str(outcome_path),'sha256':digest(outcome_path)}
        else:
            row['proposal_unavailable_reason']='Feasible lift or residual evaluation failed before a complete valid trial residual existed.'
        row.update(radius_after=state['radius'],accepted_after=state['accepted'])
        state['last_epoch']=time.time();state['last_stationarity']=stationarity
        commit(directory,state,row)
        print(json.dumps({'trial':state['trials'],'accepted':state['accepted'],'J_abs_mesh':state['objective'],
            'J_abs_independent':state['validation']['J_abs'],'radius':state['radius'],'status':state['status']}),flush=True)
        if state['status']=='needs_mesh_refinement':break
        if state['consecutive_rejections']>=12:
            state['status']='trust_obstruction_requires_diagnosis';break
        if stationarity['full_range_projected_residual_relative']<=1e-5 and row['accepted']:
            state['status']='needs_independent_stationarity_verification';break
    if state['status']=='running':state['status']='checkpointed_slice'
    state['elapsed_worker_seconds']+=time.monotonic()-began
    state['last_epoch']=time.time();state['last_slice_calls']={'fun':model.fun_calls,'jacobian':model.jac_calls}
    counters={'fun':0,'jacobian':0,'started_not_completed':[]};started={}
    for line in model.path.read_text().splitlines():
        value=json.loads(line)
        if value['event']=='started':started[value['id']]=value['kind']
        elif value['event']=='completed':
            counters[value['kind']]+=1;started.pop(value['id'],None)
    counters['started_not_completed']=[{'id':key,'kind':value} for key,value in started.items()]
    state['cumulative_journal_call_counts']=counters
    atomic(directory/'state.json',state)
    append(directory/'slices.jsonl',{'epoch':time.time(),'status':state['status'],'seconds':time.monotonic()-began,
        'accepted':state['accepted'],'trials':state['trials'],'objective':state['objective'],
        'environment':provenance()})
    print(json.dumps({'campaign':str(directory),'status':state['status'],'accepted':state['accepted'],
        'trials':state['trials'],'J_abs':state['validation']['J_abs'],'elapsed_worker_seconds':state['elapsed_worker_seconds']}),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label',required=True);parser.add_argument('--start',type=Path,required=True)
    parser.add_argument('--epoch',type=Path,required=True);parser.add_argument('--resume',action='store_true')
    parser.add_argument('--requalify-epoch',action='store_true',help='On resume only: accept a separately qualified immutable new mesh at the same physical endpoint')
    parser.add_argument('--seconds',type=float,default=3300.);parser.add_argument('--workers',type=int,default=8)
    parser.add_argument('--block-size',type=int,default=1024);parser.add_argument('--expected-extra',type=int,default=162)
    parser.add_argument('--initial-radius',type=float)
    parser.add_argument('--parent-campaign',type=Path,required=True,
        help='Stopped immutable predecessor; version 3 always uses a distinct new campaign label')
    args=parser.parse_args()
    if '/' in args.label or '\\' in args.label:parser.error('Simple campaign label required')
    if not (0<args.seconds<=3300) or args.workers<1:parser.error('A guarded slice must fit within 3300 seconds')
    if args.initial_radius is not None and args.initial_radius<=0:parser.error('Positive initial radius required')
    if args.requalify_epoch and not args.resume:parser.error('--requalify-epoch requires --resume')
    signal.signal(signal.SIGTERM,request_stop);signal.signal(signal.SIGINT,request_stop)
    os.environ['IPM_WORK_DIR']=str(ROOT)
    run(args)


if __name__=='__main__':main()
