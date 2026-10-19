"""Verifier's check of (Hmin) on a field export (verifier): zeros of W = c_l X + U in the closed first quadrant should be
only 0 and P = (x*, 0). Own inverse via vcand.main (only the sampled rho is read).
  - x axis: sign changes of W_1(x, 0);  y axis: min over y of W_2(0, y)/y and its sign changes;
  - open quadrant: grid cells (r_i, r_i+1) x (t_j, t_j+1) where both W_1 and W_2 change sign;
  - min of |W|/(c_l |X|) outside |X - P| < delta (delta = 1, 0.3, 0.1), with location.
Radial ends (8 points each side) are excluded. Grid evidence only.
Usage: python3 vzeros.py field.npz Mmax out.json
"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vcand import main as vcand_main


def crossings(x, f):
    s = np.sign(f)
    i = np.nonzero(s[:-1] * s[1:] < 0)[0]
    return [float(x[k] - f[k] * (x[k + 1] - x[k]) / (f[k + 1] - f[k])) for k in i]


def main(path, Mmax, outp):
    out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
    r = ev.r if hasattr(ev, 'r') else None
    from vcand import load_modes
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    nq = Nt // 4
    t = th[:nq + 1]
    ct, st = np.cos(t)[None, :], np.sin(t)[None, :]
    st[0, 0] = 0.0
    ct[0, -1] = 0.0
    Ur, Ut = ev.Ur[:, :nq + 1], ev.Ut[:, :nq + 1]
    U1 = Ur * ct - Ut * st
    U2 = Ur * st + Ut * ct
    cl = ev.c_l
    R2 = r[:, None]
    X1, X2 = R2 * ct, R2 * st
    W1, W2 = cl * X1 + U1, cl * X2 + U2
    trim = 8
    sl = slice(trim, len(r) - trim)
    rs = r[sl]
    res = dict(file=path, Mmax=Mmax, c_l=cl, x_star=out.get('x_star'))
    res['W1_x_axis_zeros'] = crossings(rs, W1[sl, 0])
    w2y = W2[sl, -1] / rs
    res['W2_over_y_on_y_axis_min'] = float(w2y.min())
    res['W2_over_y_on_y_axis_argmin_y'] = float(rs[np.argmin(w2y)])
    res['W2_y_axis_zeros'] = crossings(rs, W2[sl, -1])
    # open quadrant cells with sign change of both components
    A, B = W1[sl, 1:nq], W2[sl, 1:nq]          # open quadrant columns
    def chg(Z):
        c = np.stack([Z[:-1, :-1], Z[1:, :-1], Z[:-1, 1:], Z[1:, 1:]])
        return (c.max(0) > 0) & (c.min(0) < 0)
    both = chg(A) & chg(B)
    ii, jj = np.nonzero(both)
    cells = [dict(r=float(rs[i]), theta=float(t[1 + j]), x=float(rs[i] * np.cos(t[1 + j])),
                  y=float(rs[i] * np.sin(t[1 + j]))) for i, j in zip(ii, jj)]
    res['open_quadrant_cells_both_change'] = cells[:50]
    res['n_open_cells'] = len(cells)
    # min |W|/(c_l |X|) away from P (closed quadrant incl. axes)
    xs = out.get('x_star')
    Wn = np.hypot(W1[sl], W2[sl]) / (cl * rs[:, None])
    dist = np.hypot(X1[sl] - xs, X2[sl])
    res['min_W_over_clX'] = {}
    for dl in (1.0, 0.3, 0.1):
        m = dist >= dl
        k = np.argmin(np.where(m, Wn, np.inf))
        i, j = np.unravel_index(k, Wn.shape)
        res['min_W_over_clX'][str(dl)] = dict(value=float(Wn[i, j]), r=float(rs[i]), theta=float(t[j]))
    print(json.dumps(res, indent=1, default=float), flush=True)
    json.dump(res, open(outp, 'w'), indent=1, default=float)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
