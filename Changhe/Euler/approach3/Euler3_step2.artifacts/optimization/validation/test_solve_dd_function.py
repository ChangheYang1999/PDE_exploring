"""D6FP D1: the _SolveDD autograd Function: (1) values equal the direct core; (2) forward-mode tangents (torch.func.jvp) in f and in the tables
against the fp64 chain's tangents and against double-double differences; (3) vmap over jvp works; (4) reverse mode equals the fp64 reverse mode."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.equations import residuals as res
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model = case.prob, case.model
ps = prob.pressure; T = ps.tables
out = {}
with torch.no_grad():
    F = model.fields_grid(case.z_full, need_vort=False); f = res.pressure_source(F["GU"])
    direct = ps._solve_dd_core(f, T["Qc"], T["Qs"], T["sfac"], T["cosb"], T["sinb"]); viaF = ps.solve_dd(f)
    out["values_equal"] = [float((a - b).abs().max()) for a, b in zip(direct, viaF)]
# (2) tangent in f: compare with the fp64 chain tangent (same function, fp64 accuracy) on near rows and dd differences on anchors
torch.manual_seed(3)
fd = torch.randn_like(f) * f.abs().mean()
def g_dd(ff): return ps.solve_dd(ff)[1]
def g_64(ff): return ps._solve_fp64(ff)[1]
_, t_dd = torch.func.jvp(g_dd, (f,), (fd,)); _, t_64 = torch.func.jvp(g_64, (f,), (fd,))
anc = ps.anchor_rows
out["tangent_f_rel_diff_dd_vs_fp64"] = dict(all=float((t_dd - t_64).norm() / t_64.norm()), anchors=float((t_dd[:, anc] - t_64[:, anc]).norm() / t_64[:, anc].norm()))
with torch.no_grad():
    h = 1e-3
    D = (g_dd(f + h * fd) - g_dd(f - h * fd)) / (2 * h)                       # exact for a linear map up to the final roundings
out["tangent_f_vs_dd_difference"] = dict(all=float((t_dd - D).norm() / D.norm()), anchors=float((t_dd[:, anc] - D[:, anc]).norm() / D[:, anc].norm()),
                                      fp64_tangent_vs_dd_difference_anchors=float((t_64[:, anc] - D[:, anc]).norm() / D[:, anc].norm()))
# tangents in the tables (parameter direction): d tables / d c_l by autograd of build_tables, pushed through both chains
zc = case.z_full
c_l = torch.tensor(float(zc[-2]), device=dev, requires_grad=True); om = torch.tensor(float(zc[-1]), device=dev)
Tb = ps.build_tables(c_l, om)
dT = {k: torch.autograd.grad(Tb[k], c_l, torch.ones_like(Tb[k]), retain_graph=True, allow_unused=True)[0] for k in ("Qc", "Qs", "sfac", "cosb", "sinb")}
# directional tangent of each table along dc_l = 1 is sum of per-entry derivatives weighted... use jvp on build_tables instead:
def tabs(c): 
    Tt = ps.build_tables(c, om.detach()); return (Tt["Qc"], Tt["Qs"], Tt["sfac"], Tt["cosb"], Tt["sinb"])
Tp, Tdot = torch.func.jvp(tabs, (c_l.detach(),), (torch.ones_like(c_l.detach()),))
def g_dd_T(Qc, Qs, sf, cb, sb): return ps._solve_dd_core(f, Qc, Qs, sf, cb, sb)[1]
def g_64_T(Qc, Qs, sf, cb, sb): return ps._solve_fp64(f, dict(Qc=Qc, Qs=Qs, sfac=sf, cosb=cb, sinb=sb))[1]
def g_ddF_T(Qc, Qs, sf, cb, sb): return __import__("src.pressure.poisson_sh", fromlist=["_SolveDD"])._SolveDD.apply(f, Qc, Qs, sf, cb, sb, ps)[1]
_, tT_F = torch.func.jvp(g_ddF_T, Tp, Tdot); _, tT_64 = torch.func.jvp(g_64_T, Tp, Tdot)
with torch.no_grad():
    h = 1e-4
    Tpp = tabs(c_l.detach() + h); Tmm = tabs(c_l.detach() - h)
    DT_ = (g_dd_T(*Tpp) - g_dd_T(*Tmm)) / (2 * h)
out["tangent_tables_rel_diff_F_vs_fp64"] = dict(all=float((tT_F - tT_64).norm() / tT_64.norm()), anchors=float((tT_F[:, anc] - tT_64[:, anc]).norm() / tT_64[:, anc].norm()))
out["tangent_tables_F_vs_centered_difference(h1e-4)"] = dict(all=float((tT_F - DT_).norm() / DT_.norm()), anchors=float((tT_F[:, anc] - DT_[:, anc]).norm() / DT_[:, anc].norm()))
# (3) vmap over jvp in f
E = torch.stack([fd, torch.roll(fd, 1, dims=1)], 0)
try:
    tv = torch.func.vmap(lambda ee: torch.func.jvp(g_dd, (f,), (ee,))[1])(E)
    out["vmap_jvp"] = dict(ok=True, rel_diff_first=float((tv[0] - t_dd).norm() / t_dd.norm()))
except Exception as ex:
    out["vmap_jvp"] = dict(ok=False, error=repr(ex)[:300])
# (4) reverse mode
fg = f.detach().clone().requires_grad_(True); w = torch.randn_like(g_64(f))
l_dd = (ps.solve_dd(fg)[1] * w).sum(); g1, = torch.autograd.grad(l_dd, fg)
fg2 = f.detach().clone().requires_grad_(True); l64 = (ps._solve_fp64(fg2)[1] * w).sum(); g2, = torch.autograd.grad(l64, fg2)
out["reverse_mode_rel_diff"] = float((g1 - g2).norm() / g2.norm())
# cost under jvp
(torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); torch.func.jvp(g_dd, (f,), (fd,)); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_jvp_dd"] = time.time() - t0
t0 = time.time(); torch.func.jvp(g_64, (f,), (fd,)); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_jvp_fp64"] = time.time() - t0
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(ROOT, "validation", "test_solve_dd_function.json"), "w"), indent=1)
