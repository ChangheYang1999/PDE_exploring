"""Stage XIII all-column SVD trust solver and actual-loss LSMR comparison.

The secular solver is copied from the independently validated Stage XII utility;
all positive singular directions remain. No normal equations are formed.
"""
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Stage XIII solver arithmetic requires the resource supervisor')

"""Euclidean Gauss--Newton trust step from an already computed thin SVD.

For A=U diag(s) Vt and u=U.T@r, minimize .5||r+A p||^2 subject
to ||p||<=radius.  Every strictly positive supplied singular value is used;
an exact zero gets the minimum-norm coordinate zero.  No numerical-rank
threshold, loss penalty, parameter bound, or nonlinear candidate selection is
introduced here.  Vt must have orthonormal rows, as in a genuine thin SVD.

The secular parameter is called damping=lambda, so the KKT multiplier of
.5*(||p||^2-radius^2) is mu=lambda^2.  Bisection returns the feasible side of
the secular bracket.  The one multiplication by Vt.T occurs after the scalar
solve; reported KKT diagnostics use the actual returned binary64 SVD coordinates.
Numerical work is permitted only under the Stage XII resource supervisor.
"""
import math
import os

if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Stage XII numerical work requires the verified resource supervisor')

import numpy as np


def arithmetic_metadata():
    """Describe actual secular precision; longdouble width is platform-specific."""
    extended = np.finfo(np.longdouble)
    binary64 = np.finfo(np.float64)
    return {
        'secular_dtype':np.dtype(np.longdouble).name,
        'secular_dtype_bytes':int(np.dtype(np.longdouble).itemsize),
        'secular_nmant':int(extended.nmant),
        'secular_epsilon':float(extended.eps),
        'secular_precision_scope':'scalar singular-coordinate filtering, secular norms/bracketing, and diagonal KKT arithmetic',
        'returned_coordinates_dtype':np.dtype(np.float64).name,
        'final_Vt_rotation_dtype':np.dtype(np.float64).name,
        'binary64_dtype_bytes':int(np.dtype(np.float64).itemsize),
        'binary64_nmant':int(binary64.nmant),
        'binary64_epsilon':float(binary64.eps),
        'PDE_residual_and_Jacobian_arithmetic':'unchanged historical binary64; this utility does not recompute or promote PDE arrays',
    }


def _norm(value):
    """Scaled long-double vector norm, including the identically zero case."""
    value = np.asarray(value, dtype=np.longdouble)
    largest = np.max(np.abs(value), initial=np.longdouble(0))
    return largest*np.sqrt(np.sum((value/largest)**2)) if largest else np.longdouble(0)


def _number(value):
    """JSON-safe scalar; extreme magnitudes retain a separate decimal string."""
    value = np.longdouble(value)
    if abs(value) > np.finfo(float).max:
        return None
    return float(value)


