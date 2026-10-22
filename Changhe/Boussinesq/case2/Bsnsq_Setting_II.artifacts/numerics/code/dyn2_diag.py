import sys, torch, numpy as np, math
sys.path.insert(0,'code')
from dynres2 import *
d = load_state('runs/B2_p_gauss_N112.npz')
for Ni, Nj in [(512, 96), (1024, 192)]:
    dyn = DynResGrid(Ni, Nj, 112, 28, 1.0, 2.0)
    A, B = grid_from_state(dyn, d)
    cG = dyn.fit(B); dyn.set_velocity(cG)
    mm = make_model('t', 112, 28, 1.0, 2.0, float(d['sigma_a']), float(d['sigma_G']), dyn.mf.eta_of_r(dyn.r[1:-1].cpu().numpy()), dyn.th.cpu().numpy())
    ca0 = torch.tensor(d['ca'], dtype=DT, device=dev); cG0 = torch.tensor(d['cG'], dtype=DT, device=dev)
    fe = mm.fields(ca0, cG0, 2.0)
    ds = 1e-3
    An, Bn = dyn.step(A, B, ds)
    dA = (An - A)[1:-1] / ds; dB = (Bn - B)[1:-1] / ds
    pA = -fe['Ra'] / (dyn.t[1:-1] ** dyn.e_a)[:, None]; pB = -fe['RG'] / (dyn.t[1:-1] ** dyn.e_G)[:, None]
    rr = dyn.r[1:-1].cpu().numpy(); th = dyn.th.cpu().numpy()
    eA = (dA - pA).abs().cpu().numpy(); eB = (dB - pB).abs().cpu().numpy()
    for nm, e, p in [('A', eA, pA.abs().cpu().numpy()), ('B', eB, pB.abs().cpu().numpy())]:
        i, j = np.unravel_index(e.argmax(), e.shape)
        print(f"Ni={Ni} Nj={Nj} {nm}: max err {e.max():.3e} at r={rr[i]:.3f} th={th[j]:.3f} (pred there {p[i,j]:.3e}); err by radial band:")
        for lo, hi in [(0, 0.1), (0.1, 1), (1, 5), (5, 12), (12, 15), (15, 30), (30, 100), (100, 1e4), (1e4, 1e12)]:
            mk = (rr >= lo) & (rr < hi)
            if mk.any(): print(f"    {lo:>7g}-{hi:<7g}: err max {e[mk].max():.2e}  pred max {p[mk].max():.2e}")
    # source check: S from FD vs analytic from the spectral state
    S_fd = dyn.source(A)[1:-1]
    S_an = (2 * fe['a'] + fe['x'] * fe['a_x']) / (dyn.t[1:-1] ** dyn.e_G)[:, None]
    eS = (S_fd - S_an).abs().cpu().numpy()
    i, j = np.unravel_index(eS.argmax(), eS.shape)
    print(f"   source FD vs analytic: max err {eS.max():.3e} at r={rr[i]:.3f} th={th[j]:.3f}; |S|max {float(S_an.abs().max()):.3e}; err r<30: {eS[rr<30].max():.2e}")
