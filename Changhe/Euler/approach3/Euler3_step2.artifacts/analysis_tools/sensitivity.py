"""Reduced parameter sensitivity and stationarity measures of SPEC sections 7.2 and 7.3, computed from a
linearization record (QR factor of the scaled Jacobian with the two parameter columns last).

Version 2 (2026-10-28, after the verifier's source review at 21:01Z): the coefficient projector P_a is built from the
SVD of the coefficient block with the declared cutoff (rank deficient J_a allowed), the phase generator is projected
out of the coefficient block as SPEC 7.3 requires, S is inverted only by pseudo-inverse with cutoff 1e-12 relative to
its largest eigenvalue (correlation undefined and state "parameter-singular" above condition 1e12), and widths are
given both from the current point (two-sided, with the reduced gradient) and about the reduced-model minimizer.
Version 1 is kept read only as sensitivity_v1.py.

Version 3 (2026-10-28, after the verifier's V022 at 21:18Z): a directional gradient below roundoff along a zero-curvature
eigenvector gives unbounded widths (no spurious finite root); a zero phase vector is treated as absent and recorded;
zero parameter columns give undefined (null) cosines and scaled gradients instead of NaN; eigenpairs of S in physical
(c_l, omega) and in (c_l, log omega) coordinates are reported; non-finite numbers are written as explicit strings
("unbounded+", "unbounded-", "undefined"), so the JSON output is standard. Version 2 is kept as sensitivity_v2.py.

Version 4 (2026-10-28, after the verifier's V023 at 21:22Z): load_record() reads the numerics worker's record format
(Qtr, r_norm2, generator_red with parameter slots, params as a JSON string with the chain factors) as well as the format
below, and converts parameter columns given in optimizer coordinates (z_c, z_w) to physical units by
D_phys,p = D_z,p / (dc_l/dz_c, domega/dz_w), which leaves R and Q^T r unchanged. The Jacobian kind (complete J_c or
frozen-weight J_f) is carried into the output; only a J_c record supports SPEC 7 claims. analyse() is unchanged from
version 3 (kept as sensitivity_v3.py).

Version 5 (2026-10-28, after the verifier's note at 21:45Z): the Jacobian kind is read from an explicit record key
"jacobian_kind" if present, otherwise from whole-word tokens J_c, J_cw, J_f in the label (version 4 used substring
matching and read the worker's "J_cw" label as J_c). J_cw (weights differentiated, closure target lagged) and J_f are
partial models; only J_c supports SPEC 7 claims. A label naming more than one kind is "ambiguous". A record with
z_opt but without chain factors and without a coordinate declaration is rejected (verifier V036). analyse() is
unchanged apart from the version number and one step: R is renormalized to unit columns (D adjusted, J = Q R D
unchanged), so the analysis uses the SPEC 7.1 scaling even if a record's D is not the column-norm scaling (version 4
kept as sensitivity_v4.py).

Version 6 (2026-10-29, after the verifier's V398 at 17:54Z): the field d_log_omega of about_model_minimizer_halfwidth is
log1p(d_omega/omega) at the CURRENT omega, so it is a current-centre conversion and not a width about the model
minimizer. It is kept unchanged for comparison with earlier outputs, and three fields are added: model_minimizer_omega
(omega plus the omega component of the reduced Gauss-Newton step) and d_log_omega_about_minimizer_plus / _minus,
log1p(+/- d_omega/omega_min). Physical widths, roots and every other output are unchanged (version 5 kept as
sensitivity_v5.py).

Input npz keys (numerics lane, NOTES_FOR_TEAM 2026-10-28T20:43Z item 3):
  R      (n, n) upper-triangular factor of J_s = J diag(1/D), columns [a_1..a_N, c_l, omega] (parameters last)
  qtr    (n,)   Q^T r
  rr     ()     ||r||^2 (so O1 = rr / 2)
  D      (n,)   column scaling (J_s = J / D, x_s = D x)
  phase  (n-2,) optional: azimuthal phase-rotation generator in reduced coefficient coordinates (unscaled)
  params (2,)   optional: (c_l, omega) at the state, for widths in log omega
Parameter columns are in physical (c_l, omega) units.
"""
import json
import re
import sys

import numpy as np

