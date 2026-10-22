"""B(K, K) = U[K] . grad K in the X norm (lead 13:54Z, 'if cheap'), K = rho~ - X.grad rho~ = rho~ - d_t rho~ the scaling tangent of the modal trial.
FLOATING. Method: rho~ = e^{3t} cos^2 th sin th sum_m a_m(t) cos 2m th (TrialGreen conventions), hence
  K = e^{3t} cos^2 th sin th sum_m a~_m(t) cos 2m th  with  a~_m = -2 a_m - a_m'
(same form as rho~ with a_m replaced by a~_m: degree-7 polynomial per knot cell, exponential-polynomial outside). A TrialGreen object GK is built
for K (wrapper TrialK: eval, inner/outer exp-poly terms and the per-cell Taylor coefficients pc transformed accordingly), giving the canonical
inverse psi[K] in closed form; then with c_l = 0, GK.residual_modes = U[K].grad K - K, so B(K, K) = that + K, and the jets of src/xnorm_jets.py
(eps_mode_jets with c_l = 0, order <= 1) give d_t B(K, K). X norm as in xnorm_jets (exact angular integral; Gauss-Legendre on the knot cells).
Checks: K modes from GK.rho_modes against R - R' from the rho~ jets; c[K] = GK.c (should vanish: the scaling tangent carries no strain at 0);
psi[K] against the scaling identity: K = -d/dlambda [lambda^{-1} rho~(lambda X)] at lambda = 1, and the canonical inverse (no homogeneous r^{2n}
terms at infinity, no r^{-2n} terms at the origin; psi~ itself GROWS like r^{k+1}) of lambda^{-1} rho~(lambda X) is lambda^{-2} psi~(lambda X), so
psi[K] = -d/dlambda [lambda^{-2} psi~(lambda X)] = 2 psi~ - X.grad psi~, i.e. psi[K]_n(t) = 2 psi_n(t) - d_t psi_n(t) (and c[K] = 2c - 2c = 0).
Referee astra/bkk1 (19:1xZ): transforms and identities confirmed; the comparisons are consistency checks sharing the Green implementation (an added
harmonic c xy would pass them too), the inner exp-poly terms are tested only through their moments, and B = (U[K].grad K - K) + K loses about
1e-13 relative to cancellation (K ~ 386, B ~ 1200 at most).
Usage: python3 src/xnorm_BKK.py trial.npz g cell_lo cell_hi out.json   (cells as in xnorm_jets: 120 inner + 1558 knot + 240 outer)
       python3 src/xnorm_BKK.py --check trial.npz"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen
from trial_jets import TrialJets
from xnorm_jets import eps_mode_jets, cells_all, weight, REGIONS


class TrialK:
    """a~_m = -2 a_m - a_m' in place of a_m (K = rho~ - d_t rho~)."""
    def __init__(self, T):
        self.T = T
        for name in ("k", "L", "rmin", "R0", "knots", "p", "M", "tmin", "t0", "S"): setattr(self, name, getattr(T, name))
    @staticmethod
    def _transform(terms):
        out = []
        for alpha, c in terms:
            ct = -(2.0 + alpha) * c
            if c.shape[0] > 1: ct[:-1] -= c[1:] * np.arange(1, c.shape[0])[:, None]
            out.append((alpha, ct))
        return out
    def inner_terms(self): return self._transform(self.T.inner_terms())
    def outer_terms(self): return self._transform(self.T.outer_terms())
    def eval(self, t, nu=0): return -2.0 * self.T.eval(t, nu) - self.T.eval(t, nu + 1)


def green_for_K(T):
    GK = TrialGreen(TrialK(T))
    pc = GK.pc.copy(); pcK = -2.0 * pc
    pcK[:, :-1, :] -= pc[:, 1:, :] * np.arange(1, pc.shape[1])[None, :, None]       # a' Taylor coefficients: (i+1) pc[i+1]
    GK.pc = pcK; GK.build(); GK.c_l = 0.0
    return GK


def check(path):
    T = Trial(np.load(path)); G = TrialGreen(T); t0 = time.time(); G.build(); GK = green_for_K(T); print("builds %.0fs" % (time.time() - t0))
    t = np.array([-2.0, 0.3, 1.5, 2.1517, 2.7, 5.0, 9.0])
    mj = TrialJets(G, K=2).modal_jets(t); R = mj["R"]; PSI = mj["PSI"]
    KR, KRt = GK.rho_modes(t)
    print("K modes: GK.rho_modes vs R - R' from the rho~ jets: max abs diff %.2e (max |K_N| %.2e); d_t K: %.2e (max %.2e)" % (np.abs(KR - (R[0] - R[1])).max(), np.abs(KR).max(), np.abs(KRt - (R[1] - R[2])).max(), np.abs(KRt).max()))
    psiK, dpsiK = GK.psi_at(t)
    pred = 2 * PSI[0] - PSI[1]; predd = np.exp(-t)[:, None] * (2 * PSI[1] - PSI[2])
    print("psi[K]_n vs 2 psi_n - d_t psi_n (scaling identity): max abs diff %.2e (max |psi[K]| %.2e); d_r psi[K]: %.2e (max %.2e)" % (np.abs(psiK - pred).max(), np.abs(psiK).max(), np.abs(dpsiK - predd).max(), np.abs(dpsiK).max()))
    print("c[K] = GK.c = %.3e  (c[rho~] = G.c = %.6f; expected c[K] = 0 up to roundoff)" % (GK.c, G.c))
    E = GK.residual_modes(t); B = E.copy(); B[:, :GK.M + 1] += KR
    print("B(K,K) modes at the test radii: max |B_N| per radius:", " ".join("%.3e" % v for v in np.abs(B).max(1)))
    # FD check of d_t B via eps_mode_jets order 1
    def addK(Earr, Karr):
        out = Earr.copy(); out[:, :GK.M + 1] += Karr; return out
    mjK = TrialJets(GK, K=1).modal_jets(t); EK = eps_mode_jets(GK, mjK, 1); B0 = addK(EK[0], mjK["R"][0]); B1 = addK(EK[1], mjK["R"][1])
    print("B(K,K) order 0: jets vs residual_modes + K: %.2e" % np.abs(B0 - B).max())
    h = 1e-4; f = lambda s: addK(GK.residual_modes(t + s), GK.rho_modes(t + s)[0])
    fd1 = (-f(2 * h) + 8 * f(h) - 8 * f(-h) + f(-2 * h)) / (12 * h)
    print("d_t B(K,K): jets vs 5-point FD (h=1e-4): max abs diff %.2e (max |d_t B| %.2e)" % (np.abs(B1 - fd1).max(), np.abs(B1).max()))


