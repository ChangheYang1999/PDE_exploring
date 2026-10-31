#!/usr/bin/env python
"""D6FP G8 (i) follow-up (lead note 2026-10-28T22:31Z items 3 and 4): (a) table-level test of SPEC v1.4 G8: the jvp of the pressure tables
(Qc, Qs, wr, mom1, sfac, cosb, sinb) with respect to c_l and omega against five-point differences of the tables at fixed layout, and the
omitting copy (tables frozen) failing it; (b) the size of the kernel-table parameter dependence in the parameter columns (|Jp - Jp_frozen| /
|Jp| per group) on S01 at the production layout and at a refined pressure layout (nq 64 and twice the panel count); (c) the production
discrete l = 0, 1 moments of the source and of the c_l- and omega-derivative sources at the production and the refined layout.
Writes validation/g8_tables_<tag>.json."""
import sys, os, time, json, math, argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, PAIRS, ROOT
from src.optimization.lm import param_columns
from src.pressure.poisson_sh import PressureSolver
from src.equations.fields import alpha_of
from src.equations import residuals as res


def table_jvp_test(ps, c_l, omega, dev):
    out = {}
    cl_t = torch.tensor(c_l, device=dev); om_t = torch.tensor(omega, device=dev)
    keys = ("Qc", "Qs", "wr", "mom1_0", "mom1_c", "mom1_s", "sfac", "cosb", "sinb")
    def flat(T):
        return torch.cat([T[k].reshape(-1) for k in keys])
    f = lambda c, w: flat(ps.build_tables(c, w))
    for name, e in (("c_l", (torch.ones((), device=dev), torch.zeros((), device=dev))), ("omega", (torch.zeros((), device=dev), torch.ones((), device=dev)))):
        val, tan = torch.func.jvp(f, (cl_t, om_t), e)
        errs = {}
        for h in (1e-3, 1e-4, 1e-5, 1e-6):
            hc, hw = h * e[0], h * e[1]
            D4 = (8 * (f(cl_t + hc, om_t + hw) - f(cl_t - hc, om_t - hw)) - (f(cl_t + 2 * hc, om_t + 2 * hw) - f(cl_t - 2 * hc, om_t - 2 * hw))) / (12 * h)
            errs[f"{h:.0e}"] = float((tan - D4).norm() / max(float(D4.norm()), 1e-300))
        frozen_err = float((torch.zeros_like(tan) - tan).norm() / max(float(tan.norm()), 1e-300))     # the omitting copy: zero tangent
        out[name] = dict(jvp_vs_five_point=errs, tangent_norm=float(tan.norm()), table_norm=float(val.norm()), omitting_copy_error=frozen_err, PASS=min(errs.values()) <= 1e-6, omitting_copy_fails=frozen_err > 1e-4)
    return out


