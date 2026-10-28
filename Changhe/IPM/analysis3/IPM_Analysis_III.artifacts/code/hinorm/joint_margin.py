# NUMERICAL grid evidence only (float64, finite differences on the stored polar grid); not a bound.
# (1) zeros of V on the closed quadrant: min |V|/r away from 0;
# (2) the joint symbol margin of order s for conormal fields (x d_x, y d_y):
#     m_s(X) = kappa_w(X) - sup_xi [ s * g^T M g / |g|^2 + p(X, xi/|xi|) ],  g = (x xi_1, y xi_2),
#     p(X, nu) = nu^T [[-rho_y, rho_x/2], [rho_x/2, 0]] nu  (so sup_nu p = b_+),
#   and the same with ordinary derivatives (M replaced by DV^T, g = xi): m_s^ord.
import numpy as np, sys
d = np.load(__import__('os').environ.get('FIELD_NPZ', 'field.npz'))
t, th = d['t'], d['th']; cl = float(d['cl'])
V1, V2, rx, ry = d['V1'], d['V2'], d['rho_x'], d['rho_y']
T, TH = np.meshgrid(t, th, indexing='ij'); r = np.exp(T); C, S = np.cos(TH), np.sin(TH)
dr = lambda f: np.gradient(f, t, axis=0) / r
dth = lambda f: np.gradient(f, th, axis=1)
ddx = lambda f: C * dr(f) - S / r * dth(f)
ddy = lambda f: S * dr(f) + C / r * dth(f)
x, y = r * C, r * S
a = 17 / 4; mup = np.where(T < 0, -2 * a, -5 / 4)
q = (V1 * x + V2 * y) / r**2; Vth = (-V1 * S + V2 * C) / r
kap = 1 + cl + 0.5 * (mup * q + 2 * a * np.tan(TH) * Vth)
inner = (TH > 0.02) & (TH < np.pi / 2 - 0.02)
nV = np.hypot(V1, V2) / r
mask = (r > 0.05)
i = np.unravel_index(np.argmin(np.where(mask, nV, np.inf)), nV.shape)
print('min |V|/r over r > 0.05: %.4g at r = %.4f, theta = %.4f' % (nV[i], r[i], TH[i]))
mid = mask & (TH > 0.05)
j = np.unravel_index(np.argmin(np.where(mid, nV, np.inf)), nV.shape)
print('min |V|/r over r > 0.05, theta > 0.05: %.4g at r = %.4f, theta = %.4f' % (nV[j], r[j], TH[j]))
# source data on the x-axis
k0 = np.argmin(np.abs(V1[:, 0][r[:, 0] > 1])) + np.flatnonzero(r[:, 0] > 1)[0]
DV = [[ddx(V1), ddy(V1)], [ddx(V2), ddy(V2)]]
print('source (grid): r = %.4f, d_xV1 = %.4f, d_yV2 = %.4f, rho_y = %.4f, kappa = %.4f' % (
    r[k0, 0], DV[0][0][k0, 1], DV[1][1][k0, 1], ry[k0, 0], kap[k0, 1]))
M = [[ddx(V1) - V1 / x, x * ddx(V2) / y], [y * ddy(V1) / x, ddy(V2) - V2 / y]]
phis = np.linspace(0, np.pi, 181)[:-1]
def margin(s, conormal):
    best = np.full(T.shape, -np.inf)
    for ph in phis:
        n1, n2 = np.cos(ph), np.sin(ph)
        p = -ry * n1**2 + rx * n1 * n2
        if conormal:
            g1, g2 = x * n1, y * n2; gg = g1**2 + g2**2
            quad = (M[0][0] * g1**2 + (M[0][1] + M[1][0]) * g1 * g2 + M[1][1] * g2**2) / gg
        else:
            # [d_j, V.grad] h = (d_j V_i) d_i h: symbol nu^T DV^T nu = nu_i nu_j d_j V_i
            quad = DV[0][0] * n1**2 + (DV[0][1] + DV[1][0]) * n1 * n2 + DV[1][1] * n2**2
        best = np.maximum(best, s * quad + p)
    return kap - best
with np.errstate(all='ignore'):
    for s in [0, 1, 2, 3]:
        for conormal in [True, False]:
            m = margin(s, conormal)
            for name, reg in [('all', inner), ('r<1', inner & (r < 1)), ('1<r<30', inner & (r > 1) & (r < 30)), ('r>30', inner & (r > 30))]:
                v = np.where(reg, m, np.inf); ii = np.unravel_index(np.argmin(v), v.shape)
                print('s=%d %-8s %-7s min %8.3f at r = %8.3f, theta = %.3f' % (s, 'conormal' if conormal else 'ordinary', name, v[ii], r[ii], TH[ii]))
