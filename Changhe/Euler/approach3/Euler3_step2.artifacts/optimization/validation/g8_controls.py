#!/usr/bin/env python
"""D6FP G8 negative controls (SPEC 3.2 G8): in a test-only copy (monkeypatched second instance) omit one parameter dependence at a time and
re-run the G1 parameter-column test (S01 at its own parameters and the (0.42, 0.3) manufactured field, physical coordinates):
 (i) kernel-table parameter dependence, (ii) dE/dp of the tail-constraint expansion, (iii) parameter dependence of the far rows (merged far
anchor nodes: momentum rows at 4096, 16384, 65536 R0), (iv) parameter dependence of the gauge rows, (v) the pressure term of the parameter
columns. Expected: G1 fails (error >= 100 tau = 1e-4) where the omitted dependence is excited; otherwise the size of the omitted part is
reported with the reason. Writes validation/g8_controls.json."""
import sys, os, json, time, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, PAIRS, column_test, ROOT
from src.optimization.lm import param_columns
from src.optimization import tail_constraints as tcmod
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
out = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), controls={}, tau=1e-6, fail_level=1e-4)
hs = [1e-4, 1e-5, 1e-6]
cases = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "manu_a": dict(pair=PAIRS["a"], seed=3)}
for cname, cdef in cases.items():
    case = Case(cname, dev, **cdef); prob, model, tc = case.prob, case.model, case.tc
    n = case.z_phys.numel(); zp = case.z_phys
    frozen_fun = lambda q: prob.residual_vector_rebuild(case.to_full_phys(q))
    res_c = {}
    pfun = lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=True)
    Jp_ok = param_columns(pfun, zp, [n - 2, n - 1])
    def run_control(name, col_fun, excited_note):
        Jp = col_fun()
        r = {}
        for j, pname in enumerate(("c_l", "omega")):
            e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
            scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
            t = column_test(case, f"G8 {name} {pname}", Jp[:, j], frozen_fun, zp, e, hs, ref=case.r, scale=scale, deriv_scale=1.0)   # v5 (V190): physical omega judged in physical units
            omitted_rel = float((Jp[:, j] - Jp_ok[:, j]).norm() / Jp_ok[:, j].norm())
            omitted_per_group = {}                                            # lead 06:23Z: the omitted part's norm per group and block, relative to the column
            for gi, gname in enumerate(case.group_names):
                m = case.row_group == gi; omitted_per_group[gname] = dict(norm_omitted=float((Jp[m, j] - Jp_ok[m, j]).norm()), norm_column_group=float(Jp_ok[m, j].norm()), rel_to_column=float((Jp[m, j] - Jp_ok[m, j]).norm() / Jp_ok[:, j].norm()))
            if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
                m = case.anchor_mask; omitted_per_group["far_anchor_block"] = dict(norm_omitted=float((Jp[m, j] - Jp_ok[m, j]).norm()), norm_column_group=float(Jp_ok[m, j].norm()), rel_to_column=float((Jp[m, j] - Jp_ok[m, j]).norm() / Jp_ok[:, j].norm()))
            gmin = {g: min(h["second_order"][g] for h in t["per_group"].values()) for g in t["per_group"]["1e-04"]["second_order"]}
            r[pname] = dict(min_error_all=t["pass_rule"]["min_e"], per_group_min=gmin, omitted_part_rel_norm=omitted_rel, per_group=t["per_group"], group_pass=t["group_pass"], column_norm=t["column_norm"], omitted_part_per_group=omitted_per_group,   # SPEC v1.17 3.6 (j)(2)(v): group norms and the omitted part per group
                            fails_G1=(t["pass_rule"]["min_e"] > 1e-4) or any(v > 1e-3 for g, v in gmin.items() if g != "all"), expected="fail", note=excited_note)
        res_c[name] = r
        print(f"  {cname} {name}: " + json.dumps({k: dict(min_e=f"{v['min_error_all']:.1e}", omitted=f"{v['omitted_part_rel_norm']:.1e}", fails=v['fails_G1'], groups={g: f'{x:.0e}' for g, x in v['per_group_min'].items()}) for k, v in r.items()}), flush=True)
    # (i) kernel tables frozen at the base parameters
    run_control("i_kernel_tables_frozen", lambda: param_columns(lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=False), zp, [n - 2, n - 1]),
                "the exact Green operator is parameter independent; the table dependence is a discretization-level effect")
    # (ii) dE/dp omitted: expansion with detached parameters inside the constraint solve
    orig_expand = tcmod.TailConstraints.expand
    def expand_detached(self, z_red):
        zd = torch.cat([z_red[:-2], z_red[-2:].detach()])
        full = orig_expand(self, zd)
        return torch.cat([full[:-2], z_red[-2:]])
    tcmod.TailConstraints.expand = expand_detached
    run_control("ii_dE_dp_omitted", lambda: param_columns(pfun, zp, [n - 2, n - 1]), "eliminated top Chebyshev coefficients depend on p = (alpha + l)/2 and q = m kappa/2")
    tcmod.TailConstraints.expand = orig_expand
    # (iii) far rows: rows of the far anchor nodes replaced by their values with detached parameters
    nfar = model.Nr - model.Nr_src
    orig_rv = prob.residual_vector
    def rv_far_detached(z, **kw):
        r = orig_rv(z, **kw)
        zd = torch.cat([z[:-2], z[-2:].detach()])
        kw2 = {k: v for k, v in kw.items() if k != "differentiable_pressure"}
        rd = orig_rv(zd, **kw2)
        Nr, Na = model.Nr, model.Na
        rr = r.clone()
        for c in range(3):
            a0 = c * Nr * Na + model.Nr_src * Na; a1 = c * Nr * Na + Nr * Na
            rr[a0:a1] = rd[a0:a1]
        return rr
    prob.residual_vector = rv_far_detached
    run_control("iii_far_rows_param_frozen", lambda: param_columns(pfun, zp, [n - 2, n - 1]), f"{nfar} far anchor nodes (momentum rows with pressure) at 4096, 16384, 65536 R0")
    prob.residual_vector = orig_rv
    # (iv) gauge rows with detached parameters
    orig_gauge = prob.gauge_residuals
    def gauge_detached(aT, aS, c_l, omega=None, **kw):
        return orig_gauge(aT, aS, c_l.detach(), (omega.detach() if omega is not None else None), **kw)
    prob.gauge_residuals = gauge_detached
    run_control("iv_gauge_rows_param_frozen", lambda: param_columns(pfun, zp, [n - 2, n - 1]), "F-gauge norm contains alpha and m omega/c_l")
    prob.gauge_residuals = orig_gauge
    # (v) pressure term omitted from the parameter columns: grad P tangent zeroed (pressure solve on detached source and tables)
    ps = prob.pressure; orig_solve = ps.solve; orig_solve_fp64 = ps._solve_fp64; orig_solve_dd = ps.solve_dd
    def _detach_tables(tables):
        return None if tables is None else {k: (v.detach() if torch.is_tensor(v) else v) for k, v in tables.items()}
    def solve_detached(f, tables=None):
        return orig_solve(f.detach(), tables=_detach_tables(tables))
    def solve_fp64_detached(f, tables=None):                       # the configuration-M float64 Jacobian path (problem.py: evaluate inside functorch) calls _solve_fp64 directly
        return orig_solve_fp64(f.detach(), tables=_detach_tables(tables))
    def solve_dd_detached(f, tables=None):                         # the double-double value path
        fd = (f[0].detach(), f[1].detach()) if isinstance(f, (tuple, list)) else f.detach()
        return orig_solve_dd(fd, tables=_detach_tables(tables))
    ps.solve = solve_detached; ps._solve_fp64 = solve_fp64_detached; ps.solve_dd = solve_dd_detached       # SPEC v1.16 (test-only, 2026-10-29T06:2xZ): under configuration M the first
    run_control("v_pressure_term_omitted", lambda: param_columns(pfun, zp, [n - 2, n - 1]), "grad P_p = full-space pressure of 2 tr(DU DU_p) plus the table dependence")   # record (06:12Z) showed the omitted part 0.0: the patch of solve() alone did not reach the fp64 Jacobian path
    ps.solve = orig_solve; ps._solve_fp64 = orig_solve_fp64; ps.solve_dd = orig_solve_dd
    out["controls"][cname] = res_c
    del case; torch.cuda.empty_cache()
json.dump(out, open(os.path.join(ROOT, "validation", "g8_controls.json"), "w"), indent=1, default=str)
print("G8 DONE")
