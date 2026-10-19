"""Parse mc_curve logs (lines '[mc] s = ...') into a markdown table for NUM_REPORT 3.17 item 4 (fixed-s convergence table).
Usage: python3 src/fixs_table.py <label:logfile> [...]"""
import sys, re
rows = []
for arg in sys.argv[1:]:
    label, path = arg.split(':', 1)
    for line in open(path):
        if not line.startswith('[mc] s ='): continue
        g = lambda pat: re.search(pat, line).group(1)
        rows.append((label, g(r'c_l ([0-9.]+)'), g(r'x\* ([0-9.]+)'), g(r'h\(P\)-1 ([+-][0-9.e-]+)'), g(r'rms\(all\) ([0-9.e-]+)'), g(r'max ([0-9.e-]+)'),
                     g(r'\[0,0.5\) ([0-9.e/-]+)'), g(r'\[0.5,1\) ([0-9.e/-]+)'), g(r'\[1,2\) ([0-9.e/-]+)'), g(r'\[2,4\) ([0-9.e/-]+)'),
                     g(r'r<=2 ([0-9.e/-]+)'), g(r'2-10 ([0-9.e/-]+)'), g(r'10-100 ([0-9.e/-]+)'), g(r'>100 ([0-9.e/-]+)')))
print('| grid, R | c_l | x* | h(P)-1 | rms(all) | max | |X-P|<0.5 rms/max | 0.5-1 | 1-2 | 2-4 | r<=2 | 2-10 | 10-100 | >100 |')
print('|' + '---|' * 14)
for r in rows: print('| ' + ' | '.join(r) + ' |')
