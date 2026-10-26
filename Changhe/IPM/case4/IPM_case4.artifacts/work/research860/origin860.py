"""Own Decimal Cartesian Taylor algebra at the origin for the 860 T1 representation (frozen N_n, SPEC v5).

Potential polynomials are built here (not with highprecision_origin.potential_polynomial, whose Global branch uses the
ideal sqrt(2n+1)); the generic polynomial algebra (add, mul, _fields, evaluate_series, _binomial) of the frozen module is
reused. Production truncation order 48 at r <= 0.02; orders 48/56 for the integrator's disk diagnostics and the section 13 monitor (SPEC v9.3). Precision 90 by default.
"""
import math
from decimal import Decimal, localcontext
import numpy as np
import basis860 as B
from highprecision_origin import _fields, add, mul, evaluate_series, _binomial, D

LD = np.longdouble


def evaluate_series_columns(polys, x, y):
    """Binary64 evaluation of many Decimal-coefficient polynomials at the same points, vectorized over the polynomials: terms are
    accumulated as (float(v) * x**i) * y**j in a fixed order (total degree descending, then x-degree descending), the same operation
    sequence per element as the frozen highprecision_origin.evaluate_series except for the order of the monomials of equal degree (the frozen
    loop uses each polynomial's dict order).  Deterministic, no BLAS, independent of the thread count.  Returns (len(x), len(polys))."""
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float)); x = x.ravel(); y = y.ravel()
    keys = sorted({k for poly in polys for k in poly}, key=lambda k: (sum(k), k), reverse=True)
    out = np.zeros((len(x), len(polys)))
    coef = np.zeros((len(keys), len(polys)))
    for c, poly in enumerate(polys):
        for t, k in enumerate(keys):
            v = poly.get(k)
            if v is not None: coef[t, c] = float(v)
    # the frozen evaluator skips nothing: a polynomial without the monomial contributes 0*x^i*y^j = 0 exactly (x, y finite), so the shared key list is exact
    for t, (i, j) in enumerate(keys):
        xi = x**i; yj = y**j
        out += (coef[t][None, :]*xi[:, None])*yj[:, None]
    return out


def evaluate_series_ld(poly, x, y):
    """Evaluate a Decimal-coefficient polynomial {(i, j): v} at points in longdouble (SPEC v9: origin-disk R_f in extended arithmetic).
    Coefficients are converted once through 31 significant decimal digits (correctly rounded to the 64-bit significand by strtold);
    terms are summed from the highest total degree down, as the frozen binary64 evaluate_series does."""
    x = np.asarray(x, LD).ravel(); y = np.asarray(y, LD).ravel()
    if not poly: return np.zeros(len(x), LD)
    imax = max(i for (i, j) in poly); jmax = max(j for (i, j) in poly)
    xp = [np.ones(len(x), LD)]; yp = [np.ones(len(y), LD)]
    for _ in range(imax): xp.append(xp[-1]*x)
    for _ in range(jmax): yp.append(yp[-1]*y)
    out = np.zeros(len(x), LD)
    for (i, j), v in sorted(poly.items(), key=lambda kv: sum(kv[0]), reverse=True): out += LD(format(v, '.30e'))*xp[i]*yp[j]
    return out

KEYS = ('f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio', 'q')
ORIGIN_ORDER = 48      # SPEC v9.3: order 48 (potential order 52), certified uniformly for c_l in [51/50, 10] at 1e-41 (c4-ver research/basis860-origin-truncation); order 40 was certified only at four c_l values
ORIGIN_RADIUS = .02


def _series_H_q_R(m, Npow, b, db, order):
    """Polynomial (and its cl derivative) of H_m q^Npow (1+q)^b through total degree `order`; H_m = Re(x+iy)^(2m)."""
    out = {}; dout = {}
    nmax = (order-2*m-2*Npow)//2
    if nmax < 0: return out, dout
    radial, dradial = _binomial(b, db, nmax)
    for l in range(m+1):
        angular = D((-1)**l*math.comb(2*m, 2*l)); hx = 2*m-2*l; hy = 2*l
        for n, (v, dv) in enumerate(zip(radial, dradial)):
            N = n+Npow
            for qq in range(N+1):
                key = (hx+2*qq, hy+2*(N-qq)); fac = angular*math.comb(N, qq)
                out[key] = out.get(key, D(0))+fac*v; dout[key] = dout.get(key, D(0))+fac*dv
    return {k: v for k, v in out.items() if v}, {k: v for k, v in dout.items() if v}


