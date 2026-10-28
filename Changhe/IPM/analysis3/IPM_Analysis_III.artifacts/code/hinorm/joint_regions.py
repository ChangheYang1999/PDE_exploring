# NUMERICAL: joint symbol margins by region (conormal near the y-axis, ordinary near the x-axis, scaled ordinary r*grad).
import numpy as np
exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'joint_margin.py')).read().split("with np.errstate")[0].replace("print(", "(lambda *a, **k: None)("))
def margin_scaled(s):
    # scaled ordinary derivatives r d_j: commutator symbol nu^T DV^T nu - q (since [r d_j, V.grad] = (d_j V_i) r d_i - (V.grad r / r) r d_j)
    best = np.full(T.shape, -np.inf)
    for ph in phis:
        n1, n2 = np.cos(ph), np.sin(ph)
        p = -ry * n1**2 + rx * n1 * n2
        quad = DV[0][0] * n1**2 + (DV[0][1] + DV[1][0]) * n1 * n2 + DV[1][1] * n2**2 - q
        best = np.maximum(best, s * quad + p)
    return kap - best
with np.errstate(all='ignore'):
    for s in [1, 2, 3]:
        mc, mo, ms = margin(s, True), margin(s, False), margin_scaled(s)
        for name, m, reg in [('conormal, theta>pi/4', mc, (TH > np.pi/4) & (TH < np.pi/2 - 0.02)),
                             ('ordinary, theta<pi/4', mo, TH < np.pi/4),
                             ('scaled,   theta<pi/4', ms, TH < np.pi/4),
                             ('scaled,   all', ms, TH < np.pi/2 - 0.02)]:
            for rn, rr in [('r<1', r < 1), ('1<r<30', (r > 1) & (r < 30)), ('r>30', r > 30)]:
                v = np.where(reg & rr, m, np.inf); ii = np.unravel_index(np.argmin(v), v.shape)
                print('s=%d %-22s %-7s min %8.3f at r = %9.3f, theta = %.3f' % (s, name, rn, v[ii], r[ii], TH[ii]))
    # pointwise frozen ratio on the x-axis: kappa / d_y V_2 (ordinary y-derivatives, nu = e_2, p = 0 there)
    ax = 1
    rat = kap[:, ax] / DV[1][1][:, ax]
    for rv in [1e-3, 1e-2, 0.1, 0.5, 1, 2, 4, 6, 8, 8.65]:
        i = np.argmin(np.abs(r[:, ax] - rv)); print('x-axis r = %6.3f: kappa = %7.3f, d_yV2 = %7.3f, d_xV1 = %7.3f, ratio kappa/d_yV2 = %6.3f' % (r[i, ax], kap[i, ax], DV[1][1][i, ax], DV[0][0][i, ax], rat[i]))
