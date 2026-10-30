"""FLOAT Hdot^-1 norm of the density residual F of a candidate (lane c1-n1).
F odd in y, even in x: F(r,theta) = sum_{n odd} F_n(r) sin(n theta), F_n(r) = (4/pi) int_0^{pi/2} F sin(n theta) dtheta.
||F||_H^2 = sum_n pi int int K_n(r,r') F_n(r) F_n(r') r r' dr dr',  K_n = (1/2n) (min/max)^n   (Green function of -Delta on R^2, mode n).
Inner part (r <= R): quadrature on the polar product mesh (radial Gauss nodes in s = log r, midpoint in theta).
Outer part (r > R): exact sectors F_n(r) = sum_s e_{s,n} r^(alpha_s):
   outer-outer: pi/(2n) sum_{s,s'} e e' [ int_R^inf int_R^r (r'/r)^n r^(a+1) r'^(a'+1) dr' dr + (sym) ]  with
      int_R^inf r^(a+1-n) int_R^r r'^(a'+1+n) dr' dr = int_R^inf r^(a+1-n) [r^(a'+2+n) - R^(a'+2+n)]/(a'+2+n) dr
      = [ R^(a+a'+4)/(-(a+a'+4)) - R^(a'+2+n) R^(a+2-n)/(-(a+2-n)) ] / (a'+2+n)   (needs a+a'+4 < 0 and a+2-n < 0)
   inner-outer cross: 2 * pi/(2n) sum_s e_{s,n} [int_0^R F_n(r) r^(n+1) dr] * R^(alpha_s+2-n)/(n-alpha_s-2).
"""
import math
import numpy as np
import torch
import mpmath as mp
import ipm_exact as X

def _panel_size(ws):
    """number of Gauss nodes per panel: Gauss weights are symmetric, so the first index k > 0 with w_k = w_0 is the panel's last node"""
    w0 = float(ws[0])
    for k in range(1, len(ws)):
        if abs(float(ws[k])-w0) < 1e-12*abs(w0): return k+1
    return len(ws)

_GEOM = {}
def _panel_geometry(panel, s_np):
    """for each panel: A, B, half-width, Lagrange->monomial coefficient matrix (columns = basis functions in z)"""
    key = (panel, len(s_np), float(s_np[0]))
    if key in _GEOM: return _GEOM[key]
    z, _ = np.polynomial.legendre.leggauss(panel)
    V = np.vander(z, increasing=True); coeffs = np.linalg.solve(V, np.eye(panel))   # l_k(z) = sum_j coeffs[j,k] z^j
    pans = []
    for b in range(0, len(s_np), panel):
        x = s_np[b:b+panel]; half = (x[1]-x[0])/(z[1]-z[0]); mid = x[0]-half*z[0]
        pans.append((mid-half, mid+half, half))
    _GEOM[key] = (z, coeffs, pans)
    return _GEOM[key]

_GQ64 = np.polynomial.legendre.leggauss(64)
def _exp_moments(a, zi, J):
    """m_j = int_{-1}^{zi} z^j e^{a (z - zi)} dz, j = 0..J-1 (a > 0).  a >= 2J: forward recursion (stable, j/a < 1/2);
    otherwise 64-node Gauss quadrature on [-1, zi] (the integrand e^{a(z-zi)} z^j is resolved for a <= 2J <= 64)."""
    if a >= 2*J:
        out = np.empty(J); e = math.exp(-a*(zi+1.0))
        out[0] = (1.0-e)/a
        for j in range(1, J):
            out[j] = (zi**j-((-1)**j)*e)/a-(j/a)*out[j-1]
        return out
    x, w = _GQ64
    zz = (zi+1)/2*(x+1)-1; ww = w*(zi+1)/2
    ex = np.exp(a*(zz-zi))
    return np.array([np.sum(ww*ex*zz**j) for j in range(J)])

def cumulative_exp_matrix(n, s_np, ws_np, panel):
    """W^(n)_{ik} = int_0^{s_i} l_k(s) e^{(n+2)(s - s_i)} ds over the whole grid (k over all nodes; l_k the Lagrange basis of k's panel),
    exact for the piecewise polynomial interpolant of F_n; the origin region below the first node is omitted."""
    z, coeffs, pans = _panel_geometry(panel, s_np)
    Nr = len(s_np); W = np.zeros((Nr, Nr)); a_n = n+2
    for pi_, (A, B, half) in enumerate(pans):
        a = a_n*half
        b0 = pi_*panel
        # full-panel exponential moments relative to the panel end B: int_A^B l_k e^{a_n (s - B)} ds = half * sum_j coeffs[j,k] m_j(a, 1)
        mfull = _exp_moments(a, 1.0, panel)
        full_w = half*(mfull@coeffs)                       # (panel,) weights for int_A^B l_k(s) e^{a_n (s-B)} ds
        for i in range(Nr):
            si = s_np[i]
            if si >= B-1e-12:                             # later nodes: whole panel, factor e^{a_n (B - s_i)}
                if si > B+1e-12 or i >= b0+panel: W[i, b0:b0+panel] = full_w*math.exp(a_n*(B-si))
            if b0 <= i < b0+panel:                         # node inside this panel: partial moments up to z_i
                zi = z[i-b0]; mpart = _exp_moments(a, zi, panel)
                W[i, b0:b0+panel] = half*(mpart@coeffs)
    return W

