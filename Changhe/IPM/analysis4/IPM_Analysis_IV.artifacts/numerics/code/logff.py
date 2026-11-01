"""logff.py : logarithmic (polynomial in t = log r) far-field series at RATIONAL delta, ball arithmetic or exact.

rho = sum_n r^{p_n} f_n(t, theta), psi = sum_n r^{P_n} g_n(t, theta), with f_n = sum_q t^q f_{n,q}(theta) (odd sine series
columns, lists a[k]) and g_n = sum_q t^q g_{n,q}(theta) (even sine columns, lists b[j]). T = d/dt, D = d/theta.
Recursion (lead/verifier):  [(n-1)(c-1) - c T] f_n = S_n,  S_n = sum_{i+j=n} [ ((P_i + T) g_i) (D f_j) - (D g_i) ((p_j + T) f_j) ]
Poisson:  rhs_j = (1/2)[(p_n - 2j + 1 + T) a_{j-1} + (p_n + 2j + 1 + T) a_j],   [4j^2 - P_n^2 - 2 P_n T - T^2] b_j = rhs_j.
Off resonance: b_j = lam^{-1} sum_h ((2 P_n T + T^2)/lam)^h rhs_j (terminating).  At resonance (P_n = -2j, decided exactly):
T (4j - T) b_j = rhs_j  ->  b_j = beta_j + int_0^t (4j - T)^{-1} rhs_j, beta_j = 0 (free harmonic multipole set to zero).
Columns are coefficient lists in the ring of ffcore (fmpq exact or arb)."""
import sys, os, json, math, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
import ffcore
_arb_pack = ffcore._arb_pack; _arb_unpack = ffcore._arb_unpack
from flint import fmpq

def col_add(R, A, B):
    """add two column-lists (list over q of coefficient lists)"""
    Q = max(len(A), len(B)); out = []
    for q in range(Q):
        a = A[q] if q < len(A) else []; b = B[q] if q < len(B) else []
        L = max(len(a), len(b)); c = [R.zero] * L
        for k in range(len(a)): c[k] = c[k] + a[k]
        for k in range(len(b)): c[k] = c[k] + b[k]
        out.append(c)
    return out
def col_scale(R, A, s): return [[x * s for x in a] for a in A]
def col_T(R, A):
    """T = d/dt: (T A)_q = (q+1) A_{q+1}"""
    return [[x * (q + 1) for x in A[q + 1]] for q in range(len(A) - 1)] if len(A) > 1 else [[R.zero]]
def col_trim(R, A):
    A = [list(a) for a in A]
    for a in A:
        while len(a) > 1 and R.is_zero(a[-1]): a.pop()
    while len(A) > 1 and all(R.is_zero(x) for x in A[-1]): A.pop()
    return A
def poly_T_on_scalar_poly(R, v):
    """T on a t-polynomial given as list of scalars v[q]"""
    return [v[q + 1] * (q + 1) for q in range(len(v) - 1)] if len(v) > 1 else [R.zero]

