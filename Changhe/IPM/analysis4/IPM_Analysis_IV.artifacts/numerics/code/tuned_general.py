"""Tuned pure series at a general rational delta = a/b (lead's Section 12.6, Corollary T_{Q,h}), generalizing tuned_cQ.py.
Resonances: n delta = 2(j+1) with integer j >= 1, i.e. n a = 2b(j+1): resonant orders are the multiples of the period P = 2b/gcd(a, 2)
with j_n = n a/(2b) - 1 >= 1; the free stream coefficient H_n of sin(2 j_n theta) at a resonant order n is fixed by the obstruction
a_(n+P, j_(n+P) - 1) of the next resonant order through the affine response (phi_1..phi_P, sigma = [index j_(n+P)-1] phi_P):
lambda_(n+i) phi_i = T_(n,i)(e, f_i) + sum_(m<i) [T_(n+m,i-m)(Pi phi_m, f_(i-m)) + T_(i-m,n+m)(g_(i-m), phi_m)], i = 1..P.
Valid because a product with two factors of order >= n cannot occur below order 2n > n + P for n >= P (for n = P the pair (P, P) has
one factor independent of H_P). f_1 = eps (sin theta + b sin 3theta), b a certified root (interval Newton) of the first obstruction
polynomial given as integer coefficients (ascending) in a JSON file or inline; every tuned obstruction must be a ball containing zero.
usage: tuned_general.py --tag TAG --a 4 --b 9 --poly-coeffs c0,c1,...,cd --root-guess 1.8566753384 --prec 1024 --N 300"""
import sys, os, json, time, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpz_poly, fmpz, fmpq, arb, ctx
from ffcore import _logrow, FarField, make_ring
from tuned_c3 import arb_eval
from tuned_cQ import root_enclosure_poly

