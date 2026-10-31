#!/usr/bin/env python
"""SPEC v1.19 3.6 (l) table screen, version 4.5 (numerics 2026-10-29T10:1xZ; 4.5 after V239 and the lead's 10:10:03Z: a recorded table of class/reference combinations inactive by construction, with the single entry
(nonlinear row weights, J_f); there a hook count of zero is required and recorded as 'inactive (weights frozen in J_f)', a nonzero count gives OPEN; every other combination keeps the v4.3 rules; 4.1 accepted by the lead 10:06:18Z: nonlinear-row-weight class; 4.3 = 4.1 plus exactly the four checks of
the lead's 10:04:16Z note: fewer than four draws OPEN, base not bitwise or nonzero difference OPEN, threshold not finite and positive OPEN, exclusive-create output; v3 after V229 and the lead's 09:38:35Z, 09:39:59Z, 09:43:52Z and
09:44:46Z notes; v4 after V232 and the lead's 09:56:02Z note: weighted closure-target norm, tail-reduction hooks acting through a fresh reduced-to-full
conversion inside every evaluation with only the dependent coefficients perturbed, identity controls per class and reference in the record, fail closed
including the whole block, preconditions, non-overwriting output, runtime assertion of the inactive far branch). No (l) difference is formed.

For one failing parameter column (case, column label) and each of the three Jacobian references, the residual is evaluated at the base point
with ONE float64 ingredient class perturbed at a time: every entry of the class moved by one unit in the last place with an independent random
sign (torch.nextafter towards +inf or -inf; the injected norm and the fraction moved are recorded per table and draw; a zero injection gives
no screen result and the class stays double-double). The change of the rows is recorded in every group of 3.0 (c) and the far-anchor block.
References (V229 item 1): J_f = residual_vector_rebuild (weights and closure target frozen); J_cw = residual_vector_rebuild_wd (weights
recomputed, closure target held); J_c = objective_at (self-consistent). Classes perturb parameter-dependent INGREDIENTS before the downstream
arithmetic (V229 item 2): B[l] radial tables (rb.matrices), twist tables (rb.twist_tables), row scales (scale_mom, scale_vort), nonlinear row weights (Problem.nl_weights_from_ev outputs w_mom, w_vort, recomputed in the J_cw and J_c
references and frozen in J_f), pressure kernel tables (every tensor of PressureSolver.build_tables, main and fine), tail amplitudes (Problem.tail_amplitudes: t, s), tail energies
(Problem.mode_tail_energies: eT, eS), enstrophy and stretching (Problem.enstrophy_and_stretching: Z, I; when a Z gauge or Sigma_Z row is active),
closure patterns (carried_patterns V, stored and recomputed), closure target (G_required of closure_state_at / the stored closure, norm recomputed
from the perturbed target), stable-linear envelopes (jets.affine_pow outputs during linear_stable.linear_velocity: the u^(-nu/2) and 1/u jets of
the stable linear operator; its twist tables are covered by the twist class and its Chebyshev jets are parameter-independent), tail-reduction solutions (TailConstraints._solve_pair, _solve_single, _solve_k2 outputs: the dependent coefficients
before packing). The inline far-row scaling of residual_vector is INACTIVE in the production configuration (Problem.far_model is None: the far
anchors are merged nodes scaled by scale_mom) and is recorded as inactive with that evidence.
Decision (lead 09:44:46Z): a class must be carried in double-double if, in any group or row block that FAILS the registered rule on this record,
in any Jacobian, its largest screen change over the draws exceeds 1e-2 of that group's registered noise level (min over the five registered
steps of ||D_h - d|| 2h, from the record; derivative_scale asserted or divided out; V227). Groups that pass the registered rule are recorded but
do not decide. Fail closed (lead 09:43:52Z): a missing threshold, an empty group comparison or a missing whole-column result makes the class
OPEN, and an OPEN class goes to double-double. The 'every group' reading is reported as well. Output: validation/l_screen_<case>_<col>.json
(column-qualified; the record's and this script's sha256 are stored). Usage: python validation/l_screen.py <case> <record.json> <col label> [draws] [device]"""
import sys, os, json, time, hashlib, re, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT
import src.optimization.problem as problem_mod
import src.far_field.correction as corr_mod
import src.bases.jets as jets_mod
import src.equations.linear_stable as linstab_mod

CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
              "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
              "S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"))}
JACS = {"Jf": "G1_Jf_param_columns", "Jcw": "G1_Jcw_param_columns", "Jc": "G1_Jc_param_columns"}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def record_thresholds(record_path, case_name, col_label):
    """Per Jacobian: noise level per group (min over steps of ||D_h - d|| 2h), the registered pass flag per group, the whole-column PASS."""
    d = json.load(open(record_path)); out = {}
    for jk, sec in JACS.items():
        rec = d["cases"][case_name][sec][col_label]
        sc = float(rec.get("step_scale", 1.0)); ds = float(rec.get("derivative_scale", 1.0) if rec.get("derivative_scale") is not None else 1.0)
        nl = {}
        for hlab, pg in rec["per_group"].items():
            h = float(hlab) * sc
            for g, e in pg["second_order"].items():
                nd = pg["norm_d"].get(g); nf = (pg.get("norm_fd") or {}).get(g); fl = (pg.get("floor") or {}).get(g) or 0.0
                if e is None or nd is None:
                    continue
                diff = float(e) * max(float(nd), float(nf or 0.0), float(fl)) / ds       # ||D_h - d|| in derivative units (d and D_h were multiplied by ds)
                nl[g] = min(nl.get(g, float("inf")), diff * 2.0 * h)
        gp = {}
        for g, v in (rec.get("group_pass") or {}).items():
            f = v.get("PASS") if isinstance(v, dict) else None
            if f is None and isinstance(v, dict) and v.get("pass_second_order") is not None and v.get("pass_five_point") is not None:
                f = bool(v.get("pass_second_order") and v.get("pass_five_point") and (v.get("richardson_error") is not None))
            gp[g] = (None if f is None else bool(f))
        wc = rec.get("PASS"); wc = None if wc is None else bool(wc)
        if "all" not in gp and wc is not None:
            gp["all"] = wc                                                     # the whole block carries the column's registered PASS
        out[jk] = dict(noise_level=nl, group_registered_pass=gp, whole_column_PASS=wc, step_scale=sc, derivative_scale=ds, groups_in_record=sorted(set(nl) | set(gp)))
    return out


