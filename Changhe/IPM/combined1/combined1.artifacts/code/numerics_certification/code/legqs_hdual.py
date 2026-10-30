"""Rigorous duality LOWER bound of the Hdot^-1 norm of a legqs residual from its exact F record (lane c1-n3; H18 falsification check of
the mode-wise Hardy UPPER bounds of legqs_hardy.py).
For each odd sine mode n: ||F_n||_H >= |<F_n, psi>| / ||grad psi||_2 for every psi in Hdot^1 of the same mode (duality; no hypothesis beyond
F_n psi and |grad psi|^2 integrable). psi = sum_i x_i psi_i with psi_i = r^3 (1-t)^beta_i t^k_i sin(n theta) (the potential family of
hminus1.py; origin regularity 3 + 2k >= n; beta > 3/2 so that grad psi is in L^2), x the Galerkin solution of the exact Gram system
rounded to dyadic rationals (any x gives a valid bound). <F_n, psi_i> is an arb ball from the exact tuple-key F (same reduction as
legqs_norms.pair_t: exact rational reduction plus one I0 ball per scale and exponent class); G_ij = <grad psi_i, grad psi_j> / pi is an exact
rational (hminus1.diffB, pair_odd: exact Beta integrals). Modes are orthogonal in Hdot^-1, so ||F||_H^2 >= sum over the computed modes of LB_n^2.
Falsification: LB_n <= H_n_UB = ||r F_n||_2 / n must hold for every computed mode, and the total lower bound must not exceed the recorded H_upper.
Self-test (--selftest <probe json>): the pairing routine is compared with the pairing_signed of the probe record (legqs_probe.pair_t path):
a probe phi = r (1-t)^2 P(t) sin(n theta) is the degree -2 object with beta = 3 and polynomial P.
Usage: legqs_hdual.py <ID> <F record> <results dir> [--modes 1,3,5,7] [--kmax 10] [--classes 6] [--selftest <probe json>]"""
from pathlib import Path
from fractions import Fraction as Q
from math import floor
from datetime import datetime, timezone
import json, sys, time, hashlib, argparse
from flint import fmpq, fmpq_poly, arb, arb_mat, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, legqs_norms as LN, hminus1 as HM
from e2norms import fq, Z, ONE, OM, endpoint

def pair_pot(Fn, psi, delta, tables, prec=1024):
    """<F_n, psi> (arb ball, includes the angular pi) for F_n a degree-0 tuple-key field (one mode) and psi a degree -2 object of hminus1
    ({(beta, 's', n): P}: psi = r (1-t)^(beta - 1) P(t) sin(n theta)). Exponent of the product: b = -3 + ell delta/2 + q1 + (beta - 1) + q2."""
    groups = {}
    for (ell, kind, n, sc), p in Fn.items():
        q1, p1 = endpoint(p)
        for (beta, kind2, n2), P in psi.items():
            assert kind == kind2 == 's' and n == n2, (kind, n, kind2, n2)
            q2, p2 = endpoint(P)
            b = Q(-3) + Q(ell) * delta / 2 + q1 + (Q(beta) - 1) + q2
            assert b > -1, ('divergent pairing', b)
            key = (b, sc); groups[key] = groups.get(key, fmpq_poly([])) + p1 * p2 * Z * fq(Q(1, 2))
    acc = LN.Accumulator(tables)
    for (b, Ms), v in sorted(groups.items()): acc.add(v, b, Ms)
    old = ctx.prec; ctx.prec = prec; val = arb.pi() * acc.value(prec); ctx.prec = old
    assert val.is_finite(); return val

def gram(basis):
    """G_ij = <grad psi_i, grad psi_j> / pi, exact rationals."""
    gx = [HM.diffB(psi, -2, 'x') for lab, psi in basis]; gy = [HM.diffB(psi, -2, 'y') for lab, psi in basis]
    m = len(basis); G = [[None] * m for _ in range(m)]
    for i in range(m):
        for j in range(i, m):
            G[i][j] = G[j][i] = HM.pair_odd(gx[i], gx[j]) + HM.pair_odd(gy[i], gy[j])
    return G

def classes(Fn, delta):
    out = set()
    for (ell, kind, n, sc), p in Fn.items():
        q, _ = endpoint(p); out.add(Q(ell) * delta / 2 + q)
    return sorted(out)

