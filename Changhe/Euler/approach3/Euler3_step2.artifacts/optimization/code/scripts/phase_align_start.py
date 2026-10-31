#!/usr/bin/env python
"""Exact azimuthal rotation of a start file to the SPEC 6.2 phase gauge (the pivot pair's sin-type tail amplitude = 0), as the worker's LM
projection would do at its first step (Problem.phase_align). Records the pivot, the rotation angle gamma and the pivot defects before/after.
CPU only. Usage: phase_align_start.py SRC.pt --job JOB.json --out DST.pt"""
import sys, os, json, math, argparse, hashlib, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
import torch; torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.transfer import embed_state
import worker as W
ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--job", required=True); ap.add_argument("--out", required=True); a = ap.parse_args(); t0 = time.time()
J = json.load(open(a.job)); cfg = dict(J["config"]); cfg["init_from"] = a.src
model, prob = W.build(cfg, "cpu")
S = torch.load(a.src, map_location="cpu", weights_only=False); scfg = S["config"]
msrc = Model(L=scfg["L"], Nk=scfg["Nk"], m_parity=scfg.get("m_parity", "even"), R0=scfg.get("R0", 1.0), Nr=scfg.get("Nr"), c_l=scfg["c_l"], omega=scfg["omega"],
             free_params=S.get("free_params", False), channels=scfg.get("channels"), device="cpu")
z = embed_state(S["z"], msrc, model)
with torch.no_grad():
    prob.pivot = prob.choose_pivot(z, rank=int(cfg.get("pivot_rank", 1) or 1)); piv = dict(prob.pivot)      # honours the job's pivot_rank (lead IE S3-5)
    d = model.unpack_all(z); q = piv["q"]; mq = int(model.m_arr[q].item()); arr = d["A"] if piv["pot"] == "T" else d["C"]
    gamma = float(torch.atan2(arr[:, q + 1].sum(), arr[:, q].sum()) / mq)
    gd0 = [float(x) for x in prob.gauge_defects(z)]
    z2 = prob.phase_align(z)
    gd1 = [float(x) for x in prob.gauge_defects(z2)]
    U0 = model.fields_grid(z, need_vort=False)["U"]; U1 = model.fields_grid(z2, need_vort=False)["U"]
    n0 = float(U0.norm()); n1 = float(U1.norm())
rec = dict(tool="phase_align_start.py", source=a.src, source_sha256=hashlib.sha256(open(a.src, "rb").read()).hexdigest(), pivot=dict(pot=piv["pot"], q=q, m=mq, amp=float(piv.get("amp", float("nan")))),
           gamma_coefficient_angle=gamma, physical_rotation_b=-gamma, gauge_defects_before=gd0, gauge_defects_after=gd1, field_norm_ratio=n1 / n0, seconds=time.time() - t0)
S2 = dict(S); S2["z"] = z2.detach().clone()
for k in ("spec_diag", "spec_diag_holdout", "two_family", "critical", "core_resolution", "G_closure", "global_balances"):
    S2.pop(k, None)
S2["meta_phase_align"] = rec; S2["pivot"] = prob.pivot
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True); torch.save(S2, a.out)
rec["out"] = a.out; rec["out_sha256"] = hashlib.sha256(open(a.out, "rb").read()).hexdigest(); print(json.dumps(rec, indent=1))
