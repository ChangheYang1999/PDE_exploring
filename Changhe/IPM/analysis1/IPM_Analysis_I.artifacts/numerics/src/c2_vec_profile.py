"""Where do the smallest singular directions of a C2 Gram section live?  Post-hoc profile of the saved singular vectors of src/c2_gram2.py
(out_vec.npz, extended coefficients incl. KP/TAU/tails/J_inner/references) from the column pieces (_cols.pkl): the X-energy density of
h = x^2 y sum_c h_c f_c(t) a_c(theta) in t = log r, e(t) = L^6 e^{2t} (1+u^2)^{3/2-k} sum_{m,m'} [AA0 (f f' + (3f+f')(3f'+f'')) + AA1 f f']_{m m'}
(the H1m integrand of c2_gram.py integrated over theta), reported as the fraction of the X-energy per dyadic shell of r, the radius of the energy
median, and the per-mode energy fractions.  Floating, evidence only.
Usage: python3 src/c2_vec_profile.py runs/c2/c2gram2_<tag>_H1m_NJ0_vec.npz runs/c2/c2raw_<tag>_cols.pkl [section=Fminus] [nvec=3]"""
import os, sys, json, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lin_assembly import ExpPolyBasis
from c2_gram import angular_matrices_H1, radial_nodes
from c2_gram2 import step_pieces