TRUNC = (0.0, 1e-10, 1e-8, 1e-6)
CUTOFF = 1e-12          # SPEC 7.0: declared pseudo-inverse cutoff, relative


def _reduced(Raa, Rap, Rpp, qa, qp, t, v=None):
    """Projected parameter block of SPEC 7.3 in Q coordinates. P_a = projector onto range(J_a restricted to the
    complement of the scaled phase direction v), using singular values above max(t, CUTOFF) sigma_max."""
    A = Raa if v is None else Raa - np.outer(Raa @ v, v)
    Ua, sa, _ = np.linalg.svd(A)
    keep = sa > max(t, CUTOFF) * sa[0]
    Ut = Ua[:, keep]
    Ra = Rap - Ut @ (Ut.T @ Rap)
    qr_ = qa - Ut @ (Ut.T @ qa)
    Res = np.vstack([Ra, Rpp])                 # (I - P_a) J_p in Q coordinates
    qres = np.concatenate([qr_, qp])           # (I - P_a) r restricted to range(Q)
    return Res, qres, int(keep.sum()), sa


def _pinv_sym(S):
    lam, W = np.linalg.eigh(S)
    lmax = max(lam[-1], 0.0)
    ok = lam > CUTOFF * lmax if lmax > 0 else np.zeros_like(lam, bool)
    Sp = (W[:, ok] / lam[ok]) @ W[:, ok].T
    cond = float(lam[-1] / lam[0]) if lam[0] > 0 else float("inf")
    return Sp, lam, W, ok, cond


def _widths(lam, W, g, rr, D_p, params, ok, omega_min=None):
    """Displacements along the eigenvectors of S where the reduced model rises by f O1 (f = 1 %, 10 %)."""
    O1 = 0.5 * rr
    gtol = 1e-12 * (np.linalg.norm(g) + np.sqrt(max(lam[-1], 0.0) * rr))   # directional gradient at roundoff level
    out = {}
    for f in (0.01, 0.1):
        rows = []
        for k in range(2):
            w = W[:, k]; b = float(g @ w); a = float(lam[k]) if ok[k] else 0.0
            # model change along t w: b t + (1/2) a t^2 = f O1
            if a > 0:
                disc = np.sqrt(b * b + 2.0 * a * f * O1)
                t_plus, t_minus = (-b + disc) / a, (-b - disc) / a
                t_curv = np.sqrt(2.0 * f * O1 / a)
            else:
                t_curv = float("inf")
                if abs(b) <= gtol:
                    t_plus, t_minus = float("inf"), -float("inf")
                elif b > 0:
                    t_plus, t_minus = f * O1 / b, -float("inf")
                else:
                    t_plus, t_minus = float("inf"), f * O1 / b
            def phys(t):
                if not np.isfinite(t):
                    sg = np.sign(t) * np.sign(w / D_p)
                    rec = {"d_c_l": float(sg[0] * np.inf) if w[0] != 0 else 0.0, "d_omega": float(sg[1] * np.inf) if w[1] != 0 else 0.0}
                    if params is not None:
                        rec["d_log_omega"] = rec["d_omega"]
                    return rec
                d = t * w / D_p
                rec = {"d_c_l": float(d[0]), "d_omega": float(d[1])}
                if params is not None:
                    rec["d_log_omega"] = float(np.log1p(d[1] / params[1])) if d[1] / params[1] > -1 else -float("inf")
                return rec
            hw = phys(t_curv)
            if params is not None and omega_min is not None and np.isfinite(t_curv):
                dom = abs(hw["d_omega"])
                hw["model_minimizer_omega"] = float(omega_min)
                hw["d_log_omega_about_minimizer_plus"] = float(np.log1p(dom / omega_min)) if omega_min > 0 else "undefined"
                hw["d_log_omega_about_minimizer_minus"] = (float(np.log1p(-dom / omega_min))
                                                           if omega_min > 0 and dom < omega_min else -float("inf"))
            rows.append({"eigvec_scaled": w.tolist(), "eigval_scaled": float(lam[k]), "regular": bool(ok[k]),
                         "from_current_plus": phys(t_plus), "from_current_minus": phys(t_minus),
                         "about_model_minimizer_halfwidth": hw})
        out[f"{f:g}"] = rows
    return out