def moments(ps, f, dev):
    T = ps.tables
    flm = ps.analyze(f); ftw = ps.to_twisted_frame(flm) * T["sfac"][:, None] * ps.lfac
    Phi = ps.q["Phi"]; sg = ps.q["s2"].sqrt(); w = ps.q["w"]; logss = ps.q["logss"]
    fq = Phi @ ftw
    out = {}
    for l in (0, 1):
        for i, (ll, m_, t) in enumerate(ps.pmodes):
            if ll != l:
                continue
            le = float(ps.le_l[l]); fac = torch.exp(-T["p0"] * logss + le * (torch.log(sg) - torch.log((sg ** 2 + ps.R0 ** 2).sqrt())))
            integrand = fq[:, i] * fac * sg ** (l + 2) * w
            M = float(integrand.sum()); A = float(integrand.abs().sum())
            out[str((ll, m_, t))] = dict(M_disc=M, int_abs=A, ratio=M / max(A, 1e-300))
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--tag", required=True); ap.add_argument("--case", default="S01_own")
    a = ap.parse_args(); dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
    defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "manu_a": dict(pair=PAIRS["a"], seed=3), "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"))}
    case = Case(a.case, dev, **defs[a.case]); prob, model = case.prob, case.model
    c_l, omega = case.pair; zp = case.z_phys; n = zp.numel()
    out = dict(case=a.case, pair=case.pair, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    # (a) table-level jvp test at the production layout
    out["table_level_jvp_vs_FD"] = table_jvp_test(prob.pressure, c_l, omega, dev)
    print("table-level:", json.dumps({k: (v["PASS"], v["omitting_copy_fails"], {h: f"{e:.1e}" for h, e in v["jvp_vs_five_point"].items()}) for k, v in out["table_level_jvp_vs_FD"].items()}), flush=True)
    # (b) kernel-dependence size per group at the production layout and a refined layout
    groups_pde = torch.where(model.r <= 0.1 * model.R0, 0, torch.where(model.r <= 2.0 ** 8 * model.R0, 1, 2))
    Nr, Na = model.Nr, model.Na
    def per_group(colA, colB):
        d = {}
        rows = torch.arange(3 * Nr * Na, device=dev); node = (rows // Na) % Nr; g = groups_pde[node]
        for gi, gname in enumerate(case.group_names[:3]):
            m = g == gi
            d[gname] = float((colA[:3 * Nr * Na][m] - colB[:3 * Nr * Na][m]).norm() / max(float(colA[:3 * Nr * Na][m].norm()), 1e-300))
        d["all"] = float((colA - colB).norm() / max(float(colA.norm()), 1e-300))
        return d
    results = {}
    F = model.fields_grid(case.z_full, need_vort=False); src = res.pressure_source(F["GU"])
    for layout_name, ps in (("production(nq32)", prob.pressure), ("refined(nq64, panels x2)", PressureSolver(model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l, nq=64, kappa_margin=4.0, alpha_margin=0.7))):
        prob.pressure = ps
        pf = lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=True)
        pz = lambda q: prob.residual_vector(case.to_full_phys(q), differentiable_pressure=False)
        Jp = param_columns(pf, zp, [n - 2, n - 1]); Jz = param_columns(pz, zp, [n - 2, n - 1])
        r = {"n_quad": ps.n_quad, "kernel_dependence_rel_norm": {pn: per_group(Jp[:, j], Jz[:, j]) for j, pn in enumerate(("c_l", "omega"))}}
        # pressure at the far anchors and the moments
        P, gradP, _, _ = ps.solve(src)
        r["gradP_far_anchor_norms"] = [float(gradP[:, k].norm()) for k in range(model.Nr_src, model.Nr)]
        mom = {"source": moments(ps, src, dev)}
        for j, pn in enumerate(("c_l", "omega")):
            def src_of(q):
                FF = model.fields_grid(case.to_full_phys(q), need_vort=False); return res.pressure_source(FF["GU"])
            e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
            fp = torch.func.jvp(src_of, (zp,), (e,))[1]
            mom[f"d_source/d{pn}"] = moments(ps, fp, dev)
        r["discrete_moments_l0_l1"] = mom
        results[layout_name] = r
        print(f"{layout_name}: n_quad {ps.n_quad}; kernel dependence per group: " + json.dumps({pn: {g: f'{v:.1e}' for g, v in d.items()} for pn, d in r['kernel_dependence_rel_norm'].items()}), flush=True)
        print("   moments (ratio M/int|.|): " + json.dumps({k: {q: f"{v['ratio']:.1e}" for q, v in mm.items()} for k, mm in mom.items()}), flush=True)
    prob.pressure = PressureSolver(model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l)   # restore
    # the difference of the far-anchor pressure gradient between the two layouts (systematic discretization error estimate)
    P1, g1, _, _ = PressureSolver(model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l).solve(src)
    P2, g2, _, _ = PressureSolver(model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l, nq=64, kappa_margin=4.0).solve(src)
    results["gradP_layout_difference_rel_per_node_group"] = {case.group_names[gi]: float((g1[:, groups_pde == gi] - g2[:, groups_pde == gi]).norm() / max(float(g1[:, groups_pde == gi].norm()), 1e-300)) for gi in range(3)}
    results["gradP_layout_difference_far_anchors"] = [float((g1[:, k] - g2[:, k]).norm() / max(float(g1[:, k].norm()), 1e-300)) for k in range(model.Nr_src, model.Nr)]
    alpha = alpha_of(c_l); results["amplification_r_pow_2alpha_minus_1_at_anchors"] = [float((rr / model.R0) ** (2 * alpha - 1)) for rr in model.r[model.Nr_src:].tolist()]
    out["layouts"] = results
    print("gradP layout difference per group:", results["gradP_layout_difference_rel_per_node_group"], "far anchors:", results["gradP_layout_difference_far_anchors"], flush=True)
    json.dump(out, open(os.path.join(ROOT, "validation", f"g8_tables_{a.tag}.json"), "w"), indent=1, default=str)
    print("G8 TABLES DONE")


if __name__ == "__main__":
    main()
