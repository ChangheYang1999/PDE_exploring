#!/usr/bin/env python
"""Offline REFIT start file (numerics 2026-10-29T21:3xZ note; lead 16:40:13Z item 3 (iii), (v): F2 refit pilots). The worker's param_init_mode 'refit'
fails for free-parameter models (fit_field fits the two parameter slots as zeros, so TailConstraints.expand sees c_l = 0 and its constraint matrix is
singular; see status/KNOWN_ISSUES.md). This tool does the refit outside the production worker and writes a start file the worker reads as an ordinary
fresh start (init_from, keep_coefficients at the file's own parameters):
  1. load the source start (coefficients z_s at (c_l_s, omega_s)); evaluate U_src = model_src.fields_grid(z_s)['U'] on the common model grid;
  2. build the target model at (c_l_t, omega_t) with free parameters (same L, Nk, channels, R0); TailConstraints tcf of the target model;
  3. fit U_src by src.optimization.transfer.fit_field in the tail-constrained coefficient coordinates with the PARAMETERS FIXED at the target:
     expand_fixed(zr) = tcf.expand(cat(zr, [c_l_t, omega_t]))[:n_coef], n_red = tcf.n_red - 2 (column-scaled truncated-SVD least squares, unchanged);
  4. report the fit residual, condition estimate, rank, the relative change of U on the training grid and per dyadic shell j = -4..8 (discrete sampling diagnostic: unweighted norms over the training-grid samples, V470), the
     far-field norm of the fitted state; save z = cat(coefficients, [c_l_t, omega_t]) RAW (the worker applies its phase alignment and F-gauge
     projection to every fresh start) with config (target parameters, free_params true), meta and the fit record.
Usage: python scripts/refit_start.py <source start .pt> <c_l_t> <omega_t> <out .pt> [--device cuda:0] [--chunk 256]
Writes <out .pt> (exclusive create) and <out .pt>.json (the fit record). Label of the pilot that uses it: FREE (the file is an initial condition, not a result)."""
import os, sys, json, time, math, hashlib, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.tail_constraints import TailConstraints
from src.optimization.transfer import fit_field
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
DT = torch.float64


