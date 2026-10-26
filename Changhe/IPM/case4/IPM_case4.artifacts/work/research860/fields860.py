"""Stateless physical fields and residual for the 860 T1 representation (independent evaluator, SPEC v9 / v9.1 / v9.2).

Direct analytic evaluation for r > 0.02 through basis860.generator_block (own longdouble route for all 860 generators: exact exponent
differences, falling-factorial radial jets, frozen polynomial helpers); order-48 Decimal Taylor polynomials for r <= 0.02.
Residual R_f (longdouble assembly, rounded to binary64 once): r <= 0.02 Decimal series evaluated in longdouble; 0.02 < r < r_s (= 1)
w_x f_x + w_y f_y + q f with the center-subtracted q = sum_i c_i (ratio_i - s_i); r >= r_s the stable linear transport
sum_i a_i [-j_i (cl-1) f_i + 2 cl frem_i] plus the nonlinear part. Derivative columns [cl, a_1..a_59, c_0..c_799] are binary64, formed
from the rounded generator values with the same split (direct form with rounded w_x, w_y, q inside r_s; stable L_i columns outside).
Independent of the cached production provider in blocking and assembly code; both are gated against the >= 85-digit evaluator.
"""
import numpy as np
import basis860 as B
from origin860 import field_series, residual_series, evaluate_series_ld, evaluate_series_columns, ORIGIN_ORDER, ORIGIN_RADIUS

KEYS = B.KEYS
LD = B.LD


def generator_matrices(cl, x, y, cl_derivative=False, remainder=False):
    """All 860 generator field matrices at points (stateless provider), rounded once to float64 from the longdouble block."""
    return {k: v.astype(float) for k, v in B.generator_block(cl, x, y, cl_derivative, remainder).items()}


def fields_direct(prepared, x, y, derivatives=False, block_size=2048, threads=1, want_remainder=False, dtype=float):
    """Analytic evaluation (no origin series). Field sums in longdouble; returned in `dtype` (float64 by default, rounded once;
    LD keeps the longdouble values for the residual assembly). 'q' is the center-subtracted sum. With want_remainder the dict also
    carries 'Lsum' (stable linear transport sum); with derivatives the binary64 column matrices (+ 'Lstable')."""
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float)); x = x.ravel(); y = y.ravel()
    cl = LD(prepared['cl']); coeff = prepared['coeff_ld']; c_ld = prepared['c_ld']; g_ld = np.asarray(prepared['g'], LD); dc0 = prepared['c0_derivative']
    coeff64 = np.r_[prepared['c'], prepared['g']]; cl64 = float(prepared['cl'])
    out = {key: np.empty(len(x), dtype) for key in KEYS+('q',)}
    if want_remainder: out['Lsum'] = np.empty(len(x), dtype)
    dout = {key: np.empty((len(x), B.NRAW)) for key in KEYS+('q',)} if derivatives else None
    if derivatives and want_remainder: dout['Lstable'] = np.empty((len(x), B.NRAW))
    def block(lo):
        hi = min(len(x), lo+block_size); xx = x[lo:hi]; yy = y[lo:hi]
        blk = B.generator_block(cl, xx, yy, derivatives, want_remainder)
        for key in KEYS:
            out[key][lo:hi] = blk[key]@coeff
            if derivatives:
                mat = blk[key].astype(float); col0 = mat[:, 0].copy()
                mat[:, 0] = blk['d_'+key].astype(float)@coeff64+col0*dc0[0]; mat[:, 1:B.NLOW] += col0[:, None]*dc0[None, 1:B.NLOW]
                dout[key][lo:hi] = mat
        out['q'][lo:hi] = blk['qcore']@c_ld+blk['ratio'][:, B.NLOW:]@g_ld
        if derivatives: dout['q'][lo:hi] = dout['ratio'][lo:hi]; dout['q'][lo:hi, 0] += 1
        if want_remainder:
            out['Lsum'][lo:hi] = -(cl-1)*(blk['f']@(B.JCOL_LD*coeff))+2*cl*(blk['frem']@coeff)
            if derivatives:
                f64 = blk['f'].astype(float); frem64 = blk['frem'].astype(float)
                Lmat = -(cl64-1)*B.JCOL[None, :]*f64+2*cl64*frem64; ls = Lmat.copy(); ls[:, 1:B.NLOW] += Lmat[:, :1]*dc0[None, 1:B.NLOW]
                ls[:, 0] = (-B.JCOL[None, :]*f64-(cl64-1)*B.JCOL[None, :]*blk['d_f'].astype(float)+2*frem64+2*cl64*blk['d_frem'].astype(float))@coeff64+Lmat[:, 0]*dc0[0]
                dout['Lstable'][lo:hi] = ls
        return hi
    starts = list(range(0, len(x), block_size))
    if threads > 1 and len(starts) > 1:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=threads) as pool: list(pool.map(block, starts))
    else:
        for lo in starts: block(lo)
    return (out, dout) if derivatives else out


