"""axis_neighbourhood.py -- absolute residual maxima on neighbourhoods where the ratio denominators vanish (lead 00:40Z item 2): strips |y| <= eps and
|x| <= eps (within r <= 100) and discs r <= eps, eps = 1e-3, 1e-2, 1e-1; max |R| (absolute), with location; also max |R| on the axes themselves
(th = 0 and pi/2 exactly, r in [1e-4, 100]).  Sampling: 400 log-spaced radii x 48 angles inside each strip (angles th in [0, eps/r] or near pi/2),
plus the axes.  usage: python3 src/axis_neighbourhood.py states..."""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
rr = np.exp(np.linspace(np.log(1e-4), np.log(100.0), 400))
for f in [a for a in sys.argv[1:] if '=' not in a]:
    S = qdiag.State(f); out = [f"{f.split('/')[-1]} (N={S.N}, a0={S.a0:.5f}):"]
    ox = S.ev(rr, np.zeros_like(rr)); oy = S.ev(rr, np.full_like(rr, math.pi / 2))
    ix, iy = np.argmax(np.abs(ox['R'])), np.argmax(np.abs(oy['R']))
    out.append(f"  x-axis (th = 0): max|R| = {abs(ox['R'][ix]):.3e} at r = {rr[ix]:.3g};  y-axis (th = pi/2): max|R| = {abs(oy['R'][iy]):.3e} at r = {rr[iy]:.3g};  |R|/N_f on the y-axis max = {np.max(np.abs(oy['R'])/oy['Nf']):.3e}")
    for eps in [1e-3, 1e-2, 1e-1]:
        # strip |y| <= eps: angles th in (0, asin(min(1, eps/r))]; strip |x| <= eps: th in [acos(min(1, eps/r)), pi/2)
        best = {}
        for name in ['|y|<=eps', '|x|<=eps', 'disc r<=eps']:
            m = -1.0; loc = None
            if name == 'disc r<=eps':
                rs = rr[rr <= eps]; th = (np.arange(48) + 0.5) * math.pi / 96
                RR, TT = np.meshgrid(rs, th, indexing='ij'); o = S.ev(RR, TT); i = np.unravel_index(np.argmax(np.abs(o['R'])), o['R'].shape)
                m, loc = abs(o['R'][i]), (RR[i], TT[i])
            else:
                for r in rr:
                    a = math.asin(min(1.0, eps / r))
                    th = (np.arange(48) + 0.5) / 48 * a if name == '|y|<=eps' else math.pi / 2 - (np.arange(48) + 0.5) / 48 * a
                    o = S.ev(np.full_like(th, r), th); j = np.argmax(np.abs(o['R']))
                    if abs(o['R'][j]) > m: m, loc = abs(o['R'][j]), (r, th[j])
            best[name] = (m, loc)
        out.append(f"  eps = {eps:g}: " + "; ".join(f"{k}: max|R| = {v[0]:.3e} at (r = {v[1][0]:.3g}, th = {v[1][1]:.4f})" for k, v in best.items()))
    print("\n".join(out), flush=True)
