#!/usr/bin/env python
"""Re-expand a saved state in a representation with a different twist/radial-map radius R0 (or other basis settings) and write a
start file that the worker loads with init_from (Stage III single-change re-solves: R0 factor 2, PROMPT III.3; lead stage3 plan 3).

The exact embedding (transfer.embed_state) needs the same R0; across an R0 change the field is re-expanded by the linear least-squares
fit of transfer.fit_field: the source field U (and nothing else) is evaluated on the destination training grid (its radial nodes and
angular grid) and fitted in the destination basis, in the tail-constrained coordinates when the destination job uses tail constraints.
The fit error is reported (weighted relative residual of fit_field, unweighted relative L2 error and maximum pointwise error on the
grid, the F-gauge int|F|^2 of the fitted state) and saved in the start file's meta; the re-expanded state is a START, not a reading:
the worker's LM then re-solves from it and the comparison with the control is made with scripts/compare_fields.py after the solve.
The far anchors (far_radii, in units of R0) and the dyadic holdout shells (r_core = R0) move with R0: that is part of the change.
Usage: CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=4 .venv/bin/python scripts/reexpand_state.py SRC.pt --out DST.pt --R0 0.6
         [--L 6 --Nk 16 --Nr 48] [--channels NkB,NkD,NkE --chdeg LB,LD,LE] [--no_tail_constraints] [--device cpu] [--chunk 256]"""
import sys, os, json, math, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, DT
from src.optimization.transfer import fit_field
from src.optimization.tail_constraints import TailConstraints

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("--out", required=True)
ap.add_argument("--R0", type=float, default=None); ap.add_argument("--L", type=int, default=None); ap.add_argument("--Nk", type=int, default=None)
ap.add_argument("--Nr", type=int, default=None); ap.add_argument("--channels", default=None); ap.add_argument("--chdeg", default=None)
ap.add_argument("--no_tail_constraints", action="store_true"); ap.add_argument("--device", default="cpu"); ap.add_argument("--chunk", type=int, default=256)
ap.add_argument("--rcond", type=float, default=1e-12)
a = ap.parse_args()
dev = a.device
t0 = time.time()
S = torch.load(a.src, map_location="cpu", weights_only=False)
csrc = dict(S["config"])
if S.get("free_params"):
    raise SystemExit("free-parameter source states are not supported (fix c_l and omega first)")
cdst = dict(csrc)
for k in ("init_from", "perturb", "perturb_m", "perturb_m_rel", "boost_e_core"):
    cdst.pop(k, None)
if a.R0 is not None: cdst["R0"] = float(a.R0)
if a.L is not None: cdst["L"] = int(a.L)
if a.Nk is not None: cdst["Nk"] = int(a.Nk)
if a.Nr is not None: cdst["Nr"] = int(a.Nr)
if a.channels or a.chdeg:
    ch = dict(cdst.get("channels") or {})
    if a.channels:
        nb, nd, ne = [int(v) for v in a.channels.split(",")]; ch.update(NkB=nb, NkD=nd, NkE=ne)
    if a.chdeg:
        lb, ld, le = [int(v) for v in a.chdeg.split(",")]; ch.update(LB=lb, LD=ld, LE=le)
    cdst["channels"] = ch
use_tc = bool(cdst.get("tail_constraints", False)) and not a.no_tail_constraints
cdst["tail_constraints"] = use_tc            # keep the saved config consistent with the fit coordinates
cdst["families"] = ["init_from"]


def train_model(cfg):
    return Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
                 free_params=False, device=dev, channels=cfg.get("channels"), extra_r=(cfg.get("far_radii") if cfg.get("far_merged", True) else None))


Md = train_model(cdst)
# the source field on the destination training grid (same radii, same angular grid): the source model with explicit nodes
Ms = Model(L=csrc["L"], Nk=csrc["Nk"], m_parity=csrc.get("m_parity", "even"), R0=csrc.get("R0", 1.0), r_nodes=Md.r.cpu().numpy(), ntheta=Md.ntheta, nphi=Md.nphi,
           c_l=csrc["c_l"], omega=csrc["omega"], free_params=False, channels=csrc.get("channels"), device=dev, phi0=0.0)
z_src = S["z"].to(dev)
with torch.no_grad():
    U_src = Ms.fields_grid(z_src, need_vort=False)["U"]
print(f"reexpand_state: source {a.src} (L {csrc['L']}, Nk {csrc['Nk']}, R0 {csrc.get('R0', 1.0)}, channels {csrc.get('channels')}) -> destination L {cdst['L']}, Nk {cdst['Nk']}, "
      f"R0 {cdst.get('R0', 1.0)}, channels {cdst.get('channels')}, Nr {Md.Nr} (incl. far anchors {Md.extra_r}), grid {Md.ntheta} x {Md.nphi}, tail constraints {use_tc}", flush=True)
