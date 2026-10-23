"""valley_tail.py -- origin-singularity diagnostics of saved ipm3 (valley) states, following the referee's benchmark (NUM_REPORT 4L(e)(ii), (vi)):
for the angular modes b_k(t) (cos 2k th coefficients of b on the Radau grid), compute the Chebyshev coefficients in t, the alternating-sign fraction of
the tail, the log-log slope of |a_n| over the last 40 percent of the coefficients (ipm3 map: 1 + t ~ r, so a term r^delta gives a_n ~ (-1)^n n^(-1-2 delta)), delta = (-slope - 1)/2, and the amplitude estimate A_k = median(|a_n| n^(1+delta)) over the tail.  Stable (delta, A_k) across N would be
evidence for a finite-regularity limiting branch (class C^{1,delta} if 1 < 1 + delta < 2).  usage: python3 src/valley_tail.py state1.pt state2.pt ..."""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
for f in sys.argv[1:]:
    st = torch.load(f, weights_only=False); N, M = int(st['N']), int(st['M'])
    mdl = ipm3.IPM3(N=N, M=M, L=float(st['L']), gamma=1 / float(st['cl']), device='cpu')
    bhat = mdl.ang.to_coef(st['b'].cpu(), 'EE').numpy()                        # (N+1, M) cos 2k th coefficients at the Radau nodes
    tR = mdl.rad.tR_np
    # Chebyshev coefficients from Radau values: least-squares fit of degree N (the Radau grid has N+1 points: square interpolation)
    V = np.cos(np.outer(np.arccos(tR), np.arange(N + 1)))
    out = [f"VALLEY {f}: c_l={st['cl']:.6f} a0={bhat[0,0]:.6f} N={N} M={M}"]
    for k in range(min(4, M)):
        a = np.linalg.solve(V, bhat[:, k]); n = np.arange(N + 1)
        lo = int(0.6 * N); sel = np.arange(lo, N + 1); aa = np.abs(a[sel]); nn = n[sel].astype(float)
        sgn = np.sign(a[sel]); altfrac = np.mean(sgn[:-1] * sgn[1:] < 0)
        good = aa > 1e-15 * np.abs(a).max()
        if good.sum() >= 4:
            slope, icpt = np.polyfit(np.log(nn[good]), np.log(aa[good]), 1); delta = (-slope - 1) / 2     # ipm3 map: 1 + t ~ r, so r^delta -> a_n ~ n^(-1-2 delta)
            amp = np.median(aa[good] * nn[good] ** (1 + delta))
        else: slope = delta = amp = float('nan')
        out.append(f"   mode k={k}: max|a_n|={np.abs(a).max():.3e}, tail (n >= {lo}) alternating fraction {altfrac:.2f}, slope {slope:+.3f} -> delta={delta:.3f}, amplitude A_k={amp:.3e}, |a_N|/max={np.abs(a[-1])/np.abs(a).max():.1e}")
    print("\n".join(out), flush=True)