def generator_polynomial(kind, triple, cl, order):
    """Potential polynomial and cl derivative of one internal generator through degree `order` (Decimal context active)."""
    if kind == 'low':
        m, k, j = triple
        return _series_H_q_R(m, k-m, B.pdiff(cl, j, k), B.dp_cl(cl, j), order)          # exponent p_j - k in exact form (SPEC v9.1)
    m, n, j = triple; v = max(5-m, 0); chi = {}; dchi = {}
    for h, L in enumerate(B.legendre_monomial(n)):
        c, dc = _series_H_q_R(m, v+h, B.pdiff(cl, j, m+v+h), B.dp_cl(cl, j), order)
        chi = add(chi, c, B.NN_DECIMAL[n]*L); dchi = add(dchi, dc, B.NN_DECIMAL[n]*L)
    return chi, dchi


def field_series(prepared, order=ORIGIN_ORDER, derivatives=False, precision=90):
    cache = prepared['_taylor_cache']; key = ('fields', order, derivatives, precision)
    if key in cache: return cache[key]
    with localcontext() as ctx:
        ctx.prec = precision
        cl = D.from_float(float(prepared['cl']))
        cc = [D(v) for v in prepared['center']['coefficients_decimal']]
        gg = [D.from_float(float(v)) for v in prepared['g']]
        low = []; lowcl = []
        for t in B.LOW:
            chi, dchi = generator_polynomial('low', t, cl, order+4); low.append(_fields(chi, order)); lowcl.append(_fields(dchi, order))
        high = []; highcl = []
        for t in B.HIGH:
            chi, dchi = generator_polynomial('high', t, cl, order+4); high.append(_fields(chi, order)); highcl.append(_fields(dchi, order))
        total = {k: {} for k in KEYS}; dt = {k: [] for k in KEYS} if derivatives else None
        for name in KEYS[:-1]:
            for c, v in zip(cc, low): total[name] = add(total[name], v[name], c, order)
            for c, v in zip(gg, high): total[name] = add(total[name], v[name], c, order)
            if derivatives:
                clpoly = {}
                for c, v in zip(cc, lowcl): clpoly = add(clpoly, v[name], c, order)
                for c, v in zip(gg, highcl): clpoly = add(clpoly, v[name], c, order)
                clpoly = add(clpoly, low[0][name], D(prepared['center']['c0_cl_decimal']), order)
                dt[name].append(clpoly)
                ss = [D(v) for v in prepared['center']['strain_decimal']]
                for k in range(1, B.NLOW): dt[name].append(add(low[k][name], low[0][name], -ss[k]/ss[0], order))
                dt[name].extend(v[name] for v in high)
        total['q'] = add(total['ratio'], {(0, 0): cl-1}, order=order); total['q'].pop((0, 0), None)   # exact analytic center
        if derivatives:
            dt['q'] = [dict(v) for v in dt['ratio']]
            dt['q'][0] = add(dt['q'][0], {(0, 0): D(1)}, order=order)
            for poly in dt['q']: poly.pop((0, 0), None)
        result = {'fields': total, 'derivatives': dt, 'order': order, 'precision': precision, 'normalization': 'frozen binary64 N_n'}
    cache[key] = result
    return result


_PAR = {}      # data shared with fork-pool workers (set in the parent before forking; copy-on-write)

def _column_products(ks):
    """Derivative-column residual polynomials for columns ks (worker of the fork pool; same Decimal operations and precision as the serial loop, so the
    result is bitwise identical to the serial evaluation and independent of the process count)."""
    with localcontext() as ctx:
        ctx.prec = _PAR['precision']; ff = _PAR['ff']; df = _PAR['df']; wx = _PAR['wx']; wy = _PAR['wy']; order = _PAR['order']; out = []
        for k in ks:
            z = add(mul(wx, df['fx'][k], order), mul(wy, df['fy'][k], order), order=order)
            z = add(z, mul(ff['q'], df['f'][k], order), order=order)
            z = add(z, mul(ff['fx'], df['psiy'][k], order), D(-1), order)
            z = add(z, mul(ff['fy'], df['psix'][k], order), order=order)
            z = add(z, mul(ff['f'], df['q'][k], order), order=order)
            if k == 0:
                z = add(z, mul({(1, 0): D(1)}, ff['fx'], order), order=order)
                z = add(z, mul({(0, 1): D(1)}, ff['fy'], order), order=order)
            out.append(z)
        return out


