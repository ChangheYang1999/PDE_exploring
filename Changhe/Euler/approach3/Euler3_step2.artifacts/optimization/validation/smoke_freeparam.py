"""D6FP first end-to-end check on the production degree-6 configuration (S01, nest6 rung at (0.45, 1)): objective evaluation, exact
parameter columns (jvp through the pressure tables) against central differences of the frozen-weight residual with rebuilt tables,
complete gradient against central differences of the self-consistent objective, and component timings."""
import sys, os, time, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem
from src.optimization.tail_constraints import TailConstraints
from src.optimization.param_map import ParamMap
from src.optimization.lm import jacobian_fwd, param_columns
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
start = sys.argv[1] if len(sys.argv) > 1 else "starts/S01_nest6_cl0.45_om1.0_p0.pt"
S = torch.load(start, map_location="cpu", weights_only=False); cfg = S["config"]
def sync(): (torch.cuda.synchronize() if torch.cuda.is_available() else None)
t0 = time.time()
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
              free_params=True, device=dev, channels=cfg.get("channels"), extra_r=cfg.get("far_radii"))
prob = Problem(model, formulation="mom", nl_weighting=True, nl_denominator=cfg.get("nl_denominator", "all5far"), far_lambda=float(cfg.get("far_lambda", 1e-2)),
               closure_lambda=float(cfg.get("closure_lambda", 0.0)), far_radii=cfg.get("far_radii"))
sync(); print(f"build {time.time()-t0:.1f}s  n_z {model.n_z} Nq {model.Nq} Nr {model.Nr} Na {model.Na} rows {prob.n_pde_residuals()} pressure quad pts {prob.pressure.n_quad} geometry {prob.pressure.geometry_id}")
z_full = torch.cat([S["z"].to(dev), torch.tensor([cfg["c_l"], cfg["omega"]], device=dev)])
tc = TailConstraints(model); pm = ParamMap()
prob.pivot = prob.choose_pivot(z_full)
to_full = lambda zo: tc.expand(pm.expand(zo))
z_opt = pm.reduce(tc.reduce(z_full))
print("pivot", prob.pivot, "n_opt", z_opt.numel())
# base state: weights and closure target at z (as the worker does)
zf = to_full(z_opt)
t0 = time.time(); prob.update_nl_weights(zf); prob.update_closure(zf); sync(); print(f"weights+closure update {time.time()-t0:.2f}s; closure mismatch {prob.closure['mismatch'] if prob.closure else None}")
t0 = time.time(); r, aux = prob.objective_at(zf); sync(); t_obj = time.time() - t0
cost = 0.5 * float(r @ r); print(f"objective_at {t_obj:.2f}s  O1 {cost:.6e}  rows {r.numel()}  blocks {prob.row_blocks()}")
prob.commit_aux(aux)
r2 = prob.residual_vector(zf); print(f"residual_vector after commit: max |r2 - r| = {float((r2 - r).abs().max()):.2e}")
fun = lambda zo: prob.residual_vector(to_full(zo))
pfun = lambda zo: prob.residual_vector(to_full(zo), differentiable_pressure=True)
# timings: fields, pressure, residual
for name, f in [("fields_grid", lambda: model.fields_grid(zf, need_vort=False)), ("pressure solve", None), ("residual_vector", lambda: prob.residual_vector(zf)),
                ("residual_vector differentiable tables", lambda: prob.residual_vector(zf, differentiable_pressure=True)), ("build_tables", lambda: prob.pressure.build_tables(torch.tensor(0.45, device=dev), torch.tensor(1.0, device=dev))),
                ("objective_at (self-consistent)", lambda: prob.objective_at(zf))]:
    if f is None:
        F = model.fields_grid(zf, need_vort=False); src = torch.einsum('mi...,im...->...', F['GU'], F['GU'])
        f = lambda: prob.pressure.solve(src)
    f(); sync(); ts = []
    for _ in range(3):
        t0 = time.time(); f(); sync(); ts.append(time.time() - t0)
    print(f"  time {name}: median {np.median(ts):.3f}s (min {min(ts):.3f})")
