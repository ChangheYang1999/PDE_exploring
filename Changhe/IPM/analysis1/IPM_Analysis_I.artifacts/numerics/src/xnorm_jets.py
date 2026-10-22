"""Floating value of the X norms of eps~, eps~ - X.grad eps~ (= eps~ - d_t eps~), K = rho~ - X.grad rho~ and rho~ with ANALYTIC t-derivatives
(RESUME_HERE 3(i) of shift 5; replaces the finite-difference rows of NUM_REPORT 7.11, which were noise-dominated).
Modal jets from src/trial_jets.py (TrialJets.modal_jets: exact spline/exp-poly derivatives of a_m, Green ODEs for psi_n); the residual mode jets
d_t^i eps_N (i <= 2) by Leibniz on  eps = c_l R' - R + e^{-2t} sum_{n,j} [ -n psi_n R_j' + (2j+1)/2 psi_n' R_j ]  scattered to the frequencies
2j+1 +- 2n (same scattering as TrialGreen.residual_modes, vectorized over j).  Angular integration exact:
||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX = pi int e^{2t} w(t) sum_N [f_N^2 + (d_t f_N)^2 + (2N+1)^2 f_N^2] dt,  w = m^-2 (1+u^2)^-3/2.
Radial integration: Gauss-Legendre with g nodes on every knot cell of the trial (G.tb, 1558 cells, 0.00765 <= r <= 3413) plus log-spaced cells
on the inner (rmin_tot .. 0.00765) and outer (3413 .. rmax_tot) exp-polynomial ranges, with the region boundaries r = 2, 4, 16 inserted as cell
boundaries (regions are unions of whole cells). 'all' means the truncated range [rmin_tot, rmax_tot]; end densities and crude tail estimates are
saved. Refereed by astra (astra/xnorm1, 2026-10-21T18:5xZ): kernel and norm identity confirmed; the region-mask, merge and check defects it listed
are repaired in this version.
Usage:  python3 src/xnorm_jets.py trial.npz g cell_lo cell_hi out.json [rmin_tot rmax_tot n_in n_out]
  cells are indexed over the full list [inner cells] + [knot cells] + [outer cells]; cell_hi exclusive; the script prints the total count with
  cell_lo = cell_hi = 0.  python3 src/xnorm_jets.py --merge out.json piece1.json piece2.json ... sums the pieces.
  python3 src/xnorm_jets.py --check trial.npz : order-0 modes against TrialGreen.residual_modes and order 1, 2 against finite differences."""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb
from modal_fit import Trial
from trial_green import TrialGreen
from trial_jets import TrialJets


def eps_mode_jets(G, mj, K):
    """d_t^i eps_N(t), i <= K, N <= 2M+2, from the modal jets mj = TrialJets.modal_jets(t) (R up to order K+2, PSI up to order K+1)."""
    t = mj["t"]; R = mj["R"]; PSI = mj["PSI"]; nt = len(t); M = G.M; Nmax = 2 * M + 2; n = G.n; Nf = G.Nf
    em2 = np.exp(-2 * t)[:, None]; twoj1 = (2 * np.arange(M + 1) + 1.0)[None, :]
    # P^{(l)} scattered, l <= K
    Psc = np.zeros((K + 1, nt, Nmax + 1))
    for l in range(K + 1):
        for ni in range(Nf):
            nn = int(n[ni])
            c1 = np.zeros((nt, M + 1)); c2 = np.zeros((nt, M + 1))
            for l1 in range(l + 1):
                cc = comb(l, l1)
                c1 += cc * (-nn) * PSI[l1][:, ni][:, None] * R[l - l1 + 1]          # -n psi^{(l1)} R'^{(l-l1)}
                c2 += cc * 0.5 * twoj1 * PSI[l1 + 1][:, ni][:, None] * R[l - l1]     # (2j+1)/2 psi'^{(l1)} R^{(l-l1)}
            # term 1: freqs 2j+1+2n -> N = j+n ; 2j+1-2n -> N = j-n (j >= n, +), N = n-j-1 (j < n, -)
            Psc[l][:, nn:nn + M + 1] += c1
            Psc[l][:, 0:M + 1 - nn] += c1[:, nn:]
            Psc[l][:, 0:nn] -= c1[:, 0:nn][:, ::-1]
            # term 2: freqs 2n+2j+1 -> N = j+n ; 2n-2j-1 -> N = n-j-1 (j < n, +), N = j-n (j >= n, -)
            Psc[l][:, nn:nn + M + 1] += c2
            Psc[l][:, 0:nn] += c2[:, 0:nn][:, ::-1]
            Psc[l][:, 0:M + 1 - nn] -= c2[:, nn:]
    E = np.zeros((K + 1, nt, Nmax + 1))
    for i in range(K + 1):
        E[i][:, :M + 1] += G.c_l * R[i + 1] - R[i]
        for l in range(i + 1):
            E[i] += comb(i, l) * (-2.0) ** (i - l) * em2 * Psc[l]
    return E


