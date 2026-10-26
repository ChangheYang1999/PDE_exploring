"""Own high-precision (Decimal) point evaluator for the 860 T1 representation with the frozen N_n on both sides.

Point-centered Cartesian Taylor jets (frozen generic Jet class from basis_tests) of chi = sum_low a H_m q^(k-m) R^(p_j-k)
+ sum_high c H_m R^(p_j-m) t^v N_n P_n(2t-1); fields from the jet coefficients, exactly as field_tests.independent_fields.
The frozen potential_jet (ideal sqrt(2n+1)) is deliberately not used.
"""
import math
from decimal import Decimal, localcontext
import basis860 as B
from basis_tests import Jet
D = Decimal


def _harmonic_jet(X, Y, q, m, order):
    if m == 0: return Jet.constant(1, order)
    Hprev = Jet.constant(1, order); H = X
    for _ in range(1, 2*m): Hprev, H = H, 2*X*H-q*Hprev
    return H


def _legendre_jet(n, z, order):
    p0 = Jet.constant(1, order)
    if n == 0: return p0
    p1 = z
    for k in range(1, n): p0, p1 = p1, ((2*k+1)*z*p1-k*p0)/(k+1)
    return p1


def generator_jet(kind, triple, cl, X, Y, q, R, logR, t, order, cl_derivative=False):
    """Taylor jet (about the evaluation point) of one internal generator; optional cl derivative (p_j' log R chi)."""
    if kind == 'low':
        m, k, j = triple
        chi = _harmonic_jet(X, Y, q, m, order)*q.integer_power(k-m)*(logR*B.pdiff(cl, j, k)).exp(); dj = B.dp_cl(cl, j)      # exact exponent form (SPEC v9.1)
    else:
        m, n, j = triple; v = max(5-m, 0)
        chi = _harmonic_jet(X, Y, q, m, order)*(logR*B.pdiff(cl, j, m)).exp()*t.integer_power(v)*_legendre_jet(n, 2*t-1, order)*B.NN_DECIMAL[n]; dj = B.dp_cl(cl, j)
    return chi*logR*dj if cl_derivative else chi


def fields_from_jet(chi, L, xx, yy):
    rho = -(chi.derivative(2, 1)+chi.derivative(0, 3)); rhox = -(chi.derivative(3, 1)+chi.derivative(1, 3)); rhoy = -(chi.derivative(2, 2)+chi.derivative(0, 4))
    if yy:
        f = rho/yy; fx = rhox/yy; fy = rhoy/yy-rho/(yy*yy); ratio = chi.derivative(2, 1)/yy
    else:
        f = -(chi.derivative(2, 2)+chi.derivative(0, 4)); fx = -(chi.derivative(3, 2)+chi.derivative(1, 4)); fy = D(0); ratio = chi.derivative(2, 2)
    return {'f': f, 'fx': fx, 'fy': fy, 'psi': chi.derivative(1, 1), 'psix': chi.derivative(2, 1), 'psiy': chi.derivative(1, 2), 'ratio': ratio, 'chi': chi.derivative(0, 0)}


def point_setup(cl, x, y, order=5):
    L = D.from_float(float(cl)) if not isinstance(cl, Decimal) else cl
    xx = D.from_float(float(x)) if not isinstance(x, Decimal) else x; yy = D.from_float(float(y)) if not isinstance(y, Decimal) else y
    X = Jet({(0, 0): xx, (1, 0): 1}, order); Y = Jet({(0, 0): yy, (0, 1): 1}, order); q = X*X+Y*Y; R = 1+q; logR = R.log(); t = q/R
    return L, xx, yy, X, Y, q, R, logR, t


def independent_fields(prepared, x, y, precision=85, cl_derivative=False, as_decimal=False):
    """f, f_x, f_y, psi, psi_x, psi_y, psi_x/y, q, R_f at one point (floats) from an 85-digit point-centered Taylor jet.
    With cl_derivative=True also returns the total d/dcl of every field (fixed internal coefficients + analytic a_000 chain).
    as_decimal=True returns the Decimal values themselves (SPEC v9: references without binary64 intermediates)."""
    with localcontext() as ctx:
        ctx.prec = precision
        L, xx, yy, X, Y, q, R, logR, t = point_setup(prepared['cl'], x, y, 5)
        chi = Jet.constant(0, 5); dchi = Jet.constant(0, 5)
        for coef, tr in zip(prepared['center']['coefficients_decimal'], B.LOW):
            cv = D(coef)
            if not cv: continue
            chi = chi+generator_jet('low', tr, L, X, Y, q, R, logR, t, 5)*cv
            if cl_derivative: dchi = dchi+generator_jet('low', tr, L, X, Y, q, R, logR, t, 5, True)*cv
        for coef, tr in zip(prepared['g'], B.HIGH):
            if coef:
                cv = D.from_float(float(coef))
                chi = chi+generator_jet('high', tr, L, X, Y, q, R, logR, t, 5)*cv
                if cl_derivative: dchi = dchi+generator_jet('high', tr, L, X, Y, q, R, logR, t, 5, True)*cv
        if cl_derivative:   # a_000 chain: d a_000/dcl times the a_000 generator
            dchi = dchi+generator_jet('low', B.LOW[0], L, X, Y, q, R, logR, t, 5)*D(prepared['center']['c0_cl_decimal'])
        ff = fields_from_jet(chi, L, xx, yy)
        ff['q'] = L-1+ff['ratio']
        ff['Rf'] = (L*xx-ff['psiy'])*ff['fx']+(L*yy+ff['psix'])*ff['fy']+ff['q']*ff['f']
        conv = (lambda v: v) if as_decimal else float
        out = {k: conv(v) for k, v in ff.items()}
        if cl_derivative:
            dff = fields_from_jet(dchi, L, xx, yy); dff['q'] = 1+dff['ratio']
            dff['Rf'] = (xx-dff['psiy'])*ff['fx']+(L*xx-ff['psiy'])*dff['fx']+(yy+dff['psix'])*ff['fy']+(L*yy+ff['psix'])*dff['fy']+dff['q']*ff['f']+ff['q']*dff['f']
            out['d_cl'] = {k: conv(v) for k, v in dff.items()}
        return out


