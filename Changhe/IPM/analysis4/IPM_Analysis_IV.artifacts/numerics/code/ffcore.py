"""
ffcore.py : stationary far-field angular recursion of the self-similar IPM equation.

Conventions (see PROMPT.md, Part I):
  rho   = sum_n r^{p_n} f_n(theta),      p_n = 1 - n*delta, delta = 1 - 1/c_l, gamma = 1/c_l = p_1
  psi   = sum_n r^{p_n+1} g_n(theta),    -Delta psi = d_x rho,  u = (-psi_y, psi_x)
  chi   = sum_n r^{p_n+3} C_n(theta),    rho = -d_y Delta chi,  psi = chi_xy
  f_n = sum_{k>=0} a[k] sin((2k+1) theta)          (list a, index k)
  g_n = sum_{j>=1} b[j] sin(2j theta)              (list b, index j, b[0] = 0)
  C_n = sum_{m>=0} c[m] cos(2m theta)              (list c, index m)

Poisson inverse (prompt eq. 4):
  b_j = [ (p-2j+1) a_{j-1} + (p+2j+1) a_j ] / ( 2 (4 j^2 - (p+1)^2) )
Recursion (prompt eq. 5):
  (n-1)(c_l-1) f_n = sum_{i+j=n} [ (p_i+1) g_i f_j' - p_j g_i' f_j ]

Arithmetic rings: 'fmpq' (exact rationals, python-flint), 'arb' (ball arithmetic at ctx.prec bits),
'float' (numpy float64, for quick scans only).
"""
import sys, json, math, time, os, pickle
sys.set_int_max_str_digits(0)
import numpy as np
from flint import fmpq, fmpq_poly, arb, arb_poly, ctx, fmpz

# ----------------------------------------------------------------------------- rings
class RingQ:
    name = 'fmpq'
    def scalar(self, x):
        if isinstance(x, fmpq): return x
        if isinstance(x, str):
            if '/' in x:
                a, b = x.split('/'); return fmpq(int(a), int(b))
            return fmpq(int(x))
        if isinstance(x, int): return fmpq(x)
        if hasattr(x, 'numerator'): return fmpq(int(x.numerator), int(x.denominator))
        raise TypeError(type(x))
    zero = fmpq(0)
    def poly(self, coeffs): return fmpq_poly(list(coeffs))
    def coeffs(self, P, n):
        c = P.coeffs(); c = c + [fmpq(0)] * (n - len(c)); return c[:n]
    def to_float(self, x): return float(x)
    def to_str(self, x): return str(x)
    def is_zero(self, x): return x == 0
    def absf(self, x): return abs(float(x))
    def bits(self, x): return max(int(x.p).bit_length(), int(x.q).bit_length())
    def rad(self, x): return 0.0
    def log2abs(self, x):
        """float log2|x| without under/overflow (-inf for 0)"""
        if x == 0: return -float('inf')
        p, q = abs(int(x.p)), int(x.q)
        return (p.bit_length() + math.log2(p / (1 << (p.bit_length() - 1))) - 1) - (q.bit_length() + math.log2(q / (1 << (q.bit_length() - 1))) - 1) if p > 0 else -float('inf')
    def log10abs(self, x):
        if x == 0: return -float('inf')
        return float((abs(arb(x)).log() / arb(10).log()).str(20, radius=False))

class RingArb:
    name = 'arb'
    def __init__(self, prec):
        self.prec = prec; ctx.prec = prec
    def scalar(self, x):
        ctx.prec = self.prec
        if isinstance(x, arb): return x
        if isinstance(x, fmpq): return arb(x)
        if isinstance(x, str):
            if '/' in x:
                a, b = x.split('/'); return arb(fmpq(int(a), int(b)))
            return arb(x)
        if isinstance(x, (int, float)): return arb(x)
        if hasattr(x, 'numerator'): return arb(fmpq(int(x.numerator), int(x.denominator)))
        raise TypeError(type(x))
    zero = arb(0)
    def poly(self, coeffs): ctx.prec = self.prec; return arb_poly(list(coeffs))
    def coeffs(self, P, n):
        c = P.coeffs(); c = c + [arb(0)] * (n - len(c)); return c[:n]
    def to_float(self, x): return float(x.mid().str(20, radius=False)) if x.mid() != 0 else 0.0
    def to_str(self, x): return x.str(40, radius=True)
    def is_zero(self, x): return x.is_zero()
    def absf(self, x): return float(abs(x).mid().str(20, radius=False))
    def bits(self, x): return self.prec
    def rad(self, x): return float(x.rad().str(5, radius=False)) if x.rad() != 0 else 0.0
    def log2abs(self, x):
        """float log2 of |midpoint| from the exact dyadic mantissa/exponent (no under/overflow); -inf for 0"""
        m = x.mid()
        if m == 0: return -float('inf')
        man, e = m.man_exp(); man = abs(int(man)); e = int(e)
        return man.bit_length() - 1 + math.log2(man / (1 << (man.bit_length() - 1))) + e
    def log10abs(self, x):
        m = x.mid()
        if m == 0: return -float('inf')
        return float((abs(m).log() / arb(10).log()).str(20, radius=False))