def main(path, g, lo, hi, out, rmin_tot=1e-4, rmax_tot=1e7, n_in=120, n_out=240):
    T = Trial(np.load(path)); t0 = time.time(); GK = green_for_K(T); G0 = TrialGreen(T)   # G0 only for the cell list (no build needed)
    b, kind_c = cells_all(G0, rmin_tot, rmax_tot, n_in, n_out); ncell = len(b) - 1; nin = int((kind_c == 1).sum()); nknot = int((kind_c == 0).sum())
    print("GK build %.0fs; cells %d; piece [%d, %d); c[K] = %.3e" % (time.time() - t0, ncell, lo, hi, GK.c), flush=True)
    if hi <= lo: return
    assert 0 <= lo < hi <= ncell
    xg, wg = np.polynomial.legendre.leggauss(g); ta = b[lo:hi]; hc = b[lo + 1:hi + 1] - ta
    t = (ta[:, None] + 0.5 * hc[:, None] * (xg[None, :] + 1)).ravel(); wq = (0.5 * hc[:, None] * wg[None, :]).ravel()
    kind = np.repeat(kind_c[lo:hi], g)
    t1 = time.time(); mj = TrialJets(GK, K=1).modal_jets(t); E = eps_mode_jets(GK, mj, 1)
    KN = mj["R"][0]; KNt = mj["R"][1]; B0 = E[0].copy(); B0[:, :GK.M + 1] += KN; B1 = E[1].copy(); B1[:, :GK.M + 1] += KNt
    print("jets at %d nodes: %.0fs" % (len(t), time.time() - t1), flush=True)
    w = weight(T, t); r = np.exp(t)
    def dens(f, ft):
        kN = (2 * np.arange(f.shape[1]) + 1.0)[None, :]; pref = np.pi * np.exp(2 * t) * w
        return pref * (f ** 2).sum(1), pref * (ft ** 2).sum(1), pref * ((kN ** 2) * f ** 2).sum(1)
    res = dict(trial=path, g=g, piece=[lo, hi], ncell_total=ncell, n_inner=nin, n_knot=nknot, rmin_tot=rmin_tot, rmax_tot=rmax_tot, n_in=n_in, n_out=n_out,
               t_range=[float(b[lo]), float(b[hi])], c_K=float(GK.c),
               weight="m^-2 (1+u^2)^-1.5, m = u^3 (1+u^2)^((k-3)/2)", method=__doc__.split("\n")[0], norm2={}, parts_norm2={},
               parts_definition="value, d_t, d_theta parts of pi int e^{2t} w sum_N [f_N^2 + (d_t f_N)^2 + (2N+1)^2 f_N^2] dt",
               regions_note="regions are unions of whole cells (boundaries log 2, log 4, log 16 inserted); 'all' is the truncated range [rmin_tot, rmax_tot] only")
    for name, (f, ft) in {"B(K,K) = U[K].grad K": (B0, B1), "K = rho~ - X.grad rho~ (from GK)": (KN, KNt)}.items():
        parts = [q * wq for q in dens(f, ft)]; d = parts[0] + parts[1] + parts[2]; row = {}; prow = {}
        for reg, sel in REGIONS.items():
            mask = {"middle (knot cells)": kind == 0, "inner (r<0.00765)": kind == 1, "outer (r>3413)": kind == 2}[reg] if sel is None else sel(r)
            row[reg] = float(d[mask].sum()); prow[reg] = [float(q[mask].sum()) for q in parts]
        res["norm2"][name] = row; res["parts_norm2"][name] = prow
        print("%-32s " % name + "  ".join("%s %.6e" % (k2, v) for k2, v in row.items()), flush=True)
        print("   parts (value, d_t, d_theta) all: %.4e %.4e %.4e" % tuple(prow["all"]), flush=True)
    # sup-type diagnostics of B along t: max_N |B_N| and the X-density
    res["max_abs_B_mode_over_nodes"] = float(np.abs(B0).max()); res["time"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1); print("saved", out, "(%.0fs)" % res["time"])


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--check": check(a[1])
    else: main(a[0], int(a[1]), int(a[2]), int(a[3]), a[4])
