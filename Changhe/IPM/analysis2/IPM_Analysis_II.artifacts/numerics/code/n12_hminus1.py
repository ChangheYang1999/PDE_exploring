"""FLOAT estimate of the low component L(F) = ||w F||_{Hdot^-1(R^2)}, w = (1 + r^2/R^2)^(-11/10), R = 2^35 (verifier V073 weight), and of the
unweighted ||F||_{Hdot^-1}, for the residual F of an n12 potential file (exact 'generators' JSON or float 'gens/coefs' JSON).
F on a log-polar grid (ns radii on [RMIN, RGRID], nth quarter-angles, midpoint rule in theta, potential jets to order 3 by n12_eval), projected on the
odd sine modes k < 2 nth (exact for trig polynomials of degree < 2 nth); beyond RGRID the mode functions come from the EXACT far-field residual sectors
(n12_exact.sectors_general, q <= Q, exponent > -6) on a log grid continued to r = RGRID e^UEXT; below RMIN F = O(r^3) is dropped.
Mode potential u_k = (1/2k)[r^-k int_0^r t^(k+1) g_k dt + r^k int_r^inf t^(1-k) g_k dt] by the scaled log-space recursion (trapezoid);
L^2 = pi sum_k int g_k u_k r dr.  Also the dyadic profile of the integrand and the unweighted ||F||_2 for reference.
Usage: n12_hminus1.py file.json out.json ns nth RMIN RGRID [du_ext] [Q]"""
import sys, os, json, math, time
sys.set_int_max_str_digits(0)
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet
from n12_norms import load_gens
from n12_exact import sectors_general

def mode_hm1(u, gk_modes, ks, w):
    """u: log-radius grid (uniform step), gk_modes: dict k -> g_k(r) (already weighted), returns total L^2 and per-mode, plus the integrand profile per u."""
    du = u[1] - u[0]; r = np.exp(u); n = len(u)
    tw = np.full(n, du); tw[0] = tw[-1] = du/2
    tot = 0.0; per = {}; prof = np.zeros(n)
    for k in ks:
        gk = gk_modes[k]; wgt = gk*r*r*tw; q = math.exp(-k*du)
        A = np.empty(n); B = np.empty(n); acc = 0.0
        for i in range(n): acc = acc*q + wgt[i]; A[i] = acc
        acc = 0.0
        for i in range(n-1, -1, -1): acc = acc*q + wgt[i]; B[i] = acc
        uk = (A + B - wgt)/(2*k)
        contrib = math.pi*wgt*uk; per[int(k)] = float(contrib.sum()); tot += per[int(k)]; prof += contrib
    return tot, per, prof

