#!/usr/bin/env python
"""Contingency check of the full-space pressure against the radial resolution of the pressure SOURCE (lead 2026-10-25T17:49Z item 2 (b); verifier direct
comparison on nest8 (0.45, 1) p0 cont150: grad P global rel L2 9.2e-10, 12 of 54 strict failures, 1.7e-4 relative at the outermost radius).
At FIXED coefficients, the pressure source f = sum_ij d_i U_j d_j U_i is sampled on the training radial nodes (Chebyshev-Gauss in x, Nr_src = 3 Nk in the
exports) and interpolated by the PressureSolver; here it is re-sampled at 3 Nk, 6 Nk and 9 Nk source nodes, P and grad P are recomputed on the export's exchange
grid, the change against the 3 Nk values (and against the stored export) is reported globally, per radius and at the verifier's selected points
(SELECTION.json: radius_indices x angle_indices of the (Nr, ntheta x nphi) grid), together with the source moments 0 (int f) and 1 (int y f).
Nothing is exported or overwritten. Usage: pressure_source_resolution.py <start .pt> <candidate id> [--device cpu] [--selection <SELECTION.json>] [--factors 3,6,9]"""
import sys, os, json, time, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.pressure.poisson_sh import PressureSolver
from src.equations import residuals as res
ap = argparse.ArgumentParser(); ap.add_argument("zfile"); ap.add_argument("cid"); ap.add_argument("--device", default="cpu")
ap.add_argument("--selection", default=None); ap.add_argument("--factors", default="3,6,9"); ap.add_argument("--tag", default="", help="suffix of the output JSON/npz (so that reruns never overwrite earlier results)")
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(a.device)
c_l, om = (float(z[-2]), float(z[-1])) if S.get("free_params") else (cfg["c_l"], cfg["omega"])
L = cfg["L"]; Nk = cfg["Nk"]
cdir = os.path.join(ROOT, "candidates", a.cid)
smp = np.load(os.path.join(cdir, "samples.npz"))
radii = smp["radii"]; theta = smp["theta"]; phi = smp["phi"]; nth, nph = len(theta), len(phi)
P_exp = smp["P_grid"]; gP_exp = smp["gradP_grid"]; y_grid = smp["y_grid"]
sel = None
if a.selection and os.path.exists(a.selection):
    sel = json.load(open(a.selection))
ex = Model(L=L, Nk=Nk, m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), r_nodes=radii, ntheta=nth, nphi=nph, c_l=c_l, omega=om,
           free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
# check the exchange grid reproduces the export's points
yg = ex.r[:, None, None] * ex.n[None, :, :]       # (Nr, Na, 3)
dy = float(np.abs(yg.cpu().numpy().reshape(len(radii), nth, nph, 3) - y_grid).max())
print(f"exchange grid reproduced: max |y - y_export| = {dy:.2e}")
import hashlib as _hl
results = dict(candidate=a.cid, start=os.path.relpath(os.path.abspath(a.zfile), ROOT), c_l=c_l, omega=om, omega_over_c_l=om / c_l, L=L, Nk=Nk, device=a.device,
               code_sha256_12=dict(poisson_sh=_hl.sha256(open(os.path.join(ROOT, "src/pressure/poisson_sh.py"), "rb").read()).hexdigest()[:12], fields=_hl.sha256(open(os.path.join(ROOT, "src/equations/fields.py"), "rb").read()).hexdigest()[:12]),
               pairwise_definition="max over the sphere of max_i |Delta (grad P)_i| (component max; *_euclid keys: Euclidean norm of the difference vector) divided by the five-term RMS of the sphere (sqrt of the summed sphere-mean squares of |T1|..|T5|)",
               export_Nr_src=int(max(cfg.get("Nr") or 0, 3 * Nk)), grid_reproduction_max_abs=dy, factors={}, selection=None)