def trust_region_step(s, utr, vt, radius, *, relative_tolerance=1e-12,
                      max_iterations=256, max_bracket_iterations=4096):
    """Return (step, metadata) for the full-space Euclidean GN trust problem.

    Inputs are nonnegative singular values s, matching U.T@r, thin Vt, and a
    positive finite radius.  The caller supplies a valid SVD; no expensive
    orthogonality recomputation is performed.  Finite-precision metadata is a
    KKT diagnostic, not interval arithmetic or a nonlinear optimality claim.
    """
    s = np.asarray(s, dtype=float)
    utr = np.asarray(utr, dtype=float)
    vt = np.asarray(vt, dtype=float)
    radius = float(radius)
    if s.ndim != 1 or utr.shape != s.shape or vt.ndim != 2 or vt.shape[0] != len(s):
        raise ValueError('s, UTr, and thin Vt have inconsistent dimensions')
    if vt.shape[0] > vt.shape[1]:
        raise ValueError('Thin Vt must have no more rows than columns')
    if not np.all(np.isfinite(s)) or not np.all(np.isfinite(utr)) or not np.all(np.isfinite(vt)):
        raise ValueError('SVD data must be finite')
    if np.any(s < 0) or radius <= 0 or not math.isfinite(radius):
        raise ValueError('Singular values must be nonnegative and radius positive finite')
    if not 0 < relative_tolerance < .01 or max_iterations < 1 or max_bracket_iterations < 1:
        raise ValueError('Invalid secular-solve tolerance or iteration limit')

    sd, ud = s.astype(np.longdouble), utr.astype(np.longdouble)
    rd = np.longdouble(radius)
    positive = s > 0
    gn = np.zeros(len(s), dtype=np.longdouble)
    gn[positive] = -ud[positive]/sd[positive]
    gn_norm = _norm(gn)
    gradient = sd*ud
    gradient_norm = _norm(gradient)
    active = bool(gn_norm > rd)
    bracket_iterations = root_iterations = 0
    lower = upper = np.longdouble(0)

    def coordinates(damping):
        result = np.zeros(len(s), dtype=np.longdouble)
        # Extended precision avoids squaring a tiny positive binary64 singular
        # value to zero, or overflowing its undamped minimum-norm coordinate.
        result[positive] = -gradient[positive]/(sd[positive]**2+damping**2)
        return result

    if not active:
        q_long = gn
        damping = np.longdouble(0)
    else:
        # ||q(lambda)|| <= ||A.T r||/lambda^2 gives a finite feasible bound.
        upper = np.sqrt(gradient_norm/rd)
        q_upper = coordinates(upper)
        upper_norm = _norm(q_upper)
        while upper_norm > rd:
            upper *= 2
            q_upper = coordinates(upper)
            upper_norm = _norm(q_upper)
            bracket_iterations += 1
            if bracket_iterations >= max_bracket_iterations:
                raise RuntimeError('Could not find a feasible secular upper bound')
        # Bring the bracket to a factor of two before bisection.  This preserves
        # tiny positive directions even when the full spectrum is very wide.
        while True:
            lower = upper/2
            q_lower = coordinates(lower)
            lower_norm = _norm(q_lower)
            bracket_iterations += 1
            if lower_norm > rd:
                break
            upper, q_upper, upper_norm = lower, q_lower, lower_norm
            if bracket_iterations >= max_bracket_iterations:
                raise RuntimeError('Could not bracket the trust-region secular root')
        for root_iterations in range(1, max_iterations+1):
            if (rd-upper_norm)/rd <= relative_tolerance:
                break
            middle = (lower+upper)/2
            if middle == lower or middle == upper:
                break
            q_middle = coordinates(middle)
            middle_norm = _norm(q_middle)
            if middle_norm > rd:
                lower = middle
            else:
                upper, q_upper, upper_norm = middle, q_middle, middle_norm
        else:
            raise RuntimeError('Trust-region secular solve exceeded its iteration budget')
        if upper_norm > rd or (rd-upper_norm)/rd > relative_tolerance:
            raise RuntimeError('Trust-region secular root did not meet its radius tolerance')
        damping, q_long = upper, q_upper

    q = np.asarray(q_long, dtype=float)
    if not np.all(np.isfinite(q)):
        raise FloatingPointError('The finite-radius SVD coordinate step is not representable')
    # The only right-singular-vector multiplication in the utility.
    step = vt.T@q
    if not np.all(np.isfinite(step)):
        raise FloatingPointError('Rotated trust-region step is not representable')
    qd = q.astype(np.longdouble)
    multiplier = damping*damping
    response = sd*qd
    a_gradient = sd*(response+ud)
    multiplier_step = multiplier*qd
    kkt = a_gradient+multiplier_step
    q_norm, step_norm = _norm(qd), _norm(step)
    kkt_scale = max(gradient_norm, _norm(sd*response), _norm(multiplier_step))
    kkt_relative = _norm(kkt)/kkt_scale if kkt_scale else np.longdouble(0)
    complementary = multiplier*(q_norm-rd)*(q_norm+rd)
    complement_relative = abs((q_norm/rd)**2-1) if multiplier else np.longdouble(0)
    predicted = -np.sum(ud*response+response*response/2)
    positive_min = float(np.min(s[positive])) if np.any(positive) else None
    metadata = {
        'schema':'stage12-exact-euclidean-svd-gn-trust-v1',
        'arithmetic':arithmetic_metadata(),
        'radius':radius, 'active':active,
        'damping':_number(damping), 'damping_decimal':str(damping),
        'lagrange_multiplier':_number(multiplier), 'lagrange_multiplier_decimal':str(multiplier),
        'multiplier_convention':'mu=lambda^2 in A.T@(r+A p)+mu*p=0',
        'relative_tolerance':relative_tolerance,
        'bracket_iterations':bracket_iterations, 'root_iterations':root_iterations,
        'singular_values_supplied':len(s), 'positive_singular_values_used':int(np.sum(positive)),
        'exact_zero_singular_values':int(np.sum(~positive)),
        'smallest_positive_singular_value':positive_min,
        'no_numerical_rank_threshold':True, 'no_positive_singular_directions_deleted':True,
        'exact_zero_rule':'minimum-norm SVD coordinate zero',
        'unconstrained_minimum_norm':_number(gn_norm), 'unconstrained_minimum_norm_decimal':str(gn_norm),
        'svd_coordinate_step_norm':_number(q_norm), 'returned_step_norm':_number(step_norm),
        'relative_radius_gap':_number((rd-q_norm)/rd),
        'returned_step_relative_radius_gap':_number((rd-step_norm)/rd),
        'kkt_stationarity_diagonal_norm':_number(_norm(kkt)),
        'kkt_stationarity_diagonal_relative':_number(kkt_relative),
        'A_gradient_diagonal_norm':_number(_norm(a_gradient)),
        'lambda_squared_step_diagonal_norm':_number(_norm(multiplier_step)),
        'complementarity':_number(complementary),
        'complementarity_relative_to_mu_radius_squared':_number(complement_relative),
        'predicted_original_least_squares_decrease':_number(predicted),
        'predicted_response_norm':_number(_norm(response)),
        'svd_coordinate_step':q.tolist(),
        'svd_coordinate_A_gradient':[_number(v) for v in a_gradient],
        'svd_coordinate_lambda_squared_step':[_number(v) for v in multiplier_step],
        'svd_coordinate_KKT_residual':[_number(v) for v in kkt],
        'Vt_rows_orthonormal_assumed':True,
        'right_rotation_multiplications':1,
        'scope':'Finite-precision convex quadratic trust-subproblem solution; no nonlinear or interval certificate',
    }
    return step, metadata


