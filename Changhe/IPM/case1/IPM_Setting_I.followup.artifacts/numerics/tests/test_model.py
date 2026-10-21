"""Component tests for src/ipm_newton.py (run: python3 tests/test_model.py [device])."""
import sys, time, math
sys.path.insert(0, 'numerics/src')
import numpy as np, torch
from scipy.integrate import quad
import ipm_newton as ipn

dev = sys.argv[1] if len(sys.argv) > 1 else 'cuda'
beta = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
Npsi = int(sys.argv[3]) if len(sys.argv) > 3 else None
torch.manual_seed(0)
N, M, L, cl = 96, 24, 8.0, 5.5
mod = ipn.Model(N, M, L, device=dev, beta=beta, Npsi=Npsi)
print('beta =', beta, ' nmodes', mod.nmodes, ' Mq', mod.Mq, ' Npsi', mod.Npsi)
clT = torch.tensor(cl, device=mod.dev)
g = mod.geom(clT)
k = 1.0 / cl
r, w, v = mod.radii(cl)
print('nodes: r_1 = %.4g, r_N-1 = %.4g, r_N = %s' % (r[1], r[-2], r[-1]))

# ---------- 1. modal Poisson ODEs against quadrature of the Green-function integrals -------------
# choose Fhat_n(q) = q (1-q)^0.5 (0.3 + q^2) for n = 1 and 2 (any smooth function); f_n = r^2 w Fhat_n
def Fhat_fun(q): return q * (0.3 + q * q) * (1.0 - q) ** 2 * np.exp(-q)
def q_of_r(rr): return 1.0 - (1.0 + (rr / L) ** 2) ** (-(1.0 - k) / 2.0)
def f_of_r(rr): return rr ** 2 * (1.0 + (rr / L) ** 2) ** ((k - 3) / 2) * Fhat_fun(q_of_r(rr))
gp = mod.geom(clT, mod.qpsi); rp, wp_, vp_ = (lambda P1: (L * np.sqrt(np.where(P1 > 0, (1 - P1) / np.where(P1 > 0, P1, 1), np.inf)), P1 ** ((3 - k) / 2), P1 ** ((1 - k) / 2)))(gp['P1'].cpu().numpy())
Fn = torch.zeros(mod.Npsi + 1, mod.M2, device=mod.dev)
Fn[:, 0] = torch.tensor(Fhat_fun(mod.qpsi_np), device=mod.dev)
Fn[:, 1] = torch.tensor(Fhat_fun(mod.qpsi_np), device=mod.dev)
A1, A2 = mod.poisson_matrices(gp)
rhs = (L ** 2 * gp['omP1'])[:, None] * Fn
R = rhs.T[:, :, None].clone(); R1 = R.clone(); R2 = -R.clone()
R2[0, 0, 0] = -L ** 2 * Fn[0, 0] / (1.0 - k)
J1 = torch.linalg.solve(A1, R1)[:, :, 0].T.cpu().numpy(); J2 = torch.linalg.solve(A2, R2)[:, :, 0].T.cpu().numpy()
errs = []
for idx, n in [(0, 1), (1, 2)]:
    for i in [1, 5, mod.Npsi // 3, mod.Npsi // 2, 2 * mod.Npsi // 3, mod.Npsi - 3]:
        ri = rp[i]
        I1 = quad(lambda s: s ** (2 * n + 1) * f_of_r(s), 0, ri, epsabs=0, epsrel=1e-13, limit=400)[0]
        I2 = quad(lambda s: s ** (1 - 2 * n) * f_of_r(s), ri, np.inf, epsabs=0, epsrel=1e-13, limit=400)[0]
        J1ex = ri ** (-2 * n) * I1 / (ri ** 2 * vp_[i]); J2ex = ri ** (2 * n) * I2 / (ri ** 2 * vp_[i])
        errs.append((n, i, J1[i, idx] - J1ex, J2[i, idx] - J2ex, J1ex, J2ex))
print('Poisson ODE vs quadrature (n, i, dJ1, dJ2, J1, J2):')
for e in errs: print('  n=%d i=%3d  dJ1 %.2e  dJ2 %.2e   (J1 %.4e J2 %.4e)' % e)
# c from the n = 1 value at 0:  J2_1(0) = int_0^inf s^-1 f_1 ds (times 1/(r^2 v) -> limit r^2/(r^2 v(0)) = 1)
I2full = quad(lambda s: s ** (-1) * f_of_r(s), 0, np.inf, epsabs=0, epsrel=1e-13, limit=400)[0]
print('  J2_1(0) = %.12e   quad = %.12e   diff %.2e' % (J2[0, 0], I2full, J2[0, 0] - I2full))

# ---------- 2. fields from a manufactured b: identity c two ways, elliptic residual by FD --------
th = mod.ang.theta_np; q = mod.q_np
Q, TH = np.meshgrid(q, th, indexing='ij')
b_np = 1.0 + 0.2 * Q * np.cos(2 * TH) + 0.1 * Q ** 2 * np.cos(4 * TH) - 0.05 * Q ** 3 * np.cos(6 * TH)
b = torch.tensor(b_np, device=mod.dev)
fl = mod.fields(b, clT, g)
c_modal = fl['c'].item()
# c = int_0^inf rho_1(r) r^-2 dr, rho_1 the sin 3theta coefficient of rho = r^3 w Pi b: rho_1/(r^3 w) = (4/pi) int_0^{pi/2} Pi b sin(3 theta) dtheta
# by Gauss-Legendre in theta on the exact interpolant of b (valid for any angular map)
xg, wg = np.polynomial.legendre.leggauss(400); thg = (xg + 1) * np.pi / 4; wg = wg * np.pi / 4
rho1_over_r3w = np.zeros(N + 1)
for i in range(N + 1):
    bb = mod.eval_EE(b, np.full_like(thg, q[i]), thg)
    rho1_over_r3w[i] = (4 / np.pi) * np.sum(wg * np.cos(thg) ** 2 * np.sin(thg) * bb * np.sin(3 * thg))
# Clenshaw-Curtis on [0,1]
def cc_weights(N):
    x = np.cos(np.pi * np.arange(N + 1) / N); wts = np.zeros(N + 1)
    for j in range(N + 1):
        s = 0.0
        for kk in range(0, N + 1, 2):
            fac = 0.5 if (kk == 0 or kk == N) else 1.0
            ck = 2.0 / (1.0 - kk * kk) if kk != 1 else 0.0
            s += fac * ck * math.cos(kk * math.pi * j / N)
        wts[j] = 2.0 * s / N
    wts[0] *= 0.5; wts[-1] *= 0.5
    return 0.5 * wts[::-1]
wcc = cc_weights(N)
# integrand in q: rho_1 r^-2 dr = r^3 w rho1h r^-2 (r/S) dq = (r^2 w / S) rho1h dq ; r^2 w/S -> L^2/(1-k) at both ends
with np.errstate(invalid='ignore', divide='ignore'):
    r2w_over_S = np.where(np.isfinite(r), r ** 2 * w / np.maximum(g['S'].cpu().numpy(), 1e-300), 0.0)
r2w_over_S[0] = L ** 2 / (1 - k); r2w_over_S[-1] = L ** 2 / (1 - k)
c_int = np.sum(wcc * r2w_over_S * rho1_over_r3w)
print('identity check: c (modal J2_1(0)/2) = %.12f   c (int rho_1 r^-2 dr) = %.12f   diff %.2e' % (c_modal, c_int, c_modal - c_int))

# ---------- 3. transport residual vs finite differences of the interpolant --------------------
E, ident = mod.residual(b, clT, g, flds=fl)
E = E.cpu().numpy()
psit_n = fl['psit_n']
def rho_at(x, y):
    rr = np.hypot(x, y); tt = np.arctan2(y, x)
    qq = q_of_r(rr); bb = mod.eval_EE(b, qq, tt)
    ww = (1.0 + (rr / L) ** 2) ** ((k - 3) / 2)
    return rr ** 3 * ww * np.cos(tt) ** 2 * np.sin(tt) * bb
def U_at(x, y):
    rr = np.hypot(x, y); tt = np.arctan2(y, x); qq = q_of_r(rr)
    vv = (1.0 + (rr / L) ** 2) ** ((k - 1) / 2)
    nf = mod.nf_np
    ps = mod.eval_modes(psit_n, qq, tt, nf); ps_th = mod.eval_modes(psit_n, qq, tt, nf, deriv_th=1)
    # psi_r: d/dq of modes
    Dq = mod.Dq.cpu().numpy(); ps_q = mod.eval_modes(Dq @ psit_n.cpu().numpy(), qq, tt, nf)
    omP1 = (rr / L) ** 2 / (1 + (rr / L) ** 2)
    S = (1 - k) * (1 - qq) * omP1; ov = (k - 1) * omP1
    G = (2 + ov) * ps + S * ps_q
    U1 = -(rr * vv) * (np.sin(tt) * G + np.cos(tt) * ps_th)
    U2 = (rr * vv) * (np.cos(tt) * G - np.sin(tt) * ps_th)
    return U1, U2
maxrel = 0.0
for i in [3, N // 4, N // 2, 3 * N // 4, N - 4]:
    for j in [0, M // 3, M - 1]:
        x0, y0 = r[i] * np.cos(th[j]), r[i] * np.sin(th[j])
        h = 1e-4 * max(r[i], 1e-2)
        rx = (rho_at(x0 + h, y0) - rho_at(x0 - h, y0)) / (2 * h); ry = (rho_at(x0, y0 + h) - rho_at(x0, y0 - h)) / (2 * h)
        U1, U2 = U_at(np.array([x0]), np.array([y0]))
        W1 = cl * x0 + U1[0]; W2 = cl * y0 + U2[0]
        Rfd = W1 * rx + W2 * ry - rho_at(x0, y0)
        scale = r[i] ** 3 * w[i] * np.cos(th[j]) ** 2 * np.sin(th[j]) * (1 - q[i])
        Rmod = E[i, j] * scale
        rel = abs(Rfd - Rmod) / (abs(W1 * rx) + abs(W2 * ry) + abs(rho_at(x0, y0)))
        maxrel = max(maxrel, rel)
        print('  i=%3d j=%2d r=%.3g  R_fd %.6e  R_model %.6e  rel diff %.1e' % (i, j, r[i], Rfd, Rmod, rel))
print('transport residual vs FD: max relative difference %.2e (FD step error ~1e-8 expected)' % maxrel)
# q = 0 row equals the identity defect
print('row q=0: E[0,:] range %.3e .. %.3e   identity defect %.6e' % (E[0].min(), E[0].max(), ident.item()))

# ---------- 4. Jacobian columns vs finite differences ------------------------------------------
x = mod.pack(b, cl)
t0 = time.time(); J = mod.jacobian(x, batch=128); t1 = time.time()
print('Jacobian %d x %d assembled in %.1fs' % (J.shape[0], J.shape[1], t1 - t0))
F0 = mod.F(x)
rng = np.random.default_rng(1)
cols = list(rng.integers(0, N * M, 6)) + [N * M]
worst = 0.0
for cidx in cols:
    h = 1e-6 if cidx < N * M else 1e-6
    e = torch.zeros_like(x); e[cidx] = h
    d = (mod.F(x + e) - mod.F(x - e)) / (2 * h)
    err = (d - J[:, cidx]).abs().max().item(); nrm = J[:, cidx].abs().max().item()
    worst = max(worst, err / max(nrm, 1e-300))
    print('  col %6d: max|J col| %.3e  FD diff %.2e' % (cidx, nrm, err))
print('Jacobian vs FD worst relative %.2e' % worst)
