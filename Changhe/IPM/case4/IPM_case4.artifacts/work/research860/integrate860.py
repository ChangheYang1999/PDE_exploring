"""Independent whole-axis integration and trial validation for the 860 internal representation.

Port of the frozen stage13_integration_v2.independent_integral / EpochIntegrator.validate logic to the new
representation, using the stateless evaluator fields860 (original NumPy exp) which is independent of the cached
production provider. Components: order-48/56 analytic origin integral (Decimal residual polynomial, SPEC v9.3), 85-digit
Cartesian full-potential overlap check at r=0.02, all-angle uniform infinity envelope with interval expansion,
composite radial Gauss refinement (orders 16,32,64,128), independent angular rule (128 trapezoid vs 96 Gauss).
Error numbers are refinement/envelope diagnostics, not rigorous bounds.
"""
import gc, math, time
from decimal import Decimal, localcontext
import numpy as np
from threadpoolctl import threadpool_limits
import basis860 as B
from fields860 import residual as stateless_residual
from origin860 import origin_diagnostics, residual_series, evaluate_series_ld
from highprecision_origin import evaluate_series
from absolute_common import A_REF, array_hash
from absolute_model import FrozenLogMesh
from absolute_fields import _falling
from outer_envelopes import FIELDS as ENV_FIELDS, assembled_field_bounds, mode_field_constants
from log_integral import rule

D = Decimal


from hp860 import independent_fields   # own 85-digit evaluator with the frozen N_n (SPEC v5)


def outer_envelope(prepared, R, a_ref):
    """Uniform all-angle bound of |R_f| for r>=R from absolute coefficient sums (frozen inequalities).
    Low monomial H_m R^(p_j-m) t^h is bounded through t^h = sum_i (-1)^i C(h,i) u^i by the sum of pure-power bounds."""
    R = float(R); a_ref = float(a_ref); cl = float(prepared['cl'])
    if not (R >= 1 and math.isfinite(R) and a_ref > 0 and cl > 1): raise ValueError('Need finite R>=1, positive a_ref, cl>1')
    gamma = 1/cl; beta, alpha = gamma-1, gamma
    orders = {'f': 2., 'fx': 2.5, 'fy': 2.5, 'psix': 1.5, 'psiy': 1.5, 'ratio': 2.}
    targets = {'f': beta, 'fx': beta-1, 'fy': beta-1, 'psix': alpha, 'psiy': alpha, 'ratio': alpha-1}
    p, dp = B.p_exponents(cl)
    bound = {field: 0. for field in ENV_FIELDS}; active = 0
    for coefficient, (m, k, j) in zip(prepared['c'], B.LOW):
        if coefficient == 0: continue
        active += 1; h = k-m
        for i in range(h+1):
            b = p[j]-m-i; F, _ = _falling(b, dp[j]); raw = assembled_field_bounds([abs(v) for v in F], 2*m)
            for field in ENV_FIELDS:
                power = (b+m)-orders[field]
                bound[field] += math.comb(h, i)*abs(float(coefficient))*raw[field]*(1+1/R**2)**max(0., power)*R**(2*power-targets[field])
    for coefficient, mode in zip(prepared['g'], prepared['modes']):
        if coefficient == 0: continue
        active += 1; raw = mode_field_constants(mode, cl, R, beta, alpha)
        for field in ENV_FIELDS: bound[field] += abs(float(coefficient))*raw[field]
    Cf = bound['f']; Dg = math.hypot(bound['fx'], bound['fy']); V = math.hypot(bound['psix'], bound['psiy']); W = bound['ratio']
    Aa = cl*Dg+abs(cl-1)*Cf; Bb = V*Dg+W*Cf; eta = alpha+beta-1
    terms = [Aa*Aa*R**(2*beta)/(-2*beta), 2*Aa*Bb*R**(beta+eta)/(-beta-eta), Bb*Bb*R**(2*eta)/(-2*eta)]
    return {'schema': 'absolute_loss_uniform_outer_envelope_860_v2', 'radius': R, 'integral_upper_bound': sum(terms)/(2*a_ref*a_ref),
            'field_constants': bound, 'residual_constants': {'A': Aa, 'B': Bb}, 'active_functions': active, 'outward_rounded': False}


def _panel(prepared, lo, hi, radial_order, angular_order, angular_method, workers):
    s, theta, weights = rule(lo, hi, radial_order, angular_order, angular_method)
    mesh = FrozenLogMesh(s, theta, weights, 'independent_'+angular_method)
    x, y = mesh.coordinates(); root = np.sqrt(2*weights/(np.pi*A_REF**2))
    with threadpool_limits(limits=1, user_api='blas'): residual = root*stateless_residual(prepared, x, y, block_size=4096, procs=workers)
    value = float(residual@residual/2); gc.collect()
    return {'J': value, 'radial_order': radial_order, 'angular_order_or_intervals': angular_order, 'angular_method': angular_method,
            's_min': lo, 's_max': hi, 'nodes': mesh.size, 'mesh_sha256': mesh.fingerprint, 'residual_sha256': array_hash(residual)}


