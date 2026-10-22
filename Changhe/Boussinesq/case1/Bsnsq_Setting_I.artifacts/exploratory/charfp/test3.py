import sys, math, numpy as np, torch
from charlib import *
f = sys.argv[1]
P, cT, cO, NT, NO, K = load_coefs(f)
tab = VelTable(P, cO, NO, K)
a0 = 52.82895; sc = -2.0 / tab.c
for (r0, ph) in [(1.0, 85.0), (0.3, 20.0), (0.6, 10.0), (2.0, 89.0)]:
    x0, y0 = r0 * math.cos(math.radians(ph)), r0 * math.sin(math.radians(ph))
    e = 1e-4
    pts = torch.tensor([[x0, y0], [x0 + e, y0], [x0 - e, y0], [x0, y0 + e], [x0, y0 - e]], dtype=DT)
    o = reconstruct(tab, pts, a0, h=0.01, r_stop=3e-4, scale=sc)
    W, DW = tab.W_DW(pts[:1], sc)
    Thx_fd = (o['Th'][1] - o['Th'][2]) / (2 * e); Thy_fd = (o['Th'][3] - o['Th'][4]) / (2 * e)
    Omx_fd = (o['Om'][1] - o['Om'][2]) / (2 * e); Omy_fd = (o['Om'][3] - o['Om'][4]) / (2 * e)
    w1, w2 = float(W[0, 0]), float(W[0, 1])
    RT = w1 * Thx_fd + w2 * Thy_fd - (P.beta - 2) * o['Th'][0]
    NT = abs(w1 * Thx_fd) + abs(w2 * Thy_fd) + abs((P.beta - 2) * o['Th'][0])
    RO = w1 * Omx_fd + w2 * Omy_fd + o['Om'][0] - o['Thx'][0]
    NOm = abs(w1 * Omx_fd) + abs(w2 * Omy_fd) + abs(o['Om'][0]) + abs(o['Thx'][0])
    print('r %.2f phi %.0f: Thx q %.8e fd %.8e | Thy q %.8e fd %.8e | RT/NT %.2e RO/NO %.2e | Om %.6e' % (r0, ph, o['Thx'][0], Thx_fd, o['Thy'][0], Thy_fd, RT / NT, RO / NOm, o['Om'][0]))
