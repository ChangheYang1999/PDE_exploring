"""Add eps * (numerics-lane c_l direction) to one of my generated fields (G47 test of c_l softness at the c6c level).
Usage (from code/): python3 ../scratch/dir_on_shape.py field.npz dir.npz S0.npz eps out.npz
field.npz: gen_shape.py output (log-uniform r, theta = linspace(0, pi/2, nq+1), rho).
dir.npz:   numerics runs/valley_N256M64R3000_direction.npz (delta_b_per_unit_cl on the exporter's Radau x midpoint grid).
S0.npz:    numerics runs/fields_valley_N256M64R3000_S0.npz (map constants L, R, gamma, k_tail; rho(R, theta) for the tail).
Data format read from the exporter's definition (as code/vnum_import3.py): s_j = -cos(2 pi j/(2N+1)), r = L(1+s)/(1-s+a),
a = 2L/R (unclustered, p = 1); delta_rho = r^3 cos^2 sin w(r) delta_b, w = (1 + r^2/L^2)^((gamma-3)/2). For r > R the
exporter's disk closure rho = (r/R)^k rho(R, theta), k = 1/c_l, is linearized in c_l:
delta_rho = (r/R)^k [delta_rho(R, theta) + dk rho_S0(R, theta) ln(r/R)], dk = -k^2 per unit c_l."""
import sys
import numpy as np
sys.path.insert(0, 'code')
from vnum_import import bary_w, bary_eval
from vnum_import3 import bisect


def direction_on(r, th, dz, sz):
    L, R, gm, k = float(sz['L']), float(sz['R']), float(sz['gamma']), float(sz['k_tail'])
    Nn = len(dz['r']) - 1
    al = 2 * L / R
    r_of_s = lambda s: L * (1 + s) / (1 - s + al)
    s_nodes = -np.cos(2 * np.pi * np.arange(Nn + 1) / (2 * Nn + 1))
    assert np.max(np.abs(r_of_s(s_nodes) - dz['r']) / np.maximum(dz['r'], 1e-300)) < 1e-10
    M = len(dz['theta'])
    assert np.allclose(dz['theta'], (np.arange(M) + 0.5) * np.pi / (2 * M))
    C = np.cos(np.outer(2 * dz['theta'], np.arange(M)))
    wfun = lambda rr: (1 + rr ** 2 / L ** 2) ** ((gm - 3) / 2)
    Ad = np.linalg.solve(C, dz['delta_b_per_unit_cl'].T).T
    A0 = np.linalg.solve(C, (sz['a'] / wfun(sz['r'])[:, None]).T).T
    wb = bary_w(s_nodes)
    ang = np.cos(np.outer(2 * th, np.arange(M))).T
    geo = (np.cos(th) ** 2 * np.sin(th))[None, :]
    inside = r <= R
    ri = r[inside]
    si = bisect(r_of_s, ri)
    si[ri >= R * (1 - 1e-14)] = 1.0
    drho = np.zeros((len(r), len(th)))
    drho[inside] = ri[:, None] ** 3 * geo * wfun(ri)[:, None] * (bary_eval(s_nodes, wb, Ad, si) @ ang)
    dR = R ** 3 * geo[0] * wfun(R) * (bary_eval(s_nodes, wb, Ad, np.array([1.0])) @ ang)[0]
    rR = R ** 3 * geo[0] * wfun(R) * (bary_eval(s_nodes, wb, A0, np.array([1.0])) @ ang)[0]
    ro = r[~inside]
    q = (ro / R) ** k
    drho[~inside] = q[:, None] * (dR[None, :] + (-k * k) * rR[None, :] * np.log(ro / R)[:, None])
    return drho, dict(R=R, k=k, n_inside=int(inside.sum()), dmax=float(np.abs(drho).max()))


if __name__ == '__main__':
    fp, dp, sp, eps, outp = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5]
    f = np.load(fp, allow_pickle=True)
    dz = np.load(dp, allow_pickle=True)
    sz = np.load(sp, allow_pickle=True)
    drho, info = direction_on(f['r'], f['theta'], dz, sz)
    rho = f['rho'] + eps * drho
    out = {k: f[k] for k in f.files if k != 'rho'}
    out.pop('c', None); out.pop('c_l', None)
    np.savez(outp, rho=rho, eps=eps, **out)
    info.update(eps=eps, rel_change=float(np.abs(eps * drho).max() / np.abs(f['rho']).max()))
    print(info)
