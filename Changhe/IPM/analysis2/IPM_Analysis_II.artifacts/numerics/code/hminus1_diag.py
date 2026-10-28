"""FLOAT diagnostic: Hdot^-1 norm of the residual after subtracting its non-Hdot^-1 far-field sectors.
F_sub(X) := F(X) - chi(r) sum_{(h,q): alpha_hq > -2} r^{alpha_hq} E_hq(theta),  chi smooth, chi = 0 for r <= 1, 1 for r >= 2 (chi = S((r-1)) with S the smoothstep 6u^5-15u^4+10u^3).
A function ~ r^alpha Theta(theta) (no zero mode) at infinity is in Hdot^-1 iff alpha < -2; the seven sectors with alpha > -2 are (1,0),(2,0),(3,0),(4,0),(0,1),(5,0),(1,1).
Mode formula (SPEC S2): f = sum_k f_k(r) sin(k theta) (odd k), Phi_k(r) = (1/2k)[r^-k int_0^r t^{k+1} f_k dt + r^k int_r^inf t^{1-k} f_k dt],
||f||^2_{Hdot^-1} = ||grad Phi||^2_{L2(R^2)} = pi sum_k int_0^inf (Phi_k'^2 + k^2 Phi_k^2 / r^2) r dr   (int_0^{2pi} sin^2 = pi).
Also reports ||F_sub||_L2, sup|F_sub| and the same quantities for the UNsubtracted residual restricted to r <= R (for scale).
Radial grid in s = log r (trapezoid); angular modes by exact quadrature of the sine series at Chebyshev-like equispaced angles (the integrand
is a trig polynomial of degree <= 39 in theta plus the smooth F; 128 angles). Far-field tail beyond s_max from the remaining sectors (alpha < -2).
"""
import sys, os, json, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fractions import Fraction as Fr
from multiprocessing import Pool
import farfield_exact as FE
from ipm_arb import State

STATE = None
def init(path):
    global STATE
    STATE = State(path, prec=128)
def work(args):
    s, th = args
    r = math.exp(s); x = r*math.cos(th); y = r*math.sin(th)
    f = STATE.fields(x, y, order=4)
    return float(f['F'].mid())

def smoothstep(u):
    u = np.clip(u, 0, 1); return 6*u**5 - 15*u**4 + 10*u**3

