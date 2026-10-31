#!/usr/bin/env python
"""G3 single-direction capture (verifier 2026-10-29T14:33:22Z request after V332/V335; lead 14:31:05Z item 4 (a)): regenerate ONE G3 direction of a case with the
original seed and the complete direction-construction sequence of validation/g3_addon.py (seed 11; the 20 coefficient columns are drawn first, then the three
random_scaled draws, then the two mixed draws; scaled by the column norms of the production Jacobian with the parameter columns), and save everything the
seven-step ladder decision used: the base reduced optimizer vector, the exact direction, the FULL residual vector r = objective_at(X + t v) at the base and at
every +-h, +-2h for h in 1e-3 ... 1e-9 (29 points), the original scalar O1 = 0.5 * float(r @ r) and the gauge row at each point, the active set at each point,
the frozen row layout (block slices, row groups), the complete derivative d = g_c . v, J_c v (same method as g3_addon), the recomputed ladder outcomes, the
sha256 of all seven scaled directions (to be compared with G3_direction_hashes.scaled_directions_sha256 of the gates record), the code and start hashes, and
the cost accumulation (torch.dot on the device in float64, the device reduction order; plus two host references: math.fsum of the float64 squares and the
numpy longdouble sum of longdouble squares). Diagnostic only: no estimator, floor, ladder or pass rule changes. Usage:
python validation/g3_direction_capture.py <case> <direction name> [device]   -> validation/g3_capture_<case>_<direction>.json + _arrays.npz"""
import sys, os, time, json, math, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT, code_hashes
from validation.g3_addon import ladder_report, HS7, HS5
from src.optimization.lm import jacobian_fwd, param_columns

