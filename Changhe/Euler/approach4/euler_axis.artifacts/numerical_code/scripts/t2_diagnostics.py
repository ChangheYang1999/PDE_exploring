"""T2 diagnostics (lead note 17): on the upper axis q = eta = eta_s = 0 and eta < 0 far out; eta_z(s, 0) > 0 on the equator.
Reports for a run: max |q(0,z)|, max |eta(0,z)|, eta_s(0,z) at a few axis points, min eta_z(s,0) over the equator, sign of eta on the
upper axis, the five T2 row defects.  Usage: python3 scripts/t2_diagnostics.py <run_dir> [...]"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem, Config
from axi import ops, validate
torch.set_default_dtype(torch.float64)
for run_dir in sys.argv[1:]:
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device="cpu"); cfg = prob.cfg
    cl = prob.cl_of(x)
    zs = np.geomspace(0.05, 50.0, 40)
    fa = validate.fields(prob, x, zs, np.ones_like(zs), cl)          # upper axis
    # eta_s on the axis: eta(r, z) ~ eta(0,z) + s eta_s -> eta_s = (eta(h, z) - eta(0, z))/h^2
    h = 1e-3
    Rh = np.sqrt(h * h + zs * zs); fh = validate.fields(prob, x, Rh, zs / Rh, cl)
    eta_s = (fh["eta"] - fa["eta"]) / h ** 2
    rs = np.geomspace(0.05, 50.0, 40)
    fe_p = validate.fields(prob, x, np.sqrt(rs ** 2 + h ** 2), h / np.sqrt(rs ** 2 + h ** 2), cl)
    fe_m = validate.fields(prob, x, np.sqrt(rs ** 2 + h ** 2), -h / np.sqrt(rs ** 2 + h ** 2), cl)
    eta_z_eq = (fe_p["eta"] - fe_m["eta"]) / (2 * h)
    res = json.load(open(os.path.join(run_dir, "result.json"))) if os.path.exists(os.path.join(run_dir, "result.json")) else {}
    out = dict(cl=cl, max_abs_q_axis=float(np.max(np.abs(fa["q"]))), max_abs_eta_axis=float(np.max(np.abs(fa["eta"]))), eta_axis_sign_far=float(np.sign(fa["eta"][-1])),
               eta_axis_values=[float(v) for v in fa["eta"][::8]], eta_s_axis=[float(v) for v in eta_s[::8]], min_eta_z_equator=float(np.min(eta_z_eq)),
               eta_z_equator_at_r1=float(np.interp(1.0, rs, eta_z_eq)), K=cfg.K_param, target_eta_z_ring=2 * cfg.K_param ** 2 / (3 * cl),
               point_row_defects=res.get("point_row_defects"), rho_max=(res.get("validation") or {}).get("rho_max"), s_core=(res.get("validation") or {}).get("s_core"))
    json.dump(out, open(os.path.join(run_dir, "t2_diagnostics.json"), "w"), indent=1, default=float)
    print(os.path.basename(run_dir), json.dumps({k: v for k, v in out.items() if k not in ("eta_axis_values", "eta_s_axis", "point_row_defects")}, default=float))
