#!/usr/bin/env python3
"""Read-only, fixed-endpoint Stage XIII V3 derivative and descent assessment.

All scientific arithmetic is imported from the frozen implementation. This
worker never commits an incumbent, updates a radius, changes a mesh, launches
an optimizer, or alters the campaign. Run under the verified resource guard.
"""
import argparse
import gc
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from absolute_common import A_REF, np, read, atomic, npz, digest, array_hash, provenance
from absolute_chart import hp_report, coefficients
from absolute_chart_v2 import AbsoluteC5ChartV2
from absolute_model_v2 import AbsoluteLossProblem
from stage13_model_v3 import CachedAbsoluteProblem, original_namespace_identity_record
from stage13_integration_v3 import EpochIntegrator
from stage13_solver import DenseTrustModel
from stage13_campaign_v3 import numerical_sources, feasible_trial, actual_matrix_kkt
from stage13_gradient_refinement_v3 import summary, normalize_physical
from stage12_common import e
from threadpoolctl import threadpool_limits


SCHEMA = 'stage13_v3_fixed_endpoint_independent_stationarity_assessment_v1'
DIRECTIONS = ('scaled_steepest_descent', 'largest_positive_singular',
              'middle_positive_singular', 'next_weakest_positive_singular',
              'weakest_positive_singular', 'physical_cl_increasing',
              'physical_a0_increasing')


def progress(folder, phase, **values):
    atomic(folder/'progress.json', {'schema': SCHEMA, 'phase': phase,
        'epoch': time.time(), **values})


def rel_error(delta, first, second=None):
    return float(np.linalg.norm(delta)/max(np.linalg.norm(first),
        np.linalg.norm(second) if second is not None else 0., 1e-300))


def refuse_partial(path):
    if path.exists() or path.with_name(path.name+'.partial').exists():
        raise ValueError('Preserved existing or partial artifact: '+str(path))


def save_complete(folder, stem, record, **arrays):
    path = folder/(stem+'.npz'); refuse_partial(path)
    record_path = folder/(stem+'.json'); refuse_partial(record_path)
    npz(path, **arrays)
    record = {**record, 'completed': True, 'arrays_path': str(path),
        'arrays_sha256': digest(path),
        'array_sha256': {key: array_hash(value) for key, value in arrays.items()}}
    atomic(record_path, record)
    return record


def load_complete(folder, stem):
    path = folder/(stem+'.json')
    if not path.exists(): return None
    record = read(path)
    if not record.get('completed') or digest(record['arrays_path']) != record['arrays_sha256']:
        raise ValueError('Incomplete or changed saved artifact: '+str(path))
    with np.load(record['arrays_path'], allow_pickle=False) as data:
        arrays = {name: data[name].copy() for name in data.files}
    if record['array_sha256'] != {key: array_hash(value) for key, value in arrays.items()}:
        raise ValueError('Saved numerical arrays changed: '+str(path))
    return record, arrays


def a0_raw_gradient(p):
    """Complex-step includes cl, exponents and analytic center elimination."""
    gradient = np.empty(24)
    for j in range(24):
        probe = p.astype(complex); probe[j] += 1e-25j
        gradient[j] = np.imag((e.v.jet.matrices(probe[0])@coefficients(probe))[0])/1e-25
    return gradient


