"""FLOATING estimate of eta = ||F(rho~)||_Y, Y = E G (+) L^2(w_a) (lead S2_CLOSURE.md 3.5(d), notes 18/19), and of ||F(rho~)||_{L^2(e^{mu~})}.
F(rho~) = (c_l X + U[rho~]).grad rho~ - rho~ = x^2 y B(r, theta); its factor modes epshat_N = e^{-3t} F_N are the exact ExpPolys of
Operator.residual_modes (ball arithmetic), truncated at N <= NMAX. At every quadrature node (fsec prep nodes): mode vector G ->
jet gamma = -(1/2) sum (-1)^N (2N+1)^2 G_N (= B(r, pi/2)), remainder R = G - gamma x^2y-modes, quotient Q = R/(cos^4) (least squares),
energies  gamma^2 g_G(t)  and  e^{8t + mu_a(t)} Q^T A Q  (A = angular Gram against |cos|^{-1/2}); also pi sum_N G_N^2 e^{8t + mu~(t)} for the
L^2(e^{mu~}) norm (lead note 5 weight, margin.py MU_KNOTS/MU_VALS). Radial split r < 1, 1 <= r <= 100, r > 100. Diagnostics: axis residual
energy (sum (-1)^N G_N)^2, division residual energy, top-3-mode energy fraction, all relative to the mode energy.
Usage: python3 eta.py <tag> nworkers [prec=256] [NMAX=60]
"""
import sys, os, time, json, pickle, math
import numpy as np
import multiprocessing as mp
from flint import arb, fmpq, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_trial import ExactTrial, ExpPoly, q2arb
from opimage import Cells, Background, Operator
from run_section import HERE
from margin import MU_KNOTS, MU_VALS
import fsec_ang as ang
from fsec import mu_a, gG, ep_eval

def mu_tilde(t):
    """piecewise linear mu~ with mu~(0) = 0 (lead note 5): slopes MU_VALS on the intervals between MU_KNOTS"""
    knots = [float(k) for k in MU_KNOTS]; vals = [float(v) for v in MU_VALS]
    def slope(x):
        for i, k in enumerate(knots):
            if x < k: return vals[i]
        return vals[-1]
    # integrate slope from 0 to t
    if t == 0: return 0.0
    pts = sorted(set([0.0, t] + [k for k in knots if min(0.0, t) < k < max(0.0, t)]))
    s = 0.0
    for a, b in zip(pts[:-1], pts[1:]): s += slope((a + b) / 2) * (b - a)
    return s if t > 0 else -s

def worker(args):
    wid, cell_idx = args
    ctx.prec = PREC
    nm = NMAX + 1
    E = dict(G=np.zeros(3), R=np.zeros(3), Lmu=np.zeros(3), E_img=0.0, E_axis=0.0, E_div=0.0, E_top3=0.0, cells=0, max_gamma=0.0, max_gamma_t=None)
    t0 = time.time()
    for cnt, ic in enumerate(cell_idx):
        s_nodes, t_nodes, w_nodes = NODES[ic]
        eps = OP.residual_modes(ic, Nmax=NMAX)
        for a, s in enumerate(s_nodes):
            t = t_nodes[a]; w = w_nodes[a]; reg = 0 if t < 0 else (1 if t <= math.log(100.0) else 2)
            G = np.zeros(nm)
            for N, ep in eps.items():
                if N < nm and ep.terms: G[N] = ep_eval(ep, s)
            gam, R, a0 = ang.jet_split(G); Q, res = DIV(R)
            wR = math.exp(8 * t + mu_a(t)); wG = gG(t); wmu = math.exp(8 * t + mu_tilde(t))
            E["G"][reg] += w * wG * gam * gam
            E["R"][reg] += w * wR * float(Q @ AH @ Q)
            E["Lmu"][reg] += w * wmu * math.pi * float(np.sum(G * G))
            tot = float(np.sum(G * G)); E["E_img"] += w * wR * tot; E["E_axis"] += w * wR * a0 * a0; E["E_div"] += w * wR * res * res; E["E_top3"] += w * wR * float(np.sum(G[-3:] ** 2))
            if abs(gam) > E["max_gamma"]: E["max_gamma"] = abs(gam); E["max_gamma_t"] = t
        E["cells"] += 1
        if cnt % 50 == 0:
            with open(os.path.join(OUT, "progress_%d.txt" % wid), "w") as f: f.write("%d/%d cells, %.0fs\n" % (cnt + 1, len(cell_idx), time.time() - t0))
    E["G"] = E["G"].tolist(); E["R"] = E["R"].tolist(); E["Lmu"] = E["Lmu"].tolist()
    return E

