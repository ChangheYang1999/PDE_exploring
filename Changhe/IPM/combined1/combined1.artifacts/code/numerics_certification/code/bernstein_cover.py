"""Whole-plane pointwise matrix certificates by directed Bernstein covers in (t, z) = (r^2/(1+r^2), cos 2 theta) (lane c1-n3).

Method (as A2 S1_NUMERICAL_CERTIFICATES section 2, P95/P99): every fourth derivative of the canonical potential is
sum_j w^(j+1) P_j(t, z) with w = (1-t)^(delta/2), P_j exact rational bivariate polynomials (chi31, chi13 carry a factor
sin 2 theta = +-(1-z^2)^(1/2)). On a cell [tl,th] x [zl,zh] the range of a polynomial lies in the hull of its Bernstein
coefficients, and the powers of w are enclosed by a Bernstein hull over [w(th), w(tl)]; the smallest eigenvalue of a
symmetric 2x2 matrix [[a, q],[q, b]] is bounded below by max((a+b-sqrt((a-b)^2+4C^2))/2, min(a,b)-C), C >= |q|.
Cells are split (t or z, whichever helps more) until the lower bound is nonnegative; a COMPLETE cover is an exact binary
partition of [0,1] x [-1,1] including t = 0 (origin) and t = 1 (infinity). Parity makes the quadrant bound global.

Kinds: 'A' with target tau: A + tau I >= 0, i.e. theta = sup (|grad rho| - rho_y)/2 <= tau (A = [[rho_y, -rho_x/2], [-rho_x/2, 0]]).
       'B1' with target m: M_1 = I - sym DU + A >= m I (hypothesis (B4) with m = 9/10).
       'M' with target m: M = (2c+1) I + sym DU + A >= m I (hypothesis (B1) with m = 19/5).
The record of the bivariate polynomials is built here from the exact canonical coefficients (my own chi_compact rule and
Chebyshev conversion); no code is imported from the read-only sources.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from functools import lru_cache
from datetime import datetime, timezone
from hashlib import sha256
import sys, json, time, argparse
from flint import arb, arb_mat, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E

def aa(v):
    q = F(v); return arb(q.numerator) / q.denominator

def chebyshev(n, kind='T'):
    seq = [[F(1)], [F(0), F(1 if kind == 'T' else 2)]]
    while len(seq) <= n:
        nxt = [F(0)] * (len(seq[-1]) + 1)
        for k, v in enumerate(seq[-1]): nxt[k + 1] += 2 * v
        for k, v in enumerate(seq[-2]): nxt[k] -= v
        seq.append(nxt)
    return seq[n]

def build_record(source):
    """Bivariate polynomials {label_j: {(i,k): F}} for chi22 (xxyy), chi04 (yyyy), chi31 (xxxy), chi13 (xyyy), per branch j."""
    c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    J = meta['max_j'] + 1
    polys = {}
    for label, nx in [('chi22', 2), ('chi04', 0), ('chi31', 3), ('chi13', 1)]:
        D = E.chi_compact(A, c, 4, nx)           # keys (ell = j+1, kind, n) -> poly in t (no r factor for degree 4)
        for j in range(J):
            P = {}
            for (ell, kind, n), p in D.items():
                if ell != j + 1: continue
                assert n % 2 == 0
                assert kind == ('s' if label in ('chi31', 'chi13') else 'c'), (label, kind, n)
                C = chebyshev(n // 2 - 1, 'U') if kind == 's' else chebyshev(n // 2)
                for i, v in enumerate(p.coeffs()):
                    v = F(int(v.p), int(v.q))
                    if not v: continue
                    for zdeg, cz in enumerate(C):
                        if cz: P[(i, zdeg)] = P.get((i, zdeg), F(0)) + v * cz
            polys[f'{label}_{j}'] = {k: v for k, v in P.items() if v}
    return {'cl': str(c), 'delta': str(delta), 'branches': J, 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'polynomials': polys}

def plus(*terms):
    D = {}
    for factor, P in terms:
        for k, v in P.items(): D[k] = D.get(k, F(0)) + factor * v
    return {k: v for k, v in D.items() if v}

@lru_cache(None)
def trans(n, low, high):
    lo, hi = F(low), F(high)
    T = arb_mat([[aa(comb(k, i) * lo ** (k - i) * (hi - lo) ** i) if i <= k else arb(0) for k in range(n + 1)] for i in range(n + 1)])
    G = arb_mat([[aa(F(comb(i, k), comb(n, k))) if k <= i else arb(0) for k in range(n + 1)] for i in range(n + 1)])
    return G * T

def halves(n):
    L = arb_mat([[aa(F(comb(i, k), 2 ** i)) if k <= i else arb(0) for k in range(n + 1)] for i in range(n + 1)])
    R = arb_mat([[aa(F(comb(n - i, k - i), 2 ** (n - i))) if k >= i else arb(0) for k in range(n + 1)] for i in range(n + 1)])
    return L, R

def prepare(rec, kind, target):
    c = F(rec['cl']); J = rec['branches']
    P = {key: {(i, k): v for (i, k), v in v.items()} for key, v in rec['polynomials'].items()}
    S = {}
    if kind == 'A': scalar = {(0, 0): target}                     # A + target I
    elif kind == 'B1': scalar = {(0, 0): 1 - target}               # I - sym DU + A - target I
    elif kind == 'M': scalar = {(0, 0): 2 * c + 1 - target}        # (2c+1) I + sym DU + A - target I
    else: raise ValueError(kind)
    for lab in ['a', 'b', 'q']: S[lab, 0] = scalar if lab != 'q' else {}
    for j in range(J):
        p22, p04, p31, p13 = (P[f'{l}_{j}'] for l in ['chi22', 'chi04', 'chi31', 'chi13'])
        # rho_y = -(p04 + p22), -rho_x/2 = (p13 + p31)/2, sym DU = [[-p22, (p31 - p13)/2], [(p31 - p13)/2, p22]]
        if kind == 'A': a = plus((-1, p22), (-1, p04)); b = {}; q = plus((F(1, 2), p31), (F(1, 2), p13))
        elif kind == 'B1': a = plus((-1, p04)); b = plus((-1, p22)); q = p13
        else: a = plus((-2, p22), (-1, p04)); b = p22; q = p31
        for lab, p in [('a', a), ('b', b), ('q', q)]: S[lab, j + 1] = p
    nt = max(i for p in S.values() for i, k in p); nz = max(k for p in S.values() for i, k in p)
    T = trans(nt, '0', '1'); Z = trans(nz, '-1', '1').transpose(); B = {}
    for key, p in S.items():
        mat = arb_mat(nt + 1, nz + 1)
        for (i, k), v in p.items(): mat[i, k] = aa(v)
        B[key] = T * mat * Z
    return S, B, nt, nz, J

def bound(B, J, tl, th, zl, zh, delta):
    wl = (1 - aa(th)) ** aa(delta / 2); wh = (1 - aa(tl)) ** aa(delta / 2)
    N = J
    W = arb_mat([[sum((aa(F(comb(n, k) * comb(i, k), comb(N, k))) * wl ** (n - k) * (wh - wl) ** k for k in range(min(n, i) + 1)), arb(0)) for n in range(N + 1)] for i in range(N + 1)])
    rr = {}
    for label in ['a', 'b', 'q']:
        vals = (W * arb_mat([B[label, j].entries() for j in range(N + 1)])).entries(); lo = vals[0]; hi = vals[0]
        for v in vals[1:]: lo = lo.min(v); hi = hi.max(v)
        rr[label] = (lo.lower(), hi.upper())
    al, bl = rr['a'][0], rr['b'][0]; lo, hi = rr['q']
    si = arb(1) if zl <= 0 <= zh else (1 - aa(min(abs(zl), abs(zh))) ** 2).sqrt(); C = abs(lo).max(abs(hi)) * si
    return ((al + bl - ((al - bl) ** 2 + 4 * C * C).sqrt()) / 2).max(al.min(bl) - C)

def split(B, axis, L, R):
    if axis == 't': return {k: L * v for k, v in B.items()}, {k: R * v for k, v in B.items()}
    return {k: v * L.transpose() for k, v in B.items()}, {k: v * R.transpose() for k, v in B.items()}

def run(source, ID, kind, target, outdir, seconds=3000, maxdepth=60, prec=512, resume=False):
    ctx.prec = prec; start = time.monotonic(); outdir = Path(outdir)
    rec = build_record(source); delta = F(rec['delta']); target = F(target)
    S, B, nt, nz, J = prepare(rec, kind, target)
    print(f'{ID} {kind} target {target}: record built, degrees t {nt}, z {nz}, branches {J}, {time.monotonic()-start:.1f}s', flush=True)
    Lt, Rt = halves(nt); Lz, Rz = halves(nz)
    stack = [(B, F(0), F(1), F(-1), F(1), '', None)]; good = []; bad = []; n = 0; worst = arb(10); prev_seconds = 0; prev_sha = None
    outfile = outdir / f'{ID}_cover_{kind}_{str(target).replace("/", "over")}.json'
    if resume and outfile.exists():
        prior = json.loads(outfile.read_text())
        assert prior['status'] == 'INCOMPLETE' and prior['canonical_sha256'] == rec['canonical_sha256'] and prior['kind'] == kind and F(prior['target']) == target
        prev_sha = sha256(outfile.read_bytes()).hexdigest(); prev_seconds = prior.get('cumulative_seconds', prior['seconds'])
        good = prior['leaves']; bad = prior['failed']; n = prior['processed']; worst = arb(prior['worst_leaf_lower_bound']); stack = []
        for path in prior['pending_paths']:
            bb = B; tl, th, zl, zh = F(0), F(1), F(-1), F(1)
            for letter in path:
                axis = letter.lower(); l, r = split(bb, axis, Lt if axis == 't' else Lz, Rt if axis == 't' else Rz)
                bb = l if letter.islower() else r
                if axis == 't':
                    mid = (tl + th) / 2
                    if letter.islower(): th = mid
                    else: tl = mid
                else:
                    mid = (zl + zh) / 2
                    if letter.islower(): zh = mid
                    else: zl = mid
            stack.append((bb, tl, th, zl, zh, path, None))
        print(f'resumed: {len(good)} accepted, {len(stack)} pending, {n} processed, {prev_seconds:.0f}s before', flush=True)
    while stack and time.monotonic() - start < seconds:
        Bc, tl, th, zl, zh, path, cached = stack.pop(); n += 1
        low = cached if cached is not None else bound(Bc, J, tl, th, zl, zh, delta)
        if low >= 0:
            good.append({'path': path, 't': [str(tl), str(th)], 'z': [str(zl), str(zh)], 'lower_bound': low.str(40)}); worst = worst.min(low)
        elif len(path) >= maxdepth: bad.append({'path': path, 'lower': low.str(40)})
        else:
            choices = []
            for axis in ['t', 'z']:
                l, r = split(Bc, axis, Lt if axis == 't' else Lz, Rt if axis == 't' else Rz)
                if axis == 't': mid = (tl + th) / 2; nodes = [(l, tl, mid, zl, zh, path + 't'), (r, mid, th, zl, zh, path + 'T')]
                else: mid = (zl + zh) / 2; nodes = [(l, tl, th, zl, mid, path + 'z'), (r, tl, th, mid, zh, path + 'Z')]
                lows = [bound(v[0], J, v[1], v[2], v[3], v[4], delta) for v in nodes]
                score = sum(min(float(v), 0.0) for v in lows); choices.append((score, [node + (ll,) for node, ll in zip(nodes, lows)]))
            stack.extend(reversed(max(choices, key=lambda x: x[0])[1]))
        if n % 20 == 0: print(f'  processed {n} accepted {len(good)} pending {len(stack)} depth {len(path)} {time.monotonic()-start:.0f}s', flush=True)
    status = 'COMPLETE' if not stack and not bad else 'INCOMPLETE'
    out = {'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'id': ID, 'kind': kind, 'target': str(target),
           'statement': {'A': f'A + ({target}) I >= 0 on R^2, i.e. theta = sup (|grad rho| - rho_y)/2 <= {target}',
                         'B1': f'M_1 = I - sym DU + A >= ({target}) I on R^2', 'M': f'M = (2c+1) I + sym DU + A >= ({target}) I on R^2'}[kind],
           'status': status, 'accepted_leaves': len(good), 'leaves': good, 'failed': bad, 'pending_paths': [v[5] for v in stack],
           'processed': n, 'worst_leaf_lower_bound': worst.str(40), 'precision_bits': prec, 'degrees': [nt, nz], 'branches': J,
           'source_sha256': rec['source_sha256'], 'canonical_sha256': rec['canonical_sha256'],
           'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(), 'seconds': time.monotonic() - start,
           'cumulative_seconds': prev_seconds + time.monotonic() - start, 'previous_record_sha256': prev_sha}
    outfile.write_text(json.dumps(out, indent=1) + '\n')
    print(f'{ID} {kind} {target}: {status}, {len(good)} leaves, worst lower bound {worst.str(10)}, {time.monotonic()-start:.0f}s', flush=True)
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('id'); ap.add_argument('kind', choices=['A', 'B1', 'M'])
    ap.add_argument('target'); ap.add_argument('outdir'); ap.add_argument('--seconds', type=int, default=3000); ap.add_argument('--resume', action='store_true')
    a = ap.parse_args(); run(a.source, a.id, a.kind, a.target, a.outdir, a.seconds, resume=a.resume)
