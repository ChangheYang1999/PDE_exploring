"""eqb_table.py -- per-iteration table of the equal-budget comparison (runs/eqb.sh; shift 6): obj, obj/Nq (mean squared weighted residual per
residual point), max|wRG|, max|wRF|, |f| (fixed-point defect), m (strain mismatch) for K 24 / 32 / 40 at the same iteration count.
Usage: python3 code/eqb_table.py [runs/eqb24.log runs/eqb32.log runs/eqb40.log]"""
import sys, re
files = sys.argv[1:] or ['runs/eqb24.log', 'runs/eqb32.log', 'runs/eqb40.log']
pat = re.compile(r"in\s+(\d+) .*?obj=([0-9.e+-]+) \|f\|=([0-9.e+-]+) ell=([0-9.e+-]+) m=([+-][0-9.e+-]+) max\|wRG\|=([0-9.e+-]+) max\|wRF\|=([0-9.e+-]+) unf=(\d+)")
Nq = {12: 392 * 24, 16: 392 * 32, 24: 392 * 48, 32: 392 * 64, 40: 392 * 80}     # Nc 392 (Nt 56, ngc 7) x Nphi_res = 2K
rows = {}
for f in files:
    txt = open(f).read(); mk = re.search(r'# basis Nt=\d+ K=(\d+)', txt); K = int(mk.group(1)) if mk else int(re.search(r'(\d+)\.log', f).group(1)); rows[K] = []
    for line in txt.splitlines():
        m = pat.search(line)
        if m:
            rows[K].append(tuple(float(v) for v in m.groups()))
Ks = sorted(rows)
print('| it | ' + ' | '.join(f'K {K}: obj, obj/Nq, max wRG, max wRF, |f|, m' for K in Ks) + ' |')
print('|---|' + '---|' * len(Ks))
n = max(len(rows[K]) for K in Ks)
for it in range(n):
    cells = []
    for K in Ks:
        if it < len(rows[K]):
            _, obj, fn, ell, mm, rg, rf, unf = rows[K][it]
            cells.append(f'{obj:.3e}, {obj / Nq[K]:.2e}, {rg:.2e}, {rf:.2e}, {fn:.1e}, {mm:+.1e}' + (f' (unf {int(unf)})' if unf else ''))
        else:
            cells.append('')
    print(f'| {it} | ' + ' | '.join(cells) + ' |')
for K in Ks:
    if rows[K]:
        objs = [r[1] for r in rows[K]]; last = objs[-1]; i_pl = next((i for i, o in enumerate(objs) if o < 1.05 * last), len(objs) - 1)
        print(f'K {K}: final obj {last:.4e} (per point {last / Nq[K]:.3e}), within 5 percent of the final value from iteration {i_pl} on; min obj {min(objs):.4e} at iteration {objs.index(min(objs))}; final max|wRG| {rows[K][-1][5]:.3e} max|wRF| {rows[K][-1][6]:.3e}')
