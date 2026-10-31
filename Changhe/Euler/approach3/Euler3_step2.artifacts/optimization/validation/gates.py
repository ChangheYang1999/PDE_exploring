#!/usr/bin/env python
"""D6FP derivative-validation battery for SPEC v1.2 section 3 (gates G1, G2(a)(c), G3, G4(a)(b), G5(a)(b), G8) on the PRODUCTION code path.
Writes validation/gates_<tag>.json (all error tables, inputs, hashes, timings) and validation/gates_<tag>.md (summary).
Usage: CUDA_VISIBLE_DEVICES=5 python validation/gates.py --tag <tag> [--cases S01_own,S01_shift,...] [--quick]"""
import sys, os, time, json, math, argparse, hashlib, platform
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from src.equations.fields import Model, alpha_of
from src.equations import residuals as res
from src.optimization.problem import Problem
from src.optimization.tail_constraints import TailConstraints
from src.optimization.param_map import ParamMap
from src.optimization.lm import jacobian_fwd, param_columns
from src.optimization.seeds import make_seed
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DT = torch.float64
H_LADDER = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
PROD = dict(formulation="mom", nl_weighting=True, nl_denominator="all5far", far_lambda=1e-2, closure_lambda=1e-3, far_radii=[4096.0, 16384.0, 65536.0])
PAIRS = {"a": (0.42, 0.3), "b": (0.45, 0.3), "c": (0.45, 1.0), "small_omega": (0.44, 0.05), "large_omega": (0.47, 5.0), "near_edge": (0.49, 0.3)}


def sync():
    if torch.cuda.is_available():
        (torch.cuda.synchronize() if torch.cuda.is_available() else None)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def code_hashes():
    out = {}
    for rel in ("src/optimization/lm.py", "src/optimization/problem.py", "src/optimization/param_map.py", "src/equations/fields.py", "src/pressure/poisson_sh.py",
                "src/equations/residuals.py", "src/far_field/correction.py", "src/optimization/tail_constraints.py", "src/bases/radial.py", "src/bases/jets.py",
                "src/bases/solid_harmonics.py", "validation/gates.py"):
        out[rel] = sha(os.path.join(ROOT, rel))
    return out


