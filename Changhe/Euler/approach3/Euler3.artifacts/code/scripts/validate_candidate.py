#!/usr/bin/env python
"""Single-command validation of a saved start (no training): rebuilds the model from the saved config, evaluates
R_u with full-space pressure and R_Omega on (a) the training grid, (b) a finer angular/radial quadrature grid
(aliasing check), (c) holdout random Cartesian points for the pressure-free vorticity residual, and prints the
diagnostics.  Usage: validate_candidate.py <start_xxx.pt> [--device cuda:0] [--json out.json]"""
import sys, os, json, argparse, math
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem
from src.equations import residuals as res
from src.validation.diagnostics import candidate_diagnostics, summary_line

ap = argparse.ArgumentParser()
ap.add_argument("zfile"); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu")
ap.add_argument("--json", default=None); ap.add_argument("--refine", type=float, default=1.5)
ap.add_argument("--full", action="store_true", help="also holdout-grid SPEC diagnostics, critical points, strength, X5 off-grid vorticity residual maxima, orbit averages")
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False)
cfg = S["config"]; z = S["z"].to(a.device)
out = dict(zfile=a.zfile, config=cfg, meta=S.get("meta"), status=S.get("status"))
def build(scale=1.0, formulation="both"):
    L = cfg["L"]
    ch = cfg.get("channels") or {}
    Lx = max([L] + [int(ch[k]) for k in ("LB", "LD", "LE") if ch.get(k) is not None and ch.get("Nk" + k[1], 0) > 0])   # grids sized by L_ext (channel degrees)
    model = Model(L=L, Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0),
                  Nr=int(round(scale * max(cfg.get("Nr") or 0, 3 * cfg["Nk"]))), ntheta=int(round(scale * (2 * Lx + 8))), nphi=int(round(scale * (4 * Lx + 14))),
                  c_l=cfg["c_l"], omega=cfg["omega"], free_params=S.get("free_params", False), device=a.device, channels=cfg.get("channels"))
    prob = Problem(model, formulation=formulation)
    prob.pivot = S.get("pivot")
    return model, prob
for name, scale in [("training_grid", 1.0), ("refined_grid", a.refine)]:
    model, prob = build(scale)
    d = candidate_diagnostics(prob, z)
    out[name] = d
    print(f"[{name}] Nr={model.Nr} Na={model.Na}: {summary_line(d)}")
    print(f"   R_u  shells RMS: " + " ".join(f"{v:.1e}" for v in d['momentum']['terms']['sum']['shells']))
    print(f"   R_Om shells RMS: " + " ".join(f"{v:.1e}" for v in d['vorticity']['terms']['sum']['shells']))
    print(f"   rel defect R_u : " + " ".join(("--" if v is None else f"{v:.1e}") for v in d['momentum']['rel_defect_shells']))
