"""Resample a numerics-lane export onto the verifier's format (as vnum_import / vnum_import2), now also for
(i) clustered radial maps and (ii) state files that hold only the unknown b (keys b, cl, gamma, N, M, L, R, cluster, pmap).
Data format read from the exporter's definition (not its code): computational variable s on N+1 Chebyshev-Radau points
s_j = -cos(2 pi j/(2N+1)); t = T(s) = s + alpha (s_P - s) exp(-((s - s_P)/w)^2) if cluster = (s_P, w, alpha), else t = s;
r = L (1+t)/(1-t+a)^p, a = (2L/R)^(1/p); a(r, theta) = w(r) b, w = (1 + r^2/L^2)^((gamma-3)/2); rho = r^3 cos^2 sin a;
angles theta_j = (j+1/2) pi/(2M). b is a polynomial of degree N in s, so it is interpolated barycentrically in s; angularly
the exact cos(2 k theta) series, k < M. For field exports the node radii are given and s is recovered by bisection
(checked against the Radau formula). Usage: python3 vnum_import3.py in.npz out.npz N r0 [nq]"""
import sys
import numpy as np
from vnum_import import bary_w, bary_eval


def bisect(f, y, lo=-1.0, hi=1.0, n=200):
    lo = np.full(np.shape(y), lo); hi = np.full(np.shape(y), hi)
    for _ in range(n):
        mid = 0.5 * (lo + hi); big = f(mid) > y
        hi = np.where(big, mid, hi); lo = np.where(big, lo, mid)
    return 0.5 * (lo + hi)


def main(inp, outp, N, r0, nq=642):
    z = np.load(inp, allow_pickle=True)
    L, R, gm = float(z['L']), float(z['R']), float(z['gamma'])
    p = float(z['pmap']) if 'pmap' in z.files else 1.0
    cl = np.asarray(z['cluster'], dtype=float).ravel() if 'cluster' in z.files else np.array([])
    al = (2 * L / R) ** (1 / p)
    r_of_t = lambda t: L * (1 + t) / (1 - t + al) ** p
    if cl.size:
        sP, wc, alc = cl
        T = lambda s: s + alc * (sP - s) * np.exp(-((s - sP) / wc) ** 2)
    else:
        T = lambda s: s
    wfun = lambda rr: (1 + rr ** 2 / L ** 2) ** ((gm - 3) / 2)
    Nn = int(z['N'])
    s_nodes = -np.cos(2 * np.pi * np.arange(Nn + 1) / (2 * Nn + 1))
    r_nodes = r_of_t(T(s_nodes))
    if 'b' in z.files:
        b = z['b']; M = int(z['M']); th = (np.arange(M) + 0.5) * np.pi / (2 * M)
        clx = float(z['cl'])
        node_chk = 0.0
    else:
        r, th = z['r'], z['theta']; M = len(th)
        b = z['a'] / wfun(r)[:, None]
        clx = float(z['c_l'])
        node_chk = float(np.max(np.abs(r - r_nodes) / np.maximum(r, 1e-300)))
        assert node_chk < 1e-10, 'node radii do not match the stated map (clustered export without cluster key?)'
    assert np.allclose(th, (np.arange(M) + 0.5) * np.pi / (2 * M))
    C = np.cos(np.outer(2 * th, np.arange(M)))
    Ak = np.linalg.solve(C, b.T).T
    rec = np.abs(Ak @ C.T - b).max()
    wb = bary_w(s_nodes)
    rn = np.exp(np.linspace(np.log(r0), np.log(R), N))
    tn = bisect(r_of_t, rn); sn = bisect(T, tn)
    sn[-1] = 1.0
    An = bary_eval(s_nodes, wb, Ak, sn)
    thn = np.linspace(0, np.pi / 2, nq)
    an = wfun(rn)[:, None] * (An @ np.cos(np.outer(2 * thn, np.arange(M))).T)
    rho = rn[:, None] ** 3 * (np.cos(thn) ** 2 * np.sin(thn))[None, :] * an
    back = np.abs(bary_eval(s_nodes, wb, Ak, s_nodes[1:]) - Ak[1:]).max()
    rt_chk = float(np.max(np.abs(r_of_t(T(sn[:-1])) - rn[:-1]) / rn[:-1]))
    np.savez(outp, r=rn, theta=thn, rho=rho, cl_exporter=clx, L=L, R=R, source=inp,
             top_angular_share=float(np.abs(Ak[:, -4:]).max() / np.abs(Ak).max()))
    print(dict(N=N, r0=r0, R=R, M=M, nodes=Nn + 1, p=p, cluster=cl.tolist(), node_chk=node_chk, rt_chk=rt_chk, dct_rec=rec,
               back=back, a_at_r0=float(an[0, 0]), top_angular_share=float(np.abs(Ak[:, -4:]).max() / np.abs(Ak).max()),
               cl_exporter=clx))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]) if len(sys.argv) > 5 else 642)