class LogFarField:
    def __init__(self, ring, A, B, f1, beta_zero=True):
        """delta = A/B exactly; f1: list of odd-sine coefficients (ring scalars or strings)"""
        R = self.R = ring
        self.delta_exact = fmpq(A, B); self.c_exact = 1 / (1 - self.delta_exact)
        self.delta = R.scalar(self.delta_exact); self.c_l = R.scalar(self.c_exact)
        self.f = {1: [[R.scalar(x) for x in f1]]}      # order -> list over q of columns
        self.g = {}; self.stats = {}; self.resonances = {}
        self.g[1] = self.poisson(1); self._stats(1)
    def p(self, n): return 1 - n * self.delta
    def p_exact(self, n): return 1 - n * self.delta_exact
    def poisson(self, n):
        R = self.R; F = self.f[n]; Q = len(F); K = max(len(a) for a in F) - 1
        p = self.p(n); P = p + 1; Pex = self.p_exact(n) + 1
        # a_j(t) as t-polynomials per frequency index j: A[j][q]
        A = [[F[q][j] if j < len(F[q]) else R.zero for q in range(Q)] for j in range(K + 2)]
        B = [None] * (K + 2)
        res = []
        for j in range(1, K + 2):
            # rhs_j(t) = 1/2 [ (p - 2j + 1 + T) a_{j-1} + (p + 2j + 1 + T) a_j ]
            am = A[j - 1]; aj = A[j]
            Tam = poly_T_on_scalar_poly(R, am); Taj = poly_T_on_scalar_poly(R, aj)
            rhs = [R.zero] * Q
            for q in range(Q):
                v = (p - 2 * j + 1) * am[q] + (p + 2 * j + 1) * aj[q]
                if q < len(Tam): v = v + Tam[q]
                if q < len(Taj): v = v + Taj[q]
                rhs[q] = v / 2
            if all(R.is_zero(x) for x in rhs): B[j] = [R.zero]; continue
            lam_ex = 4 * j * j - Pex * Pex
            if lam_ex != 0:
                lam = 4 * j * j - P * P
                x = [v / lam for v in rhs]; term = list(x)
                for _ in range(Q + 1):
                    t1 = poly_T_on_scalar_poly(R, term); t2 = poly_T_on_scalar_poly(R, t1)
                    term = [R.zero] * len(x)
                    nz = False
                    for q in range(len(x)):
                        v = R.zero
                        if q < len(t1): v = v + 2 * P * t1[q]
                        if q < len(t2): v = v + t2[q]
                        term[q] = v / lam
                        if not R.is_zero(term[q]): nz = True
                    if not nz: break
                    x = [x[q] + term[q] for q in range(len(x))]
                B[j] = x
            else:
                # exact resonance P = -2j: T(4j - T) b = rhs ; w = (4j - T)^{-1} rhs = sum_h (T/(4j))^h rhs/(4j) ; b = int_0^t w
                w = [v / (4 * j) for v in rhs]; term = list(w)
                for _ in range(Q + 1):
                    t1 = poly_T_on_scalar_poly(R, term); term = [R.zero] * len(w); nz = False
                    for q in range(len(w)):
                        if q < len(t1): term[q] = t1[q] / (4 * j)
                        if not R.is_zero(term[q]): nz = True
                    if not nz: break
                    w = [w[q] + term[q] for q in range(len(w))]
                b = [R.zero] + [w[q] / (q + 1) for q in range(len(w))]     # beta_j = 0
                B[j] = b
                res.append({'j': j, 'forcing_t0': R.to_float(rhs[0]), 'forcing_cols': [R.to_float(v) for v in rhs]})
        if res: self.resonances[n] = res
        # back to columns: G[q][j]
        Qg = max(len(b) if b else 1 for b in B[1:]) if K + 1 >= 1 else 1
        G = [[R.zero] * (K + 2) for _ in range(Qg)]
        for j in range(1, K + 2):
            b = B[j] or [R.zero]
            for q in range(len(b)): G[q][j] = b[q]
        return col_trim(R, G)
    def step(self):
        R = self.R; n = max(self.f) + 1; t0 = time.time()
        acc = None
        edge = getattr(self, 'edge', None)
        for i in range(1, n):
            j = n - i
            if edge is not None and min(i, j) > edge: continue       # edge-only (linearized) recursion, lead request (s)
            Gi = self.g[i]; Fj = self.f[j]
            Pi = self.p(i) + 1; pj = self.p(j)
            Gt = col_add(R, col_scale(R, Gi, Pi), col_T(R, Gi))       # (P_i + T) g_i
            Ft = col_add(R, col_scale(R, Fj, pj), col_T(R, Fj))       # (p_j + T) f_j
            term = []
            for q1 in range(len(Gi)):
                for q2 in range(len(Fj)):
                    q = q1 + q2
                    P1, _ = self.products_wrap(Gt[q1] if q1 < len(Gt) else [R.zero], Fj[q2])    # ((P_i+T)g_i) * D f_j
                    _, P2 = self.products_wrap(Gi[q1], Ft[q2] if q2 < len(Ft) else [R.zero])    # (D g_i) * ((p_j+T) f_j)
                    col = [x - y for x, y in zip(P1 + [R.zero] * (len(P2) - len(P1)), P2 + [R.zero] * (len(P1) - len(P2)))]
                    while len(term) <= q: term.append([R.zero])
                    term[q] = col_add(R, [term[q]], [col])[0]
            acc = term if acc is None else col_add(R, acc, term)
        lam = (n - 1) * (self.c_l - 1)
        x = col_scale(R, acc, 1 / lam); term = x
        for _ in range(len(acc) + 1):
            term = col_scale(R, col_T(R, term), self.c_l / lam)
            if all(R.is_zero(v) for a in term for v in a): break
            x = col_add(R, x, term)
        self.f[n] = col_trim(R, x)
        self.g[n] = self.poisson(n)
        self._stats(n); self.stats[n]['time'] = time.time() - t0
        return n

    # ------------------------------------------------------------------ fast block products (Kronecker substitution)
    def _block_products(self, Gcols, Fcols, Gd_cols, Ft_cols):
        """Given column lists (over t-power q) of: Gt = (P_i+T) g_i (even-sine lists b[j]), F = f_j (odd-sine lists a[k]),
        Gd = g_i (for g_i'), Ft = (p_j+T) f_j, return the column list of  Gt * (F)' - (Gd)' * Ft  (odd-sine lists),
        using ONE polynomial multiplication per product type: columns are packed with stride S into a single polynomial."""
        R = self.R
        QG = max(len(Gcols), len(Gd_cols)); QF = max(len(Fcols), len(Ft_cols))
        J = max(max(len(b) for b in Gcols), max(len(b) for b in Gd_cols)) - 1
        K = max(max(len(a) for a in Fcols), max(len(a) for a in Ft_cols)) - 1
        S = J + K + 2                                     # stride: every block index stays below S
        def pack(cols, Q, L, weight=None, rev=False):
            coef = [R.zero] * (Q * S)
            for q in range(Q):
                col = cols[q] if q < len(cols) else []
                for idx in range(len(col)):
                    x = col[idx]
                    if weight is not None: x = x * weight(idx)
                    pos = (L - idx) if rev else idx        # reversal within the block, padded to length L+1
                    coef[q * S + pos] = coef[q * S + pos] + x
            return R.poly(coef)
        Bz = pack(Gcols, QG, J)                                             # sum_j b_j w^j         (g terms, for g f')
        Bd = pack(Gd_cols, QG, J, weight=lambda j: 2 * j)                   # 2j b_j                (g')
        Ad = pack(Fcols, QF, K, weight=lambda k: 2 * k + 1)                 # (2k+1) a_k            (f')
        Adrev = pack(Fcols, QF, K, weight=lambda k: 2 * k + 1, rev=True)
        Az = pack(Ft_cols, QF, K)                                           # (p_j + T) f_j
        Arev = pack(Ft_cols, QF, K, rev=True)
        Qout = QG + QF - 1; Mout = J + K
        S1 = R.coeffs(polymul(R, Bz, Ad), Qout * S); R1 = R.coeffs(polymul(R, Bz, Adrev), Qout * S)
        S2 = R.coeffs(polymul(R, Bd, Az), Qout * S); R2 = R.coeffs(polymul(R, Bd, Arev), Qout * S)
        out = []
        half = R.scalar(fmpq(1, 2)) if R.name != 'float' else 0.5
        for q in range(Qout):
            P1 = [R.zero] * (Mout + 1); P2 = [R.zero] * (Mout + 1); base = q * S
            for m in range(Mout + 1): P1[m] = P1[m] + S1[base + m]; P2[m] = P2[m] + S2[base + m]
            for idx in range(J + K + 1):
                t_ = idx - K
                if t_ >= 1: P1[t_ - 1] = P1[t_ - 1] + R1[base + idx]
                else: P1[-t_] = P1[-t_] - R1[base + idx]
                if t_ <= 0: P2[-t_] = P2[-t_] + R2[base + idx]
                else: P2[t_ - 1] = P2[t_ - 1] - R2[base + idx]
            out.append([(x - y) * half for x, y in zip(P1, P2)])
        return out

    def step_fast(self):
        R = self.R; n = max(self.f) + 1; t0 = time.time()
        acc = None
        edge = getattr(self, 'edge', None)
        for i in range(1, n):
            j = n - i
            if edge is not None and min(i, j) > edge: continue       # edge-only (linearized) recursion, lead request (s)
            Gi = self.g[i]; Fj = self.f[j]
            Pi = self.p(i) + 1; pj = self.p(j)
            Gt = col_add(R, col_scale(R, Gi, Pi), col_T(R, Gi))
            Ft = col_add(R, col_scale(R, Fj, pj), col_T(R, Fj))
            term = self._block_products(Gt, Fj, Gi, Ft)
            acc = term if acc is None else col_add(R, acc, term)
        lam = (n - 1) * (self.c_l - 1)
        x = col_scale(R, acc, 1 / lam); term = x
        for _ in range(len(acc) + 1):
            term = col_scale(R, col_T(R, term), self.c_l / lam)
            if all(R.is_zero(v) for a in term for v in a): break
            x = col_add(R, x, term)
        self.f[n] = col_trim(R, x)
        self.g[n] = self.poisson(n)
        self._stats(n); self.stats[n]['time'] = time.time() - t0
        return n


    # ------------------------------------------------------------------ fixed-stride cached products (fast2)
    def _ensure_stride(self, N):
        """fixed stride for a whole run: S = 2 K_N + 3 with K_N the largest odd-sine index at order N (bandwidth n(K_1+1)-1)"""
        if getattr(self, '_S', None) is None:
            K1 = len(self.f[1][0]) - 1
            KN = N * (K1 + 1) - 1
            self._L = KN + 1                      # reversal length (block position L - idx)
            self._S = 2 * KN + 3                  # block stride
            self._pk = {}                         # cache: ('g', i) -> (Bz_i for Gt, Bd_i) ; ('f', j) -> (Ad_j, Adrev_j, Az_j, Arev_j)
    def _pack(self, cols, weight=None, rev=False):
        R = self.R; S = self._S; L = self._L
        coef = [R.zero] * (len(cols) * S)
        for q, col in enumerate(cols):
            for idx, x in enumerate(col):
                if R.is_zero(x): continue
                if weight is not None: x = x * weight(idx)
                pos = (L - idx) if rev else idx
                coef[q * S + pos] = coef[q * S + pos] + x
        return R.poly(coef)
    def _packs_g(self, i):
        key = ('g', i)
        if key not in self._pk:
            R = self.R; Gi = self.g[i]; Pi = self.p(i) + 1
            Gt = col_add(R, col_scale(R, Gi, Pi), col_T(R, Gi))          # (P_i + T) g_i
            self._pk[key] = (self._pack(Gt), self._pack(Gi, weight=lambda j: 2 * j))
        return self._pk[key]
    def _packs_f(self, j):
        key = ('f', j)
        if key not in self._pk:
            R = self.R; Fj = self.f[j]; pj = self.p(j)
            Ft = col_add(R, col_scale(R, Fj, pj), col_T(R, Fj))          # (p_j + T) f_j
            self._pk[key] = (self._pack(Fj, weight=lambda k: 2 * k + 1), self._pack(Fj, weight=lambda k: 2 * k + 1, rev=True),
                             self._pack(Ft), self._pack(Ft, rev=True))
        return self._pk[key]
    def step_fast2(self, N):
        R = self.R; n = max(self.f) + 1; t0 = time.time(); self._ensure_stride(N); S = self._S; L = self._L
        acc1 = acc1r = acc2 = acc2r = None
        for i in range(1, n):
            j = n - i
            Bz, Bd = self._packs_g(i); Ad, Adrev, Az, Arev = self._packs_f(j)
            p1 = polymul(R, Bz, Ad); p1r = polymul(R, Bz, Adrev); p2 = polymul(R, Bd, Az); p2r = polymul(R, Bd, Arev)
            if acc1 is None: acc1, acc1r, acc2, acc2r = p1, p1r, p2, p2r
            else: acc1 = acc1 + p1; acc1r = acc1r + p1r; acc2 = acc2 + p2; acc2r = acc2r + p2r
        Qout = max(len(self.g[i]) + len(self.f[n - i]) - 1 for i in range(1, n))
        Mout = L                                       # frequency indices of the result are < L (bandwidth additivity)
        c1 = R.coeffs(acc1, Qout * S); c1r = R.coeffs(acc1r, Qout * S); c2 = R.coeffs(acc2, Qout * S); c2r = R.coeffs(acc2r, Qout * S)
        half = R.scalar(fmpq(1, 2)) if R.name != 'float' else 0.5
        cols = []
        for q in range(Qout):
            base = q * S; P1 = [R.zero] * (Mout + 1); P2 = [R.zero] * (Mout + 1)
            for m in range(Mout + 1): P1[m] = P1[m] + c1[base + m]; P2[m] = P2[m] + c2[base + m]
            for idx in range(S - 1):                    # reversed-product coefficients at block offset idx = L + t, t = j - k
                t_ = idx - L
                if -Mout <= t_ <= Mout + 1:
                    if t_ >= 1: P1[t_ - 1] = P1[t_ - 1] + c1r[base + idx]
                    elif -t_ <= Mout: P1[-t_] = P1[-t_] - c1r[base + idx]
                    if t_ <= 0:
                        if -t_ <= Mout: P2[-t_] = P2[-t_] + c2r[base + idx]
                    else: P2[t_ - 1] = P2[t_ - 1] - c2r[base + idx]
            cols.append([(x - y) * half for x, y in zip(P1, P2)])
        lam = (n - 1) * (self.c_l - 1)
        x = col_scale(R, cols, 1 / lam); term = x
        for _ in range(len(cols) + 1):
            term = col_scale(R, col_T(R, term), self.c_l / lam)
            if all(R.is_zero(v) for a in term for v in a): break
            x = col_add(R, x, term)
        self.f[n] = col_trim(R, x)
        self.g[n] = self.poisson(n)
        self._stats(n); self.stats[n]['time'] = time.time() - t0
        return n


    # ------------------------------------------------------------------ pair-parallel step (fork-based)
    def step_fast_parallel(self, workers):
        """same as step_fast, with the sum over pairs (i, n-i) split across forked worker processes.
        Ball results are rigorous enclosures; the summation order differs from step_fast, so radii/midpoints may differ by rounding."""
        import multiprocessing as mp, pickle
        R = self.R; n = max(self.f) + 1; t0 = time.time()
        if R.name != 'arb' or workers <= 1 or n < 8: return self.step_fast()
        chunks = [list(range(1 + w, n, workers)) for w in range(workers)]
        global _PAR_SELF; _PAR_SELF = self
        ctx = mp.get_context('fork')
        with ctx.Pool(workers) as pool:
            parts = pool.map(_par_worker, [(c, n) for c in chunks])
        acc = None
        for packed in parts:
            if packed is None: continue
            term = [[_arb_unpack(x) for x in col] for col in packed]
            acc = term if acc is None else col_add(R, acc, term)
        lam = (n - 1) * (self.c_l - 1)
        x = col_scale(R, acc, 1 / lam); term = x
        for _ in range(len(acc) + 1):
            term = col_scale(R, col_T(R, term), self.c_l / lam)
            if all(R.is_zero(v) for a in term for v in a): break
            x = col_add(R, x, term)
        self.f[n] = col_trim(R, x)
        self.g[n] = self.poisson(n)
        self._stats(n); self.stats[n]['time'] = time.time() - t0; self.stats[n]['workers'] = workers
        return n

    def products_wrap(self, b, a):
        """ffcore products with g given as even-sine list b (index j) and f as odd-sine list a; pads b[0]"""
        ff = _FF(self.R); return ff.products(list(b) if len(b) > 1 else list(b) + [self.R.zero], list(a))
    def _stats(self, n):
        R = self.R; F = self.f[n]; st = {'n': n, 'Kt': len(F) - 1, 'maxfreq': 2 * (max(len(a) for a in F) - 1) + 1, 'p_n': R.to_float(self.p(n))}
        cols = []; rads = []; lrads = []
        for q, a in enumerate(F):
            l2a = [R.log2abs(x) for x in a]
            if not a or max(l2a) == -float('inf'):
                cols.append(-float('inf')); continue
            imax = int(np.argmax(l2a)); mx = a[imax]
            fl = np.array([R.to_float(x / mx) for x in a])                 # scaled by the pivot: magnitudes <= 1
            lg = R.log10abs(mx)
            sf = float(np.sum(np.abs(fl)))
            cols.append((math.log10(sf) + lg) if (math.isfinite(sf) and sf > 0) else -float('inf'))   # zero-midpoint guard (09:40Z)
            if R.name == 'arb':
                rr = max((x / mx).rad() for x in a)
                rads.append((float(rr.str(5, radius=False)) if rr.is_finite() else float('inf')) if rr != 0 else 0.0)   # inf guard (11:44Z)
                lrads.append((float((rr.log() / arb(10).log()).str(10, radius=False)) if rr.is_finite() else float('inf')) if rr != 0 else -float('inf'))
        st['log10_col_l1'] = cols                    # l1 norm (over frequencies) of each t-power coefficient
        G = self.g.get(n)
        if G is not None:
            gcols = []
            for b in G:
                l2b = [R.log2abs(x) for x in b]
                if not b or max(l2b) == -float('inf'): gcols.append(-float('inf')); continue
                im = int(np.argmax(l2b)); mb = b[im]; flb = np.array([R.to_float(x / mb) for x in b])
                sg = float(np.sum(np.abs(flb)))
                gcols.append((math.log10(sg) + R.log10abs(mb)) if (math.isfinite(sg) and sg > 0) else -float('inf'))   # zero-midpoint guard (09:40Z)
            st['log10_gcol_l1'] = gcols              # stream coefficients ||g_{n,k}||_l1 per t-power
            st['gKt'] = len(G) - 1
            gfin = [c for c in gcols if c > -float('inf')]
            st['log10_sum_gcols'] = (math.log10(sum(10 ** (c - max(gfin)) for c in gfin)) + max(gfin)) if gfin else -float('inf')   # log10 N_n
            if R.name == 'arb':
                # stream radius monitor (norm-relative per column, coefficient-wise, zero midpoints with nonzero radius)
                grads = []; glr = -float('inf'); gzero = 0
                for b in G:
                    l2b = [R.log2abs(x) for x in b]
                    if not b or max(l2b) == -float('inf'): continue
                    im = int(np.argmax(l2b)); mb = b[im]
                    rr = max((x / mb).rad() for x in b)
                    grads.append(float((rr.log() / arb(10).log()).str(10, radius=False)) if rr != 0 else -float('inf'))
                    for x in b:
                        m = x.mid()
                        if m == 0 and x.rad() != 0: gzero += 1
                        elif m != 0 and x.rad() != 0: glr = max(glr, float(((x.rad() / abs(m)).log() / arb(10).log()).str(8, radius=False)))
                st['log10_grad_over_max'] = max(grads) if grads else -float('inf')
                st['log10_max_rel_rad_g'] = glr
                st['zero_mid_nonzero_rad_g'] = gzero
                st['zero_mid_nonzero_rad_f'] = sum(1 for a in F for x in a if x.mid() == 0 and x.rad() != 0)
        fin = [c for c in cols if c > -float('inf')]
        st['log10_sum_cols'] = (math.log10(sum(10 ** (c - max(fin)) for c in fin)) + max(fin)) if fin else -float('inf')   # log10 M_n
        if 'log10_sum_gcols' in st:
            st['log10_ratio_N_over_M'] = st['log10_sum_gcols'] - st['log10_sum_cols']
        if R.name == 'arb':
            worst = max(st.get('log10_rad_over_max', -float('inf')), st.get('log10_grad_over_max', -float('inf')))
            st['log10_worst_rel_rad_norm'] = worst
            st['midpoint_only'] = bool(worst > -6)
            if getattr(self, 'radii_reset_at', None) is not None: st['radii_reset_at'] = self.radii_reset_at; st['midpoint_only'] = True   # continuation relative to reset midpoints (V305)
        if R.name == 'arb':
            st['rad_over_max'] = max(rads) if rads else 0.0                # norm-relative radius per column, max over columns
            st['log10_rad_over_max'] = max(lrads) if lrads else -float('inf')
            # coefficient-wise maximal relative radius (log10), over all nonzero density coefficients of all columns
            mr = -float('inf')
            for a in F:
                for x in a:
                    m = x.mid()
                    if m != 0 and x.rad() != 0:
                        v = float(((x.rad() / abs(m)).log() / arb(10).log()).str(8, radius=False)); mr = max(mr, v)
            st['log10_max_rel_rad'] = mr
        if n in self.resonances: st['resonances'] = self.resonances[n]
        if R.name == 'fmpq': st['max_bits'] = max(R.bits(x) for a in F for x in a)
        self.stats[n] = st
    def run(self, N, log=None, ckpt=None, ckpt_every=10, stop_rel_rad=1e-6, fast=True, workers=1):
        # fast = step_fast (per-pair block products): measured 2-3x faster than the column-pair step and 2-3x faster than
        # step_fast2 (fixed-stride cached products, whose big multiplications cost more than they save) at these sizes.
        while max(self.f) < N:
            n = (self.step_fast_parallel(workers) if workers > 1 else self.step_fast()) if fast else self.step(); st = self.stats[n]
            if log: print(json.dumps(st), file=log, flush=True)
            if ckpt and n % ckpt_every == 0: self.save(ckpt)
            if self.R.name == 'arb' and st.get('rad_over_max', 0) > stop_rel_rad:
                if log: print(json.dumps({'stop': 'precision exhausted', 'n': n}), file=log, flush=True)
                break
        if ckpt: self.save(ckpt)
    def save(self, path):
        R = self.R
        pk = (lambda x: _arb_pack(x)) if R.name == 'arb' else (lambda x: str(x))
        state = {'ring': R.name, 'prec': getattr(R, 'prec', None), 'A': str(self.delta_exact.p), 'B': str(self.delta_exact.q),
                 'f': {n: [[pk(x) for x in a] for a in F] for n, F in self.f.items()}, 'g': {n: [[pk(x) for x in b] for b in G] for n, G in self.g.items()},
                 'stats': self.stats, 'resonances': self.resonances,
                 'radii_reset_at': getattr(self, 'radii_reset_at', None),
                 'perturbed_seed': getattr(self, 'perturbed_seed', None)}
        with open(path + '.tmp', 'wb') as fh: pickle.dump(state, fh, protocol=4)
        os.replace(path + '.tmp', path)
    @classmethod
    def load(cls, path):
        with open(path, 'rb') as fh: state = pickle.load(fh)
        R = make_ring(state['ring'], state.get('prec')); obj = cls.__new__(cls); obj.R = R
        obj.delta_exact = fmpq(int(state['A']), int(state['B'])); obj.c_exact = 1 / (1 - obj.delta_exact)
        obj.delta = R.scalar(obj.delta_exact); obj.c_l = R.scalar(obj.c_exact)
        up = (lambda x: _arb_unpack(x)) if R.name == 'arb' else (lambda x: R.scalar(x))
        obj.f = {n: [[up(x) for x in a] for a in F] for n, F in state['f'].items()}
        obj.g = {n: [[up(x) for x in b] for b in G] for n, G in state['g'].items()}
        obj.stats = state['stats']; obj.resonances = state['resonances']
        # Legacy checkpoints retained reset provenance in earlier statistic rows.
        # Any such ancestor keeps all later coefficients conditional.
        resets = [row['radii_reset_at'] for row in obj.stats.values()
                  if row.get('radii_reset_at') is not None]
        if state.get('radii_reset_at') is not None:
            resets.append(state['radii_reset_at'])
        obj.radii_reset_at = min(resets) if resets else None
        obj.perturbed_seed = state.get('perturbed_seed')
        return obj