def _popen(path):
    """Open a pickled column-piece file for reading; falls back to path + '.gz' (the artifacts folder stores the _cols.pkl pieces gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rb")
    return open(path, "rb")


def main(vec, pkl, section="Fminus", nvec=3):
    v = np.load(vec, allow_pickle=True); meta = pickle.load(_popen(pkl)); cols = meta["cols"]
    k = float(v["k"]); L = float(v["L"]); tmin = float(v["tmin"]); t00 = float(v["t0"]); Mh = int(v["Mh"]); nF = int(v["nF"]); ntot = int(v["ntot"]); next_ = int(v["next"])
    H = v[section + "_h"]; sig = v[section + "_sigma"]; hGh = v[section + "_hGh"]
    refs = [(str(n), ta, tb) for n, (ta, tb) in zip(v["ref_names"], v["ref_ta_tb"])]
    kp_pieces = meta["kp_pieces"]; tau_pieces = meta["tau_pieces"]
    # radial pieces and angular coefficient vectors of the extended basis (same construction as c2_gram2.main)
    Mang = max(int(m) for (m, p, lab) in cols) + 3
    Mang = max(Mang, Mh + 2)
    rad = [p for (m, p, lab) in cols] + [kp_pieces, tau_pieces, [(-np.inf, tmin, 0.0, [1.0])]] + [step_pieces(ta, tb) for (n, ta, tb) in refs]
    rad_of = list(range(nF)) + [nF, nF + 1] + [nF + 1] * Mh + [nF + 2] + [nF + 3 + i for i in range(len(refs))]
    # angular coefficients: function columns single mode; KP (Theta0 modes) and TAU (Theta1 modes) need A0/Bm: not saved -> approximate KP/TAU by their
    # m-vectors from the raw if present; here we only need them if the vector has KP/TAU content (it has ~1e-9): set to mode 0 and report their weight.
    acoef = np.zeros((len(rad_of), Mang))
    for i, (m, p, lab) in enumerate(cols): acoef[i, int(m)] = 1.0
    if "A0" in v.files:                      # exact angular coefficient vectors of KP (Theta_0~ modes) and TAU (Theta_1 modes)
        A0 = v["A0"]; Bm = v["Bm"]; Mt = len(A0)
        for m in range(min(Mt, Mang)): acoef[nF, m] = A0[m]
        for m in range(min(len(Bm), Mang)): acoef[nF + 1, m] = Bm[m]
    else:                                     # not saved: drop KP/TAU from the profile (their cos^2 shares are ~1e-9) and say so
        out_note = "KP/TAU dropped (A0/Bm not in the vec file)"; h_mask_kp = True
    for j in range(Mh): acoef[nF + 2 + j, j] = 1.0
    acoef[ntot, 0] = 1.0
    for i in range(len(refs)): acoef[ntot + 1 + i, 0] = 1.0
    A0h, A1h = angular_matrices_H1(Mang)
    # projection of the Phi_m family onto the sine harmonics: T[m, N] = (1/pi) int_0^{2pi} Phi_m sin((2N+1) theta) dtheta (equispaced quadrature, exact)
    Ng = 8192; th = 2 * np.pi * np.arange(Ng) / Ng; Nh = Mang + 3
    Phi = (np.cos(th) ** 2 * np.sin(th))[None, :] * np.cos(2 * np.arange(Mang)[:, None] * th[None, :])
    S = np.sin((2 * np.arange(Nh)[:, None] + 1) * th[None, :])
    T_harm = (Phi @ S.T) * (2 * np.pi / Ng) / np.pi
    ends = set(np.linspace(tmin - 25.0, tmin, 51).tolist() + np.linspace(t00, t00 + 45.0, 91).tolist())
    for pcs in rad:
        for (a, b, al, c) in pcs:
            if np.isfinite(a): ends.add(float(a))
            if np.isfinite(b): ends.add(float(b))
    bps = np.array(sorted(ends)); tq, wq = radial_nodes(bps, 12)
    F = np.array([ExpPolyBasis(pc).eval(tq) for pc in rad]); Fd = np.array([ExpPolyBasis(pc).eval(tq, 1) for pc in rad])
    uq = np.exp(tq) / L; wX = L ** 6 * np.exp(2 * tq) * (1 + uq ** 2) ** (3 - k - 1.5)
    out = dict(vec=vec, section=section, shells=[], note="X-energy density of the smallest singular directions in t = log r (H1m integrand integrated over theta); fractions per dyadic shell; X-energy fractions per band of odd sine harmonics N (angular frequency 2N+1)")
    edges = [0.0] + [2.0 ** j for j in range(-8, 13)] + [np.inf]
    for iv in range(min(nvec, H.shape[1])):
        h = H[:, iv].copy()
        if "A0" not in v.files: h[nF] = 0.0; h[nF + 1] = 0.0
        # field modes: B_m(t) = sum_c h_c f_c(t) acoef[c, m]  (radial coefficient of Phi_m)
        Bm = (acoef.T * h[None, :]) @ F[rad_of]          # (Mang, nq)
        Bmd = (acoef.T * h[None, :]) @ Fd[rad_of]
        Bs = 3 * Bm + Bmd
        dens = np.einsum("mq,mn,nq->q", Bm, A0h, Bm) + np.einsum("mq,mn,nq->q", Bs, A0h, Bs) + np.einsum("mq,mn,nq->q", Bm, A1h, Bm)
        dens = dens * wX
        E = float((dens * wq).sum()); r = np.exp(tq)
        fr = []
        for a, b in zip(edges[:-1], edges[1:]):
            sel = (r >= a) & (r < b); fr.append(float((dens[sel] * wq[sel]).sum() / E))
        cum = np.cumsum(dens * wq) / E; rmed = float(np.exp(tq[np.searchsorted(cum, 0.5)]))
        r10 = float(np.exp(tq[np.searchsorted(cum, 0.1)])); r90 = float(np.exp(tq[np.searchsorted(cum, 0.9)]))
        # angular content in ORTHOGONAL sine harmonics sin((2N+1) theta) (astra gram4: the Phi_m = cos^2 sin cos 2m theta family is not orthogonal, so
        # truncation energies of that family can exceed one): C_N(t) = sum_m T[m, N] B_m(t); X-energy per harmonic E_N = pi int wX [C_N^2 + (3C_N + C_N')^2
        # + (2N+1)^2 C_N^2] dt; sum_N E_N = E (checked); fractions per band of N
        C = T_harm.T @ Bm; Cs = T_harm.T @ Bs; Nh = C.shape[0]; kN = (2 * np.arange(Nh) + 1.0)
        EN = np.pi * ((C ** 2 + Cs ** 2 + (kN ** 2)[:, None] * C ** 2) * (wX * wq)[None, :]).sum(1)
        em = {"harmonics_sum_check": float(EN.sum() / E)}
        for lo, hi in ((0, 1), (2, 3), (4, 7), (8, 15)):
            if lo < Nh: em["N=%d..%d" % (lo, min(hi, Nh - 1))] = float(EN[lo:hi + 1].sum() / E)
        em["N>=16"] = float(EN[16:].sum() / E)
        # share of the coefficient mass by kind
        kinds = {}
        for kd in ("in", "sp", "out", "J"):
            idx = [i for i, (m, p, lab) in enumerate(cols) if (lab == "J" if kd == "J" else (lab.startswith(kd) and lab != "J"))]
            kinds[kd] = float(np.sum(h[idx] ** 2)) if idx else 0.0
        kinds["KP_TAU"] = float(h[nF] ** 2 + h[nF + 1] ** 2); kinds["tails"] = float(np.sum(h[nF + 2:ntot] ** 2)); kinds["Jinner_refs"] = float(np.sum(h[ntot:] ** 2))
        row = dict(sigma=float(sig[iv]), E_X=E, hGh_saved=float(hGh[iv]), r_median=rmed, r_10=r10, r_90=r90,
                   shell_fractions={"[%g,%g)" % (a, b): f for (a, b), f in zip(zip(edges[:-1], edges[1:]), fr) if f > 1e-4},
                   harmonic_energy_fractions=em, coefficient_mass_by_kind=kinds)
        out["shells"].append(row)
        print("sigma %.4e: E_X %.4e (saved hGh %.4e); energy median r = %.4g (10%% %.4g, 90%% %.4g); shells %s; modes %s" % (
            row["sigma"], E, hGh[iv], rmed, r10, r90, {kk: round(f, 3) for kk, f in row["shell_fractions"].items() if f > 0.01}, {kk: round(f, 3) for kk, f in em.items()}), flush=True)
    jo = vec.replace("_vec.npz", "_profile_%s.json" % section); json.dump(out, open(jo, "w"), indent=1); print("saved", jo)


if __name__ == "__main__":
    a = sys.argv; main(a[1], a[2], a[3] if len(a) > 3 else "Fminus", int(a[4]) if len(a) > 4 else 3)
