"""Fresh V3 production qualification at exact recovered original V2 points.

Old independent references retain their old source identities. New production
values, derivatives, coordinates and strict replay evidence are separate. The
original physical trust design is retained; it is not a newly normalized ball.
"""
import argparse
import copy
from pathlib import Path
import time

from absolute_common import ROOT, A_REF, np, read, atomic, npz, digest, array_hash, provenance
from absolute_chart_v2 import AbsoluteC5ChartV2
from stage13_model_v3 import CachedAbsoluteProblem
from stage13_integration_v3 import (EpochIntegrator, physical_identity, integration_sources,
    independent_sources, require_original_namespace)
from stage13_qualification_v2 import derivative_evidence, replay_pair, start_vectors


def ref(path):
    path = Path(path).resolve()
    return {'path': str(path), 'sha256': digest(path)}


def bound(reference):
    if digest(reference['path']) != reference['sha256']:
        raise ValueError('Bound reference changed: ' + reference['path'])
    return read(reference['path'])


def recovery_evidence(path, original_epoch):
    recovery = read(path)
    if not (recovery.get('passed_exact_recovery_only') and recovery.get('all_twelve_physical_points_recovered_exactly')
            and recovery.get('all_parent_bound_runtime_sources_and_original_reference_inputs_unchanged')
            and len(recovery.get('recovered_points', [])) == 12):
        raise ValueError('Exact twelve-point recovery protocol2 proof is mandatory')
    binding = bound(recovery['binding'])
    if binding['original_epoch'] != ref(original_epoch):
        raise ValueError('Recovery belongs to another original reference epoch')
    for path_name, identity in binding['input_sha256'].items():
        if digest(path_name) != identity:
            raise ValueError('Original recovery source/input changed: ' + path_name)
    for name, identity in independent_sources().items():
        if binding['input_sha256'].get(str(ROOT / name)) != identity:
            raise ValueError('Unchanged independent closure is not fully covered by recovery: ' + name)
    for row in recovery['recovered_points']:
        point = bound(row['record']); bound(row['original_point'])
        if digest(row['arrays']['path']) != row['arrays']['sha256']:
            raise ValueError('Recovered full physical arrays changed')
        if not (point['physical_arrays_recovered_exactly'] and all(point['exact_hash_checks'].values())):
            raise ValueError('A recovered physical point failed an exact hash check')
    return recovery, binding


def policy_evidence(path, old_epoch):
    policy = read(path); previous = bound(old_epoch['replay_policy'])
    if not policy.get('private_production_sources'):
        raise ValueError('The upfront policy must bind the exact private production sources')
    for name, identity in policy['private_production_sources'].items():
        if digest(ROOT / name) != identity:
            raise ValueError('A policy-bound private production source changed: ' + name)
    if (policy.get('previous_v2_policy_path') != old_epoch['replay_policy']['path']
            or policy.get('previous_v2_policy_sha256') != old_epoch['replay_policy']['sha256']):
        raise ValueError('The V3 policy must preserve the exact original V2 policy lineage')
    unchanged = ('condition_scaled_roundoff_factor', 'previous_documented_provider_relative_limit',
        'max_residual_replay_induced_loss_perturbation_fraction_of_initial_integration_error',
        'production_origin_Taylor_order', 'independent_origin_Taylor_orders',
        'origin_overlap_85digit_tolerance_unchanged', 'minimum_cold_repeats_each')
    if any(policy[key] != previous[key] for key in unchanged):
        raise ValueError('The V3 repair must not relax an existing numerical threshold')
    if not (policy['selected_runtime_workers'] == 4 and policy['fresh_process_minimum'] >= 2
            and policy['cached_fresh_process_original64epsilon_relative_replay_required']
            and policy['fail_if_cached_replay_unresolved']):
        raise ValueError('An upfront selected4 strict cached-process replay policy is required')
    return policy


