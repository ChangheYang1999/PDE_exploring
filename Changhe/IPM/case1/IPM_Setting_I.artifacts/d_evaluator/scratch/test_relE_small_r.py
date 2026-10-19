# relE by band for a manufactured growing field (E exact = 0): is the r < 0.01 relE of order 1e-4 an evaluator artifact?
import numpy as np, sys
from vpolar import LogGrid
from vresid import evaluate
k = 0.18
for N, Nt in ((6000, 64), (9000, 64), (9000, 256)):
    g = LogGrid(N, 7.652e-4, 7.652e4)
    th = 2 * np.pi * np.arange(Nt) / Nt
    r = g.r
    X = r[:, None] * np.cos(th)[None, :]; Y = r[:, None] * np.sin(th)[None, :]
    rho = X ** 2 * Y * (1 + (X ** 2 + Y ** 2) / 50.) ** ((k - 3) / 2) * (1 + 0.3 * X ** 2 / (1 + X ** 2 + Y ** 2))
    ev = evaluate(rho, g, th, c_l=None)
    out = []
    for a, b in ((r[0], 1e-3), (1e-3, 3e-3), (3e-3, 1e-2), (1e-2, 1), (1, 10), (10, 1e3), (1e3, r[-1])):
        sel = (r >= a) & (r <= b); sel[:8] = False; sel[-8:] = False
        if sel.sum() == 0: continue
        out.append('[%.1e,%.1e] %.1e' % (a, b, np.abs(ev.E[sel]).max() / np.abs(ev.dxrho[sel]).max()))
    i = np.unravel_index(np.argmax(np.abs(ev.E[8:-8]) / (np.abs(ev.dxrho[8:-8]).max(axis=1, keepdims=True))), ev.E[8:-8].shape)
    print(N, Nt, ' | '.join(out), '| worst r', r[8 + i[0]], flush=True)