DEFS = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")),
        "S11_own": dict(start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")), "S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")),
        "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
        "S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]), "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
        "manu_a": dict(pair=PAIRS["a"], seed=3), "manu_small_omega": dict(pair=PAIRS["small_omega"], seed=5), "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6),
        "manu_near_edge": dict(pair=PAIRS["near_edge"], seed=7), "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all")}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    cname, dname = sys.argv[1], sys.argv[2]
    dev = sys.argv[3] if len(sys.argv) > 3 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    out_json = os.path.join(ROOT, "validation", f"g3_capture_{cname}_{dname}.json"); out_npz = out_json.replace(".json", "_arrays.npz")
    for p in (out_json, out_npz):
        if os.path.exists(p):
            raise FileExistsError(p)
    t0 = time.time()
    case = Case(cname, dev, **DEFS[cname]); prob, model, pm = case.prob, case.model, case.pm
    zo = case.z_opt; n = zo.numel()
    # ---- identical construction sequence to g3_addon.run (seed 11; the column draw is consumed first)
    rng = np.random.default_rng(11)
    cols = sorted(rng.choice(n - 2, size=min(20, n - 2), replace=False).tolist())
    fun = lambda q: prob.residual_vector(case.to_full_opt(q))
    J = jacobian_fwd(fun, zo, chunk=256)
    Jp = param_columns(lambda q: prob.residual_vector(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
    J[:, n - 2] = Jp[:, 0]; J[:, n - 1] = Jp[:, 1]
    colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt(); del J
    zz = zo.detach().clone().requires_grad_(True)
    rr = prob.objective_graph(case.to_full_opt(zz)); c = 0.5 * (rr @ rr); g_c, = torch.autograd.grad(c, zz); g_c = g_c.detach().clone()
    _, parts = prob.complete_gradient(case.to_full_opt(zo).detach(), return_parts=True)
    dsc = pm.describe(zo)
    if parts["pattern_fd"] is not None:
        g_c[-2] += float(parts["pattern_fd"][0]) * dsc["dcl_dzc"]; g_c[-1] += float(parts["pattern_fd"][1]) * dsc["domega_dzw"]
    E = {}
    e = torch.zeros_like(zo); e[n - 2] = 1.0; E["e_zc(optimizer)"] = e
    e = torch.zeros_like(zo); e[n - 1] = 1.0; E["e_zw(optimizer)"] = e
    for i in range(3):
        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm
    for i in range(2):
        u = torch.tensor(rng.normal(size=n), device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm
    dir_hash = hashlib.sha256(b"".join(E[k].detach().cpu().numpy().tobytes() for k in E)).hexdigest()          # gates.py order: e_zc, e_zw, random_scaled_0..2, mixed_0..1
    if dname not in E:
        raise SystemExit(f"direction {dname} is not one of the optimizer-coordinate G3 directions {list(E)}")
    v = E[dname]; to_full = case.to_full_opt; zbase = zo
    dpred = float(g_c @ v)
    blocks = case.block_slices
    def Jc_v(v_):
        def fun_wd(q):
            zz_ = to_full(q); tabs = prob.pressure_tables_at(zz_, differentiable=True); ev = prob.evaluate(zz_, tables=tabs)
            return prob.residual_vector(zz_, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
        col = torch.func.jvp(fun_wd, (zbase,), (v_,))[1].clone()
        if "closure" in blocks:
            a0, a1 = blocks["closure"]; h = 1e-4 / max(float(v_.norm()), 1e-300)
            crow = lambda q: prob.closure_rows(to_full(q), closure=prob.closure_state_at(to_full(q)))
            col[a0:a1] = (8 * (crow(zbase + h * v_) - crow(zbase - h * v_)) - (crow(zbase + 2 * h * v_) - crow(zbase - 2 * h * v_))) / (12 * h)
        return col
    jcv = Jc_v(v); Fl = 1e-3 * float(case.r.norm()) * float(jcv.norm())
    gauge_row = blocks["gauge"][0]
    def act(q):
        zz_ = to_full(q); ev = prob.evaluate(zz_, tables=prob.pressure_tables_at(zz_)); a = prob.nl_active_set(ev); a["geometry"] = prob.pressure.geometry_id; return a
    # ---- the 29 stencil points: full residual vectors, original scalar, gauge row, host references, active sets
    points = [0.0] + [t for h in HS7 for t in (h, -h, 2 * h, -2 * h)]
    arrays = dict(z_base_opt=zo.detach().cpu().numpy(), direction=v.detach().cpu().numpy(), g_c=g_c.cpu().numpy(), Jc_v=jcv.detach().cpu().numpy(), colnorm=colnorm.detach().cpu().numpy(),
                  row_groups=case.row_group.cpu().numpy(), r_base_case=case.r.detach().cpu().numpy())
    vals = {}; gs = {}; acts = {}; host = {}
    for t in points:
        q = zbase + t * v
        r, _ = prob.objective_at(to_full(q), need_aux=False)
        o_dev = 0.5 * float(r @ r)                                                      # the ORIGINAL scalar of g3_addon.O1_and_g (torch.dot on the device, float64)
        vals[t] = o_dev; gs[t] = float(r[gauge_row])
        rn = r.detach().cpu().numpy().astype(np.float64)
        sq64 = rn * rn
        host[f"{t:+.1e}"] = dict(O1_device=o_dev, O1_fsum_of_float64_squares=0.5 * math.fsum(sq64.tolist()), O1_longdouble=float(0.5 * np.sum(rn.astype(np.longdouble) * rn.astype(np.longdouble))),
                                 O1_numpy_pairwise=float(0.5 * np.dot(rn, rn)), r_norm=float(np.sqrt(np.sum(sq64))), gauge=gs[t])
        arrays[f"r_{t:+.1e}"] = rn
        acts[f"{t:+.1e}"] = act(q)
        print(f"  t={t:+.1e}: O1 {o_dev:.17e} fsum {host[f'{t:+.1e}']['O1_fsum_of_float64_squares']:.17e} gauge {gs[t]:.6e}", flush=True)
    base_key = json.dumps(acts["+0.0e+00"], sort_keys=True)
    valid = {h: all(json.dumps(acts[f"{t:+.1e}"], sort_keys=True) == base_key for t in (h, -h, 2 * h, -2 * h)) for h in HS7}
    outc = {}
    for lad_name, lad in (("v1.4_ladder", HS5), ("seven_step_ladder", HS7)):
        for est_name, sub in (("O1", False), ("O_tilde_gauge_subtracted", True)):
            outc[f"{est_name}:{lad_name}"] = ladder_report(vals, gs, dpred, Fl, lad, sub, valid)
    np.savez_compressed(out_npz, **arrays)
    layout = dict(block_slices={k: [int(a), int(b)] for k, (a, b) in blocks.items()}, gauge_row=int(gauge_row), group_names=list(case.group_names), n_rows=int(case.r.numel()), n_opt=int(n),
                  npde=int(prob.w_node.numel() * prob.w_ang.numel() * 3), anchor_rows=(int(case.anchor_mask.sum()) if hasattr(case, "anchor_mask") else None))
    rec = dict(case=cname, direction=dname, pair=case.pair, cost=case.cost, n_opt=int(n), device=str(dev), device_name=(torch.cuda.get_device_name(0) if dev.startswith("cuda") else "cpu"), torch_version=torch.__version__,
               seed=11, construction="validation/g3_addon.run order: rng.choice(n-2, 20) first, then three rng.normal(n) draws (random_scaled_0..2, unit norm then divided by the column norms of J with the parameter columns), then two mixed draws",
               columns_drawn_first=cols, scaled_directions_sha256=dir_hash, scaled_directions_order=list(E), direction_norm=float(v.norm()), direction_sha256=hashlib.sha256(v.detach().cpu().numpy().tobytes()).hexdigest(),
               derivative_complete=dpred, floor=Fl, Jc_v_norm=float(jcv.norm()), Jc_v_method="jvp of the weights-differentiated residual with tables in the graph; closure block by five-point FD of the fresh closure rows along v (h = 1e-4 / |v|)",
               cost_accumulation=dict(original="0.5 * float(r @ r): torch.dot of the float64 residual vector with itself on the device (cuBLAS reduction order on CUDA), then one float64 multiply by 0.5 on the host",
                                      dtype="torch.float64", host_references="O1_fsum_of_float64_squares = 0.5 * math.fsum(r_i * r_i in float64) (exact sum of the rounded squares); O1_longdouble = 0.5 * sum in numpy longdouble of longdouble squares; O1_numpy_pairwise = 0.5 * numpy.dot"),
               points=host, active_sets={k: acts[k] for k in acts}, step_valid={f"{h:.0e}": bool(valid[h]) for h in HS7}, outcomes_recomputed=outc, layout=layout,
               arrays_npz=dict(path=os.path.relpath(out_npz, ROOT), sha256=sha(out_npz), keys=sorted(arrays), note="r_<t> = full residual vector objective_at(X + t v) at the 29 stencil points; z_base_opt; direction; g_c; Jc_v; colnorm; row_groups; r_base_case"),
               start=dict(path=DEFS[cname].get("start"), sha256=(sha(DEFS[cname]["start"]) if DEFS[cname].get("start") else None)), code_sha256=code_hashes(),
               launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None),
               exterior_monopole=bool(prob.exterior_monopole), stable_linear=bool(prob.stable_linear), seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print("recomputed outcomes:", json.dumps({k: (o["PASS"], o["PASS_rel"], o["OPEN"], o["richardson_error"]) for k, o in outc.items()}))
    print("DONE", out_json, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
