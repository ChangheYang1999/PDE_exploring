"""Diagnostics of a saved LM state: axis profiles, stagnation points on the x-axis, resonance quantity
W1'(x*) - (beta+2), per-mode coefficient decay, far-field angular amplitude, between-node residuals."""
import sys, numpy as np, torch, json
sys.path.insert(0, 'code')
from a2core import A2Model, DT, cheb_T, cheb_gauss_nodes
from lm_solve import load_state, dev, make_model, rad_of_r

def eval_state(d, r_eval, th_eval):
    """evaluate the saved state at radii r_eval and angles th_eval (any map)"""
    N, M, L = int(d['N']), int(d['M']), float(d['L'])
    mapname = str(d['mapname']) if 'mapname' in d else 'xi'
    beta_map = float(d['beta_map']) if 'beta_map' in d else float(d['beta'])
    m0 = make_model(mapname, N, M, L, beta_map, float(d['sigma_a']), float(d['sigma_G']), np.array([0.0]), np.array([0.5]))
    rad = rad_of_r(m0, mapname, np.asarray(r_eval, dtype=np.float64))
    m = make_model(mapname, N, M, L, beta_map, float(d['sigma_a']), float(d['sigma_G']), rad, th_eval)
    ca = torch.tensor(d['ca'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    f = m.fields(ca, cG, float(d['beta']))
    return m, f

def main(path):
    d = load_state(path)
    N, M, L, beta = int(d['N']), int(d['M']), float(d['L']), float(d['beta'])
    print(f"state {path}: N={N} M={M} L={L} beta={beta:.8f} sigma_a={float(d['sigma_a']):.5f} sigma_G={float(d['sigma_G']):.5f}")
    hist = json.loads(str(d['hist'])) if 'hist' in d else []
    if hist: print("  last diag:", {k: (round(v, 7) if isinstance(v, float) else v) for k, v in hist[-1].items() if k in ('Fnorm','Fmax','Ra_max','RG_max','c','G0','a_rtail','a_atail','G_rtail','G_atail','n_unknown')})
    # per-mode coefficient magnitude (Chebyshev coefficients of q_l)
    ca, cG = d['ca'], d['cG']
    print("  |ca| per angular mode l (max over n):", np.array2string(np.abs(ca).max(1), precision=2))
    print("  |cG| per angular mode l (max over n):", np.array2string(np.abs(cG).max(1), precision=2))
    # x-axis profile: theta ~ 0 (use th = 1e-6) on a fine radial grid; W1(x,0)/x = w1 ; stagnation where w1 = 0
    r_fine = np.concatenate([np.linspace(1e-3, 1, 400), np.linspace(1.0025, 60, 2000)])
    m, f = eval_state(d, r_fine, np.array([1e-7, np.pi/2 - 1e-7]))
    w1 = f['w1'][:, 0].cpu().numpy(); w2 = f['w2'][:, 1].cpu().numpy()
    a_x0 = f['a'][:, 0].cpu().numpy(); G_x0 = f['G'][:, 0].cpu().numpy()
    a_y0 = f['a'][:, 1].cpu().numpy(); G_y0 = f['G'][:, 1].cpu().numpy()
    Ra_x0 = f['Ra'][:, 0].cpu().numpy(); RG_x0 = f['RG'][:, 0].cpu().numpy()
    print("  x-axis: w1 = W1/x at r=", np.array2string(r_fine[[0, 200, 400, 600, 1000, 1500, 2399]], precision=2))
    print("          w1 =", np.array2string(w1[[0, 200, 400, 600, 1000, 1500, 2399]], precision=4))
    s = np.where(np.diff(np.sign(w1)) != 0)[0]
    for i in s:
        # linear interpolation of the zero; W1' = d(x w1)/dx = w1 + x w1' = x w1' at the zero
        x0 = r_fine[i] - w1[i] * (r_fine[i+1] - r_fine[i]) / (w1[i+1] - w1[i])
        dw1 = (w1[i+1] - w1[i]) / (r_fine[i+1] - r_fine[i])
        W1p = x0 * dw1
        print(f"  x-axis stagnation point x*={x0:.5f}: W1'(x*)={W1p:.5f}, beta+2={beta+2:.5f}, ratio (beta+2)/W1' = {(beta+2)/W1p:.5f}, "
              f"a(x*,0)={np.interp(x0, r_fine, a_x0):.4e}, G(x*,0)={np.interp(x0, r_fine, G_x0):.4e}")
        # local behaviour around x*: a and G on the axis at x* +- delta
        for dl in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
            am = np.interp(x0 - dl, r_fine, a_x0); ap_ = np.interp(x0 + dl, r_fine, a_x0)
            Gm = np.interp(x0 - dl, r_fine, G_x0); Gp = np.interp(x0 + dl, r_fine, G_x0)
            print(f"     delta={dl:5.2f}: a(x*-d)={am:.6f} a(x*+d)={ap_:.6f}  G(x*-d)={Gm:.6f} G(x*+d)={Gp:.6f}  dG/dx(central)={(Gp-Gm)/(2*dl):+.4f}")
    s2 = np.where(np.diff(np.sign(w2)) != 0)[0]
    print("  y-axis: zeros of W2/y:", [float(r_fine[i]) for i in s2] if len(s2) else "none", "; w2 range", w2.min(), w2.max())
    print("  axis profiles (r, a(x,0), G(x,0), a(0,y), G(0,y)) at selected r:")
    for i in [0, 100, 300, 400, 500, 700, 900, 1100, 1400, 1800, 2399]:
        print(f"    r={r_fine[i]:7.3f}  a_x={a_x0[i]:+.4e} G_x={G_x0[i]:+.4e}  a_y={a_y0[i]:+.4e} G_y={G_y0[i]:+.4e}  Ra_x={Ra_x0[i]:+.2e} RG_x={RG_x0[i]:+.2e}")
    # between-node residual maxima on a fine grid (desingularized, and Cartesian with normalizations)
    r_mid = np.geomspace(0.02, 2000, 300)
    th_mid = np.linspace(0, np.pi/2, 4*M+1)[1:-1]
    m2, f2 = eval_state(d, r_mid, th_mid)
    x = f2['x']; y = f2['y']; W1 = f2['W1']; W2 = f2['W2']; a = f2['a']; G = f2['G']
    Theta_x = x*y*(2*a + x*f2['a_x']); Theta_y = x**2*(a + y*f2['a_y'])
    Om_x = y*(G + x*f2['G_x']); Om_y = x*(G + y*f2['G_y'])
    Theta = x**2*y*a; Om = x*y*G
    R_Om = W1*Om_x + W2*Om_y + Om - Theta_x
    R_Th = W1*Theta_x + W2*Theta_y - (beta-2)*Theta
    N_Om = (W1*Om_x).abs() + (W2*Om_y).abs() + Om.abs() + Theta_x.abs()
    N_Th = (W1*Theta_x).abs() + (W2*Theta_y).abs() + abs(beta-2)*Theta.abs()
    r2 = m2.rt[:, None].expand_as(x)
    for lab, R, Nn in [('R_Omega', R_Om, N_Om), ('R_Theta', R_Th, N_Th)]:
        ratio = R.abs() / Nn.clamp_min(1e-300)
        TH = torch.tensor(th_mid, dtype=DT, device=dev)[None, :].expand_as(x)
        for rng, msk in [('r<1', r2 < 1), ('1<=r<10', (r2 >= 1) & (r2 < 10)), ('10<=r<100', (r2 >= 10) & (r2 < 100)), ('r>=100', r2 >= 100)]:
            rm = ratio.clone(); rm[~msk] = -1
            i = int(rm.argmax()); rr_, tt_ = float(r2.reshape(-1)[i]), float(TH.reshape(-1)[i])
            print(f"  between-node {lab:8s} {rng:9s}: max|R|={R[msk].abs().max():.3e}  max|R|/N={ratio[msk].max():.3e} at (r={rr_:.3g}, th={tt_:.3f}) (max N={Nn[msk].max():.2e})")
        # ratio excluding a sector near the y-axis (th > pi/2 - 0.15) to see whether the O(1) values are an axis effect
        msk2 = (r2 >= 10) & (TH < np.pi/2 - 0.15)
        print(f"  between-node {lab:8s} r>=10, th<pi/2-0.15: max|R|/N={ratio[msk2].max():.3e}")
    print(f"  between-node desingularized: max|R_a|={f2['Ra'].abs().max():.3e} max|R_G|={f2['RG'].abs().max():.3e}; node-level from hist: Ra_max={hist[-1]['Ra_max'] if hist else float('nan'):.3e} RG_max={hist[-1]['RG_max'] if hist else float('nan'):.3e}")
    # far-field angular amplitude of a and G at large r (scaled by expected decay)
    r_far = np.array([20., 50., 100., 300., 1000., 1e4])
    m3, f3 = eval_state(d, r_far, np.linspace(0.05, np.pi/2-0.05, 7))
    sa, sG = float(d['sigma_a']), float(d['sigma_G'])
    print("  far field: a * r^(2 sigma_a) at r=", r_far)
    print(np.array2string((f3['a'].cpu().numpy() * (r_far**(2*sa))[:, None]), precision=3))
    print("  far field: G * r^(2 sigma_G):")
    print(np.array2string((f3['G'].cpu().numpy() * (r_far**(2*sG))[:, None]), precision=3))

if __name__ == '__main__':
    for p in sys.argv[1:]:
        main(p)
