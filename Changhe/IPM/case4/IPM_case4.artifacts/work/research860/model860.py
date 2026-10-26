"""Extended-precision cached residual and binary64 Jacobian provider for the 860 T1 representation (production evaluator, SPEC v9 / v9.1).

Cache at one exact binary64 cl on the direct nodes (r > 0.02): six longdouble field matrices (N x 860: f, f_x, f_y, psi_x, psi_y,
psi_x/y), the longdouble center-subtracted low ratio block (N x 60), the longdouble stable-transport remainder f_rem (N x 860), and
their binary64 cl derivatives (for the Jacobian cl column).  All generator values come from basis860.generator_block (own longdouble
route with exact exponent differences and falling-factorial radial jets).
Residual (SPEC v9): field sums, q and R_f are formed in longdouble and rounded to binary64 once.
  r <= 0.02 (origin disk):     order-48 Decimal Taylor polynomial of R_f evaluated in longdouble (origin860.evaluate_series_ld);
  0.02 < r < r_s (= 1):        w_x f_x + w_y f_y + q f with q = sum_i c_i (ratio_i - s_i) (expm1 forms for the strained generators);
  r >= r_s:                    sum_i a_i [-j_i (cl-1) f_i + 2 cl frem_i] - psi_y f_x + psi_x f_y + ratio f   (stable linear transport).
Jacobian (binary64, SPEC v9 (c)): raw columns [cl, a_1..a_59, c_0..c_799] from the extended generator values rounded once, with
the rounded field multipliers (w_x, w_y, q inside r_s; stable L_i columns outside); origin columns from the Decimal series in binary64.
Residual vector r_i = sqrt(2 w_i/(pi a_ref^2)) R_f(X_i); J_mesh = r.r/2.
"""
import time
import numpy as np
from threadpoolctl import threadpool_limits
import basis860 as B
from absolute_common import A_REF
from absolute_model import FrozenLogMesh, array_hash
from origin860 import residual_series, evaluate_series_ld, evaluate_series_columns, ORIGIN_ORDER, ORIGIN_RADIUS

KEYS = ('f', 'fx', 'fy', 'psix', 'psiy', 'ratio')
LD = B.LD


def production_generator_matrices(cl, x, y, cl_derivative=True, remainder=True):
    """Exactly the generator values the cache stores for a point block (basis860.generator_block in longdouble), rounded once to
    float64 for comparisons: keys f, fx, fy, psi, psix, psiy, ratio, qcore [, d_<key>] [, frem, d_frem]."""
    return {k: v.astype(float) for k, v in B.generator_block(cl, x, y, cl_derivative, remainder).items()}


