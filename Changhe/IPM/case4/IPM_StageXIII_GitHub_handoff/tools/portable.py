#!/usr/bin/env python3
"""Read-only current-checkpoint checks. No optimization or finite differences."""
import argparse
import json
import os
from pathlib import Path
import platform
import sys
import time
from runtime import Runtime, digest

CANDIDATE = 'campaign/global181_v3/snapshots/accepted_00000278.json'
EXPECTED = '812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955'


def inspect(rt):
    p = rt.research/CANDIDATE
    if digest(p) != EXPECTED:
        raise ValueError('Current accepted checkpoint hash differs')
    c = rt.read(p)
    if len(c['core_parameters']) != 24 or len(c['extra_coefficients']) != 162 or len(c['modes']) != 162:
        raise ValueError('Current basis/coefficient dimensions differ')
    state = rt.read(rt.research/'campaign/global181_v3/state.json')
    if state['candidate_sha256'] != EXPECTED or state['p'] != c['core_parameters'] or state['extra'] != c['extra_coefficients']:
        raise ValueError('Accepted JSON and exact continuation state disagree')
    return {'candidate_sha256': EXPECTED, 'cl': c['cl'], 'a0': c['a0'],
            'feasible_variables': 181, 'accepted': state['accepted'],
            'trials': state['trials'], 'J_abs': state['validation']['J_abs'],
            'stationarity_established': False, 'numerical_execution': False}


def restart_audit(rt):
    root = rt.research
    state = rt.read(root/'campaign/global181_v3/state.json')
    bound = []
    def bind(path, sha, role):
        p = Path(rt.translate(str(path)))
        if digest(p) != sha:
            raise ValueError('Restart binding differs: '+role+' '+str(p))
        bound.append({'role': role, 'path': str(p), 'sha256': sha})
    for key in ('candidate', 'arrays', 'epoch', 'coordinate_map', 'parent_candidate', 'parent_continuation'):
        if key+'_path' in state:
            bind(state[key+'_path'], state[key+'_sha256'], key)
    for name, sha in state['source_sha256'].items():
        bind(root/name, sha, 'frozen numerical source')
    parent = state['parent_campaign']
    bind(parent['state_path'], parent['state_sha256'], 'immutable parent state')
    for key in ('candidate', 'arrays', 'epoch', 'coordinate_map'):
        bind(parent[key+'_path'], parent[key+'_sha256'], 'immutable parent '+key)
    for row in parent['commits']:
        bind(row['path'], row['sha256'], 'required parent event')
    for name, sha in parent['source_sha256'].items():
        bind(root/name, sha, 'parent source required by unchanged recovery')
    bind(root/'provenance/base_manifest.json', parent['base_manifest_sha256'], 'base manifest')
    bind(root/'inputs/candidates.json', parent['input_manifest_sha256'], 'input manifest')
    commits = sorted((root/'campaign/global181_v3/commits').glob('event_*.json'))
    if not commits:
        raise ValueError('Missing authoritative last event')
    last = rt.read(commits[-1])['post_state']
    for key in ('p', 'extra', 'objective', 'accepted', 'rejected', 'radius', 'events',
                'epoch_sha256', 'coordinate_map_sha256', 'epoch_anchor_candidate',
                'candidate_path', 'arrays_path', 'candidate_sha256', 'arrays_sha256'):
        if state[key] != last[key]:
            raise ValueError('Current state differs from authoritative last event: '+key)
    epoch = rt.read(state['epoch_path'])
    for name, row in epoch['meshes'].items():
        bind(row['path'], row['sha256'], name+' mesh')
    for name in ('recovery', 'original_reference_epoch', 'failed_v2_release',
                 'derivative_record', 'supplemental_replay_review'):
        row = epoch[name]
        bind(row['path'], row['sha256'], 'epoch '+name)
    review = rt.read(epoch['supplemental_replay_review']['path'])
    for row in [review['policy'], review['original_pending_epoch']]+review['diagnostics']:
        bind(row['path'], row['sha256'], 'released provider proof')
    for proof in review['fresh_native_process_guard_proofs']:
        for row in (proof['result'], proof['epoch_design']):
            bind(row['path'], row['sha256'], 'historical native provider proof')
    return {'passed': True, 'bindings': bound,
            'last_event': str(commits[-1]), 'events_recorded_in_state': state['events'],
            'V3_events_shipped': len(commits),
            'history_policy': 'Only authoritative last V3 commit is needed by unchanged recover(); required parent commits remain exact.',
            'actual_recover_called': False, 'new_host_qualification_passed': False,
            'resume_executed': False}