def physical_identity(P, g):
    return {'P_sha256': array_hash(np.asarray(P, float)), 'g_sha256': array_hash(np.asarray(g, float)), 'basis_version': B.VERSION,
            'feasible_variables': B.NFEASIBLE_CLAIMED, 'a_ref': A_REF, 'center_convention': 'center_chart'}


def independent_integral(P, g, workers=4, target_abs=1e-14, dilation=1., origin_radius=.02, initial_upper_log_radius=44.):
    began = time.time(); P = np.asarray(P, float); g = np.asarray(g, float); lam = float(dilation); target = float(target_abs)
    if not (math.isfinite(lam) and lam > 0 and math.isfinite(target) and target > 0): raise ValueError('Positive dilation and target required')
    prepared = B.prepare(P[0], P[1:], g)
    lo = math.log(float(origin_radius))
    origin = origin_diagnostics(prepared, math.exp(lo)/lam, A_REF, (48, 56))
    if any(row['divergent_at_origin'] for row in origin['rows']): raise ValueError('Center-consistent model unexpectedly has an origin constant')
    origin_value = origin['rows'][-1]['polynomial_origin_integral']; origin_error = origin['successive_order_integral_difference']
    overlap_radius = min(.02, math.exp(lo)/lam); overlap_angle = 7*math.pi/32
    ox, oy = overlap_radius*math.cos(overlap_angle), overlap_radius*math.sin(overlap_angle)
    reference = independent_fields(prepared, ox, oy, precision=85)['Rf']
    v20 = float(evaluate_series_ld(residual_series(prepared, 48)['residual'], ox, oy)[0]); v24 = float(evaluate_series_ld(residual_series(prepared, 56)['residual'], ox, oy)[0])
    overlap_tolerance = 1e-18+1e-7*abs(reference)
    overlap = {'radius': overlap_radius, 'angle': overlap_angle, 'reference_85digit_Rf': reference, 'order48_Rf': v20, 'order56_Rf': v24,
               'order48_error_abs': abs(v20-reference), 'order56_error_abs': abs(v24-reference), 'tolerance_abs': overlap_tolerance,
               'passed': bool(abs(v20-reference) <= overlap_tolerance and abs(v24-reference) <= overlap_tolerance)}
    hi = float(initial_upper_log_radius); expansions = []
    while True:
        envelope = outer_envelope(prepared, math.exp(hi)/lam, A_REF)
        expansions.append({'s_max': hi, 'base_radius': math.exp(hi)/lam, 'uniform_infinity_integral_envelope': envelope['integral_upper_bound']})
        if envelope['integral_upper_bound'] < target/16 or hi >= 100: break
        hi = min(hi+8., 100.)
    shift = math.log(lam); lower, upper = lo-shift, hi-shift
    rows = []
    for order in (16, 32, 64, 128):
        rows.append(_panel(prepared, lower, upper, order, 96, 'gauss', workers))
        if len(rows) >= 2 and abs(rows[-1]['J']-rows[-2]['J']) < target/2: break
    angular = _panel(prepared, lower, upper, rows[-1]['radial_order'], 128, 'trapezoid', workers)
    radial_error = abs(rows[-1]['J']-rows[-2]['J']); angular_error = abs(rows[-1]['J']-angular['J'])
    value = angular['J']+origin_value; roundoff = 256*np.finfo(float).eps*max(abs(value), 1e-300)
    total_error = math.fsum((radial_error, angular_error, origin_error, envelope['integral_upper_bound'], roundoff))
    return {'schema': 'independent_whole_axis_integral_860_v1', 'physical_identity': physical_identity(P, g), 'a_ref': A_REF, 'dilation': lam,
            'J_abs': value, 'error_abs': total_error, 'target_error_abs': target, 'origin_tail_error_abs': origin_error,
            'infinity_tail_error_abs': envelope['integral_upper_bound'], 'radial_quadrature_error_abs': radial_error,
            'angular_quadrature_error_abs': angular_error, 'roundoff_floor_diagnostic': roundoff, 'origin': origin,
            'origin_independent_overlap': overlap, 'infinity_envelope': envelope, 'interval_expansions': expansions,
            'radial_refinements': rows, 'independent_angular_check': angular,
            'accuracy_passed': bool(total_error <= target and overlap['passed']), 'rigorous_error_certificate': False, 'seconds': time.time()-began}


