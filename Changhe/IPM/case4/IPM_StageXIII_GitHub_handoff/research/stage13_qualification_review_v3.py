"""Release a V3 epoch only after fresh cached4 strict64epsilon process proof.

Old V2 independent references and failures remain source-bound provenance.
The selected production vectors are compared both pairwise and to the actual
saved V3 initial. Pure memoization is cleared before every cold instance.
"""
import argparse
import copy
from pathlib import Path
import time

from absolute_common import ROOT, np, read, atomic, digest, array_hash, provenance
from stage13_integration_v3 import (EpochIntegrator, integration_sources, independent_sources,
    physical_identity, require_original_namespace)
from stage13_qualification_v3 import recovery_evidence, policy_evidence, ref, bound
from stage13_qualification_review_v2 import compare


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_original(path, policy_path):
    original = read(path)
    require(original['schema'] == 'stage13_integration_epoch_v3' and original['completed']
        and original['local_qualification_passed'] and not original['passed']
        and original['fresh_process_cached_proof_pending'] and original['endpoint_restore']['passed'],
        'Complete locally passing V3 qualification with fresh-process proof pending required')
    require(original['original_physical_trust_design_retained']
        and not original['old_points_relabelled_as_new_normalized_design'],
        'Original physical design must not be relabeled as a new normalized design')
    require(original['source_sha256'] == integration_sources()
        and original['independent_source_sha256'] == independent_sources(), 'A numerical source changed')
    require(original['qualification_source_sha256'] == digest(ROOT / 'stage13_qualification_v3.py'),
        'The new local qualification worker changed')
    bound({'path': original['candidate_path'], 'sha256': original['candidate_sha256']})
    candidate = read(original['candidate_path'])
    require(physical_identity(candidate) == original['physical_identity'], 'Physical endpoint changed')
    old_epoch = bound(original['original_reference_epoch'])
    recovery_evidence(original['recovery']['path'], original['original_reference_epoch']['path'])
    policy = policy_evidence(policy_path, old_epoch)
    require(original['replay_policy'] == ref(policy_path)
        and policy['declared_epoch'] <= original['prepared_epoch'], 'Upfront immutable policy differs')
    require(len(original['representative_points']) == 12, 'All twelve fresh-production physical checks required')
    for row in original['representative_points']:
        point = bound(row)
        require(row['passed'] and point['passed'] and point['validation']['accuracy_passed']
            and point['validation']['source_sha256'] == integration_sources()
            and point['original_physical_trust_design_retained']
            and not point['old_points_relabelled_as_new_normalized_design'], 'A fresh production reference check failed')
        bound(point['original_recovered_point']['record']); bound(point['original_recovered_point']['original_point'])
        bound(point['validation']['original_reference'])
    require(sorted(row['factor'] for row in original['exact_dilation_checks']) == [2., 16., 256., 1024.],
        'All four exact-dilation independent references required')
    for row in original['exact_dilation_checks']:
        value = bound(row)
        require(row['passed'] and value['passed'] and value['integral']['accuracy_passed'], 'A dilation reference failed')
    for name in ('starting_point', 'initial_trust_coordinate'):
        bound({'path': original[name + '_path'], 'sha256': original[name + '_sha256']})
    endpoint_ref = original['endpoint_initial_arrays']
    require(digest(endpoint_ref['path']) == endpoint_ref['sha256'], 'Actual saved V3 initial arrays changed')
    derivative = bound(original['derivative_record'])
    require(derivative['completed'] and derivative['passed']
        and derivative['schema'] == 'stage13_actual_model_cache_benchmark_v3_origin20_private_scalar_exp',
        'Complete matching fresh V3 derivative/benchmark proof required')
    for name, identity in derivative['source_sha256'].items():
        require(digest(ROOT / name) == identity, 'Derivative source changed: ' + name)
    require(original['unchanged_checkpoint_comparison']['passed'], 'Accepted-six boundary value did not reproduce')
    old_failure = bound(original['failed_v2_release'])
    require(old_failure['completed'] and not old_failure['passed'], 'Original V2 release failure was rewritten')
    initial = read(original['starting_point_path'])
    require(initial['accuracy_passed'] and initial['error_abs'] > 0, 'Baseline whole-axis accuracy failed')
    return original, candidate, policy, initial, EpochIntegrator(candidate, path).mesh


