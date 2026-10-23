#!/usr/bin/env python3
"""Construct a schema-specific, standard-library-only unchanged-restart file list.

This packaging helper reads files; it never imports numerical code or calls a
campaign. Required references follow the exact V3 recover/gate implementation,
not every path-looking string in historical JSON records.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def make_plan(root):
    root = root.resolve()
    rows = {}
    def add(path, role, expected=None):
        path = Path(path)
        if not path.is_absolute():
            path = root / path
        relative = str(path.relative_to(root))
        actual = sha(path)
        if expected is not None and actual != expected:
            raise ValueError('Required binding changed: ' + relative)
        if relative not in rows:
            rows[relative] = {'source_relative': relative, 'repository_relative': 'research/' + relative,
                              'sha256': actual, 'bytes': path.stat().st_size, 'roles': []}
        if role not in rows[relative]['roles']:
            rows[relative]['roles'].append(role)
        return json.loads(path.read_text()) if path.suffix == '.json' else None
    state = add('campaign/global181_v3/state.json', 'complete accepted mutable restart state')
    for key in ('candidate', 'arrays', 'epoch', 'coordinate_map', 'parent_candidate', 'parent_continuation'):
        add(state[key + '_path'], 'recover: active ' + key, state[key + '_sha256'])
    for name, expected in state['source_sha256'].items():
        add(name, 'recover: numerical_sources immutable source', expected)
    add('workspace.json', 'numerical_sources: original source-name map')
    manifest = add('provenance/base_manifest.json', 'parent/integration immutable independent source manifest')
    for name, expected in manifest.items():
        if name.endswith('.py'):
            add('base/' + name, 'independent_sources: hash-checked base Python source', expected)
    add('inputs/candidates.json', 'fixed positive a_ref and parent input-manifest binding')
    freeze = add('provenance/stage13_numerical_sources_v2.json',
                 'private_field_namespaces: immutable source snapshot manifest loaded during production model construction')
    if freeze['base_manifest_sha256'] != sha(root / 'provenance/base_manifest.json'):
        raise ValueError('Private namespace base manifest binding changed')
    for name in ('absolute_fields.py', 'stage13_model.py', 'stage13_model_v2.py',
                 'absolute_fields_v2.py', 'highprecision_origin.py'):
        add(name, 'private_field_namespaces: dynamically executed/hash-bound production source', freeze['files'][name])
    for name in ('guard.py', 'policy.py', 'telemetry.py', 'worker_bootstrap.py'):
        add('hardware/' + name, 'native portable supervisor/worker bootstrap required for guarded validation and resume')
    parent = state['parent_campaign']
    add(parent['state_path'], 'verify_parent_continuation: immutable stopped parent state', parent['state_sha256'])
    for key in ('candidate', 'arrays', 'epoch', 'coordinate_map'):
        add(parent[key + '_path'], 'verify_parent_continuation: parent ' + key, parent[key + '_sha256'])
    for item in parent['commits']:
        add(item['path'], 'verify_parent_continuation: explicitly hash-bound parent commit', item['sha256'])
    for name, expected in parent['source_sha256'].items():
        add(name, 'verify_parent_continuation: hash-bound parent source', expected)
    commits = sorted((root / 'campaign/global181_v3/commits').glob('event_*.json'))
    last = commits[-1]
    authoritative = add(last, 'recover: final authoritative V3 post_state only')
    for key in ('p', 'extra', 'objective', 'accepted', 'rejected', 'radius', 'epoch_sha256',
                'epoch_anchor_candidate', 'coordinate_map_sha256', 'candidate_path', 'arrays_path',
                'candidate_sha256', 'arrays_sha256'):
        if authoritative['post_state'][key] != state[key]:
            raise ValueError('Final commit differs from state: ' + key)
    epoch = json.loads(Path(state['epoch_path']).read_text())
    for name in ('training', 'refined'):
        ref = epoch['meshes'][name]
        add(ref['path'], 'EpochIntegrator: loaded ' + name + ' mesh', ref['sha256'])
    for key in ('recovery', 'original_reference_epoch', 'failed_v2_release', 'derivative_record',
                'supplemental_replay_review'):
        ref = epoch[key]
        add(ref['path'], 'require_qualified: hash-bound ' + key, ref['sha256'])
    review = json.loads(Path(epoch['supplemental_replay_review']['path']).read_text())
    for ref in [review['policy'], review['original_pending_epoch']] + review['diagnostics']:
        add(ref['path'], 'require_qualified: hash-bound supplemental review evidence', ref['sha256'])
    for proof in review['fresh_native_process_guard_proofs']:
        for key in ('result', 'epoch_design'):
            ref = proof[key]
            add(ref['path'], 'require_qualified: hash-bound fresh-process ' + key, ref['sha256'])
    tests = add('results/stage13_solver_tests.json', 'verify_epoch_sources: solver mathematical tests')
    for name, expected in tests['source_sha256'].items():
        add(name, 'verify_epoch_sources: solver test source hash', expected)
    add('campaign/global181_v3/numerical_calls.jsonl', 'preserve cumulative numerical call accounting across restart')
    add('campaign/global181_v3/solver_benchmark.json', 'existing benchmark sentinel prevents a redundant optimization-adjacent benchmark on restart')
    omitted = []
    for relative, reason in [
        ('campaign/global181_v3/solver_benchmark.npz', '128 MB initial benchmark matrix; not loaded by recover/run; benchmark JSON is only an existence sentinel'),
    ]:
        path = root / relative
        omitted.append({'source_relative': relative, 'bytes': path.stat().st_size, 'sha256': sha(path), 'reason': reason})
    return {'schema': 'ipm_stage13_minimal_unchanged_restart_closure_v1',
            'checkpoint': 'accepted_00000278.json', 'feasible_dimension': 181,
            'accepted': state['accepted'], 'rejected': state['rejected'], 'trials': state['trials'],
            'events': state['events'], 'trust_radius': state['radius'],
            'last_authoritative_commit': str(last.relative_to(root)),
            'last_authoritative_commit_sha256': sha(last),
            'included_v3_commit_count': 1, 'original_v3_commit_count': len(commits),
            'all_parent_commits_preserved': True,
            'source_bytes_modified': False, 'optimization_started': False,
            'new_host_qualification_performed': False,
            'total_files': len(rows), 'total_bytes': sum(x['bytes'] for x in rows.values()),
            'files': [rows[key] for key in sorted(rows)],
            'omitted_not_required': omitted,
            'recovery_semantics': 'The unchanged V3 recover reads only the greatest V3 commit file and compares its post_state with state.json; it does not traverse earlier V3 commits. The accepted/trial/event counters remain unchanged. All seven explicitly hash-bound predecessor commits are retained. Paths nested in retained provenance JSON are not dependencies unless the actual recover/gate code dereferences them.',
            'limitations': ['Closure by unchanged recover/EpochIntegrator/require_qualified implementation, not all optional validation entrypoints.',
                            'New Linux BLAS/native environment must qualify and strict residual replay must pass before --resume.',
                            'Checkpoint restart and successful optimization are separate; no optimization has been launched.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Output exists; use a fresh path')
    result = make_plan(args.source_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'files': result['total_files'], 'bytes': result['total_bytes'], 'output': str(args.output)}))


if __name__ == '__main__':
    main()
