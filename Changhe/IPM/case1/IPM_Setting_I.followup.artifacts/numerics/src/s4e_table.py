"""Table of SPEC S4 (e) rows from runs/s4e_<tag>.json files (one per converged state) and the S4 (e) reading.
Usage: python3 src/s4e_table.py tag1 tag2 ...   (prints a markdown table; writes runs/s4e_table.md)"""
import sys, json, numpy as np
LANE = '.'
rows = [json.load(open(f'{LANE}/runs/s4e_{t}.json')) for t in sys.argv[1:]]
cols = [('tag', 'tag', '{}'), ('(N,M)', lambda r: f"({r['N']},{r['M']})", '{}'), ('L', 'L', '{:g}'), ('|F|_psi_2', 'F_psi_2', '{:.2e}'), ('c_l', 'c_l', '{:.8f}'),
        ('x*', 'xstar', '{:.6f}'), ('g(P)', 'gP', '{:.5f}'), ('h(P)-1', 'hP_minus_1', '{:+.1e}'), ('ident', 'identity_defect', '{:+.1e}'), ('d1+A', 'd1_plus_A', '{:+.1e}'),
        ('d3', 'd3', '{:.6f}'), ('d5', 'd5', '{:.5f}'), ('d7', 'd7', '{:.4f}'), ('B3 orig', 'B3_orig', '{:.4f}'), ('B3 ibp', 'B3_ibp', '{:.4f}'),
        ('med orig [min,max]', lambda r: f"{r['median_orig']:.4f} [{r['orig_min']:.3f},{r['orig_max']:.3f}]", '{}'),
        ('med ibp [min,max]', lambda r: f"{r['median_ibp']:.4f} [{r['ibp_min']:.3f},{r['ibp_max']:.3f}]", '{}'),
        ('rem7 exp', 'remainder7_fitted_exponent', '{:.2f}'), ('rem7/x^(7+b)', 'remainder7_max_over_x7+beta', '{:.2e}'), ('compat a_m\'(0) m>=2', 'compat_am_prime0_max_m>=2', '{:.1e}')]
hdr = '| ' + ' | '.join(c[0] for c in cols) + ' |\n|' + '---|' * len(cols) + '\n'
lines = []
for r in rows:
    vals = []
    for name, key, fmt in cols:
        v = key(r) if callable(key) else r.get(key)
        vals.append(fmt.format(v) if v is not None and not (isinstance(v, float) and np.isnan(v)) else 'n/a')
    lines.append('| ' + ' | '.join(vals) + ' |')
table = hdr + '\n'.join(lines) + '\n'
# reading: B_3 resolved if every value (both forms, all states) within 0.03 of the median and d3, d5, d7 agree to 1e-3 relative
allB = [r['B3_orig'] for r in rows] + [r['B3_ibp'] for r in rows] + [r['median_orig'] for r in rows] + [r['median_ibp'] for r in rows]
med = float(np.median(allB)); spread = float(np.max(np.abs(np.array(allB) - med)))
def relspread(k): v = np.array([r[k] for r in rows]); return float(np.max(np.abs(v - np.median(v))) / max(abs(np.median(v)), 1e-300))
rd = {k: relspread(k) for k in ('d3', 'd5', 'd7')}
reading = 'B_3 resolved on this family' if (spread <= 0.03 and all(x <= 1e-3 for x in rd.values()) and len(rows) >= 5) else 'not resolved'
table += f'\nB_3 values: median {med:.4f}, max deviation {spread:.4f} (criterion 0.03); relative spreads d3 {rd["d3"]:.1e}, d5 {rd["d5"]:.1e}, d7 {rd["d7"]:.1e} (criterion 1e-3); states {len(rows)} (criterion 5). Reading: {reading}.\n'
print(table); open(f'{LANE}/runs/s4e_table.md', 'w').write(table)