def build(cfg, c_l, omega, free, dev):
    return Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=c_l, omega=omega, free_params=free,
                 channels=cfg.get("channels"), device=dev, extra_r=cfg.get("far_radii"))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("source"); ap.add_argument("c_l", type=float); ap.add_argument("omega", type=float); ap.add_argument("out"); ap.add_argument("--device", default="cuda:0"); ap.add_argument("--chunk", type=int, default=256)
    a = ap.parse_args(); t0 = time.time(); dev = a.device
    if os.path.exists(a.out):
        raise FileExistsError(a.out)
    S = torch.load(a.source, map_location="cpu", weights_only=False); scfg = dict(S["config"]); free_s = bool(S.get("free_params", False)); zs = S["z"].to(dev)
    c_s, om_s = (float(zs[-2]), float(zs[-1])) if free_s else (float(scfg["c_l"]), float(scfg["omega"]))
    msrc = build(scfg, c_s, om_s, free_s, dev)
    with torch.no_grad():
        U_src = msrc.fields_grid(zs, need_vort=False)["U"]
    model = build(scfg, a.c_l, a.omega, True, dev); tcf = TailConstraints(model)
    assert (model.n_coef == msrc.n_coef) and torch.equal(model.r, msrc.r), "the target model has another grid or coefficient count"
    params = torch.tensor([a.c_l, a.omega], dtype=DT, device=dev); n_coef = model.n_coef
    expand_fixed = lambda zr: tcf.expand(torch.cat([zr, params]))[:n_coef]
    log = lambda m: print(time.strftime("%H:%M:%S", time.gmtime()) + " " + m, flush=True)
    log(f"source {a.source} ({sha(a.source)[:16]}): ({c_s!r}, {om_s!r}), free {free_s}; target ({a.c_l!r}, {a.omega!r}); n_coef {n_coef}, reduced coefficients {tcf.n_red - 2}")
    zfit, info = fit_field(model, U_src, expand=expand_fixed, n_red=tcf.n_red - 2, chunk=a.chunk)      # fit_field appends (model.c_l0, model.omega0) = the target parameters
    assert zfit.numel() == n_coef + 2 and float(zfit[-2]) == a.c_l and float(zfit[-1]) == a.omega, (zfit.numel(), float(zfit[-2]), float(zfit[-1]))
    with torch.no_grad():
        U_new = model.fields_grid(zfit, need_vort=False)["U"]; relU = float((U_new - U_src).norm() / U_src.norm().clamp_min(1e-300))
        U_keep = model.fields_grid(torch.cat([zs[:n_coef], params]), need_vort=False)["U"]; relU_keep = float((U_keep - U_src).norm() / U_src.norm().clamp_min(1e-300))
        shells = {}
        for jj in range(-4, 9):
            msk = (model.r >= model.R0 * 2.0 ** jj) & (model.r < model.R0 * 2.0 ** (jj + 1))
            if msk.any():
                d = (U_new[:, msk] - U_src[:, msk]).norm(); d0 = U_src[:, msk].norm().clamp_min(1e-300); dk = (U_keep[:, msk] - U_src[:, msk]).norm()
                shells[str(jj)] = dict(rel_change_refit=float(d / d0), rel_change_keep=float(dk / d0), n_radii=int(msk.sum()))
    # far-field norm (F-gauge quantity) of the fitted state, through the production Problem
    try:
        from src.optimization.problem import Problem
        from validation.gates import PROD
        prob = Problem(model, **PROD); aT, aS, c_l_, om_ = model.unpack(zfit); Fn2 = float(prob.tail_norm2(aT, aS, c_l_, om_))
    except Exception as e:
        Fn2 = None; log(f"far-field norm not computed: {e!r}")
    log(f"fit: rel residual {info['rel_fit_residual']:.3e}, cond {info['cond_est']:.3e}, rank {info['rank']} of {info['n_columns']}; relU(refit) {relU:.4e} against relU(keep) {relU_keep:.4e}; F_norm2 {Fn2}")
    log("per shell j: refit | keep: " + "; ".join(f"{j}: {v['rel_change_refit']:.3e} | {v['rel_change_keep']:.3e}" for j, v in shells.items()))
    cfg = dict(scfg); cfg.update(c_l=a.c_l, omega=a.omega, free_params=True)
    meta = dict(family="refit_start", source=os.path.abspath(a.source), source_sha256=sha(a.source), source_c_l=c_s, source_omega=om_s, target_c_l=a.c_l, target_omega=a.omega,
                fit=info, relU_change_refit=relU, relU_change_keep=relU_keep, relU_by_shell=shells, F_norm2_fitted=Fn2, tool="scripts/refit_start.py", tool_sha256=sha(os.path.abspath(__file__)),
                note="offline refit of the source velocity field into the basis at the target parameters with the tail constraints evaluated at the target parameters; RAW coefficients (no phase alignment, no F-gauge projection: the worker applies both to a fresh start). relU_change_* and relU_by_shell are DISCRETE SAMPLING diagnostics (unweighted Frobenius norms over the training-grid samples of the shell), not physical-volume L2 norms (V470); the raw fit quality does not establish the quality after the worker F-gauge projection", ts=now(), device=dev, torch=torch.__version__)
    torch.save(dict(z=zfit.detach().cpu(), config=cfg, free_params=True, meta=meta, kind="refit start file (numerics tool; initial condition, not a result)",
                    spec_diag_holdout=S.get("spec_diag_holdout"), two_family=S.get("two_family")), a.out)
    rec = dict(meta, out=os.path.abspath(a.out), out_sha256=sha(a.out), seconds=time.time() - t0)
    json.dump(rec, open(a.out + ".json", "w"), indent=1, default=str); log(f"DONE {a.out} sha256 {rec['out_sha256'][:16]}; {rec['seconds']:.0f} s")


if __name__ == "__main__":
    main()