# holdout points: random in log-radius, pressure-free vorticity residual, scaled by (1+r^2)^(1/(2c_l))
model, prob = build(1.0, "vort")
rng = np.random.default_rng(12345)
r = np.exp(rng.uniform(np.log(0.02), np.log(200.0), size=4000)); n = rng.normal(size=(4000, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
pts = torch.tensor(r[:, None] * n, device=a.device)
pts = torch.cat([pts, torch.tensor([[0.0, 0.0, 0.0], [0.0, 0.0, 0.5], [0.0, 0.0, -3.0]], device=a.device)])
F = model.fields_points(z, pts)
RO = res.vorticity_terms(F)['sum']
sc = (1 + (pts ** 2).sum(-1) / model.R0 ** 2) ** (1 / (2 * cfg["c_l"]))
scaled = RO.norm(dim=0) * sc
Om = F['Om'].norm(dim=0) * sc
out["holdout"] = dict(n_points=int(pts.shape[0]), rms_scaled_R_Omega=float(scaled.pow(2).mean().sqrt()), max_scaled_R_Omega=float(scaled.max()),
                      rms_scaled_Omega=float(Om.pow(2).mean().sqrt()), at_origin=dict(U=[float(v) for v in F['U'][:, -3]], Omega=[float(v) for v in F['Om'][:, -3]], R_Omega=[float(v) for v in RO[:, -3]]))
print(f"[holdout {pts.shape[0]} pts] scaled R_Omega rms {out['holdout']['rms_scaled_R_Omega']:.3e} max {out['holdout']['max_scaled_R_Omega']:.3e} (scaled |Omega| rms {out['holdout']['rms_scaled_Omega']:.3e}); U(0)={out['holdout']['at_origin']['U']}")
if a.full:
    from src.validation.spec_diagnostics import spec_diagnostics, tier_S
    from src.validation.holdout import HoldoutGrid
    from src.validation.critical_points import local_maxima_omega, zeros_of_W
    from src.validation.strength import strength_diagnostics
    from src.validation.residual_max import max_vorticity_residual
    from src.validation.orbit_averages import orbit_averages
    model, prob = build(1.0, "mom")
    c_l, om = (float(z[-2]), float(z[-1])) if S.get("free_params") else (cfg["c_l"], cfg["omega"])
    sd = spec_diagnostics(prob, z); hg = HoldoutGrid(model, r_core=model.R0); sdh = spec_diagnostics(prob, z, holdout=hg)
    out["spec_training"] = sd; out["spec_holdout"] = sdh; out["tier_S_holdout"] = tier_S(sdh)
    g = sdh["global_"]; print(f"[holdout SPEC] rho_u_max {g['rho_u_max']:.3e} rho_nl_max {g['rho_nl_max']:.2e} pi_u_max {g['pi_u_max']:.2e} rho_Om_max {g['rho_Om_max']:.2e} A_u {g['A_u']:.2e}; Sigma_Z {sdh['global_integrals'].get('Sigma_Z')}; tau0 {sdh['origin'].get('tau0_floored')}; tier S {out['tier_S_holdout'][0]}")
    # SPEC v1.11 7.3a second shell family, single spheres, rho_lin/rho_sp (v1.14); G closure when rate-(2alpha+1) channels are carried
    from src.validation.holdout import half_offset_edges, sphere_diagnostics, exchange_radii, two_family_summary, summary_text
    r_max = float(model.r.max())
    hg2 = HoldoutGrid(model, r_core=model.R0, edges=half_offset_edges(model.R0, r_max)); sdh2 = spec_diagnostics(prob, z, holdout=hg2, extras=False)
    sph = sphere_diagnostics(prob, z, exchange_radii(model.R0, model.R0 * 2.0 ** -6, r_max)); tf = two_family_summary(sdh, sdh2, sph)
    out["spec_holdout_half"] = sdh2; out["sphere_diag"] = sph; out["two_family"] = tf; out["tier_S_holdout_half"] = tier_S(sdh2)
    print("[two families] " + summary_text(tf) + f"; tier S half {out['tier_S_holdout_half'][0]}")
    if model.channels.get("NkB", 0) > 0 or model.channels.get("NkD", 0) > 0:
        from src.far_field.correction import closure_distance
        out["G_closure"] = closure_distance(prob, z)
        print(f"[G closure] ||G[F]|| {out['G_closure']['G_norm']:.4f}; dist(G, carried B/D span)/||G|| {out['G_closure']['dist_rel']:.3e} (B degree {out['G_closure'].get('max_B_degree')}, D degree {out['G_closure'].get('max_D_degree')}, rank {out['G_closure'].get('rank')})")
    mx = local_maxima_omega(model, z, c_l, om); zw = zeros_of_W(model, z, c_l, om); out["critical"] = dict(local_maxima=mx, W_zeros=zw)
    if mx: print(f"[critical] located |Omega| max {mx[0]['abs_Omega']:.4f} at r={mx[0]['r']:.3f}: strain ratio {mx[0]['strain_ratio']:.4f}; W zeros {len(zw)}")
    out["strength"] = strength_diagnostics(model, z, c_l, om, located_max_r=(mx[0]['r'] if mx else None)); print("[strength]", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in out["strength"].items() if k != "note"})
    out["X5_vorticity"] = max_vorticity_residual(model, z, c_l, om, sdh["shells"]["edges"], n_random=1024, n_ascend=12, iters=20)
    print("[X5] ascended fixed-gauge max |R_Omega| per shell:", " ".join(f"{o['ascended_max']:.2e}" for o in out["X5_vorticity"]))
    out["orbit_averages"] = orbit_averages(model, z, c_l, om, n_seeds=64, horizons=(2, 4, 8))
    from src.validation.orbit_checks import orbit_checks
    out["orbit_checks_7_14"] = orbit_checks(model, z, c_l, om, n_seeds=32, T_over_cl=4.0, dt_over_cl=0.02)
    oc = out["orbit_checks_7_14"]
    print("[SPEC 7.14 (a)] " + "; ".join(f"t={a['t_over_cl']}/c_l: det defect {a['det_rel_defect_max']:.1e}, Omega transport median {a['Omega_transport_rel_defect_median']:.2e}, beta_0 pullback median {a['beta0_pullback_rel_defect_median']:.2e}" for a in oc['a']))
    for n_, d_ in oc["b"].items():
        print(f"[SPEC 7.14 (b)] {n_}: relative defect median {d_['rel_defect_median']:.3e} max {d_['rel_defect_max']:.3e}; residual accounting closure median {d_['accounting_closure_median']:.1e} ({d_['note']})")
    for T, r_ in out["orbit_averages"]["horizons"].items(): print(f"[orbit T={T}/c_l] <s> median {r_['summary']['median_mean_s']:.3f} min {r_['summary']['min_mean_s']:.3f}; <rho_Om> median {r_['summary']['median_mean_rho_Om']:.3f}")
if a.json:
    json.dump(out, open(a.json, "w"), indent=1, default=str)
    print("wrote", a.json)
