"""Tuned pure series at c = 3 (delta = 2/3), lead's Theorem T (theory 12.4): f_1 = eps (sin theta + b sin 3theta) with b a real root of
P6 (Corollary T.3), the free harmonic multipole constants H_(3k) (coefficient of sin((2k-2) theta) in g_(3k)) chosen so that every
obstruction O_(3k+3) = a_(3k+3, 2k-1) vanishes: H_(3k) = -R_k / sigma_k (Lemma T.1), where R_k is the obstruction computed with
H_(3k) = 0 and sigma_k the coefficient of sin((2k-1) theta) in phi_3 (the linear response of order 3k+3 to H_(3k)).
Ball arithmetic (arb): b is a certified interval-Newton enclosure of the root; every obstruction after tuning is a ball that must
contain zero (its radius is the certified bound on the residual obstruction); the series coefficients carry rigorous radii.
Independent of the lead's code (FFT, double) and of the verifier's Cartesian code; uses the lane's ffcore products and Poisson inverse.
usage: tuned_c3.py --tag TAG --root 1|2 --prec 1024 --N 300 [--eps 1] [--ckpt-every 30]
"""
import sys, os, json, time, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpz_poly, fmpz, fmpq, arb, ctx
from ffcore import _logrow, FarField, make_ring

P6 = fmpz_poly([10532171936, -243275209320, 2783057141280, -20675598499400, 96180432855375, -222533688701250, 176703765525000])
ROOT_GUESS = {1: '0.280661662731966', 2: '0.646352289880934'}

def arb_eval(P, x):
    s = arb(0)
    for c in reversed(P.coeffs()): s = s * x + arb(c)
    return s

def root_enclosure(root, prec):
    """certified enclosure of the real root of P6 near ROOT_GUESS[root] at the given precision (interval Newton)"""
    ctx.prec = prec; dP = P6.derivative()
    x = arb(ROOT_GUESS[root])
    for _ in range(12):
        m = x.mid(); x = arb(m) - arb_eval(P6, arb(m)) / arb_eval(dP, arb(m, x.rad()))
    # verification: N(X) subset X for X = mid +/- r
    for e in range(int(prec * 0.3), 10, -5):
        X = arb(x.mid(), arb(2) ** (-e)); m = X.mid()
        NX = arb(m) - arb_eval(P6, arb(m)) / arb_eval(dP, X)
        if X.contains(NX): return NX
    raise ArithmeticError('root enclosure failed')