def analyse(R, qtr, rr, D, phase=None, params=None, trunc=TRUNC):
    R = np.asarray(R, float); qtr = np.asarray(qtr, float); D = np.asarray(D, float); rr = float(rr)
    n = R.shape[0]; na = n - 2
    out = {"version": 6, "n": n, "O1": 0.5 * rr, "cutoff": CUTOFF}
    # SPEC 7.1 scaling D = column norms of J: if the record's D differs (e.g. an optimizer that scales the parameter
    # columns by a subset of rows), renormalize R to unit columns; J = Q R D is unchanged
    cn = np.linalg.norm(R, axis=0)
    out["record_column_scaling_deviation"] = float(np.abs(cn[cn > 0] - 1.0).max()) if np.any(cn > 0) else None
    cs = np.where(cn > 0, cn, 1.0)
    R = R / cs[None, :]; D = D * cs
    # singular values of J_s (= those of R) and eta(t) of SPEC 7.2
    U, s, Vt = np.linalg.svd(R)
    out["sigma_max"] = float(s[0]); out["sigma_min"] = float(s[-1]); out["cond"] = float(s[0] / s[-1]) if s[-1] > 0 else float("inf")
    c = U.T @ qtr
    out["eta"] = {f"{t:g}": float((c[s > t * s[0]] ** 2).sum() / rr) for t in trunc}
    out["sigma_smallest20_J"] = s[-20:].tolist()
    out["param_content_smallest20_J"] = (Vt[-20:, na:] ** 2).sum(1).tolist()
    Raa, Rap, Rpp = R[:na, :na], R[:na, na:], R[na:, na:]
    qa, qp = qtr[:na], qtr[na:]
    out["sigma_smallest20_Ja"] = np.linalg.svd(Raa, compute_uv=False)[-20:].tolist()
    v = None
    out["phase_projected"] = False       # SPEC 7.3 requires the generator; false if absent or zero
    if phase is not None:
        v = np.asarray(phase, float) * D[:na]
        nv = np.linalg.norm(v)
        if nv > 0 and np.isfinite(nv):
            v = v / nv
            out["phase_generator_|J_a v|/sigma_max"] = float(np.linalg.norm(Raa @ v) / s[0])
            out["phase_projected"] = True
        else:
            v = None
            out["phase_status"] = "zero or non-finite phase vector; not projected"
    Jp_full = np.vstack([Rap, Rpp])
    colnorm = np.sqrt((Jp_full ** 2).sum(0))
    gp = Jp_full.T @ qtr                                                             # J_p^T r (scaled)
    out["param_column_norms_scaled"] = colnorm.tolist()
    out["scaled_param_grad"] = [float(abs(gp[k]) / (colnorm[k] * np.sqrt(rr))) if colnorm[k] > 0 else None for k in range(2)]   # SPEC 7.4 (d)
    out["param_grad_physical"] = (gp * D[na:]).tolist()                              # dO1/dp = D J_s^T r
    D_p = D[na:]
    par = None if params is None else np.asarray(params, float)
    red = {}
    for t in sorted(set((CUTOFF,) + tuple(x for x in trunc if x > 0))):
        Res, qres, rank_a, _ = _reduced(Raa, Rap, Rpp, qa, qp, t, v)
        S = Res.T @ Res; g = Res.T @ qres
        Sp, lam, W, ok, condS = _pinv_sym(S)
        singular = (not ok.all()) or condS > 1.0 / CUTOFF
        Sph = D_p[:, None] * S * D_p[None, :]                                        # S in physical (c_l, omega)
        lph, Wph = np.linalg.eigh(Sph)
        def cosr(num, den):
            return float(num / den) if den > 0 else None
        rec = {"coef_rank_kept": rank_a,
               "absorption_cos_columns": [cosr(np.linalg.norm(Res[:, k]), colnorm[k]) for k in range(2)],
               "S_scaled": S.tolist(), "S_eigvals_scaled": lam.tolist(), "S_eigvecs_scaled_columns": W.tolist(),
               "scaled_eigvecs_in_physical_units": [(W[:, k] / D_p / np.linalg.norm(W[:, k] / D_p)).tolist() for k in range(2)],
               "S_physical": Sph.tolist(), "S_physical_eigvals": lph.tolist(), "S_physical_eigvecs_columns": Wph.tolist(),
               "absorption_cos_eigvecs": [cosr(np.linalg.norm(Res @ W[:, k]), np.linalg.norm(Jp_full @ W[:, k])) for k in range(2)],
               "cond_S": condS, "parameter_singular": bool(singular),
               "g_red_scaled": g.tolist()}
        if par is not None:
            Tl = np.array([1.0, par[1]])                                              # d omega = omega d log omega
            Slog = Tl[:, None] * Sph * Tl[None, :]
            llg, Wlg = np.linalg.eigh(Slog)
            rec.update(S_cl_logomega=Slog.tolist(), S_cl_logomega_eigvals=llg.tolist(), S_cl_logomega_eigvecs_columns=Wlg.tolist())
        rec["corr_cl_omega"] = None if singular else float(Sp[0, 1] / np.sqrt(Sp[0, 0] * Sp[1, 1]))
        dps = -Sp @ g
        rec["reduced_GN_step_physical"] = (dps / D_p).tolist()
        rec["reduced_predicted_rel_decrease"] = float(g @ Sp @ g / rr)               # (1/2) g S^+ g / O1
        om_min = None if par is None else float(par[1] + (dps / D_p)[1])
        rec["model_minimizer_physical"] = None if par is None else [float(par[0] + (dps / D_p)[0]), om_min]
        rec["widths"] = _widths(lam, W, g, rr, D_p, par, ok, omega_min=om_min)
        red[f"{t:g}"] = rec
    out["reduced"] = red
    out["reduced_default_cutoff"] = f"{CUTOFF:g}"
    return _clean(out)


