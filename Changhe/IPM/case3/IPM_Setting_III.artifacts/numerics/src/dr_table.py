"""dr_table.py -- trajectory comparison table from DR logs: columns at common tau values (linear interpolation in tau).  usage: python3 src/dr_table.py tag1 tag2 ... [taus=0,2,5,...]"""
import sys, numpy as np
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
taus = [float(x) for x in kw.get('taus', '0,1,2,3,5,7.5,10,12.5,15,17.5,20,22.5,25,27.5,30').split(',')]
cols = kw.get('cols', 'c,cw,a0s,bc,ec,rt1,rt10,b3,b3p,T').split(',')
idx = dict(tau=0, c=1, cw=2, cx=3, a0s=4, rt1=5, rt10=6, rt100=7, rtall=8, bt=9, bc=10, ec=11, A1=12, A3=13, K=14, b3=15, b3p=16, T=17,
           at=18, btau=19, etau=20, I1=21, I10=22, I100=23, Iid=24, pd1=25, pdall=26)      # columns after the first '|' (new logs): a_tau b_tau/a0 e_tau/a0 I_1 I_10 I_100 I_0-(c+a0/4) | projdefect r<=1, all
data = {}
for tag in args:
    rows = []
    for line in open(f'runs/{tag}.log'):
        if line.startswith('#') or not line.strip(): continue
        parts = line.split('|'); p = parts[0].split()
        try:
            row = [float(x) for x in p[:18]]
            if len(parts) >= 2: row += [float(x) for x in parts[1].split()[:7]]
            if len(parts) >= 3: row += [float(x) for x in parts[2].split()[:2]]
            rows.append(row + [float('nan')] * (27 - len(row)))
        except ValueError: pass
    data[tag] = np.array(rows)
print('tau      ' + ' '.join(f'{tag:>14s}' for tag in args) + '   (per column: ' + ','.join(cols) + ')')
for col in cols:
    print(f'--- {col}')
    for tau in taus:
        out = []
        for tag in args:
            A = data[tag]
            if len(A) == 0 or tau > A[-1, 0] + 0.3: out.append(' ' * 14); continue
            if tau < A[0, 0] - 1e-9: out.append(' ' * 14); continue
            out.append(f'{np.interp(tau, A[:, 0], A[:, idx[col]]):+14.6e}')             # linear interpolation in tau between logged rows
        print(f'{tau:7.2f}  ' + ' '.join(out))
