"""Collect runs/scan_signed_*.json (and the control file) into one Markdown table (shift 7, NUM_REPORT 7n)."""
import json, glob
rows = []
files = ['runs/scan_signed_control.json'] + sorted(glob.glob('runs/scan_signed_[0-9]*.json'))
for fn in files:
    d = json.load(open(fn))
    for r in d['results']:
        lob = ' ; '.join(f"{l['a']:+g} at y {l['y0']:g} (s {l['s']:g})" for l in r['lobes'])
        if r['unfinished'] > 0:
            cout = 'undefined (transport incomplete)'; ratio = '-'
        else:
            cout = f"{r['c_out']:+.4f}"; ratio = f"{r['ratio']:+.3f}"
        if r['unfinished'] > 0:
            sign = 'not meaningful (incomplete transport)'
        else:
            sign = 'G >= 0' if r['negfrac_G'] == 0 else f"G < 0 on {100*r['negfrac_G']:.1f} percent of the points (min {r['G_min']:.3g} at r {r['G_min_at'][0]:.2f}, y {r['G_min_at'][1]:.2f})"
        rows.append((lob, r['c_in'], r['beta'], r['A'], cout, ratio, sign, r['unfinished'], r['steps'], fn.split('/')[-1]))
print('| lobes (relative amplitude a_i at y_i, width s_i) | c_in | beta | A | c_out | c_out/c_in | sign of transported G | unfinished | steps | file |')
print('|---|---|---|---|---|---|---|---|---|---|')
for row in rows:
    print(f"| {row[0]} | {row[1]:g} | {row[2]:.3f} | {row[3]:.3f} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} |")