# Explicit name for callers that also use a separate fixed-damping SVD backend.
solve_trust_region_svd = trust_region_step


class DenseTrustModel:
    """Full thin SVD of the actual absolute-loss feasible residual Jacobian."""
    def __init__(self,matrix,residual):
        from scipy.linalg import svd
        import time
        self.A=np.asarray(matrix,dtype=float)
        self.r=np.asarray(residual,dtype=float).ravel()
        if self.A.ndim!=2 or self.A.shape[0]!=len(self.r) or self.A.shape[0]<self.A.shape[1]:
            raise ValueError('Expected a tall full feasible residual Jacobian')
        if not np.all(np.isfinite(self.A)) or not np.all(np.isfinite(self.r)):
            raise ValueError('Nonfinite absolute-loss model')
        began=time.perf_counter()
        self.U,self.s,self.vt=svd(self.A,full_matrices=False,check_finite=False,lapack_driver='gesdd')
        self.factor_seconds=time.perf_counter()-began
        self.utr=self.U.T@self.r
        self.rank_floor=max(self.A.shape)*np.finfo(float).eps*self.s[0] if len(self.s) else 0.
        self.diagnostic_rank=int(np.sum(self.s>self.rank_floor))
        self.gradient=self.A.T@self.r

    def step(self,radius):
        import time
        began=time.perf_counter()
        step,metadata=trust_region_step(self.s,self.utr,self.vt,radius)
        # Reevaluate the prediction with the original matrix, because tiny
        # singular values and the final right rotation can amplify roundoff.
        response=self.A@step
        prediction=float(-self.r@response-response@response/2)
        metadata.update(actual_matrix_predicted_decrease=prediction,
            actual_matrix_response_norm=float(np.linalg.norm(response)),
            factor_seconds=self.factor_seconds,secular_and_rotation_seconds=time.perf_counter()-began,
            full_columns=self.A.shape[1],diagnostic_numerical_rank=self.diagnostic_rank,
            rank_threshold_only_diagnostic=True)
        return step,metadata

    def stationarity(self):
        return {'full_range_projected_residual_relative':float(np.linalg.norm(self.utr)/max(np.linalg.norm(self.r),1e-300)),
            'coordinate_gradient_norm':float(np.linalg.norm(self.gradient)),
            'coordinate_gradient_max_abs':float(np.max(abs(self.gradient),initial=0)),
            'singular_values':self.s.tolist(),'diagnostic_numerical_rank':self.diagnostic_rank,
            'all_columns':self.A.shape[1],'smallest_positive_singular_value':float(min(self.s[self.s>0])) if np.any(self.s>0) else None,
            'rank_threshold_only_diagnostic':True,'independent_stationarity_certificate':False}

    def compare_lsmr(self,radius,maxiter=None):
        """Same damping on the actual matrix; returned steps are diagnostics.

        The campaign independently evaluates both feasible nonlinear trial
        residuals. This function never promotes an iterative candidate.
        """
        from scipy.sparse.linalg import lsmr
        import time
        svd_step,metadata=self.step(radius)
        damping=float(metadata['damping'])
        began=time.perf_counter()
        iterative=lsmr(self.A,-self.r,damp=damping,atol=1e-12,btol=1e-12,
            conlim=1e16,maxiter=maxiter or max(1000,8*self.A.shape[1]))
        elapsed=time.perf_counter()-began
        lsmr_step=iterative[0];svd_response=self.A@svd_step;iterative_response=self.A@lsmr_step
        difference=np.linalg.norm(iterative_response-svd_response)/max(np.linalg.norm(svd_response),1e-300)
        normal_residual=self.A.T@(self.r+iterative_response)+damping*damping*lsmr_step
        gradient_scale=max(np.linalg.norm(self.gradient),np.linalg.norm(self.A.T@iterative_response),
            damping*damping*np.linalg.norm(lsmr_step),1e-300)
        report={'schema':'stage13_actual_absolute_loss_svd_lsmr_benchmark_v1',
            'matrix_shape':list(self.A.shape),'SVD':metadata,
            'LSMR':{'seconds':elapsed,'stop':int(iterative[1]),'iterations':int(iterative[2]),
                'reported_normr':float(iterative[3]),'reported_normar':float(iterative[4]),
                'condition_indicator':float(iterative[6]),'step_norm':float(np.linalg.norm(lsmr_step)),
                'actual_matrix_KKT_relative':float(np.linalg.norm(normal_residual)/gradient_scale),
                'actual_predicted_decrease':float(-self.r@iterative_response-iterative_response@iterative_response/2),
                'same_damping':damping,'atol':1e-12,'btol':1e-12,'conlim':1e16,
                'maxiter':maxiter or max(1000,8*self.A.shape[1])},
            'LSMR_response_relative_difference_from_full_SVD':float(difference),
            'LSMR_step_relative_difference_from_full_SVD':float(np.linalg.norm(lsmr_step-svd_step)/max(np.linalg.norm(svd_step),1e-300)),
            'all_positive_SVD_directions_retained':True,
            'no_normal_equation_matrix_formed':True,'nonlinear_trial_evaluations_pending':True,
            'selected_backend':'full_SVD'}
        return report,{'svd_step':svd_step,'lsmr_step':lsmr_step,
            'singular_values':self.s,'Vt':self.vt,'UTr':self.utr}
