"""eta_k.py -- windowed derivative residual ratios eta_k = ||D^k R||_2 / ||D^k rho||_2, k = 2..6 (lead 00:59Z item 3; FINAL_REPORT 3.40 for k = 3),
D^k = all k-th Cartesian partials with multinomial (Frobenius) weights, by central finite differences of the EVALUATED fields (canonical U) on a
tensor stencil with step h = hrel * r; L2 over a polar sample of the window [rmin, rmax] (nr log-spaced radii x 32 angles, weight r^2 dlog r dth).
Finite differences at order k lose ~ eps/h^k: the two steps hrel = 0.02, 0.05 and the two windows [0.1, 10], [0.05, 20] are the consistency levels;
disagreement between the steps marks rounding-dominated values.  Smooth convergence needs eta_k -> 0 for every k; a finite-regularity limit of
regularity s keeps eta_k from falling for k > s.  Sampled diagnostic only.  usage: python3 src/eta_k.py states... [nr=40]"""
import sys, math, numpy as np
sys.path.insert(0, 'numerics/src'); import qdiag
def fd_weights(k, m):
    """weights of the central stencil -m..m for the k-th derivative (exact for polynomials of degree <= 2m)."""
    pts = np.arange(-m, m + 1, dtype=float); V = np.vander(pts, increasing=True).T   # V[j, i] = pts[i]^j
    rhs = np.zeros(2 * m + 1); rhs[k] = math.factorial(k); return np.linalg.solve(V, rhs)
def eta(S, k, rmin, rmax, hrel, nr=40, nth=32):
    m = k // 2 + 1 if k % 2 == 0 else (k + 1) // 2 + 1
    rr = np.exp(np.linspace(np.log(rmin), np.log(rmax), nr)); th = (np.arange(nth) + 0.5) * np.pi / (2 * nth)
    RR, TT = np.meshgrid(rr, th, indexing='ij'); X, Y = RR * np.cos(TT), RR * np.sin(TT); H = hrel * RR
    offs = range(-m, m + 1); vals = {}
    for i in offs:
        for j in offs:
            o = S.ev_xy(X + i * H, Y + j * H); vals[(i, j)] = (o['R'], o['rho'])
    numR = np.zeros_like(RR); numr = np.zeros_like(RR)
    for a in range(k + 1):                                   # d_x^a d_y^(k-a)
        wa = fd_weights(a, m); wb = fd_weights(k - a, m); DR = np.zeros_like(RR); Dr = np.zeros_like(RR)
        for ii, i in enumerate(offs):
            if wa[ii] == 0: continue
            for jj, j in enumerate(offs):
                if wb[jj] == 0: continue
                DR += wa[ii] * wb[jj] * vals[(i, j)][0]; Dr += wa[ii] * wb[jj] * vals[(i, j)][1]
        DR /= H ** k; Dr /= H ** k; mult = math.comb(k, a)
        numR += mult * DR ** 2; numr += mult * Dr ** 2
    w = RR ** 2 * np.log(rr[1] / rr[0]) * (np.pi / (2 * nth))
    return math.sqrt((numR * w).sum()), math.sqrt((numr * w).sum())
if __name__ == '__main__':
    kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a); nr = int(kw.get('nr', 40))
    print(f"{'state':>24s} {'N':>4s} {'a0':>9s} | window [0.1,10]: eta_2..6 (hrel .02 | .05)                                   | window [0.05,20]: eta_2..6 (hrel .02 | .05)")
    for f in [a for a in sys.argv[1:] if '=' not in a]:
        S = qdiag.State(f); row = f"{f.split('/')[-1]:>24s} {S.N:4d} {S.a0:9.4f} |"
        for (r1, r2) in [(0.1, 10.0), (0.05, 20.0)]:
            for hrel in [0.02, 0.05]:
                es = []; absn = []
                for k in range(2, 7):
                    nR, nr_ = eta(S, k, r1, r2, hrel, nr=nr); es.append(nR / nr_); absn.append((nR, nr_))
                row += " " + " ".join(f"{e:.1e}" for e in es) + (" |" if hrel == 0.02 else " ||")
                row += "\n      abs ||D^k R||, ||D^k rho|| (" + f"[{r1},{r2}] h={hrel}): " + " ".join(f"{a:.2e}/{b:.2e}" for a, b in absn)
        print(row, flush=True)
