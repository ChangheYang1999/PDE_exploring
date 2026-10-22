"""Local residuals on sampled circles around a zero Q of W (default: the interior zero Q+ located by zero_jac, read from
runs/zjac_<state>.log; or pass x y). For each radius rho the fields are evaluated directly from the spectral basis at
72 angles (points inside the open quadrant only), and the Cartesian residuals of PROMPT.md Section 4 are formed:
  R_Theta = W.grad Theta - (beta-2) Theta = x^2 y R_a,   N_Theta = |W1 Theta_x| + |W2 Theta_y| + |beta-2| |Theta|,
  R_Omega = W.grad Omega + Omega - Theta_x = x y R_G,     N_Omega = |W1 Omega_x| + |W2 Omega_y| + |Omega| + |Theta_x|.
Reported per rho: max |R_Theta|, max and min N_Theta (no floor: min N is printed instead), the pointwise max of
|R_Theta|/N_Theta and the fraction of the circle points with ratio > 0.1; the same for Omega; max |W| on the circle; and the
affine prediction s_lin = |(beta-2) Theta(Q)| + rho |(DW(Q)^T - (beta-2) I) grad Theta(Q)| of max |R_Theta| on the circle from
the sampled Jacobian (central differences on a polar stencil: radial increment r0*h, angular increment h radians) and gradient
at Q (exact at an exact zero; at beta = 2 it is rho |DW^T grad Theta|). The supplied Q is an approximate zero (|W(Q)| is
printed), so the quantities 'at Q' are printed both as stagnation-point defects (Omega - Theta_x) and as the full residuals
(including the W.grad terms). Ratios |R|/N are undefined where N = 0 (counted separately; none occurred in the logged runs).
Conditional reading (checked by an external referee): if W_n, Theta_n converge in C^1 on a common neighbourhood of a point q
with W(q) = 0, DW(q) invertible and grad Theta(q) != 0, then for every small fixed rho the sup of |R_Theta| over the disc of
radius rho is at least rho |DW(q)^T grad Theta(q)|/2 for all large n: the residual cannot tend to zero under these hypotheses.
Sampled values of fitted states; nothing here is a statement about profiles."""
import sys, re, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def pick(F, idx): return F[idx, idx]