class RingF:
    name = 'float'
    def scalar(self, x):
        if isinstance(x, str) and '/' in x:
            a, b = x.split('/'); return int(a) / int(b)
        return float(x)
    zero = 0.0
    def poly(self, coeffs): return np.asarray(list(coeffs), dtype=float)
    def coeffs(self, P, n):
        out = np.zeros(n); m = min(n, len(P)); out[:m] = P[:m]; return list(out)
    def to_float(self, x): return float(x)
    def to_str(self, x): return repr(float(x))
    def is_zero(self, x): return x == 0.0
    def absf(self, x): return abs(float(x))
    def bits(self, x): return 53
    def rad(self, x): return 0.0
    def log2abs(self, x): return math.log2(abs(x)) if x != 0 else -float('inf')
    def log10abs(self, x): return math.log10(abs(x)) if x != 0 else -float('inf')

def polymul(R, A, B):
    if R.name == 'float':
        return np.convolve(A, B)
    return A * B

def make_ring(kind, prec=None):
    if kind == 'fmpq': return RingQ()
    if kind == 'arb': return RingArb(prec or 256)
    if kind == 'float': return RingF()
    raise ValueError(kind)

# ----------------------------------------------------------------------------- core
class FarField:
    def __init__(self, ring, c_l, f1, delta=None):
        """c_l: scalar-like (string '4076.../2251...' or fmpq/arb). If delta is given (e.g. arb(1)/sqrt(5))
        it overrides 1-1/c_l (used for algebraic parameters where delta is the natural quantity)."""
        self.R = ring
        R = ring
        self.delta_exact = None            # fmpq when the parameter is an exact rational (decides exact resonances)
        self.stopped = None                # set to a dict when the pure ansatz is obstructed (failed exact resonance)
        if delta is not None:
            self.delta = R.scalar(delta); self.gamma = 1 - self.delta; self.c_l = 1 / self.gamma
            if isinstance(delta, fmpq): self.delta_exact = delta
        else:
            self.c_l = R.scalar(c_l); self.gamma = 1 / self.c_l; self.delta = 1 - self.gamma
            try:
                clq = RingQ().scalar(c_l) if isinstance(c_l, (str, int, fmpq)) or hasattr(c_l, 'numerator') else None
                if clq is not None: self.delta_exact = 1 - 1 / clq
            except Exception: self.delta_exact = None
            if R.name == 'fmpq': self.delta_exact = self.delta
        self.f = {1: [R.scalar(x) for x in f1]}     # order -> list a[k]
        self.g = {}                                  # order -> list b[j]
        self.stats = {}
        self.g[1], self.stats[1] = self.poisson(self.f[1], 1)
        self._fill_stats(1)

    def p(self, n): return 1 - n * self.delta

    # Poisson inverse -(d^2 + (p+1)^2) g = p cos f - sin f'
    def poisson(self, a, n):
        R = self.R; p = self.p(n); K = len(a) - 1
        b = [R.zero] * (K + 2)
        mind = None; minden_j = None; res = []
        pp1sq = (p + 1) * (p + 1)
        for j in range(1, K + 2):
            aj = a[j] if j <= K else R.zero
            num = (p - 2 * j + 1) * a[j - 1] + (p + 2 * j + 1) * aj
            den = 2 * (4 * j * j - pp1sq)
            if R.name == 'fmpq': den_zero = R.is_zero(den)
            elif R.name == 'arb': den_zero = den.contains(0)
            else: den_zero = (den == 0.0)
            if den_zero:
                # Exact resonance n*delta = 2(j+1) (P = p+1 = -2j) or P = +2j: decided EXACTLY from delta_exact when known.
                exact_res = None
                if self.delta_exact is not None:
                    nd = n * self.delta_exact
                    exact_res = (nd == 2 * (j + 1)) or (nd == 2 * (1 - j))
                if exact_res is None or (R.name == 'arb' and not exact_res):
                    # a ball denominator containing zero without a proven exact resonance: enclosure uncertified
                    raise ArithmeticError(f'order {n}, mode j={j}: Poisson denominator encloses zero but exact resonance is not proven '
                                          f'(delta_exact={self.delta_exact}); increase precision or supply an exact rational parameter')
                # proven exact resonance: the mode sin(2j theta) of g is a free harmonic multipole; compatibility needs num = 0.
                # Three statuses: 'compatible' (num exactly zero), 'incompatible' (num certified nonzero: exact nonzero or
                # ball excluding zero), 'open' (ball contains zero but is not exactly zero: precision failure).
                if R.name == 'arb':
                    if num.is_zero(): status = 'compatible'
                    elif not num.contains(0): status = 'incompatible'
                    else: status = 'open'
                else:
                    status = 'compatible' if R.is_zero(num) else 'incompatible'
                if status == 'open':
                    raise ArithmeticError(f'order {n}, mode j={j}: exact resonance, compatibility numerator ball contains zero but is not exactly zero; increase precision')
                res.append({'j': j, 'status': status, 'num_zero': status == 'compatible', 'num': R.to_float(num), 'num_str': R.to_str(num)})
                b[j] = R.zero
                continue
            b[j] = num / den
            d = R.absf(den)
            if not R.is_zero(num) and (mind is None or d < mind):
                mind = d; minden_j = j
        out = {'min_active_den': mind, 'min_active_den_j': minden_j}
        if res: out['resonances'] = res
        return b, out

    # products: given g (b[j], j>=1) and f (a[k]); returns odd-sine coefficient lists of g f' and g' f
    def products(self, b, a):
        R = self.R
        J = len(b) - 1; K = len(a) - 1
        Bz = R.poly(b)                                       # sum b_j z^j
        Bd = R.poly([2 * j * b[j] for j in range(J + 1)])    # g' coefficients 2j b_j (cos(2j theta))
        Ad = R.poly([(2 * k + 1) * a[k] for k in range(K + 1)])  # f' coefficients (cos((2k+1)theta))
        Az = R.poly(a)
        Mout = J + K                                         # max index m = J + K (freq 2(J+K)+1)
        P1 = [R.zero] * (Mout + 1); P2 = [R.zero] * (Mout + 1)
        # ---- P1 = g f' = sum b_j (2k+1)a_k [ sin((2(j+k)+1)th) + sin((2(j-k-1)+1)th) ] / 2
        S = R.coeffs(polymul(R, Bz, Ad), J + K + 1)
        for m in range(J + K + 1): P1[m] = P1[m] + S[m]
        Adrev = R.poly([(2 * (K - i) + 1) * a[K - i] for i in range(K + 1)])  # reversed f'
        Rr = R.coeffs(polymul(R, Bz, Adrev), J + K + 1)      # coefficient of z^{K+t} is sum_{j-k=t} b_j c_k
        for idx in range(J + K + 1):
            t = idx - K
            if t >= 1: P1[t - 1] = P1[t - 1] + Rr[idx]
            else: P1[-t] = P1[-t] - Rr[idx]
        # ---- P2 = g' f = sum 2j b_j a_k [ sin((2(j+k)+1)th) + sin((2(k-j)+1)th) ] / 2
        S = R.coeffs(polymul(R, Bd, Az), J + K + 1)
        for m in range(J + K + 1): P2[m] = P2[m] + S[m]
        Arev = R.poly([a[K - i] for i in range(K + 1)])
        Rr = R.coeffs(polymul(R, Bd, Arev), J + K + 1)       # coefficient of z^{K+t} is sum_{j-k=t} 2j b_j a_k
        for idx in range(J + K + 1):
            t = idx - K                                      # t = j - k ;  k - j = -t
            if t <= 0: P2[-t] = P2[-t] + Rr[idx]
            else: P2[t - 1] = P2[t - 1] - Rr[idx]
        half = R.scalar(fmpq(1, 2)) if R.name != 'float' else 0.5
        P1 = [x * half for x in P1]; P2 = [x * half for x in P2]
        return P1, P2

    def step(self):
        """compute the next order n = max+1"""
        R = self.R
        n = max(self.f) + 1
        t0 = time.time()
        acc = None
        for i in range(1, n):
            j = n - i
            P1, P2 = self.products(self.g[i], self.f[j])
            pi1 = self.p(i) + 1; pj = self.p(j)
            term = [pi1 * x - pj * y for x, y in zip(P1, P2)]
            if acc is None: acc = term
            else:
                if len(term) > len(acc): acc = acc + [R.zero] * (len(term) - len(acc))
                for m in range(len(term)): acc[m] = acc[m] + term[m]
        den = (n - 1) * (self.c_l - 1)
        fn = [x / den for x in acc]
        # trim trailing exact zeros
        while len(fn) > 1 and R.is_zero(fn[-1]): fn.pop()
        self.f[n] = fn
        self.g[n], st = self.poisson(fn, n)
        self.stats[n] = st
        self._fill_stats(n)
        self.stats[n]['time'] = time.time() - t0
        failed = [r for r in st.get('resonances', []) if not r['num_zero']]
        if failed and self.stopped is None:
            self.stopped = {'n': n, 'resonances': failed, 'reason': 'pure ansatz obstructed: failed compatibility at an exact resonance; later orders would be the b=0 continuation'}
        return n

    def _fill_stats(self, n):
        """per-order statistics, computed in scaled form (coefficients divided by their max modulus) so that no float64
        under/overflow occurs; magnitudes are stored both as floats (when representable) and as log10 values."""
        R = self.R; a = self.f[n]; st = self.stats[n]
        st['n'] = n; st['K'] = len(a) - 1; st['maxfreq'] = 2 * (len(a) - 1) + 1
        st['p_n'] = R.to_float(self.p(n))
        # scale = max |a_k| as a ring element; pivot chosen from exact dyadic exponents (no float under/overflow)
        l2a = [R.log2abs(x) for x in a]
        imax = int(np.argmax(l2a)) if len(a) else 0
        mx = a[imax] if len(a) else R.zero
        if R.is_zero(mx):
            for k in ('l1', 'l2', 'L2', 'Linf', 'maxabs', 'alpha', 'beta', 'betap', 'Lambda', 'y_n'): st[k] = 0.0
            for k in ('log10_l1', 'log10_l2', 'log10_Linf', 'log10_maxabs'): st[k] = -float('inf')
            st['argmax_k'] = 0; st['A_sigma'] = {}; st['log10_A_sigma'] = {}
            st['d_n'] = float(abs(n * R.to_float(self.delta) - 2 * round(n * R.to_float(self.delta) / 2)))
            return
        lg = R.log10abs(mx)
        st['log10_maxabs'] = lg
        fl = np.array([R.to_float(x / mx) for x in a])            # scaled coefficients, max modulus 1
        st['argmax_k'] = imax
        def put(key, val_scaled):
            st['log10_' + key] = (math.log10(val_scaled) + lg) if val_scaled > 0 else -float('inf')
            v = st['log10_' + key]
            st[key] = float(10 ** v) if -300 < v < 300 else (0.0 if v <= -300 else float('inf'))
        put('maxabs', 1.0)
        put('l1', float(np.sum(np.abs(fl))))
        put('l2', float(math.sqrt(float(np.sum(fl * fl)))))
        put('L2', float(math.sqrt(math.pi * float(np.sum(fl * fl)))))
        put('Linf', float(linf_odd_sine(fl)))
        st['alpha'] = st['l1']; st['log10_alpha'] = st['log10_l1']
        st['A_sigma'] = {}; st['log10_A_sigma'] = {}
        ks = 2 * np.arange(len(fl)) + 1
        for sig in (0.05, 0.1, 0.2, 0.5):
            # sum |a_k| e^{sig k}: factor out e^{sig kmax}
            kmax = float(ks[-1]); w = np.exp(sig * (ks - kmax)); v = float(np.sum(np.abs(fl) * w))
            lgA = (math.log10(v) + sig * kmax / math.log(10) + lg) if v > 0 else -float('inf')
            st['log10_A_sigma'][str(sig)] = lgA
            st['A_sigma'][str(sig)] = float(10 ** lgA) if -300 < lgA < 300 else (0.0 if lgA <= -300 else float('inf'))
        if R.name == 'arb':
            rads = [R.rad(x / mx) for x in a]                       # radii relative to the max modulus
            st['rad_over_max'] = float(max(rads)) if rads else 0.0
            relr = []
            for x, ab in zip(a, np.abs(fl)):
                rr = R.rad(x / mx)
                relr.append(rr / ab if ab > 0 else (0.0 if rr == 0 else float('inf')))
            st['max_rel_rad'] = float(max(relr)) if relr else 0.0
            st['max_rad'] = st['rad_over_max'] * st['maxabs'] if st['maxabs'] < float('inf') else float('inf')
            # log10 of the norm-relative radius without float underflow (rad_over_max prints 0.0 below 1e-308)
            try:
                rr = max((x / mx).rad() for x in a)
                st['log10_rad_over_max'] = float((rr.log() / arb(10).log()).str(10, radius=False)) if rr != 0 else -float('inf')
            except Exception:
                st['log10_rad_over_max'] = None
        elif R.name == 'fmpq':
            st['max_bits'] = int(max(R.bits(x) for x in a))
            st['den_bits'] = int(max(int(x.q).bit_length() for x in a))
        nd = n * R.to_float(self.delta)
        st['d_n'] = float(abs(nd - 2 * round(nd / 2)))
        P = R.to_float(self.p(n)) + 1
        b = self.g.get(n)
        if b is not None and len(b) > 1:
            bl = np.array([R.to_float(x / mx) for x in b]); js = np.arange(len(bl))
            beta_s = float(np.sum(np.abs(bl))); betap_s = float(np.sum(2 * js * np.abs(bl)))
            st['log10_beta'] = (math.log10(beta_s) + lg) if beta_s > 0 else -float('inf')
            st['log10_betap'] = (math.log10(betap_s) + lg) if betap_s > 0 else -float('inf')
            st['beta'] = float(10 ** st['log10_beta']) if -300 < st['log10_beta'] < 300 else 0.0
            st['betap'] = float(10 ** st['log10_betap']) if -300 < st['log10_betap'] < 300 else 0.0
            alpha_s = float(np.sum(np.abs(fl)))
            st['Lambda'] = float(max(betap_s, abs(P) * beta_s) / alpha_s) if alpha_s > 0 else 0.0
            act = [abs(2 * j + P) for j in range(1, len(a) + 1) if (not R.is_zero(a[j - 1])) or (j < len(a) and not R.is_zero(a[j]))]
            st['min_active_lin_div'] = float(min(act)) if act else None
        st['log10_y_n'] = (math.log10(n) + st['log10_l1'] - math.log10(st['d_n'])) if st['d_n'] > 0 else float('inf')
        st['y_n'] = float(10 ** st['log10_y_n']) if -300 < st['log10_y_n'] < 300 else float('inf')

    def run(self, N, log=None, ckpt=None, ckpt_every=10, stop_rel_rad=1e-6, continue_after_resonance=False):
        while max(self.f) < N:
            n = self.step()
            st = self.stats[n]
            if self.stopped is not None and self.stopped['n'] == n and not continue_after_resonance:
                if log: print(json.dumps({k: v for k, v in st.items() if k != 'A_sigma'}), file=log, flush=True)
                if log: print(json.dumps({'stop': self.stopped['reason'], 'n': n, 'resonances': self.stopped['resonances']}), file=log, flush=True)
                break
            if log:
                print(json.dumps(_logrow(st)), file=log, flush=True)
            if ckpt and n % ckpt_every == 0: self.save(ckpt)
            if self.R.name == 'arb' and st.get('rad_over_max', 0) > stop_rel_rad:
                if log: print(json.dumps({'stop': 'precision exhausted (norm-relative radius)', 'n': n, 'rad_over_max': st['rad_over_max'], 'max_rel_rad': st['max_rel_rad']}), file=log, flush=True)
                break
        if ckpt: self.save(ckpt)

    # -------------------------------------------------------------- chi reconstruction
    def chi_coeffs(self, n):
        """C_n cosine coefficients c[m] from f_n: f = -[(p+1) sin D + cos D'], D = C'' + (p+3)^2 C.
        Mode bookkeeping: a_k = [ (p+3+2k) d_{k+1} - (p+1-2k) d_k ] / 2 for k >= 1 and
        a_0 = (p+3)/2 d_1 - (p+1) d_0 (the m = 0 cosine mode has no factor 1/2)."""
        R = self.R; a = self.f[n]; p = self.p(n); K = len(a) - 1
        if R.is_zero(p + 1):
            raise ValueError(f'order {n}: p_n = -1 (n delta = 2): chi_n needs an r^2 log r term unless f_n(pi/2) = 0; potential ansatz (2) degenerate')
        for k in range(K + 1):
            if R.is_zero(p + 1 - 2 * k) or R.is_zero((p + 3) * (p + 3) - 4 * k * k):
                raise ValueError(f'order {n}: singular chi pivot (p+1-2k = 0 or (p+3)^2 = 4k^2 at k={k}); potential ansatz (2) degenerate at this order')
        d = [R.zero] * (K + 1)
        if K == 0:
            d[0] = -a[0] / (p + 1)
        else:
            d[K] = -2 * a[K] / (p + 1 - 2 * K)
            for k in range(K - 1, 0, -1):
                d[k] = ((p + 3 + 2 * k) * d[k + 1] - 2 * a[k]) / (p + 1 - 2 * k)
            d[0] = ((p + 3) * d[1] / 2 - a[0]) / (p + 1)
        c = [d[m] / ((p + 3) * (p + 3) - 4 * m * m) for m in range(K + 1)]
        return c

    # -------------------------------------------------------------- checkpoints
    def save(self, path):
        R = self.R
        state = {'ring': R.name, 'prec': getattr(R, 'prec', None),
                 'c_l': R.to_str(self.c_l), 'delta': R.to_str(self.delta),
                 'N': max(self.f), 'stats': self.stats, 'stopped': self.stopped,
                 'delta_exact': (str(self.delta_exact) if self.delta_exact is not None else None)}
        if R.name == 'arb':
            state['f'] = {n: [_arb_pack(x) for x in a] for n, a in self.f.items()}
            state['g'] = {n: [_arb_pack(x) for x in b] for n, b in self.g.items()}
            state['c_l_pack'] = _arb_pack(self.c_l); state['delta_pack'] = _arb_pack(self.delta)
        elif R.name == 'fmpq':
            state['f'] = {n: [str(x) for x in a] for n, a in self.f.items()}
            state['g'] = {n: [str(x) for x in b] for n, b in self.g.items()}
        else:
            state['f'] = {n: [float(x) for x in a] for n, a in self.f.items()}
            state['g'] = {n: [float(x) for x in b] for n, b in self.g.items()}
        tmp = path + '.tmp'
        with open(tmp, 'wb') as fh: pickle.dump(state, fh, protocol=4)
        os.replace(tmp, path)

    @classmethod
    def load(cls, path):
        with open(path, 'rb') as fh: state = pickle.load(fh)
        R = make_ring(state['ring'], state.get('prec'))
        obj = cls.__new__(cls); obj.R = R
        if R.name == 'arb':
            obj.c_l = _arb_unpack(state['c_l_pack']); obj.delta = _arb_unpack(state['delta_pack']); obj.gamma = 1 - obj.delta
            obj.f = {n: [_arb_unpack(x) for x in a] for n, a in state['f'].items()}
            obj.g = {n: [_arb_unpack(x) for x in b] for n, b in state['g'].items()}
        elif R.name == 'fmpq':
            obj.c_l = R.scalar(state['c_l']); obj.gamma = 1 / obj.c_l; obj.delta = 1 - obj.gamma
            obj.f = {n: [R.scalar(x) for x in a] for n, a in state['f'].items()}
            obj.g = {n: [R.scalar(x) for x in b] for n, b in state['g'].items()}
        else:
            obj.c_l = float(state['c_l']); obj.gamma = 1 / obj.c_l; obj.delta = 1 - obj.gamma
            obj.f = {n: list(a) for n, a in state['f'].items()}; obj.g = {n: list(b) for n, b in state['g'].items()}
        obj.stats = state['stats']
        obj.stopped = state.get('stopped'); obj.delta_exact = None
        de = state.get('delta_exact')
        if de is not None: obj.delta_exact = RingQ().scalar(de)
        return obj