base = {}; grids = {}
# five momentum terms on the export grid (DU_grid[.., m, i] = d_m U_i; checked by scripts/gradp_point_context.py): RMS per radius for the normalization asked by the lead (18:52Z (a))
Ug = smp["U_grid"]; DUg = smp["DU_grid"]
_T1 = (1 - c_l) * Ug; _T2 = c_l * np.einsum('...mi,...m->...i', DUg, y_grid)
_Jy = np.stack([-y_grid[..., 1], y_grid[..., 0], np.zeros_like(y_grid[..., 2])], -1); _T3 = -om * np.einsum('...mi,...m->...i', DUg, _Jy)
_T4 = np.einsum('...mi,...m->...i', DUg, Ug); _T5 = om * np.stack([-Ug[..., 1], Ug[..., 0], np.zeros_like(Ug[..., 2])], -1)
rms5 = np.sqrt(sum((t ** 2).sum(-1).reshape(len(radii), -1).mean(1) for t in (_T1, _T2, _T3, _T4, _T5)))      # (Nr,) unweighted node mean, five non-pressure pieces (rotation pieces split): the 18:52Z definition
results["five_term_rms_per_radius"] = [float(v) for v in rms5]
wang = smp["angular_weights"].reshape(-1); wang = wang / wang.sum()                                                 # exchange-grid angular weights (32 x 64)
def _wrms(t):                                                                                                        # weighted RMS of a vector field per sphere
    return np.sqrt(((t ** 2).sum(-1).reshape(len(radii), -1) * wang[None, :]).sum(1))
_T3spec = _T5 + _T3                                                                                                  # omega [J U - (J y . grad) U]
def _spec_den(gP_):                                                                                                   # SPEC 7.2 per-sphere denominator: sum of the weighted RMS of the five terms incl. grad P
    return _wrms(_T1) + _wrms(_T2) + _wrms(_T3spec) + _wrms(_T4) + _wrms(gP_)
def _nl_scale(gP_):                                                                                                   # nonlinear scale: RMS((U . grad) U) + RMS(grad P)
    return _wrms(_T4) + _wrms(gP_)
