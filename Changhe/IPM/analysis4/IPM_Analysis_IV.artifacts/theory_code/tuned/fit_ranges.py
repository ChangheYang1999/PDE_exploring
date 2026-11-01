"""Full-precision density A_f of the block-maximum fits of fit_hhf.py (same blocks and windows), with ranges rounded
outward to four significant digits (NUMERICAL EVIDENCE only).  usage: fit_ranges.py [--lo=100,200,300,400] file ..."""
import math, re, sys
import numpy as np
LOS = (100, 200, 300, 400)
args = sys.argv[1:]
if args and args[0].startswith('--lo='):
    LOS = tuple(int(x) for x in args[0][5:].split(','))
    args = args[1:]
def out(x, up):
    e = math.floor(math.log10(abs(x))) - 3
    v = (math.ceil if up else math.floor)(x / 10 ** e)
    return f"{v * 10 ** e:.{max(0, -e)}f}"
for fn in args:
    Q = int(re.search(r'Q=(\d+)', open(fn).readline()).group(1))
    d = {}
    for line in open(fn):
        if line.startswith('n '):
            a = line.split()
            d[int(a[1])] = float(a[2])
    N = max(d)
    B = np.array([((j + 1) * Q, max(d[n] for n in range(j * Q + 1, (j + 1) * Q + 1)))
                  for j in range(N // Q) if all(n in d for n in range(j * Q + 1, (j + 1) * Q + 1))])
    A = []
    for lo in LOS:
        s = B[:, 0] >= lo
        X = np.vstack([B[s, 0], np.ones(s.sum())]).T
        cf, *_ = np.linalg.lstsq(X, B[s, 1], rcond=None)
        A.append(10 ** cf[0])
    print(fn, ' '.join(f'{a:.12g}' for a in A), '| range', out(min(A), False), 'to', out(max(A), True),
          '| spread %.4f%%' % ((max(A) / min(A) - 1) * 100))