def physical_diagnostics(unscaled, residual, tangent, extra_count):
    """Euclidean tangent gradient in raw (cl,c1..c23,extras) coordinates.

    B is the full physical tangent, B=QR. For chart gradient g=B.T grad,
    the unique tangent vector is Q solve(R.T,g). No normal equations or
    deleted singular directions are used. Its norm is a local parameter
    metric, not a coordinate-free PDE stationarity certificate.
    """
    B = np.zeros((24+extra_count, 19+extra_count))
    B[:24, :19] = tangent; B[24:, 19:] = np.eye(extra_count)
    Q, R = np.linalg.qr(B, mode='reduced')
    g = unscaled.T@residual
    physical = Q@np.linalg.solve(R.T, g)
    reconstruction_error = rel_error(B.T@physical-g, g)
    if reconstruction_error > 1e-10:
        raise ValueError('Physical tangent gradient does not reconstruct the complete chart gradient')
    return {'unscaled_feasible_gradient_components': g.tolist(),
        'unscaled_feasible_gradient_norm': float(np.linalg.norm(g)),
        'physical_euclidean_tangent_gradient_components': physical.tolist(),
        'physical_euclidean_tangent_gradient_norm': float(np.linalg.norm(physical)),
        'physical_gradient_cl_component': float(physical[0]),
        'physical_tangent_rank': int(np.linalg.matrix_rank(B)),
        'physical_gradient_chart_reconstruction_relative_error': reconstruction_error,
        'definition': 'B=diag(core_tangent,I162)=QR; physical tangent gradient Q solve(R.T,J_feasible.T@residual). Raw cl and coefficients use their existing Euclidean parameter units.',
        'normal_equations_used': False}, physical


def spectrum(model):
    value = model.stationarity(); positive = model.s > 0
    value.update(exact_zero_singular_values=int(np.count_nonzero(~positive)),
        all_strictly_positive_pairs_retained=True,
        positive_singular_range_projection_relative=float(
            np.linalg.norm(model.utr[positive])/max(np.linalg.norm(model.r), 1e-300)),
        singular_value_condition_positive=float(model.s[positive][0]/model.s[positive][-1]),
        stationarity_accepted=False)
    return value


