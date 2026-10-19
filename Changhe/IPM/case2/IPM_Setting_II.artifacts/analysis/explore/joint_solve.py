"""Find an S^+_even-compatible test density meeting BOTH the moment law and the wall identity (lead, 2026-10-17).
F(s,t) = F7 + s (F15 - F7) + t (Fk - F7), samples of explore/joint_scan.py (p0 = 0.5, seed 1); 2D Newton with
finite differences on G = (kappa - tgt, 3 kw/c - tgt).  Then report c, min V_r/r after rescaling c -> 1/p0 - 1/2."""
import numpy as np, sys
sys.path.insert(0, 'explore')
sys.argv = ['x', '0.5', '0', '1']
import joint_scan as J
G = J.G; r = J.r
rng = np.random.default_rng(1)
Fs = []
for i in range(40):
    F = 0*r
    for L in [1.0, 4.0]:
        for f in J.feats(L*np.exp(rng.uniform(-1, 1.5))):
            F = F + rng.uniform(-1.5, 1.5)*f
    Fs.append(F)
k3 = int(sys.argv_k) if hasattr(sys, 'argv_k') else 32
def ev(st, k):
    F = Fs[7] + st[0]*(Fs[15] - Fs[7]) + st[1]*(Fs[k] - Fs[7])
    c, kap, kw3, _, _ = J.wall(F)
    return np.array([kap - J.tgt, kw3 - J.tgt]), c, F
for k in [32, 21, 25]:
    st = np.array([0.3, 0.0])
    ok = False
    for it in range(25):
        g, c, F = ev(st, k)
        print(f"k={k} it={it} s,t={st[0]:.5f},{st[1]:.5f} c={c:.4f} G={g[0]:+.2e},{g[1]:+.2e}", flush=True)
        if np.abs(g).max() < 2e-5: ok = True; break
        Jm = np.zeros((2,2)); e = 1e-4
        for j in range(2):
            d = np.zeros(2); d[j] = e
            Jm[:, j] = (ev(st + d, k)[0] - g)/e
        step = np.linalg.solve(Jm, -g)
        if np.abs(step).max() > 0.3: step *= 0.3/np.abs(step).max()
        st = st + step
    if ok:
        rho = J.X**2*np.exp(2*F)*(1+r**2)**((J.p0-2)/2)
        Wr_r, Wt_r, c, bp, _, _, _ = J.D.velocity(G, rho/G.w, J.p0)
        lam = (1/J.p0 - 0.5)/c
        vr = (1/J.p0 + lam*Wr_r)
        print(f"SOLVED k={k}: s,t={st}, c={c:.6f}, min V_r/r (rescaled) = {vr.min():.4f}, F range [{F.min():.3f},{F.max():.3f}]", flush=True)
        np.save(f'runs/joint_F_k{k}.npy', F)
