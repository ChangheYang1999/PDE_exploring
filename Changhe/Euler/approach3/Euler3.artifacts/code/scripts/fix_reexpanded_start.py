#!/usr/bin/env python
"""Corrected re-expanded warm start (shift 10; lead rule (iii): the carried B/D/E coefficients come from a stated rule, not from the
ill-conditioned fit). Takes a start written by reexpand_state.py (A/C velocity fit kept) and replaces the channel coefficients:
  --rule zero     : B = D = E = 0 (the carried first correction is absent; closure mismatch m = 1 by definition).
  --rule closure  : B and D closure-consistent: the carried pattern coefficients c solve min || sqrt(w) (V c - G_required(F)) || on the
                    closure grid (G_required from the fitted leading tail F, as in Problem.update_closure); the whole value sits in the
                    first radial (Chebyshev k = 0) coefficient of each carried mode, the other radial coefficients are 0; E = 0.
Writes a start file with the same config and a meta_fix record (rule, source sha, mismatch before/after, non-finite counts).
CPU only; a diagnostic/preparation tool; the output is a START, never a reading. Usage:
  fix_reexpanded_start.py SRC.pt --job JOB.json --out DST.pt --rule zero|closure"""
import sys, os, json, math, argparse, time, hashlib
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, DT
from src.optimization.transfer import embed_state
def alpha_of(c):
    return (1.0 - float(c)) / float(c)
import worker as W

ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--job", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--rule", choices=["zero", "closure"], required=True)
a = ap.parse_args(); t0 = time.time()
J = json.load(open(a.job)); cfg = dict(J["config"]); cfg["init_from"] = a.src
model, prob = W.build(cfg, "cpu")
S = torch.load(a.src, map_location="cpu", weights_only=False); scfg = S["config"]
msrc = Model(L=scfg["L"], Nk=scfg["Nk"], m_parity=scfg.get("m_parity", "even"), R0=scfg.get("R0", 1.0), Nr=scfg.get("Nr"), c_l=scfg["c_l"], omega=scfg["omega"],
             free_params=S.get("free_params", False), channels=scfg.get("channels"), device="cpu")
z = embed_state(S["z"], msrc, model)
dd = model.unpack_all(z)
rec = dict(rule=a.rule, source=a.src, source_sha256=hashlib.sha256(open(a.src, "rb").read()).hexdigest(), job=J["job_id"], R0=model.R0)
rec["nonfinite_before"] = {k: int((~torch.isfinite(dd[k])).sum()) for k in ("A", "C", "B", "D", "E") if dd[k].numel()}
rec["coef_norm_before"] = {k: float(dd[k].norm()) for k in ("A", "C", "B", "D", "E") if dd[k].numel()}
prob.pivot = prob.choose_pivot(z); prob.maybe_rebuild_pressure(z); prob.update_nl_weights(z); prob.update_closure(z)   # autograd inside first_correction
rec["closure_mismatch_before"] = (prob.closure or {}).get("mismatch")
with torch.no_grad():
    B = torch.zeros_like(dd["B"]); D = torch.zeros_like(dd["D"]); E = torch.zeros_like(dd["E"]) if dd["E"].numel() else dd["E"]
    if a.rule == "closure":
        cl = prob.closure; V = cl["V"]; w = cl["w"]; G = cl["G_req"]                      # V (Na, 3, J), w (Na,), G (Na, 3)
        A_ = (V * w[:, None, None]).reshape(-1, V.shape[-1]); b_ = (G * w[:, None]).reshape(-1)
        c = torch.linalg.lstsq(A_, b_[:, None], rcond=None).solution[:, 0]
        alpha = alpha_of(float(dd["c_l"])); R0 = model.R0
        for j in range(c.numel()):
            q = int(cl["idx"][j]); l = float(cl["l"][j])
            if bool(cl["isB"][j]):
                B[0, q] = c[j] / R0 ** (2 * alpha + 1 + l)
            else:
                D[0, q] = c[j] / R0 ** (2 * alpha + l)
        rec["closure_lstsq_relres"] = float(((A_ @ c - b_).norm() / b_.norm()))
        rec["closure_pattern_count"] = int(c.numel())
    z_new = model.pack(dd["A"], dd["C"], dd["c_l"], dd["omega"], extra=dict(B=B, D=D, E=E))
prob.update_closure(z_new)
rec["closure_mismatch_after"] = (prob.closure or {}).get("mismatch")
with torch.no_grad():
    d2 = model.unpack_all(z_new)
    rec["coef_norm_after"] = {k: float(d2[k].norm()) for k in ("A", "C", "B", "D", "E") if d2[k].numel()}
    U0 = model.fields_grid(z, need_vort=False)["U"]; U1 = model.fields_grid(z_new, need_vort=False)["U"]
    rec["relU_change_training_grid"] = float((U1 - U0).norm() / U0.norm()); rec["maxU_after"] = float(U1.norm(dim=0).max()) if U1.dim() == 3 else float(U1.abs().max())
S2 = dict(S); S2["z"] = z_new.detach().clone(); S2["meta_fix"] = rec
for k in ("spec_diag", "spec_diag_holdout", "two_family"):
    if k in S2:
        S2.pop(k)                      # the source's diagnostics belong to the ORIGINAL state; the corrected start is unevaluated
S2.setdefault("meta", {}); 
if isinstance(S2.get("meta"), dict):
    S2["meta"]["fix_reexpanded_start"] = rec
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
torch.save(S2, a.out)
rec["out"] = a.out; rec["out_sha256"] = hashlib.sha256(open(a.out, "rb").read()).hexdigest(); rec["seconds"] = time.time() - t0
print(json.dumps(rec, indent=1))
