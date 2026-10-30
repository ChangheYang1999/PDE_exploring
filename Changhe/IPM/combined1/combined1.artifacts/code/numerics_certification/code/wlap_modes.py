"""Per-angular-mode split of NORM-T-WLAP-v1: N_a(F)^2 = sum over odd n of N_a(F_n)^2, from a stored F record (lane c1-n3).
Delta F is formed from the compactified F polynomials by the exact beta-form algebra of hminus1.py (laplacian), an
independent derivative path from e2norms.residual_polynomials; the mode totals must agree with the wlap record exactly.
Usage: wlap_modes.py <ID> <F record or exact source> <outdir> [a list, default 0,1/5,2/5,3/5,4/5,1]"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, hminus1 as H
from e2norms import aq, fq, Z

def run(ID, path, outdir, a_list, only_modes=None):
    ctx.prec = 512; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_wlap_modes.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    F_ell, delta, can_sha, src_sha = H.load_F(path, log)
    F = H.normalize(H.from_ell(F_ell, delta)) if all(isinstance(k[0], int) for k in F_ell) else F_ell
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: per-mode N_a from {path}; {len(F)} F components; canonical {can_sha}')
    if only_modes: F = {k: p for k, p in F.items() if k[2] in only_modes}
    lap = H.laplacian(F, 0)
    modes = sorted({n for (beta, kind, n) in lap})
    log(f'Laplacian formed ({time.monotonic()-t0:.0f}s): {len(lap)} components, modes {modes[:5]}..{modes[-3:]} ({len(modes)} modes)')
    # group polynomials per mode, products done once: N_a(F_n)^2/pi = sum_b int_0^1 P_(n,b)(t) (1-t)^(b + a - 2) dt
    groups = {}
    for n in modes:
        rows = []
        for (beta, kind, nn), p in lap.items():
            if nn != n or kind != 's': continue
            q, p2 = H.endpoint(p); rows.append((beta, q, p2))
        g = {}
        for i, (beta, q, p) in enumerate(rows):
            for j in range(i, len(rows)):
                beta2, q2, p2 = rows[j]
                b = Q(2 - 3) + beta + beta2 + q + q2
                g[b] = g.get(b, fmpq_poly([])) + p * p2 * fq(Q(1, 2) * (1 if i == j else 2)) * Z
        groups[n] = g
    log(f'group polynomials formed ({time.monotonic()-t0:.0f}s)')
    rec = {'id': ID, 'source': str(path), 'canonical_sha256': can_sha, 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'only_modes': only_modes,
           'method': 'exact Beta integrals per sin(n theta) mode of Delta F (beta-form algebra of hminus1.py), rational times pi; 512-bit balls',
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'per_a': {}}
    for a in a_list:
        per = {}; tot = fmpq(0); div = False; cache = {}
        for n in modes:
            v = fmpq(0)
            for b, p in groups[n].items():
                bb = b + Q(a) - 2
                if bb <= -1: div = True; break
                v += E.integral(p, bb, cache)
            if div: log(f'a={a}: mode {n} divergent'); break
            per[n] = v; tot += v
        if div: rec['per_a'][str(a)] = {'status': 'INFINITE'}; continue
        N = (arb.pi() * aq(Q(str(tot)))).sqrt()
        rows = []; cum = fmpq(0)
        for n in modes:
            cum += per[n]
            rows.append({'mode': n, 'N_a_mode_sq_over_pi_exact': str(per[n]), 'N_a_mode': str((arb.pi() * aq(Q(str(per[n])))).sqrt().str(20)),
                         'share_of_square': float(aq(Q(str(per[n]))) / aq(Q(str(tot)))) if tot != 0 else None,
                         'cumulative_N_a': str((arb.pi() * aq(Q(str(cum)))).sqrt().str(20))})
        label = 'N_a (all modes)' if not only_modes else f'projected N_a (modes {only_modes}) = LB of N_a'
        rec['per_a'][str(a)] = {'N_a_LB': str(N.lower()), 'N_a_UB': str(N.upper()), 'sq_over_pi_exact': str(tot), 'label': label, 'modes': rows}
        top = sorted(rows, key=lambda r: -(r['share_of_square'] or 0))[:6]
        log(f'a={a}: {label} = {N.str(25)}; top modes ' + ', '.join(f"n={r['mode']} {r['N_a_mode'][:12]} ({100*(r['share_of_square'] or 0):.1f}%)" for r in top) + f' ({time.monotonic()-t0:.0f}s)')
        for lim in (3, 15, 31, 61, 121):
            c = fmpq(0)
            for n in modes:
                if n <= lim: c += per[n]
            log(f'   modes <= {lim}: partial N_a = {(arb.pi() * aq(Q(str(c)))).sqrt().str(20)}')
        (outdir / f'{ID}_wlap_modes.json').write_text(json.dumps(rec, indent=1) + '\n')
    rec['elapsed_seconds'] = round(time.monotonic() - t0, 1)
    (outdir / f'{ID}_wlap_modes.json').write_text(json.dumps(rec, indent=1) + '\n'); log(f'DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    ID, path, outdir = sys.argv[1:4]
    a_list = [Q(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['0', '1/5', '2/5', '3/5', '4/5', '1'])]
    only = [int(x) for x in sys.argv[5].split(',')] if len(sys.argv) > 5 else None
    run(ID, path, outdir, a_list, only)
