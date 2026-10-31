"""D6FP D1 / Test T (lead 00:25:26Z item 2, fixed before it runs): for S01, S05, S09, S20 and the V027 input, at z and z +- h e for two random
unit coefficient directions (parameters fixed), h = 1e-6 and 1e-8, the self-consistent residual r in fp64 and in dd2 (double-double source and
chain). Per block b: n_b = ||d2_fp64 - d2_dd2||_b / (sqrt(6) ||r_b||) with d2 the second difference (the h-independent fp64 noise of one
evaluation; valid if the two h agree within a factor 3); c_b(x) = ||D_b(x)|| / ||r_b|| at all five points, D = r_fp64 - r_dd2; cos(D_b(z),
D_b(z + h e)) at h = 1e-8; O1 change at all five points with sign and the split of 2 r . D by block. T2: for every block whose c_b(z) exceeds
its limit (1e-12; anchors 1e-11): (i) c_b(z) <= 2 n_b; (ii) |cos| <= 0.5 and c_b(z + h e) / c_b(z) in [1/3, 3]; O1 at S09: the five signed
changes not all of one sign, or |mean| < std. Output validation/d1_test_T.json."""
import sys, os, json, time, math
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
import glob
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
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
def limit(nm):
    return 1e-11 if nm == "far_anchor_block" else 1e-12
def run(name, case):
    prob = case.prob; zp = case.z_phys
    rng = np.random.default_rng(3)
    E = []
    for t in range(2):
        e = torch.tensor(rng.normal(size=zp.numel()), device=dev); e[-2:] = 0; E.append(e / e.norm())
    def ev(precision, q):
        prob.source_precision = "dd" if precision == "dd2" else "fp64"; prob.pressure.chain_precision = "dd" if precision == "dd2" else "fp64"
        with torch.no_grad():
            return prob.objective_at(case.to_full_phys(q), need_aux=False)[0]
    pts = {"z": zp}
    for h in (1e-6, 1e-8):
        for k, e in enumerate(E):
            pts[f"+{h:.0e}e{k}"] = zp + h * e; pts[f"-{h:.0e}e{k}"] = zp - h * e
    R = {p: {} for p in ("fp64", "dd2")}
    for p in R:
        for nm, q in pts.items():
            R[p][nm] = ev(p, q)
    prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
    blk = blocks_of(case); r0 = R["fp64"]["z"]
    rec = dict(blocks={}, O1={})
    for b, m in blk.items():
        nb = float(r0[m].norm())
        if nb == 0.0:
            rec["blocks"][b] = dict(norm=0.0, note="zero block norm (gauge row satisfied): n/a"); continue
        noise = {}
        for h in (1e-6, 1e-8):
            vals = []
            for k in range(2):
                d2f = R["fp64"][f"+{h:.0e}e{k}"] - 2 * R["fp64"]["z"] + R["fp64"][f"-{h:.0e}e{k}"]
                d2d = R["dd2"][f"+{h:.0e}e{k}"] - 2 * R["dd2"]["z"] + R["dd2"][f"-{h:.0e}e{k}"]
                vals.append(float((d2f[m] - d2d[m]).norm()) / (math.sqrt(6.0) * nb))
            noise[f"{h:.0e}"] = max(vals)
        n_b = max(noise.values()); valid = (max(noise.values()) / max(min(noise.values()), 1e-300)) <= 3.0
        c = {}; cosv = {}
        for nm in ("z", "+1e-08e0", "-1e-08e0", "+1e-08e1", "-1e-08e1"):
            Dx = (R["fp64"][nm] - R["dd2"][nm])[m]; c[nm] = float(Dx.norm()) / nb
        D0 = (R["fp64"]["z"] - R["dd2"]["z"])[m]
        for nm in ("+1e-08e0", "+1e-08e1"):
            Dx = (R["fp64"][nm] - R["dd2"][nm])[m]
            cosv[nm] = float((D0 @ Dx) / max(float(D0.norm() * Dx.norm()), 1e-300))
        exceeds = c["z"] > limit(b)
        t2 = None
        if exceeds:
            ratios = [c[nm] / max(c["z"], 1e-300) for nm in ("+1e-08e0", "-1e-08e0", "+1e-08e1", "-1e-08e1")]
            t2 = dict(i_c_le_2n=bool(c["z"] <= 2 * n_b), ii_cos_le_half=bool(max(abs(v) for v in cosv.values()) <= 0.5), ii_ratio_in_range=bool(all(1 / 3 <= v <= 3 for v in ratios)), ratios=ratios)
            t2["pass"] = bool(t2["i_c_le_2n"] and t2["ii_cos_le_half"] and t2["ii_ratio_in_range"])
        rec["blocks"][b] = dict(norm=nb, n_rows=int(m.sum()), noise_n_b=noise, n_b=n_b, noise_valid_factor3=bool(valid), c_b=c, cos_D0_Dh=cosv, limit=limit(b), exceeds_limit=bool(exceeds), T2=t2)
    # O1 changes at the five points (signed, relative) and the split of 2 r . D by block at z
    o = {}
    for nm in ("z", "+1e-08e0", "-1e-08e0", "+1e-08e1", "-1e-08e1"):
        rf = R["fp64"][nm]; rd = R["dd2"][nm]; o[nm] = (float(rf @ rf) - float(rd @ rd)) / float(rf @ rf)
    vals = list(o.values()); mean = sum(vals) / len(vals); std = math.sqrt(sum((v - mean) ** 2 for v in vals) / len(vals))
    D = R["fp64"]["z"] - R["dd2"]["z"]
    split = {b: float(2 * (r0[m] @ D[m])) / float(r0 @ r0) for b, m in blk.items()}
    rec["O1"] = dict(rel_change_signed=o, mean=mean, std=std, all_one_sign=bool(all(v > 0 for v in vals) or all(v < 0 for v in vals)), passes_sign_rule=bool((not (all(v > 0 for v in vals) or all(v < 0 for v in vals))) or abs(mean) < std),
                     split_2rD_by_block=split, exceeds_1e13=bool(abs(o["z"]) > 1e-13))
    rec["T2_all_pass"] = all((v.get("T2") is None or v["T2"]["pass"]) for v in rec["blocks"].values() if "norm" in v and v["norm"] > 0) and ((not rec["O1"]["exceeds_1e13"]) or rec["O1"]["passes_sign_rule"])
    print(name, json.dumps({b: (f"c {v['c_b']['z']:.2e}", f"n {v['n_b']:.2e}", "valid" if v["noise_valid_factor3"] else "noise-unstable", ("T2 " + ("pass" if v["T2"]["pass"] else "FAIL")) if v.get("T2") else "within limit") for b, v in rec["blocks"].items() if "c_b" in v}),
          "O1", {k: f"{v:+.2e}" for k, v in o.items()}, "sign rule", rec["O1"]["passes_sign_rule"], "T2 all", rec["T2_all_pass"], flush=True)
    return rec
out = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), cases={})
starts = dict(S01="S01_nest6_cl0.45_om1.0_p0.pt", S05="S05_nest6_cl0.45_om0.3_p0.pt")
for key in ("S09", "S20"):
    m = sorted(glob.glob(os.path.join(ROOT, "starts", f"{key}_*.pt"))); starts[key] = os.path.basename(m[0]) if m else None
for key in ("S01", "S05", "S09", "S20"):
    if starts[key] is None:
        continue
    case = Case(key, dev, start=os.path.join(ROOT, "starts", starts[key])); out["cases"][key] = dict(start=starts[key], **run(key, case)); del case; torch.cuda.empty_cache()
inp = "RUN_ROOT/verifier/artifacts/inputs/manufactured_geometric_even"
d = np.load(os.path.join(inp, "coeffs.npz"), allow_pickle=True); T = lambda a: torch.tensor(np.asarray(a, dtype=float))
arrays = dict(A=T(d["A"]), C=T(d["C"]), B=T(d["B"]), D=T(d["D"]), E=T(d["E"]), channels=json.loads(str(d["channels"])), m_parity=str(d["m_parity"]), R0=float(d["R0"]), Nk=int(d["Nk"]), Nr=48, desc="V027 input")
case = Case("V027", dev, arrays=arrays, pair=(0.42, 0.3), align=False, grid=(20, 38)); out["cases"]["V027_input"] = dict(start=inp, **run("V027_input", case))
out["T2_all_pass_all_cases"] = all(v["T2_all_pass"] for v in out["cases"].values())
json.dump(out, open(os.path.join(MYROOT, "validation", "d1_test_T.json"), "w"), indent=1)
print("DONE T2 all cases:", out["T2_all_pass_all_cases"])