REGION_BOUNDARIES_R = (2.0, 4.0, 16.0)      # the region boundaries r = 2, 4, 16 are inserted as cell boundaries (astra/xnorm1 item 4)


def cells_all(G, rmin_tot, rmax_tot, n_in, n_out):
    """Cell boundaries in t: n_in log-spaced inner cells on [log rmin_tot, tb[0]], the knot cells tb, n_out outer cells on [tb[-1], log rmax_tot],
    with the region boundaries log 2, log 4, log 16 inserted (so that every region is a union of whole cells). Returns (b, kind) with
    kind[c] = 1 (inner exp-poly range), 0 (knot range), 2 (outer exp-poly range) for each cell c."""
    tb = np.asarray(G.tb, float)
    assert np.all(np.diff(tb) > 0), "knot boundaries must increase"
    assert np.log(rmin_tot) < tb[0] and np.log(rmax_tot) > tb[-1], "rmin_tot / rmax_tot must lie outside the knot range"
    inner = np.linspace(np.log(rmin_tot), tb[0], n_in + 1)[:-1] if n_in > 0 else np.zeros(0)
    outer = np.linspace(tb[-1], np.log(rmax_tot), n_out + 1)[1:] if n_out > 0 else np.zeros(0)
    b = np.r_[inner, tb, outer]
    for rb in REGION_BOUNDARIES_R:
        x = np.log(rb)
        if b[0] < x < b[-1] and np.min(np.abs(b - x)) > 1e-12: b = np.sort(np.r_[b, x])
    assert np.all(np.diff(b) > 0)
    mid = 0.5 * (b[:-1] + b[1:])
    kind = np.where(mid < tb[0], 1, np.where(mid > tb[-1], 2, 0))
    return b, kind


def weight(T, t):
    k = T.k; L = T.L; u = np.exp(t) / L
    m = u ** 3 * (1 + u ** 2) ** ((k - 3) / 2)
    return m ** -2 * (1 + u ** 2) ** -1.5


REGIONS = {"r<2": lambda r: r < 2, "4<=r<=16": lambda r: (r >= 4) & (r <= 16), "rest (2<=r<4 or r>16)": lambda r: ~((r < 2) | ((r >= 4) & (r <= 16))),
           "all": lambda r: np.ones_like(r, bool), "middle (knot cells)": None, "inner (r<0.00765)": None, "outer (r>3413)": None}


