"""Certified lower bound of lambda_min(M(X)) for r >= R from the far-field sector bounds (farfield_bounds.field_bound).
M11 = 2c_l+1 + DU11 + rho_y, M22 = 2c_l+1 + DU22, M12 = (DU12+DU21)/2 - rho_x/2;  lambda_min >= min(M11, M22) - |M12|.
Uses rho_y >= inf_theta(leading sector)*r^{gamma-1} - (subleading bounds) when that is positive, else the absolute bound."""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import numpy as np
from flint import arb, ctx
from farfield_bounds import sector_fields, field_bound, sup_trig, A

def inf_trig(T, M=20000):
    if os.environ.get('FARFIELD_ARB_GRID'):
        from farfield_bounds import inf_trig_arb
        return inf_trig_arb(T)
    """Rigorous lower bound of inf_theta T(theta) (signed): grid min minus rounding margin minus Bernstein correction."""
    deg = max(k for (_, k) in T); n = len(T)
    th = np.linspace(0, 2*math.pi, M, endpoint=False)
    vals = np.zeros(M); csum = 0.0
    for (kind, k), c in T.items():
        cf = float(c); csum += abs(cf)
        vals += cf*(np.sin(k*th) if kind == 's' else np.cos(k*th))
    margin = (2*n + 4)*2.0**-53*csum + deg*csum*2.0**-50 + sum(abs(float(c) - c) if not isinstance(c, arb) else float(c.rad()) for c in T.values())
    gmin = arb(float(vals.min())) - arb(margin)
    sup = sup_trig(T, M)
    spacing = 2*arb.pi()/M*(1 + arb(2)**-40)
    return gmin - spacing/2*deg*sup

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    ctx.prec = 128
    Q = 6
    sectors, p = sector_fields(cl, a, Q)
    g = Fr(1)/cl; e1 = g - 1
    CL = A(cl)
    out = {}
    for R in [float(x) for x in sys.argv[2:]]:
        B = {}
        for name in ['rho_x', 'rho_y', 'DU11', 'DU12', 'DU21', 'DU22']:
            B[name], rows, tail = field_bound(sectors, p, cl, a, name, R, e1, Q)
        # rho_y lower bound: leading sector (0,0) inf minus the rest
        e00, T00 = sectors[(0, 0)]['rho_y']
        inf00 = inf_trig(T00)
        rest = arb(0)
        for (j, q), fields in sectors.items():
            if (j, q) == (0, 0): continue
            e, T = fields['rho_y']; rest += sup_trig(T)*arb(R)**A(e - e1)
        # tail part of rho_y: B['rho_y'] includes all sectors + tail; tail alone = B - sum of sector sups; recompute tail via field_bound rows
        Bfull, rows, tail = field_bound(sectors, p, cl, a, 'rho_y', R, e1, Q)
        rho_y_lo_coef = inf00 - rest - arb(tail)          # rho_y >= rho_y_lo_coef * r^{gamma-1} for r >= R (if coef > 0 it stays positive)
        rR = arb(R)**A(e1)
        # uniform bounds for all r >= R: each perturbation is (coefficient) r^(gamma-1), decreasing in r. M22 >= 2c_l+1 - |DU22|_c r^(gamma-1) >= value at R.
        # M11 >= 2c_l+1 + (rho_y_lo_coef - |DU11|_c) r^(gamma-1): if the coefficient is >= 0 the infimum over r >= R is the limit 2c_l+1, else the value at R.
        M22_lo = 2*CL + 1 - B['DU22']*rR
        coef11 = (rho_y_lo_coef if rho_y_lo_coef > 0 else -B['rho_y']) - B['DU11']
        M11_lo = 2*CL + 1 + (coef11*rR if coef11 < 0 else arb(0))
        M12_hi = (B['DU12'] + B['DU21'] + B['rho_x'])/2*rR
        # lambda_min >= min(M11, M22) - |M12| pointwise; the right side as a function of r >= R is >= its value with the uniform bounds above
        lam_lo = (M11_lo if M11_lo < M22_lo else M22_lo) - M12_hi
        print('r >= %g: rho_y >= %.4g r^(gamma-1) [inf of leading sector %.4g]; |DU22| <= %.4g r^(gamma-1); M22 >= %.5f, M11 >= %.5f, |M12| <= %.5f  =>  lambda_min(M) >= %.5f for all r >= %g' % (R, float(rho_y_lo_coef), float(inf00), float(B['DU22']), float(M22_lo.lower()), float(M11_lo.lower()), float(M12_hi.upper()), float(lam_lo.lower()), R))
        out[str(R)] = {'lambda_min_lower_bound': float(lam_lo.lower()), 'rho_y_coef_lower': float(rho_y_lo_coef), 'bounds_coef_r^(gamma-1)': {k: float(v) for k, v in B.items()}, 'Q': Q}
    json.dump(out, open(os.environ.get('FARFIELD_M_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'farfield_M_cert_088.json')), 'w'), indent=1)