for k in [int(v) for v in a.factors.split(",")]:
    t0 = time.time()
    Nr_k = k * Nk
    train = Model(L=L, Nk=Nk, m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=Nr_k, c_l=c_l, omega=om,
                  free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
    ps = PressureSolver(train, p0=2 * alpha_of(c_l) + 2, omega=om, c_l=c_l, eval_model=ex)
    with torch.no_grad():
        GU = train.fields_grid(z, need_vort=False)["GU"]
        f_src = res.pressure_source(GU)
        P, gradP, Plm, dPlm = ps.solve(f_src)
        M0 = float(ps.volume_integral(f_src))
        ytr = train.r[:, None, None] * train.n[None, :, :]
        M1 = [float(ps.volume_integral(f_src * ytr[..., i])) for i in range(3)]
        gP0 = ps.gradP_origin(f_src).cpu().numpy().tolist()
    Pg = P.cpu().numpy().reshape(len(radii), nth, nph); gPg = gradP.permute(1, 2, 0).cpu().numpy().reshape(len(radii), nth, nph, 3)
    grids[str(k)] = dict(P=Pg, gradP=gPg)
    rec = dict(Nr_src=Nr_k, seconds=time.time() - t0, source_moment0=M0, source_moment1=M1, gradP_origin=gP0,
               source_nodes_max_r=float(train.r.max()))
    # against the stored export
    rec["vs_export"] = dict(P_rel_L2=float(np.linalg.norm(Pg - P_exp) / np.linalg.norm(P_exp)), gradP_rel_L2=float(np.linalg.norm(gPg - gP_exp) / np.linalg.norm(gP_exp)),
                            P_max_abs=float(np.abs(Pg - P_exp).max()), gradP_max_abs=float(np.abs(gPg - gP_exp).max()))
    if not base:
        base = dict(P=Pg, gP=gPg, k=k)
    else:
        dP = Pg - base["P"]; dg = gPg - base["gP"]
        per_r = [float(np.abs(dg[j]).max() / max(np.abs(base["gP"][j]).max(), 1e-300)) for j in range(len(radii))]
        rec[f"vs_{base['k']}Nk"] = dict(P_rel_L2=float(np.linalg.norm(dP) / np.linalg.norm(base["P"])), gradP_rel_L2=float(np.linalg.norm(dg) / np.linalg.norm(base["gP"])),
                                        gradP_rel_max_per_radius=per_r, gradP_rel_max=float(max(per_r)), r_at_max=float(radii[int(np.argmax(per_r))]),
                                        gradP_rel_outermost=per_r[-1], gradP_rel_innermost=per_r[0])
        if sel is not None:
            ri = np.array(sel["radius_indices"]); ai = np.array(sel["angle_indices"])
            it, ip = ai // nph, ai % nph
            sub_b = base["gP"][ri][:, it, ip, :]; sub_k = gPg[ri][:, it, ip, :]
            rel_pts = np.abs(sub_k - sub_b).max(-1) / np.maximum(np.abs(sub_b).max(-1), 1e-300)
            rec[f"vs_{base['k']}Nk"]["selected_points"] = dict(n=int(rel_pts.size), gradP_rel_max=float(rel_pts.max()), gradP_rel_median=float(np.median(rel_pts)),
                                                              per_radius_max=[float(v) for v in rel_pts.max(1)], radii=[float(radii[j]) for j in ri],
                                                              P_rel_max=float((np.abs(Pg[ri][:, it, ip] - base["P"][ri][:, it, ip]) / np.maximum(np.abs(base["P"][ri][:, it, ip]), 1e-300)).max()))
    results["factors"][str(k)] = rec
    msg = f"Nr_src {Nr_k} ({k} Nk): {rec['seconds']:.0f} s; moment0 {M0:.6e}, moment1 {M1}; vs export P rel L2 {rec['vs_export']['P_rel_L2']:.2e}, gradP rel L2 {rec['vs_export']['gradP_rel_L2']:.2e}"
    if k != base["k"]:
        vb = rec["vs_%dNk" % base["k"]]
        msg += f"; vs {base['k']}Nk: gradP rel L2 {vb['gradP_rel_L2']:.2e}, max per radius {vb['gradP_rel_max']:.2e} at r {vb['r_at_max']:.3g}, outermost {vb['gradP_rel_outermost']:.2e}"
        if "selected_points" in vb:
            msg += f"; selected points: gradP rel max {vb['selected_points']['gradP_rel_max']:.2e}, median {vb['selected_points']['gradP_rel_median']:.2e}"
    print(msg, flush=True)
# pairwise comparisons normalized by the five-term RMS per radius (max over the sphere of |Delta grad P| / RMS5(radius)), and the outermost-sphere agreement
ks = sorted(grids, key=int)
results["pairwise"] = {}
for i in range(len(ks)):
    for j in range(i + 1, len(ks)):
        ga, gb = grids[ks[i]]["gradP"], grids[ks[j]]["gradP"]
        d = np.abs(gb - ga).max(-1).reshape(len(radii), -1).max(1)            # (Nr,) max |Delta grad P| component per sphere
        de = np.sqrt(((gb - ga) ** 2).sum(-1)).reshape(len(radii), -1).max(1)   # (Nr,) max Euclidean norm of the difference vector per sphere (lead 19:12Z)
        ratio = d / np.maximum(rms5, 1e-300); ratio_e = de / np.maximum(rms5, 1e-300)
        den_spec = _spec_den(ga); den_nl = _nl_scale(ga)
        ratio_spec = de / np.maximum(den_spec, 1e-300); ratio_nl = de / np.maximum(den_nl, 1e-300)                 # vector max over the sphere against the SPEC denominator / the nonlinear scale (lead 19:16Z)
        outer = dict(radius=float(radii[-1]), radius_over_R0=float(radii[-1] / cfg.get("R0", 1.0)), max_abs_delta_gradP=float(d[-1]), rms_gradP=float(np.sqrt((ga[-1] ** 2).sum(-1).mean())),
                     rel_to_local_gradP=float(d[-1] / max(np.sqrt((ga[-1] ** 2).sum(-1).mean()), 1e-300)), rel_to_five_terms=float(ratio[-1]))
        results["pairwise"][f"{ks[i]}Nk_vs_{ks[j]}Nk"] = dict(max_over_radii_delta_gradP_over_rms5=float(ratio.max()), max_over_radii_delta_gradP_over_rms5_euclid=float(ratio_e.max()), per_radius_euclid=[float(v) for v in ratio_e],
                                                             SPEC_denominator_vector_max=dict(max_over_radii=float(ratio_spec.max()), radius_at_max_over_R0=float(radii[int(np.argmax(ratio_spec))] / cfg.get("R0", 1.0)), per_radius=[float(v) for v in ratio_spec],
                                                                                              definition="max over the sphere of |Delta grad P| (Euclidean) / [sum of the angular-weighted RMS of (1-c_l)U, c_l (y.grad)U, omega(JU - (Jy.grad)U), (U.grad)U, grad P] (SPEC 7.2 five-term denominator)"),
                                                             nonlinear_scale_vector_max=dict(max_over_radii=float(ratio_nl.max()), radius_at_max_over_R0=float(radii[int(np.argmax(ratio_nl))] / cfg.get("R0", 1.0)), outermost=float(ratio_nl[-1]), per_radius=[float(v) for v in ratio_nl],
                                                                                             definition="max over the sphere of |Delta grad P| (Euclidean) / [RMS((U.grad)U) + RMS(grad P)] (angular-weighted)"),
                                                             outermost_max_abs_delta_gradP_euclid=float(de[-1]), radius_at_max=float(radii[int(np.argmax(ratio))]),
                                                             radius_at_max_over_R0=float(radii[int(np.argmax(ratio))] / cfg.get("R0", 1.0)), per_radius=[float(v) for v in ratio], outermost_sphere=outer,
                                                             gradP_rel_L2=float(np.linalg.norm(gb - ga) / np.linalg.norm(ga)), P_rel_L2=float(np.linalg.norm(grids[ks[j]]["P"] - grids[ks[i]]["P"]) / np.linalg.norm(grids[ks[i]]["P"])))
        print(f"   SPEC denominator (vector max): {ratio_spec.max():.4e} at {radii[int(np.argmax(ratio_spec))] / cfg.get('R0', 1.0):.4g} R0; nonlinear scale RMS((U.grad)U) + RMS(grad P): max {ratio_nl.max():.3e} at {radii[int(np.argmax(ratio_nl))] / cfg.get('R0', 1.0):.4g} R0, outermost {ratio_nl[-1]:.3e}", flush=True)
        print(f"{ks[i]} Nk vs {ks[j]} Nk: max over radii of |Delta grad P| / RMS(five terms) = {ratio.max():.3e} at r = {radii[int(np.argmax(ratio))]:.4g} ({radii[int(np.argmax(ratio))] / cfg.get('R0', 1.0):.4g} R0); "
              f"outermost sphere: max |Delta grad P| {outer['max_abs_delta_gradP']:.3e} = {outer['rel_to_local_gradP']:.3e} of the local RMS grad P = {outer['rel_to_five_terms']:.3e} of the five-term RMS; grad P rel L2 {results['pairwise'][f'{ks[i]}Nk_vs_{ks[j]}Nk']['gradP_rel_L2']:.3e}", flush=True)
_npz = os.path.join(ROOT, "reports", f"pressure_gradP_grids_{a.cid}{a.tag}.npz")
np.savez(_npz, radii=radii, **{f"P_{k}Nk": grids[k]["P"] for k in grids}, **{f"gradP_{k}Nk": grids[k]["gradP"] for k in grids})
import hashlib
results["grids_npz"] = dict(path=os.path.relpath(_npz, ROOT), sha256=hashlib.sha256(open(_npz, "rb").read()).hexdigest(), keys=[f"P_{k}Nk" for k in grids] + [f"gradP_{k}Nk" for k in grids], note="full exchange-grid arrays (Nr, ntheta, nphi[, 3]) per source resolution; the verifier's selected points are radius_indices x angle_indices (angle = itheta * nphi + iphi)")
if sel is not None:
    results["selection"] = dict(path=a.selection, points=sel.get("points"), radius_indices=sel["radius_indices"], radii=sel.get("radii"), sha256=sel.get("selection_sha256"))
results["omp_threads"] = os.environ.get("OMP_NUM_THREADS"); results["written"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
op = os.path.join(ROOT, "reports", f"pressure_source_resolution_{a.cid}{a.tag}.json"); json.dump(results, open(op, "w"), indent=1)
print(f"wrote {op}")