def main(path, g, lo, hi, out, rmin_tot=1e-4, rmax_tot=1e7, n_in=120, n_out=240):
    T = Trial(np.load(path)); G = TrialGreen(T); t0 = time.time(); G.build()
    b, kind_c = cells_all(G, rmin_tot, rmax_tot, n_in, n_out); ncell = len(b) - 1
    nin = int((kind_c == 1).sum()); nknot = int((kind_c == 0).sum())
    print("cells: %d inner + %d knot (incl. the region splits) + %d outer = %d; piece [%d, %d)" % (nin, nknot, ncell - nin - nknot, ncell, lo, hi), flush=True)
    if hi <= lo: return
    assert 0 <= lo < hi <= ncell, "cell range out of bounds"
    xg, wg = np.polynomial.legendre.leggauss(g)
    ta = b[lo:hi]; tbb = b[lo + 1:hi + 1]; hc = tbb - ta
    t = (ta[:, None] + 0.5 * hc[:, None] * (xg[None, :] + 1)).ravel()                      # (ncells*g,)
    wq = (0.5 * hc[:, None] * wg[None, :]).ravel()
    kind = np.repeat(kind_c[lo:hi], g)
    J = TrialJets(G, K=2); t1 = time.time(); mj = J.modal_jets(t); E = eps_mode_jets(G, mj, 2)
    print("jets at %d nodes: %.0fs" % (len(t), time.time() - t1), flush=True)
    R = mj["R"]; w = weight(T, t); r = np.exp(t)
    def dens(f, ft):
        kN = (2 * np.arange(f.shape[1]) + 1.0)[None, :]; pref = np.pi * np.exp(2 * t) * w
        return pref * (f ** 2).sum(1), pref * (ft ** 2).sum(1), pref * ((kN ** 2) * f ** 2).sum(1)      # value, d_t, d_theta parts
    quantities = {"K = rho~ - X.grad rho~": (R[0] - R[1], R[1] - R[2]), "eps~": (E[0], E[1]), "eps~ - X.grad eps~": (E[0] - E[1], E[1] - E[2]), "rho~": (R[0], R[1])}
    res = dict(trial=path, g=g, piece=[lo, hi], ncell_total=ncell, n_inner=nin, n_knot=nknot, rmin_tot=rmin_tot, rmax_tot=rmax_tot, n_in=n_in, n_out=n_out,
               t_range=[float(b[lo]), float(b[hi])], weight="m^-2 (1+u^2)^-1.5, m = u^3 (1+u^2)^((k-3)/2)", method=__doc__.split("\n")[0], norm2={}, parts_norm2={},
               parts_definition="norm^2 = value + dt + dth: pi int e^{2t} w sum_N f_N^2 dt, pi int e^{2t} w sum_N (d_t f_N)^2 dt, pi int e^{2t} w sum_N (2N+1)^2 f_N^2 dt",
               regions_note="regions are unions of whole cells (boundaries log 2, log 4, log 16 inserted); 'all' is the truncated range [rmin_tot, rmax_tot] only",
               end_densities={}, tail_estimates_norm2={})
    for name, (f, ft) in quantities.items():
        parts = [q * wq for q in dens(f, ft)]; d = parts[0] + parts[1] + parts[2]; row = {}; prow = {}
        for reg, sel in REGIONS.items():
            if sel is None:
                mask = {"middle (knot cells)": kind == 0, "inner (r<0.00765)": kind == 1, "outer (r>3413)": kind == 2}[reg]
            else: mask = sel(r)
            row[reg] = float(d[mask].sum()); prow[reg] = [float(q[mask].sum()) for q in parts]
        res["norm2"][name] = row; res["parts_norm2"][name] = prow
        dens_nodes = (parts[0] + parts[1] + parts[2]) / wq                     # integrand D(t) at the nodes
        res["end_densities"][name] = [float(dens_nodes[0]), float(dens_nodes[-1])]
        # tail estimates beyond the truncated range (only meaningful for the first / last piece): inner integrand ~ C e^{2t} (K, rho~: int_{-inf}^{t0} ~ D(t0)/2),
        # outer ~ C e^{-t} (int_{t1}^{inf} ~ D(t1)); for the residual quantities the decay is faster and these overestimate
        res["tail_estimates_norm2"][name] = {"inner (<= D(t_first)/2)": float(dens_nodes[0] / 2), "outer (<= D(t_last))": float(dens_nodes[-1])}
        print("%-22s " % name + "  ".join("%s %.6e" % (k2, v) for k2, v in row.items()), flush=True)
        print("   parts (value, d_t, d_theta) all: %.4e %.4e %.4e;  end densities %.2e / %.2e" % (tuple(prow["all"]) + (dens_nodes[0], dens_nodes[-1])), flush=True)
    res["time"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1); print("saved", out, "(%.0fs)" % res["time"])


