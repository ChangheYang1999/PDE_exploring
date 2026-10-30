"""Second arithmetic path for the legqs component norms (lane c1-n3): recompute the norms of a legqs candidate from its F record with
EVERY radial integral taken by the t-monomial 2F1 ball route (Accumulator.BALL_DEGREE = 0: one Beta x 2F1 evaluation per monomial at 1536
bits, no exact recurrences, no composition), and check that the result overlaps the production record (exact R1 + R2 I0 reduction). The two
routes share only the field algebra (fields, products, derivatives, canonical form) and differ in the integration arithmetic.
Usage: legqs_secondpath.py <ID> <F record> <outdir> [norm labels, default G0,rF,G1,P2]"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import legqs_norms as LN

def run(ID, record, outdir, labels=('G0', 'rF', 'G1', 'P2'), prec=1024):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir)
    F, raw = LN.load_F(record); delta = Q(raw['delta'])
    D = {(0, 0): F}
    for d in range(2):
        for nx in range(d + 2):
            D[d + 1, nx] = LN.canon_t(LN.diff_t(D[d, 0], d, 'y', delta) if nx == 0 else LN.diff_t(D[d, nx - 1], d, 'x', delta))
    print(f'derivatives recomputed ({time.monotonic()-t0:.0f}s)', flush=True)
    prod = json.loads((outdir / f'{ID}_legqs_norms.json').read_text())['norms']
    LN.Accumulator.BALL_DEGREE = 0
    out = {'id': ID, 'record': str(record), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'method': __doc__,
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'norms': {}}
    tables = LN.ScaleTables()
    for label, d, a, tp, ser in LN.STANDARD:
        if label not in labels: continue
        r = LN.norm_t(D, d, delta, a, tp, ser, 56, label, tables, prec)
        p = prod.get(label, {})
        ok = None
        if r['status'] == 'FINITE' and p.get('status') == 'FINITE':
            ok = bool(arb(r['norm_lower']) <= arb(p['norm_upper']) and arb(p['norm_lower']) <= arb(r['norm_upper']))
        out['norms'][label] = {'second_path': r, 'production_lower': p.get('norm_lower'), 'production_upper': p.get('norm_upper'), 'intervals_overlap': ok}
        print(f"{label}: second path {r.get('norm_lower_ball','INFINITE')[:40]} | production {str(p.get('norm_lower'))[:40]} | overlap {ok} ({r.get('elapsed_seconds',0):.0f}s; ball groups {r.get('n_ball_groups')})", flush=True)
        (outdir / f'{ID}_legqs_secondpath.json').write_text(json.dumps(out, indent=1) + '\n')
    out['elapsed_seconds'] = round(time.monotonic() - t0, 1); (outdir / f'{ID}_legqs_secondpath.json').write_text(json.dumps(out, indent=1) + '\n')
    print(f'DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3], tuple(sys.argv[4].split(',')) if len(sys.argv) > 4 else ('G0', 'rF', 'G1', 'P2'))
