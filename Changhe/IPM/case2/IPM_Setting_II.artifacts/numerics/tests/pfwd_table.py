"""Table of forward-evolution states: python3 tests/pfwd_table.py runs/pfwd/scan_p05_*.npz"""
import sys, json, numpy as np
rows = []
for fn in sys.argv[1:]:
    try:
        d = np.load(fn); a = json.loads(str(d['args'])); h = json.loads(str(d['hist']))[-1]
    except Exception as e:
        print(fn, 'ERR', e); continue
    r = h['ring20']
    rows.append((a['kind'], str(a['par']), a['p'], h['s'], h['dgds'], r['m1'], r['m2'], r['e1_deg'], h['c_moment'], h['c_target'], h['d_moment'],
                 h['R_rel_bands'].get('1-100', float('nan')), h['R_rel_bands'].get('100-10000', float('nan')), fn.split('/')[-1]))
print("%-10s %-8s %5s %6s %8s | %8s %8s %7s | %8s %8s %8s %8s | %7s %7s  file" % ('kind', 'par', 'p', 's', 'dg/ds', 'm1', 'm2', 'e1deg', 'c_mom', 'c_tgt', 'deficit', 'd_mom', 'R1-100', 'R>100'))
for r in sorted(rows):
    print("%-10s %-8s %5.2f %6.1f %8.1e | %8.5f %8.5f %7.2f | %8.5f %8.5f %8.5f %8.1e | %7.1e %7.1e  %s" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[9] - r[8], r[10], r[11], r[12], r[13]))