class Case:
    """One test configuration: a field (saved state or manufactured), a parameter pair, the production objective, both coordinate systems."""
    def __init__(self, name, device, start=None, pair=None, m_parity="even", seed=0, channels=None, Nk=16, Nr=48, R0=0.3, arrays=None, align=True, grid=None):
        """arrays (D6FP D1): explicit coefficient arrays dict(A, C, B, D, E (torch, (n, Nq)), channels, m_parity, R0, Nk, Nr) for an externally defined
        field (the verifier's inputs); grid = (ntheta, nphi) overrides the model's angular grid; align=False skips the phase alignment."""
        self.name = name; self.device = device
        extra_kw = {}
        if grid is not None:
            extra_kw = dict(ntheta=int(grid[0]), nphi=int(grid[1]))
        if arrays is not None:
            L = 6; far = PROD["far_radii"]; c0, w0 = pair; self.start_sha = None; self.start = None
            Nk, Nr, R0, m_parity, channels = int(arrays["Nk"]), int(arrays["Nr"]), float(arrays["R0"]), arrays["m_parity"], arrays["channels"]
        elif start is not None:
            S = torch.load(start, map_location="cpu", weights_only=False); cfg = S["config"]
            self.start_sha = sha(start); self.start = start
            L, Nk, Nr, R0 = cfg["L"], cfg["Nk"], cfg.get("Nr"), cfg.get("R0", 1.0); m_parity = cfg.get("m_parity", "even"); channels = cfg.get("channels")
            far = cfg.get("far_radii")
            c0, w0 = (float(S["z"][-2]), float(S["z"][-1])) if S.get("free_params") else (cfg["c_l"], cfg["omega"])
        else:
            L = 6; far = PROD["far_radii"]; c0, w0 = pair; self.start_sha = None; self.start = None
            channels = channels if channels is not None else dict(NkB=4, NkD=4, NkE=4, core_damp=2, LB=15, LD=14, LE=6)
        c_l, omega = pair if pair is not None else (c0, w0)
        self.pair = (float(c_l), float(omega)); self.own = pair is None or (abs(c_l - c0) < 1e-15 and abs(omega - w0) < 1e-15)
        self.model = Model(L=L, Nk=Nk, Nr=Nr, m_parity=m_parity, R0=R0, c_l=c_l, omega=omega, free_params=True, channels=channels, device=device, extra_r=far, **extra_kw)
        self.prob = Problem(self.model, **PROD)
        self.tc = TailConstraints(self.model); self.pm = ParamMap()
        model = self.model
        if arrays is not None:
            extra = {nm: arrays[nm].to(device) for nm in ("B", "D", "E") if nm in arrays and arrays[nm].numel() > 0}
            z = model.pack(arrays["A"].to(device), arrays["C"].to(device), c_l, omega, extra=extra)
            self.field_desc = f"external coefficient arrays ({arrays.get('desc', 'unnamed')}) at ({c_l}, {omega})"
        elif start is not None:
            zs = S["z"].to(device)
            z = torch.cat([zs[: model.n_coef], torch.tensor([c_l, omega], device=device)]) if not S.get("free_params") else zs.clone()
            z[-2] = c_l; z[-1] = omega
            self.field_desc = f"saved state {os.path.basename(start)} (coefficients kept) at ({c_l}, {omega}); source parameters ({c0}, {w0})"
        else:
            rng = np.random.default_rng(seed)
            d = model.unpack_all(torch.zeros(model.n_z, device=device))
            def blk(n, scale):
                k = np.arange(n)[:, None]
                return torch.tensor(rng.normal(size=(n, model.Nq)) * (0.55 ** k) * scale, dtype=DT, device=device)
            l = model.l_arr.cpu().numpy()[None, :]
            A = blk(model.Nk, 1.0) * torch.tensor(0.7 ** (l - 1), dtype=DT, device=device); C = blk(model.Nk, 0.8) * torch.tensor(0.7 ** (l - 1), dtype=DT, device=device)
            extra = {}
            for nm in ("B", "D", "E"):
                n = dict(model.layout)[nm]
                if n > 0:
                    extra[nm] = blk(n, 0.3) * torch.tensor(0.8 ** (l - 1), dtype=DT, device=device)
            z = model.pack(A, C, c_l, omega, extra=extra)
            aT, aS, cc, ww = model.unpack(z); n2 = float(self.prob.tail_norm2(aT, aS, cc, ww))
            z = z.clone(); z[: model.n_coef] /= math.sqrt(n2)
            self.field_desc = f"manufactured smooth random field (seed {seed}, geometric radial decay 0.55, angular decay 0.7, all blocks A C B D E, parity {m_parity}) at ({c_l}, {omega})"
        self.prob.pivot = self.prob.choose_pivot(z)
        self.prob.ensure_geometry(z)
        if align:
            z = self.prob.phase_align(z)
        self.z_opt = self.pm.reduce(self.tc.reduce(z)); self.z_phys = self.tc.reduce(z)
        self.z_full = self.to_full_opt(self.z_opt)
        r, aux = self.prob.objective_at(self.z_full); self.prob.commit_aux(aux)
        self.r = r; self.cost = 0.5 * float(r @ r)
        # row groups (SPEC 3.0 (c))
        Nr, Na = model.Nr, model.Na; npde = 3 * Nr * Na
        rows = torch.arange(npde, device=device); node = (rows // Na) % Nr
        rr = model.r[node]
        self.groups = {}
        g = torch.full((r.numel(),), -1, dtype=torch.long, device=device)
        g[:npde] = torch.where(rr <= 0.1 * model.R0, 0, torch.where(rr <= 2.0 ** 8 * model.R0, 1, 2))
        self.group_names = ["near_origin(r<=0.1R0)", "core_intermediate", "far(r>256R0)"]
        # separate far-anchor block (the appended anchor nodes; SPEC 3.0 (c) as applied by the verifier: assessed as its own block)
        self.anchor_mask = torch.zeros(r.numel(), dtype=torch.bool, device=device)
        if model.extra_r:
            self.anchor_mask[:npde] = node >= model.Nr_src
        blocks = self.prob.row_blocks()
        self.block_slices = {b[0]: (b[1], b[2] if b[2] is not None else r.numel()) for b in blocks}
        for nm, (a0, a1) in self.block_slices.items():
            if nm != "pde":
                g[a0:a1] = 2 + {"closure": 1, "gauge": 2, "far": 3, "radial_lambda": 4}.get(nm, 5)
        self.group_names += ["closure", "gauge"]
        self.row_group = g
        self.n_far_nodes = int(len(model.extra_r)) if model.extra_r else 0

    # coordinate maps
    def to_full_opt(self, zo):
        return self.tc.expand(self.pm.expand(zo))

    def to_full_phys(self, zp):
        return self.tc.expand(zp)

    def group_errors(self, d, dh, floor_rel=1e-10, ref=None):
        """e(h) per group and block: ||D_h - d|| / max(||d||, ||D_h||, F), F = floor_rel * norm of the undifferentiated quantity ref in the group."""
        out = {}
        def one(mask, label):
            dd, dq = d[mask], dh[mask]
            F = floor_rel * float(ref[mask].norm()) if ref is not None else 0.0
            den = max(float(dd.norm()), float(dq.norm()), F)
            if den == 0:
                out[label] = dict(e=0.0, absolute=True, norm_d=0.0, norm_fd=0.0); return
            out[label] = dict(e=float((dd - dq).norm() / den), max_comp=float((dd - dq).abs().max()), norm_d=float(dd.norm()), norm_fd=float(dq.norm()),
                              floor=F, absolute_only=(F > max(float(dd.norm()), float(dq.norm()))))
        one(torch.ones_like(self.row_group, dtype=torch.bool), "all")
        for i, nm in enumerate(self.group_names):
            m = self.row_group == i
            if m.any():
                one(m, nm)
        if hasattr(self, "anchor_mask") and self.anchor_mask.any():
            one(self.anchor_mask, "far_anchor_block")
        return out


def stencil_ladder(fun, z, e, hs, record_active=None):
    """Centered D_h and five-point D4_h along direction e (absolute step h) for every h in hs; fun returns a tensor. Returns dict h -> (D_h, D4_h),
    plus active-set records when record_active(z) is given (called at every stencil point)."""
    out = {}; active = {}
    cache = {}
    if record_active is not None:
        active[0.0] = record_active(z)                     # v4 (V187): the BASE active set is recorded too; every stencil point must agree with it
    def f(t):
        if t not in cache:
            cache[t] = fun(z + t * e)
            if record_active is not None:
                active[t] = record_active(z + t * e)
        return cache[t]
    for h in hs:
        D = (f(h) - f(-h)) / (2 * h)
        D4 = (8 * (f(h) - f(-h)) - (f(2 * h) - f(-2 * h))) / (12 * h)
        out[h] = (D, D4)
    return out, active


def scalar_decisions(Ds, D4s, dpred, Fl, hs, tau=1e-6):
    """SPEC 3.0 (d) for a scalar derivative test, evaluated twice: with the floor Fl (the registered decision) and with F = 0 (PASS_rel); the
    Richardson value is formed from the first passing consecutive second-order pair of each evaluation. Ds, D4s: dict '1e-03' -> value."""
    def decide(F):
        e2 = {h: abs(Ds[f"{h:.0e}"] - dpred) / max(abs(dpred), abs(Ds[f"{h:.0e}"]), F) for h in hs}
        e4 = {h: abs(D4s[f"{h:.0e}"] - dpred) / max(abs(dpred), abs(D4s[f"{h:.0e}"]), F) for h in hs}
        pr = pass_rule(e2, e4, tau)
        hs_sorted = sorted(e2.keys(), reverse=True); rich = None; pair = None
        for i in range(len(hs_sorted) - 1):                                      # v4 (V187): every adjacent passing pair is inspected; the smallest Richardson error counts
            if e2[hs_sorted[i]] <= tau and e2[hs_sorted[i + 1]] <= tau:
                h, hp = hs_sorted[i], hs_sorted[i + 1]; R = Ds[f"{hp:.0e}"] + (Ds[f"{hp:.0e}"] - Ds[f"{h:.0e}"]) / 99.0
                r_ = abs(R - dpred) / max(abs(dpred), abs(R), F)
                if rich is None or r_ < rich:
                    rich = r_; pair = (f"{h:.0e}", f"{hp:.0e}")
        return pr, rich, pair, bool(pr["pass_second_order"] and pr["pass_five_point"] and rich is not None and rich <= tau), e2, e4
    pr, rich, pair, ok, _, _ = decide(Fl)
    pr0, rich0, pair0, ok0, e20, e40 = decide(0.0)
    return dict(pass_rule=pr, richardson_error=rich, richardson_pair=pair, PASS_floor_rule=ok, pass_rule_F0=pr0, richardson_error_F0=rich0, richardson_pair_F0=pair0, PASS_rel_rule=ok0,
                errors_second_order_F0={f"{h:.0e}": e20[h] for h in hs}, errors_five_point_F0={f"{h:.0e}": e40[h] for h in hs})


def pass_rule(errs, errs4, tau):
    """SPEC 3.0 (d): two consecutive ladder steps with e <= tau (second order) AND two consecutive with e4 <= tau (five point) AND the Richardson
    value of the passing pair within tau (checked by the caller through 'richardson'). errs: dict h -> e."""
    hs = sorted(errs.keys(), reverse=True)
    ok2 = any(errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau for i in range(len(hs) - 1))
    ok4 = any(errs4[hs[i]] <= tau and errs4[hs[i + 1]] <= tau for i in range(len(hs) - 1))
    ratios = {f"{hs[i]:.0e}->{hs[i+1]:.0e}": (errs[hs[i]] / errs[hs[i + 1]] if errs[hs[i + 1]] > 0 else None) for i in range(len(hs) - 1)}
    return dict(pass_second_order=ok2, pass_five_point=ok4, ratios_second_order=ratios, min_e=min(errs.values()), min_e4=min(errs4.values()))


def richardson_error(lad, d, h_pair, mask=None, scale=1.0, ref=None, floor_rel=1e-10):
    """Richardson value D_h' + (D_h' - D_h)/99 from the second-order pair (h, h' = h/10) against d, judged with the registered floor F = floor_rel * ||ref||
    over the rows (SPEC 3.0 (d)(iii)); d and the Richardson value are multiplied by the step scale s_j of the column (3.0 (b')(1)); v3 2026-10-29 (V179)."""
    h, hp = h_pair
    Dh, Dhp = lad[h][0], lad[hp][0]
    R = (Dhp + (Dhp - Dh) / 99.0) * scale; dd = d * scale
    F = 0.0
    if mask is not None:
        R, dd = R[mask], dd[mask]
        if ref is not None:
            F = floor_rel * float(ref[mask].norm())
    elif ref is not None:
        F = floor_rel * float(ref.norm())
    return float((R - dd).norm() / max(float(dd.norm()), float(R.norm()), F, 1e-300))


def richardson_witness(lad, d, h_pair, mask=None, scale=1.0, ref=None, floor_rel=1e-10):
    """v5c (V192 item 6, recording only): the Richardson comparison with its witnesses: ||R - d|| s, ||d|| s, ||R|| s and the floor F (same arithmetic as richardson_error)."""
    h, hp = h_pair
    Dh, Dhp = lad[h][0], lad[hp][0]
    R = (Dhp + (Dhp - Dh) / 99.0) * scale; dd = d * scale
    F = 0.0
    if mask is not None:
        R, dd = R[mask], dd[mask]
        if ref is not None:
            F = floor_rel * float(ref[mask].norm())
    elif ref is not None:
        F = floor_rel * float(ref.norm())
    nd, nR, ndiff = float(dd.norm()), float(R.norm()), float((R - dd).norm())
    return dict(richardson_error=ndiff / max(nd, nR, F, 1e-300), norm_diff_scaled=ndiff, norm_d_scaled=nd, norm_R_scaled=nR, floor=F, scale=scale)


def best_richardson(lad, dcol, errs, hs, tau, scale, ref, mask=None, dscale=None):
    """v4 (V187, SPEC 3.0 (d)): over ALL adjacent pairs of ladder steps whose second-order errors are both within tau, the Richardson error (floored, scaled)
    is formed and the smallest is returned with its pair (None if no pair passes). The former harness took the first passing pair only."""
    best = None; best_pair = None; allp = {}
    for i in range(len(hs) - 1):
        w = richardson_witness(lad, dcol, (hs[i] * scale, hs[i + 1] * scale), mask=mask, scale=(scale if dscale is None else dscale), ref=ref); r = w["richardson_error"]
        allp[f"{hs[i]:.0e}->{hs[i + 1]:.0e}"] = dict(w, pair_passes_second_order=bool(errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau))   # v5c (lead 06:59Z (b), V192 item 6): every pair with its witnesses
        if errs[hs[i]] <= tau and errs[hs[i + 1]] <= tau and (best is None or r < best):
            best, best_pair = r, (f"{hs[i]:.0e}", f"{hs[i + 1]:.0e}")
    best_richardson.last_all = allp
    return best, best_pair


def column_test(case, label, dcol, fun, z, e, h_steps, tau_all=1e-6, tau_group=1e-5, ref=None, record_active=None, scale=1.0, deriv_scale=None):
    """G1-type test of a derivative column dcol against the ladder of fun along e (direction with |e| = 1 in the perturbed coordinate; step h*scale).
    deriv_scale (v5, V190): the factor by which d and D_h are multiplied before the comparison with the fixed floor F; None = scale (coefficient columns, SPEC
    3.0 (b')(1)); 1.0 for the physical omega column at small omega, whose step is relative (h omega) but whose derivative is judged in physical units."""
    ds_ = scale if deriv_scale is None else deriv_scale
    lad, active = stencil_ladder(fun, z, e, [h * scale for h in h_steps], record_active)
    errs = {}; errs4 = {}; per_group = {}; errs0 = {}; errs40 = {}
    dcol_s = dcol * ds_                                     # SPEC 3.0 (b')(1) (V179; v3): the column and the differences are multiplied by the derivative scale (s_j for
    for h in h_steps:                                       # coefficient columns; 1 for parameter columns) and compared against the FIXED floor F = 1e-10 ||r_block||
        D, D4 = lad[h * scale]; D = D * ds_; D4 = D4 * ds_
        ge = case.group_errors(dcol_s, D, ref=ref); ge4 = case.group_errors(dcol_s, D4, ref=ref)
        ge0 = case.group_errors(dcol_s, D, ref=None); ge40 = case.group_errors(dcol_s, D4, ref=None)        # F = 0 (SPEC 3.0 (c): PASS_rel; lead 23:24Z item 3)
        errs[h] = ge["all"]["e"]; errs4[h] = ge4["all"]["e"]; errs0[h] = ge0["all"]["e"]; errs40[h] = ge40["all"]["e"]
        per_group[f"{h:.0e}"] = dict(second_order={k: v["e"] for k, v in ge.items()}, five_point={k: v["e"] for k, v in ge4.items()},
                                   second_order_F0={k: v["e"] for k, v in ge0.items()}, five_point_F0={k: v["e"] for k, v in ge40.items()},
                                   norm_d={k: v.get("norm_d") for k, v in ge.items()}, norm_fd={k: v.get("norm_fd") for k, v in ge.items()}, norm_fd_five_point={k: v.get("norm_fd") for k, v in ge4.items()},
                                   floor={k: v.get("floor") for k, v in ge.items()},
                                   max_comp={k: v.get("max_comp") for k, v in ge.items()}, floor_above_norms={k: v.get("absolute_only") for k, v in ge.items()})
    pr = pass_rule(errs, errs4, tau_all); pr0 = pass_rule(errs0, errs40, tau_all)
    hs = sorted(errs.keys(), reverse=True)
    # Richardson: the best over all adjacent passing second-order pairs (v4; with the floor, 3.0 (d)(iii)), and the F = 0 variant
    rich, rich_pair = best_richardson(lad, dcol, errs, hs, tau_all, scale, ref, dscale=ds_); rich_all = dict(best_richardson.last_all)
    rich0, rich0_pair = best_richardson(lad, dcol, errs0, hs, tau_all, scale, None, dscale=ds_); rich0_all = dict(best_richardson.last_all)
    # group pass: every group and block within tau_group at two consecutive steps (second order) and five point; the same with F = 0 (PASS_rel)
    group_pass = {}
    for gname in ["all"] + case.group_names + (["far_anchor_block"] if (hasattr(case, "anchor_mask") and bool(case.anchor_mask.any())) else []):
        eg = {h: per_group[f"{h:.0e}"]["second_order"].get(gname) for h in hs}; eg4 = {h: per_group[f"{h:.0e}"]["five_point"].get(gname) for h in hs}
        if any(v is None for v in eg.values()):
            continue
        t = tau_all if gname == "all" else tau_group
        p = pass_rule(eg, eg4, t); group_pass[gname] = dict(pass_second_order=p["pass_second_order"], pass_five_point=p["pass_five_point"], min_e=p["min_e"], min_e4=p["min_e4"])
        eg0 = {h: per_group[f"{h:.0e}"]["second_order_F0"].get(gname) for h in hs}; eg40 = {h: per_group[f"{h:.0e}"]["five_point_F0"].get(gname) for h in hs}
        p0 = pass_rule(eg0, eg40, t); group_pass[gname].update(pass_second_order_F0=p0["pass_second_order"], pass_five_point_F0=p0["pass_five_point"], min_e_F0=p0["min_e"], min_e4_F0=p0["min_e4"])
    # per-group Richardson on the first passing second-order pair of that group (SPEC 3.0 (d) (iii) applied per group)
    for gname, gp in group_pass.items():
        t = tau_all if gname == "all" else tau_group
        eg = {h: per_group[f"{h:.0e}"]["second_order"].get(gname) for h in hs}
        gp["richardson_error"] = None
        if gname == "all":
            mask = None
        elif gname == "far_anchor_block":
            mask = case.anchor_mask
        else:
            gi = case.group_names.index(gname); mask = case.row_group == gi
        eg_f = {h: (v if v is not None else float("inf")) for h, v in eg.items()}
        gp["richardson_error"], gp["richardson_pair"] = best_richardson(lad, dcol, eg_f, hs, t, scale, ref, mask=mask, dscale=ds_); gp["richardson_all_pairs"] = dict(best_richardson.last_all)
        gp["PASS"] = bool(gp["pass_second_order"] and gp["pass_five_point"] and gp["richardson_error"] is not None and gp["richardson_error"] <= t)
        # the same decision with F = 0 (Richardson is floor-free already; its pair is the first passing F = 0 pair)
        eg0 = {h: per_group[f"{h:.0e}"]["second_order_F0"].get(gname) for h in hs}
        eg0_f = {h: (v if v is not None else float("inf")) for h, v in eg0.items()}
        gp["richardson_error_F0"], gp["richardson_pair_F0"] = best_richardson(lad, dcol, eg0_f, hs, t, scale, None, mask=mask, dscale=ds_); gp["richardson_all_pairs_F0"] = dict(best_richardson.last_all)
        gp["PASS_rel"] = bool(gp["pass_second_order_F0"] and gp["pass_five_point_F0"] and gp["richardson_error_F0"] is not None and gp["richardson_error_F0"] <= t)
        gp["absolute_only"] = bool(gp["PASS"] and not gp["PASS_rel"])          # SPEC 3.0 (c): passes only because of the floor (lead 23:24Z item 3)
    active_same = None
    if active:
        keys = [json.dumps(a, sort_keys=True) for a in active.values()]
        active_same = len(set(keys)) == 1
    ok = pr["pass_second_order"] and pr["pass_five_point"] and (rich is not None and rich <= tau_all) and all(v["PASS"] for v in group_pass.values()) and (active_same is not False)
    ok_rel = pr0["pass_second_order"] and pr0["pass_five_point"] and (rich0 is not None and rich0 <= tau_all) and all(v["PASS_rel"] for v in group_pass.values()) and (active_same is not False)
    return dict(label=label, errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=per_group,
                errors_second_order_F0={f"{h:.0e}": errs0[h] for h in hs}, errors_five_point_F0={f"{h:.0e}": errs40[h] for h in hs},
                pass_rule=pr, richardson_error=rich, richardson_pair=rich_pair, richardson_all_pairs=rich_all, pass_rule_F0=pr0, richardson_error_F0=rich0, richardson_pair_F0=rich0_pair, richardson_all_pairs_F0=rich0_all, group_pass=group_pass, PASS=bool(ok), PASS_rel=bool(ok_rel), absolute_only=bool(ok and not ok_rel),
                active_set_base_recorded=bool(active) and (0.0 in active),
                column_norm=float(dcol.norm()), active_sets_identical=active_same,
                active_sets=({f"{t:+.1e}": a for t, a in active.items()} if active else None), step_scale=scale, derivative_scale=ds_,
                scaling_convention="v5c (2026-10-29, V190, V192: derivative_scale separate from step_scale; physical omega judged in physical units; every Richardson pair with its difference and extrapolated-vector norms and the floor) v4 (V179, V187): base active set recorded and compared; Richardson over all adjacent passing pairs (3.0 (d)); v3: d and D_h multiplied by the step scale s_j against the fixed floor F = 1e-10 ||r_block|| (SPEC 3.0 (b')(1)); Richardson judged with F (3.0 (d)(iii)); the F = 0 variants are scale-free")


def run_case(case, quick=False, n_coef_cols=20, seed=11, save=None, sections=("G1", "G2G4", "G3", "G5")):
    """save: optional callable(out) invoked after every gate section (progressive saving; both full chains of 2026-10-28 lost their results to a crash in G5)."""
    prob, model, tc, pm = case.prob, case.model, case.tc, case.pm
    dev = case.device
    out = dict(name=case.name, field=case.field_desc, pair=case.pair, own_parameters=case.own, start_sha256=case.start_sha, n_opt=int(case.z_opt.numel()), n_rows=int(case.r.numel()),
               cost=case.cost, geometry=prob.pressure.geometry_id, n_quad=prob.pressure.n_quad, blocks=case.block_slices, pivot=prob.pivot, closure_mismatch=(prob.closure or {}).get("mismatch"),
               exterior_monopole=bool(prob.exterior_monopole), discrete_moments=prob.pressure.discrete_moments(res.pressure_source(model.fields_grid(case.z_full, need_vort=False)["GU"]), lmax=1),
               stable_linear=bool(prob.stable_linear))
    hs = [1e-3, 1e-4, 1e-5, 1e-6] if quick else H_LADDER
    zo, zp, zf = case.z_opt, case.z_phys, case.z_full
    n = zo.numel()
    def act(zz_full):
        ev = prob.evaluate(zz_full, tables=prob.pressure_tables_at(zz_full))
        return prob.nl_active_set(ev) | dict(geometry=prob.pressure.geometry_id)
    # D6FP 2026-10-29 (SPEC v1.11 3.5 (d), lead 04:05Z item 3): section selection, CONTROL FLOW ONLY. The coefficient-column draw and the five G3
    # normal draws come from one generator in the original order (cols first, then the 3 + 2 normals), so a part that skips G1 reproduces exactly
    # the G3 directions of the unsplit run; every part records the drawn columns and SHA-256 hashes of the raw draws (and of the scaled directions,
    # which also need the column norms of J, where G3 runs). No numerical value changes.
    sections = tuple(sections); out["sections_run"] = list(sections)
    rng = np.random.default_rng(seed)
    cols = sorted(rng.choice(n - 2, size=min(n_coef_cols, n - 2), replace=False).tolist())
    g3_draws = [rng.normal(size=n) for _ in range(5)]                                  # consumed by G3 in order: random_scaled_0..2, mixed_0..1
    fun = lambda q: prob.residual_vector(case.to_full_opt(q))
    out["G1_coefficient_columns_drawn"] = cols
    out["G3_direction_hashes"] = dict(raw_draws_sha256=hashlib.sha256(b"".join(np.ascontiguousarray(u, dtype=np.float64).tobytes() for u in g3_draws)).hexdigest(),
                                      scaled_directions_sha256=None, order=["random_scaled_0", "random_scaled_1", "random_scaled_2", "mixed_0", "mixed_1"])
    g1 = {}; g1w = {}; g1c = {}; g2 = {}; g4 = {}; g3 = {}; g5 = {}
    def run_coef_columns(which):
        """G1 coefficient columns (SPEC v1.16 3.6 (j)(c),(d), lead 06:08Z; test-only change of 2026-10-29T06:2xZ). Records per column the FULL column_test
        output needed by the rounding-level and coverage checker: per group and step ||d||, ||D_h||, floor and e (per_group), the group decisions
        (group_pass), the five-point errors, PASS, PASS_rel, active sets. The harness J_c closure block uses the five-point step 1e-4 * s_j, with s_j the
        step scale of column j (was the fixed 1e-4: at rounding level for far-channel columns of norm 1e-11, diag_coef_S09_own). The PDE and closure rows
        are at most quadratic in the coefficients, so the centered and five-point differences are exact up to rounding at any step."""
        E = torch.zeros(len(cols), n, device=dev)
        for i, k in enumerate(cols):
            E[i, k] = 1.0
        Jcols = torch.func.vmap(lambda ee: torch.func.jvp(fun, (zo,), (ee,))[1])(E).T          # (rows, ncols); also gives the step scales
        hq = [1e-3, 1e-4, 1e-5, 1e-6] if quick else [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
        sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
        def coef_scale(i):
            return max(1.0, 1e-7 / max(float(Jcols[:, i].norm()), 1e-300) / 1e-3)
        def rec_of(k, t, extra=None):
            r = dict(column=k, PASS=t["PASS"], PASS_rel=t["PASS_rel"], absolute_only=t["absolute_only"], errors=t["errors_second_order"], errors_five_point=t["errors_five_point"],
                     errors_second_order_F0=t["errors_second_order_F0"], richardson=t["richardson_error"], richardson_F0=t["richardson_error_F0"], norm=t["column_norm"], step_scale=t["step_scale"],
                     active_sets_identical=t["active_sets_identical"], per_group=t["per_group"], group_pass=t["group_pass"], pass_rule=t["pass_rule"], pass_rule_F0=t["pass_rule_F0"],
                     active_sets=t.get("active_sets"), active_set_base_recorded=t.get("active_set_base_recorded"), richardson_pair=t.get("richardson_pair"), richardson_pair_F0=t.get("richardson_pair_F0"),
                     errors_five_point_F0=t.get("errors_five_point_F0"), derivative_scale=t.get("derivative_scale"), scaling_convention=t.get("scaling_convention"),
                     richardson_all_pairs=t.get("richardson_all_pairs"), richardson_all_pairs_F0=t.get("richardson_all_pairs_F0"))
            if extra:
                r.update(extra)
            return r
        if "Jf" in which:
            coef_res = []
            for i, k in enumerate(cols):
                e = torch.zeros_like(zo); e[k] = 1.0
                t_f = column_test(case, f"G1 J_f coefficient column {k}", Jcols[:, i], fun, zo, e, hq, ref=case.r, scale=coef_scale(i))
                coef_res.append(dict(column=k, Jf=rec_of(k, t_f)))
            out["G1_Jf_coefficient_columns"] = dict(columns=cols, results=coef_res, all_pass=all(c["Jf"]["PASS"] for c in coef_res), record_version="v2 (full per-group records, 2026-10-29)")
        if "Jcw" in which:
            fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
            Jcols_w = torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E).T
            coef_w = []
            for i, k in enumerate(cols):
                e = torch.zeros_like(zo); e[k] = 1.0
                t_w = column_test(case, f"G1 J_cw coefficient column {k}", Jcols_w[:, i], fun_w, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=coef_scale(i))
                coef_w.append(rec_of(k, t_w))
            out["G1_Jcw_coefficient_columns"] = dict(columns=cols, results=coef_w, all_pass=all(c["PASS"] for c in coef_w), record_version="v2 (full per-group records, 2026-10-29)")
        if "Jc" in which:
            jc_coef = []
            def jc_coef_column(k, scale):
                def fun_wd(q):
                    zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
                    return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
                e = torch.zeros_like(zo); e[k] = 1.0
                col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
                if "closure" in case.block_slices:
                    a0, a1 = case.block_slices["closure"]; h = 1e-4 * scale                    # scaled step (SPEC v1.16 3.6 (j)(d)); was the fixed 1e-4
                    crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
                    col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
                return col
            for i, k in enumerate(cols[: (3 if quick else 20)]):
                e = torch.zeros_like(zo); e[k] = 1.0; sc = coef_scale(i)
                t_c = column_test(case, f"G1 J_c coefficient column {k}", jc_coef_column(k, sc), sc_fun_o, zo, e, hq, ref=case.r, record_active=lambda q: act(case.to_full_opt(q)), scale=sc)
                jc_coef.append(rec_of(k, t_c, extra=dict(closure_block_step=1e-4 * sc)))
            out["G1_Jc_coefficient_columns"] = dict(columns=cols[: (3 if quick else 20)], results=jc_coef, all_pass=all(c["PASS"] for c in jc_coef), record_version="v2 (full per-group records; closure block step 1e-4 * s_j, 2026-10-29)")
    if "G1" in sections:
        # ---------------- G1: frozen-weight Jacobian J_f parameter columns (physical and optimizer coordinates) ----------------
        t0 = time.time()
        g1 = {}
        for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
            pfun = lambda q: prob.residual_vector(to_full(q), differentiable_pressure=True)
            frozen_fun = lambda q: prob.residual_vector_rebuild(to_full(q))             # frozen weights and closure target, tables rebuilt, same layout
            Jp = param_columns(pfun, zc, [n - 2, n - 1])
            for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
                e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
                scale = 1.0
                if coords == "physical" and pname == "omega" and case.pair[1] < 0.5:
                    scale = case.pair[1]                                                   # relative step at small omega (SPEC 3.0 (b))
                g1[f"{coords}:{pname}"] = column_test(case, f"G1 J_f column {pname} ({coords})", Jp[:, j], frozen_fun, zc, e, hs, ref=case.r, scale=scale, deriv_scale=1.0)
        out["G1_Jf_param_columns"] = g1
        # ---------------- G1: PRODUCTION Jacobian J_cw (weights differentiated, closure target lagged) parameter columns ----------------
        g1w = {}
        for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
            pfun_w = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
            ref_w = lambda q: prob.residual_vector_rebuild_wd(to_full(q))
            Jpw = param_columns(pfun_w, zc, [n - 2, n - 1])
            for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
                e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
                scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
                g1w[f"{coords}:{pname}"] = column_test(case, f"G1 J_cw column {pname} ({coords}, production: weights differentiated)", Jpw[:, j], ref_w, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale, deriv_scale=1.0)
        out["G1_Jcw_param_columns"] = g1w
        # ---------------- G1: complete Jacobian J_c parameter columns vs the self-consistent residual ----------------
        g1c = {}
        def jc_param_column(zc, to_full, j):
            # weights differentiable (forward mode), closure block by five-point differences of the fresh closure rows (production uses centered h = 1e-4)
            def fun_wd(q):
                zz = to_full(q)
                tabs = prob.pressure_tables_at(zz, differentiable=True)
                ev = prob.evaluate(zz, tables=tabs)
                nl_w = prob.nl_weights_from_ev(ev, differentiable=True)
                return prob.residual_vector(zz, tables=tabs, nl_w=nl_w, closure=prob.closure, ev=ev)
            e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
            col = torch.func.jvp(fun_wd, (zc,), (e,))[1]
            if "closure" in case.block_slices:
                a0, a1 = case.block_slices["closure"]
                def crow(q):
                    zz = to_full(q); return prob.closure_rows(zz, closure=prob.closure_state_at(zz))
                h = 1e-4
                col = col.clone(); col[a0:a1] = (8 * (crow(zc + h * e) - crow(zc - h * e)) - (crow(zc + 2 * h * e) - crow(zc - 2 * h * e))) / (12 * h)
            return col
        for coords, zc, to_full in (("optimizer", zo, case.to_full_opt), ("physical", zp, case.to_full_phys)):
            sc_fun = lambda q: prob.objective_at(to_full(q), need_aux=False)[0]
            for j, pname in enumerate(("c_l", "omega") if coords == "physical" else ("z_c", "z_w")):
                col = jc_param_column(zc, to_full, j)
                e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
                scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
                g1c[f"{coords}:{pname}"] = column_test(case, f"G1 J_c column {pname} ({coords}, self-consistent residual)", col, sc_fun, zc, e, hs, ref=case.r, record_active=lambda q, tf=to_full: act(tf(q)), scale=scale, deriv_scale=1.0)
        out["G1_Jc_param_columns"] = g1c
        # ---------------- G1: random coefficient columns (J_f vs residual_vector; J_cw vs residual_vector_wd; J_c vs objective_at) ----------------
        run_coef_columns(("Jf", "Jcw", "Jc"))
        out["t_G1"] = time.time() - t0
        if save:
            save(out)
    if ("G1_coef" in sections or "G1_Jc_coef" in sections) and "G1" not in sections:          # coefficient-column sections alone (SPEC v1.16 3.6 (j)(d))
        t0 = time.time()
        run_coef_columns(("Jf", "Jcw", "Jc") if "G1_coef" in sections else ("Jc",))
        out["t_G1_coef"] = time.time() - t0
        if save:
            save(out)
    if "G2G4" in sections:
        # ---------------- G2 (a): assembly identity for d_p R_u; (c) U_p, DU_p vs differences; G4 (a)(b): pressure derivative ----------------
        t0 = time.time()
        g2 = {}; g4 = {}
        def fields_and_pressure(zp_):
            zz = case.to_full_phys(zp_)
            F = model.fields_grid(zz, need_vort=False)
            tabs = prob.pressure_tables_at(zz, differentiable=True)
            src = res.pressure_source(F["GU"])
            P, gradP, _, _ = prob.pressure.solve(src, tables=tabs["main"])
            mt = res.momentum_terms(F, gradP)
            return F["U"], F["GU"], gradP, mt["sum"], src, F["c_l"], F["omega"]
        U, GU, gradP, Ru, src, cl_t, om_t = fields_and_pressure(zp)
        yv = res.yvec(model.y); Jy = res.Jvec(yv)
        W = cl_t * yv - om_t * Jy + U
        groups_pde = torch.where(model.r <= 0.1 * model.R0, 0, torch.where(model.r <= 2.0 ** 8 * model.R0, 1, 2))   # per node
        def per_group_rel(a, b, resolved_only=False):
            """relative difference per radial group of (3, Nr, Na) tensors."""
            o = {}
            for gi, gname in enumerate(case.group_names[:3]):
                m = groups_pde == gi
                if not m.any():
                    continue
                da, db = a[:, m], b[:, m]
                o[gname] = float((da - db).norm() / max(float(db.norm()), 1e-300))
            return o
        for j, pname in enumerate(("c_l", "omega")):
            e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
            (U_, GU_, gP_, Ru_, src_, _, _), (Up, GUp, gPp, Rup, srcp, _, _) = torch.func.jvp(fields_and_pressure, (zp,), (e,))
            # (a) formula of SPEC 2.4
            if pname == "c_l":
                lhs = -U + (1 - cl_t) * Up + torch.einsum('m...,mi...->i...', yv + Up, GU) + torch.einsum('m...,mi...->i...', W, GUp) + om_t * res.Jvec(Up) + gPp
            else:
                lhs = (1 - cl_t) * Up + torch.einsum('m...,mi...->i...', -Jy + Up, GU) + torch.einsum('m...,mi...->i...', W, GUp) + res.Jvec(U) + om_t * res.Jvec(Up) + gPp
            g2[f"G2a_identity_{pname}"] = dict(per_group=per_group_rel(lhs, Rup), all=float((lhs - Rup).norm() / Rup.norm()), threshold=1e-10)
            g2[f"G2a_identity_{pname}"]["PASS"] = all(v <= 1e-10 for v in g2[f"G2a_identity_{pname}"]["per_group"].values())
            # (c) U_p, DU_p vs differences of U, DU at fixed a
            def Ufun(q):
                F = model.fields_grid(case.to_full_phys(q), need_vort=False); return torch.cat([F["U"].reshape(-1), F["GU"].reshape(-1)])
            dcol = torch.cat([Up.reshape(-1), GUp.reshape(-1)])
            scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
            lad, _ = stencil_ladder(Ufun, zp, e, [h * scale for h in hs])
            errs = {}; errs4 = {}
            nU = U.numel()
            node_of_U = torch.arange(nU, device=dev) // model.Na % model.Nr; node_of_G = torch.arange(GU.numel(), device=dev) // model.Na % model.Nr
            gidx = torch.cat([groups_pde[node_of_U], groups_pde[node_of_G]])
            pg = {}
            for h in hs:
                D, D4 = lad[h * scale]
                errs[h] = float((dcol - D).norm() / max(float(D.norm()), float(dcol.norm()))); errs4[h] = float((dcol - D4).norm() / max(float(D4.norm()), float(dcol.norm())))
                pg[f"{h:.0e}"] = {case.group_names[gi]: float((dcol[gidx == gi] - D[gidx == gi]).norm() / max(float(D[gidx == gi].norm()), 1e-300)) for gi in range(3) if (gidx == gi).any()}
            pr = pass_rule(errs, errs4, 1e-6)
            g2[f"G2c_Up_DUp_{pname}"] = dict(errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=pg, pass_rule=pr,
                                            PASS=pr["pass_second_order"] and pr["pass_five_point"], step_scale=scale)
            # G4 (a): grad P_p vs differences of grad P (tables rebuilt at each stencil point, fixed layout); per group, resolved range
            def gPfun(q):
                zz = case.to_full_phys(q); F = model.fields_grid(zz, need_vort=False); tabs = prob.pressure_tables_at(zz)
                return prob.pressure.solve(res.pressure_source(F["GU"]), tables=tabs["main"])[1].reshape(-1)
            dcol = gPp.reshape(-1); lad, _ = stencil_ladder(gPfun, zp, e, [h * scale for h in hs])
            errs = {}; errs4 = {}; pg = {}
            gi_g = groups_pde[node_of_U]
            for h in hs:
                D, D4 = lad[h * scale]
                m = gi_g == 1
                errs[h] = float((dcol[m] - D[m]).norm() / max(float(D[m].norm()), 1e-300)); errs4[h] = float((dcol[m] - D4[m]).norm() / max(float(D4[m].norm()), 1e-300))
                pg[f"{h:.0e}"] = {case.group_names[gi]: float((dcol[gi_g == gi] - D[gi_g == gi]).norm() / max(float(D[gi_g == gi].norm()), 1e-300)) for gi in range(3) if (gi_g == gi).any()}
            pr = pass_rule(errs, errs4, 1e-6)
            g4[f"G4a_gradP_{pname}"] = dict(resolved_range_errors_second_order={f"{h:.0e}": errs[h] for h in hs}, resolved_range_errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, per_group=pg, pass_rule=pr,
                                           PASS=pr["pass_second_order"] and pr["pass_five_point"], note="resolved range = core_intermediate group; other groups reported")
            # G4 (b): the derivative source 2 tr(DU DU_p) vs the jvp of the source actually used
            fp = 2.0 * torch.einsum('mi...,im...->...', GU, GUp)
            g4[f"G4b_source_{pname}"] = dict(rel=float((fp - srcp).norm() / srcp.norm()), PASS=bool(float((fp - srcp).norm() / srcp.norm()) <= 1e-12))
        out["G2"] = g2; out["G4"] = g4; out["t_G2_G4"] = time.time() - t0
        if save:
            save(out)
    if "G3" in sections:
        # ---------------- G3: complete loss gradient vs directional differences of O1 ----------------
        t0 = time.time()
        J = jacobian_fwd(fun, zo, chunk=256)
        Jp = param_columns(lambda q: prob.residual_vector(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
        J[:, n - 2] = Jp[:, 0]; J[:, n - 1] = Jp[:, 1]
        colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt()
        g_frozen = J.T @ case.r
        # the PRODUCTION Jacobian J_cw (weights differentiated) for the floor of G3 (SPEC 3.0 (c): F = 1e-3 ||r|| ||J v|| with the complete J; the closure target
        # part of J_c is lagged in J_cw, weight 1e-3) and for the frozen-model comparison
        fun_w2 = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
        Jw = jacobian_fwd(fun_w2, zo, chunk=256)
        Jpw = param_columns(lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True), zo, [n - 2, n - 1])
        Jw[:, n - 2] = Jpw[:, 0]; Jw[:, n - 1] = Jpw[:, 1]
        g_cw = Jw.T @ case.r
        def grad_complete_opt(zo_):
            zz = zo_.detach().clone().requires_grad_(True)
            rr = prob.objective_graph(case.to_full_opt(zz)); c = 0.5 * (rr @ rr)
            g, = torch.autograd.grad(c, zz); g = g.detach().clone()
            gfull, parts = prob.complete_gradient(case.to_full_opt(zo_).detach(), return_parts=True)
            d = pm.describe(zo_)
            if parts["pattern_fd"] is not None:
                g[-2] += float(parts["pattern_fd"][0]) * d["dcl_dzc"]; g[-1] += float(parts["pattern_fd"][1]) * d["domega_dzw"]
            return g, gfull
        g_c, g_c_full = grad_complete_opt(zo)
        O1 = lambda q: 0.5 * float((lambda rr: rr @ rr)(prob.objective_at(case.to_full_opt(q), need_aux=False)[0]))
        dirs = {"e_zc": None, "e_zw": None}
        E = {}
        e = torch.zeros_like(zo); e[n - 2] = 1.0; E["e_zc(optimizer)"] = e
        e = torch.zeros_like(zo); e[n - 1] = 1.0; E["e_zw(optimizer)"] = e
        for i in range(3):
            u = torch.tensor(g3_draws[i], device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm        # unit norm in the SCALED coordinates D X
        for i in range(2):
            u = torch.tensor(g3_draws[3 + i], device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm   # mixed: unit scaled norm with parameter components
        out["G3_direction_hashes"]["scaled_directions_sha256"] = hashlib.sha256(b"".join(E[k].detach().cpu().numpy().tobytes() for k in E)).hexdigest()   # order: e_zc, e_zw, random_scaled_0..2, mixed_0..1
        g3 = {}
        def act_o(q):
            return act(case.to_full_opt(q))
        for dname, v in E.items():
            dpred = float(g_c @ v); dfro = float(g_frozen @ v)
            c0 = case.cost
            vals = {}; act_rec = {0.0: act_o(zo)}                                   # v5 (V190): the base active set is part of the comparison
            def f(t):
                if t not in vals:
                    vals[t] = O1(zo + t * v); act_rec[t] = act_o(zo + t * v)
                return vals[t]
            errs = {}; errs4 = {}; Ds = {}
            Fl = 1e-3 * float(case.r.norm()) * float((Jw @ v).norm())
            D4s = {}
            for h in hs:
                D = (f(h) - f(-h)) / (2 * h); D4 = (8 * (f(h) - f(-h)) - (f(2 * h) - f(-2 * h))) / (12 * h)
                errs[h] = abs(D - dpred) / max(abs(dpred), abs(D), Fl); errs4[h] = abs(D4 - dpred) / max(abs(dpred), abs(D4), Fl); Ds[f"{h:.0e}"] = D; D4s[f"{h:.0e}"] = D4
            sc = scalar_decisions(Ds, D4s, dpred, Fl, hs)
            keys = set(json.dumps(a, sort_keys=True) for a in act_rec.values())
            g3[dname] = dict(derivative_complete=dpred, derivative_frozen_model=dfro, derivative_Jcw_model=float(g_cw @ v), rel_diff_frozen_vs_complete=abs(dfro - dpred) / max(abs(dpred), 1e-300),
                             rel_diff_Jcw_vs_complete=abs(float(g_cw @ v) - dpred) / max(abs(dpred), 1e-300),
                             fd_values={k: float(v_) for k, v_ in Ds.items()}, fd_values_five_point={k: float(v_) for k, v_ in D4s.items()}, errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs},
                             floor=Fl, active_sets_identical=(len(keys) == 1), active_sets={f"{t:+.1e}": a for t, a in act_rec.items()}, **sc,
                             PASS=bool(sc["PASS_floor_rule"] and len(keys) == 1), PASS_rel=bool(sc["PASS_rel_rule"] and len(keys) == 1))
            g3[dname]["absolute_only"] = bool(g3[dname]["PASS"] and not g3[dname]["PASS_rel"])
        # physical coordinates for the two parameter directions
        g_phys = {}
        dsc = pm.describe(zo)
        g3["complete_gradient_parameters"] = dict(optimizer=dict(z_c=float(g_c[-2]), z_w=float(g_c[-1])), physical=dict(c_l=float(g_c[-2]) / dsc["dcl_dzc"], omega=float(g_c[-1]) / dsc["domega_dzw"]),
                                                  frozen_model_optimizer=dict(z_c=float(g_frozen[-2]), z_w=float(g_frozen[-1])),
                                                  scaled_complete={"z_c": float(g_c[-2] / (colnorm[-2] * case.r.norm())), "z_w": float(g_c[-1] / (colnorm[-1] * case.r.norm()))},
                                                  rel_diff_frozen_vs_complete_full_vector=float((g_frozen - g_c).norm() / g_c.norm()))
        # physical-coordinate directional test for c_l and omega (fixed a): O1 as a function of z_phys
        O1p = lambda q: 0.5 * float((lambda rr: rr @ rr)(prob.objective_at(case.to_full_phys(q), need_aux=False)[0]))
        for j, pname in enumerate(("c_l", "omega")):
            e = torch.zeros_like(zp); e[n - 2 + j] = 1.0
            chain = dsc["dcl_dzc"] if j == 0 else dsc["domega_dzw"]
            dpred = float(g_c[-2 + j]) / chain                       # dO1/dp at FIXED REDUCED coordinates a (the physical reference O1(tc.expand(z_phys)))
            scale = case.pair[1] if (pname == "omega" and case.pair[1] < 0.5) else 1.0
            errs = {}; errs4 = {}; Ds = {}; act_rec = {0.0: act(case.to_full_phys(zp))}      # v5 (V190): base active set
            vals = {}
            def f(t):
                if t not in vals:
                    vals[t] = O1p(zp + t * e); act_rec[t] = act(case.to_full_phys(zp + t * e))
                return vals[t]
            Fl = 1e-3 * float(case.r.norm()) * float(Jpw[:, j].norm()) / chain
            D4s = {}
            for h in hs:
                hh = h * scale
                D = (f(hh) - f(-hh)) / (2 * hh); D4 = (8 * (f(hh) - f(-hh)) - (f(2 * hh) - f(-2 * hh))) / (12 * hh)
                errs[h] = abs(D - dpred) / max(abs(dpred), abs(D), Fl); errs4[h] = abs(D4 - dpred) / max(abs(dpred), abs(D4), Fl); Ds[f"{h:.0e}"] = D; D4s[f"{h:.0e}"] = D4
            sc = scalar_decisions(Ds, D4s, dpred, Fl, hs)
            keys = set(json.dumps(a, sort_keys=True) for a in act_rec.values())
            g3[f"e_{pname}(physical)"] = dict(derivative_complete=dpred, derivative_complete_full_z=float(g_c_full[-2 + j]), fd_values=Ds, fd_values_five_point=D4s, errors_second_order={f"{h:.0e}": errs[h] for h in hs},
                                            errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, floor=Fl, active_sets_identical=(len(keys) == 1), **sc,
                                            PASS=bool(sc["PASS_floor_rule"] and len(keys) == 1), PASS_rel=bool(sc["PASS_rel_rule"] and len(keys) == 1), step_scale=scale)
            g3[f"e_{pname}(physical)"]["absolute_only"] = bool(g3[f"e_{pname}(physical)"]["PASS"] and not g3[f"e_{pname}(physical)"]["PASS_rel"])
        out["G3"] = g3; out["t_G3"] = time.time() - t0
        if save:
            save(out)
        del J, Jw
    if "G5" in sections:
        # ---------------- G5 (a)(b): field consistency at sample points ----------------
        t0 = time.time()
        rng5 = np.random.default_rng(seed + 1)
        radii = np.concatenate([[0.0], model.R0 * np.logspace(-3, np.log10(65536.0 / model.R0), 24)])
        pts = []
        for rr_ in radii:
            if rr_ == 0.0:
                pts.append([0.0, 0.0, 0.0]); continue
            th = math.acos(rng5.uniform(-1, 1)); ph = rng5.uniform(0, 2 * math.pi)
            pts.append([rr_ * math.sin(th) * math.cos(ph), rr_ * math.sin(th) * math.sin(ph), rr_ * math.cos(th)])
        pts += [[0.0, 0.0, 0.05 * model.R0], [0.0, 0.0, 3.0 * model.R0], [0.0, 0.0, -400.0 * model.R0]]       # axis points
        pts = torch.tensor(pts, dtype=DT, device=dev)
        rp = pts.norm(dim=1)
        def Upts(q, P):
            F = model.fields_points(case.to_full_phys(q), P, need_vort=False); return F["U"], F["GU"]
        Up_, GUp_ = Upts(zp, pts)
        g5 = dict(points=pts.cpu().numpy().tolist(), seed=seed + 1)
        # (a) spatial differences of U vs DU: displacement eps * max(r, 1e-3 R0) along each axis; best over eps
        best = {0: [], 1: [], 2: []}
        for ip in range(pts.shape[0]):
            y0 = pts[ip]; hbase = max(float(rp[ip]), 1e-3 * model.R0)
            errs_eps = []
            for eps in (1e-3, 1e-4, 1e-5, 1e-6):
                hh = eps * hbase
                G_fd = torch.zeros(3, 3, device=dev)
                for i in range(3):
                    e3 = torch.zeros(3, device=dev); e3[i] = hh
                    Up1, _ = Upts(zp, torch.stack([y0 + e3, y0 - e3])); G_fd[i] = (Up1[:, 0] - Up1[:, 1]) / (2 * hh)
                errs_eps.append(float((G_fd - GUp_[:, :, ip]).norm() / max(float(GUp_[:, :, ip].norm()), 1e-300)))
            gi = 0 if rp[ip] <= 0.1 * model.R0 else (1 if rp[ip] <= 256 * model.R0 else 2)
            best[gi].append(min(errs_eps))
        g5["G5a_spatial_FD_vs_DU_best_rel_per_group"] = {case.group_names[gi]: (max(v) if v else None) for gi, v in best.items()}
        g5["G5a_PASS"] = all((max(v) if v else 0.0) <= 5e-7 for v in best.values())
        # (b) divergence of U and of U_p at every point
        divU = (GUp_[0, 0] + GUp_[1, 1] + GUp_[2, 2]).abs() / GUp_.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
        e = torch.zeros_like(zp); e[n - 2] = 1.0
        (_, _), (Upc, GUpc) = torch.func.jvp(lambda q: Upts(q, pts), (zp,), (e,))
        e = torch.zeros_like(zp); e[n - 1] = 1.0
        (_, _), (Upw, GUpw) = torch.func.jvp(lambda q: Upts(q, pts), (zp,), (e,))
        divc = (GUpc[0, 0] + GUpc[1, 1] + GUpc[2, 2]).abs() / GUpc.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
        divw = (GUpw[0, 0] + GUpw[1, 1] + GUpw[2, 2]).abs() / GUpw.reshape(9, -1).norm(dim=0).clamp_min(1e-300)
        g5["G5b_div_rel_max"] = dict(U=float(divU.max()), U_c=float(divc.max()), U_w=float(divw.max()))
        g5["G5b_PASS"] = bool(max(float(divU.max()), float(divc.max()), float(divw.max())) <= 1e-10)
        # (c) second part: the source tr(DU^2) used by the pressure equals the one recomputed from the DU used in the residual (same tensor in this code)
        Fg = model.fields_grid(zf, need_vort=False); s1 = res.pressure_source(Fg["GU"]); s2 = torch.einsum('mi...,im...->...', Fg["GU"], Fg["GU"])
        g5["G5c_source_consistency_rel"] = float((s1 - s2).norm() / s2.norm())
        out["G5"] = g5; out["t_G5"] = time.time() - t0
        if save:
            save(out)
    summ = {}
    if "G1" in sections:
        summ.update(G1_Jf=all(v["PASS"] for v in g1.values()), G1_Jcw_production=all(v["PASS"] for v in g1w.values()), G1_Jc=all(v["PASS"] for v in g1c.values()), G1_coef_Jf=out["G1_Jf_coefficient_columns"]["all_pass"],
                    G1_coef_Jcw=out["G1_Jcw_coefficient_columns"]["all_pass"], G1_coef_Jc=out["G1_Jc_coefficient_columns"]["all_pass"])
    if "G1" not in sections:
        for key, name in (("G1_Jf_coefficient_columns", "G1_coef_Jf"), ("G1_Jcw_coefficient_columns", "G1_coef_Jcw"), ("G1_Jc_coefficient_columns", "G1_coef_Jc")):
            if key in out:
                summ[name] = out[key]["all_pass"]
    if "G2G4" in sections:
        summ.update(G2a=all(v["PASS"] for k, v in g2.items() if k.startswith("G2a")), G2c=all(v["PASS"] for k, v in g2.items() if k.startswith("G2c")),
                    G4a=all(v["PASS"] for k, v in g4.items() if k.startswith("G4a")), G4b=all(v["PASS"] for k, v in g4.items() if k.startswith("G4b")))
    if "G3" in sections:
        summ.update(G3=all(v["PASS"] for k, v in g3.items() if isinstance(v, dict) and "PASS" in v))
    if "G5" in sections:
        summ.update(G5a=g5["G5a_PASS"], G5b=g5["G5b_PASS"])
    out["summary"] = summ
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,S05_own,S01_shift_a,S05_shift_c,manu_small_omega,manu_large_omega,manu_near_edge,manu_a,manu_allm_c")
    ap.add_argument("--quick", action="store_true"); ap.add_argument("--device", default=("cuda:0" if torch.cuda.is_available() else "cpu"))
    ap.add_argument("--sections", default="G1,G2G4,G3,G5", help="SPEC v1.11 3.5 (d) / v1.16 3.6 (j): comma-separated subset of G1,G2G4,G3,G5, or the coefficient-column sections G1_coef (J_f, J_cw, J_c) and G1_Jc_coef (J_c only)")
    a = ap.parse_args()
    dev = a.device
    t_all = time.time()
    results = dict(tag=a.tag, sections=a.sections, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), host=platform.node(), precision_mode=__import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE, jacobian_precision=("dd" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "dd" else "fp64"), residual_precision=("fp64" if __import__("src.optimization.problem", fromlist=["PRECISION_MODE"]).PRECISION_MODE == "fp64" else "dd"), gpu=((torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu") if torch.cuda.is_available() else "cpu"),
                   cuda_visible=os.environ.get("CUDA_VISIBLE_DEVICES"), torch=torch.__version__, code_sha256=code_hashes(), tf32=dict(matmul=torch.backends.cuda.matmul.allow_tf32, cudnn=torch.backends.cudnn.allow_tf32),
                   ladder=H_LADDER, pairs=PAIRS, cases={})
    defs = {
        "S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")),
        "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")),
        "S10_own": dict(start=os.path.join(ROOT, "starts", "S10_d6t_cl0.45_om0.3.pt")),
        "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")),                # SPEC v1.9 R3 release battery cases
        "S20_own": dict(start=os.path.join(ROOT, "starts", "S20_s4allm_cl0.45_om1.0.pt")),
        "S11_own": dict(start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")),
        "S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
        "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"]),
        "manu_a": dict(pair=PAIRS["a"], seed=3), "manu_b": dict(pair=PAIRS["b"], seed=4), "manu_small_omega": dict(pair=PAIRS["small_omega"], seed=5),
        "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6), "manu_near_edge": dict(pair=PAIRS["near_edge"], seed=7),
        "manu_allm_c": dict(pair=PAIRS["c"], seed=8, m_parity="all"),
    }
    for cname in a.cases.split(","):
        t0 = time.time()
        print(f"=== case {cname} ===", flush=True)
        case = Case(cname, dev, **defs[cname])
        def _save(o, _name=case.name):
            results[_name] = dict(o, partial=True)
            json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
        res_ = run_case(case, quick=a.quick, save=_save, sections=tuple(a.sections.split(",")))
        res_["seconds"] = time.time() - t0; res_["peak_GB"] = (torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0) / 2 ** 30 if torch.cuda.is_available() else 0.0
        results["cases"][cname] = res_
        print(f"  summary {json.dumps(res_['summary'])}  ({res_['seconds']:.0f}s)", flush=True)
        for k, v in (res_.get("G1_Jf_param_columns") or {}).items():
            print(f"  G1 J_f {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} PASS {v['PASS']}", flush=True)
        for k, v in (res_.get("G1_Jcw_param_columns") or {}).items():
            print(f"  G1 J_cw(prod) {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} PASS {v['PASS']}", flush=True)
        for k, v in (res_.get("G1_Jc_param_columns") or {}).items():
            print(f"  G1 J_c {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v['richardson_error']} active-sets-identical {v['active_sets_identical']} PASS {v['PASS']}", flush=True)
        for k, v in (res_.get("G3") or {}).items():
            if isinstance(v, dict) and "PASS" in v:
                print(f"  G3 {k}: e2 {json.dumps({kk: f'{vv:.1e}' for kk, vv in v['errors_second_order'].items()})} rich {v.get('richardson_error')} PASS {v['PASS']}", flush=True)
        json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
        del case; torch.cuda.empty_cache()
    results["seconds_total"] = time.time() - t_all
    json.dump(results, open(os.path.join(ROOT, "validation", f"gates_{a.tag}.json"), "w"), indent=1, default=str)
    print("ALL CASES DONE", json.dumps({c: r["summary"] for c, r in results["cases"].items()}))


if __name__ == "__main__":
    main()
