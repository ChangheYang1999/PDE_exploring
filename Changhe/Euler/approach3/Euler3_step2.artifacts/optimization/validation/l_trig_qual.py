#!/usr/bin/env python
"""Qualification of the double-double sin and cos in the pressure kernel tables (lead 11:29:05Z item 1 (b), 11:41:09Z, 12:01:35Z; V277): for one stencil
set (case, column) the J_cw double-double ladder is repeated in three variants: dd (dd_elementary sin/cos: the (l) arithmetic, the baseline), mp (sin and
cos of the ACTUAL paired arguments from mpmath at 50 digits in a LOCAL context, each value rounded once to a (hi, lo) pair; everything else stays at the
34 digits of the named evaluations), cutoff0 (every table contribution from an exp argument with exp(x) < 1e-250 set to zero before the sums). The change
of D_h and D4_h in every group and the whole column at every step is recorded against 1e-3 of the group's registered noise level (from the gate record,
as in l_eval); the number of arguments whose mpmath pairs differ from the dd_elementary pairs is counted. Source tie (lead 12:01:35Z (c)): the baseline
ladder (dd variant) is compared bitwise, hi and lo words of D_h and D4_h at all five steps, with the earlier frozen copy's saved l_eval arrays of the same
stencil set, and the earlier copy's base pressure tables with the current builder. The gate record is a hashed run input given by an absolute path
(lead 12:01:35Z (a)). Runs from a frozen copy; the (l) outcomes themselves stay those of l_eval. Usage:
python validation/l_trig_qual.py <case> <column label> </abs/path/record.json> [device] [earlier frozen copy dir]
v5.1 (2026-10-29T15:1xZ): the tie scope is stated in the lead's words (14:54:54Z item 3); v5 kept as l_trig_qual.py.v5_ab075a60. v5 (2026-10-29, shift 4): the ladder tie accepts l_eval v5 records that save the far-anchor-block rows only (bitwise on those rows, selected by the compared anchor mask) and adds a whole-column norm tie; v4 kept as l_trig_qual.py.v4_578042ff."""
import sys, os, json, time, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np
import torch, mpmath as mp
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT
from validation import dd_chain as DC
from validation import dd_pressure as DDP
from validation import dd_elementary as DDE
from validation.l_screen import record_thresholds
import src.optimization.problem as problem_mod

