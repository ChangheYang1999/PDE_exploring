"""Failure map per SPEC 9.1 (pre-registered protocol): floors among B2-passing runs, collapsed runs, dominant equation and
shell, failure class per run (F1 swirl collapse; F5 regularity/interface defect > 1e-3; F6 solver non-convergence, i.e. the
weighted cost did not decrease over the last 20 percent of the iteration budget; F7 plateau with none dominant; F2 to F4 need
the verifier's far-field and pressure checks and are left to INDEPENDENT_VALIDATION), GPU hours and wall time.
Usage: python3 scripts/failure_map.py   -> FAILURE_MAP.csv (per run), FAILURE_MAP.md (per c_l table)"""
import os, sys, json, glob, math, csv, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
import torch

def level_of(cfg):
    sh = cfg.get("shells", [])
    return f"D{cfg.get('D')}n{cfg.get('nmax')}K{sh[0][1] if sh else 0}-{cfg.get('ball_radial', 'cheb')}-e{cfg.get('emax')}"

rows = []
for f in sorted(glob.glob(os.path.join(ROOT, "runs", "*", "result.json"))):
    jid = os.path.basename(os.path.dirname(f))
    if jid.startswith("zz_"):
        continue
    r = json.load(open(f)); cfg = r.get("cfg", {}); v = r.get("validation") or {}; rep = r.get("report", {})
    vf = os.path.join(os.path.dirname(f), "validation.json")
    dom_eq = dom_shell = None
    if os.path.exists(vf):
        # dominant equation = argmax of the registered per-equation rho_max (all point sets: Gauss, random, axis collar, origin);
        # shell = the shell/point set attaining it (verifier audit 02:08Z: the earlier Gauss-only selector mislabelled collar maxima)
        vv = json.load(open(vf)); be = vv.get("rho_max_by_eq") or {}
        cand = {e: val for e, val in be.items() if e != "div" and val is not None and math.isfinite(val)}
        if cand:
            dom_eq = max(cand, key=cand.get); target = cand[dom_eq]; dom_shell = "?"
            for s in vv.get("shells", []):
                for pset in ("gauss", "random", "collar"):
                    val = s.get(f"rho_{dom_eq}_{pset}")
                    if val is not None and abs(val - target) <= 1e-9 * max(1.0, abs(target)):
                        dom_shell = f"{s['k']} {pset}"
            if dom_shell == "?" and isinstance(vv.get("origin"), dict):
                val = vv["origin"].get(f"rho_{dom_eq}")
                if val is not None and abs(val - target) <= 1e-9 * max(1.0, abs(target)):
                    dom_shell = "origin"
    # F6: cost decrease over the last 20 percent of iterations
    f6 = None
    pt = os.path.join(os.path.dirname(f), "final.pt")
    if os.path.exists(pt):
        try:
            h = torch.load(pt, weights_only=False, map_location="cpu").get("history", [])
            c = [x["cost"] for x in h if "cost" in x]
            if len(c) >= 10:
                n80 = int(0.8 * len(c)); f6 = c[-1] / max(c[n80], 1e-300)
        except Exception:
            pass
    s_core = v.get("s_core"); s_far = v.get("s_far")
    b2 = (s_core is not None and s_far is not None and s_core >= 0.05 and s_far >= 0.05)
    ifc = rep.get("interfaces", [])
    ifc_rel = max([d["dphi"] / max(d["phi_scale"], 1e-300) for d in ifc], default=float("nan"))          # value jump of phi (the Stage I criterion)
    # derivative-aware interface jump (verifier A8/B4 criterion, lead note 31 item 5): value and derivative jumps of phi (C^3 rows) and q
    # (C^2 rows), each scaled by the field scale and the appropriate power of the interface radius
    def _dj(d):
        R = d.get("R", 1.0); ps = max(d["phi_scale"], 1e-300); qs = max(d["q_scale"], 1e-300)
        return max(abs(d["dphi"]) / ps, abs(d["dphiR"]) * R / ps, abs(d["dphiRR"]) * R * R / ps, abs(d["dq"]) / qs, abs(d["dqR"]) * R / qs)
    ifc_rel_der = max([_dj(d) for d in ifc], default=float("nan"))
    if not b2:
        cls = "F1"
    elif f6 is not None and f6 > 0.99:
        cls = "F6"
    elif math.isfinite(ifc_rel_der) and ifc_rel_der > 1e-3:
        cls = "F5"
    else:
        cls = "F7"
    # Stage II approach diagnostics (lead note 27 item 1): core scale, vorticity maximum, spectral coefficient decay per element,
    # c_l drift, far-field convergence of R^alpha U between R = 100 and R = 1000 (relative change), q0 pin, parity, exterior merge tol
    decay = {}
    for el in rep.get("spectral", []):
        for fld in ("phi", "q"):
            bn = el.get(f"{fld}_by_n") or {}
            if len(bn) >= 6:
                ks = sorted(int(k) for k in bn); third = max(1, len(ks) // 3)
                lo = max(bn[str(k)] for k in ks[:third]); hi = max(bn[str(k)] for k in ks[-third:])
                decay[f"{fld}_el{el['element']}_n"] = hi / max(lo, 1e-300)
            bk = el.get(f"{fld}_by_k") or {}
            if len(bk) >= 6:
                ks = sorted(int(k) for k in bk); third = max(1, len(ks) // 3)
                lo = max(bk[str(k)] for k in ks[:third]); hi = max(bk[str(k)] for k in ks[-third:])
                decay[f"{fld}_el{el['element']}_k"] = hi / max(lo, 1e-300)
    worst_decay = max(decay.values()) if decay else None
    tail = rep.get("RalphaU_vs_R") or []
    tail_conv = None
    try:
        t100 = [t for t in tail if abs(t["R"] - 100.0) < 1e-9][0]; t1000 = [t for t in tail if abs(t["R"] - 1000.0) < 1e-9][0]
        tail_conv = dict(pol=abs(t1000["RaUpol_rms"] - t100["RaUpol_rms"]) / max(abs(t1000["RaUpol_rms"]), 1e-300),
                         sw=abs(t1000["RaUt_rms"] - t100["RaUt_rms"]) / max(abs(t1000["RaUt_rms"]), 1e-300))
    except Exception:
        pass
    vv_full = json.load(open(vf)) if os.path.exists(vf) else {}
    extra = dict(a_eff=v.get("a_eff"), Omega_max=v.get("Omega_max"), R_Omega_max=vv_full.get("R_Omega_max"), worst_coef_decay_ratio=worst_decay,
                 cl_drift=(None if cfg.get("cl") is None or r.get("cl") is None else r.get("cl") - cfg.get("cl")),
                 tail_conv_pol_100_1000=(tail_conv or {}).get("pol"), tail_conv_sw_100_1000=(tail_conv or {}).get("sw"),
                 q0_pin=cfg.get("q0_pin"), parity=f"{cfg.get('parity_phi')}/{cfg.get('parity_q')}" if (cfg.get("parity_phi") or cfg.get("parity_q")) else "",
                 merge_tol=cfg.get("merge_tol"), rel_Rq=rep.get("rel_Rq_inner"), rel_Reta=rep.get("rel_Reta_inner"), rho_M=v.get("rho_M_max"),
                 tags=";".join(r.get("tags") or []), parent=r.get("parent") or (r.get("from_state") or "").split("/runs/")[-1].split("/")[0])
    rows.append(dict(job_id=jid, branch=r.get("branch"), stage=r.get("stage"), family=(r.get("init") or {}).get("family", "transfer"), cl_start=cfg.get("cl"),
                     cl_final=r.get("cl"), free_cl=cfg.get("free_cl", False), level=level_of(cfg), rho_max=v.get("rho_max"), m_max=v.get("m_max"), s_core=s_core, s_far=s_far,
                     B2=b2, dominant_eq=dom_eq, dominant_shell=dom_shell, cost_ratio_last20pct=f6, interface_rel_jump=ifc_rel, interface_rel_jump_derivatives=ifc_rel_der, failure_class=cls,
                     n_iter=r.get("n_iter"), gpu_hours=round((r.get("elapsed_s") or 0) / 3600, 3), finished=r.get("finished"), device=r.get("device", "cuda"), **extra))
rows.sort(key=lambda d: (d["cl_start"] or 0, d["family"], d["job_id"]))
with open(os.path.join(ROOT, "FAILURE_MAP.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(x) for x in rows]
# per c_l table
by = {}
for d in rows:
    key = round(d["cl_start"], 3)
    by.setdefault(key, []).append(d)
lines = [f"# FAILURE_MAP.md (numerics lane; SPEC 9.1 protocol). Generated {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} from {len(rows)} finished runs.", "",
         "Floor f_N(c_l) = smallest holdout rho_max among runs passing B2 (s_core >= 0.05 and s_far >= 0.05); collapsed runs (B2 fails) never define a floor.",
         "Failure classes: F1 swirl collapse; F5 interface/regularity defect > 1e-3 (since 02:10Z the derivative-aware jump: value and derivative jumps of phi and q scaled by the field scale and the interface radius; before, the phi value jump only); F6 no cost decrease over the last 20 percent of iterations; F7 plateau, none dominant.",
         "F2 (fictitious tail), F3 (stagnation-structure violation) and F4 (pressure mismatch) are assigned only from the verifier's independent checks.",
         "Iteration counts: the 'iterations' columns and n_iter are len(history) of the run record; for the six runs resumed on CPU inside an LM stage after the GPU withdrawal (fmA_cl0p73, fmAL0_cl0p74, refl_D36_cl0p74_q3p5, refl_D48_cl0p74_q3p5, refl_D36_cl0p749_q3p5, refl_D48_cl0p749_q3p5) this double counts the checkpoint prefix; the actual LM iteration counts (1500, 2500, 2500, 1600, 2500, 1600) and the recomputed last-20-percent cost ratios are in docs/RESUME_HISTORY_QUALIFICATION.md (recorded 2026-10-29T12:36Z; no class changes).", "",
         "| c_l start | runs | families | levels | floor rho_max (B2 pass) | best run | collapsed (F1) | F5 | F6 | F7 | dominant eq/shell of best | free-c_l endpoints | GPU h |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for key in sorted(by):
    g = by[key]
    fams = sorted(set(d["family"] for d in g)); levels = sorted(set(d["level"] for d in g))
    passing = [d for d in g if d["B2"] and d["rho_max"] is not None]
    best = min(passing, key=lambda d: d["rho_max"]) if passing else None
    cnt = {c: sum(1 for d in g if d["failure_class"] == c) for c in ("F1", "F5", "F6", "F7")}
    ends = sorted(set(round(d["cl_final"], 4) for d in g if d["free_cl"]))
    gpu = sum(d["gpu_hours"] for d in g)
    lines.append(f"| {key:.3f} | {len(g)} | {', '.join(fams)} | {', '.join(levels)} | {('%.2e' % best['rho_max']) if best else 'none (all collapsed)'} | {best['job_id'][:48] if best else ''} | "
                 f"{cnt['F1']} | {cnt['F5']} | {cnt['F6']} | {cnt['F7']} | {(best['dominant_eq'], best['dominant_shell']) if best else ''} | {ends if ends else ''} | {gpu:.2f} |")
tot_gpu = sum(d["gpu_hours"] for d in rows)
lines += ["", f"Total GPU hours in finished runs: {tot_gpu:.2f} (one GPU slot each; 2 jobs per GPU). Runs by class: " + ", ".join(f"{c}: {sum(1 for d in rows if d['failure_class'] == c)}" for c in ("F1", "F5", "F6", "F7")) + ".", ""]
# Stage II table (lead note 27): the T1 ladder / chain / reflection-class states, one row per (branch, c_l, level)
def is_stage2(d):
    j = d["job_id"]
    return any(j.startswith(pfx) for pfx in ("lad2", "lad3", "lad4", "chain", "fmA", "fmB", "refl", "t1lad2_cl0p740", "t1seed", "rm5")) and (d.get("q0_pin") is not None)
s2 = [d for d in rows if is_stage2(d)]
# far-field convergence of R^alpha U between R = 100 and R = 1000 for the Stage II states whose report predates the RalphaU_vs_R diagnostic
if "--no-tail" not in sys.argv:
    sys.path.insert(0, os.path.join(ROOT, "src"))
    from axi.problem import Problem
    from axi import validate as _val
    import numpy as _np
    mu = _np.cos(_np.linspace(0.03, _np.pi - 0.03, 41))
    from axi import diagnostics as _diag
    for d in s2:
        try:
            st65 = torch.load(os.path.join(ROOT, "runs", d["job_id"], "final.pt"), weights_only=False, map_location="cpu")
            prob65, x65 = Problem.from_state(st65, device="cpu")
            w65, where65, _ = _diag.interface_jumps_spec65(prob65, x65)
            d["interface_jump_spec65"] = w65; d["interface_jump_spec65_where"] = where65
            if w65 > 1e-3 and d["failure_class"] == "F7":
                d["failure_class"] = f"F7 (F5 secondary: SPEC 6.5 jump {w65:.1e})"
        except Exception:
            pass
        if d.get("tail_conv_pol_100_1000") is not None:
            continue
        try:
            st = torch.load(os.path.join(ROOT, "runs", d["job_id"], "final.pt"), weights_only=False, map_location="cpu")
            prob, x = Problem.from_state(st, device="cpu"); cl = prob.cl_of(x); al = (1 - cl) / cl
            vals = {}
            for R in (100.0, 1000.0):
                fl = _val.fields(prob, x, _np.full_like(mu, R), mu, cl)
                vals[R] = (R ** al * _np.sqrt(_np.mean(fl["Ur"] ** 2 + fl["Uz"] ** 2)), R ** al * _np.sqrt(_np.mean(fl["Ut"] ** 2)))
            d["tail_conv_pol_100_1000"] = abs(vals[1000.0][0] - vals[100.0][0]) / max(abs(vals[1000.0][0]), 1e-300)
            d["tail_conv_sw_100_1000"] = abs(vals[1000.0][1] - vals[100.0][1]) / max(abs(vals[1000.0][1]), 1e-300)
        except Exception as ex:
            pass
s2.sort(key=lambda d: (d.get("q0_pin") or 0, d.get("parity") or "", -(d["cl_final"] or 0), d["level"]))
lines += ["", "## Stage II failure map: pinned-q0 T1 branches by c_l and level (prompt Stage II approach tests; lead note 27)", "",
          "Columns: level D/nmax/K; rho_max (holdout SPEC 6.1) and its equation/shell; m_max; s_core, s_far (swirl fractions; B2 needs both >= 0.05);",
          "a_eff (core scale, reporting gauge; a core escaping to large radii would show as a_eff growing along the chain or with level);",
          "|Omega|max and its radius; worst spectral decay ratio (max coefficient in the top third of degrees over the bottom third, over elements and",
          "both fields; growth toward 1 or above means increasingly oscillatory coefficients); c_l drift (final - start, zero for fixed c_l);",
          "far-field convergence of R^alpha U between R = 100 and R = 1000 (relative change, poloidal / swirl); SPEC 6.5 interface jump (phi to total",
          "order 3 including mu-derivatives, q to order 2, 64 angles per interface, relative to the same derivative's scale on the interface; A8 needs",
          "<= 1e-6, B4 <= 1e-3; a jump above 1e-3 is recorded as 'F5 secondary' on an F7 run so the B4 failures are not hidden); SPEC 9.1 class.", "",
          "| branch (q0, parity) | c_l | level | iterations | rho_max (eq, shell) | m_max | rel R_q | rel R_eta | s_core | s_far | a_eff | max vorticity @R | worst coef decay | c_l drift | tail conv pol / sw | SPEC 6.5 jump | class | job |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def f(x, fmt):
    return (fmt % x) if isinstance(x, (int, float)) and x == x else ""
for d in s2:
    lines.append(f"| q0 {d['q0_pin']}{(' ' + d['parity']) if d['parity'] else ''} | {f(d['cl_final'], '%.4f')} | {d['level']} | {d['n_iter']} | {f(d['rho_max'], '%.2f')} ({d['dominant_eq']}, {d['dominant_shell']}) | {f(d['m_max'], '%.1f')} | "
                 f"{f(d['rel_Rq'], '%.3f')} | {f(d['rel_Reta'], '%.4f')} | {f(d['s_core'], '%.2f')} | {f(d['s_far'], '%.2f')} | {f(d['a_eff'], '%.3f')} | {f(d['Omega_max'], '%.2f')} @ {f(d['R_Omega_max'], '%.2f')} | "
                 f"{f(d['worst_coef_decay_ratio'], '%.1e')} | {f(d['cl_drift'], '%+.4f')} | {f(d['tail_conv_pol_100_1000'], '%.1e')} / {f(d['tail_conv_sw_100_1000'], '%.1e')} | {f(d.get('interface_jump_spec65'), '%.1e')} | {d['failure_class']} | {d['job_id'][:40]} |")
# SPEC 9.1 floors per (branch, c_l, level): the best B2-admissible holdout rho_max among all runs of that branch at that c_l and level
# (lead note 31 item 5: at D36 and c_l 0.749 for q0 = 3.5 this is the 1.88 L1 state, not a later continuation)
lines += ["", "## SPEC 9.1 floors per branch, c_l and level: best B2-admissible holdout rho_max (dominant equation, shell), with the number of runs", "",
          "| branch | c_l | level | runs | floor rho_max | dominant eq, shell | job |", "|---|---|---|---|---|---|---|"]
fl = {}
for d in s2:
    if not d["B2"] or d["rho_max"] is None:
        continue
    key = (f"q0 {d['q0_pin']}{(' ' + d['parity']) if d['parity'] else ''}", round(d["cl_final"], 4), d["level"] + (" Rm20" if any(float(r) > 10 for r in [d["job_id"].count("Rm20") and 20 or 10]) else ""))
    fl.setdefault(key, []).append(d)
for key in sorted(fl, key=lambda k: (k[0], -k[1], k[2])):
    g = fl[key]; best = min(g, key=lambda d: d["rho_max"])
    lines.append(f"| {key[0]} | {key[1]:.4f} | {key[2]} | {len(g)} | {best['rho_max']:.2f} | {best['dominant_eq']}, {best['dominant_shell']} | {best['job_id'][:44]} |")
# per c_l value tried in the pinned T1 class: number of finished runs and best swirl-retaining holdout rho_max (lead note 43 item 4)
lines += ["", "## T1 class (pinned q0: Stage I positive-strain ladder seeds, ladder, all chains including fmC/fmD/fmE/fmF/fmap, reflection class, direct seeds, free-c_l, outer-domain and sensitivity variants) per final c_l: finished runs and best swirl-retaining rho_max", "",
          "Swirl-retaining = swirl magnitude filter (s_core and s_far >= 0.05); runs that collapsed are counted but define no value.", "",
          "| c_l (final) | finished runs | swirl-retaining runs | best swirl-retaining rho_max (level, job) |", "|---|---|---|---|"]
def is_t1(d):
    # the whole pinned T1 class: the Stage II set plus the q0-raised chain (fmC), the chain from the 0.68 direct seed (fmD), the large-step
    # chain (fmap), the free-c_l runs of the class (freecl_*) and the Stage I positive-strain ladder seeds (t1lad_, t1lad2_ at 0.60 to 0.74)
    j = d["job_id"]
    return is_stage2(d) or (any(j.startswith(pfx) for pfx in ("fmC", "fmD", "fmE", "fmF", "fmap", "freecl", "t1lad")) and (d.get("q0_pin") is not None))   # "freecl" covers freecl_, freeclwide_, freeclmid_
t1 = [d for d in rows if is_t1(d)]
bycl = {}
for d in t1:
    bycl.setdefault(round(d["cl_final"], 4), []).append(d)
for c in sorted(bycl, reverse=True):
    g = bycl[c]; ok = [d for d in g if d["B2"] and d["rho_max"] is not None]
    best = min(ok, key=lambda d: d["rho_max"]) if ok else None
    lines.append(f"| {c:.4f} | {len(g)} | {len(ok)} | {('%.2f (%s, %s)' % (best['rho_max'], best['level'].split('-')[0], best['job_id'][:36])) if best else 'none'} |")
lines.append(f"| all | {len(t1)} | {sum(1 for d in t1 if d['B2'])} | |")
# hand-written narrative per branch (lead note 27 items 1 to 3), maintained in docs/FAILURE_MAP_NARRATIVE.md
nar = os.path.join(ROOT, "docs", "FAILURE_MAP_NARRATIVE.md")
if os.path.exists(nar):
    lines += ["", open(nar).read()]
open(os.path.join(ROOT, "FAILURE_MAP.md"), "w").write("\n".join(lines))
print("\n".join(lines[6:]))