def smoke(rt, whole_axis=False):
    if not os.environ.get('IPM_RESOURCE_SESSION') or not os.environ.get('IPM_RESOURCE_RUN'):
        raise RuntimeError('Run numerical checks through research/hardware/guard.py')
    began = time.time()
    import numpy as np
    import scipy
    import psutil
    from threadpoolctl import threadpool_limits, threadpool_info
    from absolute_common import A_REF
    from absolute_fields_v2 import prepare_candidate, residual, fields
    from absolute_chart import hp_report
    from absolute_model import tensor_gauss_mesh
    from absolute_model_v2 import AbsoluteLossProblem
    c = rt.read(rt.research/CANDIDATE)
    p, extra = np.asarray(c['core_parameters']), np.asarray(c['extra_coefficients'])
    ref = rt.read(rt.repo/'verification/smoke_reference.json')
    expected = ref['candidate']
    xy = np.asarray(ref['spot_coordinates'])
    with threadpool_limits(limits=1):
        prepared = prepare_candidate(c, 'center_chart')
        rr = residual(prepared, xy[:, 0], xy[:, 1])
        ff = fields(prepared, xy[:, 0], xy[:, 1])
        hp = hp_report(p)
        if hp['max_abs'] >= 1e-10 or hp['center_abs'] >= 1e-10 or not hp['physical_bounds']:
            raise ValueError('High-precision center/five-Taylor/bounds check failed')
        mesh = tensor_gauss_mesh(-4., 8., radial_panels=3, radial_order=8,
                                 angular_order=12, name='handoff_smoke_288_nodes')
        finite = AbsoluteLossProblem(c, mesh, A_REF, block_size=128).fun()
        actual = {'spot_Rf': rr.tolist(), 'spot_Rrho': (xy[:, 1]*rr).tolist(),
                  'spot_f': ff['f'].tolist(), 'spot_psi': ff['psi'].tolist(),
                  'fresh_finite_rule_J': float(finite@finite/2)}
        comparisons = []
        for name, value in actual.items():
            a, b = np.asarray(value), np.asarray(expected[name])
            err = float(np.max(abs(a-b)))
            tol = (5e-17+1e-7*float(abs(b))) if name == 'fresh_finite_rule_J' else 1e-12+1e-9*float(np.max(abs(b)))
            if not np.all(np.isfinite(a)) or err > tol:
                raise ValueError('Relocated value mismatch: '+name)
            comparisons.append({'quantity': name, 'max_abs_difference': err, 'tolerance': tol})
        state = rt.read(rt.research/'campaign/global181_v3/state.json')
        with np.load(state['arrays_path'], allow_pickle=False) as data:
            if not np.array_equal(p, data['p']) or not np.array_equal(extra, data['extra']):
                raise ValueError('Saved NPZ vectors differ from accepted JSON')
            saved_j = float(data['residual']@data['residual']/2)
            tol = 64*np.finfo(float).eps*max(abs(saved_j), abs(state['objective']), 1e-300)
            if abs(saved_j-state['objective']) > tol:
                raise ValueError('Saved NPZ residual norm differs from state')
        integral = None
        if whole_axis:
            from stage13_integration_v2 import independent_integral
            integral = independent_integral(c, p, extra, workers=1, target_abs=1e-16)
            tol = float(expected['current_epoch_J_comparison_tolerance'])
            if not integral['accuracy_passed'] or abs(integral['J_abs']-expected['historical_J_abs_loaded']) > tol:
                raise ValueError('Fresh whole-axis independent objective failed reproduction')
    return {'passed': True, 'seconds': time.time()-began, 'candidate_sha256': EXPECTED,
            'a_ref': A_REF, 'five_Taylor': hp, 'values': actual, 'comparisons': comparisons,
            'finite_rule_is_whole_axis_J': False,
            'saved_mesh_J_reconstructed_from_arrays': saved_j,
            'fresh_full_production_residual_replay': False,
            'fresh_whole_axis_integral': integral,
            'optimization_launched': False, 'FD_or_trial_launched': False,
            'environment': {'host': platform.node(), 'python': platform.python_version(), 'machine': platform.machine(),
                'python_executable': sys.executable, 'numpy': np.__version__, 'scipy': scipy.__version__,
                'psutil': psutil.__version__, 'threadpools': threadpool_info(),
                'resource_session': os.environ.get('IPM_RESOURCE_SESSION'),
                'resource_run': os.environ.get('IPM_RESOURCE_RUN'), 'pid': os.getpid()}}