_PAR_SELF = None
def _par_worker(args):
    """compute the partial pair sum for the chunk of velocity indices i (child process after fork)"""
    chunk, n = args; self = _PAR_SELF; R = self.R
    ctx.prec = R.prec
    acc = None
    for i in chunk:
        j = n - i
        Gi = self.g[i]; Fj = self.f[j]; Pi = self.p(i) + 1; pj = self.p(j)
        Gt = col_add(R, col_scale(R, Gi, Pi), col_T(R, Gi)); Ft = col_add(R, col_scale(R, Fj, pj), col_T(R, Fj))
        term = self._block_products(Gt, Fj, Gi, Ft)
        acc = term if acc is None else col_add(R, acc, term)
    if acc is None: return None
    return [[_arb_pack(x) for x in col] for col in acc]

class _FF(FarField):
    """thin wrapper to reuse FarField.products without a parameter set"""
    def __init__(self, R): self.R = R

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument('--tag', required=True); ap.add_argument('--ring', default='arb'); ap.add_argument('--prec', type=int, default=512)
    ap.add_argument('--A', type=int, required=True); ap.add_argument('--B', type=int, required=True); ap.add_argument('--f1', default='sin1'); ap.add_argument('--N', type=int, default=60)
    ap.add_argument('--ckpt-every', type=int, default=10); ap.add_argument('--resume', action='store_true'); ap.add_argument('--slow', action='store_true'); ap.add_argument('--workers', type=int, default=1); ap.add_argument('--stop-rel-rad', type=float, default=1e-6); ap.add_argument('--edge', type=int, default=None); ap.add_argument('--reset-radii', action='store_true', help='after --resume, replace every ball by its midpoint (radius 0): the continuation is then certified only relative to the loaded midpoints'); ap.add_argument('--perturb-radii', type=int, default=None, help='after --resume, replace every ball by a random boundary point mid +/- rad (seed); sensitivity diagnostic')
    args = ap.parse_args(); R = make_ring(args.ring, args.prec)
    LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if args.f1 == 'sin1': f1 = ['1']
    elif args.f1 == 'cand007': f1 = json.load(open(os.path.join(LANE, 'notes', 'cand007_f1.json')))['f1_sine_coefficients_exact']
    elif args.f1.startswith('coeffs:'): f1 = args.f1[7:].split(',')
    ck = os.path.join(LANE, 'ckpt', args.tag + '.pkl')
    if args.resume and os.path.exists(ck):
        L = LogFarField.load(ck); mode = 'a'
        if args.reset_radii and R.name == 'arb':
            L.f = {n: [[arb(x.mid()) for x in col] for col in cols] for n, cols in L.f.items()}
            L.g = {n: [[arb(x.mid()) for x in col] for col in cols] for n, cols in L.g.items()}
            L.radii_reset_at = max(L.f)
        if args.perturb_radii is not None and R.name == 'arb':
            # sensitivity diagnostic (verifier V364): replace every loaded ball [m +/- r] by the exact point m + s r, s = +1 or -1 chosen at random
            # (seed args.perturb_radii), i.e. a point on the boundary of the certified enclosure; the continuation from these points is one sample
            # of the uncertainty set of the loaded state; its radii again bound only the arithmetic of the continuation (a diagnostic, not a bound)
            import random; rng = random.Random(args.perturb_radii); cnt = 0
            def _pert(x):
                global cnt
                if x.rad() == 0: return arb(x.mid())
                cnt += 1; return arb(x.mid()) + (arb(x.rad()) if rng.random() < 0.5 else -arb(x.rad()))
            L.f = {n: [[_pert(x) for x in col] for col in cols] for n, cols in L.f.items()}
            L.g = {n: [[_pert(x) for x in col] for col in cols] for n, cols in L.g.items()}
            L.radii_reset_at = max(L.f); L.perturbed_seed = args.perturb_radii; print(f'perturbed {cnt} balls to their boundary (seed {args.perturb_radii})', flush=True)
    else:
        L = LogFarField(R, args.A, args.B, f1); mode = 'w'
    L.edge = args.edge
    with open(os.path.join(LANE, 'logs', args.tag + '.jsonl'), mode) as log:
        print(json.dumps({'tag': args.tag, 'ring': R.name, 'prec': getattr(R, 'prec', None), 'delta': f'{args.A}/{args.B}', 'c_l': str(L.c_exact), 'f1': f1, 'N_target': args.N, 'log_series': True, 'resumed_from': (max(L.f) if mode == 'a' else None), 'fast_products': not args.slow, 'edge_only_min_ij_le': args.edge, 'radii_reset_at': getattr(L, 'radii_reset_at', None), 'perturbed_seed': getattr(L, 'perturbed_seed', None)}), file=log, flush=True)
        if mode == 'w': print(json.dumps(L.stats[1]), file=log, flush=True)
        L.run(args.N, log=log, ckpt=ck, ckpt_every=args.ckpt_every, fast=not args.slow, workers=args.workers, stop_rel_rad=args.stop_rel_rad)
        print(json.dumps({'done': True, 'N': max(L.f)}), file=log, flush=True)
