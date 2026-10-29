"""T3 diagnostics (lead note 18 item 2) for a run: Q = q_zz(0,0)/2 (> 0 required); e = eta_z(0,0) versus 2 K Q/(1 + c); the axis first
integral defect w eta - 2 q (q - K) on 0 < z < 1 and z > 1 (relative to max |2 q (q - K)|); the finite part int_0^1 (Q/q(0,z) - 1/z^2) dz
(exactly 1 for an exact T3 profile); the equator relation E(s)(c - f(s))/A(s) versus K (1 + 4c)/(1 + c) with f = phi_z(s,0),
A = q_zz(s,0)/2, E = eta_z(s,0); and whether eta changes sign in z > 0.  Usage: python3 scripts/t3_diagnostics.py <run_dir> [...]"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem, Config
from axi import validate
torch.set_default_dtype(torch.float64)
for run_dir in sys.argv[1:]:
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device="cpu"); cfg = prob.cfg
    cl = prob.cl_of(x); K = cfg.K_param
    def F(r, z):
        r = np.atleast_1d(np.asarray(r, float)); z = np.atleast_1d(np.asarray(z, float))
        R = np.sqrt(r * r + z * z); Rs = np.where(R > 1e-12, R, 1e-12); mu = np.where(R > 1e-12, np.clip(z / Rs, -1, 1), 1.0)
        return validate.fields(prob, x, Rs, mu, cl)
    h = 1e-3
    Q = float((F(0, h)["q"][0] - 2 * F(0, 0)["q"][0] + F(0, -h)["q"][0]) / (2 * h * h))
    e = float((F(0, h)["eta"][0] - F(0, -h)["eta"][0]) / (2 * h))
    e_target = 2 * K * Q / (1 + cl)
    # axis first integral
    out = dict(cl=cl, K=K, Q=Q, e=e, e_target=e_target)
    for lo, hi, nm in ((0.02, 0.98, "0<z<1"), (1.02, 20.0, "z>1")):
        zs = np.linspace(lo, hi, 300) if hi < 2 else np.geomspace(lo, hi, 300)
        f = F(np.zeros_like(zs), zs)
        w = cl * zs + f["Uz"]; defect = w * f["eta"] - 2 * f["q"] * (f["q"] - K)
        out[f"axis_first_integral_rel_defect_{nm}"] = float(np.max(np.abs(defect)) / max(np.max(np.abs(2 * f["q"] * (f["q"] - K))), 1e-300))
    # finite part int_0^1 (Q/q - 1/z^2) dz with Gauss-Legendre in z (integrand regular if q = Q z^2 + ...)
    zg, wg = np.polynomial.legendre.leggauss(80); zg = 0.5 * (zg + 1); wg = 0.5 * wg
    fq = F(np.zeros_like(zg), zg)["q"]
    with np.errstate(divide="ignore", invalid="ignore"):
        integrand = Q / fq - 1.0 / zg ** 2
    out["finite_part_int_0_1"] = float(np.sum(wg * integrand)) if np.all(np.isfinite(integrand)) else float("nan")
    # equator relation
    rs = np.geomspace(0.05, 20.0, 40)
    fp = F(rs, h); fm = F(rs, -h); f0 = F(rs, 0.0)
    A = (fp["q"] - 2 * f0["q"] + fm["q"]) / (2 * h * h); E = (fp["eta"] - fm["eta"]) / (2 * h); fz = -f0["Ur_over_r"]   # phi_z = -U^r/r
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = E * (cl - fz) / A
    out["equator_relation_target"] = K * (1 + 4 * cl) / (1 + cl)
    out["equator_relation_values_r"] = [float(v) for v in rs[::8]]; out["equator_relation_values"] = [float(v) for v in ratio[::8]]
    out["q_on_equator_max_abs"] = float(np.max(np.abs(f0["q"])))
    # eta sign change in z > 0 (half-plane sample)
    R = np.geomspace(0.05, 20.0, 60); mu = np.linspace(0.02, 1.0, 50); RR, MM = np.meshgrid(R, mu, indexing="ij")
    fe = validate.fields(prob, x, RR.ravel(), MM.ravel(), cl)["eta"]
    out["eta_changes_sign_upper_half"] = bool(np.min(fe) < 0 < np.max(fe)); out["eta_min_max_upper"] = [float(np.min(fe)), float(np.max(fe))]
    res = json.load(open(os.path.join(run_dir, "result.json"))) if os.path.exists(os.path.join(run_dir, "result.json")) else {}
    out["rho_max"] = (res.get("validation") or {}).get("rho_max"); out["s_core"] = (res.get("validation") or {}).get("s_core"); out["point_row_defects"] = res.get("point_row_defects")
    json.dump(out, open(os.path.join(run_dir, "t3_diagnostics.json"), "w"), indent=1, default=float)
    print(os.path.basename(run_dir), json.dumps({k: v for k, v in out.items() if "values" not in k and k != "point_row_defects"}, default=float))