def merge(out, pieces):
    """Sum the pieces. Checks: same trial file, same grid parameters (rmin_tot, rmax_tot, n_in, n_out, ncell_total), same weight and method, the
    same set of quantities and regions, parts present in every piece, integer cell ranges tiling [0, ncell_total) AND the physical t ranges
    adjacent (astra/xnorm1 item 4). Different Gauss orders g are allowed and recorded."""
    tot = None; ptot = None; meta = []; base = None
    for p in pieces:
        d = json.load(open(p)); meta.append(dict(file=p, piece=d["piece"], t_range=d["t_range"], g=d["g"]))
        if base is None:
            base = d; tot = {q: {k: 0.0 for k in v} for q, v in d["norm2"].items()}; ptot = {q: {k: [0.0, 0.0, 0.0] for k in v} for q, v in d["parts_norm2"].items()}
        for key in ("trial", "ncell_total", "rmin_tot", "rmax_tot", "n_in", "n_out", "weight", "method"):
            assert d.get(key) == base.get(key), "piece %s differs in %s" % (p, key)
        assert set(d["norm2"]) == set(tot) and all(set(d["norm2"][q]) == set(tot[q]) for q in tot), "quantities/regions differ in " + p
        assert "parts_norm2" in d and set(d["parts_norm2"]) == set(ptot), "parts missing in " + p
        for q, v in d["norm2"].items():
            for k, x in v.items(): tot[q][k] += x
        for q, v in d["parts_norm2"].items():
            for k, x in v.items(): ptot[q][k] = [a1 + b1 for a1, b1 in zip(ptot[q][k], x)]
    # coverage check: integer cell ranges tile [0, ncell_total) and the physical t ranges are adjacent
    meta.sort(key=lambda m: m["piece"][0])
    ok = meta[0]["piece"][0] == 0 and meta[-1]["piece"][1] == base["ncell_total"]
    ok = ok and all(meta[i]["piece"][1] == meta[i + 1]["piece"][0] and abs(meta[i]["t_range"][1] - meta[i + 1]["t_range"][0]) < 1e-12 for i in range(len(meta) - 1))
    res = dict(trial=base["trial"], pieces=meta, coverage_complete=bool(ok), ncell_total=base["ncell_total"], rmin_tot=base["rmin_tot"], rmax_tot=base["rmax_tot"],
               weight=base["weight"], method=base["method"], regions_note=base.get("regions_note"),
               norm2=tot, norm={q: {k: float(np.sqrt(x)) for k, x in v.items()} for q, v in tot.items()}, parts_norm2=ptot)
    if "K = rho~ - X.grad rho~" in res["norm"] and "eps~ - X.grad eps~" in res["norm"]:
        rK = res["norm"]["K = rho~ - X.grad rho~"]["all"]; rF = res["norm"]["eps~ - X.grad eps~"]["all"]
        res["ratio_||K||_X_over_||eps~-X.grad eps~||_X"] = rK / rF
    json.dump(res, open(out, "w"), indent=1)
    print("coverage complete:", ok)
    for q, v in res["norm"].items(): print("%-32s " % q + "  ".join("%s %.6e" % (k, x) for k, x in v.items()))
    if "ratio_||K||_X_over_||eps~-X.grad eps~||_X" in res: print("||K||_X / ||eps~ - X.grad eps~||_X = %.6e" % res["ratio_||K||_X_over_||eps~-X.grad eps~||_X"])
    if res["parts_norm2"]:
        for q, v in res["parts_norm2"].items(): print("   parts norm2 (value, d_t, d_theta) all for %s: %.4e %.4e %.4e" % ((q,) + tuple(v["all"])))
    print("saved", out)


