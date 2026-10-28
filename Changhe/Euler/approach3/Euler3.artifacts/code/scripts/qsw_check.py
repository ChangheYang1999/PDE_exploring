#!/usr/bin/env python
"""Smoke test of the mean-swirl block (Q_sw, d50 closure) on saved starts: qsw_check.py <start files...>"""
import sys, os, time, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.far_field.ray_functional import ray_functionals
dev = "cuda:0"
for zf in sys.argv[1:]:
    S = torch.load(zf, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(dev)
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
                  free_params=S.get("free_params", False), channels=cfg.get("channels"), device=dev, extra_r=cfg.get("far_radii") if cfg.get("far_merged", True) else None)
    prob = Problem(model, formulation="mom"); prob.pivot = S.get("pivot")
    t0 = time.time()
    npo = int(os.environ.get("QSW_NPO", "12"))  # radial samples per octave for the mean-swirl block (export grid = 4)
    rf = ray_functionals(prob, z, n_per_octave=npo, k_in=8, k_out=16, radii_tau=[2.0 ** 8 * model.R0, 2.0 ** 12 * model.R0])
    print(os.path.relpath(zf, ROOT), f"n_per_octave {npo} {time.time() - t0:.0f}s tau_F", {k: round(v, 4) for k, v in rf["tau_F"].items()})
    print("   mean_swirl:", json.dumps(rf["mean_swirl"]))
    print(f"   GPU peak {torch.cuda.max_memory_allocated() / 2**30:.1f} GB"); torch.cuda.reset_peak_memory_stats()
    sys.stdout.flush()