def main(path, out, ns, nth, RMIN, RGRID, du_ext=0.02, Q=3):
    t0 = time.time()
    gens, coefs, cl, p = load_gens(path); clf = float(cl); g = 1/clf
    s = np.linspace(math.log(RMIN), math.log(RGRID), ns); ds = s[1]-s[0]
    th = (np.arange(nth)+0.5)/nth*math.pi/2
    S, TH = np.meshgrid(s, th, indexing='ij'); r = np.exp(S).ravel(); x = (np.exp(S)*np.cos(TH)).ravel(); y = (np.exp(S)*np.sin(TH)).ravel()
    ORD = 3; cache = make_cache(x, y, ORD); J = {}
    for gen, c in zip(gens, coefs):
        c = float(c)
        if c == 0: continue
        gj = generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], ORD, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
    rho = -(J[(2, 1)] + J[(0, 3)]); rho_x = -(J[(3, 0)] + J[(1, 2)]) if False else None
    # grad rho needs order 4 jets of the potential: rho_x = -(phi_xxxy + phi_xyyy), rho_y = -(phi_xxyy + phi_yyyy) -> use ORD 4
    print('order-3 jets done in %.0f s; recomputing with order 4 for grad rho' % (time.time()-t0), flush=True)
    ORD = 4; cache = make_cache(x, y, ORD); J = {}
    for gen, c in zip(gens, coefs):
        c = float(c)
        if c == 0: continue
        gj = generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], ORD, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
    rho = -(J[(2, 1)] + J[(0, 3)]); rho_x = -(J[(3, 1)] + J[(1, 3)]); rho_y = -(J[(2, 2)] + J[(0, 4)]); U1 = -J[(1, 2)]; U2 = J[(2, 1)]
    F = ((clf*x + U1)*rho_x + (clf*y + U2)*rho_y - rho).reshape(ns, nth)
    print('F on %d x %d grid in %.0f s; sup|F| = %.4g' % (ns, nth, time.time()-t0, np.abs(F).max()), flush=True)
    ks = np.arange(1, 2*nth, 2)
    W = (4/math.pi)*(math.pi/2/nth)*np.sin(np.outer(ks, th))      # f_k = (4/pi) int_0^(pi/2) F sin(k theta) dtheta (odd k; F odd in y, even in x)
    fk = F @ W.T                                                  # ns x nk
    # far-field continuation from the exact sectors
    X = sectors_general(gens, coefs, cl, qmax=Q, hmax=8, jmax=7)
    secs = [(float(X['alpha'](h, q)), {int(k): float(v) for k, v in Sd.items()}) for (h, q), Sd in X['E'].items() if Sd and float(X['alpha'](h, q)) > -6]
    u_ext = np.arange(s[-1] + du_ext, s[-1] + 60.0, du_ext)
    # combined grid: grid part at step ds, far part at step du_ext -> resample both onto a common uniform grid of step du = min(ds, du_ext) by linear interpolation in log r
    du = min(ds, du_ext); u_all = np.arange(s[0], s[-1] + 60.0, du); r_all = np.exp(u_all)
    w_all = (1 + (r_all/2.0**35)**2)**(-1.1)
    modes_w = {}; modes_1 = {}
    for j, k in enumerate(ks):
        far = np.zeros_like(u_all)
        for al, Sd in secs:
            if k in Sd: far += Sd[k]*np.exp(al*u_all)
        gk = np.where(u_all <= s[-1] + 1e-12, np.interp(u_all, s, fk[:, j]), far)
        modes_w[int(k)] = w_all*gk; modes_1[int(k)] = gk
    totw, perw, profw = mode_hm1(u_all, modes_w, ks, None); tot1, per1, prof1 = mode_hm1(u_all, modes_1, ks, None)
    L2grid = math.sqrt(math.pi*np.sum(fk**2*(np.exp(s)**2)[:, None]*ds))
    dyadic = {}
    for jj in range(int(math.floor(u_all[0]/math.log(2))), int(math.ceil(u_all[-1]/math.log(2)))):
        sel = (r_all >= 2.0**jj) & (r_all < 2.0**(jj+1))
        if sel.any(): dyadic[jj] = float(profw[sel].sum())
    res = {'file': path, 'grid': {'ns': ns, 'nth': nth, 'RMIN': RMIN, 'RGRID': RGRID, 'du_ext': du_ext, 'Q': Q}, 'L_weighted': math.sqrt(totw), 'Hminus1_unweighted': math.sqrt(tot1),
           'per_mode_weighted_sq': perw, 'L2_grid_part': L2grid, 'sup_F_grid': float(np.abs(F).max()), 'dyadic_profile_weighted_sq': dyadic,
           'far_sectors_used': [(al, len(Sd)) for al, Sd in secs], 'E2_estimate_low_part': 2**26.5*math.sqrt(totw)}
    json.dump(res, open(out, 'w'), indent=1)
    print('L(F) = ||wF||_Hdot^-1 about %.6g ; unweighted ||F||_Hdot^-1 about %.6g ; 2^26.5 L about %.4g ; ||F||_L2(grid) %.4g ; modes 1,3,5 (sq): %s' % (math.sqrt(totw), math.sqrt(tot1), 2**26.5*math.sqrt(totw), L2grid, {k: '%.3e' % perw[k] for k in (1, 3, 5)}))
    print('dyadic profile of L^2 (j: r in [2^j, 2^(j+1))):', {j: '%.3e' % v for j, v in dyadic.items() if v > 1e-6*totw})

if __name__ == '__main__':
    a = sys.argv
    main(a[1], a[2], int(a[3]), int(a[4]), float(a[5]), float(a[6]), float(a[7]) if len(a) > 7 else 0.02, int(a[8]) if len(a) > 8 else 3)