class Model860:
    version = 'model860_v6_T1_origin48_longdouble_assembly_centered_q_stableL_exact_exponents_v93'

    def __init__(self, mesh, a_ref=A_REF, block_size=4096, mode_block=64, workers=4, threads=1, shared_series_cache=None):
        if a_ref != A_REF: raise ValueError('a_ref must equal the fixed reference amplitude')
        self.shared_series_cache = shared_series_cache      # optional dict {(P bytes, g bytes): Decimal origin-series cache}; lets point tests reuse the series of identical coefficients (values unchanged)
        self.mesh = mesh; self.a_ref = float(a_ref); self.block_size = int(block_size); self.mode_block = int(mode_block)
        self.workers = int(workers); self.threads = int(threads)
        if self.workers < 1 or self.block_size < 1 or self.threads < 1: raise ValueError('positive workers/threads/block size required')
        self.root = np.sqrt(2*mesh.weights/(np.pi*self.a_ref**2)); self.root.setflags(write=False)
        self.x, self.y = mesh.coordinates(); r = np.hypot(self.x, self.y); self.small = r <= ORIGIN_RADIUS; self.direct = np.flatnonzero(~self.small)
        self.stable = (r[self.direct] >= B.R_SWITCH)            # within the direct index set: nodes using the stable linear form
        self.jcol = B.JCOL; self.jcol_ld = B.JCOL_LD
        self._cl = None; self._basis = None; self._dbasis = None; self._qcore = None; self._frem = None; self._dfrem = None
        self._key = None; self._prepared = None; self._fields = None; self._residual = None; self._jacobian = None
        self.fun_calls = self.jac_calls = 0; self.cache_builds = 0; self.cache_build_seconds = 0.; self.evaluation_cache_hits = 0
        self.jacobian_seconds = 0.; self.origin_series_seconds = 0.; self.assembly_seconds = 0.

    @property
    def physical_columns(self): return B.NRAW

    @property
    def estimated_basis_cache_bytes(self): return int(len(self.direct)*(16*(7*B.NRAW+B.NLOW)+8*7*B.NRAW))

    def cache_record(self):
        return {'version': self.version, 'workers': self.workers, 'cache_build_threads': self.threads, 'block_size': self.block_size, 'mode_block': self.mode_block,
                'cache_builds': self.cache_builds, 'cache_build_seconds': self.cache_build_seconds, 'basis_cache_bytes': self.estimated_basis_cache_bytes,
                'direct_nodes': int(len(self.direct)), 'Taylor_nodes': int(np.count_nonzero(self.small)), 'stable_linear_nodes': int(np.count_nonzero(self.stable)),
                'centered_direct_nodes': int(np.count_nonzero(~self.stable)), 'switch_radius': B.R_SWITCH,
                'origin_order': ORIGIN_ORDER, 'exact_cl_cache_key': True, 'cl_interpolation_used': False, 'all_raw_columns': B.NRAW, 'feasible_columns': B.NFEASIBLE_CLAIMED,
                'evaluation_cache_hits': self.evaluation_cache_hits, 'jacobian_seconds': self.jacobian_seconds, 'origin_series_seconds': self.origin_series_seconds, 'assembly_seconds': self.assembly_seconds,
                'generator_provider': 'basis860.generator_block (longdouble, all 860 generators; cache build in point blocks of block_size nodes)',
                'residual_assembly': {'arithmetic': 'longdouble field sums (one matrix-vector product per field over all direct nodes), longdouble products, one rounding to binary64',
                                      'chunking': 'cache build: blocks of %d nodes; residual: whole direct node set in one call per field; origin disk: longdouble evaluation of the order-%d Decimal polynomial; Jacobian origin columns: Decimal column polynomials formed in a fork pool of `workers` processes (bitwise identical to serial), evaluated in binary64' % (self.block_size, ORIGIN_ORDER),
                                      'forms': {'r_le_0.02': 'Decimal series (exact a_000) in longdouble', '0.02_lt_r_lt_r_s': 'centered q direct form', 'r_ge_r_s': 'stable linear transport'},
                                      'a_000': 'analytic Decimal value carried to the 64-bit significand (prepare: c_ld)'},
                'jacobian_columns': 'binary64 from rounded longdouble generator values and rounded field multipliers', 'extended_arithmetic': B.extended_arithmetic_statement(), 'mesh_sha256': self.mesh.fingerprint}

    def _ensure_basis(self, cl):
        if self._cl == cl and self._basis is not None: return
        began = time.perf_counter(); n = len(self.direct)
        if self._basis is None:
            self._basis = {key: np.empty((n, B.NRAW), LD) for key in KEYS}; self._dbasis = {key: np.empty((n, B.NRAW)) for key in KEYS}
            self._qcore = np.empty((n, B.NLOW), LD); self._frem = np.empty((n, B.NRAW), LD); self._dfrem = np.empty((n, B.NRAW))
        self._cl = None
        def fill(lo):
            hi = min(lo+self.block_size, n); ii = self.direct[lo:hi]
            blk = B.generator_block(cl, self.x[ii], self.y[ii], True, True)
            for key in KEYS: self._basis[key][lo:hi] = blk[key]; self._dbasis[key][lo:hi] = blk['d_'+key]
            self._qcore[lo:hi] = blk['qcore']; self._frem[lo:hi] = blk['frem']; self._dfrem[lo:hi] = blk['d_frem']
            return hi-lo
        starts = list(range(0, n, self.block_size))
        if self.threads > 1:
            from concurrent.futures import ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=self.threads) as pool: list(pool.map(fill, starts))
        else:
            for lo in starts: fill(lo)
        self._cl = cl; self.cache_builds += 1; self.cache_build_seconds += time.perf_counter()-began

    def _arguments(self, P, g):
        P = np.asarray(P, float); g = np.asarray(g, float)
        if P.shape != (B.NLOW,) or g.shape != (B.NHIGH,): raise ValueError('Expected 60 raw chart parameters and 800 high coefficients')
        if not np.all(np.isfinite(P)) or not np.all(np.isfinite(g)) or P[0] <= 1: raise ValueError('Finite parameters with cl>1 required')
        return P, g, (P.tobytes(), g.tobytes())

    def _assemble_residual(self, P, g):
        """Longdouble field sums and R_f on the direct nodes; returns (R_f float64 on direct nodes, longdouble fields dict incl. q)."""
        prepared = self._prepared; cl = LD(P[0]); coeff = prepared['coeff_ld']; c_ld = prepared['c_ld']; g_ld = np.asarray(g, LD)
        ff = {k: mat@coeff for k, mat in self._basis.items()}
        ff['q'] = self._qcore@c_ld+self._basis['ratio'][:, B.NLOW:]@g_ld
        xx = np.asarray(self.x[self.direct], LD); yy = np.asarray(self.y[self.direct], LD)
        wx = cl*xx-ff['psiy']; wy = cl*yy+ff['psix']
        rr = wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f']
        if np.any(self.stable):
            st = self.stable
            Lsum = -(cl-1)*(self._basis['f'][st]@(self.jcol_ld*coeff))+2*cl*(self._frem[st]@coeff)
            rr[st] = Lsum-ff['psiy'][st]*ff['fx'][st]+ff['psix'][st]*ff['fy'][st]+ff['ratio'][st]*ff['f'][st]
        return rr.astype(float), ff

    def _evaluate(self, P, g, key, derivatives):
        if key == self._key and (not derivatives or self._jacobian is not None):
            self.evaluation_cache_hits += 1; return self._residual, self._jacobian
        if key != self._key:
            self._key = None; self._jacobian = None
            self._prepared = B.prepare(P[0], P[1:], g); self._ensure_basis(float(P[0]))
            if self.shared_series_cache is not None: self._prepared['_taylor_cache'] = self.shared_series_cache.setdefault(key, {})
            t0 = time.perf_counter(); rr_direct, ff = self._assemble_residual(P, g); self.assembly_seconds += time.perf_counter()-t0
            rr = np.empty(self.mesh.size); rr[self.direct] = rr_direct
            if np.any(self.small):
                t0 = time.perf_counter(); series = residual_series(self._prepared, order=ORIGIN_ORDER, derivatives=False)
                rr[self.small] = evaluate_series_ld(series['residual'], self.x[self.small], self.y[self.small]).astype(float); self.origin_series_seconds += time.perf_counter()-t0
            self._residual = self.root*rr; self._fields = {k: v.astype(float) for k, v in ff.items()}; self._key = key
        if derivatives and self._jacobian is None:
            t0 = time.perf_counter(); prepared = self._prepared; cl = float(P[0]); coeff = np.r_[prepared['c'], g]; ff = self._fields; dc0 = prepared['c0_derivative']
            xx, yy = self.x[self.direct], self.y[self.direct]; wx = cl*xx-ff['psiy']; wy = cl*yy+ff['psix']; st = self.stable; ns = ~st
            result = np.empty((self.mesh.size, B.NRAW))
            def chained(name):
                derivative = self._basis[name].astype(float); col0 = derivative[:, 0].copy()
                derivative[:, 0] = self._dbasis[name]@coeff+col0*dc0[0]
                derivative[:, 1:B.NLOW] += col0[:, None]*dc0[None, 1:B.NLOW]
                return derivative
            # common nonlinear part: - f_x psi_y,i + f_y psi_x,i + f ratio_i   (ratio_i = d(psi_x/y)/d a_i, chained)
            res = -ff['fx'][:, None]*chained('psiy'); res += ff['fy'][:, None]*chained('psix'); res += ff['f'][:, None]*chained('ratio')
            cfx = chained('fx'); cfy = chained('fy'); cf = chained('f')
            # inside r_s: w_x f_x,i + w_y f_y,i + q f_i  (+ cl column: x f_x + y f_y + f)
            res[ns] += wx[ns, None]*cfx[ns]+wy[ns, None]*cfy[ns]+ff['q'][ns, None]*cf[ns]
            res[ns, 0] += xx[ns]*ff['fx'][ns]+yy[ns]*ff['fy'][ns]+ff['f'][ns]
            # r >= r_s: nonlinear transport products + stable linear columns L_i = -j(cl-1) f_i + 2 cl frem_i with the a_000 chain; cl column = d/dcl of sum a_i L_i
            if np.any(st):
                res[st] += -ff['psiy'][st, None]*cfx[st]+ff['psix'][st, None]*cfy[st]+ff['ratio'][st, None]*cf[st]
                f64 = self._basis['f'][st].astype(float); frem64 = self._frem[st].astype(float)
                Lmat = -(cl-1)*self.jcol[None, :]*f64+2*cl*frem64; lin = Lmat.copy()
                lin[:, 1:B.NLOW] += Lmat[:, :1]*dc0[None, 1:B.NLOW]
                dL_fixed = -self.jcol[None, :]*f64-(cl-1)*self.jcol[None, :]*self._dbasis['f'][st]+2*frem64+2*cl*self._dfrem[st]
                lin[:, 0] = dL_fixed@coeff+Lmat[:, 0]*dc0[0]
                res[st] += lin; del f64, frem64, Lmat, lin, dL_fixed
            del cfx, cfy, cf
            result[self.direct] = res; del res
            if np.any(self.small):
                t1 = time.perf_counter(); series = residual_series(prepared, order=ORIGIN_ORDER, derivatives=True, procs=self.workers)
                result[self.small] = evaluate_series_columns(series['derivatives'], self.x[self.small], self.y[self.small])
                self.origin_series_seconds += time.perf_counter()-t1
            result *= self.root[:, None]; self._jacobian = result; self.jacobian_seconds += time.perf_counter()-t0
        if not np.all(np.isfinite(self._residual)) or (derivatives and not np.all(np.isfinite(self._jacobian))): raise ValueError('Nonfinite residual/Jacobian')
        return self._residual, self._jacobian

    def condition_sums(self, P, g):
        """SPEC v9.3 section 11: S_R(X_i) for the last evaluated point, R_f assembled with every field replaced by sum_i |c_i| |phi_i(X)| and every
        product in absolute value (centered q terms inside r_s, stable L_i terms outside; origin disk: the Decimal R_f polynomial with absolute
        coefficients at (|x|, |y|)).  Unweighted (multiply by root for the residual scale).  Binary64 output from longdouble sums."""
        P, g, key = self._arguments(P, g)
        if key != self._key: self._evaluate(P, g, key, False)
        prepared = self._prepared; cl = LD(P[0]); ac = abs(prepared['coeff_ld']); acl = abs(prepared['c_ld']); ag = abs(np.asarray(g, LD))
        S = {k: abs(mat)@ac for k, mat in self._basis.items()}
        Sq = abs(self._qcore)@acl+abs(self._basis['ratio'][:, B.NLOW:])@ag
        xx = abs(np.asarray(self.x[self.direct], LD)); yy = abs(np.asarray(self.y[self.direct], LD))
        SR = (cl*xx+S['psiy'])*S['fx']+(cl*yy+S['psix'])*S['fy']+Sq*S['f']
        if np.any(self.stable):
            st = self.stable; SL = abs(cl-1)*(abs(self._basis['f'][st])@(self.jcol_ld*ac))+2*cl*(abs(self._frem[st])@ac)
            SR[st] = SL+S['psiy'][st]*S['fx'][st]+S['psix'][st]*S['fy'][st]+S['ratio'][st]*S['f'][st]
        out = np.empty(self.mesh.size); out[self.direct] = SR.astype(float)
        if np.any(self.small):
            series = residual_series(prepared, order=ORIGIN_ORDER, derivatives=False)
            out[self.small] = evaluate_series_ld({k: abs(v) for k, v in series['residual'].items()}, abs(self.x[self.small]), abs(self.y[self.small])).astype(float)
        return out

    def fun(self, P, g):
        self.fun_calls += 1; P, g, key = self._arguments(P, g)
        with threadpool_limits(limits=self.workers, user_api='blas'): value, _ = self._evaluate(P, g, key, False)
        return value.copy()

    def jacobian(self, P, g):
        self.jac_calls += 1; P, g, key = self._arguments(P, g)
        with threadpool_limits(limits=self.workers, user_api='blas'): _, value = self._evaluate(P, g, key, True)
        return value.copy()

    def clear_cache(self):
        self._cl = None; self._basis = None; self._dbasis = None; self._qcore = None; self._frem = None; self._dfrem = None
        self._key = None; self._prepared = None; self._fields = None; self._residual = None; self._jacobian = None


def feasible_matrix(J, chart, column_scales=None):
    """A = [J_low @ T_55, J_high] * diag(scales); scales default to inverse initial column norms (all 855 retained)."""
    reduced = np.column_stack((J[:, :B.NLOW]@chart.base_tangent, J[:, B.NLOW:]))
    norms = np.linalg.norm(reduced, axis=0)
    if len(norms) != B.NFEASIBLE_CLAIMED or not np.all(np.isfinite(norms)) or np.any(norms <= 0): raise ValueError('zero/nonfinite feasible column requires diagnosis')
    scales = 1/norms if column_scales is None else np.asarray(column_scales, float)
    if scales.shape != norms.shape or np.any(scales <= 0) or not np.all(np.isfinite(scales)): raise ValueError('complete positive scales required')
    return reduced*scales, scales
