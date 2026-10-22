"""Compact table from runs/elliptic_defect.log (code/elliptic_defect.py output): per state and finite-difference step, the sampled regional maxima
of |E| (r < 1 / 1-10 / 10-100 / >= 100), the grid maximum of the pointwise ratio |E|/N_E, the largest regional ratio max|E|/max|Omega| and the
largest regional ratio max|E|/max|R_Theta| outside r < 1. Usage: python3 code/elliptic_summary.py runs/elliptic_defect.log"""
import sys, collections
rows = collections.defaultdict(list)
for line in open(sys.argv[1]):
    p = line.split()
    if len(p) >= 13 and p[4] in ('1e-03', '3e-04', '1e-04'):
        rows[(p[0], p[1], p[2], p[3], p[4])].append(p[5:])
print("state                      N   M  beta   h       max|E| by region: r<1 / 1-10 / 10-100 / >=100        grid max(|E|/N_E)  max_reg max|E|/max|Om|  max_reg(outside r<1) max|E|/max|R_T|")
for k, v in rows.items():
    mE = [float(r[1]) for r in v]; rat = max(float(r[2]) for r in v); qO = max(float(r[4]) for r in v)
    qT = max(float(r[7]) for r in v if r[0] != 'r<1')
    print(f"{k[0]:26s} {k[1]:>3s} {k[2]:>3s} {k[3]:>5s}  {k[4]:6s}  " + ' / '.join(f'{x:.2e}' for x in mE) + f"    {rat:.2e}           {qO:.2e}             {qT:.2e}")