tc = TailConstraints(Md, nu=float(cdst.get("nu", 0.0) or 0.0)) if use_tc else None     # the worker uses the configured nu (0 for Euler jobs)
z_dst, info = fit_field(Md, U_src, chunk=a.chunk, expand=(tc.expand if tc is not None else None), n_red=(tc.n_red if tc is not None else None), rcond=a.rcond)
with torch.no_grad():
    U_fit = Md.fields_grid(z_dst, need_vort=False)["U"]
    w_ang = Md.grid.w / (4 * math.pi)
    num = (((U_fit - U_src) ** 2).sum(0) * w_ang[None, :]).sum(1); den = ((U_src ** 2).sum(0) * w_ang[None, :]).sum(1)
    rel_l2 = math.sqrt(num.sum().item() / max(den.sum().item(), 1e-300))
    maxpt = (U_fit - U_src).norm(dim=0).max().item(); maxU = U_src.norm(dim=0).max().item()
    per_radius = (num / den.clamp_min(1e-300)).sqrt()
    worst = int(torch.argmax(per_radius).item())
# F-gauge of the fitted state (int |F|^2; 1 in the F-gauge)
gauge = None
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("worker", os.path.join(ROOT, "scripts", "worker.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
    cfg = dict(cdst)
    for k in ("core_pin", "nonaxi_pin", "balance_lambda", "radial_lambda_w", "fsw", "efrac", "nu", "pin_c_l"):
        cfg.pop(k, None)
    cfg["closure_lambda"] = 0.0
    model, prob = W.build(cfg, "cpu")
    with torch.no_grad():
        aT, aS, _, _ = model.unpack(z_dst.cpu().clone())
        gauge = float(prob.tail_norm2(aT, aS, torch.tensor(cfg["c_l"]), torch.tensor(cfg["omega"])))
except Exception as e:
    print(f"  F-gauge check failed: {e!r}")
fit = dict(rel_fit_residual_weighted=info["rel_fit_residual"], cond_est=info["cond_est"], rank=info["rank"], n_columns=info["n_columns"], rcond=info["rcond"], method=info["method"],
           rel_l2_error_grid=rel_l2, max_pointwise_error=maxpt, max_U=maxU, worst_radius=float(Md.r[worst]), worst_radius_rel_error=float(per_radius[worst]),
           F_norm2_fitted=gauge, tail_constraints=use_tc, seconds=time.time() - t0)
print(f"  fit: weighted relative residual {info['rel_fit_residual']:.3e}, unweighted relative L2 error {rel_l2:.3e}, max pointwise error {maxpt:.3e} (max|U| {maxU:.3f}), "
      f"worst radius r = {fit['worst_radius']:.4g} (relative error {fit['worst_radius_rel_error']:.3e}); rank {info['rank']} of {info['n_columns']}, cond {info['cond_est']:.2e}; "
      f"F-gauge int|F|^2 of the fitted state {gauge}; {fit['seconds']:.1f} s", flush=True)
src_hold = S.get("spec_diag_holdout") or S.get("spec_diag") or {}
meta = dict(family="reexpand", source=os.path.relpath(os.path.abspath(a.src), ROOT), source_config=dict(L=csrc["L"], Nk=csrc["Nk"], R0=csrc.get("R0", 1.0), channels=csrc.get("channels")),
            fit=fit, note="re-expanded START (linear fit of the source velocity on the destination training grid); not a solved or evaluated state",
            source_rho_u=(src_hold.get("global_") or {}).get("rho_u_max"), source_rho_u_half=(S.get("two_family") or {}).get("rho_u_max_half"))
# The ORIGINAL source's holdout diagnostics are kept in the slots the worker reads for its init_from bookkeeping (meta source_rho_u etc.), so that the
# arm reading's 'start' column refers to the original state; they are NOT diagnostics of the fitted state (which is unevaluated). The same data sit
# under 'original_source_diagnostics' with that name (astra referee 2026-10-26).
out = dict(z=z_dst.detach().cpu(), config=cdst, meta=meta, free_params=False, status="reexpand", iterations=0, lam=None,
           spec_diag_holdout=S.get("spec_diag_holdout"), two_family=S.get("two_family"), spec_diag=None,
           original_source_diagnostics=dict(note="diagnostics of the ORIGINAL source state, not of this fitted start", source=meta["source"],
                                            spec_diag_holdout=S.get("spec_diag_holdout"), two_family=S.get("two_family")))
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
torch.save(out, a.out)
print(f"wrote {a.out} (z {tuple(z_dst.shape)}); use it as init_from in a job with the SAME L, Nk, R0, parity and channels (embed_state is then the identity)")
