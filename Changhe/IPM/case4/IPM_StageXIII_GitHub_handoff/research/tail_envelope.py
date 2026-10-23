"""Uniform far-field envelopes for the center-compatible analytic potentials.

Every inequality used to derive the envelope is uniform over r>=R and the
whole quadrant. The returned scalar is evaluated in ordinary binary64; no
outward-rounded interval certificate is claimed. Run numerical callers under
the separate absolute-loss resource supervisor.
"""
import math
import os

if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Absolute-loss tail envelopes require the resource supervisor')

from absolute_fields import _core_exponents, _falling
from outer_envelopes import FIELDS, assembled_field_bounds, mode_field_constants


def outer_envelope(prepared, R, a_ref):
    """Bound full physical Rf using all saved core and added coefficients.

    For beta=gamma-1 and alpha=gamma, fields obey f<=C*r^beta,
    |grad f|<=D*r^(beta-1), |U|<=V*r^alpha, ratio<=W*r^(alpha-1).
    Thus |Rf|<=A*r^beta+B*r^(alpha+beta-1). Absolute coefficient
    sums preserve every mode and require no fitted asymptotic slope.
    """
    R = float(R)
    a_ref = float(a_ref)
    cl = float(prepared['parameters'][0])
    if not (R >= 1 and math.isfinite(R) and a_ref > 0 and cl > 1):
        raise ValueError('Need finite R>=1, positive reference amplitude, and cl>1')
    gamma = 1/cl
    beta, alpha = gamma-1, gamma
    if not 0 < gamma < 1:
        raise ValueError('Need the sublinear canonical branch')
    orders = {'f': 2., 'fx': 2.5, 'fy': 2.5, 'psix': 1.5, 'psiy': 1.5, 'ratio': 2.}
    targets = {'f': beta, 'fx': beta-1, 'fy': beta-1,
               'psix': alpha, 'psiy': alpha, 'ratio': alpha-1}
    Achi = (3+gamma)/2
    bound = {field: 0. for field in FIELDS}
    contributions = []
    for index, (coefficient, data) in enumerate(zip(prepared['coefficients'], _core_exponents(cl))):
        if coefficient == 0:
            continue
        m, b, db, sigma, _ = data
        F, _ = _falling(b, db)
        raw = assembled_field_bounds([abs(value) for value in F], 2*m)
        one = {}
        for field in FIELDS:
            power = Achi-sigma-orders[field]
            factor = (1+1/R**2)**max(0., power) * R**(2*power-targets[field])
            one[field] = abs(float(coefficient)) * raw[field] * factor
            bound[field] += one[field]
        contributions.append({'kind': 'core', 'index': index, 'm': m, 'sigma': sigma,
                              'field_constants': one})
    for index, (coefficient, mode) in enumerate(zip(prepared['extra'], prepared['modes'])):
        if coefficient == 0:
            continue
        raw = mode_field_constants(mode, cl, R, beta, alpha)
        one = {field: abs(float(coefficient))*raw[field] for field in FIELDS}
        for field in FIELDS:
            bound[field] += one[field]
        contributions.append({'kind': 'extra', 'index': index, 'family': mode['family'],
                              'm': mode['m'], 'field_constants': one})
    C = bound['f']
    D = math.hypot(bound['fx'], bound['fy'])
    V = math.hypot(bound['psix'], bound['psiy'])
    W = bound['ratio']
    A = cl*D+abs(cl-1)*C
    B = V*D+W*C
    eta = alpha+beta-1
    terms = [A*A*R**(2*beta)/(-2*beta),
             2*A*B*R**(beta+eta)/(-beta-eta),
             B*B*R**(2*eta)/(-2*eta)]
    integral_bound = sum(terms)/(2*a_ref*a_ref)
    return {'schema': 'absolute_loss_uniform_outer_envelope_v1',
            'radius': R, 'log_radius': math.log(R), 'reference_amplitude': a_ref,
            'integral_upper_bound': integral_bound,
            'integral_upper_bound_arithmetic': 'Conservative analytic formula evaluated in binary64; no outward rounding certificate.',
            'field_constants': bound, 'combined_field_constants': {'C_f': C, 'D_grad_f': D, 'V_U': V, 'W_ratio': W},
            'field_exponents': targets,
            'residual_constants': {'A': A, 'B': B},
            'residual_exponents': {'beta': beta, 'eta': eta},
            'integrated_nonnegative_terms_before_normalization': terms,
            'active_mode_count': len(contributions),
            'uniform_all_angles_and_radii': True,
            'assumes_leading_cancellation': False,
            'outward_rounded_numerical_certificate': False,
            'literal_saved_center_repaired': False,
            'origin_divergence_not_resolved_by_this_outer_bound': True,
            'derivation': [
                '|Re(z^d) derivatives of order j| <= falling(d,j), |z|<=1.',
                '|Im(z^n)/Im(z)| <= n on |z|<=1; its y-derivative divided by y is bounded by n(n-1)(n-2)/3.',
                'Legendre d_t^h P_n(2t-1) <= (n+h)!/[h!(n-h)!] on 0<=t<=1, with campaign normalization retained.',
                's=log(1+r^2) derivatives use Stirling coefficients and u<=1/(1+R^2).',
                'Local Hermite-polynomial Gaussian tails use monomial suprema at z=max(z_lower,sqrt(power),0).',
                '|Rf| <= (cl D+abs(cl-1)C)r^beta+(VD+WC)r^(alpha+beta-1).',
                'Integrate each positive cross term in dlog(r), multiply angular interval pi/2, and divide by pi*a_ref^2.'
            ],
            'per_mode_contributions': contributions}
