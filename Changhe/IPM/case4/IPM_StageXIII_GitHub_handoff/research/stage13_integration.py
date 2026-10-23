"""Whole-axis integration epochs for Stage XIII.

Training always contains the origin, middle and infinity transformations.  Its
finite positive rule stays fixed during an epoch.  Independent adaptive panel
integration and analytic endpoint diagnostics are repeated for every proposed
physical point.  All error numbers are numerical diagnostics, not interval
certificates or a proof uniform over a trust ball.
"""
import gc
import hashlib
import json
import math
from pathlib import Path
import time

from absolute_common import ROOT, A_REF, np, read, atomic, npz, digest, array_hash, provenance
from absolute_model import FrozenLogMesh
from absolute_fields import prepare_candidate
from highprecision_origin import origin_diagnostics
from tail_envelope import outer_envelope
from log_integral import rule
from whole_axis_mesh import build_whole_axis_mesh


INTEGRATION_SOURCES = ('stage13_integration.py', 'stage13_model.py',
    'whole_axis_mesh.py', 'absolute_model.py', 'absolute_fields.py',
    'highprecision_origin.py', 'tail_envelope.py', 'outer_envelopes.py',
    'log_integral.py', 'absolute_common.py', 'absolute_chart.py', 'absolute_chart_v2.py',
    'field_tests.py')


def integration_sources():
    return {name: digest(ROOT/name) for name in INTEGRATION_SOURCES}


def physical_identity(candidate, p=None, extra=None):
    p = np.asarray(candidate.get('core_parameters', [candidate['cl']]+candidate['coefficients'][1:])
        if p is None else p, dtype=float)
    extra = np.asarray(candidate.get('extra_coefficients', []) if extra is None else extra, dtype=float)
    if p.shape != (24,) or len(extra) != len(candidate.get('modes', [])):
        raise ValueError('A complete physical candidate is required')
    modes = json.dumps(candidate.get('modes', []), sort_keys=True, separators=(',', ':'), allow_nan=False)
    return {'p_sha256': array_hash(p), 'extra_sha256': array_hash(extra),
        'modes_sha256': hashlib.sha256(modes.encode()).hexdigest(),
        'feasible_variables': 19+len(extra), 'a_ref': A_REF,
        'center_convention': 'center_chart'}


def _evaluate(candidate, p, extra, mesh, workers, block_size=1024):
    # This separate object has no training-rule state or coefficient cache.
    # The field algebra is the validated common physical evaluator; quadrature
    # nodes, angular rules, endpoint treatment and error accounting differ.
    # Deliberately use the original stateless evaluator here, independently of
    # the new optimizer's exact-last-cl field cache.  A value-only integral
    # does not need a full raw-Jacobian basis or its cl derivative cache.
    from absolute_model import AbsoluteLossProblem
    from threadpoolctl import threadpool_limits
    problem = AbsoluteLossProblem(candidate, mesh, a_ref=A_REF, block_size=block_size)
    with threadpool_limits(limits=workers, user_api='blas'):
        residual = problem.fun(p, extra)
    result = float(residual@residual/2)
    del problem
    gc.collect()
    return result, residual


def _panel(candidate, p, extra, lo, hi, radial_order, angular_order, angular_method, workers):
    s, theta, weights = rule(lo, hi, radial_order, angular_order, angular_method)
    mesh = FrozenLogMesh(s, theta, weights, 'independent_'+angular_method)
    value, residual = _evaluate(candidate, p, extra, mesh, workers)
    return {'J': value, 'radial_order': radial_order,
        'angular_order_or_intervals': angular_order, 'angular_method': angular_method,
        's_min': lo, 's_max': hi, 'nodes': mesh.size,
        'mesh_sha256': mesh.fingerprint, 'residual_sha256': array_hash(residual)}


