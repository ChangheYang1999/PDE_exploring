"""SPEC 9.1 Jacobian diagnostics: the five smallest singular values (normalized by the largest) of the column-scaled, gauged
Jacobian at a run's final state, with and without the c_l column.  Usage: python3 scripts/jacobian_svals.py <run_dir> [...]"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem, Config
torch.set_default_dtype(torch.float64)
dev = "cuda" if torch.cuda.is_available() else "cpu"
for run_dir in sys.argv[1:]:
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    cfg = Config.from_json(d["cfg"]); out = {}
    if cfg.free_cl:    # evaluate at the FINAL c_l
        p0 = Problem(cfg, device="cpu"); cfg.cl = float(d["x"][p0.ix_cl]); d = dict(d); d["cfg"] = cfg.to_json()
    for free in (False, True):
        c2 = Config.from_json(d["cfg"]); c2.free_cl = free
        prob = Problem(c2, device=dev)
        if "gauge_target" in d: prob.cfg.gauge_target = d["gauge_target"]
        if "row_scale" in d: prob.cfg.w_q, prob.cfg.w_eta = d["row_scale"]
        x = d["x"].clone()
        if free and not cfg.free_cl:
            # insert the c_l unknown at its index (after the field coefficients)
            x = torch.cat([x[:prob.ix_cl], torch.tensor([prob.cl]), x[prob.ix_cl:]])
        if not free and cfg.free_cl:
            p0 = Problem(cfg, device="cpu"); x = torch.cat([x[:p0.ix_cl], x[p0.ix_cl + 1:]])
        J = prob.jacobian(x.to(dev))
        dcol = torch.sqrt(torch.clamp(torch.sum(J * J, 0), min=1e-300))
        S = torch.linalg.svdvals(J / dcol[None, :]).cpu().numpy()
        out["free_cl" if free else "fixed_cl"] = dict(sigma_min5_over_max=[float(v / S[0]) for v in S[-5:][::-1]], cond=float(S[0] / S[-1]), nx=int(J.shape[1]), rows=int(J.shape[0]))
    json.dump(out, open(os.path.join(run_dir, "jacobian_svals.json"), "w"), indent=1)
    print(os.path.basename(run_dir), json.dumps(out))