def replay(rt):
    """Actual recovery preflight and strict R replay, without recover's writes."""
    if not os.environ.get('IPM_RESOURCE_SESSION') or not os.environ.get('IPM_RESOURCE_RUN'):
        raise RuntimeError('Run replay through research/hardware/guard.py')
    began = time.time()
    from types import SimpleNamespace
    import numpy as np
    from threadpoolctl import threadpool_limits, threadpool_info
    from absolute_common import A_REF
    from stage13_campaign_v3 import numerical_sources, verify_parent_continuation, verify_epoch_sources
    from stage13_integration_v3 import EpochIntegrator
    from stage13_model_v3 import CachedAbsoluteProblem
    state = rt.read(rt.research/'campaign/global181_v3/state.json')
    if state['source_sha256'] != numerical_sources():
        raise ValueError('Actual production source closure does not match resumed state')
    verify_parent_continuation(state['parent_campaign'])
    seed = rt.read(state['parent_candidate_path'])
    integrator = EpochIntegrator(seed, state['epoch_path'])
    args = SimpleNamespace(workers=state['workers'])
    verify_epoch_sources(integrator, args, state['epoch_anchor_candidate'])
    p, extra = np.asarray(state['p']), np.asarray(state['extra'])
    with threadpool_limits(limits=state['workers'], user_api='blas'):
        model = CachedAbsoluteProblem(seed, integrator.mesh, A_REF,
                                      workers=state['workers'], block_size=1024)
        value = model.fun(p, extra)
        pools = threadpool_info()
        model.clear_cache()
        del model
        with np.load(state['arrays_path'], allow_pickle=False) as arrays:
            if not np.array_equal(p, arrays['p']) or not np.array_equal(extra, arrays['extra']):
                raise ValueError('Exact incumbent coefficient vectors differ')
            saved = arrays['residual'].copy()
        difference = float(np.linalg.norm(value-saved))
        tolerance = float(64*np.finfo(float).eps*max(np.linalg.norm(value), np.linalg.norm(saved), 1e-300))
    result = {'passed': difference <= tolerance, 'seconds': time.time()-began,
              'production_source_closure_passed': True, 'immutable_parent_gate_passed': True,
              'actual_EpochIntegrator_require_qualified_passed': True,
              'actual_verify_epoch_sources_passed': True, 'workers': state['workers'],
              'residual_difference_norm': difference, 'unchanged_64epsilon_threshold': tolerance,
              'bitwise_equal': bool(np.array_equal(value, saved)),
              'fresh_mesh_J': float(value@value/2), 'threadpools_inside_context': pools,
              'recover_called': False, 'continuation_journal_written': False,
              'optimization_or_trial_launched': False, 'Jacobian_or_FD_evaluated': False,
              'new_host_qualification_completed': False,
              'environment': {'host': platform.node(), 'machine': platform.machine(),
                              'python_executable': sys.executable, 'python': platform.python_version(),
                              'resource_session': os.environ.get('IPM_RESOURCE_SESSION'),
                              'resource_run': os.environ.get('IPM_RESOURCE_RUN'), 'pid': os.getpid()},
              'limitation': 'A replay PASS qualifies this check on this measured host only; complete new-host derivative/provider qualification remains required.'}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('inspect', 'restart-audit', 'smoke', 'objective', 'replay'))
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rt = Runtime(args.repo)
    out = args.output.expanduser().resolve()
    if out.exists() or out == rt.research or rt.research in out.parents:
        parser.error('Choose a fresh output outside immutable research/')
    rt.install()
    result = {'action': args.action, 'current': inspect(rt)}
    if args.action == 'restart-audit':
        result['restart'] = restart_audit(rt)
    elif args.action in ('smoke', 'objective'):
        result['numerics'] = smoke(rt, args.action == 'objective')
    elif args.action == 'replay':
        result['replay'] = replay(rt)
    result.update(passed=not rt.blocked and result.get('replay', {}).get('passed', True), relocation=rt.record())
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps({'passed': result['passed'], 'action': args.action, 'output': str(out)}))
    if not result['passed']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