def hminus1(F, mesh, R, E_sectors=None, nmax=None):
    """F: (Nr, Nt) tensor on a midpoint-theta product mesh (quarter plane); mesh.ws weights for ds, mesh.r radii (all <= R assumed for the
    inner nodes; nodes with r > R are ignored); E_sectors: dict exponent(mpq) -> sine dict (mpq) of the residual beyond R.
    Returns dict with inner, cross, outer, total (floats) and per-mode contributions."""
    r = mesh.r; sel = (r <= R)
    rr = r[sel]; ws = mesh.ws[sel]; Fi = F[sel]
    th = mesh.theta; wth = mesh.wth
    Nt = mesh.Nt
    if nmax is None: nmax = 2*Nt-1
    ns = list(range(1, nmax+1, 2))
    S = torch.stack([torch.sin(n*th) for n in ns])                    # (nn, Nt)
    Fn = (4/math.pi)*(Fi*wth[None, :])@S.T                              # (Nr, nn):  F_n(r_i)
    # inner double integral per mode, kink-free form:  I_n = int int (r_</r_>)^n F_n(r) F_n(r') r r' dr dr' = 2 int_0^R F_n(r) r^(1-n) J_n(r) dr,
    #   J_n(r) = int_0^r F_n(r') r'^(1+n) dr'  (cumulative integral, computed panel-wise by Lagrange interpolation on the Gauss nodes in s = log r,
    #   exact for the polynomial interpolant of the integrand on each panel). Nodes must form complete Gauss panels of equal size in s.
    inner = {}; cross = {}; outer = {}
    s_np = torch.log(rr).cpu().numpy(); ws_np = ws.cpu().numpy(); panel = _panel_size(ws)
    Fn_np = Fn.cpu().numpy(); rr_np = rr.cpu().numpy()
    for k, n in enumerate(ns):
        fn = Fn_np[:, k]
        if not np.any(fn): inner[n] = 0.0; continue
        Wn = cumulative_exp_matrix(n, s_np, ws_np, panel)   # J~_n(r_i) = int_0^{s_i} F_n e^{(n+2)(s'-s_i)} ds'
        Jt = Wn@fn
        inner[n] = math.pi/(2*n)*2*float((ws_np*fn*rr_np**4*Jt).sum())   # I_n = 2 int F_n r^4 J~_n ds
    # exact far part
    if E_sectors:
        Rm = mp.mpf(R)
        # outer-outer and cross per mode
        for k, n in enumerate(ns):
            tot_oo = mp.mpf(0); tot_cr = mp.mpf(0)
            # scaled moment int_0^R F_n (r/R)^(n+2) ds = sum_i w_i (r_i/R)^(n+2) F_n(r_i)   (stable); times R^(n+2) R^(alpha+2-n) = R^(alpha+4)
            mom = float((Fn[:, k]*ws*(rr/R)**(n+2)).sum())
            items = [(a, X.qfloat(E[n])) for a, E in E_sectors.items() if n in E and E[n] != 0]
            for a, e in items:
                af = mp.mpf(int(a.numerator))/int(a.denominator)
                if af+2-n >= 0: return None
                tot_cr += e*mp.power(Rm, af+4)/(n-af-2)
                for a2, e2 in items:
                    af2 = mp.mpf(int(a2.numerator))/int(a2.denominator)
                    if af+af2+4 >= 0: return None
                    # I(a, a2) = int_R^inf r^(a+1-n) int_R^r r'^(a2+1+n) dr' dr
                    I = (mp.power(Rm, af+af2+4)/(-(af+af2+4)) - mp.power(Rm, af2+2+n)*mp.power(Rm, af+2-n)/(-(af+2-n)))/(af2+2+n)
                    tot_oo += e*e2*I
            outer[n] = float(mp.pi/(2*n)*2*tot_oo)      # factor 2: both orderings r < r' and r > r' (sum over ordered sector pairs covers the sectors, not the orderings)
            cross[n] = float(2*mp.pi/(2*n)*mom*tot_cr)
    tot_in = sum(inner.values()); tot_cr = sum(cross.values()); tot_out = sum(outer.values())
    return {'inner': tot_in, 'cross': tot_cr, 'outer': tot_out, 'total_sq': tot_in+tot_cr+tot_out, 'H': math.sqrt(max(tot_in+tot_cr+tot_out, 0)),
            'per_mode_sq': {n: inner[n]+cross.get(n, 0)+outer.get(n, 0) for n in ns if abs(inner[n]+cross.get(n, 0)+outer.get(n, 0)) > 1e-30}}
