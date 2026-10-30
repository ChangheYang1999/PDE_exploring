"""Mode-wise Hardy upper bound of the Hdot^-1 norm of a legqs residual from its exact F record (lane c1-n3).
Lemma (hminus1_mode_hardy.py; astra-refereed, T4-327 CONFIRMS the mode-wise identity and the constant 1/n under g, r g in L^2):
for g = f(r) sin(n theta), n >= 1: ||g||_H <= ||r g||_2 / n. The angular modes of F are orthogonal in Hdot^-1 (the Riesz potential
commutes with rotations), so ||F||_H^2 = sum_n ||F_n||_H^2 <= sum_n ||r F_n||_2^2 / n^2, where ||r F_n||_2 is the exact per-mode
weighted norm (legqs_norms.normsq_t with (1-t)^(-1) t, the weight r^2). Requires that F has no mode-0 (cos, n = 0) part: F is odd in y
for every candidate of this family (sine modes only); the script asserts it. Output: <ID>_legqs_hardy.json with the per-mode ||r F_n||_2
balls, the H upper bound, and the E_2 upper bound with this H (E_2^2 = P2^2 + 2^14 G1^2 + 2^18 G0^2 + 2^18 (20/21) H^2) when the norm
record is COMPLETE. Usage: legqs_hardy.py <ID> <F record (legqs format)> <outdir>"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import legqs_norms as LN

def run(ID, record, outdir, prec=1024):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir)
    F, raw = LN.load_F(record); delta = Q(raw['delta'])
    kinds = {kind for (ell, kind, n, sc) in F}; modes = sorted({n for (ell, kind, n, sc) in F})
    assert kinds == {'s'} and 0 not in modes, ('F is not a pure sine series', kinds, modes[:3])
    tables = LN.ScaleTables(); rows = []; H2 = arb(0)
    for n in modes:
        Fn = {k: p for k, p in F.items() if k[2] == n}
        r = LN.normsq_t([(1, Fn)], 0, delta, a_shift=Q(-1), t_power=1, tables=tables, prec=prec)
        assert r['status'] == 'FINITE', ('||r F_n|| infinite', n, r)
        rfn2 = r['hi']                                 # ball of ||r F_n||_2^2 (no series: lo == hi)
        H2 += rfn2 / (n * n)
        rows.append({'n': n, 'rF_n_sq': rfn2.str(30), 'rF_n': rfn2.sqrt().str(30), 'H_n_UB': (rfn2.sqrt() / n).str(30), 'components': len(Fn)})
        print(f'mode {n}: ||r F_n||_2 = {rfn2.sqrt().str(20)}  H_n <= {(rfn2.sqrt()/n).str(15)}', flush=True)
    H = H2.sqrt()
    out = {'id': ID, 'record': str(record), 'source_sha256': raw.get('source_sha256'), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'method': __doc__, 'modes': rows,
           'H_upper': str(H.upper()), 'H_upper_ball': H.str(30), 'rF_check': str((sum((arb(r['rF_n_sq']) for r in rows), arb(0))).sqrt().str(30)),
           'elapsed_seconds': round(time.monotonic() - t0, 1)}
    normrec = outdir / f'{ID}_legqs_norms.json'
    if normrec.exists():
        nr = json.loads(normrec.read_text()); N = nr.get('norms', {})
        if all(N.get(k, {}).get('status') == 'FINITE' for k in ('G0', 'G1', 'P2')):
            up = {k: arb(N[k]['norm_upper']) for k in ('G0', 'G1', 'P2')}; lo = {k: arb(N[k]['norm_lower']) for k in ('G0', 'G1', 'P2')}
            E2_up = (up['P2'] ** 2 + 2 ** 14 * up['G1'] ** 2 + 2 ** 18 * up['G0'] ** 2 + 2 ** 18 * arb(20) / 21 * H ** 2).sqrt()
            E2_lo = (lo['P2'] ** 2 + 2 ** 14 * lo['G1'] ** 2 + 2 ** 18 * lo['G0'] ** 2).sqrt()
            out['E2_upper_with_mode_hardy_H'] = str(E2_up.upper()); out['E2_lower_without_H'] = str(E2_lo.lower())
            if N.get('rF', {}).get('status') == 'FINITE': out['E2_upper_with_rF_for_H'] = nr.get('assembly', {}).get('E2_upper_with_rF_for_H')
            print('E_2 in [', out['E2_lower_without_H'][:24], ',', out['E2_upper_with_mode_hardy_H'][:24], '] (H by the mode-wise Hardy bound)')
    (outdir / f'{ID}_legqs_hardy.json').write_text(json.dumps(out, indent=1) + '\n')
    print(f'H <= {H.upper().str(20)} (rF total check {out["rF_check"][:24]}); DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3])