def _clean(x):
    """Standard JSON: non-finite floats become explicit strings."""
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    if isinstance(x, (float, np.floating)):
        if np.isnan(x):
            return "undefined"
        if np.isinf(x):
            return "unbounded+" if x > 0 else "unbounded-"
        return float(x)
    return x


KINDS = ("J_c", "J_cw", "J_f")


def jacobian_kind(label, explicit=None):
    """Explicit record key first; otherwise whole-word tokens of the label. Returns J_c, J_cw, J_f, unknown or
    ambiguous."""
    if explicit is not None:
        return explicit if explicit in KINDS else "unknown"
    if not label:
        return "unknown"
    found = set(re.findall(r"(?<![A-Za-z0-9_])(J_cw|J_c|J_f)(?![A-Za-z0-9_])", label))
    if len(found) == 1:
        return found.pop()
    return "ambiguous" if found else "unknown"


def load_record(path, coords=None):
    """Read a linearization record (.npz). Returns (kwargs for analyse, metadata). coords overrides the record's
    declaration ("physical" or "optimizer"); without either, a record with z_opt and chain factors is read as optimizer
    coordinates (worker_d6 convention, verifier V023) and the assumption is recorded."""
    d = np.load(path, allow_pickle=False)
    f = set(d.files)
    meta = {"record": str(path), "keys": sorted(f)}
    R = d["R"]; n = R.shape[0]; na = n - 2
    qtr = d["qtr"] if "qtr" in f else d["Qtr"]
    rr = float(d["rr"] if "rr" in f else d["r_norm2"])
    D = np.array(d["D"], float)
    phase = None
    if "phase" in f:
        phase = np.array(d["phase"], float)
    elif "generator_red" in f:
        gr = np.array(d["generator_red"], float)
        if gr.size == n:
            meta["generator_param_slots"] = gr[na:].tolist()
            gr = gr[:na]
        phase = gr
    par, chain = None, None
    if "params" in f:
        pv = d["params"]
        if pv.dtype.kind in "US":
            pj = json.loads(str(pv))
            meta["params_record"] = pj
            if "c_l" in pj and "omega" in pj:
                par = np.array([pj["c_l"], pj["omega"]], float)
            if "dcl_dzc" in pj and "domega_dzw" in pj:
                chain = np.array([pj["dcl_dzc"], pj["domega_dzw"]], float)
        else:
            par = np.array(pv, float)
    decl = coords or (str(d["param_coords"]) if "param_coords" in f else None)
    if decl is None:
        if "z_opt" in f and chain is None:
            raise ValueError("ambiguous coordinates: record has z_opt but no chain factors; declare coords explicitly")
        decl = "optimizer" if "z_opt" in f else "physical"
        meta["coords_assumed"] = True
    else:
        meta["coords_assumed"] = False
    meta["param_coords_in_record"] = decl
    if decl == "optimizer":
        if chain is None or not np.all(np.isfinite(chain)) or np.any(chain <= 0):
            raise ValueError("optimizer-coordinate record without positive chain factors")
        D = D.copy(); D[na:] = D[na:] / chain                 # J_s unchanged; physical scaling of the parameter columns
        meta["chain_factors"] = chain.tolist()
    meta["label"] = str(d["label"]) if "label" in f else None
    meta["jacobian_kind"] = jacobian_kind(meta["label"], str(d["jacobian_kind"]) if "jacobian_kind" in f else None)
    meta["supports_SPEC7_claims"] = meta["jacobian_kind"] == "J_c"
    for k in ("it", "ts", "note", "n_rows", "cost"):
        if k in f:
            v = d[k]; meta[k] = v.item() if v.shape == () else v.tolist()
    return dict(R=R, qtr=qtr, rr=rr, D=D, phase=phase, params=par), meta


