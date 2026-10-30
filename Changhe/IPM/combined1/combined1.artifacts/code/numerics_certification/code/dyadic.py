"""NORM-T-DYADIC-v1 (theory_v01 section 2): per-annulus norms of the exact residual (lane c1-n3).

Annuli A_j = {2^j <= r < 2^(j+1)}, j = jmin..jmax, inner disc {r < 2^jmin}, exterior {r >= 2^(jmax+1)}.
Per region: ||F||_2, ||r F||_2, ||grad F||_2, ||omega D^2 F||_2 (rigorous enclosures: the same exact group polynomials
as the whole-plane Beta integrals, integrated over [t1, t2] with incomplete Beta functions in ball arithmetic;
the exterior as exact total minus the lower incomplete integral), and sup |F| (FLOAT by sampling, plus a rigorous
upper bound sum_n sup_r |f_n(r)| from Bernstein coefficients of the exact mode polynomials).
Squares over all regions add up to the whole-plane squares (checked against the exact totals).
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E
from e2norms import fq, aq, Z, OM, ONE, endpoint

def groups_for(D, d, delta, a_shift=Q(0), t_power=0):
    """Exact group polynomials {b: P_b} with ||W D^d F||_2^2 = (pi/2) sum_b int_0^1 P_b(t) (1-t)^b dt (times the series
    factor for omega). Returns (groups, bad) where bad lists nonintegrable diagonal sectors."""
    groups = {}; bad = []
    for nx in range(d + 1):
        modes = {}
        for (ell, kind, n), p in D[d, nx].items():
            q, p2 = endpoint(p); modes.setdefault((kind, n), []).append((ell, q, p2))
            b = Q(d - 3) + ell * delta + 2 * q + a_shift
            if b <= -1: bad.append((nx, ell, kind, n, q, str(b)))
        if bad: continue
        for (kind, n), rows in modes.items():
            for i, (ell, q, p) in enumerate(rows):
                for j in range(i, len(rows)):
                    ell2, q2, p2 = rows[j]
                    b = Q(d - 3) + (ell + ell2) * delta / 2 + q + q2 + a_shift
                    factor = comb(d, nx) * (2 if n == 0 and kind == 'c' else 1) * (1 if i == j else 2)
                    v = p * p2 * factor
                    if d % 2 == 0: v *= Z
                    if t_power: v *= Z ** t_power
                    groups[b] = groups.get(b, fmpq_poly([])) + v
    return groups, bad

def incomplete_table(z, b, need):
    """I_k = int_0^z t^k (1-t)^b dt for k < need, ball arithmetic (recurrence, anchored by beta_lower every 64 steps)."""
    zb = aq(z); bb = aq(b)
    out = [zb.beta_lower(arb(1), bb + 1)]
    for k in range(1, need):
        if k % 64 == 0: out.append(zb.beta_lower(arb(k + 1), bb + 1))
        else: out.append((k * out[-1] - zb ** k * (1 - zb) ** (bb + 1)) / (k + bb + 1))
    return out

def region_integral(poly, b, z1, z2, cache):
    """int_{z1}^{z2} poly(t) (1-t)^b dt (ball), z2 may be 1 (exact Beta total minus lower incomplete)."""
    need = poly.degree() + 1
    ckey = ('coef', id(poly))
    if ckey not in cache:
        cache[ckey] = [aq(Q(str(c))) if c else None for c in poly.coeffs()]       # convert the big rationals once
    ca = cache[ckey]
    def table(z):
        key = (z, b)
        if key not in cache: cache[key] = incomplete_table(z, b, need)
        tab = cache[key]
        while len(tab) < need:
            k = len(tab); zb = aq(z); bb = aq(b); tab.append((k * tab[-1] - zb ** k * (1 - zb) ** (bb + 1)) / (k + bb + 1))
        return tab
    if z2 == 1:
        tkey = ('total', id(poly), b)
        if tkey not in cache:
            bet = [fq(1 / (b + 1))]
            while len(bet) < need:
                k = len(bet); bet.append(bet[-1] * k / fq(b + k + 1))
            cache[tkey] = aq(Q(str(sum((c * bet[k] for k, c in enumerate(poly.coeffs())), fmpq(0)))))
        t1 = table(z1)
        return cache[tkey] - sum((ca[k] * t1[k] for k in range(need) if ca[k] is not None), arb(0))
    t1 = table(z1); t2 = table(z2)
    return sum((ca[k] * (t2[k] - t1[k]) for k in range(need) if ca[k] is not None), arb(0))

def annulus_norm_sq(groups, edges, series=(), N=56):
    """Squared norms per region [edges[i], edges[i+1]) in t (edges[-1] may be 1). Returns list of (lo, hi) arbs."""
    wp = ONE; eps = fmpq(0); pref = arb(1)
    for cc, alpha in series:
        mid, al, p, e = E.series_factor(cc, alpha, N); wp = wp * p; eps += e; pref *= aq(mid) ** aq(al)
    cache = {}; out = []
    wprod = {b: p * wp for b, p in groups.items()} if series else {}
    for z1, z2 in zip(edges[:-1], edges[1:]):
        S = arb(0); T = arb(0)
        for b, p in groups.items():
            s = region_integral(p, b, z1, z2, cache); S += s
            if series: T += region_integral(wprod[b], b, z1, z2, cache)
        if series:
            lo = T - aq(eps) * S; hi = T + aq(eps) * S
        else: lo = hi = S
        out.append((arb.pi() / 2 * pref * lo, arb.pi() / 2 * pref * hi))
    return out

def bernstein_sup(p, z1, z2):
    """Rigorous bound of sup_{[z1,z2]} |p(t)| by the Bernstein coefficients of p on [z1, z2] (exact rationals)."""
    # p(z1 + (z2-z1) s) as a polynomial in s, then Bernstein coefficients b_i = sum_j C(i,j)/C(n,j) a_j
    n = p.degree(); a = p.coeffs()
    h = fq(z2 - z1); zz = fq(z1)
    # substitute t = zz + h s
    sub = fmpq_poly([zz, h]); ps = fmpq_poly([0])
    for c in reversed(a): ps = ps * sub + c
    cs = ps.coeffs(); cs += [fmpq(0)] * (n + 1 - len(cs))
    best = fmpq(0)
    for i in range(n + 1):
        bi = sum((fmpq(comb(i, j)) / comb(n, j) * cs[j] for j in range(i + 1)), fmpq(0))
        if abs(bi) > best: best = abs(bi)
    return best

def sup_bounds(F, delta, edges, nsamp=64):
    """Per region: FLOAT sup |F| by sampling (r x theta), and a rigorous UB sum_n sup_r |f_n(r)| (mode-sum)."""
    import math
    modes = {}
    for (ell, kind, n), p in F.items(): modes.setdefault(n, []).append((ell, p))
    out = []
    for z1, z2 in zip(edges[:-1], edges[1:]):
        # rigorous mode-sum UB: |f_n(r)| <= r * sum_ell (1-t)^(ell delta/2) |P|, r and (1-t)^.. monotone on the region
        z2e = Q(1) - Q(1, 10 ** 12) if z2 == 1 else z2    # exterior handled with the tail factor below
        ub = arb(0)
        for n, rows in modes.items():
            sn = arb(0)
            for ell, p in rows:
                q, p2 = endpoint(p)
                # f piece = r (1-t)^(ell delta/2 + q) p2(t); r^2 = t/(1-t); bound sup over [z1, z2]
                bp = aq(Q(str(bernstein_sup(p2, z1, z2e))))
                beta = Q(ell) * delta / 2 + q
                # r (1-t)^beta = t^(1/2) (1-t)^(beta - 1/2): monotone pieces; evaluate on an interval
                tt = arb(aq(z1)); tt = tt.union(aq(z2e))
                fac = tt.sqrt() * (1 - tt) ** aq(beta - Q(1, 2)) if z2 != 1 else arb.union(aq(z1).sqrt() * (1 - aq(z1)) ** aq(beta - Q(1, 2)), arb(0))
                if z2 == 1 and beta - Q(1, 2) < 0: fac = arb('[+/- inf]')
                sn += fac.abs_upper() * bp if fac.is_finite() else arb('[+/- inf]')
            ub += sn
        # FLOAT sampling (radial factors in ball arithmetic, angular synthesis in float64)
        import numpy as np
        from fractions import Fraction as QQ
        from flint import arb, ctx
        if z2 == 1: tsf = np.linspace(float(z1), 1 - 1e-9, nsamp)
        else: tsf = np.linspace(float(z1), float(z2), nsamp)
        ts_q = [QQ(float(t)) for t in tsf]
        th = np.linspace(0, math.pi / 2, nsamp)
        vals = np.zeros((nsamp, nsamp))
        old = ctx.prec; ctx.prec = 1500
        for (ell, kind, n), p in F.items():
            co = [arb(str(c.p)) / arb(str(c.q)) for c in p.coeffs()]
            pv = []
            for tq in ts_q:
                ta = arb(str(tq)); v = arb(0)
                for c in reversed(co): v = v * ta + c
                v *= (1 - ta) ** (arb(ell) * arb(str(delta.numerator)) / arb(str(delta.denominator)) / 2) * (ta / (1 - ta)).sqrt()
                pv.append(float(v.mid()))
            ang = np.sin(n * th) if kind == 's' else np.cos(n * th)
            vals += np.outer(np.array(pv), ang)
        ctx.prec = old
        out.append({'sup_F_float': float(np.abs(vals).max()), 'sup_F_modesum_UB': str(ub.upper()) if ub.is_finite() else 'inf'})
    return out

def run(source, ID, outdir, jmin=-4, jmax=14):
    ctx.prec = 512; outdir = Path(outdir); t0 = time.monotonic()
    logf = open(outdir / f'{ID}_dyadic.log', 'a')
    def log(*a):
        msg = ' '.join(str(x) for x in a); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID} dyadic profile, j = {jmin}..{jmax}')
    D, fields = E.residual_polynomials(A, c, 2, log)
    radii = [Q(0)] + [Q(2) ** j for j in range(jmin, jmax + 2)]
    edges = [r * r / (1 + r * r) for r in radii] + [Q(1)]
    labels = [f'r<2^{jmin}'] + [f'[2^{j},2^{j+1})' for j in range(jmin, jmax + 1)] + [f'r>=2^{jmax+1}']
    specs = [('G0', 0, Q(0), 0, ()), ('rF', 0, Q(-1), 1, ()), ('G1', 1, Q(0), 0, ()), ('P2', 2, Q(-4, 5), 0, E.OMEGA)]
    rec = {'id': ID, 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'regions': labels, 'edges_t': [str(e) for e in edges], 'norms': {}}
    for label, d, a, tp, ser in specs:
        groups, bad = groups_for(D, d, delta, a, tp)
        if bad: rec['norms'][label] = {'status': 'INFINITE', 'bad': bad[:5]}; log(label, 'INFINITE'); continue
        sqs = annulus_norm_sq(groups, edges, ser)
        tot_lo = sum((s[0] for s in sqs), arb(0)); tot_hi = sum((s[1] for s in sqs), arb(0))
        rows = [{'region': lab, 'norm_LB': str(lo.sqrt().lower()) if lo.lower() > 0 else '0', 'norm_UB': str(hi.sqrt().upper()),
                 'sq_UB': str(hi.upper())} for lab, (lo, hi) in zip(labels, sqs)]
        rec['norms'][label] = {'status': 'FINITE', 'rows': rows, 'total_from_regions_LB': str(tot_lo.sqrt().lower()), 'total_from_regions_UB': str(tot_hi.sqrt().upper())}
        log(f'{label}: total from regions [{tot_lo.sqrt().lower()}, {tot_hi.sqrt().upper()}] ({time.monotonic()-t0:.0f}s)')
        for r in rows: log(f'   {r["region"]:>14}: [{r["norm_LB"][:12]}, {r["norm_UB"][:12]}]')
    rec['sup'] = [dict(region=lab, **s) for lab, s in zip(labels, sup_bounds(D[0, 0], delta, edges))]
    for s in rec['sup']: log(f'   sup|F| {s["region"]:>14}: FLOAT {s["sup_F_float"]:.4e}  modesum UB {s["sup_F_modesum_UB"][:12]}')
    rec['elapsed_seconds'] = time.monotonic() - t0; rec['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (outdir / f'{ID}_dyadic.json').write_text(json.dumps(rec, indent=1) + '\n'); log(f'DONE {ID} {rec["elapsed_seconds"]:.0f}s')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else -4, int(sys.argv[5]) if len(sys.argv) > 5 else 14)