def main():
    cname, rec_path, col = sys.argv[1], sys.argv[2], sys.argv[3]
    draws = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    dev = sys.argv[5] if len(sys.argv) > 5 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    problem_mod.TABLE_CACHE = False
    t0 = time.time()
    _tag = re.sub(r"[^A-Za-z0-9]+", "_", col).strip("_")
    _path = os.path.join(ROOT, "validation", f"l_screen_{cname}_{_tag}.json")
    if os.path.exists(_path):
        raise FileExistsError(f"{_path} exists: the screen never overwrites a record (lead 10:04:16Z (d)); move it aside first")
    thr = record_thresholds(rec_path, cname, col)
    case = Case(cname, dev, **CASE_TABLE[cname]); prob, model = case.prob, case.model
    zp = case.z_phys.detach().clone()
    assert prob.far_model is None and prob.far_radii is None, "the inline far-row scaling branch is active: screen it as a class"   # lead 09:56:02Z item 1 (c)
    def zf():
        return case.to_full_phys(zp)                                        # recomputed inside every evaluation so that the tail-reduction hooks act (V232)
    def groups_of(vec):
        out = {"all": float(vec.norm())}
        for gi, gname in enumerate(case.group_names):
            out[gname] = float(vec[case.row_group == gi].norm())
        if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
            out["far_anchor_block"] = float(vec[case.anchor_mask].norm())
        return out
    refs = {"Jf": lambda: prob.residual_vector_rebuild(zf()), "Jcw": lambda: prob.residual_vector_rebuild_wd(zf()), "Jc": lambda: prob.objective_at(zf(), need_aux=False)[0]}
    def evaluate(ref):
        with torch.no_grad() if ref != "Jc" else torch.enable_grad():
            return refs[ref]().detach().clone()
    gen = torch.Generator(device="cpu")
    realized = []
    identity = [False]                                                          # V232 (a): identity injection must reproduce every reference bitwise
    def pert(t, seed):
        if identity[0]:
            realized.append(dict(shape=list(t.shape), norm_injected=0.0, rel_norm=0.0, frac_moved=0.0, identity=True)); return t
        gen.manual_seed(seed)
        sign = (torch.rand(t.shape, generator=gen, dtype=torch.float64) < 0.5).to(t.device)
        up = torch.nextafter(t, torch.full_like(t, float("inf"))); dn = torch.nextafter(t, torch.full_like(t, float("-inf")))
        tp = torch.where(sign, up, dn); real = tp - t; nt = float(t.norm())
        realized.append(dict(shape=list(t.shape), norm_injected=float(real.norm()), rel_norm=(float(real.norm()) / nt if nt > 0 else 0.0), frac_moved=float((real != 0).double().mean())))
        return tp
    # ---- ingredient classes: install(seed) -> restore
    rb = model.rb; O = dict(matrices=rb.matrices, twist=rb.twist_tables, scale_mom=prob.scale_mom, scale_vort=prob.scale_vort, build=prob.pressure.build_tables,
                           build_fine=(prob.fine_ps.build_tables if getattr(prob, "fine_ps", None) is not None else None), tail_amp=prob.tail_amplitudes,
                           tail_en=prob.mode_tail_energies, ens=prob.enstrophy_and_stretching, carried=corr_mod.carried_patterns, csa=prob.closure_state_at,
                           sp=case.tc._solve_pair, ss=case.tc._solve_single, sk=case.tc._solve_k2)
    def counter():
        c = [0]
        def nxt():
            c[0] += 1; return c[0]
        return nxt
    def cls_B(seed):
        n = counter(); rb.matrices = lambda *a, **k: pert(O["matrices"](*a, **k), seed + 97 * n()); return lambda: setattr(rb, "matrices", O["matrices"])
    def cls_twist(seed):
        n = counter()
        def tw(*a, **k):
            C, S = O["twist"](*a, **k); i = n(); return pert(C, seed + 11 * i), pert(S, seed + 13 * i)
        rb.twist_tables = tw; return lambda: setattr(rb, "twist_tables", O["twist"])
    def cls_scales(seed):
        prob.scale_mom = lambda c: pert(O["scale_mom"](c), seed + 1); prob.scale_vort = lambda c: pert(O["scale_vort"](c), seed + 2)
        def r():
            prob.scale_mom = O["scale_mom"]; prob.scale_vort = O["scale_vort"]
        return r
    def cls_pressure(seed):
        n = counter()
        def wrap(orig):
            def b(*a, **k):
                T = orig(*a, **k); i = n()
                return {kk: (pert(v, seed + 31 * i + j) if (torch.is_tensor(v) and v.dim() > 0) else v) for j, (kk, v) in enumerate(T.items())}
            return b
        prob.pressure.build_tables = wrap(O["build"])
        if O["build_fine"] is not None:
            prob.fine_ps.build_tables = wrap(O["build_fine"])
        def r():
            prob.pressure.build_tables = O["build"]
            if O["build_fine"] is not None:
                prob.fine_ps.build_tables = O["build_fine"]
        return r
    def cls_tail_amp(seed):
        n = counter()
        def ta(*a, **k):
            t, s = O["tail_amp"](*a, **k); i = n(); return pert(t, seed + 3 * i), pert(s, seed + 5 * i)
        prob.tail_amplitudes = ta; return lambda: setattr(prob, "tail_amplitudes", O["tail_amp"])
    def cls_tail_en(seed):
        n = counter()
        def te(*a, **k):
            eT, eS = O["tail_en"](*a, **k); i = n(); return pert(eT, seed + 7 * i), pert(eS, seed + 19 * i)
        prob.mode_tail_energies = te; return lambda: setattr(prob, "mode_tail_energies", O["tail_en"])
    def cls_ens(seed):
        n = counter()
        def en(*a, **k):
            Z, I = O["ens"](*a, **k); i = n(); return pert(torch.as_tensor(Z), seed + 23 * i), pert(torch.as_tensor(I), seed + 29 * i)
        prob.enstrophy_and_stretching = en; return lambda: setattr(prob, "enstrophy_and_stretching", O["ens"])
    saved_closure = {}
    def cls_closure_patterns(seed):
        n = counter()
        def cp(*a, **k):
            V, labels = O["carried"](*a, **k); return pert(V, seed + 37 * n()), labels
        corr_mod.carried_patterns = cp
        if prob.closure is not None and prob.closure.get("V") is not None:
            saved_closure["V"] = prob.closure["V"]; prob.closure["V"] = pert(prob.closure["V"], seed + 41)
        def r():
            corr_mod.carried_patterns = O["carried"]
            if "V" in saved_closure:
                prob.closure["V"] = saved_closure.pop("V")
        return r
    def wnorm(G, cl):
        """Production weighted norm of the closure target: sqrt(sum_q w_q |G_q|^2) with the grid weights of the closure state (closure_state_at)."""
        return float((((G ** 2).sum(-1)) * cl["grid"].w).sum().sqrt())
    def cls_closure_target(seed):
        n = counter()
        def csa(z):
            cl = O["csa"](z); i = n()
            if cl is not None and cl.get("G_req") is not None:
                cl = dict(cl); cl["G_req"] = pert(cl["G_req"], seed + 43 * i); cl["G_req_norm"] = max(wnorm(cl["G_req"], cl), 1e-300)
            return cl
        prob.closure_state_at = csa
        if prob.closure is not None and prob.closure.get("G_req") is not None:
            saved_closure["G_req"] = prob.closure["G_req"]; saved_closure["G_req_norm"] = prob.closure["G_req_norm"]
            prob.closure["G_req"] = pert(prob.closure["G_req"], seed + 47)
            prob.closure["G_req_norm"] = max(wnorm(prob.closure["G_req"], prob.closure), 1e-300)
        def r():
            prob.closure_state_at = O["csa"]
            if "G_req" in saved_closure:
                prob.closure["G_req"] = saved_closure.pop("G_req"); prob.closure["G_req_norm"] = saved_closure.pop("G_req_norm")
        return r
    def cls_tail_reduction(seed):
        """Only the DEPENDENT coefficients solved by the constraints are perturbed: the top two entries of each column from _solve_pair / _solve_single,
        the top entry from _solve_k2 (n > 1); the free coefficients are returned unchanged (V232)."""
        n = counter()
        def top(x, m, sd):
            if not torch.is_tensor(x) or x.numel() <= m:
                return x
            return torch.cat([x[:-m], pert(x[-m:], sd)])
        def sp(*a, **k):
            aa, bb = O["sp"](*a, **k); i = n(); return top(aa, 2, seed + 53 * i), top(bb, 2, seed + 53 * i + 1)
        def ss(*a, **k):
            return top(O["ss"](*a, **k), 2, seed + 59 * n())
        def sk(free, nn):
            out = O["sk"](free, nn); return out if nn == 1 else top(out, 1, seed + 61 * n())
        case.tc._solve_pair = sp; case.tc._solve_single = ss; case.tc._solve_k2 = sk
        def r():
            case.tc._solve_pair = O["sp"]; case.tc._solve_single = O["ss"]; case.tc._solve_k2 = O["sk"]
        return r
    O["lin_vel"] = linstab_mod.linear_velocity; O["affine_pow"] = jets_mod.affine_pow; O["nlw"] = prob.nl_weights_from_ev
    def cls_nlw(seed):
        """Nonlinear row weights (Problem.nl_weights_from_ev: w_mom, w_vort from the field norms at z; recomputed in the J_cw and J_c references, frozen
        in J_f): the returned weight tensors are the ingredient before the row scaling sqrt(w)."""
        n = counter()
        def nlw(*a, **k):
            out = O["nlw"](*a, **k); i = n()
            if isinstance(out, (tuple, list)):
                return type(out)(pert(x, seed + 71 * i + j) if torch.is_tensor(x) else x for j, x in enumerate(out))
            return pert(out, seed + 71 * i) if torch.is_tensor(out) else out
        prob.nl_weights_from_ev = nlw
        return lambda: setattr(prob, "nl_weights_from_ev", O["nlw"])
    def cls_linstab(seed):
        """Stable linear operator (src/equations/linear_stable.linear_velocity): its parameter-dependent radial envelopes u^(-nu/2) and 1/u jets come
        from jets.affine_pow; the wrapper perturbs every affine_pow output DURING linear_velocity only (rb.matrices is covered by the B[l] class)."""
        n = counter()
        def lv(model_, z):
            jets_mod.affine_pow = lambda *a, **k: pert(O["affine_pow"](*a, **k), seed + 67 * n())
            try:
                return O["lin_vel"](model_, z)
            finally:
                jets_mod.affine_pow = O["affine_pow"]
        linstab_mod.linear_velocity = lv
        return lambda: setattr(linstab_mod, "linear_velocity", O["lin_vel"])
    INACTIVE_BY_CONSTRUCTION = {("nonlinear row weights", "Jf"): "inactive (weights frozen in J_f)"}   # lead 10:10:03Z: the only entry; a hook count of zero is REQUIRED there
    classes = [("B[l] radial tables", cls_B), ("twist tables", cls_twist), ("row scales", cls_scales), ("nonlinear row weights", cls_nlw), ("pressure kernel tables", cls_pressure), ("stable-linear envelopes", cls_linstab),
               ("tail amplitudes", cls_tail_amp), ("tail energies", cls_tail_en), ("enstrophy and stretching", cls_ens), ("closure patterns", cls_closure_patterns),
               ("closure target", cls_closure_target), ("tail-reduction solutions", cls_tail_reduction)]
    inactive = {"far-row scaling (inline, far_model)": dict(active=False, asserted_at_runtime=True, evidence=f"Problem.far_model is None: {prob.far_model is None}; far_radii {prob.far_radii}; merged far anchors model.extra_r {getattr(model, 'extra_r', None)} scaled by scale_mom")}
    if not getattr(prob, "stable_linear", False):
        inactive["stable-linear envelopes"] = dict(active=False, evidence=f"Problem.stable_linear is {getattr(prob, 'stable_linear', None)}: linear_velocity is not called")
        classes = [c for c in classes if c[0] != "stable-linear envelopes"]
    if not (prob.gauge == "Z" or prob.sigmaZ is not None):
        inactive["enstrophy and stretching"] = dict(active=False, evidence=f"gauge {prob.gauge!r}, sigmaZ {prob.sigmaZ!r}: enstrophy_and_stretching is not called by gauge_residuals")
        classes = [c for c in classes if c[0] != "enstrophy and stretching"]
    results = {}
    base = {}
    for ref in refs:
        r0 = evaluate(ref); r0b = evaluate(ref)
        base[ref] = dict(norms=groups_of(r0), reproducibility_norm=float((r0 - r0b).norm()), bitwise=bool(torch.equal(r0, r0b)), evaluated_twice=True)
        print(f"[{ref}] base evaluated; reproducibility norm {base[ref]['reproducibility_norm']:.3e} bitwise {base[ref]['bitwise']}", flush=True)
        for name, installer in classes:
            if (name, ref) in INACTIVE_BY_CONSTRUCTION:
                # lead 10:10:03Z item 2: install the hooks with an identity injection; the hook count MUST be zero (recorded as inactive), a nonzero count gives OPEN
                identity[0] = True; del realized[:]
                restore = installer(7)
                try:
                    r_id = evaluate(ref)
                finally:
                    restore(); identity[0] = False
                hc = len(realized)
                results.setdefault(name, {})[ref] = dict(inactive_by_construction=True, status=INACTIVE_BY_CONSTRUCTION[(name, ref)], hooks_called=hc, bitwise=bool(torch.equal(r_id, r0)),
                                                         open_if_nonzero=(hc != 0))
                print(f"[{ref}] {name:28s} {INACTIVE_BY_CONSTRUCTION[(name, ref)]}: hooks called {hc} (zero required)", flush=True); continue
            # identity control (V232 (a)): the hooks installed with an identity injection must reproduce the reference bitwise
            identity[0] = True; del realized[:]
            restore = installer(7)
            try:
                r_id = evaluate(ref)
            finally:
                restore(); identity[0] = False
            ident = dict(bitwise=bool(torch.equal(r_id, r0)), norm_diff=float((r_id - r0).norm()), hooks_called=len(realized))
            per_draw = []; inj = []; nan_seen = False
            for dnum in range(draws):
                del realized[:]
                restore = installer(1000 + 1000 * dnum + 100000 * list(refs).index(ref))
                try:
                    r = evaluate(ref)
                finally:
                    restore()
                dlt = r - r0; nan_seen = nan_seen or (not bool(torch.isfinite(dlt).all()))
                per_draw.append(groups_of(dlt)); inj.append(dict(total_norm=sum(x["norm_injected"] for x in realized), tables=list(realized)))
            maxes = {g: max(pd[g] for pd in per_draw) for g in per_draw[0]}
            res = results.setdefault(name, {})
            res[ref] = dict(per_draw=per_draw, max_change=maxes, injected=inj, identity_control=ident, nan_response=nan_seen, n_draws=len(per_draw),
                            screen_valid=(all(x["total_norm"] > 0 for x in inj) and ident["bitwise"] and ident["hooks_called"] > 0 and not nan_seen and len(per_draw) == draws))
            print(f"[{ref}] {name:28s} identity bitwise {ident['bitwise']} hooks {ident['hooks_called']}; nan {nan_seen}", flush=True)
            print(f"[{ref}] {name:28s} far_anchor_block {maxes.get('far_anchor_block', float('nan')):.2e} (thr {1e-2 * thr[ref]['noise_level'].get('far_anchor_block', float('nan')):.2e}); injected min {min(x['total_norm'] for x in inj):.2e}", flush=True)
    # decisions
    decisions = {}
    for name in results:
        failing_groups = {}; every_group = {}; open_reasons = []
        for ref in refs:
            T = thr[ref]; R = results[name][ref]; B = base[ref]
            if R.get("inactive_by_construction"):
                if R.get("hooks_called", 1) != 0 or not R.get("bitwise", False):
                    open_reasons.append(f"{ref}: class recorded inactive by construction but its hook was called {R.get('hooks_called')} times or the identity evaluation differs (lead 10:10:03Z)")
                continue
            if not (B.get("evaluated_twice") and B.get("bitwise") is True and B.get("reproducibility_norm") == 0.0):
                open_reasons.append(f"{ref}: base reproducibility not bitwise or nonzero difference ({B.get('reproducibility_norm')})")   # lead 10:04:16Z (b)
            if (R.get("n_draws") or 0) < 4:
                open_reasons.append(f"{ref}: fewer than four draws ({R.get('n_draws')})")                                                   # lead 10:04:16Z (a)
            if not R["identity_control"]["bitwise"] or R["identity_control"]["hooks_called"] == 0:
                open_reasons.append(f"{ref}: identity control failed (bitwise {R['identity_control']['bitwise']}, hooks {R['identity_control']['hooks_called']})")
            if R["nan_response"]:
                open_reasons.append(f"{ref}: non-finite response")
            if not all(x["total_norm"] > 0 for x in R["injected"]):
                open_reasons.append(f"{ref}: zero injected perturbation in some draw")
            groups = list(T["groups_in_record"])
            if "all" not in groups:
                open_reasons.append(f"{ref}: whole-block group missing from the record")
            for g in groups:
                nlev = T["noise_level"].get(g); ch = R["max_change"].get(g); flag = T["group_registered_pass"].get(g)
                if nlev is None or ch is None or not (isinstance(nlev, float) and math.isfinite(nlev) and nlev > 0) or not math.isfinite(ch):
                    open_reasons.append(f"{ref}:{g}: threshold not finite and positive, or comparison missing or non-finite"); continue       # lead 10:04:16Z (c)
                if flag is None:
                    open_reasons.append(f"{ref}:{g}: registered pass flag missing"); continue
                exceeds = bool(ch > 1e-2 * nlev)
                entry = dict(max_change=ch, noise_level=nlev, threshold=1e-2 * nlev, exceeds=exceeds, registered_pass=flag)
                every_group[f"{ref}:{g}"] = entry
                if flag is False:
                    failing_groups[f"{ref}:{g}"] = entry
            if T["whole_column_PASS"] is None:
                open_reasons.append(f"{ref}: whole-column PASS missing")
        dd_lead_rule = bool(open_reasons) or any(v["exceeds"] for v in failing_groups.values()) or not failing_groups
        dd_every_group = bool(open_reasons) or any(v["exceeds"] for v in every_group.values())
        decisions[name] = dict(double_double_required=dd_lead_rule, status=("OPEN" if open_reasons else ("double-double" if dd_lead_rule else "float64")),
                               open_reasons=open_reasons, failing_groups=failing_groups, every_group_reading=dict(double_double=dd_every_group, groups_exceeding=[k for k, v in every_group.items() if v["exceeds"]]))
        print(f"DECISION {name:28s}: {decisions[name]['status']} (lead 09:44:46Z rule; every-group reading: {'double-double' if dd_every_group else 'float64'})", flush=True)
    for name, info in inactive.items():
        decisions[name] = dict(double_double_required=False, status="inactive", evidence=info["evidence"])
    out = dict(case=cname, pair=case.pair, cost=case.cost, column=col, record=rec_path, record_sha256=sha(rec_path), script_sha256=sha(__file__), draws=draws, device=dev,
               references={"Jf": "residual_vector_rebuild (weights and closure target frozen)", "Jcw": "residual_vector_rebuild_wd (weights recomputed, closure target held)", "Jc": "objective_at (self-consistent)"},
               thresholds=thr, base=base, classes=results, inactive=inactive, decisions=decisions, perturbation="one unit in the last place, independent random sign per entry (torch.nextafter)",
               rule="lead 09:44:46Z: double-double if, in any group failing the registered rule on this record, in any Jacobian, the largest change over the draws exceeds 1e-2 of the group's noise level (V227); fail closed (lead 09:43:52Z); every-group reading reported; empirical evidence over the draws, not a bound",
               seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    tag = re.sub(r"[^A-Za-z0-9]+", "_", col).strip("_")
    path = os.path.join(ROOT, "validation", f"l_screen_{cname}_{tag}.json")
    with open(path, "x") as fh_:                                              # lead 10:04:16Z (d): exclusive create; an existing file raises FileExistsError and stops the run
        json.dump(out, fh_, indent=1, default=str)
    print("DONE", path, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
