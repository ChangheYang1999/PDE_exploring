"""Tuned pure series at delta = 2/Q (c = Q/(Q-2)), lead's Theorem T_Q (theory 12.5), generalizing tuned_c3.py (Q = 3):
f_1 = eps (sin theta + b sin 3theta) with b a real root of the first obstruction polynomial P_Q (Q = 3: P6, Q = 4: the degree-8 P of the lead's
tq_cert_Q4.out); resonant orders n = Qk (k >= 2) with free stream coefficient H_n of sin((2k-2) theta); H_n = -R_k/sigma_k where R_k is the
obstruction a_(n+Q, k-1) of the provisional (H_n = 0) orders and sigma_k the coefficient of sin((2k-1) theta) in the linear response phi_Q:
lambda_(n+i) phi_i = T_(n,i)(e_k, f_i) + sum_(m=1)^(i-1) [T_(n+m, i-m)(Pi_(n+m) phi_m, f_(i-m)) + T_(i-m, n+m)(g_(i-m), phi_m)], i = 1..Q.
Ball arithmetic; every tuned obstruction must be a ball containing zero.
usage: tuned_cQ.py --tag TAG --Q 4 --root-guess 0.6267874990781 --prec 1024 --N 300 [--eps 1] [--ckpt-every 30]"""
import sys, os, json, time, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
from flint import fmpz_poly, fmpz, fmpq, arb, ctx
from ffcore import _logrow, FarField, make_ring
from tuned_c3 import arb_eval, P6

POLY = {3: P6,
        5: fmpz_poly([-1036676038330181003765585261650053069657146197729728, 97176244422540629170104488884810858372869293931198250, -4344130168318349401263307316559240742908620386872136305, 118874904900035160148867780512049861401592105677077910390, -2086215849912557527315714202774550542928956587817722068720, 22556717972979665502310346687917491391189763392765688910834, -134304016016634804824511865431649179461532417596130819804810, 343942685552121005702979630343741421684883240029584998839700, 96549878125639096091461816487189803701669872496369810145860, -1849582665856514197710510679282827418757876087988604188044760, 2053735073663219060083079169180600478346016799964425568590080]),   # verifier's topic 130 (period five), ascending coefficients
        4: fmpz_poly([-17775107835680457282107307, 1142367926478965394242628352, -28547059979232840548373570964, 357367348597738878814260316240,
                      -2135646950051033144752986241898, 2588931390935970663652418519632, 25822813920036852456341976404620,
                      -92969766411149135035547416328960, 82668272572218361620942808786146])}

def root_enclosure_poly(P, guess, prec):
    ctx.prec = prec; dP = P.derivative(); x = arb(guess)
    for _ in range(14):
        m = x.mid(); x = arb(m) - arb_eval(P, arb(m)) / arb_eval(dP, arb(m))
    for e in range(int(prec * 0.3), 10, -5):
        X = arb(x.mid(), arb(2) ** (-e)); m = X.mid()
        NX = arb(m) - arb_eval(P, arb(m)) / arb_eval(dP, X)
        if X.contains(NX): return NX
    raise ArithmeticError('root enclosure failed')