def independent_integral(candidate, p, extra, workers=8, target_abs=1e-14,
        dilation=1., origin_radius=.02, initial_upper_log_radius=44.):
    """Whole-axis value with adaptive interval/rule and explicit endpoint errors.

    Dilation is a change in evaluation coordinates, never a basis refit.
    The independently refined point estimate uses the analytic origin integral
    and a sufficiently expanded middle interval.  The omitted infinity value
    is bounded by the independently derived all-angle outer envelope.
    """
    began = time.time()
    p = np.asarray(p, dtype=float); extra = np.asarray(extra, dtype=float)
    lam = float(dilation); target = float(target_abs)
    if not (math.isfinite(lam) and lam > 0 and math.isfinite(target) and target > 0):
        raise ValueError('Positive dilation and integration target required')
    prepared = prepare_candidate(candidate, 'center_chart', parameters=p, extra=extra)
    lo = math.log(float(origin_radius))/1.  # fixed physical origin overlap
    origin = origin_diagnostics(prepared, math.exp(lo)/lam, A_REF, (12, 16))
    if any(row['divergent_at_origin'] for row in origin['rows']):
        raise ValueError('Center-consistent model unexpectedly has an origin constant')
    origin_value = origin['rows'][-1]['polynomial_origin_integral']
    origin_error = origin['successive_order_integral_difference']
    # Independently evaluate the full analytic potential at the overlap point
    # with Cartesian high precision, rather than compare two truncations alone.
    from field_tests import independent_fields
    from highprecision_origin import residual_series, evaluate_series
    overlap_radius = min(.02, math.exp(lo)/lam)
    overlap_angle = 7*math.pi/32
    ox, oy = overlap_radius*math.cos(overlap_angle), overlap_radius*math.sin(overlap_angle)
    reference = independent_fields(prepared, ox, oy, precision=85)['Rf']
    series12 = residual_series(prepared, 12)['residual']
    series16 = residual_series(prepared, 16)['residual']
    v12 = float(evaluate_series(series12, ox, oy))
    v16 = float(evaluate_series(series16, ox, oy))
    overlap_tolerance = 1e-18+1e-7*abs(reference)
    overlap = {'radius': overlap_radius, 'angle': overlap_angle,
        'reference_85digit_Rf': reference, 'order12_Rf': v12, 'order16_Rf': v16,
        'order12_error_abs': abs(v12-reference), 'order16_error_abs': abs(v16-reference),
        'tolerance_abs': overlap_tolerance,
        'passed': bool(abs(v12-reference) <= overlap_tolerance and abs(v16-reference) <= overlap_tolerance),
        'scope': 'Independent Cartesian full-potential evaluation at an origin overlap point; no continuous Taylor remainder certificate.'}
    hi = float(initial_upper_log_radius); expansions = []
    while True:
        envelope = outer_envelope(prepared, math.exp(hi)/lam, A_REF)
        expansions.append({'s_max': hi, 'base_radius': math.exp(hi)/lam,
            'uniform_infinity_integral_envelope': envelope['integral_upper_bound']})
        if envelope['integral_upper_bound'] < target/16 or hi >= 100:
            break
        hi = min(hi+8., 100.)

    # Evaluate the dilation by translating s exactly. The integration interval
    # and endpoint division use physical coordinates; p/coefficients unchanged.
    shift = math.log(lam)
    lower, upper = lo-shift, hi-shift
    rows = []
    for order in (16, 32, 64, 128):
        row = _panel(candidate, p, extra, lower, upper, order, 96, 'gauss', workers)
        rows.append(row)
        if len(rows) >= 2 and abs(rows[-1]['J']-rows[-2]['J']) < target/2:
            break
    angular = _panel(candidate, p, extra, lower, upper, rows[-1]['radial_order'], 128,
        'trapezoid', workers)
    radial_error = abs(rows[-1]['J']-rows[-2]['J'])
    angular_error = abs(rows[-1]['J']-angular['J'])
    value = angular['J']+origin_value
    roundoff = 256*np.finfo(float).eps*max(abs(value), 1e-300)
    total_error = math.fsum((radial_error, angular_error, origin_error,
        envelope['integral_upper_bound'], roundoff))
    return {'schema': 'stage13_independent_whole_axis_integral_v1',
        'physical_identity': physical_identity(candidate, p, extra),
        'a_ref': A_REF, 'center_convention': 'center_chart', 'dilation': lam,
        'J_abs': value, 'error_abs': total_error, 'target_error_abs': target,
        'origin_tail_error_abs': origin_error,
        'infinity_tail_error_abs': envelope['integral_upper_bound'],
        'radial_quadrature_error_abs': radial_error,
        'angular_quadrature_error_abs': angular_error,
        'roundoff_floor_diagnostic': roundoff,
        'origin': origin, 'origin_independent_overlap': overlap, 'infinity_envelope': envelope,
        'interval_expansions': expansions, 'radial_refinements': rows,
        'independent_angular_check': angular,
        'accuracy_passed': bool(total_error <= target and overlap['passed']),
        'whole_axis_integral_is_mathematically_scale_invariant': True,
        'finite_rule_exact_invariance_claimed': False,
        'rigorous_error_certificate': False,
        'limitation': 'Origin and quadrature errors are order/refinement estimates; infinity envelope uses non-outward-rounded binary64. This is not a uniform trust-neighborhood certificate.',
        'seconds': time.time()-began}