def run(ID, record, outdir, modes, kmax, nclasses, prec=3000, selftest=None, tag=''):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_legqs_hdual{tag}.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    F, raw = LN.load_F(record); delta = Q(raw['delta']); tables = LN.ScaleTables()
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: duality lower bound of H from {record} ({len(F)} components, {time.monotonic()-t0:.0f}s load)')
    out = {'id': ID, 'record': str(record), 'source_sha256': raw.get('source_sha256'), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'method': __doc__, 'kmax': kmax, 'max_classes': nclasses, 'modes': []}
    dest = outdir / f'{ID}_legqs_hdual{tag}.json'
    if selftest:
        pr = json.load(open(selftest)); n = int(pr.get('angular_mode', 1)); P = fmpq_poly([0])
        for k, v in pr['probe_coefficients'].items(): P += fq(Q(v)) * Z ** int(k)
        Fn = {k: p for k, p in F.items() if k[2] == n}
        val = pair_pot(Fn, {(Q(3), 's', n): P}, delta, tables, prec)
        prob = json.loads((outdir / f'{ID}_legqs_probe.json').read_text())['probes'].get(Path(selftest).name)
        ref = arb(prob['pairing_signed']) if prob else None
        ok = (ref is not None and val.overlaps(ref))
        out['selftest'] = {'probe': Path(selftest).name, 'pair_pot': val.str(30), 'legqs_probe_pairing_signed': prob['pairing_signed'] if prob else None, 'overlap': ok}
        log(f'SELFTEST {Path(selftest).name}: pair_pot {val.str(25)} vs probe record {prob["pairing_signed"][:30] if prob else None}: overlap {ok}')
        assert ok, 'self-test failed'
    hardy = json.loads((outdir / f'{ID}_legqs_hardy.json').read_text()); hub = {r['n']: arb(r['H_n_UB']) for r in hardy['modes']}
    total_lb2 = arb(0)
    assert len(set(modes)) == len(modes), 'duplicate modes would be double counted'
    for n in modes:
        t1 = time.monotonic()
        Fn = {k: p for k, p in F.items() if k[2] == n}
        cls = [b for b in classes(Fn, delta) if b > Q(3, 2)]
        betas = cls[:nclasses] + [Q(n + 3, 2)]
        betas = sorted(set(betas))
        basis = HM.basis_mode(n, betas, kmax)
        log(f'mode {n}: {len(Fn)} F keys, classes {[str(b) for b in cls][:8]}..., basis {len(basis)} (betas {[str(b) for b in betas]}, kmax {kmax})')
        G = gram(basis); tg = time.monotonic() - t1
        bvec = []
        for i, (lab, psi) in enumerate(basis):
            bvec.append(pair_pot(Fn, psi, delta, tables, prec))
            if i == 0: log(f'  first pairing {time.monotonic()-t1-tg:.1f}s')
        tp = time.monotonic() - t1 - tg
        m = len(basis)
        def solve_subset(idx):
            """Galerkin coefficients on a subset of basis indices: arb solve at high precision, mpmath fallback; returns a full-length rational vector."""
            k = len(idx); old = ctx.prec; ctx.prec = 2 * prec
            try:
                Ga = arb_mat([[E.aq(Q(int(G[i][j].p), int(G[i][j].q))) for j in idx] for i in idx])
                ba = arb_mat([[bvec[i] / arb.pi()] for i in idx])
                ca = Ga.solve(ba); xs = [HM.rationalize(ca[r, 0], 800) for r in range(k)]
            except Exception as ex:
                import mpmath as mp
                mp.mp.dps = 600
                try:
                    Gm = mp.matrix([[mp.mpf(int(G[i][j].p)) / mp.mpf(int(G[i][j].q)) for j in idx] for i in idx])
                    bm = mp.matrix([mp.mpf((bvec[i] / arb.pi()).mid().str(500, radius=False)) for i in idx])
                    xm = mp.lu_solve(Gm, bm); xs = [Q(str(xm[r])) if False else Q(mp.nstr(xm[r], 300)) for r in range(k)]
                except Exception as ex2:
                    ctx.prec = old; return None
            ctx.prec = old
            x = [Q(0)] * m
            for r, i in enumerate(idx): x[i] = xs[r]
            return x
        cands = []
        xfull = solve_subset(list(range(m)))
        if xfull is not None: cands.append(('galerkin all', xfull))
        for bt in betas:
            idx = [i for i, (lab, psi) in enumerate(basis) if lab[0] == str(bt)]
            xs = solve_subset(idx)
            if xs is not None: cands.append((f'galerkin class {bt}', xs))
        for i in range(m):
            e = [Q(0)] * m; e[i] = Q(1); cands.append((f'single {basis[i][0]}', e))
        best = None
        for lab, xv in cands:
            num = arb(0); den = fmpq(0)
            for i in range(m):
                if xv[i]: num += bvec[i] * E.aq(xv[i])
            for i in range(m):
                if xv[i]:
                    for j in range(m):
                        if xv[j]: den += fq(xv[i]) * G[i][j] * fq(xv[j])
            if den <= 0: continue
            lb = abs(num) / (arb.pi() * E.aq(Q(int(den.p), int(den.q)))).sqrt()
            if not lb.is_finite(): continue
            if best is None or lb.lower() > best[1].lower(): best = (lab, lb, num, den, xv)
        lab, lb, num, den, xbest = best
        quot = 2 * (num / arb.pi()) - E.aq(Q(int(den.p), int(den.q)))   # 2<F,psi>/pi - |grad psi|^2/pi = LB^2/pi at the exact Galerkin optimum
        ok = lb.lower() <= hub[n].upper()
        Ln = lb.lower() if lb.lower() > 0 else arb(0)           # astra referee: never square a negative lower endpoint
        total_lb2 += arb(Ln) ** 2
        row = {'n': n, 'basis_size': m, 'pairing_radius_max': str(max(b.rad() for b in bvec)), 'n_candidates': len(cands), 'betas': [str(b) for b in betas], 'kmax': kmax, 'chosen': lab, 'F_psi': num.str(30), 'grad_psi_sq_over_pi': str(den)[:80],
               'grad_psi_sq_over_pi_exact': str(den), 'x_rational': {f'{basis[i][0][0]},{basis[i][0][1]}': str(xbest[i]) for i in range(m) if xbest[i]},
               'basis_labels': '(beta, k) -> psi = r^3 (1-t)^beta t^k sin(n theta); x_rational keys are beta,k', 'pairings_balls': [b.str(40) for b in bvec],
               'LB_certified_nonneg': str(Ln),
               'LB': lb.str(30), 'LB_lower': str(lb.lower()), 'galerkin_quotient_over_pi': quot.str(20), 'H_n_UB_hardy': hub[n].str(30),
               'LB_le_UB': ok, 'ratio_LB_over_UB': (lb / hub[n]).str(12), 'seconds_gram': round(tg, 1), 'seconds_pairings': round(tp, 1)}
        out['modes'].append(row)
        log(f'  mode {n}: H_n >= {lb.lower().str(20)} (UB {hub[n].upper().str(20)}; ratio {(lb/hub[n]).str(8)}; LB <= UB: {ok}; {lab}; gram {tg:.0f}s, pairings {tp:.0f}s)')
        dest.write_text(json.dumps(out, indent=1) + '\n')
    H_lb = total_lb2.sqrt()
    out['H_lower'] = str(H_lb.lower()); out['H_lower_ball'] = H_lb.str(30); out['H_upper_hardy'] = hardy['H_upper'][:80]
    out['LB_le_UB_total'] = H_lb.lower() <= arb(hardy['H_upper']).upper()
    normrec = outdir / f'{ID}_legqs_norms.json'
    if normrec.exists():
        N = json.loads(normrec.read_text())['norms']
        if all(N.get(k, {}).get('status') == 'FINITE' for k in ('G0', 'G1', 'P2')):
            lo = {k: arb(N[k]['norm_lower']) for k in ('G0', 'G1', 'P2')}
            E2_lo = (lo['P2'] ** 2 + 2 ** 14 * lo['G1'] ** 2 + 2 ** 18 * lo['G0'] ** 2 + 2 ** 18 * arb(20) / 21 * arb(H_lb.lower()) ** 2).sqrt()
            out['E2_lower_with_H_lower'] = str(E2_lo.lower()); out['E2_lower_without_H'] = hardy.get('E2_lower_without_H', '')[:40]
            out['E2_upper_with_mode_hardy_H'] = hardy.get('E2_upper_with_mode_hardy_H', '')[:40]
    out['elapsed_seconds'] = round(time.monotonic() - t0, 1)
    dest.write_text(json.dumps(out, indent=1) + '\n')
    log(f'H >= {H_lb.lower().str(20)} over modes {modes} (Hardy UB {hardy["H_upper"][:22]}); LB <= UB: {out["LB_le_UB_total"]}; E_2 >= {out.get("E2_lower_with_H_lower", "")[:20]}; DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('ID'); ap.add_argument('record'); ap.add_argument('outdir')
    ap.add_argument('--modes', default='1,3,5,7'); ap.add_argument('--kmax', type=int, default=10); ap.add_argument('--classes', type=int, default=6)
    ap.add_argument('--selftest', default=None); ap.add_argument('--tag', default='')
    a = ap.parse_args()
    run(a.ID, a.record, a.outdir, [int(v) for v in a.modes.split(',')], a.kmax, a.classes, selftest=a.selftest, tag=a.tag)
