#!/usr/bin/env python
"""SPEC v1.19 3.6 (l), scope test (lead 09:32:45Z item 1 (b)): base-point sensitivity of the residual rows to float64 rounding of one table class
at a time. No (l) difference is formed. For each class, one-ulp perturbations with independent random signs are
injected into the float64 table at the base point, and the change of the rows is recorded in every group of 3.0 (c) and the far-anchor block,
over N draws (default 4). Amended by the lead at 09:38:35Z (after V227): every entry of the class is moved by ONE UNIT IN THE LAST PLACE with an independent random sign
(torch.nextafter towards +inf or -inf), at least twice the largest rounding error of a correctly rounded entry (strict side); the norm of the
injected perturbation is recorded for every class and draw; a class with a zero recorded perturbation has no screen result and stays double-double. A class may stay float64 only if its largest change in every group is below 1e-2 of that group's registered noise
level, the smallest value over the five registered steps of ||D_h - d|| 2h in the failing record (J_cw column; S01_shift_a z_c, S05_shift_c z_c
and physical c_l). Usage: python validation/l_sensitivity.py <case> <record.json> <column label> [draws] [device]
Writes validation/l_sensitivity_<case>.json. Classes: B[l] (rb.matrices), twist (rb.twist_tables), row_scales (scale_mom, scale_vort),
pressure_tables (PressureSolver.build_tables), tail_rows (gauge_residuals), tail_reduction (TailConstraints.expand, coefficients only),
closure_rows (Problem.closure_rows). The far-row scaling (1 + rho/R0^2)^(1/(2 c_l)), formed inline in residual_vector, is perturbed as its own class through a test-only copy of
residual_vector (same statements; verified bitwise against the production function at the base point), lead 09:39:59Z item 2."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT
import src.optimization.problem as problem_mod

EPS = 2.0 ** -53
CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
              "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
              "S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"))}


def noise_levels(record_path, case_name, col_label, jac="G1_Jcw_param_columns"):
    """Per group: min over the five registered steps of ||D_h - d|| 2h, with ||D_h - d|| = e max(||d||, ||D_h||, F) from the record; also the
    column's step scale (h is the registered step times the step scale)."""
    d = json.load(open(record_path)); rec = d["cases"][case_name][jac][col_label]
    sc = float(rec.get("step_scale", 1.0)); out = {}
    for hlab, pg in rec["per_group"].items():
        h = float(hlab) * sc
        for g, e in pg["second_order"].items():
            nd = pg["norm_d"].get(g); nf = (pg.get("norm_fd") or {}).get(g); fl = (pg.get("floor") or {}).get(g) or 0.0
            if e is None or nd is None:
                continue
            diff = float(e) * max(float(nd), float(nf or 0.0), float(fl))
            val = diff * 2.0 * h
            out[g] = min(out.get(g, float("inf")), val)
    return out, sc


