"""NC-T-ORIGIN-INV seven-cell test (theory_v03 section 9 item 1) for a legqs candidate from its exact F record (lane c1-n3).
N_a(F) = ||(1+r^2)^((2-a)/2) Delta F||_2 (NORM-T-WLAP-v1); the projection of Delta F on the angular modes 1 and 3 gives a lower bound
N_a^(1,3) <= N_a (orthogonal modes). N_a is nonincreasing in a, so the value at the right end h of a cell [a_left, h] bounds N_a from
below on the whole cell; the cell is excluded when N_h^(1,3) exceeds the cell threshold (theory_v03 section 5 table, rounded up:
15.88162, 8.716729, 4.799949, 2.565236, 1.263642, 0.5028299, 0.06411577 for the cells ending at 1/4, 1/2, 3/4, 1, 5/4, 3/2, 1 + 1/c;
the last cell is tested with the value at a = 7/4 >= 1 + 1/c). Delta F = F_xx + F_yy from the F record by two exact derivatives
(legqs_norms.diff_t); the weight (1-t)^(a-2) is the a_shift of the degree-2 form. Usage: legqs_cells.py <ID> <F record> <outdir>"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import legqs_norms as LN

CELLS = [(Q(0), Q(1, 4), '15.88162'), (Q(1, 4), Q(1, 2), '8.716729'), (Q(1, 2), Q(3, 4), '4.799949'), (Q(3, 4), Q(1), '2.565236'),
         (Q(1), Q(5, 4), '1.263642'), (Q(5, 4), Q(3, 2), '0.5028299'), (Q(3, 2), Q(7, 4), '0.06411577')]

def run(ID, record, outdir, modes=(1, 3), prec=1024):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir)
    F, raw = LN.load_F(record); delta = Q(raw['delta'])
    D1y = LN.canon_t(LN.diff_t(F, 0, 'y', delta)); D1x = LN.canon_t(LN.diff_t(F, 0, 'x', delta))
    Fyy = LN.diff_t(D1y, 1, 'y', delta); Fxx = LN.diff_t(D1x, 1, 'x', delta)
    Lap = LN.canon_t(LN.plus_t((1, Fxx), (1, Fyy)))
    Lap13 = {k: p for k, p in Lap.items() if k[2] in modes}
    print(f'Laplacian: {len(Lap)} components, modes {sorted({k[2] for k in Lap})[:6]}..., projected {len(Lap13)} components ({time.monotonic()-t0:.0f}s)', flush=True)
    tables = LN.ScaleTables(); rows = []
    for a_left, h, thr in CELLS:
        r = LN.normsq_t([(1, Lap13)], 2, delta, a_shift=h - 2, tables=tables, prec=prec)
        if r['status'] != 'FINITE':
            rows.append({'cell': [str(a_left), str(h)], 'status': 'INFINITE'}); print(f'h = {h}: INFINITE'); continue
        Nh = r['hi'].sqrt(); lb = Nh.lower(); ratio = arb(lb) / arb(thr)
        rows.append({'cell': [str(a_left), str(h)], 'N_h_modes13_sq_ball': r['hi'].str(30), 'N_h_modes13_LB': str(lb), 'threshold_left_end': thr,
                     'ratio_LB_over_threshold': ratio.str(10), 'excluded': bool(ratio.lower() > 1), 'n_groups': r['n_groups'], 'ball_radius': r['S_ball_radius']})
        print(f'h = {h}: N_h(modes {modes}) >= {Nh.str(15)}  threshold {thr}  ratio {ratio.str(6)}  excluded {ratio.lower() > 1}', flush=True)
    out = {'id': ID, 'record': str(record), 'source_sha256': raw.get('source_sha256'), 'modes': list(modes), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'method': __doc__, 'cells': rows,
           'all_excluded': all(r.get('excluded') for r in rows), 'elapsed_seconds': round(time.monotonic() - t0, 1)}
    (outdir / f'{ID}_legqs_cells.json').write_text(json.dumps(out, indent=1) + '\n')
    print(f'all seven cells excluded: {out["all_excluded"]}; DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3])