def residual_series(prepared, order=ORIGIN_ORDER, derivatives=False, precision=90, procs=1):
    """Decimal Taylor polynomial of R_f (and of its 860 raw derivative columns) about the origin. The derivative-column products may run in a
    fork process pool (procs > 1): each column is computed by the same code in the same Decimal context, so the polynomials are bitwise
    identical to the serial result (the cache key does not depend on procs)."""
    cache = prepared['_taylor_cache']; key = ('residual', order, derivatives, precision)
    if key in cache: return cache[key]
    with localcontext() as ctx:
        ctx.prec = precision
        data = field_series(prepared, order, derivatives, precision); ff = data['fields']; cl = D.from_float(float(prepared['cl']))
        wx = add({(1, 0): cl}, ff['psiy'], D(-1), order); wy = add({(0, 1): cl}, ff['psix'], order=order)
        rf = add(add(mul(wx, ff['fx'], order), mul(wy, ff['fy'], order), order=order), mul(ff['q'], ff['f'], order), order=order)
        dr = []
        if derivatives:
            df = data['derivatives']; procs = max(1, int(procs))
            _PAR.update(precision=precision, ff=ff, df=df, wx=wx, wy=wy, order=order)
            if procs > 1:
                import multiprocessing as mp
                chunks = [list(range(lo, min(B.NRAW, lo+8))) for lo in range(0, B.NRAW, 8)]
                with mp.get_context('fork').Pool(procs) as pool: parts = pool.map(_column_products, chunks)
                for part in parts: dr.extend(part)
            else: dr = _column_products(range(B.NRAW))
            _PAR.clear()
        result = {'residual': rf, 'derivatives': dr if derivatives else None, 'order': order, 'precision': precision,
                  'constant': str(rf.get((0, 0), D(0))),
                  'degree_l1_coefficients': {str(n): str(sum((abs(v) for k, v in rf.items() if sum(k) == n), D(0))) for n in range(order+1)}}
    cache[key] = result
    return result


def origin_diagnostics(prepared, radius=ORIGIN_RADIUS, a_ref=1., orders=(48, 56), precision=90):
    """Analytic dr/r dtheta disk integral of the squared residual polynomial (same formula as the frozen code)."""
    rows = []
    for order in orders:
        s = residual_series(prepared, order, False, precision); p = s['residual']
        constant = p.get((0, 0), D(0))
        if constant: integral = None; divergent = True
        else:
            integral = 0.; divergent = False
            for (i, j), v in p.items():
                for (k, l), w in p.items():
                    degree = i+j+k+l
                    if degree:
                        angular = .5*math.exp(math.lgamma((i+k+1)/2)+math.lgamma((j+l+1)/2)-math.lgamma((degree+2)/2))
                        integral += float(v)*float(w)*radius**degree/degree*angular/(math.pi*a_ref*a_ref)
        theta = np.linspace(0, math.pi/2, 129); rv = evaluate_series(p, radius*np.cos(theta), radius*np.sin(theta))
        bound = sum(float(abs(v))*radius**sum(k) for k, v in p.items())
        rows.append({'order': order, 'precision': precision, 'constant_residual_decimal': str(constant), 'divergent_at_origin': divergent,
                     'polynomial_origin_integral': integral, 'polynomial_boundary_sampled_max': float(np.max(abs(rv))),
                     'polynomial_boundary_coefficient_l1_bound': bound, 'degree_l1_coefficients': s['degree_l1_coefficients']})
    delta = None if any(r['polynomial_origin_integral'] is None for r in rows) else abs(rows[-1]['polynomial_origin_integral']-rows[-2]['polynomial_origin_integral'])
    return {'radius': radius, 'rows': rows, 'successive_order_integral_difference': delta, 'remainder_rigorous_bound': False}
