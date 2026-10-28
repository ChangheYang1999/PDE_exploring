# NUMERICAL estimate (float64, grid data; not a bound) of the Fourier moments S_k(a) = sum_q |q|^k |a^(q)|, k = 0, 1, 2
# for the principal coupling coefficients B_ij (polar frame) and b_eta of the injectivity analysis,
# on a periodic cylinder window, from field.npz. Used only for an order-of-magnitude rank estimate.
import numpy as np, json, sys
z = np.load(sys.argv[1] if len(sys.argv) > 1 else 'field.npz')
t = z['t']; th = z['th']; gx = z['rho_x']; gy = z['rho_y']
# extend theta in [0, pi/2] to [0, 2 pi) by the parities: rho odd in y, even in x
# g1 = rho_x: odd in x, odd in y; g2 = rho_y: even in x, even in y
def ext(f, sx, sy):
    q1 = f                                  # theta in [0, pi/2]
    q2 = sx * f[:, ::-1][:, 1:]             # theta in (pi/2, pi]: (x,y) -> (-x,y), theta -> pi - theta
    up = np.concatenate([q1, q2], axis=1)   # [0, pi]
    lo = sy * up[:, ::-1][:, 1:-1]          # (pi, 2 pi): (x,y) -> (x,-y), theta -> -theta
    return np.concatenate([up, lo], axis=1)
G1 = ext(gx, -1, -1); G2 = ext(gy, 1, 1)
n_th = G1.shape[1]; TH = np.arange(n_th) * 2 * np.pi / n_th
c = np.cos(TH)[None, :]; s = np.sin(TH)[None, :]
# Cartesian B = [[-g2, g1/2], [g1/2, 0]]; polar frame B_p = R^T B R with R = [[c, -s], [s, c]]
B11 = -G2 * c * c + G1 * c * s
B22 = -G2 * s * s - G1 * c * s
B12 = G2 * c * s + 0.5 * G1 * (c * c - s * s)
out = {}
for (t0, t1, w) in [(-3.0, 11.0, 1.0), (-2.0, 9.5, 1.0)]:
    m = (t >= t0) & (t <= t1); tt = t[m]
    # smooth cutoff, equal to 1 on [t0 + w, t1 - w]
    def bump(x):
        y = np.zeros_like(x); i = (x > 0) & (x < 1)
        y[i] = 1 / (1 + np.exp(1 / x[i] - 1 / (1 - x[i]))); y[x >= 1] = 1; return y
    chi = bump((tt - t0) / w) * bump((t1 - tt) / w)
    ell = tt[-1] - tt[0] + (tt[1] - tt[0])
    xi = 2 * np.pi * np.fft.fftfreq(len(tt), d=(tt[1] - tt[0]))
    nn = np.fft.fftfreq(n_th, d=1.0 / n_th)
    Q = np.hypot(xi[:, None], nn[None, :])
    res = {}
    for name, a in [('B11', B11), ('B22', B22), ('B12', B12),
                    ('b_eta0.1', (np.sqrt(G1**2 + G2**2 + 0.01) - G2) / 2),
                    ('g1', G1), ('g2', G2)]:
        A = a[m] * chi[:, None]
        ah = np.fft.fft2(A) / A.size
        res[name] = dict(S2=float((Q**2 * abs(ah)).sum()), S1=float((Q * abs(ah)).sum()), S0=float(abs(ah).sum()), sup=float(abs(A).max()))
    tot = res['B11']['S1'] + res['B22']['S1'] + 2 * res['B12']['S1'] + 2 * res['b_eta0.1']['S1']
    # second-order rule (topic 94 (9)): Lambda^2 >= [S2mat(B) + S2(b_eta)] / [2 (E - eta/2)], S2mat <= sum_ij S2(B_ij)
    S2sum = res['B11']['S2'] + res['B22']['S2'] + 2 * res['B12']['S2'] + res['b_eta0.1']['S2']
    rule = {}
    for E in [0.5, 1.0, 1.25]:
        L2 = S2sum / (2 * (E - 0.05))
        # lattice points |p| < Lambda on the (ell x 2 pi) torus ~ Lambda^2 ell / 2; parity classes divide by 4
        rule['E=%g' % E] = dict(Lambda=float(np.sqrt(L2)), N_lattice=float(L2 * ell / 2), N_parity=float(L2 * ell / 8))
    out['window_%g_%g' % (t0, t1)] = dict(ell=float(ell), coeffs=res, Sigma_S1=float(tot), S2_sum=float(S2sum), second_order_rule=rule)
print(json.dumps(out, indent=1))