def make_epoch_meshes(directory, label='epoch_0001', level=0, upper_log_radius=16.):
    """Write immutable three-block meshes. Level increases radial/angular order."""
    directory = Path(directory)
    if directory.exists():
        raise ValueError('Refusing to replace an integration epoch directory')
    directory.mkdir(parents=True)
    factor = 2**int(level)
    if level < 0 or level > 3:
        raise ValueError('A reviewed mesh level between zero and three is required')
    train, tmeta, tblocks = build_whole_axis_mesh(.02, upper_log_radius,
        24*factor, 16*factor, 128*factor, 64+32*level, name=label+'_training')
    fine, fmeta, fblocks = build_whole_axis_mesh(.02, upper_log_radius,
        48*factor, 32*factor, 256*factor, 96+32*level, name=label+'_refined')
    paths = {}
    for name, mesh, meta, blocks in (('training', train, tmeta, tblocks), ('refined', fine, fmeta, fblocks)):
        path = directory/(name+'.npz')
        npz(path, s=mesh.s, theta=mesh.theta, weights=mesh.weights, block_ids=blocks)
        paths[name] = {'path': str(path.resolve()), 'sha256': digest(path),
            'fingerprint': mesh.fingerprint, 'metadata': meta}
    return train, fine, tblocks, fblocks, paths


