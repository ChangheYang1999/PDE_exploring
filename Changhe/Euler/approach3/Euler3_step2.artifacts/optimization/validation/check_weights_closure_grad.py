"""D6FP: isolate the two differentiated ingredients of the complete gradient: (a) the nonlinear shell weights w(z) (nl_weights_from_ev, forward and
reverse mode) against central differences along z_c, z_w and a coefficient direction; (b) the closure target G_req(z) (first_correction_graph) VJP
against differences of v . G_req(z). Also the smoothness of O1 along z_c: O1 at steps 0, +-1e-6 ... +-1e-3 with the active set at each point."""
import sys, os, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.far_field.correction import first_correction_graph, first_correction
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01_own", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"))
prob, model = case.prob, case.model
zo = case.z_opt; n = zo.numel()
def weights_of(q):
    zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
    return prob.nl_weights_from_ev(ev, differentiable=True)[0]
rng = np.random.default_rng(3)
dirs = {"e_zc": None, "e_zw": None, "coef": None}
for name in dirs:
    e = torch.zeros_like(zo)
    if name == "e_zc": e[-2] = 1.0
    elif name == "e_zw": e[-1] = 1.0
    else:
        e[:-2] = torch.tensor(rng.normal(size=n - 2), device=dev); e = e / e.norm()
    jv = torch.func.jvp(weights_of, (zo,), (e,))[1]
    zz = zo.detach().clone().requires_grad_(True); w = weights_of(zz); v = torch.randn(w.numel(), device=dev)
    g, = torch.autograd.grad((w * v).sum(), zz)
    line = f"weights along {name}: |jvp| {float(jv.norm()):.3e}; "
    for h in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
        with torch.no_grad():
            d = (weights_of(zo + h * e) - weights_of(zo - h * e)) / (2 * h)
        line += f"h {h:.0e}: FD-jvp rel {float((d - jv).norm() / max(float(d.norm()), 1e-300)):.1e}, (v.FD - v.g)/|v.FD| {abs(float(v @ d) - float(g @ e)) / max(abs(float(v @ d)), 1e-300):.1e} | "
    print(line, flush=True)
    # active sets along the direction
    acts = []
    for t in (-1e-3, -1e-4, -1e-5, 0.0, 1e-5, 1e-4, 1e-3):
        zz = case.to_full_opt(zo + t * e); ev = prob.evaluate(zz, tables=prob.pressure_tables_at(zz))
        a = prob.nl_active_set(ev); acts.append((t, a["median_shell"], a["clamped_shells"]))
    print("   active sets (t, median shell, clamped):", acts, flush=True)
# closure target
def Greq(q):
    fc = first_correction_graph(prob, case.to_full_opt(q), ntheta=prob.closure["grid"].ntheta, nphi=prob.closure["grid"].nphi); return fc["G"].reshape(-1)
fc0 = first_correction(prob, case.z_full); G0 = fc0["G"].reshape(-1)
print(f"first_correction_graph vs frozen first_correction: max rel diff {float((Greq(zo).detach() - G0).abs().max() / G0.abs().max()):.2e}")
v = torch.randn(G0.numel(), device=dev)
zz = zo.detach().clone().requires_grad_(True); g, = torch.autograd.grad((Greq(zz) * v).sum(), zz)
for name in ("e_zc", "e_zw", "coef"):
    e = torch.zeros_like(zo)
    if name == "e_zc": e[-2] = 1.0
    elif name == "e_zw": e[-1] = 1.0
    else:
        e[:-2] = torch.tensor(rng.normal(size=n - 2), device=dev); e = e / e.norm()
    line = f"G_req VJP along {name}: v.g.e {float(g @ e):+.6e}; "
    for h in (1e-3, 1e-4, 1e-5, 1e-6):
        d = (float(v @ Greq(zo + h * e).detach()) - float(v @ Greq(zo - h * e).detach())) / (2 * h)
        line += f"h {h:.0e}: FD {d:+.6e} rel {abs(d - float(g @ e)) / max(abs(d), 1e-300):.1e} | "
    print(line, flush=True)
# O1 profile along z_c and z_w
for k, name in ((-2, "z_c"), (-1, "z_w")):
    e = torch.zeros_like(zo); e[k] = 1.0
    vals = []
    for t in (-1e-3, -3e-4, -1e-4, -3e-5, -1e-5, 0.0, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3):
        r, _ = prob.objective_at(case.to_full_opt(zo + t * e), need_aux=False); vals.append((t, 0.5 * float(r @ r)))
    O0 = vals[5][1]
    print(f"O1 profile along {name}: " + ", ".join(f"{t:+.0e}: {(o - O0) / O0:+.3e}" for t, o in vals), flush=True)
