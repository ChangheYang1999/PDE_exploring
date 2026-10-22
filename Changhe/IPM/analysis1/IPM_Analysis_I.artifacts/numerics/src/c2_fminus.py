"""C2 in the F- form (lead 16:58Z / 17:31Z), floating point, evidence only: paired finite sections of the unnormalized linearization
L h = (V~.grad - 1) h + W[h].grad rho~ on h = x^2 y sum_{m<Mh} b_m(t) cos(2m theta).
Column sets:
  F-   : inner powers e^{2j tau'} (j = 1..7; plus the constant for m = 0, i.e. the J direction), coarse degree-7 B-splines in t
         (every `stride`-th knot of the trial), outer power laws e^{alpha_q (t - t0)} with alpha_q < k - 3 strictly (growth < k),
         plus two scalar columns: KP = d/dk' of the tail  = x^2 y chi(t) t e^{(k-3)(t-t0)} Theta_0~  and
         TAU = x^2 y chi(t) e^{(k-3)(t-t0)} Theta_1, Theta_1 = Theta_0~ cos 2theta (mode coefficients B_m), chi = sum of the last
         `ncut` B-splines of the trial's knot vector (C^6 cutoff, = 1 near t0).
  free : F- plus the pure tails x^2 y chi(t) e^{(k-3)(t-t0)} cos(2m theta) for every m < Mh.
Rows: residual modes N < Mout at collocation radii (21 inner, midpoints of the coarse cells, 40 outer to 1e5 L), weighted by
(1+u)^{1/2}/m(r) (allowed growth k - 1/2); columns weighted by the sup proxy max_t |b| e^{3t}/m x (1 + (2m)^2)^{s/2}, s = 2.
Outputs: sigma_1..sigma_8 of both sections, count below 1e-3 sigma_max, overlaps of the 6 smallest right singular vectors with the
tail columns and with K~, and the LSQ solve of the lead's ell(Phi) test (F- columns): L(chi r^k Phi + g + dk KP + dtau TAU) = 0.
Usage: python3 c2_fminus.py trial.npz Mh stride Mout out.json [ppc=1] [save_raw.npz]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from scipy.interpolate import BSpline
from modal_fit import Trial, NIN, outer_alphas
from trial_green import TrialGreen
from lin_assembly import ExpPolyBasis
from lin_fast import FastAssembler as LinAssembler
P = 7


def coarse_splines(T, stride):
    kn_int = T.knots[P + 1:-(P + 1)][::stride]
    knots = np.r_[np.full(P + 1, T.tmin), kn_int, np.full(P + 1, T.t0)]
    nb = len(knots) - P - 1
    cells = np.unique(np.r_[T.tmin, kn_int, T.t0])
    spl = BSpline(knots, np.eye(nb), P, extrapolate=True)
    tab = np.stack([spl(cells[:-1], nu=nu) / factorial(nu) for nu in range(P + 1)], axis=-1)
    out = []
    for b in range(nb):
        out.append(ExpPolyBasis([(cells[ci], cells[ci + 1], 0.0, tab[ci, b]) for ci in range(len(cells) - 1) if np.any(tab[ci, b])]))
    return out, cells


def cutoff_pieces(T, ncut, alpha, tfactor):
    """Pieces of chi(t) * e^{alpha (t - t0)} * (t if tfactor else 1), chi = sum of the last ncut B-splines of T's knot vector."""
    nk = T.knots; nb = len(nk) - P - 1
    cells = np.unique(nk); cells = cells[(cells >= T.tmin) & (cells <= T.t0)]
    spl = BSpline(nk, np.eye(nb), P, extrapolate=True)
    chi_coef = np.zeros(nb); chi_coef[nb - ncut:] = 1.0
    chi = BSpline(nk, chi_coef, P, extrapolate=True)
    pieces = []
    for ci in range(len(cells) - 1):
        a, b = cells[ci], cells[ci + 1]
        poly = np.array([chi(a, nu=nu) / factorial(nu) for nu in range(P + 1)])
        if not np.any(np.abs(poly) > 1e-14): continue
        if tfactor:   # multiply by (a + sigma)
            poly = np.r_[poly, 0.0] * a + np.r_[0.0, poly]
        pieces.append((a, b, alpha, poly * np.exp(alpha * (a - T.t0))))
    pieces.append((T.t0, np.inf, alpha, [T.t0, 1.0] if tfactor else [1.0]))
    return pieces


