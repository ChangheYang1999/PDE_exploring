#!/usr/bin/env python3
"""Bind actual destination checks; this command never performs numerical work.

Run only after the documented objective, two fresh-process strict replays and
complete model/derivative benchmark have passed under a fresh supervisor.
An attestation records these measured checks; it is not an existence proof or
a rigorous uniform trust-neighborhood certificate.
"""
import argparse
import json
from pathlib import Path
import platform
import sys
import time
from runtime import Runtime, digest


def blas_signature(pools):
    keys = ('user_api', 'internal_api', 'prefix', 'version', 'threading_layer', 'architecture')
    records = [{k: row.get(k) for k in keys} for row in pools if row.get('user_api') == 'blas']
    return sorted(records, key=lambda row: json.dumps(row, sort_keys=True))


def numerical_signature():
    """No PDE work: import native libraries and identify their loaded BLAS."""
    import numpy
    import scipy
    import scipy.linalg
    import psutil
    import threadpoolctl
    return {'numpy': numpy.__version__, 'scipy': scipy.__version__,
            'psutil': psutil.__version__, 'threadpoolctl': threadpoolctl.__version__,
            'blas': blas_signature(threadpoolctl.threadpool_info())}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--objective', type=Path, required=True)
    p.add_argument('--replay', type=Path, action='append', required=True)
    p.add_argument('--benchmark', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.output.exists() or len(a.replay) < 2:
        p.error('Fresh output and at least two independently launched replay results required')
    state = json.loads((a.repo/'research/campaign/global181_v3/state.json').read_text())
    epoch = Runtime(a.repo).read(state['epoch_path'])
    expected = state['candidate_sha256']
    evidence = {}
    runs = []
    environments = []
    def read(path):
        path = Path(path).resolve()
        evidence[str(path)] = digest(path)
        return json.loads(path.read_text())
    def validate_environment(env):
        if env.get('host') != platform.node() or env.get('machine') != platform.machine():
            raise ValueError('Evidence belongs to another host/architecture')
        if env.get('python_executable', sys.executable) != sys.executable:
            raise ValueError('Evidence belongs to another interpreter')
        run = Path(env['resource_run'])
        session = Path(env['resource_session'])
        result = read(run/'result.json')
        definition = read(session/'session.json')
        baseline_path = session/'session_baseline.json'
        read(baseline_path)
        if digest(baseline_path) != definition['baseline_sha256']:
            raise ValueError('Fresh supervisor baseline differs')
        if (definition['hostname'] != platform.node() or definition['python_executable'] != sys.executable
                or result.get('success') is not True or result.get('stop_reasons')
                or result.get('returncode') != 0 or result['session_id'] != definition['session_id']
                or result['command'][0] != sys.executable):
            raise ValueError('Actual fresh supervisor proof failed')
        runs.append(str(run.resolve()))
        environments.append(env)
    obj = read(a.objective)
    if obj.get('passed') is not True or obj.get('action') != 'objective' or obj['current']['candidate_sha256'] != expected:
        raise ValueError('Current objective reproduction did not pass')
    if not obj['numerics']['fresh_whole_axis_integral']['accuracy_passed']:
        raise ValueError('Whole-axis integration accuracy failed')
    validate_environment(obj['numerics']['environment'])
    replay_runs = []
    for path in a.replay:
        row = read(path)
        if row.get('passed') is not True or row.get('action') != 'replay' or row['current']['candidate_sha256'] != expected:
            raise ValueError('Current strict replay failed')
        r = row['replay']
        if (r.get('passed') is not True or r['workers'] != state['workers']
                or not r.get('actual_EpochIntegrator_require_qualified_passed')
                or r['residual_difference_norm'] > r['unchanged_64epsilon_threshold']):
            raise ValueError('Unchanged strict replay requirement failed')
        validate_environment(r['environment'])
        replay_runs.append(r['environment']['resource_run'])
    if len(set(replay_runs)) != len(replay_runs):
        raise ValueError('Replay evidence must be independent native-process runs')
    benchmark = read(a.benchmark)
    if (not benchmark.get('completed') or not benchmark.get('passed')
            or benchmark.get('candidate_sha256') != expected
            or benchmark.get('schema') != 'stage13_actual_model_cache_benchmark_v3_origin20_private_scalar_exp'
            or benchmark.get('feasible_columns') != 181 or not benchmark.get('full_cl_derivative_included')
            or not benchmark.get('all_extra_coefficients_directly_FD_checked')
            or benchmark.get('selected_runtime_workers') != state['workers']
            or benchmark.get('mesh_sha256') != epoch['meshes']['training']['fingerprint']):
        raise ValueError('Complete current derivative/provider benchmark did not pass')
    validate_environment(benchmark['environment'])
    for name, sha in benchmark['source_sha256'].items():
        if digest(a.repo/'research'/name) != sha:
            raise ValueError('Benchmark numerical source changed: '+name)
    for key in ('reference_arrays', 'production_arrays', 'derivative_arrays'):
        path = Path(benchmark[key+'_path']).resolve()
        if digest(path) != benchmark[key+'_sha256']:
            raise ValueError('Benchmark array evidence changed: '+str(path))
        evidence[str(path)] = benchmark[key+'_sha256']
    unchanged = benchmark.get('old_independent_provider_after_private_evaluations', {})
    if not unchanged.get('passed') or not unchanged.get('same_original_stateless_source_and_functions'):
        raise ValueError('Independent provider after private-cache control failed')
    if unchanged.get('artifact_path'):
        path = Path(unchanged['artifact_path']).resolve()
        if digest(path) != unchanged['artifact_sha256']:
            raise ValueError('Independent provider array evidence changed')
        evidence[str(path)] = unchanged['artifact_sha256']
    for name, sha in state['source_sha256'].items():
        if digest(a.repo/'research'/name) != sha:
            raise ValueError('Frozen released source changed: '+name)
    # Numerical imports occur only after all evidence/identity checks above.
    signature = numerical_signature()
    for env in environments:
        for key in ('numpy', 'scipy', 'psutil', 'threadpoolctl'):
            if key in env and env[key] != signature[key]:
                raise ValueError('Numerical package changed since evidence: '+key)
        if 'threadpools' in env and blas_signature(env['threadpools']) != signature['blas']:
            raise ValueError('Loaded BLAS changed since qualification evidence')
    q = {'schema': 'stage13_actual_new_host_qualification_v1', 'created_epoch': time.time(),
         'host': platform.node(), 'machine': platform.machine(), 'python_executable': sys.executable,
         'candidate_sha256': expected, 'source_sha256': state['source_sha256'],
         'training_mesh_fingerprint': epoch['meshes']['training']['fingerprint'],
         'numerical_signature': signature,
         'fresh_native_provider_replay_passed': True, 'complete_derivative_check_passed': True,
         'independent_J_abs_reproduced': True, 'resources_rebaselined': True,
         'evidence': [{'path': k, 'sha256': v} for k, v in sorted(evidence.items())],
         'optimization_launched': False, 'stationarity_established': False,
         'scope': 'Current accepted278, unchanged production arithmetic and selected four-thread policy on this measured host.'}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with a.output.open('x') as f:
        json.dump(q, f, indent=2, allow_nan=False)
        f.write('\n')
    print(json.dumps({'qualification': str(a.output), 'evidence_files': len(evidence)}))


if __name__ == '__main__':
    main()
