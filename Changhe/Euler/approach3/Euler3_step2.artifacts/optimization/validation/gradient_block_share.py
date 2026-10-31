"""D6FP deliverable D (lead 23:30:59Z item 3): contribution of each row block (near origin, core, far momentum rows, far anchors, closure, gauge)
to the two parameter components of the complete gradient, g_p = sum_blocks r_B . (J_c)_B e_p, for S01_own, S05_own and the V027 input, in
optimizer coordinates (z_c, z_w) and physical (c_l, omega) through the chain factors. The J_c parameter columns are the production J_cw columns
(weights and pressure tables differentiated, forward mode) with the closure block replaced by five-point differences of the fresh closure rows
(target and patterns refreshed), as in gates.py jc_param_column. Also the fraction of |g_p| carried by the far-anchor block (report if > 1 per cent).
Output validation/gradient_block_share.json."""
import sys, os, json, time
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
def jc_param_columns(case):
    prob = case.prob; zo = case.z_opt; n = zo.numel(); to_full = case.to_full_opt
    def fun_wd(q):
        zz = to_full(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
        return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
    cols = []
    for j in range(2):
        e = torch.zeros_like(zo); e[n - 2 + j] = 1.0
        col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
        if "closure" in case.block_slices:
            a0, a1 = case.block_slices["closure"]
            def crow(q):
                zz = to_full(q); return prob.closure_rows(zz, closure=prob.closure_state_at(zz))
            h = 1e-4
            col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
        cols.append(col)
    return torch.stack(cols, 1)
def blocks_of(case):
    blk = {}
    for i, nm in enumerate(case.group_names):
        m = case.row_group == i
        if nm.startswith("far(") and hasattr(case, "anchor_mask"):
            m = m & ~case.anchor_mask
        if m.any():
            blk[nm] = m
    blk["far_anchor_block"] = case.anchor_mask
    return blk
def share(case):
    J = jc_param_columns(case); r = case.r; d = case.pm.describe(case.z_opt); chain = (d["dcl_dzc"], d["domega_dzw"])
    g = (r @ J).tolist()
    out = dict(g_opt=dict(z_c=g[0], z_w=g[1]), g_phys=dict(c_l=g[0] / chain[0], omega=g[1] / chain[1]), chain=dict(dcl_dzc=chain[0], domega_dzw=chain[1]), blocks={})
    for nm, m in blocks_of(case).items():
        gb = (r[m] @ J[m]).tolist()
        out["blocks"][nm] = dict(z_c=gb[0], z_w=gb[1], share_z_c=abs(gb[0]) / max(abs(g[0]), 1e-300), share_z_w=abs(gb[1]) / max(abs(g[1]), 1e-300), n_rows=int(m.sum()))
    out["far_anchor_share_above_1pct"] = bool(out["blocks"]["far_anchor_block"]["share_z_c"] > 0.01 or out["blocks"]["far_anchor_block"]["share_z_w"] > 0.01)
    return out
res = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), cases={})
for name, kw in (("S01_own", dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"))), ("S05_own", dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")))):
    case = Case(name, dev, **kw); res["cases"][name] = share(case)
    print(name, json.dumps({k: (f"{v['share_z_c']:.3e}", f"{v['share_z_w']:.3e}") for k, v in res["cases"][name]["blocks"].items()}), "g_opt", res["cases"][name]["g_opt"], flush=True)
    del case; torch.cuda.empty_cache()
inp = "RUN_ROOT/verifier/artifacts/inputs/manufactured_geometric_even"
d = np.load(os.path.join(inp, "coeffs.npz"), allow_pickle=True); T = lambda a: torch.tensor(np.asarray(a, dtype=float))
arrays = dict(A=T(d["A"]), C=T(d["C"]), B=T(d["B"]), D=T(d["D"]), E=T(d["E"]), channels=json.loads(str(d["channels"])), m_parity=str(d["m_parity"]), R0=float(d["R0"]), Nk=int(d["Nk"]), Nr=48, desc="V027 input")
case = Case("V027_input", dev, arrays=arrays, pair=(0.42, 0.3), align=False, grid=(20, 38)); res["cases"]["V027_input"] = share(case)
print("V027_input", json.dumps({k: (f"{v['share_z_c']:.3e}", f"{v['share_z_w']:.3e}") for k, v in res["cases"]["V027_input"]["blocks"].items()}), "g_opt", res["cases"]["V027_input"]["g_opt"], flush=True)
res["any_far_anchor_share_above_1pct"] = any(v["far_anchor_share_above_1pct"] for v in res["cases"].values())
json.dump(res, open(os.path.join(MYROOT, "validation", "gradient_block_share.json"), "w"), indent=1)
print("DONE; far-anchor share above 1 per cent anywhere:", res["any_far_anchor_share_above_1pct"])