def main(trial, Mh, stride, Mout, out, ppc=1, save_npz=None):
    T = Trial(np.load(trial)); G = TrialGreen(T); G.build(); k = T.k; L = T.L
    splines, cells = coarse_splines(T, stride); alphas = outer_alphas(k)
    mid = np.concatenate([np.linspace(a, b, ppc + 2)[1:-1] for a, b in zip(cells[:-1], cells[1:])])
    kn_fine = T.knots[P + 1:-(P + 1)]                                            # the trial's interior knots
    cut_mid = 0.5 * (kn_fine[-10:] + np.r_[kn_fine[-9:], T.t0])                   # midpoints of the last 10 trial knot intervals (the cutoff transition)
    t_eval = np.unique(np.r_[T.tmin - np.linspace(0.0, 3.0, 21), mid, cut_mid, T.t0 + np.linspace(0.05, np.log(1e5 * L / T.R0), 40)])
    Ne = len(t_eval); r = np.exp(t_eval); u = r / L; mr = u ** 3 * (1 + u ** 2) ** ((k - 3) / 2); e3 = np.exp(3 * t_eval)
    LA = LinAssembler(G, t_eval, Mout)
    cols = []; labels = []; kinds = []
    for m in range(Mh):
        if m == 0: cols.append((0, ExpPolyBasis([(-np.inf, T.tmin, 0.0, [1.0]), (T.tmin, T.t0, 0.0, [1.0])]), "J")); kinds.append("J")
        for j in range(1, NIN + 1): cols.append((m, ExpPolyBasis([(-np.inf, T.tmin, 2.0 * j, [1.0])]), "in%d" % j)); kinds.append("in")
        for b, sp in enumerate(splines): cols.append((m, sp, "sp%d" % b)); kinds.append("sp")
        for q, al in enumerate(alphas):
            if q == 0: continue
            cols.append((m, ExpPolyBasis([(T.t0, np.inf, float(al), [1.0])]), "out%d" % q)); kinds.append("out")
    nF = len(cols)
    print("F- function columns: %d (%d radial per mode); rows %d x %d = %d" % (nF, nF // Mh, Ne, Mout, Ne * Mout), flush=True)
    t0 = time.time(); Mat, cvec = LA.assemble(cols, verbose=500); print("assembly %.0fs" % (time.time() - t0), flush=True)
    # scalar columns KP, TAU (sums over all trial modes of the tail profile) and the free-tail columns per mode
    A0 = T.Aout[:, 0]; Mt = T.M
    Bm = np.zeros(Mt + 1); Bm[0] = A0[1] / 2; Bm[1] = A0[0] + A0[2] / 2
    for j in range(2, Mt): Bm[j] = (A0[j - 1] + A0[j + 1]) / 2 if j + 1 < Mt else A0[j - 1] / 2
    ncut = 10
    kp_pieces = cutoff_pieces(T, ncut, k - 3, True); tau_pieces = cutoff_pieces(T, ncut, k - 3, False)
    KP = np.zeros(Ne * Mout); TAU = np.zeros(Ne * Mout); cKP = 0.0; cTAU = 0.0; t0 = time.time()
    for m in range(Mt):
        if A0[m] != 0.0:
            o, c = LA.column(m, ExpPolyBasis(kp_pieces)); KP += A0[m] * o.ravel(); cKP += A0[m] * c
        if Bm[m] != 0.0:
            o, c = LA.column(m, ExpPolyBasis(tau_pieces)); TAU += Bm[m] * o.ravel(); cTAU += Bm[m] * c
    tails = []; ctails = []
    for m in range(Mh):
        o, c = LA.column(m, ExpPolyBasis(tau_pieces)); tails.append(o.ravel()); ctails.append(c)
    print("scalar and tail columns %.0fs" % (time.time() - t0), flush=True)
    if save_npz:   # raw assembled data for the Gram-orthonormalized post-processing (src/c2_gram.py); the pieces of every column are pickled alongside
        import pickle
        np.savez(save_npz, Mat=Mat, KP=KP, TAU=TAU, tails=np.column_stack(tails), cvec=cvec, cKP=cKP, cTAU=cTAU, ctails=np.array(ctails),
                 t_eval=t_eval, col_m=np.array([m for (m, b, lab) in cols]), col_kind=np.array(kinds), col_label=np.array([lab for (m, b, lab) in cols]),
                 A0=A0, Bm=Bm, Mh=Mh, Mout=Mout, Ne=Ne, stride=stride, ppc=ppc, k=k, L=L, tmin=T.tmin, t0=T.t0, ncut=ncut)
        pickle.dump(dict(cols=[(m, b.pieces, lab) for (m, b, lab) in cols], kp_pieces=kp_pieces, tau_pieces=tau_pieces, cells=cells),
                    open(save_npz.replace(".npz", "_cols.pkl"), "wb"))
        print("saved raw matrices to", save_npz, flush=True)
    # weights
    roww = np.repeat((1 + u) ** 0.5 / mr, Mout)
    def colweight(m, basis):
        bval = basis.eval(t_eval, 0); return max(np.max(np.abs(bval) * e3 / mr), 1e-300) * (1 + (2 * m) ** 2)
    cw = np.array([colweight(m, b) for (m, b, lab) in cols])
    cw_KP = max(np.max(np.abs(ExpPolyBasis(kp_pieces).eval(t_eval)) * np.abs(A0).sum() * e3 / mr), 1e-300)
    cw_TAU = max(np.max(np.abs(ExpPolyBasis(tau_pieces).eval(t_eval)) * np.abs(Bm).sum() * e3 / mr), 1e-300)
    cw_tail = [max(np.max(np.abs(ExpPolyBasis(tau_pieces).eval(t_eval)) * e3 / mr), 1e-300) * (1 + (2 * m) ** 2) for m in range(Mh)]
    MF = np.column_stack([Mat / cw[None, :], KP / cw_KP, TAU / cw_TAU]) * roww[:, None]
    Mfree = np.column_stack([MF, np.column_stack(tails) / np.array(cw_tail)[None, :] * roww[:, None]])
    res = dict(trial=trial, Mh=Mh, stride=stride, Mout=Mout, ppc=ppc, Ne=Ne, ncolF=MF.shape[1], ncolfree=Mfree.shape[1], ncut=ncut,
               row_weight="(1+u)^0.5/m", col_weight="max|b|e^{3t}/m * (1+(2m)^2)")
    for name, Mw in [("Fminus", MF), ("free", Mfree)]:
        t0 = time.time(); U_, S_, Vt = np.linalg.svd(Mw, full_matrices=False)
        res[name] = dict(sigma_max=float(S_[0]), sigma_small8=[float(x) for x in S_[-8:][::-1]], n_below_1em3=int((S_ < 1e-3 * S_[0]).sum()),
                         n_below_1em6=int((S_ < 1e-6 * S_[0]).sum()), svd_time=time.time() - t0)
        if name == "free":
            ntail = Mh; tail_idx = np.arange(Mw.shape[1] - ntail, Mw.shape[1])
            res[name]["tail_mass_of_6_smallest"] = [float(np.linalg.norm(Vt[-1 - i][tail_idx]) ** 2) for i in range(6)]
            res[name]["KP_TAU_mass_of_6_smallest"] = [float(Vt[-1 - i][nF] ** 2 + Vt[-1 - i][nF + 1] ** 2) for i in range(6)]
        else:
            res[name]["KP_TAU_mass_of_6_smallest"] = [float(Vt[-1 - i][nF] ** 2 + Vt[-1 - i][nF + 1] ** 2) for i in range(6)]
        labels_all = [lab + "_m%d" % m for (m, b, lab) in cols] + ["KP", "TAU"] + (["tail_m%d" % m for m in range(Mh)] if name == "free" else [])
        jidx = [i for i, (m, b, lab) in enumerate(cols) if lab == "J"]
        res[name]["J_mass_of_6_smallest"] = [float(Vt[-1 - i][jidx[0]] ** 2) for i in range(6)]
        res[name]["spline_m0_mass_of_6_smallest"] = [float(np.sum(Vt[-1 - i][[ic for ic, (m, b, lab) in enumerate(cols) if m == 0 and lab.startswith("sp")]] ** 2)) for i in range(6)]
        if name == "Fminus":
            keep = [i for i in range(Mw.shape[1]) if i not in jidx]
            S2 = np.linalg.svd(Mw[:, keep], compute_uv=False)
            res["Fminus_noJ"] = dict(sigma_max=float(S2[0]), sigma_small8=[float(x) for x in S2[-8:][::-1]], n_below_1em6=int((S2 < 1e-6 * S2[0]).sum()))
            print("Fminus_noJ", json.dumps(res["Fminus_noJ"]), flush=True)
        for i in range(3):
            v = Vt[-1 - i]; top = np.argsort(-np.abs(v))[:8]
            res[name]["smallest_vec_%d_top" % i] = [(labels_all[j], float(v[j])) for j in top]
        # kind decomposition of every near-null right singular vector (sigma < 1e-6 sigma_max)
        kind_of = [k for k in kinds] + ["KP", "TAU"] + (["tail"] * Mh if name == "free" else [])
        kind_of = np.array(kind_of); small_idx = np.where(S_ < 1e-6 * S_[0])[0]
        summary = {}
        for i in small_idx:
            v = Vt[i]; masses = {kd: float(np.sum(v[kind_of == kd] ** 2)) for kd in ["J", "in", "sp", "out", "KP", "TAU", "tail"]}
            dom = max(masses, key=masses.get); summary[dom] = summary.get(dom, 0) + 1
        res[name]["near_null_count_by_dominant_kind"] = summary
        # mass distribution of the near-null vectors over mode m and over the radial position of the spline supports
        col_m = np.array([m for (m, b, lab) in cols] + [-1, -1] + ([m for m in range(Mh)] if name == "free" else []))
        col_t = np.array([(0.5 * (b.pieces[0][0] + b.pieces[-1][1]) if (lab.startswith("sp")) else np.nan) for (m, b, lab) in cols] + [np.nan] * (2 + (Mh if name == "free" else 0)))
        mass_m = np.zeros(Mh); tb_edges = np.linspace(T.tmin, T.t0, 11); mass_t = np.zeros(10)
        for i in small_idx:
            v2 = Vt[i] ** 2
            for m in range(Mh): mass_m[m] += v2[col_m == m].sum()
            for kdx in range(10):
                sel = (col_t >= tb_edges[kdx]) & (col_t < tb_edges[kdx + 1]); mass_t[kdx] += v2[sel].sum()
        res[name]["near_null_mass_by_mode"] = [float(x) for x in mass_m]
        res[name]["near_null_mass_by_t_decile_of_[tmin,t0]"] = [float(x) for x in mass_t]
        if name == "free":
            res[name]["tail_dominant_sigmas"] = [float(S_[i]) for i in small_idx if np.sum(Vt[i][kind_of == "tail"] ** 2) > 0.5]
            res[name]["tail_mass_all_small"] = [float(np.sum(Vt[i][kind_of == "tail"] ** 2)) for i in small_idx]
        print(name, json.dumps(res[name]), flush=True)
    # ell(Phi) test: for tail increments Phi (per-mode tails m = 0..3 and Theta_0~ itself restricted to Mh modes), solve the F- LSQ
    ell = {}
    for lab, coefs in [("Theta0", A0[:Mh]), ("cos0", np.eye(Mh)[0]), ("cos2", np.eye(Mh)[1]), ("cos4", np.eye(Mh)[2]), ("cos6", np.eye(Mh)[3])]:
        rhs = -sum(coefs[m] * tails[m] for m in range(Mh)) * roww
        sol, resid, rk, sv = np.linalg.lstsq(MF, rhs, rcond=1e-6)
        dk = sol[nF] / cw_KP; dtau = sol[nF + 1] / cw_TAU
        ell[lab] = dict(dk=float(dk), dtau=float(dtau), rel_residual=float(np.linalg.norm(MF @ sol - rhs) / max(np.linalg.norm(rhs), 1e-300)))
        print("ell test %s: dk = %.4e, dtau = %.4e, relative LSQ residual %.2e" % (lab, dk, dtau, ell[lab]["rel_residual"]), flush=True)
    res["ell"] = ell
    json.dump(res, open(out, "w"), indent=1); print("saved", out)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], int(a[2]), int(a[3]), int(a[4]), a[5], int(a[6]) if len(a) > 6 else 1, a[7] if len(a) > 7 else None)