class Integrator860:
    """Training/refined three-block meshes of the frozen epoch plus fresh independent integration per physical trial."""
    def __init__(self, epoch_record, workers=4):
        self.record = epoch_record; self.workers = int(workers)
        for name in ('training', 'refined'):
            row = epoch_record['meshes'][name]; mesh = FrozenLogMesh.load(row['path'])
            if mesh.fingerprint != row['fingerprint']: raise ValueError('mesh identity differs')
            with np.load(row['path'], allow_pickle=False) as arrays: blocks = arrays['block_ids'].copy()
            setattr(self, 'mesh' if name == 'training' else 'refined_mesh', mesh)
            setattr(self, 'training_blocks' if name == 'training' else 'refined_blocks', blocks)
        self.default_target = float(epoch_record.get('default_independent_error_abs', 1e-14))
        self.relative_accuracy = float(epoch_record.get('relative_accuracy', 1e-6))
        self.initial_upper_log_radius = float(epoch_record.get('independent_initial_upper_log_radius', 44.))

    def stateless(self, P, g, mesh):
        prepared = B.prepare(P[0], P[1:], g); x, y = mesh.coordinates(); root = np.sqrt(2*mesh.weights/(np.pi*A_REF**2))
        with threadpool_limits(limits=1, user_api='blas'): r = root*stateless_residual(prepared, x, y, block_size=4096, procs=self.workers)
        return r

    def validate(self, P, g, coarse_r=None, predicted_reduction=None, reference=None):
        began = time.time(); P = np.asarray(P, float); g = np.asarray(g, float)
        import chart860
        feasible = chart860.hp_report(P)
        if feasible['max_abs'] >= 1e-10 or not feasible['physical_bounds'] or abs(feasible['a0']) <= 1e-12: raise ValueError('Trial validation requires C5 feasibility and admissibility')
        if coarse_r is None: coarse_r = self.stateless(P, g, self.mesh)
        coarse_r = np.asarray(coarse_r, float)
        if coarse_r.shape != (self.mesh.size,) or not np.all(np.isfinite(coarse_r)): raise ValueError('complete training residual required')
        coarse_J = float(coarse_r@coarse_r/2)
        fine_r = self.stateless(P, g, self.refined_mesh); fine_J = float(fine_r@fine_r/2)
        blocks = {}
        for i, name in enumerate(('origin', 'middle', 'infinity')):
            x = coarse_r[self.training_blocks == i]; y = fine_r[self.refined_blocks == i]; a, b = float(x@x/2), float(y@y/2)
            blocks[name] = {'training_J': a, 'refined_J': b, 'refinement_error_diagnostic': abs(a-b)}
        mesh_error = math.fsum(row['refinement_error_diagnostic'] for row in blocks.values())
        target = max(self.default_target, self.relative_accuracy*abs(coarse_J)/8)
        if predicted_reduction is not None:
            prediction = float(predicted_reduction)
            if not (math.isfinite(prediction) and prediction > 0): raise ValueError('Predicted decrease must be positive')
            target = min(target, .02*prediction)
        independent = independent_integral(P, g, self.workers, target_abs=target, initial_upper_log_radius=self.initial_upper_log_radius)
        difference = abs(coarse_J-independent['J_abs'])
        roundoff = 256*np.finfo(float).eps*max(coarse_J, fine_J, independent['J_abs'], 1e-300)
        error = max(difference+independent['error_abs'], mesh_error+independent['error_abs'])+roundoff
        tolerance = max(self.default_target, self.relative_accuracy*abs(independent['J_abs']))
        accuracy = bool(independent['accuracy_passed'] and error <= tolerance)
        pair_error = error+(0. if reference is None else float(reference['error_abs']))
        requires = bool(not accuracy or (predicted_reduction is not None and pair_error > .05*predicted_reduction))
        return {'schema': 'trial_whole_axis_validation_860_v1', 'physical_identity': physical_identity(P, g), 'J_abs': independent['J_abs'],
                'error_abs': error, 'training_J_abs': coarse_J, 'refined_J_abs': fine_J, 'training_difference_from_independent': difference,
                'three_block_mesh_error_diagnostic': mesh_error, 'block_contributions': blocks,
                'origin_tail_error_abs': independent['origin_tail_error_abs'], 'infinity_tail_error_abs': independent['infinity_tail_error_abs'],
                'radial_quadrature_error_abs': independent['radial_quadrature_error_abs'], 'angular_quadrature_error_abs': independent['angular_quadrature_error_abs'],
                'independent_integral': independent, 'accuracy_tolerance': tolerance, 'five_Taylor_validation': feasible,
                'accuracy_passed': accuracy, 'requires_refinement': requires, 'prediction': predicted_reduction,
                'reference_plus_trial_error_abs': pair_error, 'prediction_uncertainty_fraction_limit': .05,
                'mesh_sha256': self.mesh.fingerprint, 'a_ref': A_REF, 'rigorous_error_certificate': False, 'seconds': time.time()-began}
