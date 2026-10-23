"""eta3.py -- windowed third-derivative residual ratio (lead 19:13Z item 4; FINAL_REPORT 3.40): eta_3 = ||D^3 R||_2 / ||D^3 rho||_2 on a fixed radial
window, with D^3 the four third partial derivatives (xxx, xxy, xyy, yyy) by central finite differences of the EVALUATED fields on a Cartesian stencil
(step h = hrel * r), L2 norms over a polar sample of the window (log-spaced radii, 32 angles).  A profile has eta_3 = 0; sampled diagnostic only.
usage: python3 src/eta3.py state.pt [rmin rmax [hrel]]"""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
f = sys.argv[1]; rmin = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1; rmax = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0; hrel = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-2
S = qdiag.State(f)
rr = np.exp(np.linspace(np.log(rmin), np.log(rmax), 40)); th = (np.arange(32) + 0.5) * np.pi / 64
RR, TT = np.meshgrid(rr, th, indexing='ij'); X, Y = RR * np.cos(TT), RR * np.sin(TT); H = hrel * RR
def fld(dx, dy):
    e = S.ev_xy(X + dx * H, Y + dy * H); return e['R'], e['rho']
def d3(F):      # F(dx, dy) -> dict of third derivatives via 4-point stencils: f_xxx = (f(2h) - 2 f(h) + 2 f(-h) - f(-2h)) / (2 h^3)
    def g(dx, dy): return F(dx, dy)
    Rxxx = (g(2, 0)[0] - 2 * g(1, 0)[0] + 2 * g(-1, 0)[0] - g(-2, 0)[0]) / (2 * H ** 3); rxxx = (g(2, 0)[1] - 2 * g(1, 0)[1] + 2 * g(-1, 0)[1] - g(-2, 0)[1]) / (2 * H ** 3)
    Ryyy = (g(0, 2)[0] - 2 * g(0, 1)[0] + 2 * g(0, -1)[0] - g(0, -2)[0]) / (2 * H ** 3); ryyy = (g(0, 2)[1] - 2 * g(0, 1)[1] + 2 * g(0, -1)[1] - g(0, -2)[1]) / (2 * H ** 3)
    # f_xxy = [f(h,h) - 2 f(0,h) + f(-h,h) - f(h,-h) + 2 f(0,-h) - f(-h,-h)] / (2 h^3)
    Rxxy = (g(1, 1)[0] - 2 * g(0, 1)[0] + g(-1, 1)[0] - g(1, -1)[0] + 2 * g(0, -1)[0] - g(-1, -1)[0]) / (2 * H ** 3)
    rxxy = (g(1, 1)[1] - 2 * g(0, 1)[1] + g(-1, 1)[1] - g(1, -1)[1] + 2 * g(0, -1)[1] - g(-1, -1)[1]) / (2 * H ** 3)
    Rxyy = (g(1, 1)[0] - 2 * g(1, 0)[0] + g(1, -1)[0] - g(-1, 1)[0] + 2 * g(-1, 0)[0] - g(-1, -1)[0]) / (2 * H ** 3)
    rxyy = (g(1, 1)[1] - 2 * g(1, 0)[1] + g(1, -1)[1] - g(-1, 1)[1] + 2 * g(-1, 0)[1] - g(-1, -1)[1]) / (2 * H ** 3)
    return (Rxxx, Rxxy, Rxyy, Ryyy), (rxxx, rxxy, rxyy, ryyy)
(DR, Dr) = d3(fld)
w = RR ** 2 * np.log(rr[1] / rr[0]) * (np.pi / 64)                                   # dX = r dr dth = r^2 dlog r dth
mult = (1, 3, 3, 1)                                                                   # Frobenius norm over ordered indices (lead's convention): xxx, xxy, xyy, yyy
nR = np.sqrt(sum((d ** 2 * w).sum() for d in DR)); nr = np.sqrt(sum((d ** 2 * w).sum() for d in Dr))
nRF = np.sqrt(sum(m * (d ** 2 * w).sum() for m, d in zip(mult, DR))); nrF = np.sqrt(sum(m * (d ** 2 * w).sum() for m, d in zip(mult, Dr)))
# step check at hrel/2
H = H / 2; (DR2, Dr2) = d3(fld); nR2 = np.sqrt(sum((d ** 2 * w).sum() for d in DR2)); nr2 = np.sqrt(sum((d ** 2 * w).sum() for d in Dr2))
print(f"ETA3 {f}: c_l={S.cl:.6f} a0={S.a0:.4f} window r in [{rmin:g}, {rmax:g}] (40 log radii x 32 angles): eta_3 (four components once) = {nR/nr:.4e} (hrel={hrel:g}) / {nR2/nr2:.4e} (hrel/2); eta_3 (Frobenius, multiplicities 1,3,3,1) = {nRF/nrF:.4e}; "
      f"||D^3 rho||_2 = {nr:.4g}, ||D^3 R||_2 = {nR:.4g}; pointwise max|R|/Nf on the window = {np.max(np.abs(fld(0,0)[0])/S.ev_xy(X, Y)['Nf']):.2e}")
