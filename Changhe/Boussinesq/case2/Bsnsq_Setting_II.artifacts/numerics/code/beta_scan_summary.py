"""Compact table from runs/beta_scan.log (code/beta_scan.py output): per state, the stored beta, the rebuilt and stored norms, the group norms at the
stored beta, the ratios |F_group|(delta = +-0.01) / |F_group|(0) for the standard and tail rows, the central-difference derivatives d|F_group|^2/dbeta
(h = 0.001) and the coefficients of delta^2 of the squared group norms (from the delta = +-0.01 values) with their shares.
Usage: python3 code/beta_scan_summary.py runs/beta_scan.log"""
import sys, re
blocks = open(sys.argv[1]).read().split('state ')[1:]
print("state                      beta_stored  |F| rebuilt   |F| stored    |F_std|      |F_tail|     |F_orig|    std x(+-0.01)      tail x(+-0.01)   d|F|^2/dbeta: all / std / tail / orig (h=1e-3)        delta^2 coeff: std / tail / orig (shares pct)")
for b in blocks:
    name = b.split(':')[0]; m = re.search(r'beta_stored=([0-9.]+)', b); beta = float(m.group(1))
    m = re.search(r'\|F\| rebuilt ([0-9.e+-]+) stored ([0-9.e+-]+); group norms at stored beta: std ([0-9.e+-]+) origin ([0-9.e+-]+) tail ([0-9.e+naN-]+)', b)
    Freb, Fst, g_std, g_or, g_tail = [float(x) for x in m.groups()]
    rows = {}
    for ln in b.split('\n'):
        mm = re.match(r'\s+([0-9.]+)\s+([+-][0-9.]+)\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s+([0-9.e+naN-]+)\s+([0-9.e+-]+)', ln)
        if mm: rows[float(mm.group(2))] = [float(x) for x in mm.groups()[2:]]   # all, std, origin, tail, all_minus_origin
    d = re.search(r'\(h=0.001\): all ([+-][0-9.e+-]+) std ([+-][0-9.e+-]+) origin ([+-][0-9.e+-]+) tail ([+-]?[0-9.e+naN-]+)', b)
    der = [float(x) for x in d.groups()]
    def c2(idx):   # coefficient of delta^2 of |F_group|^2 from the symmetric pair at +-0.01 (F affine in beta => exact)
        return (rows[0.01][idx] ** 2 + rows[-0.01][idx] ** 2 - 2 * rows[0.0][idx] ** 2) / 2 / 1e-4
    cs, ct, co = c2(1), c2(3), c2(2); tot = cs + ct + co
    print(f"{name:26s} {beta:11.6f}  {Freb:.6e}  {Fst:.6e}  {g_std:.4e}  {g_tail:.4e}  {g_or:.3e}  {rows[0.01][1]/g_std:6.3f} / {rows[-0.01][1]/g_std:6.3f}  {rows[0.01][3]/g_tail:8.1f} / {rows[-0.01][3]/g_tail:8.1f}  {der[0]:+.3e} / {der[1]:+.3e} / {der[3]:+.3e} / {der[2]:+.3e}   {cs:.3e} / {ct:.3e} / {co:.3e} ({100*cs/tot:.3f} / {100*ct/tot:.2f} / {100*co/tot:.2f})")