TRIG_DPS = 50                 # local context inside trig_mp only (lead 12:01:35Z (c)); the global precision stays the one set by dd_tables at import (34)
CASE_TABLE = {"S01_shift_a": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt"), pair=PAIRS["a"]),
              "S05_shift_c": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"), pair=PAIRS["c"])}
HS = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
COUNT = dict(args=0, differing_pairs=0, dps_seen=set())


def trig_mp(h, l):
    """sin and cos of the double-double arguments (h + l) by mpmath at TRIG_DPS digits in a local context, rounded once to pairs; counts the pairs that differ from dd_elementary."""
    (s_dd_h, s_dd_l), (c_dd_h, c_dd_l) = DDE.sincos_dd(h, l)
    hv = h.detach().cpu().double().reshape(-1).tolist(); lv = l.detach().cpu().double().reshape(-1).tolist()
    sh = []; sl = []; ch = []; cl = []
    with mp.workdps(TRIG_DPS):
        COUNT["dps_seen"].add(mp.mp.dps)
        for a, b in zip(hv, lv):
            x = mp.mpf(a) + mp.mpf(b); s_ = mp.sin(x); c_ = mp.cos(x)
            s1 = float(s_); s2 = float(s_ - mp.mpf(s1)); c1 = float(c_); c2 = float(c_ - mp.mpf(c1))
            sh.append(s1); sl.append(s2); ch.append(c1); cl.append(c2)
    S = (torch.tensor(sh, dtype=torch.float64, device=h.device).reshape(h.shape), torch.tensor(sl, dtype=torch.float64, device=h.device).reshape(h.shape))
    C = (torch.tensor(ch, dtype=torch.float64, device=h.device).reshape(h.shape), torch.tensor(cl, dtype=torch.float64, device=h.device).reshape(h.shape))
    COUNT["args"] += h.numel(); COUNT["differing_pairs"] += int(((S[0] != s_dd_h) | (S[1] != s_dd_l) | (C[0] != c_dd_h) | (C[1] != c_dd_l)).sum())
    return S, C


def bits_equal(a, b):
    """bitwise equality of two float64 arrays (NaN patterns included)."""
    a = np.ascontiguousarray(a, dtype=np.float64); b = np.ascontiguousarray(b, dtype=np.float64)
    return bool(a.shape == b.shape and np.array_equal(a.view(np.uint64), b.view(np.uint64)))


def main():
    cname, col, rec_path = sys.argv[1], sys.argv[2], sys.argv[3]
    dev = sys.argv[4] if len(sys.argv) > 4 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    earlier = sys.argv[5] if len(sys.argv) > 5 else None          # an earlier frozen copy (runs_l/<name>) holding the named l_eval record of this stencil set (lead 11:35:30Z item 2, 12:01:35Z (c))
    if not os.path.isabs(rec_path) or not os.path.isfile(rec_path):
        raise SystemExit(f"REFUSED: the gate record must be an absolute path to an existing file (lead 12:01:35Z (a)): {rec_path}")
    if earlier is not None and not os.path.isabs(earlier):
        raise SystemExit(f"REFUSED: the earlier copy must be an absolute path: {earlier}")
    global_dps_at_start = mp.mp.dps
    if global_dps_at_start != 34:
        raise SystemExit(f"REFUSED: the global mpmath precision is {global_dps_at_start}, not the 34 digits of the named evaluations")
    problem_mod.TABLE_CACHE = False
    out_path = os.path.join(ROOT, "validation", f"l_trig_qual_{cname}_{col.replace(':', '_')}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time()
    case = Case(cname, dev, **CASE_TABLE[cname]); prob, model = case.prob, case.model
    coords, pname = col.split(":")
    zc = (case.z_opt if coords == "optimizer" else case.z_phys).detach().clone(); to_full = case.to_full_opt if coords == "optimizer" else case.to_full_phys
    n = zc.numel(); j = {"z_c": 0, "c_l": 0, "z_w": 1, "omega": 1}[pname]; e = torch.zeros_like(zc); e[n - 2 + j] = 1.0
    scale = case.pair[1] if (coords == "physical" and pname == "omega" and case.pair[1] < 0.5) else 1.0
    thr = record_thresholds(rec_path, cname, col)["Jcw"]
    def groups_of(vec):
        out = {"all": float(vec.norm())}
        for gi, g in enumerate(case.group_names):
            out[g] = float(vec[case.row_group == gi].norm())
        if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
            out["far_anchor_block"] = float(vec[case.anchor_mask].norm())
        return out
    tcache = {}
    points_seen = {}
    def ladder_with(trig, cutoff_zero=False, tag="dd"):
        def fun_dd(q, t):
            zf = to_full(q); key = (float(zf[-2]), float(zf[-1]), tag)
            if key not in tcache:
                T = DC.tables_dd(model, key[0], key[1], device=zf.device); T["P"] = DDP.build_tables_dd(prob.pressure, key[0], key[1], trig=trig, cutoff_zero=cutoff_zero); tcache[key] = T
            # exact per-point record (V277): nominal offset in hex, the variant tag, the exact parameter values in hex
            points_seen[f"{float(t).hex()}:{tag}"] = dict(offset=float(t), variant=tag, c_l_hex=float(zf[-2]).hex(), omega_hex=float(zf[-1]).hex(), arg_range=tcache[key]["P"]["arg_range"], exp_cutoff=tcache[key]["P"].get("exp_cutoff"))
            rh, rl, _ = DC.residual_dd(prob, zf, ref="Jcw", T=tcache[key], case=case, q=q, coords=coords); return rh, rl
        lad, _, pairs = DC.ladder_dd(fun_dd, zc, e, [h * scale for h in HS])
        assert sum(1 for k in points_seen if k.endswith(":" + tag)) == 20, f"variant {tag}: expected 20 derivative points"      # V277
        assert mp.mp.dps == global_dps_at_start, f"global mpmath precision changed to {mp.mp.dps} during variant {tag}"
        return lad, pairs
    tie = None
    if earlier:
        import importlib.util
        spec_ = importlib.util.spec_from_file_location("dd_pressure_earlier", os.path.join(earlier, "validation", "dd_pressure.py")); mod_e = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(mod_e)
        zf0 = to_full(zc); Te = mod_e.build_tables_dd(prob.pressure, float(zf0[-2]), float(zf0[-1])); Tn = DDP.build_tables_dd(prob.pressure, float(zf0[-2]), float(zf0[-1]))
        tie = {k: dict(bitwise=bool(torch.equal(Te[k][0], Tn[k][0]) and torch.equal(Te[k][1], Tn[k][1])), max_abs_diff=float(max((Te[k][0] - Tn[k][0]).abs().max(), (Te[k][1] - Tn[k][1]).abs().max()))) for k in ("Qc", "Qs", "wr", "mom1_0", "mom1_c", "mom1_s", "sfac", "cosb", "sinb")}
        tie["earlier_copy"] = earlier; tie["earlier_dd_pressure_sha256"] = hashlib.sha256(open(os.path.join(earlier, "validation", "dd_pressure.py"), "rb").read()).hexdigest()
        # the earlier dd_pressure imports dd_elementary, dd_tables, exact_matmul and fields_dd: their hashes in the earlier copy and here must be equal for the tie (V277)
        tie["shared_module_hashes_equal"] = {}
        tie["ladder_module_hashes"] = {}
        for rel in ("validation/dd_chain.py", "validation/dd_pressure.py", "validation/l_eval.py"):
            pe = os.path.join(earlier, rel); he = hashlib.sha256(open(pe, "rb").read()).hexdigest() if os.path.isfile(pe) else None; hn = hashlib.sha256(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()
            tie["ladder_module_hashes"][rel] = dict(equal=(he == hn), earlier=he, current=hn)        # information (v5); dd_pressure may differ by instrumentation only (lead 11:35:30Z), the base tables are compared bitwise above
        for rel in ("validation/dd_elementary.py", "validation/dd_tables.py", "src/pressure/exact_matmul.py", "src/equations/fields_dd.py"):
            he = hashlib.sha256(open(os.path.join(earlier, rel), "rb").read()).hexdigest(); hn = hashlib.sha256(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()
            tie["shared_module_hashes_equal"][rel] = dict(equal=(he == hn), earlier=he, current=hn)
        print("base tables of the earlier copy vs the current dd_pressure:", json.dumps(tie)[:600], flush=True)
        assert mp.mp.dps == global_dps_at_start
    lad_dd, pairs_dd = ladder_with(None, tag="dd")                          # dd_elementary sin/cos (the (l) arithmetic)
    # ladder tie (lead 12:01:35Z (c)): the baseline ladder against the earlier copy's saved l_eval arrays of the same stencil set, hi and lo words, all steps
    if earlier:
        npz_path = os.path.join(earlier, "validation", f"l_eval_{cname}_Jcw_{col.replace(':', '_')}_arrays.npz"); js_path = npz_path.replace("_arrays.npz", ".json")
        lt = dict(earlier_arrays=npz_path, present=os.path.isfile(npz_path) and os.path.isfile(js_path))
        if lt["present"]:
            Z = np.load(npz_path); per = {}
            # v5 (2026-10-29T14:3xZ): l_eval saves all rows only for the two named comparisons; its v5 records of the other stencil sets save the
            # far-anchor-block rows (D_hi_far_<h> ...; the block where the registered rule fails and (l) decides). The tie is then taken bitwise on
            # those rows (selection by the case's anchor mask, which the record also saves and which is compared), plus a whole-column tie through
            # the earlier record's ladder norms (ladder_pairs, float64 equality; reported, deciding only through the rows). Scope stated in the record.
            full_rows = all(f"{nm}_{h:.0e}" in Z.files for h in HS for nm in ("D_hi", "D_lo", "D4_hi", "D4_lo"))
            far_rows = (not full_rows) and all(f"{nm}_far_{h:.0e}" in Z.files for h in HS for nm in ("D_hi", "D_lo", "D4_hi", "D4_lo"))
            if far_rows:
                am = case.anchor_mask
                lt["anchor_mask_equal"] = bool("anchor_mask" in Z.files and np.array_equal(Z["anchor_mask"].astype(bool), am.cpu().numpy().astype(bool)))
                lt["anchor_rows"] = int(am.sum()); lt["saved_far_rows"] = int(Z[f"D_hi_far_{HS[0]:.0e}"].shape[0])
                sel = lambda v: v[am].cpu().numpy(); key = lambda nm, h: f"{nm}_far_{h:.0e}"
                lt["scope"] = "the far-anchor-block rows bitwise (hi, lo, rounded D_h and D4_h) at all five steps; the whole-column ladder norms in float64 equality, with the relative differences; hash equality of dd_chain.py, dd_pressure.py and l_eval.py between the copies (lead 14:54:54Z item 3; the rows are those the earlier l_eval v5 record saved, selected by the case anchor mask, compared with the saved mask)"
            else:
                sel = lambda v: v.cpu().numpy(); key = lambda nm, h: f"{nm}_{h:.0e}"
                lt["scope"] = "all rows (named comparison record)" if full_rows else "no usable D_h/D4_h arrays in the earlier record"
            if full_rows or far_rows:
                for h in HS:
                    hh = h * scale; (Dh_hi, Dh_lo), (D4_hi, D4_lo) = pairs_dd[hh]; D, D4 = lad_dd[hh]
                    per[f"{h:.0e}"] = dict(D_hi=bits_equal(sel(Dh_hi), Z[key("D_hi", h)]), D_lo=bits_equal(sel(Dh_lo), Z[key("D_lo", h)]),
                                           D4_hi=bits_equal(sel(D4_hi), Z[key("D4_hi", h)]), D4_lo=bits_equal(sel(D4_lo), Z[key("D4_lo", h)]),
                                           rounded_D_equals_hi=bits_equal(sel(D), Z[key("D_hi", h)]), rounded_D4_equals_hi=bits_equal(sel(D4), Z[key("D4_hi", h)]))
            lt["per_step"] = per
            lt["all_bitwise"] = bool((full_rows or far_rows) and all(all(v.values()) for v in per.values()) and (lt.get("anchor_mask_equal", True)))
            # whole-column scalar tie against the earlier record's ladder norms (every record of l_eval v4+ stores them)
            try:
                lp = json.load(open(js_path)).get("ladder_pairs", {}); nt = {}
                for h in HS:
                    hh = h * scale; (Dh_hi, Dh_lo), (D4_hi, D4_lo) = pairs_dd[hh]; e_ = lp.get(f"{h:.0e}", {})
                    mine = dict(D_hi_norm=float(Dh_hi.norm()), D_lo_norm=float(Dh_lo.norm()), D4_hi_norm=float(D4_hi.norm()), D4_lo_norm=float(D4_lo.norm()))
                    nt[f"{h:.0e}"] = {k: dict(equal=(e_.get(k) == v), earlier=e_.get(k), current=v, rel_diff=(abs(e_.get(k) - v) / max(abs(v), 1e-300) if isinstance(e_.get(k), float) else None)) for k, v in mine.items()}
                lt["norm_tie"] = nt; lt["norm_tie_all_equal"] = bool(lp) and all(all(x["equal"] for x in row.values()) for row in nt.values())
            except Exception as ex:
                lt["norm_tie"] = None; lt["norm_tie_all_equal"] = False; lt["norm_tie_error"] = repr(ex)
            lt["earlier_arrays_sha256"] = hashlib.sha256(open(npz_path, "rb").read()).hexdigest(); lt["earlier_record_sha256"] = hashlib.sha256(open(js_path, "rb").read()).hexdigest()
            ej = json.load(open(js_path)); lt["earlier_record_sources"] = ej.get("sources"); lt["earlier_record_ts"] = ej.get("ts")
        else:
            lt["all_bitwise"] = False; lt["note"] = "the earlier copy holds no saved l_eval arrays of this stencil set: the ladder tie is NOT established"
        tie["ladder_tie"] = lt
        print("ladder tie:", json.dumps({k: lt[k] for k in lt if k != "earlier_record_sources"})[:700], flush=True)
    lad_mp, _ = ladder_with(trig_mp, tag="mp")                       # mpmath sin/cos of the same paired arguments (lead 11:29:05Z (b))
    lad_cz, _ = ladder_with(None, cutoff_zero=True, tag="cutoff0")   # exp cutoff replacement: contributions with exp(x) < 1e-250 set to zero before the sums (lead 11:41:09Z)
    res = {}; all_ok = True; res_cz = {}; all_ok_cz = True; bitwise_cz = True
    for h in HS:
        hh = h * scale
        D0, D40 = lad_dd[hh]; D1, D41 = lad_mp[hh]; D2, D42 = lad_cz[hh]
        g2 = groups_of(D1 - D0); g4 = groups_of(D41 - D40); c2 = groups_of(D2 - D0); c4 = groups_of(D42 - D40)
        bitwise_cz = bitwise_cz and bool(torch.equal(D2, D0) and torch.equal(D42, D40))
        row = {}; rowc = {}
        for g in g2:
            nlev = thr["noise_level"].get(g); lim = (1e-3 * nlev / (2 * hh)) if nlev else None     # the noise level is ||D_h - d|| 2h: the limit on a change of D_h is 1e-3 nlev / (2h)
            ok = (lim is not None) and g2[g] <= lim and g4[g] <= lim
            okc = (lim is not None) and c2[g] <= lim and c4[g] <= lim
            all_ok = all_ok and bool(ok); all_ok_cz = all_ok_cz and bool(okc)
            row[g] = dict(change_D=g2[g], change_D4=g4[g], limit_on_D=lim, within=bool(ok))
            rowc[g] = dict(change_D=c2[g], change_D4=c4[g], limit_on_D=lim, within=bool(okc))
        res[f"{h:.0e}"] = row; res_cz[f"{h:.0e}"] = rowc
    tie_ok = bool(tie and tie.get("ladder_tie", {}).get("all_bitwise") and all(v["equal"] for v in tie["shared_module_hashes_equal"].values()) and all(tie[k]["bitwise"] for k in ("Qc", "Qs", "wr", "mom1_0", "mom1_c", "mom1_s", "sfac", "cosb", "sinb")))
    rec = dict(case=cname, column=col, reference="Jcw", steps=HS, scale=scale, record=rec_path, record_sha256=hashlib.sha256(open(rec_path, "rb").read()).hexdigest(),
               mpmath_digits_global=global_dps_at_start, mpmath_digits_trig_local=sorted(COUNT["dps_seen"]), mpmath_digits_global_at_end=mp.mp.dps,
               trig_arguments=COUNT["args"], differing_pairs=COUNT["differing_pairs"], per_step=res, all_within=all_ok, earlier_copy_table_tie=tie,
               exp_cutoff_replacement=dict(per_step=res_cz, all_within=all_ok_cz, bitwise_identical_to_dd=bitwise_cz, bitwise_scope="once-rounded D_h and D4_h arrays (float64) of the cutoff variant against the dd variant", rule="lead 11:41:09Z: contributions with exp(x) < 1e-250 set to zero before the sums; change of D_h, D4_h per group and step against 1e-3 of the registered noise level (as a limit on D_h); counts and largest weights stay in the per-point ranges as description"),
               admission=dict(trig_within=all_ok, exp_replacement_within=all_ok_cz, source_tie=tie_ok, all_three=bool(all_ok and all_ok_cz and tie_ok), rule="V277 last paragraph / lead 11:56:57Z item 5: admission of the stencil set requires the trig change, the exp replacement and the source-version tie jointly"),
               launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None),
               pressure_arg_ranges_per_point=points_seen,
               rule="lead 11:29:05Z item 1 (b): change of D_h and D4_h from mpmath sin/cos tables below 1e-3 of the group's registered noise level at every step; the noise level ||D_h - d|| 2h is converted to a limit on D_h by dividing by 2h; mpmath at 50 digits only inside the trig evaluation (lead 12:01:35Z (c))",
               sources=DC.source_hashes(ROOT), seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_path, "x") as fh_:
        json.dump(rec, fh_, indent=1, default=str)
    print("trig qualification", cname, col, "all within:", all_ok, "differing pairs:", COUNT["differing_pairs"], "of", COUNT["args"], "| exp cutoff replacement within:", all_ok_cz, "bitwise:", bitwise_cz, "| source tie:", tie_ok, "| admission (all three):", rec["admission"]["all_three"], f"{time.time() - t0:.0f}s"); print("DONE", out_path)


if __name__ == "__main__":
    main()