def fields(prepared, x, y, derivatives=False, block_size=2048, threads=1):
    """Fields at points (float64; longdouble sums rounded once; origin disk from the Decimal series evaluated in longdouble)."""
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float)); x = x.ravel(); y = y.ravel()
    small = np.hypot(x, y) <= ORIGIN_RADIUS; large = ~small
    out = {key: np.empty(len(x)) for key in KEYS+('q',)}
    dout = {key: np.empty((len(x), B.NRAW)) for key in out} if derivatives else None
    if np.any(large):
        value = fields_direct(prepared, x[large], y[large], derivatives, block_size, threads=threads)
        ff, df = value if derivatives else (value, None)
        for key in out:
            out[key][large] = ff[key]
            if derivatives: dout[key][large] = df[key]
    if np.any(small):
        series = field_series(prepared, order=ORIGIN_ORDER, derivatives=derivatives)
        for key in out:
            out[key][small] = evaluate_series_ld(series['fields'][key], x[small], y[small]).astype(float)
            if derivatives:
                dout[key][small] = evaluate_series_columns(series['derivatives'][key], x[small], y[small])
    return (out, dout) if derivatives else out


def _residual_chunk(args):
    prepared, x, y, block_size = args
    return residual(prepared, x, y, False, block_size, threads=1, procs=1)