def diagnostic_vectors(path, original, candidate, policy, mesh):
    data = read(path)
    require(data['schema'] == 'stage13_unchanged_endpoint_reproducibility_diagnostic_v3_origin20_private_scalar_exp'
        and data['completed'] and data['candidate_and_input_files_unchanged']
        and data['physical_parameter_arrays_unchanged'] and data['numerical_sources_unchanged'],
        'Complete unchanged-input V3 fresh-process diagnostic required')
    require(data['environment_at_start']['epoch'] >= policy['declared_epoch']
        and data['candidate_sha256'] == original['candidate_sha256']
        and data['training_mesh']['mesh_sha256'] == mesh.fingerprint
        and data['integration_source_sha256'] == integration_sources(), 'Process source/input/mesh identity differs')
    require(data['base_manifest_sha256'] == digest(ROOT / 'provenance/base_manifest.json'),
        'Diagnostic frozen independent base manifest differs')
    guard_path = Path(data['environment_at_start']['resource_run']) / 'result.json'
    guard = read(guard_path); command = guard['command']
    require(guard['success'] and guard['returncode'] == 0 and not guard['stop_reasons']
        and Path(guard['cwd']).resolve() == ROOT, 'A fresh process lacks a successful matching supervisor result')
    def option(name):
        require(command.count(name) == 1, 'Exactly one original diagnostic option required: ' + name)
        return command[command.index(name) + 1]
    def command_path(value):
        p = Path(value)
        return (p if p.is_absolute() else Path(guard['cwd']) / p).resolve()
    require(any(command_path(value) == ROOT / 'stage13_reproducibility_v3.py'
        for value in command if not str(value).startswith('--')), 'Supervisor command is not the exact V3 replay worker')
    require(command_path(option('--start')) == Path(original['candidate_path']).resolve(),
        'Supervisor candidate differs')
    require(command_path(option('--initial-npz')) == Path(data['initial_npz_path']).resolve()
        and command_path(option('--benchmark-checks')) == Path(data['stateless_control_provenance']['fresh_full_benchmark_checks_path']).resolve()
        and option('--label') == data['label'] and option('--workers') == '4'
        and option('--methods') == 'cached' and option('--repeats') == '3',
        'Supervisor command settings/input references differ')
    design_path = command_path(option('--epoch-design'))
    design = read(design_path)
    require(design_path == ROOT / 'integration_epochs' / original['label'] / 'epoch_design.json'
        and data['input_sha256'].get(str(design_path)) == digest(design_path)
        and design['physical_identity'] == original['physical_identity']
        and design['meshes'] == original['meshes'] and design['replay_policy'] == original['replay_policy'],
        'Supervisor epoch design differs from the immutable local qualification')
    if '--block-size' in command:
        require(option('--block-size') == '1024', 'Supervisor replay block size differs')
    require(int(guard['worker_pid']) > 1 and int(guard['supervisor_pid']) > 1
        and guard['worker_pid'] != guard['supervisor_pid'], 'Native worker/supervisor PIDs missing')
    require(data['workers'] == [4] and data['methods'] == ['cached']
        and data['fresh_repeats_per_method_and_workers'] == 3 and len(data['runs']) == 3
        and data['fresh_cached_instance_for_each_repeat'] and data['block_size'] == 1024,
        'Exactly three fresh cached4 instances at the qualified block policy required')
    require(data['original_namespace_identity_at_start']['passed']
        and data['original_namespace_identity_at_finish']['passed']
        and data['exact_input_scalar_exp_LRU_cleared_before_each_cached_repeat']
        and not data['cache_counters_or_resource_ledgers_reset'], 'Original namespace or cold-cache proof failed')
    require(data['initial_npz_path'] == original['endpoint_initial_arrays']['path']
        and data['input_sha256'][data['initial_npz_path']] == original['endpoint_initial_arrays']['sha256'],
        'Process initial anchor differs from the actual local V3 initial')
    for name, identity in data['source_sha256'].items():
        require(digest(ROOT / name) == identity, 'Diagnostic source changed: ' + name)
    for name, identity in data['input_sha256'].items():
        require(digest(name) == identity, 'Diagnostic input changed: ' + name)
    require(digest(data['reference_artifact_path']) == data['reference_artifact_sha256'], 'Reference arrays changed')
    p = np.asarray(candidate['core_parameters']); extra = np.asarray(candidate['extra_coefficients'])
    with np.load(original['endpoint_initial_arrays']['path'], allow_pickle=False) as arrays:
        actual_initial = arrays['residual'].copy()
    with np.load(data['reference_artifact_path'], allow_pickle=False) as arrays:
        require(array_hash(arrays['p']) == array_hash(p) and array_hash(arrays['extra']) == array_hash(extra)
            and np.array_equal(arrays['s'], mesh.s) and np.array_equal(arrays['theta'], mesh.theta)
            and np.array_equal(arrays['weights'], mesh.weights), 'Saved reference coordinates or parameters differ')
        initial, benchmark = arrays['initial'].copy(), arrays['benchmark'].copy()
    require(np.array_equal(initial, actual_initial), 'Process replaced its actual saved V3 initial vector')
    rows = []
    for row in data['runs']:
        clear = row['scalar_exp_LRU_clear_before_cold_instance']
        require(row['method'] == 'cached' and row['workers'] == 4 and row['fresh_instance']
            and clear['performed'] and clear['after']['current_entries'] == 0
            and not clear['counters_reset'] and not clear['resource_ledgers_reset']
            and row['original_namespace_identity_before']['passed']
            and row['original_namespace_identity_after']['passed'], 'A selected cold instance is incomplete')
        for pools in (row['threadpools_inside_context_before'], row['threadpools_inside_context_after']):
            require(pools and all(pool['num_threads'] == 4 for pool in pools if pool['user_api'] == 'blas'),
                'Recorded loaded BLAS thread policy differs from selected4')
        require(all(clear['before'][key] == clear['after'][key]
            for key in ('calls', 'hits', 'misses', 'evictions', 'peak_entries')), 'Memoization clear reset counters')
        require(digest(row['artifact_path']) == row['artifact_sha256'], 'Replay arrays changed')
        with np.load(row['artifact_path'], allow_pickle=False) as arrays:
            require(array_hash(arrays['p']) == array_hash(p) and array_hash(arrays['extra']) == array_hash(extra),
                'Replay physical parameters changed')
            residual = arrays['residual'].copy()
            require(np.array_equal(arrays['difference_from_initial'], residual - initial)
                and np.array_equal(arrays['difference_from_benchmark'], residual - benchmark), 'Saved differences differ')
        require(residual.shape == (mesh.size,) and np.all(np.isfinite(residual))
            and array_hash(residual) == row['residual_sha256'], 'Invalid saved selected-policy residual')
        rows.append({'label': data['label'] + '/' + row['label'], 'diagnostic': str(Path(path).resolve()),
            'vector': residual, 'artifact': ref(row['artifact_path'])})
    return data, rows, initial, benchmark, {'result': ref(guard_path),
        'worker_pid': int(guard['worker_pid']), 'supervisor_pid': int(guard['supervisor_pid']),
        'command_verified': True, 'epoch_design': ref(design_path)}