class TunedFarField(FarField):
    def __init__(self, ring, b, eps='1'):
        self.H = {}; self.obstruction = {}; self.sigma = {}; self.Rk = {}; self._provisional = False
        super().__init__(ring, '3', [ring.scalar(eps), ring.scalar(eps) * b], delta=fmpq(2, 3))

    def poisson(self, a, n):
        """parent's Poisson inverse, except at the exact resonances n = 3k (mode j = k-1): the compatibility numerator must be a ball
        containing zero (tuned); the free coefficient b_j is set to H_n (0 until determined)."""
        R = self.R; p = self.p(n); K = len(a) - 1
        b = [R.zero] * (K + 2); mind = None; minden_j = None; res = []
        pp1sq = (p + 1) * (p + 1)
        for j in range(1, K + 2):
            aj = a[j] if j <= K else R.zero
            num = (p - 2 * j + 1) * a[j - 1] + (p + 2 * j + 1) * aj
            den = 2 * (4 * j * j - pp1sq)
            if den.contains(0):
                nd = n * self.delta_exact
                if not (nd == 2 * (j + 1)): raise ArithmeticError(f'order {n}, j={j}: denominator ball contains zero without exact resonance')
                if not num.contains(0) and not self._provisional:
                    raise ArithmeticError(f'order {n}, j={j}: obstruction certified NONZERO: {num.str(20, radius=True)}')
                if self._provisional: b[j] = R.zero; continue          # untuned provisional pass: recorded later after the correction
                self.obstruction[n] = {'j': j, 'num_mid': R.to_float(num), 'num_rad': R.rad(num), 'log10_num_rad': R.log10abs(arb(num.rad())) if num.rad() != 0 else -float('inf')}
                res.append({'j': j, 'status': 'tuned (ball contains zero)', 'num_zero': True, 'num': R.to_float(num), 'num_str': R.to_str(num)})
                b[j] = self.H.get(n, R.zero)
                continue
            b[j] = num / den
            d = R.absf(den)
            if not R.is_zero(num) and (mind is None or d < mind): mind = d; minden_j = j
        out = {'min_active_den': mind, 'min_active_den_j': minden_j}
        if res: out['resonances'] = res
        return b, out

    def T(self, i, j, g, f):
        """T_(i,j)(g, f) = P_i g f' - p_j g' f as an odd-sine coefficient list"""
        P1, P2 = self.products(g, f); pi1 = self.p(i) + 1; pj = self.p(j)
        return [pi1 * x - pj * y for x, y in zip(P1, P2)]

    @staticmethod
    def add(u, v, scale=None):
        R_zero = u[0] * 0 if u else (v[0] * 0)
        L = max(len(u), len(v)); out = []
        for m in range(L):
            x = u[m] if m < len(u) else R_zero; y = v[m] if m < len(v) else R_zero
            out.append(x + (y if scale is None else scale * y))
        return out

    def responses(self, k):
        """phi_1, phi_2, phi_3 and sigma_k for the block n = 3k (Theorem T, response coefficients)"""
        R = self.R; n = 3 * k; lam = lambda m: (m - 1) * (self.c_l - 1)
        ek = [R.zero] * k; ek[k - 1] = R.scalar(1)                      # sin((2k-2) theta): stream index j = k-1
        f1, f2, f3, g1, g2 = self.f[1], self.f[2], self.f[3], self.g[1], self.g[2]
        phi1 = [x / lam(n + 1) for x in self.T(n, 1, ek, f1)]
        Pphi1, _ = self.poisson(phi1, n + 1)
        acc = self.T(n, 2, ek, f2); acc = self.add(acc, self.T(1, n + 1, g1, phi1)); acc = self.add(acc, self.T(n + 1, 1, Pphi1, f1))
        phi2 = [x / lam(n + 2) for x in acc]
        Pphi2, _ = self.poisson(phi2, n + 2)
        acc = self.T(n, 3, ek, f3); acc = self.add(acc, self.T(1, n + 2, g1, phi2)); acc = self.add(acc, self.T(n + 2, 1, Pphi2, f1))
        acc = self.add(acc, self.T(2, n + 1, g2, phi1)); acc = self.add(acc, self.T(n + 1, 2, Pphi1, f2))
        phi3 = [x / lam(n + 3) for x in acc]
        sigma = phi3[k - 1] if k - 1 < len(phi3) else R.zero
        return phi1, phi2, phi3, sigma

    def run_tuned(self, N, log=None, ckpt=None, ckpt_every=30):
        """orders 2..N. Whenever the last computed order n = 3k (k >= 2) has no H_n yet: provisional orders n+1..n+3 with H_n = 0,
        then H_n = -R_k/sigma_k (Lemma T.1), the affine correction of f_(n+1..n+3), g_n[k-1] = H_n, and the Poisson inverses of the
        corrected f_(n+1), f_(n+2), f_(n+3) (the last one checks that the tuned obstruction O_(n+3) is a ball containing zero)."""
        R = self.R; emitted = set()
        def emit(n):
            st = self.stats[n]; row = _logrow(st)
            if n in self.H: row['H'] = R.to_float(self.H[n]); row['H_str'] = self.H[n].str(30, radius=True); row['log10_absH'] = R.log10abs(self.H[n])
            if n in self.obstruction: row['obstruction'] = self.obstruction[n]
            if n in self.sigma: row['sigma_k'] = R.to_float(self.sigma[n]); row['sigma_str'] = self.sigma[n].str(20, radius=True); row['R_k'] = R.to_float(self.Rk[n])
            if log: print(json.dumps(row), file=log, flush=True)
            emitted.add(n)
        def resonant_open(n): return n % 3 == 0 and n >= 6 and n not in self.H
        while max(self.f) < N:
            n = max(self.f)
            if not resonant_open(n):
                n = self.step()
                if not resonant_open(n): emit(n)
                if ckpt and n % ckpt_every == 0: self.save(ckpt); self.save_H(ckpt)
                continue
            k = n // 3; t0 = time.time()
            phi1, phi2, phi3, sigma = self.responses(k); self.sigma[n] = sigma
            self._provisional = True
            for _ in range(3): self.step()
            self._provisional = False
            f0 = self.f[n + 3]; Rk = f0[k - 1] if k - 1 < len(f0) else R.zero; self.Rk[n] = Rk
            if sigma.contains(0): raise ArithmeticError(f'sigma_{k} ball contains zero: {sigma.str(20, radius=True)}')
            H = -Rk / sigma; self.H[n] = H
            self.f[n + 1] = self.add(self.f[n + 1], phi1, H); self.f[n + 2] = self.add(self.f[n + 2], phi2, H); self.f[n + 3] = self.add(self.f[n + 3], phi3, H)
            gn = list(self.g[n])
            while len(gn) < k: gn.append(R.zero)
            gn[k - 1] = H; self.g[n] = gn
            for m in (n + 1, n + 2, n + 3):
                self.g[m], st = self.poisson(self.f[m], m); self.stats[m].update(st); self._fill_stats(m)
            self._fill_stats(n); self.stats[n]['time_block'] = time.time() - t0
            for m in (n, n + 1, n + 2): emit(m)
            if ckpt and any((n + i) % ckpt_every == 0 for i in range(4)): self.save(ckpt); self.save_H(ckpt)
        for m in sorted(self.f):
            if m not in emitted and m > 1: emit(m)
        if ckpt: self.save(ckpt); self.save_H(ckpt)

    def save_H(self, ckpt):
        d = {'H': {str(n): {'mid': self.R.to_float(h), 'str': h.str(40, radius=True)} for n, h in self.H.items()},
             'sigma': {str(n): self.sigma[n].str(30, radius=True) for n in self.sigma},
             'R_k': {str(n): self.Rk[n].str(30, radius=True) for n in self.Rk},
             'obstruction': {str(n): v for n, v in self.obstruction.items()}}
        json.dump(d, open(ckpt.replace('.pkl', '_H.json'), 'w'), indent=0)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--tag', required=True); ap.add_argument('--root', type=int, default=1)
    ap.add_argument('--prec', type=int, default=1024); ap.add_argument('--N', type=int, default=60); ap.add_argument('--eps', default='1')
    ap.add_argument('--ckpt-every', type=int, default=30)
    args = ap.parse_args()
    LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    R = make_ring('arb', args.prec)
    b = root_enclosure(args.root, args.prec)
    T = TunedFarField(R, b, args.eps)
    ck = os.path.join(LANE, 'ckpt', args.tag + '.pkl')
    with open(os.path.join(LANE, 'logs', args.tag + '.jsonl'), 'w') as log:
        print(json.dumps({'tag': args.tag, 'ring': 'arb', 'prec': args.prec, 'c_l': '3', 'delta': '2/3', 'f1': f'eps (sin + b sin3), eps = {args.eps}, root {args.root}',
                          'b_enclosure': b.str(60, radius=True), 'N_target': args.N, 'tuned': True}), file=log, flush=True)
        print(json.dumps(_logrow(T.stats[1])), file=log, flush=True)
        T.run_tuned(args.N, log=log, ckpt=ck, ckpt_every=args.ckpt_every)
        print(json.dumps({'done': True, 'N': max(T.f)}), file=log, flush=True)