if __name__ == '__main__':
    exact_json, out_json = sys.argv[1], sys.argv[2]
    smin, smax, ds, nth, nproc = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
    d = json.load(open(exact_json)); cl = Fr(d['cl']); a = [Fr(v) for v in d['a_canonical']]
    g = Fr(1)/cl; lam = 1-g
    X = FE.expand(cl, a, qmax=6, hmax=7)
    def alpha(h, q): return float(g - h*lam - 2*q)
    sub = [(hq, alpha(*hq), {k: float(v) for k, v in S.items()}) for hq, S in X['E'].items() if S and alpha(*hq) > -2]
    rest = [(hq, alpha(*hq), {k: float(v) for k, v in S.items()}) for hq, S in X['E'].items() if S and alpha(*hq) <= -2]
    print('subtracted sectors:', [(hq, round(al, 3)) for hq, al, S in sub], flush=True)
    svals = np.arange(smin, smax + ds/2, ds); rvals = np.exp(svals)
    thetas = (np.arange(nth) + 0.5)/nth*math.pi/2          # quadrant; F odd in y, even in x: full-circle sine modes from the quadrant
    tasks = [(float(s), float(t)) for s in svals for t in thetas]
    gridfile = out_json.replace('.json', '_Fgrid.npz'); shared = os.path.join(os.path.dirname(out_json), 'hminus1_diag_131_Fgrid_shared.npz') if '131' in out_json else gridfile
    if not os.path.exists(gridfile) and os.path.exists(shared): gridfile = shared
    if os.path.exists(gridfile):
        Fgrid = np.load(gridfile)['Fgrid']; print('loaded grid', gridfile, flush=True)
    else:
        t0 = time.time()
        with Pool(nproc, initializer=init, initargs=(exact_json,)) as pool:
            vals = pool.map(work, tasks, chunksize=16)
        Fgrid = np.array(vals).reshape(len(svals), nth)
        np.savez(gridfile, Fgrid=Fgrid, svals=svals, thetas=thetas)
        print('evaluated %d points in %.0f s' % (len(tasks), time.time()-t0), flush=True)
    c_lo, c_hi = float(sys.argv[8]), float(sys.argv[9])
    chi = smoothstep((rvals - c_lo)/(c_hi - c_lo))
    # subtracted far field on the grid
    Fsub = Fgrid.copy()
    for hq, al, S in sub:
        prof = np.zeros(nth)
        for k, v in S.items(): prof += v*np.sin(k*thetas)
        Fsub -= (chi*rvals**al)[:, None]*prof[None, :]
    # sine modes on the quadrant: f_k = (4/pi) int_0^{pi/2} f sin(k theta) dtheta for odd k (f odd in y, even in x -> only odd k)
    ks = np.arange(1, 40, 2)
    W = (4/math.pi)*(math.pi/2/nth)*np.sin(np.outer(ks, thetas))        # (nk x nth) quadrature weights (midpoint rule; exact for trig polys of degree < 2 nth)
    fk = Fsub @ W.T                      # (ns x nk)
    fk_full = Fgrid @ W.T
    # mode potentials: Phi_k(r) = (1/2k)[ r^-k I1(r) + r^k I2(r) ], I1 = int_0^r t^{k+1} f_k dt = int t^{k+2} f_k ds, I2 = int_r^inf t^{1-k} f_k dt = int t^{2-k} f_k ds
    # tails: below smin: F_sub = O(r^7): f_k ~ c r^7 -> I1(r_min) ~ f_k(r_min) r_min^{k+2}/(k+9)? we neglect (r_min tiny); above smax: from 'rest' sectors analytically
    def restmode(k, r):   # sum over remaining sectors of r^alpha * coefficient of sin k
        return sum(S.get(k, 0.0)*r**al for hq, al, S in rest)
    res = {}
    for name, F_k in (('F_sub', fk), ('F_full_cut_R', fk_full)):
        total = 0.0; L2 = 0.0; permode = {}
        for j, k in enumerate(ks):
            f = F_k[:, j]
            # log-space mode integrals (no overflow): r^-k I1(r) = int_{s'<s} e^{-k(s-s')} e^{2s'} f_k(s') ds',  r^k I2(r) = int_{s'>s} e^{-k(s'-s)} e^{2s'} f_k(s') ds'
            g = rvals**2*f
            S1 = svals[:, None]; S2 = svals[None, :]
            Kmat1 = np.where(S2 <= S1, np.exp(-k*(S1 - S2)), 0.0); Kmat2 = np.where(S2 >= S1, np.exp(-k*(S2 - S1)), 0.0)
            wts = np.full(len(svals), ds); wts[0] = wts[-1] = ds/2
            I1s = Kmat1 @ (g*wts); I2s = Kmat2 @ (g*wts)
            if name == 'F_sub':
                # analytic tail beyond s_max from the remaining sectors: r^k int_R^inf t^{1-k} c t^alpha dt = c r^k R^{alpha+2-k}/(k-2-alpha)
                tail = sum(S.get(k, 0.0)*rvals[-1]**(al + 2 - k)/(k - 2 - al) for hq, al, S in rest if al + 2 - k < 0)
                I2s = I2s + tail*np.exp(-k*(svals[-1] - svals))*rvals[-1]**k*0 + tail*(rvals/rvals[-1])**k
            I1 = None; I2 = None
            Phi = (I1s + I2s)/(2*k)
            dPhi = np.gradient(Phi, svals)/rvals          # d/dr = (1/r) d/ds
            integrand = (dPhi**2 + k**2*Phi**2/rvals**2)*rvals**2   # (...) r dr = (...) r^2 ds
            Ek = math.pi*np.trapezoid(integrand, svals)
            permode[int(k)] = Ek; total += Ek
            L2 += math.pi*np.trapezoid(f**2*rvals**2, svals)
        res[name] = {'Hminus1_norm': math.sqrt(total), 'L2_norm': math.sqrt(L2), 'per_mode_energy': permode}
        print('%s: ||.||_{Hdot^-1} = %.6g  ||.||_{L2} = %.6g  (modes k=1,3,5: %s)' % (name, math.sqrt(total), math.sqrt(L2), [round(permode[k], 6) for k in (1, 3, 5)]), flush=True)
    res['sup_Fsub'] = float(np.abs(Fsub).max()); res['sup_Fsub_location'] = [float(rvals[np.unravel_index(np.abs(Fsub).argmax(), Fsub.shape)[0]]), float(thetas[np.unravel_index(np.abs(Fsub).argmax(), Fsub.shape)[1]])]
    res['grid'] = {'smin': smin, 'smax': smax, 'ds': ds, 'ntheta': nth, 'cutoff': [c_lo, c_hi]}; res['subtracted_sectors'] = [[list(hq), al] for hq, al, S in sub]
    # decay check of F_sub at large r: sup over theta of |F_sub| r^{2.13}
    tailchk = [(float(rvals[i]), float(np.abs(Fsub[i]).max()), float(np.abs(Fsub[i]).max()*rvals[i]**2.1295)) for i in range(0, len(rvals), max(1, len(rvals)//12))]
    res['Fsub_profile'] = tailchk
    print('sup|F_sub| = %.4g at r=%.3g; profile (r, max|F_sub|, max|F_sub| r^2.13):' % (res['sup_Fsub'], res['sup_Fsub_location'][0]), [(round(a, 3), '%.2e' % b, '%.2e' % c) for a, b, c in tailchk], flush=True)
    json.dump(res, open(out_json, 'w'), indent=1)