def run(args):
    began = time.time(); output = args.output.resolve()
    require(not output.exists(), 'Choose a fresh immutable V3 release output')
    require(len(args.diagnostic) >= 2 and len(set(str(p.resolve()) for p in args.diagnostic)) == len(args.diagnostic),
        'Two distinct fresh-process diagnostics required')
    original, candidate, policy, initial_record, mesh = validate_original(args.original_epoch, args.policy)
    rows = []; diagnostic_refs = []; processes = set(); worker_pids = set(); supervisor_pids = set()
    guard_proofs = []; anchor = baseline = None
    for path in args.diagnostic:
        data, process_rows, ri, rb, guard_proof = diagnostic_vectors(path, original, candidate, policy, mesh)
        process = data['environment_at_start']['resource_run']
        require(process and process not in processes, 'Distinct supervisor/native processes required')
        processes.add(process)
        require(guard_proof['worker_pid'] not in worker_pids and guard_proof['supervisor_pid'] not in supervisor_pids,
            'Fresh-process diagnostics reused a native worker or supervisor PID')
        worker_pids.add(guard_proof['worker_pid']); supervisor_pids.add(guard_proof['supervisor_pid'])
        guard_proofs.append(guard_proof)
        if anchor is None:
            anchor, baseline = ri, rb
        else:
            require(np.array_equal(anchor, ri) and np.array_equal(baseline, rb), 'Process saved anchors differ')
        rows += process_rows; diagnostic_refs.append(ref(path))
    endpoint = original['endpoint_restore']
    condition_bound = float(policy['condition_scaled_roundoff_factor'] * np.finfo(float).eps
        * endpoint['positive_term_condition_norm'])
    loss_limit = float(policy['max_residual_replay_induced_loss_perturbation_fraction_of_initial_integration_error']
        * initial_record['error_abs'])
    relative_limit = policy['previous_documented_provider_relative_limit']
    pairs = []; anchored = []; provider = []
    for index, a in enumerate(rows):
        row = compare(a['vector'], anchor, condition_bound, relative_limit, loss_limit)
        row.update(a=a['label'], b='actual_saved_V3_cached_initial', diagnostic=a['diagnostic']); anchored.append(row)
        row = compare(a['vector'], baseline, condition_bound, relative_limit, loss_limit)
        row.update(a=a['label'], b='fresh_benchmark_unchanged_stateless_reference'); provider.append(row)
        for b in rows[index + 1:]:
            row = compare(a['vector'], b['vector'], condition_bound, relative_limit, loss_limit)
            row.update(a=a['label'], b=b['label'], cross_process=a['diagnostic'] != b['diagnostic'])
            pairs.append(row)
    strict_pairs = bool(pairs and any(row['cross_process'] for row in pairs)
        and all(row['within_original_residual_relative_64epsilon'] for row in pairs))
    strict_anchor = bool(anchored and all(row['within_original_residual_relative_64epsilon'] for row in anchored))
    passed = bool(strict_pairs and strict_anchor and all(row['new_policy_passed'] for row in pairs + anchored + provider))
    review = {'schema': 'stage13_explicit_replay_policy_review_v3_private_scalar_exp', 'completed': True,
        'passed': passed, 'original_pending_epoch': ref(args.original_epoch), 'policy': ref(args.policy),
        'diagnostics': diagnostic_refs, 'physical_identity': physical_identity(candidate),
        'fresh_native_process_guard_proofs': guard_proofs,
        'cached_selected_workers': 4, 'cached_selected_policy_original64epsilon_passed': strict_pairs,
        'cached_selected_policy_vs_original_initial64epsilon_passed': strict_anchor,
        'cached_fresh_instance_process_strict_pairs': pairs, 'cached_vs_actual_saved_initial_strict_checks': anchored,
        'all_provider_and_reference_comparisons': provider,
        'condition_scaled_64epsilon_bound': condition_bound, 'induced_loss_change_limit': loss_limit,
        'original_local_endpoint_restore': endpoint, 'original_failed_V2_release': original['failed_v2_release'],
        'original_failed_V2_release_rewritten': False, 'original12_physical_design_retained': True,
        'old_points_relabelled_as_new_normalized_design': False,
        'original_integration_sources': integration_sources(), 'independent_source_sha256': independent_sources(),
        'reviewer_source_sha256': digest(__file__), 'all_selected_cold_memoization_clears_verified': True,
        'all_old_independent_namespace_sentinels_passed': True,
        'rigorous_floating_point_error_enclosure': False, 'uniform_neighborhood_certificate': False,
        'optimization_performed': False, 'elapsed_seconds': time.time() - began, 'environment': provenance()}
    output.mkdir(parents=True); atomic(output / 'review.json', review)
    if passed:
        released = copy.deepcopy(original)
        released.update(label=original['label'] + '_released_fresh_process', passed=True,
            original_pending_epoch=ref(args.original_epoch), supplemental_replay_review=ref(output / 'review.json'),
            supplemental_replay_policy=ref(args.policy), supplemental_replay_diagnostics=diagnostic_refs,
            fresh_process_cached_proof_pending=False, fresh_process_cached_replay_released=True,
            reviewer_source_sha256=digest(__file__), review_epoch=time.time())
        atomic(output / 'epoch.json', released)
        EpochIntegrator(candidate, output / 'epoch.json').require_qualified(candidate, 4)
    print({'review_path': str(output / 'review.json'), 'passed': passed,
        'strict_pairs': strict_pairs, 'strict_actual_initial': strict_anchor}, flush=True)
    if not passed:
        raise SystemExit(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostic', action='append', type=Path, required=True)
    parser.add_argument('--policy', type=Path, required=True)
    parser.add_argument('--original-epoch', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    run(parser.parse_args())


if __name__ == '__main__':
    main()
