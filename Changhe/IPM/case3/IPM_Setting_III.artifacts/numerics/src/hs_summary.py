"""one-line summary per HS log from its '# RESULT' json line.  Usage: python3 src/hs_summary.py runs/hsE_*.log"""
import sys, json
print("# tag                      NxM    c      hstep  GN node|R_h|max   sampled |R_h|/N_f by region (<.1, .1-1, 1-100, >=100; y-axis included for hsE/hsF, sampled_table default since 08:55Z)   E = e/a0    B          smin2(rows)/smax   D = c+cH-1   wall")
for f in sys.argv[1:]:
    res = None
    for line in open(f):
        if line.startswith('# RESULT'): res = json.loads(line[len('# RESULT'):])
    if res is None: print(f, 'no result'); continue
    sm = ' '.join('%.1e' % r[3] for r in res['sampled'])
    print(f"{res['tag']:26s} {res['N']:3d}x{res['M']:<3d} {res['c']:.3f}  {res.get('hstep','x'):5s}  {res['nodes_Fmax']:.1e}          {sm:40s}   {res['E']:+.3f}    {res['B']:+.3f}    {res['smin2_rows_only']/res['smax']:.1e}            {res.get('centre_defect_single', float('nan')):+.1e}    {res['wall']:.0f}s")