# Jacobian timings
sync(); t0 = time.time(); J = jacobian_fwd(fun, z_opt, chunk=int(cfg.get("chunk", 256))); sync(); t_jac = time.time() - t0
print(f"Jacobian (coefficient columns, chunk {cfg.get('chunk', 256)}): {t_jac:.1f}s  shape {tuple(J.shape)}  peak mem {(torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0)/2**30:.1f} GB")
n = z_opt.numel(); pidx = [n - 2, n - 1]
sync(); t0 = time.time(); Jp = param_columns(pfun, z_opt, pidx); sync(); t_p = time.time() - t0
print(f"parameter columns (jvp through the tables): {t_p:.2f}s")
Jp_frozen = J[:, pidx].clone()
print(f"  norm of kernel-dependence part: |Jp - Jp_frozen_tables| / |Jp| = {[float((Jp[:, j] - Jp_frozen[:, j]).norm() / Jp[:, j].norm()) for j in range(2)]}")
# FD of the frozen-weight residual with rebuilt tables (same layout) in optimizer coordinates
def fun_rebuilt(zo):
    return prob.residual_vector_rebuild(to_full(zo))
blocks = prob.row_blocks()
for j, k in enumerate(pidx):
    name = "z_c" if j == 0 else "z_w"
    for h in (1e-3, 1e-4, 1e-5, 1e-6):
        e = torch.zeros_like(z_opt); e[k] = h
        with torch.no_grad():
            d = (fun_rebuilt(z_opt + e) - fun_rebuilt(z_opt - e)) / (2 * h)
        err = float((Jp[:, j] - d).norm() / max(float(d.norm()), 1e-300))
        per = {b[0]: float((Jp[b[1]:b[2], j] - d[b[1]:b[2]]).norm() / max(float(d[b[1]:b[2]].norm()), 1e-300)) for b in blocks}
        print(f"  G1 column {name}: h {h:.0e} rel err {err:.2e}  per block {json.dumps({k_: f'{v:.1e}' for k_, v in per.items()})}")
# complete gradient vs FD of the self-consistent objective
sync(); t0 = time.time(); gc, parts = prob.complete_gradient(zf, return_parts=True); sync(); t_g = time.time() - t0
print(f"complete gradient (full z): {t_g:.2f}s  pattern-FD part {parts['pattern_fd']}")
# chain to optimizer coordinates for the parameter entries
d = pm.describe(z_opt); gc_opt = gc.clone(); gc_opt[-2] *= d["dcl_dzc"]; gc_opt[-1] *= d["domega_dzw"]
# the coefficient part: z_full coefficients = E(a) ... the gradient wrt reduced a needs the chain through tc.expand; use autograd on the composed map instead:
zz = z_opt.detach().clone().requires_grad_(True)
rr = prob.objective_graph(to_full(zz)); cc = 0.5 * (rr @ rr); g_opt, = torch.autograd.grad(cc, zz); g_opt = g_opt.detach(); g_opt[-2] += gc_opt[-2] - gc[-2] * d["dcl_dzc"] + parts['pattern_fd'][0] * d["dcl_dzc"]; g_opt[-1] += parts['pattern_fd'][1] * d["domega_dzw"]
def O1(zo):
    rr_, _ = prob.objective_at(to_full(zo)); return 0.5 * float(rr_ @ rr_)
for j, k in enumerate(pidx):
    name = "z_c" if j == 0 else "z_w"
    for h in (1e-3, 1e-4, 1e-5):
        e = torch.zeros_like(z_opt); e[k] = h
        dd = (O1(z_opt + e) - O1(z_opt - e)) / (2 * h)
        print(f"  G3 dO1/d{name}: complete gradient {float(g_opt[k]):+.6e}  FD(h={h:.0e}) {dd:+.6e}  rel diff {abs(float(g_opt[k]) - dd) / max(abs(dd), 1e-300):.2e}   frozen-model J^T r {float(J[:, k] @ r + 0*Jp[:, j] @ r):+.6e} (with exact p-cols {float(Jp[:, j] @ r):+.6e})")
print(f"peak GPU memory {(torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0)/2**30:.1f} GB")
