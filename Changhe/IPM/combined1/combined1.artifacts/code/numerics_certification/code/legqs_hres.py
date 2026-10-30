"""Rigorous two-sided enclosure of ||F_n||_H per mode for a legqs residual via a Galerkin potential and its residual (lane c1-n3; answer to
c1-n4 15:16Z: a rigorous omitted-component estimate instead of nested-basis agreement).
For psi in the potential family restricted to the branch classes of F_n (so that Delta psi is representable in the tuple-key form of F) and
g = F_n + Delta psi (one sine mode n), the triangle inequality in Hdot^-1 with ||Delta psi||_H = ||grad psi||_2 and the mode-n Hardy bound
||g||_H <= ||r g||_2 / n (hminus1_mode_hardy.py lemma; T4-327) give
    | ||F_n||_H - ||grad psi||_2 | <= ||r g||_2 / n,
so  LB2_n = ||grad psi||_2 - ||r g||_2 / n <= ||F_n||_H <= ||grad psi||_2 + ||r g||_2 / n = UB_n.
||grad psi||_2^2 = pi x^T G x with x^T G x an exact rational (hminus1 Gram), ||r g||_2 is a ball from legqs_norms.normsq_t on the exact field F_n + Delta psi
(a_shift = -1, t_power = 1, as in legqs_hardy.py). Built-in check: with psi = 0 the same call must reproduce ||r F_n||_2 of the Hardy record.
The duality bound |<F_n, psi>| / ||grad psi||_2 of legqs_hdual.py is reported for the same psi. Total: H^2 <= sum_(computed n) UB_n^2 +
sum_(other n) (||r F_n||_2 / n)^2 (Hardy record), H^2 >= sum_(computed n) max(LB_n, LB2_n)^2.
Usage: legqs_hres.py <ID> <F record> <results dir> [--modes 1,3] [--kmax 14] [--classes 8] [--tag _hres]"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib, argparse
from flint import fmpq, fmpq_poly, arb, arb_mat, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, legqs_norms as LN, hminus1 as HM
from e2norms import fq, Z, ONE, OM, endpoint
from legqs_hdual import pair_pot, gram

def run(ID, record, outdir, modes, kmax, nclasses, prec=3000, tag='_hres'):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_legqs_hres.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    F, raw = LN.load_F(record); delta = Q(raw['delta']); tables = LN.ScaleTables()
    hardy = json.loads((outdir / f'{ID}_legqs_hardy.json').read_text()); hrows = {r['n']: r for r in hardy['modes']}
    assert hardy.get('source_sha256') == raw.get('source_sha256'), ('Hardy record does not belong to this F record', hardy.get('source_sha256'), raw.get('source_sha256'))
    assert sorted(hrows) == sorted({k[2] for k in F}), 'Hardy record modes differ from the F record modes'
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: two-sided mode enclosures of H from {record} ({len(F)} components, {time.monotonic()-t0:.0f}s load)')
    out = {'id': ID, 'record': str(record), 'source_sha256': raw.get('source_sha256'), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'method': __doc__, 'kmax': kmax, 'max_classes': nclasses, 'modes': []}
    dest = outdir / f'{ID}_legqs_hdual{tag}.json'
    assert len(set(modes)) == len(modes)
    UB2_total = arb(0); LB2_total = arb(0)
    for n in modes:
        t1 = time.monotonic()
        Fn = {k: p for k, p in F.items() if k[2] == n}
        # branch classes of F_n with their (ell, q): beta = ell delta/2 + q
        cls = {}
        for (ell, kind, nn, sc), p in Fn.items():
            q, _ = endpoint(p); cls[Q(ell) * delta / 2 + q] = (ell, q)
        betas = sorted(b for b in cls if b > Q(3, 2))[:nclasses]
        basis = HM.basis_mode(n, betas, kmax); m = len(basis)
        log(f'mode {n}: {len(Fn)} F keys, {len(cls)} classes, basis {m} (no integer class; betas {[str(b) for b in betas][:3]}..., kmax {kmax})')
        # check: ||r F_n||_2 from the same normsq_t call equals the Hardy record
        r0 = LN.normsq_t([(1, Fn)], 0, delta, a_shift=Q(-1), t_power=1, tables=tables, prec=prec); assert r0['status'] == 'FINITE'
        rFn = r0['hi'].sqrt(); chk = rFn.overlaps(arb(hrows[n]['rF_n'])); assert chk, ('||r F_n|| does not reproduce the Hardy record', n)
        G = gram(basis); bvec = [pair_pot(Fn, psi, delta, tables, prec) for lab, psi in basis]
        old = ctx.prec; ctx.prec = 2 * prec
        Ga = arb_mat([[E.aq(Q(int(G[i][j].p), int(G[i][j].q))) for j in range(m)] for i in range(m)])
        ba = arb_mat([[bvec[i] / arb.pi()] for i in range(m)])
        ca = Ga.solve(ba); x = [HM.rationalize(ca[i, 0], 800) for i in range(m)]
        ctx.prec = old
        # psi, Delta psi, residual g = F_n + Delta psi in the tuple-key form
        psi = HM.normalize(HM.plusB(*[HM.scale(p, xi) for (lab, p), xi in zip(basis, x) if xi]))
        lap = HM.laplacian(psi, -2)
        Fplus = dict(Fn)
        for (beta, kind, nn, *_), P in lap.items():
            hit = None
            for b0, (ell, q0) in cls.items():
                qq = beta - Q(ell) * delta / 2
                if qq.denominator == 1 and qq >= 0: hit = (ell, int(qq)); break
            assert hit is not None, ('Laplacian class not representable', beta)
            key = (hit[0], 's', n, ()); Fplus[key] = Fplus.get(key, fmpq_poly([])) + P * OM ** hit[1]
        rg = LN.normsq_t([(1, Fplus)], 0, delta, a_shift=Q(-1), t_power=1, tables=tables, prec=prec); assert rg['status'] == 'FINITE', rg
        R = rg['hi'].sqrt()
        den = fmpq(0); num = arb(0)
        for i in range(m):
            if x[i]:
                num += bvec[i] * E.aq(x[i])
                for j in range(m):
                    if x[j]: den += fq(x[i]) * G[i][j] * fq(x[j])
        Egrad = (arb.pi() * E.aq(Q(int(den.p), int(den.q)))).sqrt()
        UB = Egrad + R / n; LB2 = Egrad - R / n; LBd = abs(num) / Egrad
        LBbest = LBd if LBd.lower() >= LB2.lower() else LB2
        Lcert = LBbest.lower() if LBbest.lower() > 0 else arb(0)
        hub = arb(hrows[n]['H_n_UB'])
        UBuse = UB if UB.upper() <= hub.upper() else hub
        UB2_total += arb(UBuse.upper()) ** 2; LB2_total += arb(Lcert) ** 2
        row = {'n': n, 'basis_size': m, 'betas': [str(b) for b in betas], 'kmax': kmax, 'rFn_check_overlaps_hardy_record': chk, 'rFn': rFn.str(25),
               'grad_psi': Egrad.str(30), 'grad_psi_sq_over_pi_exact': str(den), 'residual_r_g': R.str(30), 'residual_over_n': (R / n).str(20),
               'UB_n': str(UB.upper()), 'LB2_n': str(LB2.lower()), 'LB_duality_n': str(LBd.lower()), 'LB_certified': str(Lcert),
               'hardy_UB_n': hrows[n]['H_n_UB'], 'UB_n_improves_hardy': bool(UB.upper() < hub.upper()),
               'x_rational': {f'{basis[i][0][0]},{basis[i][0][1]}': str(x[i]) for i in range(m) if x[i]}, 'pairings_balls': [b.str(40) for b in bvec],
               'seconds': round(time.monotonic() - t1, 1)}
        out['modes'].append(row)
        log(f'  mode {n}: ||grad psi|| = {Egrad.str(15)}, ||r g||/n = {(R/n).str(10)} -> {LB2.lower().str(12)} <= ||F_n||_H <= {UB.upper().str(12)} (duality LB {LBd.lower().str(12)}; Hardy UB {hub.upper().str(12)}; rF_n check {chk}; {time.monotonic()-t1:.0f}s)')
        dest.write_text(json.dumps(out, indent=1) + '\n')
    other = arb(0)
    for nn, r in hrows.items():
        if nn not in modes: other += arb(r['rF_n_sq']) / (nn * nn)
    H_UB = (UB2_total + other).sqrt(); H_LB = LB2_total.sqrt()
    out['H_upper_new'] = str(H_UB.upper()); out['H_lower_new'] = str(H_LB.lower()); out['H_upper_hardy'] = hardy['H_upper'][:60]
    out['other_modes_hardy_sq'] = other.str(20); out['modes_computed'] = modes
    normrec = outdir / f'{ID}_legqs_norms.json'
    if normrec.exists():
        NR = json.loads(normrec.read_text()); assert NR.get('source_sha256') == raw.get('source_sha256'), 'norm record does not belong to this F record'; N = NR['norms']
        lo = {k: arb(N[k]['norm_lower']) for k in ('G0', 'G1', 'P2')}; up = {k: arb(N[k]['norm_upper']) for k in ('G0', 'G1', 'P2')}
        out['E2_lower_new'] = str((lo['P2'] ** 2 + 2 ** 14 * lo['G1'] ** 2 + 2 ** 18 * lo['G0'] ** 2 + 2 ** 18 * arb(20) / 21 * arb(H_LB.lower()) ** 2).sqrt().lower())
        out['E2_upper_new'] = str((up['P2'] ** 2 + 2 ** 14 * up['G1'] ** 2 + 2 ** 18 * up['G0'] ** 2 + 2 ** 18 * arb(20) / 21 * arb(H_UB.upper()) ** 2).sqrt().upper())
    out['elapsed_seconds'] = round(time.monotonic() - t0, 1); dest.write_text(json.dumps(out, indent=1) + '\n')
    log(f'H in [{H_LB.lower().str(15)}, {H_UB.upper().str(15)}] (modes {modes} two-sided, other modes by Hardy; Hardy total {hardy["H_upper"][:20]}); E_2 in [{out.get("E2_lower_new","")[:14]}, {out.get("E2_upper_new","")[:14]}]; DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('ID'); ap.add_argument('record'); ap.add_argument('outdir')
    ap.add_argument('--modes', default='1,3'); ap.add_argument('--kmax', type=int, default=14); ap.add_argument('--classes', type=int, default=8); ap.add_argument('--tag', default='_hres')
    a = ap.parse_args()
    run(a.ID, a.record, a.outdir, [int(v) for v in a.modes.split(',')], a.kmax, a.classes, tag=a.tag)
