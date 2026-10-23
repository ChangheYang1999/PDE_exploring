"""Residual table (PROMPT section 6 format) for a saved FORCED sheet-1 state: between-node max|R_f|, max|R_f|/N_f,
max|R_f|/N_v by region, where R_f = (c_l X + U).grad rho - rho - mu y phi is the residual of the forced equation, plus the
unforced residual R (= mu y phi at an exact forced solution) for reference, the identity c_l + c - 1 = mu/a0, and the
denominators' minima.  Not a candidate: a forced state (mu != 0)."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
for f in sys.argv[1:]:
    st = torch.load(f); N, M, L = st['N'], st['M'], st['L']; cl = st['cl']; mu = st.get('mu', 0.0); beta = st.get('beta', float('nan')); Lf = st.get('Lf', L)
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev); b = st['b'].to(dev); flds = mdl.fields(b)
    c = mdl.psi_xy0(flds).item(); a0 = b[0,0].item()
    print(f"{f}: N={N} M={M} L={L} Lf={Lf} c_l={cl} beta={beta} mu={mu:.10f} a0={a0:.10f} c={c:.10f} (c_l+c-1)a0-mu={(cl+c-1)*a0-mu:.2e}")
    # between-node grid: midpoints in t and theta, plus 3 extra angles near the axes
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np
    thm = np.concatenate([[0.25*th[0], 0.5*th[0]], 0.5*(th[:-1]+th[1:]), [0.5*(th[-1]+np.pi/2), np.pi/2 - 0.25*(np.pi/2-th[-1])]])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT)
    phi = (1 + RR**2/Lf**2)**(-2)
    Rf = ev['R'] - mu*ev['y']*phi
    print("   region r        points   max|R_f|     max|R_f|/N_f   max|R_f|/N_v   min N_f      max|R| (unforced, = mu y phi)")
    for lo, hi in [(0, 0.01), (0.01, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e8), (1e8, 1e30)]:
        m = (RR >= lo) & (RR < hi)
        if not m.any(): continue
        print(f"   [{lo:8.0e},{hi:8.0e}) {m.sum():6d}   {np.abs(Rf[m]).max():.2e}     {(np.abs(Rf[m])/ev['Nf'][m]).max():.2e}       {(np.abs(Rf[m])/ev['Nv'][m]).max():.2e}       {ev['Nf'][m].min():.2e}     {np.abs(ev['R'][m]).max():.2e}")
    # dense rays near axes
    rr = np.logspace(-3, 6, 600)
    for ang in [0.005, np.pi/4, np.pi/2 - 0.005]:
        e = mdl.evaluate(b, cl, flds, rr, np.full_like(rr, ang)); ph = (1 + rr**2/Lf**2)**(-2)
        q = np.abs(e['R'] - mu*e['y']*ph)/e['Nf']
        print(f"   ray theta={ang:.3f}: max|R_f|/N_f = {q.max():.2e} at r = {rr[q.argmax()]:.2e}")