def prepare(args, candidate, old_epoch, recovery_binding):
    directory = ROOT / 'integration_epochs' / args.label; path = directory / 'epoch_design.json'
    if directory.exists():
        if not path.exists():
            raise ValueError('Incomplete/colliding V3 design directory')
        design = read(path)
        if (design['candidate_sha256'] != digest(args.start)
                or design['original_reference_epoch'] != ref(args.reference_epoch)
                or design['recovery'] != ref(args.recovery) or design['replay_policy'] != ref(args.replay_policy)):
            raise ValueError('Existing immutable V3 design binds other inputs')
        if (design['source_sha256_at_design'] != integration_sources()
                or design['independent_source_sha256'] != independent_sources()):
            raise ValueError('Existing V3 design binds a different production or independent source map')
        return directory, design
    failed = recovery_binding['failed_release_review']; old_review = bound(failed)
    if old_review['passed']:
        raise ValueError('The original failed V2 release must remain failed')
    directory.mkdir(parents=True)
    design = {'schema': 'stage13_integration_epoch_v3', 'label': args.label,
        'physical_identity': physical_identity(candidate), 'candidate_path': str(args.start.resolve()),
        'candidate_sha256': digest(args.start), 'a_ref': A_REF, 'center_convention': 'center_chart',
        'workers': args.workers, 'mesh_level': old_epoch['mesh_level'],
        'upper_log_radius': old_epoch['upper_log_radius'], 'meshes': copy.deepcopy(old_epoch['meshes']),
        'default_independent_error_abs': old_epoch['default_independent_error_abs'],
        'relative_accuracy': old_epoch['relative_accuracy'],
        'independent_initial_upper_log_radius': old_epoch['independent_initial_upper_log_radius'],
        'original_reference_epoch': ref(args.reference_epoch), 'recovery': ref(args.recovery),
        'failed_v2_release': failed, 'replay_policy': ref(args.replay_policy),
        'source_sha256_at_design': integration_sources(), 'independent_source_sha256': independent_sources(),
        'original_physical_trust_design_retained': True,
        'old_points_relabelled_as_new_normalized_design': False,
        'old_trust_coordinates': recovery_binding['initial_coordinates'],
        'fresh_production_column_scales_used_only_for_new_campaign_and_radius_conversion': True,
        'production_origin_order': 20, 'independent_origin_orders': [20, 24],
        'prepared_epoch': time.time(), 'whole_axis_qualified': False, 'neighborhood_validated': False,
        'representative_neighborhood_only': True, 'uniform_rigorous_certificate': False,
        'fresh_process_cached_proof_pending': True, 'passed': False}
    atomic(path, design); return directory, design


def fresh(candidate, mesh, p, extra, workers):
    model = CachedAbsoluteProblem(candidate, mesh, A_REF, block_size=1024, workers=workers)
    result = model.fun(p, extra); cache = model.cache_record(); model.clear_cache()
    return result, cache