def main():
    cname, rec_path, col = sys.argv[1], sys.argv[2], sys.argv[3]
    draws = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    dev = sys.argv[5] if len(sys.argv) > 5 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    problem_mod.TABLE_CACHE = False                                        # every evaluation rebuilds its tables (no cache hits on perturbed tables)
    t0 = time.time()
    case = Case(cname, dev, **CASE_TABLE[cname]); prob, model = case.prob, case.model
    zp = case.z_phys.detach().clone()
    def groups_of(vec):
        out = {"all": float(vec.norm())}
        for gi, gname in enumerate(case.group_names):
            m = case.row_group == gi; out[gname] = float(vec[m].norm())
        if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
            out["far_anchor_block"] = float(vec[case.anchor_mask].norm())
        return out
    import math as _math
    from src.equations import residuals as res
    hooks = dict(far_scaling=None)
    def residual_vector_copy(z, tables):
        """Test-only copy of Problem.residual_vector (same statements, same order) with a hook on the inline far-row scaling
        (1 + rho/R0^2)^(1/(2 c_l)); verified bitwise against the production function at the base point (r0 vs r0_copy below)."""
        model_ = prob.model
        aT, aS, c_l, omega = model_.unpack(z)
        ev = prob.evaluate(z, tables=tables)
        w_mom = prob.nl_w_mom; w_vort = prob.nl_w_vort
        wn = (prob.w_node[:, None] * prob.w_ang[None, :]).sqrt()
        parts = []
        if prob.formulation in ("mom", "both"):
            sc = prob.scale_mom(c_l)
            if prob.nl_weighting and w_mom is not None:
                sc = sc * w_mom.sqrt()
            parts.append((ev['R_u'] * (wn * sc[:, None])[None]).reshape(-1))
        if prob.formulation in ("vort", "both"):
            w = prob.both_weight if prob.formulation == "both" else 1.0
            sc = prob.scale_vort(c_l)
            if prob.nl_weighting and w_vort is not None:
                sc = sc * w_vort.sqrt()
            parts.append((w * ev['R_Om'] * (wn * sc[:, None])[None]).reshape(-1))
        if prob.far_model is not None:
            Ff = prob.far_model.fields_grid(z, need_vort=True)
            Rf = res.vorticity_terms(Ff)['sum']
            scf = (1 + prob.far_model.rho / prob.model.R0 ** 2) ** (1 / (2 * c_l))
            if hooks["far_scaling"] is not None:
                scf = hooks["far_scaling"](scf)
            wf = (prob.far_weight / (prob.n_shells + len(prob.far_radii))) * torch.ones_like(scf)
            wnf = (wf[:, None] * (prob.far_model.grid.w / (4 * _math.pi))[None, :]).sqrt()
            parts.append((Rf * (wnf * scf[:, None])[None]).reshape(-1))
        cr = prob.closure_rows(z, closure=None)
        if cr is not None:
            parts.append(cr)
        rl = prob.radial_lambda_rows(ev, c_l) if prob.radial_lambda_w > 0 else None
        if rl is not None:
            parts.append(rl)
        parts.append(prob.gauge_residuals(aT, aS, c_l, omega, F=ev['F'], z=z, include_sigmaZ=True, tables=tables))
        return torch.cat(parts)
    def resid():
        with torch.no_grad():
            zf = case.to_full_phys(zp)
            tabs = prob.pressure_tables_at(zf, differentiable=False)
            return residual_vector_copy(zf, tabs).detach().clone()
    r0 = resid(); r0b = resid()
    repro = float((r0 - r0b).norm())
    with torch.no_grad():
        r_prod = prob.residual_vector_rebuild(case.to_full_phys(zp)).detach().clone()
    copy_vs_production = float((r0 - r_prod).norm()); copy_bitwise = bool(torch.equal(r0, r_prod))
    print("test-only residual copy vs production residual_vector_rebuild: bitwise", copy_bitwise, "norm diff", copy_vs_production, flush=True)
    base_norms = groups_of(r0)
    nl, sc = noise_levels(rec_path, cname, col)
    gen = torch.Generator(device="cpu")
    realized = []                                                            # lead 09:38:35Z (after V227): one unit in the last place with an independent random sign
    def pert(t, seed):
        gen.manual_seed(seed)
        sign = (torch.rand(t.shape, generator=gen, dtype=t.dtype) < 0.5).to(t.device)
        up = torch.nextafter(t, torch.full_like(t, float("inf"))); dn = torch.nextafter(t, torch.full_like(t, float("-inf")))
        tp = torch.where(sign, up, dn)
        real = tp - t                                                        # exact (difference of neighbours)
        nt = float(t.norm())
        realized.append(dict(shape=list(t.shape), norm_injected=float(real.norm()), rel_norm=(float(real.norm()) / nt if nt > 0 else 0.0), frac_moved=float((real != 0).double().mean())))
        return tp
    results = {}
    seed0 = 1000
    # class definitions: (name, install(seed) -> restore())
    rb = model.rb; orig_matrices = rb.matrices; orig_twist = rb.twist_tables
    orig_scale_mom = prob.scale_mom; orig_scale_vort = prob.scale_vort
    orig_build = prob.pressure.build_tables; orig_build_fine = prob.fine_ps.build_tables if getattr(prob, "fine_ps", None) is not None else None
    orig_gauge = prob.gauge_residuals; orig_closure = prob.closure_rows; orig_expand = case.tc.expand
    npar = 2
    def cls_B(seed):
        cnt = [0]
        def m(*a, **k):
            cnt[0] += 1; return pert(orig_matrices(*a, **k), seed + 97 * cnt[0])
        rb.matrices = m
        return lambda: setattr(rb, "matrices", orig_matrices)
    def cls_twist(seed):
        cnt = [0]
        def tw(*a, **k):
            cnt[0] += 1; C, S = orig_twist(*a, **k); return pert(C, seed + 11 * cnt[0]), pert(S, seed + 13 * cnt[0])
        rb.twist_tables = tw
        return lambda: setattr(rb, "twist_tables", orig_twist)
    def cls_scales(seed):
        prob.scale_mom = lambda c: pert(orig_scale_mom(c), seed + 1); prob.scale_vort = lambda c: pert(orig_scale_vort(c), seed + 2)
        def restore():
            prob.scale_mom = orig_scale_mom; prob.scale_vort = orig_scale_vort
        return restore
    def cls_pressure(seed):
        cnt = [0]
        def wrap(orig):
            def b(*a, **k):
                cnt[0] += 1; T = orig(*a, **k)
                return {kk: (pert(v, seed + 31 * cnt[0] + i) if (torch.is_tensor(v) and v.dim() > 0) else v) for i, (kk, v) in enumerate(T.items())}
            return b
        prob.pressure.build_tables = wrap(orig_build)
        if orig_build_fine is not None:
            prob.fine_ps.build_tables = wrap(orig_build_fine)
        def restore():
            prob.pressure.build_tables = orig_build
            if orig_build_fine is not None:
                prob.fine_ps.build_tables = orig_build_fine
        return restore
    def cls_tail_rows(seed):
        prob.gauge_residuals = lambda *a, **k: pert(orig_gauge(*a, **k), seed + 5)
        return lambda: setattr(prob, "gauge_residuals", orig_gauge)
    def cls_tail_reduction(seed):
        def ex(z):
            full = orig_expand(z); p = pert(full, seed + 7); p = torch.cat([p[:-npar], full[-npar:]])     # parameters unperturbed
            return p
        case.tc.expand = ex
        return lambda: setattr(case.tc, "expand", orig_expand)
    def cls_closure(seed):
        def cr(*a, **k):
            out = orig_closure(*a, **k); return None if out is None else pert(out, seed + 9)
        prob.closure_rows = cr
        return lambda: setattr(prob, "closure_rows", orig_closure)
    def cls_far_scaling(seed):
        hooks["far_scaling"] = lambda t: pert(t, seed + 17)
        def restore():
            hooks["far_scaling"] = None
        return restore
    classes = [("B[l]", cls_B), ("twist", cls_twist), ("row_scales", cls_scales), ("far_row_scaling", cls_far_scaling), ("pressure_tables", cls_pressure),
               ("tail_rows", cls_tail_rows), ("tail_reduction", cls_tail_reduction), ("closure_rows", cls_closure)]
    for name, installer in classes:
        per_draw = []; realized_class = []
        for dnum in range(draws):
            del realized[:]
            restore = installer(seed0 + 1000 * dnum)
            try:
                r = resid()
            finally:
                restore()
            per_draw.append(groups_of(r - r0)); realized_class.append(list(realized))
        maxes = {g: max(pd[g] for pd in per_draw) for g in per_draw[0]}
        verdict = {}
        for g, mx in maxes.items():
            nlev = nl.get(g)
            verdict[g] = dict(max_change=mx, noise_level=nlev, ratio=(mx / nlev if nlev else None), may_stay_float64=(bool(mx < 1e-2 * nlev) if nlev else None))
        inj = [sum(x["norm_injected"] for x in d_) for d_ in realized_class]
        screen_valid = all(v > 0 for v in inj) and len(inj) == draws
        results[name] = dict(per_draw=per_draw, max_change=maxes, verdict=verdict, realized_perturbations=realized_class, injected_norm_per_draw=inj, screen_valid=screen_valid,
                             class_may_stay_float64=(screen_valid and all(v["may_stay_float64"] for g, v in verdict.items() if v["may_stay_float64"] is not None and g != "all")))
        print(f"{name:16s} far_anchor_block max {maxes.get('far_anchor_block', float('nan')):.3e} vs 1e-2 noise {1e-2 * nl.get('far_anchor_block', float('nan')):.3e} -> {'float64 ok' if results[name]['class_may_stay_float64'] else ('DOUBLE-DOUBLE NEEDED' if results[name]['screen_valid'] else 'NO SCREEN RESULT (zero injected perturbation): double-double')}; injected {min(inj):.2e}; "
              + "; ".join(f"{g}: {maxes[g]:.2e}/{nl.get(g, float('nan')):.2e}" for g in maxes if g not in ('all', 'far_anchor_block')), flush=True)
    out = dict(case=cname, pair=case.pair, cost=case.cost, record=rec_path, column=col, step_scale=sc, eps=EPS, draws=draws, device=dev,
               base_reproducibility_norm=repro, copy_vs_production_norm=copy_vs_production, copy_bitwise_equal=copy_bitwise, base_group_norms=base_norms, noise_levels=nl, classes=results, seconds=time.time() - t0,
               rule="lead 09:32:45Z item 1 (b) amended 09:38:35Z: one-ulp random-sign perturbation of every entry of the class; a class may stay float64 only if its largest change in every group over the draws is below 1e-2 of the group's noise level (min over the five registered steps of ||D_h - d|| 2h from the failing J_cw record, V227); zero injected perturbation = no screen result; empirical evidence over the draws, not a bound",
               ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    json.dump(out, open(os.path.join(ROOT, "validation", f"l_sensitivity_{cname}.json"), "w"), indent=1)
    print("DONE", cname, f"{time.time() - t0:.0f}s", "base reproducibility", repro)


if __name__ == "__main__":
    main()