def analytic_phase(folder, state, seed, integrator, p, extra, scales, args):
    existing = load_complete(folder, 'analytic')
    if existing is not None: return existing
    started = time.time(); chart = AbsoluteC5ChartV2(p); T = chart.base_tangent
    all_matrices = []; all_residuals = []; all_raw_gradients = []
    summaries = []; physical = []; phys_vectors = []; svds = []
    for name, mesh, blocks in (
            ('training', integrator.mesh, integrator.training_blocks),
            ('refined', integrator.refined_mesh, integrator.refined_blocks)):
        progress(folder, 'analytic_'+name, accepted=state['accepted'])
        problem = CachedAbsoluteProblem(seed, mesh, A_REF,
            block_size=args.block_size, workers=args.workers)
        r = problem.fun(p, extra); raw = problem.jacobian(p, extra)
        unscaled = np.column_stack((raw[:, :24]@T, raw[:, 24:]))
        if unscaled.shape != (mesh.size, 181):
            raise ValueError('Exactly all 181 current feasible columns are required')
        A = unscaled*scales
        raw_gradient = raw.T@r
        problem.clear_cache(); del problem, raw; gc.collect()
        scaled_summary, scaled_blocks = summary(A, r, blocks)
        unscaled_summary, unscaled_blocks = summary(unscaled, r, blocks)
        phys, vector = physical_diagnostics(unscaled, r, T, len(extra))
        with threadpool_limits(limits=1, user_api='blas'):
            model = DenseTrustModel(A, r)
        svds.append({'singular_values': model.s.copy(), 'vt': model.vt.copy(),
            'utr': model.utr.copy(), 'gradient': model.gradient.copy(),
            'spectrum': spectrum(model)})
        all_matrices.append(A); all_residuals.append(r); all_raw_gradients.append(raw_gradient)
        summaries.append({'scaled': scaled_summary, 'unscaled': unscaled_summary,
            'scaled_block_gradients': scaled_blocks.tolist(),
            'unscaled_block_gradients': unscaled_blocks.tolist()})
        physical.append(phys); phys_vectors.append(vector)
        del unscaled, model; gc.collect()
    A, fine_A = all_matrices; r, fine_r = all_residuals
    with np.load(state['arrays_path'], allow_pickle=False) as saved:
        if not np.array_equal(saved['p'], p) or not np.array_equal(saved['extra'], extra):
            raise ValueError('Accepted physical arrays changed')
        discrepancy = float(np.linalg.norm(saved['residual']-r))
        tolerance = 64*np.finfo(float).eps*max(np.linalg.norm(saved['residual']), np.linalg.norm(r), 1e-300)
    if discrepancy > tolerance:
        raise ValueError('Fresh V3 training residual failed original 64-epsilon restore')
    progress(folder, 'independent_refined_endpoint_value')
    stateless = AbsoluteLossProblem(seed, integrator.refined_mesh, A_REF, block_size=args.block_size)
    independent_r = stateless.fun(p, extra)
    independent_disagreement = rel_error(independent_r-fine_r, fine_r, independent_r)
    if independent_disagreement >= 5e-9:
        raise ValueError('Cached and independent stateless refined residuals disagree')
    positive_indices = np.flatnonzero(svds[0]['singular_values'] > 0)
    if len(positive_indices) != 181:
        raise ValueError('Unexpected exact null pair: preserve matrix and audit gauge before proceeding')
    raw_a0 = a0_raw_gradient(p)
    a0_feasible = np.r_[raw_a0@T, np.zeros(len(extra))]
    cl_feasible = np.r_[T[0], np.zeros(len(extra))]
    seeds = [-svds[0]['gradient'], svds[0]['vt'][positive_indices[0]],
        svds[0]['vt'][positive_indices[len(positive_indices)//2]],
        svds[0]['vt'][positive_indices[-2]], svds[0]['vt'][positive_indices[-1]],
        cl_feasible*scales, a0_feasible*scales]
    directions = []; physical_directions = []; direction_metadata = []
    for name, value in zip(DIRECTIONS, seeds):
        v, raw_v, length = normalize_physical(value, T, scales)
        directions.append(v); physical_directions.append(raw_v)
        direction_metadata.append({'name': name, 'coordinate_direction': v.tolist(),
            'linearized_physical_direction': raw_v.tolist(),
            'physical_direction_norm': float(np.linalg.norm(raw_v)),
            'raw_selection_physical_length': length,
            'cl_directional_change': float(raw_v[0]),
            'a0_directional_change': float(raw_a0@raw_v[:24]),
            'scaled_coordinate_norm': float(np.linalg.norm(v))})
    directions = np.asarray(directions)
    g = svds[0]['gradient']; fg = svds[1]['gradient']
    gradient_difference = float(np.linalg.norm(fg-g))
    gradient_relative = rel_error(fg-g, fg, g)
    block_difference = (np.asarray(summaries[1]['scaled_block_gradients'])
        -np.asarray(summaries[0]['scaled_block_gradients']))
    record = {'schema': SCHEMA, 'phase': 'analytic', 'accepted': state['accepted'],
        'snapshot_path': state['candidate_path'], 'snapshot_sha256': state['candidate_sha256'],
        'dimension': 181, 'raw_physical_dimension': 186, 'a_ref': A_REF,
        'five_Taylor': hp_report(p), 'chart_geometry': chart.geometry_diagnostics,
        'training': summaries[0], 'refined': summaries[1],
        'training_spectrum': svds[0]['spectrum'], 'refined_spectrum': svds[1]['spectrum'],
        'training_physical_gradient': physical[0], 'refined_physical_gradient': physical[1],
        'raw_unconstrained_physical_gradient_scope': '186 raw physical columns before C5 projection; distinct from 181 feasible and Euclidean tangent gradients',
        'gradient_refinement': {'difference_norm': gradient_difference,
            'relative_difference': gradient_relative, 'agreement_1e_3': bool(gradient_relative < 1e-3),
            'by_block_difference_norms': np.linalg.norm(block_difference, axis=1).tolist(),
            'rigorous_error_bound': False},
        'endpoint_residual_restore': {'difference_norm': discrepancy, 'tolerance': float(tolerance), 'passed': True},
        'independent_refined_residual': {'relative_disagreement': independent_disagreement,
            'tolerance': 5e-9, 'J_abs_refined': float(independent_r@independent_r/2), 'passed': True},
        'parameter_derivatives': {'a0_raw_gradient': raw_a0.tolist(),
            'a0_unscaled_feasible_gradient': a0_feasible.tolist(),
            'cl_unscaled_feasible_gradient': cl_feasible.tolist(),
            'method': 'Complex-step of complete analytic-center Taylor coefficient, including cl and radial exponents; new global modes vanish at center'},
        'directions': direction_metadata, 'no_rank_truncation': True,
        'column_scales_fixed_from_original_campaign': True,
        'physical_a0_and_cl_free': True, 'optimization_performed': False,
        'stationarity_accepted': False, 'elapsed_seconds': time.time()-started,
        'environment': provenance()}
    arrays = {'p': p, 'extra': extra, 'core_tangent': T, 'column_scales': scales,
        'training_residual': r, 'refined_residual': fine_r, 'independent_refined_residual': independent_r,
        'training_scaled_jacobian': A, 'refined_scaled_jacobian': fine_A,
        'training_singular_values': svds[0]['singular_values'], 'refined_singular_values': svds[1]['singular_values'],
        'training_vt': svds[0]['vt'], 'refined_vt': svds[1]['vt'],
        'training_utr': svds[0]['utr'], 'refined_utr': svds[1]['utr'],
        'training_gradient': g, 'refined_gradient': fg,
        'training_unconstrained_raw_gradient': all_raw_gradients[0],
        'refined_unconstrained_raw_gradient': all_raw_gradients[1],
        'training_physical_tangent_gradient': phys_vectors[0],
        'refined_physical_tangent_gradient': phys_vectors[1],
        'directions': directions, 'physical_directions': np.asarray(physical_directions),
        'a0_raw_gradient': raw_a0, 'a0_feasible_gradient': a0_feasible,
        'analytic_training_directional_residual_derivatives': A@directions.T,
        'analytic_refined_directional_residual_derivatives': fine_A@directions.T}
    record = save_complete(folder, 'analytic', record, **arrays)
    progress(folder, 'analytic_complete', gradient_norm=float(np.linalg.norm(g)),
        positive_projection=record['training_spectrum']['positive_singular_range_projection_relative'])
    return record, arrays


def physical_probe(folder, step_multiple, chart, p, extra, scales, direction,
                   model, args):
    tag = float(step_multiple).hex().replace('-', 'minus').replace('+', 'plus').replace('.', 'p')
    stem = 'step_'+tag
    delta = step_multiple*scales*direction
    pp = chart.lift_delta(delta[:19]); ee = extra+delta[19:]
    hp = hp_report(pp)
    if hp['max_abs'] >= 1e-10 or not hp['physical_bounds'] or abs(hp['a0']) <= 1e-12:
        raise ValueError('Independent feasible nonlinear probe fails C5 or physical bounds')
    existing = load_complete(folder, stem)
    if existing is not None:
        record, arrays = existing
        if not np.array_equal(arrays['p'], pp) or not np.array_equal(arrays['extra'], ee):
            raise ValueError('Probe physical coefficients differ on resume')
        return record, arrays['residual']
    began = time.time(); rr = model.fun(pp, ee)
    record = {'schema': SCHEMA, 'phase': 'independent_refined_probe',
        'signed_linearized_physical_step': step_multiple,
        'p': pp.tolist(), 'extra_sha256': array_hash(ee),
        'actual_full_physical_displacement_norm': float(np.linalg.norm(np.r_[pp-p, ee-extra])),
        'cl_change': float(pp[0]-p[0]), 'a0': hp['a0'],
        'five_Taylor': hp, 'J_abs_refined_rule': float(rr@rr/2),
        'independent_provider': 'Unchanged stateless absolute_model_v2.AbsoluteLossProblem on original refined whole-axis rule',
        'chart_lift': (chart.last_diagnostics if np.any(delta[:19]) else {
            'zero_core_step': True, 'core_endpoint_preserved_bitwise': True,
            'independent_HP': hp}), 'seconds': time.time()-began}
    record = save_complete(folder, stem, record, p=pp, extra=ee, residual=rr)
    return record, rr


def probes_phase(folder, analytic, arrays, seed, integrator, p, extra, scales, args):
    existing = load_complete(folder, 'directional_checks')
    if existing is not None: return existing[0]
    chart = AbsoluteC5ChartV2(p)
    if not np.array_equal(chart.base_tangent, arrays['core_tangent']):
        raise ValueError('Endpoint chart did not reproduce bitwise')
    model = AbsoluteLossProblem(seed, integrator.refined_mesh, A_REF, block_size=args.block_size)
    baseline = arrays['independent_refined_residual']; fine_r = arrays['refined_residual']
    all_rows = []; all_derivatives = []
    for index, name in enumerate(DIRECTIONS):
        directory = folder/name; directory.mkdir(exist_ok=True)
        existing_direction = load_complete(directory, 'checks')
        if existing_direction is not None:
            row, saved = existing_direction
            all_rows.append(row); all_derivatives.append(saved['FD_derivatives'])
            continue
        direction = arrays['directions'][index]
        expected = arrays['analytic_refined_directional_residual_derivatives'][:, index]
        expected_gradient = float(fine_r@expected)
        steps = []; derivatives = []; probe_records = {}
        for level in range(3):
            h = args.physical_step/(2**level); values = []; records = []
            for factor in (-2., -1., 1., 2.):
                signed = factor*h
                progress(folder, 'directional_probes', direction=name, level=level,
                    signed_physical_step=signed, completed_directions=len(all_rows))
                probe, value = physical_probe(directory, signed, chart, p, extra,
                    scales, direction, model, args)
                values.append(value); records.append(probe)
                probe_records[str(signed)] = {'path': probe['arrays_path'],
                    'sha256': probe['arrays_sha256'], 'J_abs_refined': probe['J_abs_refined_rule']}
            fd = (values[0]-8*values[1]+8*values[2]-values[3])/(12*h)
            objectives = [value['J_abs_refined_rule'] for value in records]
            objective_fd = (objectives[0]-8*objectives[1]+8*objectives[2]-objectives[3])/(12*h)
            residual_fd_gradient = float(baseline@fd)
            predicted_changes = [float(s*expected_gradient) for s in (-h, h)]
            observed_changes = [objectives[1]-float(baseline@baseline/2),
                                objectives[2]-float(baseline@baseline/2)]
            steps.append({'linearized_physical_step': h,
                'residual_derivative_relative_disagreement': rel_error(fd-expected, fd, expected),
                'analytic_residual_derivative_norm': float(np.linalg.norm(expected)),
                'FD_residual_derivative_norm': float(np.linalg.norm(fd)),
                'analytic_objective_directional_derivative': expected_gradient,
                'FD_residual_dot_objective_derivative': residual_fd_gradient,
                'FD_objective_derivative': float(objective_fd),
                'FD_objective_derivative_abs_disagreement': abs(float(objective_fd)-expected_gradient),
                'FD_residual_dot_abs_disagreement': abs(residual_fd_gradient-expected_gradient),
                'minus_plus_linear_objective_change': predicted_changes,
                'minus_plus_observed_objective_change': observed_changes,
                'maximum_probe_Taylor_defect': max(value['five_Taylor']['max_abs'] for value in records),
                'minus_plus_cl_changes': [records[1]['cl_change'], records[2]['cl_change']],
                'minus_plus_a0_changes': [records[1]['a0']-hp_report(p)['a0'], records[2]['a0']-hp_report(p)['a0']]})
            derivatives.append(fd)
        refinements = [rel_error(derivatives[k]-derivatives[k+1], derivatives[k], derivatives[k+1]) for k in (0, 1)]
        passed = bool(all(item['residual_derivative_relative_disagreement'] < 1e-3 for item in steps)
            and max(refinements) < 1e-3)
        row = {'schema': SCHEMA, 'name': name, 'metadata': analytic['directions'][index],
            'steps': steps, 'successive_step_relative_disagreements': refinements,
            'passed': passed, 'pass_scope': 'Three-step selected feasible residual derivative consistency, not stationarity',
            'probe_artifacts': probe_records,
            'endpoint_a0': hp_report(p)['a0'], 'endpoint_cl': float(p[0]),
            'all_probes_are_independently_evaluated_nonlinear_feasible_points': True,
            'chart_reanchored': False,
            'chart_convention': 'Every probe uses the same exact endpoint chart and fixed original campaign column scales; no endpoint is moved or reanchored.'}
        row = save_complete(directory, 'checks', row,
            FD_derivatives=np.asarray(derivatives), analytic_derivative=expected,
            scaled_coordinate_direction=direction,
            physical_direction=arrays['physical_directions'][index])
        all_rows.append(row); all_derivatives.append(np.asarray(derivatives))
        print(json.dumps({'direction': name, 'completed': len(all_rows), 'passed': passed}), flush=True)
    result = {'schema': SCHEMA, 'phase': 'selected_independent_feasible_FD',
        'dimension_of_analytic_gradient': 181, 'selected_direction_count': 7,
        'steps_per_direction': 3, 'unique_independent_probes_per_direction': 8,
        'rows': all_rows, 'passed': bool(all(row['passed'] for row in all_rows)),
        'all181_independent_FD_columns_evaluated': False,
        'stationarity_accepted': False, 'optimization_performed': False,
        'environment': provenance()}
    result = save_complete(folder, 'directional_checks', result,
        all_FD_derivatives=np.asarray(all_derivatives))
    progress(folder, 'directional_probes_complete', passed=result['passed'])
    return result


def descent_phase(folder, analytic, arrays, state, seed, integrator, p, extra, scales, args):
    existing = load_complete(folder, 'descent_checks')
    if existing is not None: return existing[0]
    chart = AbsoluteC5ChartV2(p)
    A = arrays['training_scaled_jacobian']; r = arrays['training_residual']
    with threadpool_limits(limits=1, user_api='blas'):
        factors = DenseTrustModel(A, r)
    production = CachedAbsoluteProblem(seed, integrator.mesh, A_REF,
        block_size=args.block_size, workers=args.workers)
    baseline_path = folder/'independent_baseline_validation.json'
    if baseline_path.exists():
        baseline = read(baseline_path)
    else:
        progress(folder, 'descent_baseline_validation')
        baseline = integrator.validate(p, extra, coarse_r=r)
        atomic(baseline_path, baseline)
    if not baseline['accuracy_passed'] or baseline.get('requires_refinement'):
        raise ValueError('Independent accepted-endpoint validation is inaccurate')
    rows = []; steps = []; pps = []; ees = []
    for index, factor in enumerate((1., .5)):
        directory = folder/('trust_radius_'+str(index)); directory.mkdir(exist_ok=True)
        radius = float(state['radius'])*factor
        step, subproblem = factors.step(radius)
        subproblem['actual_matrix_KKT_relative'] = actual_matrix_kkt(A, r, step, subproblem)
        if subproblem['actual_matrix_KKT_relative'] > 1e-8:
            raise ValueError('Unmodified trust subproblem fails original full-matrix KKT check')
        prediction = subproblem['actual_matrix_predicted_decrease']
        pp, ee, hp = feasible_trial(chart, p, extra, step, scales)
        existing_trial = load_complete(directory, 'checks')
        if existing_trial is not None:
            row, saved = existing_trial
            if not np.array_equal(saved['p'], pp) or not np.array_equal(saved['extra'], ee):
                raise ValueError('Trust diagnostic changed physical proposal on resume')
        else:
            progress(folder, 'unpromoted_trust_descent', radius=radius)
            rr = production.fun(pp, ee)
            validation = integrator.validate(pp, ee, coarse_r=rr,
                predicted_reduction=prediction, reference=baseline)
            decrease = float(baseline['J_abs']-validation['J_abs'])
            uncertainty = float(baseline['error_abs']+validation['error_abs'])
            mesh_decrease = float(r@r/2-rr@rr/2)
            ratio = mesh_decrease/prediction
            original_acceptance_passed = bool(
                mesh_decrease > 128*np.finfo(float).eps*max(float(r@r/2), 1e-300)
                and ratio > .1 and validation['accuracy_passed']
                and not validation.get('requires_refinement', False)
                and uncertainty <= .05*prediction and decrease > uncertainty)
            row = {'schema': SCHEMA, 'phase': 'unpromoted_feasible_descent',
                'radius_fraction': factor, 'radius': radius, 'trust_subproblem': subproblem,
                'baseline_validation_path': str(baseline_path),
                'baseline_validation_sha256': digest(baseline_path),
                'baseline_J_abs': baseline['J_abs'], 'trial_J_abs': validation['J_abs'],
                'independent_decrease': decrease, 'integration_uncertainty': uncertainty,
                'independent_gain_ratio': decrease/prediction,
                'predicted_decrease': prediction, 'mesh_decrease': mesh_decrease,
                'mesh_gain_ratio': ratio, 'trial_validation': validation,
                'trial_five_Taylor': hp, 'trial_cl': float(pp[0]), 'trial_a0': hp['a0'],
                'actual_full_physical_displacement_norm': float(np.linalg.norm(np.r_[pp-p, ee-extra])),
                'original_acceptance_checks_passed': original_acceptance_passed,
                'validated_descent_found': original_acceptance_passed,
                'accepted_incumbent_changed': False, 'trial_is_not_an_accepted_candidate': True,
                'optimization_performed': False}
            row = save_complete(directory, 'checks', row, p=pp, extra=ee,
                residual=rr, scaled_coordinate_step=step)
        rows.append(row); steps.append(step); pps.append(pp); ees.append(ee)
    production.clear_cache()
    result = {'schema': SCHEMA, 'phase': 'unpromoted_trust_descent',
        'rows': rows, 'validated_descent_exists': bool(any(row['validated_descent_found'] for row in rows)),
        'stationarity_accepted': False, 'accepted_incumbent_changed': False,
        'optimization_performed': False, 'environment': provenance()}
    result = save_complete(folder, 'descent_checks', result,
        scaled_coordinate_steps=np.asarray(steps), trial_ps=np.asarray(pps), trial_extras=np.asarray(ees))
    progress(folder, 'descent_complete', validated_descent_exists=result['validated_descent_exists'])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--campaign', type=Path, required=True)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--phase', choices=('analytic', 'probes', 'descent', 'all'), default='all')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--block-size', type=int, default=1024)
    parser.add_argument('--physical-step', type=float, default=2e-4)
    args = parser.parse_args()
    if args.workers != 4 or args.block_size != 1024 or not np.isfinite(args.physical_step) or args.physical_step <= 0:
        parser.error('Preserve qualified four-thread, block1024 arithmetic and a positive finite probe step')
    folder = args.output.resolve()
    allowed_results = Path(__file__).resolve().parents[1]/'results'
    if folder != allowed_results and allowed_results not in folder.parents:
        raise ValueError('New assessment outputs must stay inside this assessment results directory')
    folder.mkdir(parents=True, exist_ok=True)
    if (folder/'checks.json').exists(): raise ValueError('Completed assessment is immutable')
    state_path = folder/'bound_campaign_state.json'
    state = read(state_path if state_path.exists() else args.campaign/'state.json')
    if digest(args.snapshot) != state['candidate_sha256']:
        raise ValueError('Explicit requested snapshot is not the bound accepted state')
    for key, sha_key in (('candidate_path', 'candidate_sha256'), ('arrays_path', 'arrays_sha256'),
            ('epoch_path', 'epoch_sha256'), ('coordinate_map_path', 'coordinate_map_sha256'),
            ('parent_candidate_path', 'parent_candidate_sha256')):
        if digest(state[key]) != state[sha_key]: raise ValueError('Bound endpoint changed: '+key)
    if state['source_sha256'] != numerical_sources():
        raise ValueError('Frozen campaign numerical closure changed')
    if not state_path.exists(): atomic(state_path, state)
    seed = read(state['parent_candidate_path']); p = np.asarray(state['p']); extra = np.asarray(state['extra'])
    if p.shape != (24,) or extra.shape != (162,): raise ValueError('Current181D space required')
    with np.load(state['coordinate_map_path'], allow_pickle=False) as values:
        scales = values['column_scales'].copy()
    if scales.shape != (181,) or np.any(scales <= 0): raise ValueError('All fixed positive scales required')
    integrator = EpochIntegrator(seed, Path(state['epoch_path']))
    integrator.require_qualified(state['epoch_anchor_candidate'], workers=args.workers)
    binding = {'schema': SCHEMA, 'candidate_path': state['candidate_path'],
        'candidate_sha256': state['candidate_sha256'], 'accepted': state['accepted'],
        'bound_state_sha256': digest(state_path), 'script_sha256': digest(Path(__file__)),
        'epoch_sha256': state['epoch_sha256'], 'coordinate_map_sha256': state['coordinate_map_sha256'],
        'source_sha256': numerical_sources(), 'base_manifest_sha256': digest(ROOT/'provenance/base_manifest.json'),
        'verification_dependency_sha256': {'stage13_gradient_refinement_v3.py': digest(ROOT/'stage13_gradient_refinement_v3.py')},
        'workers': args.workers, 'block_size': args.block_size, 'physical_step': args.physical_step,
        'selected_directions': list(DIRECTIONS), 'a_ref': A_REF,
        'original_independent_namespace': original_namespace_identity_record()}
    if not binding['original_independent_namespace']['passed']:
        raise ValueError('Original independent namespaces changed')
    if (folder/'binding.json').exists():
        if read(folder/'binding.json') != binding: raise ValueError('Bound endpoint, source or settings changed')
    else: atomic(folder/'binding.json', binding)
    with threadpool_limits(limits=args.workers, user_api='blas'):
        analytic, arrays = analytic_phase(folder, state, seed, integrator, p, extra, scales, args)
        if (not np.array_equal(arrays['p'], p) or not np.array_equal(arrays['extra'], extra)
                or not np.array_equal(arrays['column_scales'], scales)
                or analytic['snapshot_sha256'] != state['candidate_sha256']):
            raise ValueError('Saved analytic evidence belongs to a different endpoint or coordinate map')
        if args.phase in ('probes', 'all'):
            probes_phase(folder, analytic, arrays, seed, integrator, p, extra, scales, args)
        if args.phase in ('descent', 'all'):
            descent_phase(folder, analytic, arrays, state, seed, integrator, p, extra, scales, args)
    direction_record = folder/'directional_checks.json'; descent_record = folder/'descent_checks.json'
    if direction_record.exists() and descent_record.exists():
        fd = read(direction_record); descent = read(descent_record)
        result = {'schema': SCHEMA, 'completed': True,
            'binding_path': str(folder/'binding.json'), 'binding_sha256': digest(folder/'binding.json'),
            'analytic_path': str(folder/'analytic.json'), 'analytic_sha256': digest(folder/'analytic.json'),
            'directional_path': str(direction_record), 'directional_sha256': digest(direction_record),
            'descent_path': str(descent_record), 'descent_sha256': digest(descent_record),
            'selected_derivative_checks_passed': fd['passed'],
            'gradient_quadrature_agreement_1e_3': analytic['gradient_refinement']['agreement_1e_3'],
            'validated_descent_exists': descent['validated_descent_exists'],
            'stationarity_accepted': False,
            'reason': 'A validated feasible descent rules out stationarity at the tested precision; failure to find one is not a stationarity certificate.',
            'optimization_performed': False, 'campaign_written': False,
            'original_namespace_at_finish': original_namespace_identity_record(),
            'environment': provenance()}
        atomic(folder/'checks.json', result)
    progress(folder, 'requested_phase_complete', requested_phase=args.phase,
        full_assessment_complete=(folder/'checks.json').exists())
    print(json.dumps({'output': str(folder), 'phase': args.phase,
        'full_assessment_complete': (folder/'checks.json').exists()}), flush=True)


if __name__ == '__main__': main()