def _arb_pack(x):
    m, e = x.mid().man_exp()
    if x.rad() == 0: return (str(m), int(e), '0')
    rm, re_ = x.rad().man_exp()                       # radius is itself a dyadic; store exactly
    return (str(m), int(e), f'{int(rm)}*2^{int(re_)}')

def _arb_unpack(t):
    m, e, r = t
    m = int(m); saved = ctx.prec
    ctx.prec = max(saved, m.bit_length() + 64)       # exact reconstruction of the dyadic midpoint
    v = arb(fmpz(m)) * (arb(2) ** int(e))
    assert v.is_exact()
    ctx.prec = saved
    if r != '0':
        if '*2^' in r:
            rm, re_ = r.split('*2^'); rad = arb(fmpz(int(rm))) * (arb(2) ** int(re_))
        else: rad = arb(r)
        v = arb(v, rad)
    return v

def _logrow(st):
    row = {k: v for k, v in st.items() if k not in ('A_sigma', 'log10_A_sigma')}
    for sig in ('0.1', '0.5'):
        if sig in st.get('A_sigma', {}): row['A' + sig] = st['A_sigma'][sig]; row['log10_A' + sig] = st['log10_A_sigma'][sig]
    return row

# ----------------------------------------------------------------------------- helpers
def linf_odd_sine(a, factor=8):
    """sup norm of sum a_k sin((2k+1)theta) on a fine grid (float64; indicative, not certified)"""
    a = np.asarray(a, dtype=float); K = len(a)
    M = max(256, factor * (2 * K + 1))
    th = np.linspace(0, math.pi / 2, M)          # odd-sine series: |f| symmetric; quarter period suffices
    ks = 2 * np.arange(K) + 1
    vals = np.sin(np.outer(th, ks)) @ a
    return float(np.max(np.abs(vals)))