def check(path):
    T = Trial(np.load(path)); G = TrialGreen(T); G.build(); J = TrialJets(G, K=2)
    t = np.array([0.3, 1.5, 2.1517, 2.7, 5.0]); mj = J.modal_jets(t); E = eps_mode_jets(G, mj, 2)
    e0 = G.residual_modes(t); print("order 0 vs residual_modes: max abs diff %.3e (max |eps| %.3e)" % (np.abs(E[0] - e0).max(), np.abs(e0).max()))
    assert np.abs(E[0] - e0).max() < 1e-10
    f = lambda s: G.residual_modes(t + s)
    for h in [3e-4, 1e-4]:
        fd1 = (-f(2 * h) + 8 * f(h) - 8 * f(-h) + f(-2 * h)) / (12 * h)
        fd2 = (-f(2 * h) + 16 * f(h) - 30 * e0 + 16 * f(-h) - f(-2 * h)) / (12 * h * h)
        d1 = np.abs(E[1] - fd1).max(); d2 = np.abs(E[2] - fd2).max()
        print("5-point FD h=%.0e: d_t eps modes: max abs diff jet-FD %.3e (max |d_t eps| %.3e); d_t^2: %.3e (max %.3e)" % (h, d1, np.abs(E[1]).max(), d2, np.abs(E[2]).max()))
        if h == 1e-4: assert d1 < 1e-6 and d2 < 1e-2, "finite-difference check failed"
    nz = np.abs(f(1e-6) - 2 * e0 + f(-1e-6)).max(); print("noise proxy of residual_modes |f(t+h) - 2 f(t) + f(t-h)| at h = 1e-6: %.2e" % nz)
    # manufactured-mode test (astra/xnorm1 item 3): M = 0, c_l = 1/3, R_0 = e^{3t}, psi_1 = e^{4t}  ->  eps = e^{5t} (5 sin th - sin 3 th)
    class Stub: pass
    S = Stub(); S.M = 0; S.n = np.array([1]); S.Nf = 1; S.c_l = 1.0 / 3.0
    tt = np.array([0.0, 0.7]); mjs = dict(t=tt, R=np.stack([3.0 ** i * np.exp(3 * tt)[:, None] for i in range(5)]), PSI=np.stack([4.0 ** i * np.exp(4 * tt)[:, None] for i in range(4)]))
    Es = eps_mode_jets(S, mjs, 2); exact = np.stack([5.0 ** i * np.exp(5 * tt)[:, None] * np.array([5.0, -1.0, 0.0])[None, :] for i in range(3)])
    print("manufactured modes (M = 0, R_0 = e^{3t}, psi_1 = e^{4t}): max abs diff of d_t^i eps_N, i <= 2, from e^{5t} 5^i (5, -1, 0): %.2e" % np.abs(Es - exact).max())
    assert np.abs(Es - exact).max() < 1e-12
    # modal X-density against the (t, theta)-grid route of TrialJets.eps_jets at one radius (angular integral by a fine midpoint rule)
    th = (np.arange(4096) + 0.5) * (np.pi / 2) / 4096; Ej, RHO, PSI = J.eps_jets(t[2:3], th, K=2)
    f = Ej[(0, 0)] - Ej[(1, 0)]; ft = Ej[(1, 0)] - Ej[(2, 0)]; fth = Ej[(0, 1)] - Ej[(1, 1)]
    grid = 4 * ((f ** 2 + ft ** 2 + fth ** 2).sum(1) * (np.pi / 2) / 4096)
    F = E[0][2:3] - E[1][2:3]; Ft = E[1][2:3] - E[2][2:3]; kN = (2 * np.arange(F.shape[1]) + 1.0)[None, :]
    modal = np.pi * ((F ** 2).sum(1) + (Ft ** 2).sum(1) + (kN ** 2 * F ** 2).sum(1))
    print("angular integral of (F^2 + F_t^2 + F_th^2), F = eps - d_t eps, at t = %.4f: grid %.10e  modal %.10e  rel %.2e" % (t[2], grid[0], modal[0], abs(grid[0] - modal[0]) / modal[0]))
    assert abs(grid[0] - modal[0]) / modal[0] < 1e-10
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--merge": merge(a[1], a[2:])
    elif a[0] == "--check": check(a[1])
    else:
        extra = [float(a[5]), float(a[6]), int(a[7]), int(a[8])] if len(a) > 5 else []
        main(a[0], int(a[1]), int(a[2]), int(a[3]), a[4], *extra)