class TunedQ(FarField):
    def __init__(self, ring, Q, b, eps='1'):
        self.Q = Q; self.H = {}; self.obstruction = {}; self.sigma = {}; self.Rk = {}; self._provisional = False
        super().__init__(ring, str(fmpq(Q, Q - 2)), [ring.scalar(eps), ring.scalar(eps) * b], delta=fmpq(2, Q))

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

    def responses(self, k):
        R = self.R; Q = self.Q; n = Q * k; lam = lambda m: (m - 1) * (self.c_l - 1)
        ek = [R.zero] * k; ek[k - 1] = R.scalar(1)
        phi = {}; Pphi = {}
        for i in range(1, Q + 1):
            acc = self.T(n, i, ek, self.f[i])
            for m in range(1, i):
                acc = self.add(acc, self.T(n + m, i - m, Pphi[m], self.f[i - m]))
                acc = self.add(acc, self.T(i - m, n + m, self.g[i - m], phi[m]))
            phi[i] = [x / lam(n + i) for x in acc]
            if i < Q: Pphi[i], _ = self.poisson(phi[i], n + i)
        sigma = phi[Q][k - 1] if k - 1 < len(phi[Q]) else R.zero
        return phi, sigma

    def run_tuned(self, N, log=None, ckpt=None, ckpt_every=30):
        R = self.R; Q = self.Q; emitted = set()
        def emit(n):
            st = self.stats[n]; row = _logrow(st)
            if n in self.H: row['H'] = R.to_float(self.H[n]); row['H_str'] = self.H[n].str(30, radius=True); row['log10_absH'] = R.log10abs(self.H[n])
            if n in self.obstruction: row['obstruction'] = self.obstruction[n]
            if n in self.sigma: row['sigma_k'] = R.to_float(self.sigma[n]); row['sigma_str'] = self.sigma[n].str(20, radius=True); row['R_k'] = R.to_float(self.Rk[n])
            if log: print(json.dumps(row), file=log, flush=True)
            emitted.add(n)
        def resonant_open(n): return n % Q == 0 and n >= 2 * Q and n not in self.H
        while max(self.f) < N:
            n = max(self.f)
            if not resonant_open(n):
                n = self.step()
                if not resonant_open(n): emit(n)
                if ckpt and n % ckpt_every == 0: self.save(ckpt); self.save_H(ckpt)
                continue
            k = n // Q; t0 = time.time()
            phi, sigma = self.responses(k); self.sigma[n] = sigma
            self._provisional = True
            for _ in range(Q): self.step()
            self._provisional = False
            f0 = self.f[n + Q]; Rk = f0[k - 1] if k - 1 < len(f0) else R.zero; self.Rk[n] = Rk
            if sigma.contains(0): raise ArithmeticError(f'sigma_{k} ball contains zero: {sigma.str(20, radius=True)}')
            H = -Rk / sigma; self.H[n] = H
            for i in range(1, Q + 1): self.f[n + i] = self.add(self.f[n + i], phi[i], H)
            gn = list(self.g[n])
            while len(gn) < k: gn.append(R.zero)
            gn[k - 1] = H; self.g[n] = gn
            for m in range(n + 1, n + Q + 1):
                self.g[m], st = self.poisson(self.f[m], m); self.stats[m].update(st); self._fill_stats(m)
            self._fill_stats(n); self.stats[n]['time_block'] = time.time() - t0
            for m in range(n, n + Q): emit(m)
            if ckpt and any((n + i) % ckpt_every == 0 for i in range(Q + 1)): self.save(ckpt); self.save_H(ckpt)
        for m in sorted(self.f):
            if m not in emitted and m > 1: emit(m)
        if ckpt: self.save(ckpt); self.save_H(ckpt)

    def save_H(self, ckpt):
        d = {'Q': self.Q, 'H': {str(n): {'mid': self.R.to_float(h), 'str': h.str(40, radius=True)} for n, h in self.H.items()},
             'sigma': {str(n): self.sigma[n].str(30, radius=True) for n in self.sigma},
             'R_k': {str(n): self.Rk[n].str(30, radius=True) for n in self.Rk},
             'obstruction': {str(n): v for n, v in self.obstruction.items()}}
        json.dump(d, open(ckpt.replace('.pkl', '_H.json'), 'w'), indent=0)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--tag', required=True); ap.add_argument('--Q', type=int, required=True)
    ap.add_argument('--root-guess', required=True); ap.add_argument('--prec', type=int, default=1024); ap.add_argument('--N', type=int, default=60)
    ap.add_argument('--eps', default='1'); ap.add_argument('--ckpt-every', type=int, default=30)
    args = ap.parse_args(); LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    R = make_ring('arb', args.prec); b = root_enclosure_poly(POLY[args.Q], args.root_guess, args.prec)
    T = TunedQ(R, args.Q, b, args.eps); ck = os.path.join(LANE, 'ckpt', args.tag + '.pkl')
    with open(os.path.join(LANE, 'logs', args.tag + '.jsonl'), 'w') as log:
        print(json.dumps({'tag': args.tag, 'ring': 'arb', 'prec': args.prec, 'Q': args.Q, 'c_l': str(fmpq(args.Q, args.Q - 2)), 'delta': f'2/{args.Q}',
                          'f1': f'eps (sin + b sin3), eps = {args.eps}, root near {args.root_guess}', 'b_enclosure': b.str(60, radius=True), 'N_target': args.N, 'tuned': True}), file=log, flush=True)
        print(json.dumps(_logrow(T.stats[1])), file=log, flush=True)
        T.run_tuned(args.N, log=log, ckpt=ck, ckpt_every=args.ckpt_every)
        print(json.dumps({'done': True, 'N': max(T.f)}), file=log, flush=True)