def run(args):
    began = time.time(); candidate = read(args.start); old_epoch = read(args.reference_epoch)
    if args.workers != 4 or old_epoch['physical_identity'] != physical_identity(candidate):
        raise ValueError('V3 repair binds the unchanged accepted-six endpoint at selected4')
    policy = policy_evidence(args.replay_policy, old_epoch)
    recovery, recovery_binding = recovery_evidence(args.recovery, args.reference_epoch)
    directory, design = prepare(args, candidate, old_epoch, recovery_binding)
    print({'design_path': str(directory / 'epoch_design.json'), 'qualification_performed': False}, flush=True)
    if args.prepare_only:
        return
    if (directory / 'epoch.json').exists():
        raise ValueError('A completed V3 local epoch cannot be overwritten')
    if any((directory / name).exists() for name in
            ('starting_point.json', 'endpoint_initial.npz', 'initial_trust_coordinates.npz', 'trust_points')):
        raise ValueError('A partial V3 qualification is preserved; choose a fresh immutable label')
    derivative = derivative_evidence(args.derivative_record, candidate); benchmark = read(args.derivative_record)
    if not (benchmark['schema'] == 'stage13_actual_model_cache_benchmark_v3_origin20_private_scalar_exp'
            and benchmark['mesh_sha256'] == design['meshes']['training']['fingerprint']
            and benchmark['candidate_sha256'] == digest(args.start)):
        raise ValueError('The complete fresh V3 benchmark must bind this endpoint and exact mesh')
    for key in ('reference', 'production'):
        if digest(benchmark[key + '_arrays_path']) != benchmark[key + '_arrays_sha256']:
            raise ValueError('Fresh benchmark ' + key + ' arrays changed')
    p, extra = start_vectors(candidate); chart = AbsoluteC5ChartV2(p)
    integrator = EpochIntegrator(candidate, directory / 'epoch_design.json')
    with np.load(benchmark['reference_arrays_path'], allow_pickle=False) as arrays:
        stateless0 = arrays['residual'].copy()
        if array_hash(arrays['p']) != array_hash(p) or array_hash(arrays['extra']) != array_hash(extra):
            raise ValueError('Fresh benchmark stateless physical parameters differ')
    with np.load(benchmark['production_arrays_path'], allow_pickle=False) as arrays:
        production_benchmark = arrays['residual'].copy(); raw_jacobian = arrays['raw_jacobian'].copy()
        if array_hash(arrays['p']) != array_hash(p) or array_hash(arrays['extra']) != array_hash(extra):
            raise ValueError('Fresh benchmark production physical parameters differ')
    reduced = np.column_stack((raw_jacobian[:, :24] @ chart.base_tangent, raw_jacobian[:, 24:]))
    norms = np.linalg.norm(reduced, axis=0)
    if norms.shape != (181,) or not np.all(np.isfinite(norms)) or np.any(norms <= 0):
        raise ValueError('Every actual V3 feasible column must retain a positive scale')
    scales = 1 / norms
    r0, initial_cache = fresh(candidate, integrator.mesh, p, extra, args.workers)
    old_initial_ref = {'path': old_epoch['starting_point_path'], 'sha256': old_epoch['starting_point_sha256']}
    old_initial = bound(old_initial_ref)
    initial = integrator.validate_reference(p, extra, r0, old_initial, old_initial_ref)
    if not initial['accuracy_passed']:
        raise ValueError('Fresh V3 baseline disagrees with the unchanged whole-axis reference')
    starting_path = directory / 'starting_point.json'; atomic(starting_path, initial)
    npz(directory / 'endpoint_initial.npz', p=p, extra=extra, residual=r0, stateless_residual=stateless0)
    coordinate_path = directory / 'initial_trust_coordinates.npz'
    npz(coordinate_path, scales=scales, column_norms=norms, base_tangent=chart.base_tangent,
        reference_residual=r0, production_raw_jacobian=raw_jacobian)
    points = []
    for row in recovery['recovered_points']:
        proof = bound(row['record']); old_point = bound(row['original_point'])
        with np.load(row['arrays']['path'], allow_pickle=False) as arrays:
            pp, ee = arrays['p'].copy(), arrays['extra'].copy()
        if physical_identity(candidate, pp, ee) != row['physical_identity']:
            raise ValueError('Recovered full physical point identity changed')
        rr, cache = fresh(candidate, integrator.mesh, pp, ee, args.workers)
        validation = integrator.validate_reference(pp, ee, rr, old_point['validation'], row['original_point'])
        path = directory / 'trust_points' / ('point_' + str(row['index']).zfill(3) + '.json')
        path.parent.mkdir(exist_ok=True)
        record = {'index': row['index'], 'direction': old_point['direction'],
            'signed_trust_radius_multiple': old_point['signed_trust_radius_multiple'],
            'original_recovered_point': row, 'physical_identity': row['physical_identity'],
            'fresh_production_residual_sha256': array_hash(rr), 'production_cache': cache,
            'validation': validation, 'passed': validation['accuracy_passed'],
            'original_physical_trust_design_retained': True,
            'old_points_relabelled_as_new_normalized_design': False, 'candidate_promoted': False}
        atomic(path, record); points.append({**ref(path), 'passed': record['passed'],
            'direction': record['direction'], 'signed_trust_radius_multiple': record['signed_trust_radius_multiple']})
        print({'original_physical_point': row['index'], 'passed': record['passed']}, flush=True)
        if not record['passed']:
            raise ValueError('Fresh V3 production failed an exact original physical reference check')
    restored, final_cache = fresh(candidate, integrator.mesh, p, extra, args.workers)
    local_difference = float(np.linalg.norm(restored - r0))
    local_limit = float(64 * np.finfo(float).eps * max(np.linalg.norm(r0), np.linalg.norm(restored), 1e-300))
    old_condition = old_epoch['endpoint_restore']
    condition_path = old_condition['condition_arrays_path']; condition_sha = old_condition['condition_arrays_sha256']
    if digest(condition_path) != condition_sha:
        raise ValueError('Original unchanged positive-term condition scale changed')
    condition_bound = policy['condition_scaled_roundoff_factor'] * np.finfo(float).eps * old_condition['positive_term_condition_norm']
    provider_pairs = {name: replay_pair(a, b, condition_bound, initial['error_abs'], policy)
        for name, a, b in [('stateless_initial_cached', stateless0, r0),
            ('stateless_final_cached', stateless0, restored),
            ('benchmark_cached_initial', production_benchmark, r0)]}
    endpoint = {'passed': bool(local_difference <= local_limit
            and provider_pairs['benchmark_cached_initial']['strict64epsilon_passed']
            and all(row['condition_policy_passed'] for row in provider_pairs.values())),
        'bitwise_residual_restored': bool(np.array_equal(r0, restored)),
        'residual_difference_norm': local_difference, 'tolerance': local_limit,
        'physical_p_bitwise_restored': True, 'physical_extra_bitwise_restored': True,
        'positive_term_condition_norm': old_condition['positive_term_condition_norm'],
        'condition_scaled64epsilon_bound': float(condition_bound),
        'condition_arrays_path': condition_path, 'condition_arrays_sha256': condition_sha,
        'condition_reference_unchanged_old_stateless_provider': True,
        'stateless_and_cross_provider_checks': provider_pairs,
        'provider': 'Fresh V3 cached selected4 instances; no old failed cache values relabelled',
        'initial_cache': initial_cache, 'final_cache': final_cache}
    previous_J = candidate['objectives']['J_abs_independent']
    previous_error = candidate['objectives']['integration_error_diagnostic']
    discrepancy = abs(initial['J_abs'] - previous_J); comparison_limit = initial['error_abs'] + previous_error
    record = dict(design)
    record.update(completed=True, passed=False, local_qualification_passed=bool(endpoint['passed']),
        whole_axis_qualified=True, neighborhood_validated=True, endpoint_restore=endpoint,
        fresh_process_cached_proof_pending=True, fresh_process_cached_replay_released=False,
        source_sha256=integration_sources(), independent_source_sha256=independent_sources(),
        derivative_record=derivative, qualification_source_sha256=digest(__file__),
        starting_point_path=str(starting_path), starting_point_sha256=digest(starting_path),
        endpoint_initial_arrays=ref(directory / 'endpoint_initial.npz'),
        representative_points=points, exact_dilation_checks=copy.deepcopy(old_epoch['exact_dilation_checks']),
        exact_dilation_reference_reuse_only=True,
        initial_trust_coordinate_path=str(coordinate_path), initial_trust_coordinate_sha256=digest(coordinate_path),
        initial_column_scaled_trust_radius=.5 * float(np.linalg.norm(r0)), initial_trust_dimension=181,
        all_column_norms_positive=True, geometry=chart.geometry_diagnostics,
        unchanged_checkpoint_comparison={'passed': discrepancy <= comparison_limit,
            'difference': discrepancy, 'combined_error_diagnostic': comparison_limit,
            'physical_coefficients_changed': False},
        trust_qualification_scope='Fresh V3 production checked at the twelve EXACT ORIGINAL V2 physical points; their old normalized design is retained. New V3 production column scales are separate campaign preconditioning, not a relabeling of these points. Every future trial receives fresh independent integration.',
        all_19_core_and_every_extra_direction_retained=True, per_trial_independent_validation_required=True,
        original_independent_namespace=require_original_namespace(), optimization_performed=False,
        candidate_refit=False, environment=provenance(), elapsed_seconds=time.time() - began)
    if discrepancy > comparison_limit:
        record['local_qualification_passed'] = False
    atomic(directory / 'epoch.json', record)
    print({'epoch_path': str(directory / 'epoch.json'), 'local_passed': record['local_qualification_passed'],
        'passed': False, 'fresh_process_proof_pending': True}, flush=True)
    if not record['local_qualification_passed']:
        raise SystemExit(2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=Path, required=True)
    parser.add_argument('--label', required=True)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--reference-epoch', type=Path, required=True)
    parser.add_argument('--recovery', type=Path, required=True)
    parser.add_argument('--derivative-record', type=Path)
    parser.add_argument('--replay-policy', type=Path, required=True)
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    if '/' in args.label or '\\' in args.label:
        parser.error('Simple immutable epoch label required')
    run(args)


if __name__ == '__main__':
    main()