if __name__ == "__main__":
    a = sys.argv; tag = a[1]; nw = int(a[2]); PREC = int(a[3]) if len(a) > 3 else 256; NMAX = int(a[4]) if len(a) > 4 else 60
    OUT = os.path.join(HERE, "runs", tag); os.makedirs(OUT, exist_ok=True)
    ctx.prec = PREC; T0 = time.time()
    T = ExactTrial(prec=PREC); T.build_green(verbose=False)
    CELLS = Cells(T, inner_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4)], outer_extra=[fmpq(1, 2), fmpq(1), fmpq(2), fmpq(4), fmpq(8)])
    bg = Background(T, CELLS, nmax=None)
    OP = Operator(T, CELLS, bg, Nmax=NMAX)
    NODES = pickle.load(open(os.path.join(HERE, "runs", "fsec_prep_L40_ng3_8_16.pkl"), "rb"))[0]
    nm = NMAX + 1; AH = ang.A_half(nm - 2); M4, DIV = ang.div_cos4(nm)
    idx = list(range(CELLS.n)); chunks = [idx[w::nw] for w in range(nw)]
    print("eta: %d cells over %d workers, NMAX %d, prec %d (build %.0fs)" % (CELLS.n, nw, NMAX, PREC, time.time() - T0), flush=True)
    mp.set_start_method("fork")
    tot = None
    with mp.Pool(nw) as pool:
        for E in pool.imap_unordered(worker, [(w, chunks[w]) for w in range(nw)]):
            if tot is None: tot = E
            else:
                for k in ("G", "R", "Lmu"): tot[k] = [x + y for x, y in zip(tot[k], E[k])]
                for k in ("E_img", "E_axis", "E_div", "E_top3", "cells"): tot[k] += E[k]
                if E["max_gamma"] > tot["max_gamma"]: tot["max_gamma"] = E["max_gamma"]; tot["max_gamma_t"] = E["max_gamma_t"]
            print("  worker done; cells so far %d (%.0fs)" % (tot["cells"], time.time() - T0), flush=True)
    eta_G = math.sqrt(sum(tot["G"])); eta_R = math.sqrt(sum(tot["R"])); eta = math.sqrt(eta_G ** 2 + eta_R ** 2); eta_mu = math.sqrt(sum(tot["Lmu"]))
    res = dict(tag=tag, NMAX=NMAX, prec=PREC, cells=tot["cells"], eta_Y=eta, eta_G_axis_part=eta_G, eta_R_remainder_part=eta_R, eta_L2_mu_tilde=eta_mu,
               split_regions=["r < 1", "1 <= r <= 100", "r > 100"], G_energy_by_region=tot["G"], R_energy_by_region=tot["R"], L2mu_energy_by_region=tot["Lmu"],
               diag=dict(axis_residual_energy_fraction=tot["E_axis"] / (tot["E_img"] + 1e-300), division_residual_energy_fraction=tot["E_div"] / (tot["E_img"] + 1e-300),
                         top3_mode_energy_fraction=tot["E_top3"] / (tot["E_img"] + 1e-300), max_abs_gamma=tot["max_gamma"], at_t=tot["max_gamma_t"]),
               definitions="F = (c_l X + U[rho~]).grad rho~ - rho~ (exact modes, truncated N <= NMAX); gamma = axis coefficient of F/(x^2 y); Y norm per S2_L2_THEORY 5.2 (a = 17/4, mu_a' = -17/2 / -5/4; G weights e^{-t/2}, e^{27t/4}); L^2(e^{mu~}) with the note-5 weight; Gauss nodes of fsec prep (3 per spline cell, 8 per sub-cell, 16 per half-line stretch of length 40)",
               status="FLOATING (numerical estimate, not a certificate)", seconds=time.time() - T0)
    json.dump(res, open(os.path.join(OUT, "eta.json"), "w"), indent=1); print(json.dumps(res, indent=1))