def generator_fields(kind, triple, cl, x, y, precision=85, cl_derivative=False):
    """Fields of one generator at one point (Decimal values kept) for identity tests and Jacobian spot columns."""
    with localcontext() as ctx:
        ctx.prec = precision
        L, xx, yy, X, Y, q, R, logR, t = point_setup(cl, x, y, 5)
        chi = generator_jet(kind, triple, L, X, Y, q, R, logR, t, 5, cl_derivative)
        return fields_from_jet(chi, L, xx, yy)


def monomial_fields(m, k, j, cl, x, y, precision=85):
    """Fields of the specified monomial generator chi_{mkj} = H_m q^(k-m) R^(p_j-k) at one point (for T0 identities)."""
    with localcontext() as ctx:
        ctx.prec = precision
        L, xx, yy, X, Y, q, R, logR, t = point_setup(cl, x, y, 5); p, _ = B.p_exponents(L)
        chi = _harmonic_jet(X, Y, q, m, 5)*q.integer_power(k-m)*(logR*(p[j]-k)).exp()
        return fields_from_jet(chi, L, xx, yy)


def old_generator_fields(m, s, cl, x, y, precision=85):
    """Fields of an old core generator H_m R^(A-m-sigma_s) at one point (old source form)."""
    with localcontext() as ctx:
        ctx.prec = precision
        L, xx, yy, X, Y, q, R, logR, t = point_setup(cl, x, y, 5); gamma = 1/L; delta = (1-gamma)/2; A = (3+gamma)/2
        sigma = [D(0), D(1), D(2), delta, 2*delta, 3*delta][s]
        chi = _harmonic_jet(X, Y, q, m, 5)*(logR*(A-m-sigma)).exp()
        return fields_from_jet(chi, L, xx, yy)


def old_global_fields(m, n, cl, x, y, precision=85):
    """Fields of an old Global generator H_m R^(A-m) t^max(5-m,0) N_n P_n(2t-1) with the frozen N_n (old source form)."""
    return generator_fields('high', (m, n, 0), cl, x, y, precision)


def point_reference(prepared, x, y, digits=85, columns=True):
    """SPEC v9 gated reference at one point: R_f and the 860 center-eliminated raw Jacobian columns from the >= 85-digit evaluator with
    no binary64 intermediate other than the exact binary64 inputs: the background fields stay Decimal (independent_fields as_decimal)
    and the center-elimination factor -s_i/s_0 is formed from Decimal strains at the exact binary64 cl.  Values are rounded once."""
    import numpy as np
    cl = prepared['cl']
    with localcontext() as ctx:
        ctx.prec = digits
        tot = independent_fields(prepared, x, y, digits, cl_derivative=columns, as_decimal=True)
        L = D.from_float(float(cl)); xx = D.from_float(float(x)); yy = D.from_float(float(y))
        out = {'Rf': float(tot['Rf']), 'Rf_decimal': tot['Rf'], 'fields_decimal': {k: v for k, v in tot.items() if k != 'd_cl'}}
        if not columns: return out
        wx = L*xx-tot['psiy']; wy = L*yy+tot['psix']; q = tot['q']; f = tot['f']; fx = tot['fx']; fy = tot['fy']
        s, _ = B.strain_values(L)
        def column(gf): return wx*gf['fx']+wy*gf['fy']+q*gf['f']-fx*gf['psiy']+fy*gf['psix']+f*gf['ratio']
        g0 = generator_fields('low', B.LOW[0], cl, x, y, digits); col0 = column(g0); cols = np.empty(B.NRAW)
        cols[0] = float(tot['d_cl']['Rf'])
        for idx in range(1, B.NRAW):
            kind, tr = ('low', B.LOW[idx]) if idx < B.NLOW else ('high', B.HIGH[idx-B.NLOW]); gf = generator_fields(kind, tr, cl, x, y, digits)
            cols[idx] = float(column(gf)+((-s[idx]/s[0])*col0 if idx < B.NLOW else D(0)))
        out['columns'] = cols; out['d_cl_decimal'] = tot['d_cl']
        return out