class TunedGeneral(FarField):
    def __init__(self, ring, a, b_den, b, eps='1', f1=None):
        """f1: optional explicit list of sine coefficients a[k] of sin((2k+1) theta) (ring elements); default eps (sin + b sin3)"""
        self.a_num = a; self.b_den = b_den; self.P = 2 * b_den // math.gcd(a, 2)
        self.H = {}; self.obstruction = {}; self.sigma = {}; self.Rk = {}; self._provisional = False
        if f1 is None: f1 = [ring.scalar(eps), ring.scalar(eps) * b]
        super().__init__(ring, str(fmpq(b_den, b_den - a)), f1, delta=fmpq(a, b_den))

    def jres(self, n):
        """free stream index j at a resonant order n (None if n is not resonant)"""
        if (n * self.a_num) % (2 * self.b_den) != 0: return None
        j = n * self.a_num // (2 * self.b_den) - 1
        return j if j >= 1 else None

    def poisson(self, a, n):
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
                if self._provisional: b[j] = R.zero; continue
                if not num.contains(0): raise ArithmeticError(f'order {n}, j={j}: obstruction certified NONZERO: {num.str(20, radius=True)}')
                self.obstruction[n] = {'j': j, 'num_mid': R.to_float(num), 'num_rad': R.rad(num), 'log10_num_rad': R.log10abs(arb(num.rad())) if num.rad() != 0 else -float('inf')}
                res.append({'j': j, 'status': 'tuned (ball contains zero)', 'num_zero': True, 'num': R.to_float(num), 'num_str': R.to_str(num)})
                b[j] = self.H.get(n, R.zero); continue
            b[j] = num / den; d = R.absf(den)
            if not R.is_zero(num) and (mind is None or d < mind): mind = d; minden_j = j
        out = {'min_active_den': mind, 'min_active_den_j': minden_j}
        if res: out['resonances'] = res
        return b, out

    def T(self, i, j, g, f):
        P1, P2 = self.products(g, f); pi1 = self.p(i) + 1; pj = self.p(j)
        return [pi1 * x - pj * y for x, y in zip(P1, P2)]

    @staticmethod
    def add(u, v, scale=None):
        z = (u[0] if u else v[0]) * 0; L = max(len(u), len(v)); out = []
        for m in range(L):
            x = u[m] if m < len(u) else z; y = v[m] if m < len(v) else z
            out.append(x + (y if scale is None else scale * y))
        return out

    def responses(self, n):
        R = self.R; P = self.P; lam = lambda m: (m - 1) * (self.c_l - 1)
        j = self.jres(n); e = [R.zero] * (j + 1); e[j] = R.scalar(1)
        jt = self.jres(n + P); target = jt - 1
        phi = {}; Pphi = {}
        for i in range(1, P + 1):
            acc = self.T(n, i, e, self.f[i])
            for m in range(1, i):
                acc = self.add(acc, self.T(n + m, i - m, Pphi[m], self.f[i - m]))
                acc = self.add(acc, self.T(i - m, n + m, self.g[i - m], phi[m]))
            phi[i] = [x / lam(n + i) for x in acc]
            if i < P: Pphi[i], _ = self.poisson(phi[i], n + i)
        sigma = phi[P][target] if target < len(phi[P]) else R.zero
        return phi, sigma, target

    def run_tuned(self, N, log=None, ckpt=None, ckpt_every=30):
        R = self.R; P = self.P; emitted = set()
        def emit(n):
            st = self.stats[n]; row = _logrow(st)
            if n in self.H: row['H'] = R.to_float(self.H[n]); row['H_str'] = self.H[n].str(30, radius=True); row['log10_absH'] = R.log10abs(self.H[n]); row['H_mode_j'] = self.jres(n)
            if n in self.obstruction: row['obstruction'] = self.obstruction[n]
            if n in self.sigma: row['sigma_k'] = R.to_float(self.sigma[n]); row['sigma_str'] = self.sigma[n].str(20, radius=True); row['R_k'] = R.to_float(self.Rk[n])
            if log: print(json.dumps(row), file=log, flush=True)
            emitted.add(n)
        def resonant_open(n): return self.jres(n) is not None and n not in self.H
        while max(self.f) < N:
            n = max(self.f)
            if not resonant_open(n):
                n = self.step()
                if not resonant_open(n): emit(n)
                if ckpt and n % ckpt_every == 0: self.save(ckpt); self.save_H(ckpt)
                continue
            t0 = time.time()
            phi, sigma, target = self.responses(n); self.sigma[n] = sigma
            self._provisional = True
            for _ in range(P): self.step()
            self._provisional = False
            f0 = self.f[n + P]; Rk = f0[target] if target < len(f0) else R.zero; self.Rk[n] = Rk
            if sigma.contains(0): raise ArithmeticError(f'sigma at n={n} ball contains zero: {sigma.str(20, radius=True)}')
            H = -Rk / sigma; self.H[n] = H
            for i in range(1, P + 1): self.f[n + i] = self.add(self.f[n + i], phi[i], H)
            gn = list(self.g[n]); j = self.jres(n)
            while len(gn) < j + 1: gn.append(R.zero)
            gn[j] = H; self.g[n] = gn
            for m in range(n + 1, n + P + 1):
                self.g[m], st = self.poisson(self.f[m], m); self.stats[m].update(st); self._fill_stats(m)
            self._fill_stats(n); self.stats[n]['time_block'] = time.time() - t0
            for m in range(n, n + P): emit(m)
            if ckpt and any((n + i) % ckpt_every == 0 for i in range(P + 1)): self.save(ckpt); self.save_H(ckpt)
        for m in sorted(self.f):
            if m not in emitted and m > 1: emit(m)
        if ckpt: self.save(ckpt); self.save_H(ckpt)

    def save_H(self, ckpt):
        d = {'delta': f'{self.a_num}/{self.b_den}', 'period': self.P, 'H': {str(n): {'mid': self.R.to_float(h), 'str': h.str(40, radius=True), 'mode_j': self.jres(n)} for n, h in self.H.items()},
             'sigma': {str(n): self.sigma[n].str(30, radius=True) for n in self.sigma},
             'R_k': {str(n): self.Rk[n].str(30, radius=True) for n in self.Rk},
             'obstruction': {str(n): v for n, v in self.obstruction.items()}}
        json.dump(d, open(ckpt.replace('.pkl', '_H.json'), 'w'), indent=0)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--tag', required=True); ap.add_argument('--a', type=int, required=True); ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--f1-single', type=int, default=0, help='leading profile eps sin(M theta) for this odd M (lead request 18:03Z); then --poly-coeffs and --root-guess are ignored')
    ap.add_argument('--poly-coeffs', required=False, default='', help='ascending integer coefficients of the first obstruction polynomial, comma separated, or @file.json with key coeffs_ascending')
    ap.add_argument('--root-guess', required=False, default='0'); ap.add_argument('--prec', type=int, default=1024); ap.add_argument('--N', type=int, default=60)
    ap.add_argument('--eps', default='1'); ap.add_argument('--ckpt-every', type=int, default=30)
    args = ap.parse_args(); LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    R = make_ring('arb', args.prec)
    if args.f1_single:
        M = args.f1_single; assert M % 2 == 1 and M >= 1
        f1 = [R.zero] * ((M - 1) // 2) + [R.scalar(args.eps)]; b = None; f1_desc = f'eps sin({M} theta), eps = {args.eps}'; b_desc = 'none (single harmonic)'
    else:
        if args.poly_coeffs.startswith('@'): coeffs = [int(x) for x in json.load(open(args.poly_coeffs[1:]))['coeffs_ascending']]
        else: coeffs = [int(x) for x in args.poly_coeffs.split(',')]
        b = root_enclosure_poly(fmpz_poly(coeffs), args.root_guess, args.prec); f1 = None
        f1_desc = f'eps (sin + b sin3), eps = {args.eps}, root near {args.root_guess}'; b_desc = b.str(60, radius=True)
    T = TunedGeneral(R, args.a, args.b, b, args.eps, f1=f1); ck = os.path.join(LANE, 'ckpt', args.tag + '.pkl')
    with open(os.path.join(LANE, 'logs', args.tag + '.jsonl'), 'w') as log:
        print(json.dumps({'tag': args.tag, 'ring': 'arb', 'prec': args.prec, 'delta': f'{args.a}/{args.b}', 'period': T.P, 'c_l': str(fmpq(args.b, args.b - args.a)),
                          'f1': f1_desc, 'b_enclosure': b_desc, 'N_target': args.N, 'tuned': True}), file=log, flush=True)
        print(json.dumps(_logrow(T.stats[1])), file=log, flush=True)
        T.run_tuned(args.N, log=log, ckpt=ck, ckpt_every=args.ckpt_every)
        print(json.dumps({'done': True, 'N': max(T.f)}), file=log, flush=True)
