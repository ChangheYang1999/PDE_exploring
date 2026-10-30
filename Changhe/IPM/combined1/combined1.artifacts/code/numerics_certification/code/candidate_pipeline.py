"""One exact residual assembly, all registered norms for one candidate (lane c1-n3, N3).

Order follows theory_v02 section 9 item 2: the cheap filters first, then the norms.
  1. NORM-T-WEAK-v1 (a = 0): I_k, A_k, B_k, C_k, H_k, m_k for a list of k (default 0..8 and 128); weak distance LB = max_k m_k.
  2. NORM-T-WL2-v1: ||(1+r^2)^(-a/2) F||_2 for a in a list (default 1/2, 3/4, 1, 6/5).
  3. NORM-T-WLAP-v1: N_a(F) = ||(1+r^2)^((2-a)/2) Delta F||_2 on a cover of a.
  4. NORM-A2-E2 components G0, rF, G1, P2 (and Pw1, D2, rD2), the E_2 assembly; Q3 only with --q3 (slow).
Everything is an exact Beta integral (rational times pi) of the exact compactified polynomials; square roots in 512-bit balls.
Records (same formats as wlap_norms.py and e2norms.py, so assemble_norms.py works unchanged):
  <out>/<ID>_wlap.json, <out>/<ID>_e2norms.json, <out>/<ID>_pipeline.log, and the F cache <out>/<stem>_Fpoly_cache.json for hminus1.py.
Usage: candidate_pipeline.py <source.json> <ID> <outdir> [--k 0,1,...] [--a 0,1/5,...] [--wl2 1/2,3/4,1,6/5] [--q3] [--series 56]
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib, argparse
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, hminus1 as H
from e2norms import fq, aq, Z, OM, ONE

def ell_to_beta(D, delta): return H.normalize(H.from_ell(D, delta))
def scale_poly(D, W): return {k: p * W for k, p in D.items()}
def S(a, b): return Q(a) ** a * Q(b) ** b / Q(a + b) ** (a + b)
def now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')

def integ(p, b, cache, exact, shift=0):
    """int_0^1 t^shift p(t) (1-t)^b dt: exact rational (E.integral; small shifts only) or a 512-bit ball.
    Ball path: the first Beta moment B(shift+1, b+1) = Gamma(shift+1) Gamma(b+1) / Gamma(shift+b+2) is evaluated directly (rigorous
    arb gamma, any shift), the next deg(p) moments by the recursion bet[j+1] = bet[j] (j+1)/(b+j+2). No dense shifted polynomial."""
    if exact: return E.integral(p * Z ** shift if shift else p, b, cache)
    key = ('ball', b, shift)
    bb = aq(b)
    if key not in cache:
        s0 = arb(shift + 1)
        cache[key] = [(s0.gamma() * (bb + 1).gamma() / (s0 + bb + 1).gamma())]
    bet = cache[key]; need = p.degree() + 1
    while len(bet) < need:
        j = shift + len(bet) - 1; bet.append(bet[-1] * (j + 1) / (bb + j + 2))
    return sum((aq(Q(str(c))) * bet[k] for k, c in enumerate(p.coeffs()) if c), arb(0))

def normB_shift(D, d, a_shift, t_power, exact):
    """||D^d-object||_2^2 / pi with weight (1-t)^a_shift t^t_power (H.normB with a switchable integrator). None if divergent.
    Products grouped by exponent, one integration per group."""
    cache = {}; groups = {}
    comps = D if isinstance(D, list) else [(1, D)]
    for mult, comp in comps:
        modes = {}
        for (beta, kind, n), p in comp.items():
            q, p2 = H.endpoint(p); modes.setdefault((kind, n), []).append((beta, q, p2))
        for (kind, n), rows in modes.items():
            for i, (beta, q, p) in enumerate(rows):
                for j in range(i, len(rows)):
                    beta2, q2, p2 = rows[j]
                    b = Q(d - 3) + beta + beta2 + q + q2 + a_shift
                    if b <= -1: return None
                    factor = Q(mult) * (2 if (kind == 'c' and n == 0) else 1) * (1 if i == j else 2) * Q(1, 2)
                    v = p * p2 * fq(factor)
                    if d % 2 == 0: v *= Z
                    groups[b] = groups.get(b, fmpq_poly([])) + v
    total = fmpq(0) if exact else arb(0)
    for b, v in groups.items(): total += integ(v, b, cache, exact, t_power)   # the t^t_power shift is applied inside the integrator
    return total

def pair_shift(F, Wpoly, k, exact):
    """int F phi_k dX / pi for phi_k = y t^k u0^2 (F degree-0 form), with the t^k shift applied after the product."""
    groups = {}; cache = {}
    for (beta, kind, n), p in F.items():
        if kind != 's' or n != 1: continue
        q1, p1 = H.endpoint(p)
        b = Q(-3) + beta + q1 + 2
        if b <= -1: return None
        groups[b] = groups.get(b, fmpq_poly([])) + p1 * Z * fq(Q(1, 2))
    total = fmpq(0) if exact else arb(0)
    for b, v in groups.items(): total += integ(v, b, cache, exact, k)
    return total

def weak_stage(F, fields, c, delta, k_list, rec, log, save, exact_max_degree=1500):
    """NORM-T-WEAK-v1 at a = 0 (theory_v02 section 2; T4-064 AUDITED): for phi_k = y t^k u0^2.
    Exact rationals while 2k plus the field degrees stay below exact_max_degree, 512-bit balls beyond (the Beta-moment cache
    of exact rationals would need tens of GB at k of order 2000); both are rigorous."""
    u1 = ell_to_beta(fields['u1'], delta); u2 = ell_to_beta(fields['u2'], delta)          # degree-3 form r (1-t)^beta P trig
    rx = ell_to_beta(fields['rho_x'], delta); ry = ell_to_beta(fields['rho_y'], delta)   # degree-4 form (1-t)^beta P trig (no r)
    maxdeg = max([p.degree() for D in (F, u1, u2, rx, ry) for p in D.values()] + [0])
    for k in k_list:
        t0 = time.monotonic(); exact = (2 * k + 2 * maxdeg + 8) <= exact_max_degree
        Lk = fq(3 * c + 1) * ONE + fq(2 * c * k) * OM - fq(4 * c) * Z    # 3c + 1 + 2ck u0 - 4ct
        Gk = ONE + fq(2 * k) * OM + 4 * Z                               # 1 + 2k u0 + 4t
        Ik = pair_shift(F, None, k, exact)                                                   # int F phi_k / pi
        Ak2 = normB_shift({(Q(0), 's', 1): Lk}, 0, Q(4), 2 * k, exact)                        # ||phi_k L_k||_2^2 / pi: W^2 = t^(2k) (1-t)^4
        Bk2 = normB_shift([(1, scale_poly(u1, Gk)), (1, scale_poly(u2, Gk))], 0, Q(4), 2 * k, exact)   # ||t^k u0^2 G_k u||_2^2 / pi
        Ck2 = normB_shift([(1, rx), (1, ry)], 1, Q(3), 2 * k + 1, exact)                      # ||r t^k u0^2 D rho||_2^2 / pi (r^2 = t/(1-t))
        if k == 0: Hk = Q(1); Hk_a = arb(1)
        elif k <= 4096: Hk = S(k, 2) + 2 * k * S(k, 3) + 4 * S(k + 1, 2); Hk_a = aq(Hk)
        else:                                                           # rigorous ball of H_k (exact k^k rationals are too large)
            def Sa(a_, b_): return (arb(a_) * arb(a_).log() + arb(b_) * arb(b_).log() - arb(a_ + b_) * arb(a_ + b_).log()).exp()
            Hk_a = Sa(k, 2) + 2 * k * Sa(k, 3) + 4 * Sa(k + 1, 2); Hk = None
        if None in (Ik, Ak2, Bk2, Ck2):
            rec['WEAK_a0'][str(k)] = {'status': 'divergent'}; log(f'k={k}: divergent'); save(); continue
        conv = (lambda v: aq(Q(str(v)))) if exact else (lambda v: v)
        Isigned = arb.pi() * conv(Ik); I = abs(Isigned); Ak = (arb.pi() * conv(Ak2)).sqrt(); Bk = (arb.pi() * conv(Bk2)).sqrt(); Ck = (arb.pi() * conv(Ck2)).sqrt()
        Dk = Ak + Bk + Ck
        m = 2 * I / (Dk + (Dk ** 2 + 4 * Hk_a * I).sqrt())
        rec['WEAK_a0'][str(k)] = {'arithmetic': 'exact rational Beta integrals' if exact else '512-bit ball Beta moments',
                                  'I_k_signed_over_pi_exact': str(Ik) if exact else None, 'I_k_signed': Isigned.str(30), 'I_k_LB': str(I.lower()),
                                  'A_k_UB': str(Ak.upper()), 'B_k_UB': str(Bk.upper()), 'C_k_UB': str(Ck.upper()), 'H_k': str(Hk) if Hk is not None else str(Hk_a.upper()), 'm_k_LB': str(m.lower()),
                                  'seconds': round(time.monotonic() - t0, 1)}
        log(f'k={k} ({"exact" if exact else "ball"}): I_k={I.str(12)} A_k={Ak.str(10)} B_k={Bk.str(10)} C_k={Ck.str(10)} H_k={float(Hk_a.mid()):.3e}  m_k >= {m.lower().str(12)}  ({time.monotonic()-t0:.0f}s)')
        ms = {kk: arb(v['m_k_LB']) for kk, v in rec['WEAK_a0'].items() if 'm_k_LB' in v}
        kbest = max(ms, key=lambda kk: float(ms[kk].lower())); rec['weak_distance_LB_a0'] = str(ms[kbest].lower()); rec['weak_distance_LB_a0_at_k'] = kbest
        save()
    log(f'weak L^2 distance (a = 0) >= {rec.get("weak_distance_LB_a0")} at k = {rec.get("weak_distance_LB_a0_at_k")}')

def wl2_stage(F, wl2_list, rec, log, save):
    for a in wl2_list:
        v = H.normB(F, 0, Q(a))                                         # ||w_a F||_2^2 / pi, w_a^2 = (1-t)^a
        n = (arb.pi() * aq(Q(str(v)))).sqrt() if v is not None else None
        rec['WL2'][str(a)] = {'LB': str(n.lower()), 'UB': str(n.upper())} if n is not None else {'status': 'INFINITE'}
        log(f'||w_a F||_2 a={a}: {rec["WL2"][str(a)]}'); save()

def wlap_stage(lap, a_list, rec, log, save):
    groups = {}; modes = {}
    for (beta, kind, n), p in lap.items():
        q, p2 = H.endpoint(p); modes.setdefault((kind, n), []).append((beta, q, p2))
    for (kind, n), rows in modes.items():
        for i, (beta, q, p) in enumerate(rows):
            for j in range(i, len(rows)):
                beta2, q2, p2 = rows[j]
                b = Q(2 - 3) + beta + beta2 + q + q2
                factor = (2 if (kind == 'c' and n == 0) else 1) * (1 if i == j else 2) * Q(1, 2)
                groups[b] = groups.get(b, fmpq_poly([])) + p * p2 * fq(factor) * Z
    for a in a_list:
        tot = fmpq(0); cache = {}; div = False
        for b, p in groups.items():
            bb = b + Q(a) - 2
            if bb <= -1: div = True; break
            tot += E.integral(p, bb, cache)
        if div: rec['WLAP'][str(a)] = {'status': 'INFINITE'}; log(f'N_a a={a}: INFINITE'); save(); continue
        n = (arb.pi() * aq(Q(str(tot)))).sqrt()
        rec['WLAP'][str(a)] = {'LB': str(n.lower()), 'UB': str(n.upper()), 'sq_over_pi_exact': str(tot)}
        log(f'N_a(F) a={a}: [{n.lower().str(25)}, {n.upper().str(25)}]'); save()

def run(source, ID, outdir, k_list, a_list, wl2_list, with_q3=False, N=56, prec=512):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    logf = open(outdir / f'{ID}_pipeline.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    code_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    log(f'[{now()}] {ID}: candidate pipeline; {meta} source_sha256={src_sha} canonical_sha256={can_sha} code_sha256={code_sha}')
    cached = outdir / (Path(source).stem + '_Fpoly_cache.json')
    raw = json.loads(cached.read_text()) if cached.exists() else None
    if raw and raw.get('canonical_sha256') == can_sha:
        # reuse the stored exact F (build_F_record.py / e2norms.py); fields from the chi derivatives, derivatives of F by E.diff
        F_ell = {(r['ell'], r['kind'], r['mode']): fmpq_poly([fmpq(v) for v in r['coeff']]) for r in raw['polynomials']['0,0']}
        log(f'loaded cached F record {cached} ({len(F_ell)} components)')
        from weak_from_cache import fields_from_source
        fields = fields_from_source(A, c, log)
        D = {(0, 0): F_ell}; max_order = 3 if with_q3 else 2
        for d in range(max_order):
            for nx in range(d + 2):
                D[d + 1, nx] = E.diff(D[d, 0], d, 'y', delta) if nx == 0 else E.diff(D[d, nx - 1], d, 'x', delta)
            log(f'derivative order {d+1} done ({time.monotonic()-t0:.0f}s)')
    else:
        D, fields = E.residual_polynomials(A, c, 3 if with_q3 else 2, log)
        try:
            poly = {'0,0': [{'ell': ell, 'kind': kind, 'mode': n, 'coeff': [str(v) for v in p.coeffs()]} for (ell, kind, n), p in sorted(D[0, 0].items())]}
            cached.write_text(json.dumps({'canonical_sha256': can_sha, 'delta': str(delta), 'polynomials': poly}, separators=(',', ':')) + '\n')
            log(f'cached F record {cached} ({cached.stat().st_size/1e6:.1f} MB)')
        except Exception as ex: log(f'cache write failed: {ex}')
    log(f'residual polynomials ready ({time.monotonic()-t0:.0f}s)')
    F = ell_to_beta(D[0, 0], delta)
    lap = ell_to_beta(E.plus((1, D[2, 0]), (1, D[2, 2])), delta)
    rec = {'id': ID, 'source_path': str(source), 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'cl': str(c), 'utc': now(), 'code_sha256': code_sha,
           'WLAP': {}, 'WL2': {}, 'WEAK_a0': {}, 'status': 'RUNNING',
           'method': 'exact Beta integrals of the exact compactified polynomials (rational times pi), 512-bit balls for the square roots; candidate_pipeline.py'}
    wrec = outdir / f'{ID}_wlap.json'
    def save():
        rec['elapsed_seconds'] = round(time.monotonic() - t0, 1); wrec.write_text(json.dumps(rec, indent=1) + '\n')
    weak_stage(F, fields, c, delta, k_list, rec, log, save)
    wl2_stage(F, wl2_list, rec, log, save)
    wlap_stage(lap, a_list, rec, log, save)
    rec['status'] = 'COMPLETE'; save(); log(f'wlap record complete ({time.monotonic()-t0:.0f}s)')
    # NORM-A2-E2 components
    erec = {'utc_start': now(), 'name': ID, 'source_path': str(source), 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'reference_meta': meta,
            'cl': str(c), 'delta': str(delta), 'precision_bits': prec, 'series_degree': N, 'code_sha256': code_sha, 'pipeline': 'candidate_pipeline.py',
            'norms': {}, 'status': 'RUNNING'}
    dest = outdir / f'{ID}_e2norms.json'
    def esave():
        erec['utc_updated'] = now(); erec['elapsed_seconds'] = round(time.monotonic() - t0, 1); dest.write_text(json.dumps(erec, indent=1) + '\n')
    def on_update(partial): erec['norms'] = partial; esave()
    erec['norms'] = E.standard_norms(D, delta, N, log, on_update); esave()
    erec['assembly'] = E.e2_assembly(erec['norms']); erec['status'] = 'COMPLETE'; esave()
    log(json.dumps(erec['assembly'], indent=1)); log(f'DONE {ID} {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('ID'); ap.add_argument('outdir')
    ap.add_argument('--k', default='0,1,2,3,4,5,6,7,8,128'); ap.add_argument('--a', default='0,1/5,2/5,3/5,4/5,1,5/4,3/2')
    ap.add_argument('--wl2', default='1/2,3/4,1,6/5'); ap.add_argument('--q3', action='store_true'); ap.add_argument('--series', type=int, default=56)
    args = ap.parse_args()
    run(args.source, args.ID, args.outdir, [int(x) for x in args.k.split(',')], [Q(x) for x in args.a.split(',')], [Q(x) for x in args.wl2.split(',')], args.q3, args.series)
