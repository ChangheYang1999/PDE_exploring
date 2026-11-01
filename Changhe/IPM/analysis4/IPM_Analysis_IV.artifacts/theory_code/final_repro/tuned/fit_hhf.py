"""Growth fits for hh_float.py outputs (NUMERICAL EVIDENCE only).  The l1 norms oscillate within each period of Q orders,
so the fits use block maxima: m_j = max log10||f_n|| over the block jQ < n <= (j+1)Q, fitted linearly in the block end
n_j = (j+1)Q, m_j = n_j log10 A + C, on the blocks with n_j >= lo (lo = 100, 150, 200), separately for the density f and the
stream g (unit amplitude).  The spread over lo is a crude error indicator.  Apparent exterior radius A^(1/delta), times
|eps|^(1/delta).  usage: fit_hhf.py [--lo=100,150,200] file ..."""
import re, sys
import numpy as np
LOS = (100, 150, 200)
args = sys.argv[1:]
if args and args[0].startswith('--lo='):
    LOS = tuple(int(x) for x in args[0][5:].split(','))
    args = args[1:]
for fn in args:
    hdr = open(fn).readline()
    m = re.search(r'Q=(\d+) h=(\d+)', hdr)
    if not m:
        print(fn, 'no header'); continue
    Q, h = int(m.group(1)), int(m.group(2)); dl = 2 * h / Q
    d = {}
    for line in open(fn):
        if line.startswith('n '):
            a = line.split()
            d[int(a[1])] = (float(a[2]), float(a[3]))
    N = max(d)
    if N < 200:
        print(fn, 'too short', N); continue
    blocks = []
    for j in range(N // Q):
        ns = [n for n in range(j * Q + 1, (j + 1) * Q + 1) if n in d]
        if len(ns) == Q:
            blocks.append(((j + 1) * Q, max(d[n][0] for n in ns), max(d[n][1] for n in ns if d[n][1] == d[n][1])))
    B = np.array(blocks)
    res = []
    for lo in LOS:
        s = B[:, 0] >= lo
        if s.sum() < 4:
            continue
        X = np.vstack([B[s, 0], np.ones(s.sum())]).T
        cf, *_ = np.linalg.lstsq(X, B[s, 1], rcond=None)
        cg, *_ = np.linalg.lstsq(X, B[s, 2], rcond=None)
        rms = np.sqrt(np.mean((X @ cf - B[s, 1]) ** 2))
        res.append((lo, 10 ** cf[0], 10 ** cg[0], rms))
    Af = [r[1] for r in res]
    print('%s Q=%d h=%d N=%d | ' % (fn, Q, h, N) + ' | '.join('n>=%d A_f=%.4f A_g=%.4f rms=%.2f' % r for r in res)
          + ' | radius_f %.3g to %.3g' % (min(Af) ** (1 / dl), max(Af) ** (1 / dl)))
