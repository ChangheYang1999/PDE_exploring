"""Resample a numerics-lane field export (src/export_fields.py: Chebyshev-Radau radii of the map r = L(1+t)/(1-t+2L/R),
midpoint angles theta_j = (j+1/2) pi/(2M), a = rho/(x^2 y)) onto the verifier's format: r uniform in log r on [r0, R],
theta uniform on [0, pi/2] with endpoints. Only (r, theta, a or rho, L, R) are read. Radially: barycentric interpolation of
a in t through the given nodes (own weights from the node positions); angularly: exact cos(2 k theta) series of a, k < M
(DCT-II inversion on the midpoints). The exporter's unknown is b = a / w, w = (1 + r^2/L^2)^((gamma - 3)/2), a polynomial in t
on the Radau nodes; b (not a) is interpolated and a = w b (21:4xZ: interpolating a directly differs by 10 percent at r ~ R
when b carries high-degree noise). rho = r^3 cos^2 sin a. The exporter's c_l is stored as cl_exporter only.
Usage: python3 vnum_import.py in.npz out.npz N r0 [nq]"""
import sys
import numpy as np


def bary_w(t):
    n = len(t)
    lw = np.zeros(n)
    sg = np.ones(n)
    for j in range(n):
        d = t[j] - np.delete(t, j)
        lw[j] = -np.log(np.abs(d)).sum()
        sg[j] = np.prod(np.sign(d))
    lw -= lw.max()
    return sg * np.exp(lw)


def bary_eval(t, wb, f, tn):
    """f: (n, M) values at nodes t; returns (len(tn), M)."""
    D = tn[:, None] - t[None, :]
    hit = np.abs(D) < 1e-15
    D[hit] = 1.0
    C = wb[None, :] / D
    out = (C @ f) / C.sum(1)[:, None]
    for i, j in zip(*np.nonzero(hit)):
        out[i] = f[j]
    return out


def main(inp, outp, N, r0, nq=642):
    z = np.load(inp, allow_pickle=True)
    r, th, a = z['r'], z['theta'], z['a']
    L, R = float(z['L']), float(z['R'])
    gm = float(z['gamma'])
    wfun = lambda rr: (1 + rr ** 2 / L ** 2) ** ((gm - 3) / 2)
    a = a / wfun(r)[:, None]                            # b
    al = 2 * L / R
    t = (r * (1 + al) - L) / (r + L)
    M = len(th)
    assert np.allclose(th, (np.arange(M) + 0.5) * np.pi / (2 * M))
    # angular coefficients A_k(r_i): a = sum_k A_k cos(2 k theta)
    C = np.cos(np.outer(2 * th, np.arange(M)))
    Ak = np.linalg.solve(C, a.T).T                      # (n, M)
    rec = np.abs(Ak @ C.T - a).max()
    wb = bary_w(t)
    rn = np.exp(np.linspace(np.log(r0), np.log(R), N))
    tn = (rn * (1 + al) - L) / (rn + L)
    tn[-1] = 1.0
    An = bary_eval(t, wb, Ak, tn)
    thn = np.linspace(0, np.pi / 2, nq)
    an = wfun(rn)[:, None] * (An @ np.cos(np.outer(2 * thn, np.arange(M))).T)
    rho = rn[:, None] ** 3 * (np.cos(thn) ** 2 * np.sin(thn))[None, :] * an
    # self-check: interpolate back to the original nodes (r > 0) and compare with the given rho
    Ab = bary_eval(t, wb, Ak, t)
    back = np.abs(Ab @ C.T - a).max()
    V = np.polynomial.chebyshev.chebvander(t, len(t) - 1)
    cb = np.abs(np.linalg.solve(V, Ak)).max(1)
    print('max_k |cheb coeff of b_k(t)| at n = N/4, N/2, 3N/4, N:', [float(cb[n]) for n in (len(t) // 4, len(t) // 2, 3 * len(t) // 4, len(t) - 1)])
    np.savez(outp, r=rn, theta=thn, rho=rho, cl_exporter=float(z['c_l']), c_exporter=float(z['c']), L=L, R=R,
             source=inp, top_angular_share=float(np.abs(Ak[:, -4:]).max() / np.abs(Ak).max()))
    print(dict(N=N, r0=r0, R=R, M=M, nodes=len(r), dct_rec=rec, back=back, a_at_r0=float(an[0, 0]),
               top_angular_share=float(np.abs(Ak[:, -4:]).max() / np.abs(Ak).max()), cl_exporter=float(z['c_l'])))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]) if len(sys.argv) > 5 else 642)