def selftest(seed=0):
    """Compare against dense formulas on random tall problems, one with a rank deficient coefficient block and a
    phase-like direction, and check the two-sided widths on the model."""
    rng = np.random.default_rng(seed)
    m, n = 400, 30
    na = n - 2
    errs = {}
    for case in ("full_rank", "rank_deficient"):
        J = rng.standard_normal((m, n)) @ np.diag(np.logspace(0, -6, n))
        J[:, -1] += 0.9 * J[:, 3]
        if case == "rank_deficient":
            J[:, 5] = 2.0 * J[:, 4]                        # exact coefficient dependence
        r = rng.standard_normal(m)
        D = np.linalg.norm(J, axis=0)
        Js = J / D
        Q, R = np.linalg.qr(Js)
        phase = rng.standard_normal(na) / D[:na]           # unscaled generator, arbitrary for the test
        out = analyse(R, Q.T @ r, r @ r, D, phase=phase, params=(0.45, 1.0))
        rec = out["reduced"]["1e-12"]
        Ja, Jp = Js[:, :na], Js[:, na:]
        vs = phase * D[:na]; vs /= np.linalg.norm(vs)
        Jav = Ja - np.outer(Ja @ vs, vs)
        Ua, sa, _ = np.linalg.svd(Jav, full_matrices=False)
        Ut = Ua[:, sa > 1e-12 * sa[0]]
        Pa = Ut @ Ut.T
        Sd = Jp.T @ (np.eye(m) - Pa) @ Jp
        gd = Jp.T @ (np.eye(m) - Pa) @ r
        cosd = np.linalg.norm((np.eye(m) - Pa) @ Jp, axis=0) / np.linalg.norm(Jp, axis=0)
        PJ = Js @ np.linalg.pinv(Js)
        S = np.array(rec["S_scaled"]); g = np.array(rec["g_red_scaled"])
        e = {"S": float(np.abs(S - Sd).max() / np.abs(Sd).max()),
             "g_red": float(np.abs(g - gd).max() / np.abs(gd).max()),
             "cos": float(np.abs(np.array(rec["absorption_cos_columns"]) - cosd).max()),
             "eta0": abs(out["eta"]["0"] - float(r @ PJ @ r / (r @ r))) if case == "full_rank" else None,
             "grad": float(np.abs(np.array(out["param_grad_physical"]) - J.T[-2:] @ r).max() / np.abs(J.T[-2:] @ r).max())}
        # widths: model change at the reported displacement equals f O1
        lam = np.array(rec["S_eigvals_scaled"]); W = np.array(rec["S_eigvecs_scaled_columns"])
        wmax = 0.0
        for f in ("0.01", "0.1"):
            for k in range(2):
                for side in ("from_current_plus", "from_current_minus"):
                    d = rec["widths"][f][k][side]
                    if isinstance(d["d_c_l"], str) or isinstance(d["d_omega"], str):
                        continue
                    dps = np.array([d["d_c_l"], d["d_omega"]]) * D[na:]
                    model = g @ dps + 0.5 * dps @ S @ dps
                    wmax = max(wmax, abs(model - float(f) * 0.5 * (r @ r)) / (0.5 * (r @ r)))
        e["width_model_check"] = wmax                     # width algebra on the tool's own S and g
        e["S_min_eig_rel_err"] = float(abs(np.linalg.eigvalsh(S)[0] - np.linalg.eigvalsh(Sd)[0]) / np.linalg.eigvalsh(Sd)[0])
        errs[case] = e
    # singular S: identical parameter columns up to scale
    J = rng.standard_normal((m, n)); J[:, -1] = 3.0 * J[:, -2]
    D = np.linalg.norm(J, axis=0); Q, R = np.linalg.qr(J / D)
    o = analyse(R, Q.T @ rng.standard_normal(m), 1.0, D)
    errs["singular_S_flagged"] = o["reduced"]["1e-12"]["parameter_singular"] and o["reduced"]["1e-12"]["corr_cl_omega"] is None
    # verifier V022 edge cases: exact singular 2x2 with g along the regular direction, zero phase, zero parameter column
    R = np.array([[1., 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]); q = np.array([0.1, 0.5, 0.3, 0.7])
    o = analyse(R, q, q @ q + 1, np.ones(4), phase=np.zeros(2), params=(0.45, 1.0))
    w0 = o["reduced"]["1e-12"]["widths"]["0.1"][0]
    errs["singular_direction_unbounded"] = all(isinstance(w0[sd][c], str) for sd in ("from_current_plus", "from_current_minus") for c in ("d_c_l", "d_omega"))
    errs["zero_phase_recorded"] = (o["phase_projected"] is False) and ("phase_status" in o)
    R = np.array([[1., 0, 0.2, 0], [0, 1, 0.5, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
    o = analyse(R, q, q @ q + 1, np.ones(4))
    errs["zero_column_null"] = o["scaled_param_grad"][1] is None and o["reduced"]["1e-12"]["absorption_cos_columns"][1] is None
    json.dumps(o, allow_nan=False)
    errs["json_standard"] = True
    # physical eigenpairs: S_physical v = lambda v
    J = rng.standard_normal((m, n)); D = np.linalg.norm(J, axis=0) * np.r_[np.ones(n - 2), 10.0, 0.1]
    Q, R = np.linalg.qr(J / D); o = analyse(R, Q.T @ rng.standard_normal(m), 1.0, D, params=(0.45, 2.0))
    rec = o["reduced"]["1e-12"]; Sph = np.array(rec["S_physical"]); Wph = np.array(rec["S_physical_eigvecs_columns"])
    errs["physical_eigpair_residual"] = float(max(np.linalg.norm(Sph @ Wph[:, k] - rec["S_physical_eigvals"][k] * Wph[:, k]) for k in range(2)) / np.abs(Sph).max())
    # load_record: a worker-format record in optimizer coordinates gives the physical-coordinate analysis
    import os, tempfile
    J = rng.standard_normal((m, n)); r = rng.standard_normal(m)
    zc, zw = 0.3, np.log(2.0); sg = 1 / (1 + np.exp(-zc)); C = np.array([0.1 * sg * (1 - sg), np.exp(zw)])
    Jz = J.copy(); Jz[:, -2:] = J[:, -2:] * C
    Dz = np.linalg.norm(Jz, axis=0); Q, R = np.linalg.qr(Jz / Dz)
    ph = np.r_[rng.standard_normal(na), 0.0, 0.0]
    tmp = os.path.join(tempfile.mkdtemp(), "rec.npz")
    np.savez(tmp, R=R, Qtr=Q.T @ r, r_norm2=float(r @ r), D=Dz, generator_red=ph, z_opt=np.zeros(n),
             params=json.dumps(dict(c_l=0.4 + 0.1 * sg, omega=2.0, z_c=zc, z_w=zw, dcl_dzc=C[0], domega_dzw=C[1])),
             label="frozen-weight model J_f (test)")
    kw, meta = load_record(tmp)
    o1 = analyse(**kw)
    Dp = np.linalg.norm(J, axis=0); Q2, R2 = np.linalg.qr(J / Dp)
    o2 = analyse(R2, Q2.T @ r, r @ r, Dp, phase=ph[:na], params=(0.4 + 0.1 * sg, 2.0))
    a1, a2 = o1["reduced"]["1e-12"], o2["reduced"]["1e-12"]
    errs["load_record_optimizer_to_physical"] = {
        "S_physical": float(np.abs(np.array(a1["S_physical"]) - np.array(a2["S_physical"])).max() / np.abs(np.array(a2["S_physical"])).max()),
        "param_grad_physical": float(np.abs(np.array(o1["param_grad_physical"]) - np.array(o2["param_grad_physical"])).max() / np.abs(np.array(o2["param_grad_physical"])).max()),
        "step_physical": float(np.abs(np.array(a1["reduced_GN_step_physical"]) - np.array(a2["reduced_GN_step_physical"])).max() / np.abs(np.array(a2["reduced_GN_step_physical"])).max()),
        "coords_assumed": meta["coords_assumed"], "jacobian_kind": meta["jacobian_kind"]}
    os.remove(tmp)
    # record whose D is not the column-norm scaling (parameter columns scaled by a subset of rows): same results
    Dw = Dz.copy(); Dw[-2:] = np.linalg.norm(Jz[: m // 2, -2:], axis=0); Qw, Rw = np.linalg.qr(Jz / Dw)
    np.savez(tmp, R=Rw, Qtr=Qw.T @ r, r_norm2=float(r @ r), D=Dw, generator_red=ph, z_opt=np.zeros(n),
             params=json.dumps(dict(c_l=0.4 + 0.1 * sg, omega=2.0, z_c=zc, z_w=zw, dcl_dzc=C[0], domega_dzw=C[1])),
             label="J_f (test)")
    kw3, _ = load_record(tmp)
    o3 = analyse(**kw3); a3 = o3["reduced"]["1e-12"]
    errs["non_column_norm_D"] = {
        "S_physical": float(np.abs(np.array(a3["S_physical"]) - np.array(a2["S_physical"])).max() / np.abs(np.array(a2["S_physical"])).max()),
        "eta": max(abs(o3["eta"][k] - o2["eta"][k]) for k in o2["eta"]),
        "scaled_param_grad": max(abs(x - y) for x, y in zip(o3["scaled_param_grad"], o2["scaled_param_grad"])),
        "record_deviation": o3["record_column_scaling_deviation"]}
    os.remove(tmp)
    # V036 negative control: z_opt present, chain factors removed, no declaration -> must be rejected
    np.savez(tmp, R=R, Qtr=Q.T @ r, r_norm2=float(r @ r), D=Dz, generator_red=ph, z_opt=np.zeros(n),
             params=json.dumps(dict(c_l=0.4 + 0.1 * sg, omega=2.0)), label="production Jacobian J_cw (test)")
    try:
        load_record(tmp)
        errs["ambiguous_coords_rejected"] = False
    except ValueError:
        errs["ambiguous_coords_rejected"] = True
    os.remove(tmp)
    # Jacobian kind from labels (verifier 21:45Z: the worker's J_cw label must not read as J_c)
    cases = {"production Jacobian J_cw (pressure tables and nonlinear weights differentiated; closure target lagged)": "J_cw",
             "frozen-weight model J_f (test)": "J_f", "complete Jacobian J_c": "J_c", "J_c versus J_f comparison": "ambiguous",
             "no kind": "unknown", "XJ_c": "unknown"}
    errs["jacobian_kind_labels"] = all(jacobian_kind(k) == v for k, v in cases.items())
    errs["jacobian_kind_explicit"] = jacobian_kind("J_c", "J_cw") == "J_cw" and jacobian_kind(None, "other") == "unknown"
    return errs


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] != "--selftest":
        kw, meta = load_record(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
        res = analyse(**kw)
        res["record_meta"] = _clean(meta)
        if not meta["supports_SPEC7_claims"]:
            res["label"] = {"J_f": "frozen-weight model", "J_cw": "lagged-closure model (weights differentiated, closure target lagged)"}.get(
                meta["jacobian_kind"], meta["jacobian_kind"] + " Jacobian") + ": does not establish SPEC 7 stationarity"
        print(json.dumps(res, indent=1, allow_nan=False))
    else:
        print(json.dumps(selftest(), indent=1))