def main(path, Q=None, rhos=(0.01, 0.03, 0.1, 0.3, 1.0), nang=72, h=1e-5):
    d = load_state(path); beta = float(d['beta']); name = path.split('/')[-1].replace('.npz', '')
    if Q is None:
        import glob
        logs = glob.glob(f'runs/zjac_{name}.log') + glob.glob(f'runs/zjac_{name.replace("_", "")}.log')
        for lg in logs:
            mm = re.search(r'Q\+ := interior zero[^:]*: \(([-0-9.e+]+),([-0-9.e+]+)\)', open(lg).read())
            if mm: Q = (float(mm.group(1)), float(mm.group(2))); break
    if Q is None: print('no Q given/found'); return
    qx, qy = Q; r0 = np.hypot(qx, qy); t0 = np.arctan2(qy, qx)
    print(f"state {path}: N={int(d['N'])} M={int(d['M'])} beta={beta:.6f} a0={float(d['ca'][0,0]) if False else ''} Q=({qx:.5f},{qy:.5f}) r={r0:.3f}")
    # stencil at Q for DW and grad Theta
    rr = np.array([r0 * (1 - h), r0, r0 * (1 + h)]); tt = np.array([t0 - h, t0, t0 + h])
    m, f = eval_state(d, rr, tt)
    g = {k: f[k].cpu().numpy() for k in ('W1', 'W2', 'a', 'a_x', 'a_y', 'G', 'Ra', 'RG', 'G_x', 'G_y')}
    c, s = np.cos(t0), np.sin(t0)
    def grad(F):
        F_r = (F[2, 1] - F[0, 1]) / (rr[2] - rr[0]); F_t = (F[1, 2] - F[1, 0]) / (tt[2] - tt[0])
        return c * F_r - s * F_t / r0, s * F_r + c * F_t / r0
    W1x, W1y = grad(g['W1']); W2x, W2y = grad(g['W2']); DW = np.array([[W1x, W1y], [W2x, W2y]])
    a, ax, ay, G = g['a'][1, 1], g['a_x'][1, 1], g['a_y'][1, 1], g['G'][1, 1]
    Theta = qx**2 * qy * a; Tx = 2 * qx * qy * a + qx**2 * qy * ax; Ty = qx**2 * a + qx**2 * qy * ay; Om = qx * qy * G
    gT = np.array([Tx, Ty]); ev = np.linalg.eigvals(DW)
    Gx, Gy = g['G_x'][1, 1], g['G_y'][1, 1]; Omx = qy * G + qx * qy * Gx; Omy = qx * G + qx * qy * Gy
    W1q, W2q = g['W1'][1, 1], g['W2'][1, 1]; Wq = np.hypot(W1q, W2q)
    RTq = W1q * Tx + W2q * Ty - (beta - 2) * Theta; NTq = abs(W1q * Tx) + abs(W2q * Ty) + abs(beta - 2) * abs(Theta)
    ROq = W1q * Omx + W2q * Omy + Om - Tx; NOq = abs(W1q * Omx) + abs(W2q * Omy) + abs(Om) + abs(Tx)
    Aeff = DW.T - (beta - 2) * np.eye(2); slope = np.linalg.norm(Aeff @ gT)
    print(f"  at Q (approximate zero): |W|={Wq:.2e}  Theta={Theta:+.4e} Omega={Om:+.4e} Theta_x={Tx:+.4e} |gradTheta|={np.linalg.norm(gT):.4e} |gradOmega|={np.hypot(Omx,Omy):.3e}")
    print(f"  defects at Q: Omega-Theta_x={Om-Tx:+.3e} (exact-solution value at an exact zero: 0); -(beta-2)Theta={-(beta-2)*Theta:+.3e}")
    print(f"  full residuals at Q: R_Theta={RTq:+.3e} (N_Theta={NTq:.3e}, |W||gradTheta|={Wq*np.linalg.norm(gT):.2e}); R_Omega={ROq:+.3e} (N_Omega={NOq:.3e}, |R_Omega|/N_Omega={abs(ROq)/NOq if NOq>0 else float('nan'):.3e}; W.gradOmega={W1q*Omx+W2q*Omy:+.2e})")
    print(f"  DW eig = {np.array2string(ev, precision=4)}  det={np.linalg.det(DW):+.4e}  |DW^T gradTheta| = {np.linalg.norm(DW.T @ gT):.4e}  affine slope |(DW^T-(beta-2)I) gradTheta| = {slope:.4e}")
    ang = np.linspace(0, 2 * np.pi, nang, endpoint=False)
    print("   rho   | max|R_T|  s_lin    max N_T  min N_T  max|R_T|/N_T  frac>0.1 | max|R_Om| max N_Om  min N_Om max|R_Om|/N_Om frac>0.1 | max|W|  n_pts   (s_lin = affine prediction |(beta-2)Theta(Q)| + rho |(DW^T-(beta-2)I) gradTheta(Q)|; frac over the points with N > 0)")
    for rho in rhos:
        X = qx + rho * np.cos(ang); Y = qy + rho * np.sin(ang); ok = (X > 1e-9) & (Y > 1e-9)
        X, Y = X[ok], Y[ok]; R = np.hypot(X, Y); T = np.arctan2(Y, X); idx = np.arange(len(X))
        m, f = eval_state(d, R, T)
        F = {k: pick(f[k].cpu().numpy(), idx) for k in ('W1', 'W2', 'a', 'a_x', 'a_y', 'G', 'G_x', 'G_y', 'Ra', 'RG')}
        Th = X**2 * Y * F['a']; Thx = 2 * X * Y * F['a'] + X**2 * Y * F['a_x']; Thy = X**2 * F['a'] + X**2 * Y * F['a_y']
        Omg = X * Y * F['G']; Omx = Y * F['G'] + X * Y * F['G_x']; Omy = X * F['G'] + X * Y * F['G_y']
        RT = X**2 * Y * F['Ra']; NT = np.abs(F['W1'] * Thx) + np.abs(F['W2'] * Thy) + abs(beta - 2) * np.abs(Th)
        RO = X * Y * F['RG']; NO = np.abs(F['W1'] * Omx) + np.abs(F['W2'] * Omy) + np.abs(Omg) + np.abs(Thx)
        # consistency of the two residual forms (direct Cartesian vs desingularized): report the max discrepancy once
        RT_dir = F['W1'] * Thx + F['W2'] * Thy - (beta - 2) * Th; RO_dir = F['W1'] * Omx + F['W2'] * Omy + Omg - Thx
        with np.errstate(divide='ignore', invalid='ignore'):
            rT = np.where(NT > 0, np.abs(RT) / NT, np.nan); rO = np.where(NO > 0, np.abs(RO) / NO, np.nan)
        nunT = int(np.isnan(rT).sum()); nunO = int(np.isnan(rO).sum()); Wn = np.hypot(F['W1'], F['W2'])
        fT = np.mean(rT[~np.isnan(rT)] > 0.1) if nunT < len(rT) else float('nan'); fO = np.mean(rO[~np.isnan(rO)] > 0.1) if nunO < len(rO) else float('nan')
        s_lin = abs((beta - 2) * Theta) + rho * slope
        # witness inequality (external referee): at the circle point z of max |R_Theta|, every exact beta = 2 profile within delta_W of W(z) and
        # delta_g of grad Theta(z) satisfies rho0 <= delta_W G0 + (V0 + delta_W) delta_g  (rho0 = |W.grad Theta|(z), V0 = |W(z)|, G0 = |grad Theta(z)|)
        iz = int(np.argmax(np.abs(RT))); rho0 = abs(RT[iz]) if beta == 2 else abs(F['W1'][iz] * Thx[iz] + F['W2'][iz] * Thy[iz]); V0 = Wn[iz]; G0 = np.hypot(Thx[iz], Thy[iz])
        dW_only = rho0 / G0; dg_only = rho0 / V0 if V0 > 0 else float('inf')
        print(f"         witness z at phi={np.degrees(np.arctan2(Y[iz]-qy, X[iz]-qx)):.0f} deg: rho0=|W.gradTheta|={rho0:.3e} V0=|W|={V0:.3e} G0=|gradTheta|={G0:.3e}; excluded tolerances: delta_g = 0 needs delta_W >= {dW_only:.3e} ({dW_only/V0*100:.0f} percent of V0); delta_W = 0 needs delta_g >= {dg_only:.3e} ({dg_only/G0*100:.0f} percent of G0); with delta_W = 0.1 V0: delta_g >= {max(0.0,(rho0 - 0.1*V0*G0)/(1.1*V0)):.3e} ({max(0.0,(rho0 - 0.1*V0*G0)/(1.1*V0))/G0*100:.0f} percent of G0)")
        print(f"  {rho:5.2f}  | {np.abs(RT).max():8.3e} {s_lin:8.3e} {NT.max():8.3e} {NT.min():8.3e} {np.nanmax(rT):8.3e}   {fT:5.2f}  | {np.abs(RO).max():8.3e} {NO.max():8.3e} {NO.min():8.3e} {np.nanmax(rO):8.3e}     {fO:5.2f}  | {Wn.max():7.3f}  {len(X)}   [undefined ratios: {nunT} {nunO}; form check: {np.abs(RT-RT_dir).max():.1e} {np.abs(RO-RO_dir).max():.1e}]")

if __name__ == '__main__':
    if len(sys.argv) >= 4: main(sys.argv[1], (float(sys.argv[2]), float(sys.argv[3])))
    else: main(sys.argv[1])