class EpochIntegrator:
    """Immutable numerical mesh plus independently checked trial acceptance."""
    def __init__(self, candidate_template, immutable_epoch_record_path):
        self.candidate = json.loads(json.dumps(candidate_template))
        self.path = Path(immutable_epoch_record_path).resolve()
        self.record = read(self.path)
        if self.record.get('schema') != 'stage13_integration_epoch_v1':
            raise ValueError('An explicit Stage XIII integration epoch is required')
        for name in ('training', 'refined'):
            row = self.record['meshes'][name]
            if digest(row['path']) != row['sha256']:
                raise ValueError('Immutable '+name+' mesh changed')
            mesh = FrozenLogMesh.load(row['path'])
            if mesh.fingerprint != row['fingerprint']:
                raise ValueError('Mesh identity mismatch')
            with np.load(row['path'], allow_pickle=False) as data:
                blocks = data['block_ids'].copy()
            setattr(self, 'mesh' if name == 'training' else 'refined_mesh', mesh)
            setattr(self, 'training_blocks' if name == 'training' else 'refined_blocks', blocks)
        self.workers = int(self.record['workers'])
        self._fine_problem = None

    def require_qualified(self, candidate, workers=8):
        r = self.record
        if not (r.get('passed') and r.get('whole_axis_qualified') and r.get('neighborhood_validated')
                and r.get('representative_neighborhood_only') and not r.get('uniform_rigorous_certificate')):
            raise ValueError('Incomplete empirical whole-axis epoch qualification')
        if r['physical_identity'] != physical_identity(candidate):
            raise ValueError('Epoch qualification binds a different physical endpoint')
        if int(workers) != self.workers:
            raise ValueError('Worker policy differs from the qualified epoch')
        if r['source_sha256'] != integration_sources():
            raise ValueError('Numerical integration/chart/field sources changed after qualification')
        if not r['endpoint_restore']['passed']:
            raise ValueError('Reference endpoint restoration was not established')
        derivative = r.get('derivative_record')
        if not derivative or not derivative.get('passed'):
            raise ValueError('Independent derivative qualification is mandatory')
        if digest(derivative['path']) != derivative['sha256']:
            raise ValueError('Independent derivative qualification record changed')
        return True

    def validate(self, p24, extraK, coarse_r=None, predicted_reduction=None, reference=None):
        began = time.time()
        p = np.asarray(p24, dtype=float); extra = np.asarray(extraK, dtype=float)
        from absolute_chart import hp_report
        feasible = hp_report(p)
        if (feasible['max_abs'] >= 1e-10 or not feasible['physical_bounds']
                or abs(feasible['a0']) <= 1e-12):
            raise ValueError('Whole-axis trial validation requires unchanged C5 and physical admissibility')
        if coarse_r is None:
            coarse_J, coarse_r = _evaluate(self.candidate, p, extra, self.mesh, self.workers)
        else:
            coarse_r = np.asarray(coarse_r, dtype=float)
            if coarse_r.shape != (self.mesh.size,) or not np.all(np.isfinite(coarse_r)):
                raise ValueError('A complete training residual is required')
            coarse_J = float(coarse_r@coarse_r/2)
        fine_J, fine_r = _evaluate(self.candidate, p, extra, self.refined_mesh, self.workers)
        blocks = {}
        for i, name in enumerate(('origin', 'middle', 'infinity')):
            x = coarse_r[self.training_blocks == i]; y = fine_r[self.refined_blocks == i]
            a, b = float(x@x/2), float(y@y/2)
            blocks[name] = {'training_J': a, 'refined_J': b,
                'refinement_error_diagnostic': abs(a-b)}
        mesh_error = math.fsum(row['refinement_error_diagnostic'] for row in blocks.values())
        default_target = float(self.record.get('default_independent_error_abs', 1e-14))
        target = max(default_target,
            self.record.get('relative_accuracy', 1e-6)*abs(coarse_J)/8)
        if predicted_reduction is not None:
            prediction = float(predicted_reduction)
            if not (math.isfinite(prediction) and prediction > 0):
                raise ValueError('Predicted decrease must be positive')
            target = min(target, .02*prediction)
        independent = independent_integral(self.candidate, p, extra, self.workers,
            target_abs=target, initial_upper_log_radius=self.record.get('independent_initial_upper_log_radius', 44.))
        difference = abs(coarse_J-independent['J_abs'])
        roundoff = 256*np.finfo(float).eps*max(coarse_J, fine_J, independent['J_abs'], 1e-300)
        # Include the observed training discrepancy explicitly, so it cannot be
        # hidden by optimistic radial-order differences or cancellation.
        error = max(difference+independent['error_abs'], mesh_error+independent['error_abs'])+roundoff
        tolerance = max(default_target, self.record.get('relative_accuracy', 1e-6)*abs(independent['J_abs']))
        accuracy = bool(independent['accuracy_passed'] and error <= tolerance)
        pair_error = error+(0. if reference is None else float(reference['error_abs']))
        requires = bool(not accuracy or (predicted_reduction is not None and pair_error > .05*predicted_reduction))
        return {'schema': 'stage13_trial_whole_axis_validation_v1',
            'physical_identity': physical_identity(self.candidate, p, extra),
            'J_abs': independent['J_abs'], 'error_abs': error,
            'training_J_abs': coarse_J, 'refined_J_abs': fine_J,
            'training_difference_from_independent': difference,
            'three_block_mesh_error_diagnostic': mesh_error,
            'block_contributions': blocks,
            'origin_tail_error_abs': independent['origin_tail_error_abs'],
            'infinity_tail_error_abs': independent['infinity_tail_error_abs'],
            'radial_quadrature_error_abs': independent['radial_quadrature_error_abs'],
            'angular_quadrature_error_abs': independent['angular_quadrature_error_abs'],
            'independent_integral': independent, 'accuracy_tolerance': tolerance,
            'five_Taylor_validation': feasible,
            'accuracy_passed': accuracy, 'requires_refinement': requires,
            'prediction': predicted_reduction, 'reference_plus_trial_error_abs': pair_error,
            'prediction_uncertainty_fraction_limit': .05,
            'mesh_sha256': self.mesh.fingerprint, 'epoch_path': str(self.path),
            'epoch_sha256': digest(self.path), 'a_ref': A_REF,
            'source_sha256': integration_sources(),
            'finite_quadrature_exact_invariance_claimed': False,
            'rigorous_error_certificate': False, 'seconds': time.time()-began}