def eval_odd_sine(a, th):
    a = np.asarray(a, dtype=float); ks = 2 * np.arange(len(a)) + 1
    return np.sin(np.outer(np.asarray(th), ks)) @ a

def eval_even_sine(b, th):
    b = np.asarray(b, dtype=float); js = 2 * np.arange(len(b))
    return np.sin(np.outer(np.asarray(th), js)) @ b

def eval_even_cos(c, th):
    c = np.asarray(c, dtype=float); ms = 2 * np.arange(len(c))
    return np.cos(np.outer(np.asarray(th), ms)) @ c

# ----------------------------------------------------------------------------- Candidate 007 extraction
CAND007 = 'source/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json'

def load_candidate007(root):
    """returns (c_l fmpq, dict branch j -> list of leading cosine moments L_{j,m} as fmpq, m = 0..mmax)"""
    import collections
    with open(os.path.join(root, CAND007)) as fh: d = json.load(fh)
    cl = RingQ().scalar(d['cl_exact'])
    L = collections.defaultdict(lambda: fmpq(0)); mmax = collections.defaultdict(int)
    for gen in d['generators']:
        j, m = gen['j'], gen['m']
        L[(j, m)] += RingQ().scalar(gen['coef']); mmax[j] = max(mmax[j], m)
    br = {j: [L[(j, m)] for m in range(mmax[j] + 1)] for j in mmax}
    return cl, br

def f_from_C(c, p):
    """exact: given C = sum c[m] cos(2m theta) and exponent p (chi term r^{p+3} C), return a[k] of f = -[(p+1) sin D + cos D'],
    D = C'' + (p+3)^2 C.  a_k = [ (p+3+2k) d_{k+1} - (p+1-2k) d_k ] / 2 (k >= 1),  a_0 = (p+3)/2 d_1 - (p+1) d_0"""
    M = len(c) - 1
    if isinstance(p, (int, float)) and not isinstance(p, bool): p = fmpq(p) if isinstance(p, int) else p
    d = [(-(2 * m) ** 2 + (p + 3) ** 2) * c[m] for m in range(M + 1)]
    a = []
    for k in range(M + 1):
        dk1 = d[k + 1] if k + 1 <= M else 0
        if k == 0: a.append((p + 3) * dk1 / 2 - (p + 1) * d[0])
        else: a.append(((p + 3 + 2 * k) * dk1 - (p + 1 - 2 * k) * d[k]) / 2)
    return a