def residual_parallel(prepared, x, y, block_size=4096, procs=8):
    """Residual over many points with a fork-based process pool (bitwise identical to the serial evaluation: each point is
    computed by the same code; chunks are disjoint). The origin-series cache is populated in the parent before forking."""
    import multiprocessing as mp
    x = np.asarray(x, float).ravel(); y = np.asarray(y, float).ravel()
    if np.any(np.hypot(x, y) <= ORIGIN_RADIUS): residual_series(prepared, order=ORIGIN_ORDER, derivatives=False)     # warm the Decimal cache once
    n = len(x); procs = max(1, min(int(procs), n))
    if procs == 1: return residual(prepared, x, y, False, block_size, threads=1, procs=1)
    chunk = -(-n//(procs*2)); chunk = max(block_size, -(-chunk//block_size)*block_size)
    pieces = [(prepared, x[lo:lo+chunk], y[lo:lo+chunk], block_size) for lo in range(0, n, chunk)]
    ctx = mp.get_context('fork')
    with ctx.Pool(procs) as pool: parts = pool.map(_residual_chunk, pieces)
    return np.concatenate(parts)


def residual(prepared, x, y, derivatives=False, block_size=2048, threads=1, procs=1):
    """R_f at points (binary64, assembled in longdouble); optionally the binary64 raw derivative columns."""
    if procs > 1 and not derivatives: return residual_parallel(prepared, x, y, block_size, procs)
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float)); x = x.ravel(); y = y.ravel(); cl = LD(prepared['cl']); cl64 = float(prepared['cl'])
    r = np.hypot(x, y); small = r <= ORIGIN_RADIUS; large = ~small
    rf = np.empty(len(x)); dr = np.empty((len(x), B.NRAW)) if derivatives else None
    if np.any(large):
        xl, yl = x[large], y[large]; stable = r[large] >= B.R_SWITCH
        value = fields_direct(prepared, xl, yl, derivatives, block_size, threads=threads, want_remainder=True, dtype=LD)
        ff, df = value if derivatives else (value, None)
        xld = np.asarray(xl, LD); yld = np.asarray(yl, LD)
        wx = cl*xld-ff['psiy']; wy = cl*yld+ff['psix']
        val = wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f']
        val[stable] = (ff['Lsum']-ff['psiy']*ff['fx']+ff['psix']*ff['fy']+ff['ratio']*ff['f'])[stable]
        rf[large] = val.astype(float)
        if derivatives:
            f64 = {k: ff[k].astype(float) for k in ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio', 'q')}; wx64 = cl64*xl-f64['psiy']; wy64 = cl64*yl+f64['psix']
            d = -f64['fx'][:, None]*df['psiy']+f64['fy'][:, None]*df['psix']+f64['f'][:, None]*df['ratio']
            lin = wx64[:, None]*df['fx']+wy64[:, None]*df['fy']+f64['q'][:, None]*df['f']; lin[:, 0] += xl*f64['fx']+yl*f64['fy']+f64['f']
            lin[stable] = (-f64['psiy'][:, None]*df['fx']+f64['psix'][:, None]*df['fy']+f64['ratio'][:, None]*df['f']+df['Lstable'])[stable]
            dr[large] = d+lin
    if np.any(small):
        series = residual_series(prepared, order=ORIGIN_ORDER, derivatives=derivatives, procs=procs if derivatives else 1)
        rf[small] = evaluate_series_ld(series['residual'], x[small], y[small]).astype(float)
        if derivatives:
            dr[small] = evaluate_series_columns(series['derivatives'], x[small], y[small])
    return (rf, dr) if derivatives else rf


def condition_sums(prepared, x, y, block_size=2048):
    """SPEC v9.3 section 11: S_R at points for the stateless provider (same definition as Model860.condition_sums); binary64 output."""
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float)); x = x.ravel(); y = y.ravel(); cl = LD(prepared['cl'])
    r = np.hypot(x, y); small = r <= ORIGIN_RADIUS; large = ~small; out = np.empty(len(x))
    ac = abs(prepared['coeff_ld']); acl = abs(prepared['c_ld']); ag = abs(np.asarray(prepared['g'], LD))
    if np.any(large):
        xl, yl = x[large], y[large]; stable = r[large] >= B.R_SWITCH; SR = np.empty(len(xl), LD)
        for lo in range(0, len(xl), block_size):
            hi = min(len(xl), lo+block_size); blk = B.generator_block(cl, xl[lo:hi], yl[lo:hi], False, True)
            S = {k: abs(blk[k])@ac for k in ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio')}; Sq = abs(blk['qcore'])@acl+abs(blk['ratio'][:, B.NLOW:])@ag
            xx = abs(np.asarray(xl[lo:hi], LD)); yy = abs(np.asarray(yl[lo:hi], LD))
            v = (cl*xx+S['psiy'])*S['fx']+(cl*yy+S['psix'])*S['fy']+Sq*S['f']
            st = stable[lo:hi]
            if np.any(st):
                SL = abs(cl-1)*(abs(blk['f'][st])@(B.JCOL_LD*ac))+2*cl*(abs(blk['frem'][st])@ac); v[st] = SL+S['psiy'][st]*S['fx'][st]+S['psix'][st]*S['fy'][st]+S['ratio'][st]*S['f'][st]
            SR[lo:hi] = v
        out[large] = SR.astype(float)
    if np.any(small):
        series = residual_series(prepared, order=ORIGIN_ORDER, derivatives=False)
        out[small] = evaluate_series_ld({k: abs(v) for k, v in series['residual'].items()}, abs(x[small]), abs(y[small])).astype(float)
    return out


def exact_dilation_fields(prepared, x, y, factor):
    """Exact evaluation at X/L with the dilation scalings; never a basis refit."""
    factor = float(factor)
    if not factor > 0: raise ValueError('Positive dilation required')
    ff = fields(prepared, np.asarray(x)/factor, np.asarray(y)/factor)
    scales = {'f': 1., 'fx': 1/factor, 'fy': 1/factor, 'psi': factor*factor, 'psix': factor, 'psiy': factor, 'ratio': 1., 'q': 1.}
    return {k: v*scales[k] for k, v in ff.items()}
