"""D6FP D1 / R1-R2 invariance record (lead 23:08Z item 2, 00:06Z (a)): for S01, S05, S09, S20 and the V027 input, the change of each row block of
the self-consistent residual r and of O1 between the float64 path and v2 (double-double source and chain), relative to the block norm; and the
float64 noise estimate of each block from second differences along two coefficient directions at h = 1e-6 (as in the term split), so that a
change within twice that noise can be read as a precision gain. Output validation/d1_invariance.json."""
import sys, os, json, time
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
starts = dict(S01="S01_nest6_cl0.45_om1.0_p0.pt", S05="S05_nest6_cl0.45_om0.3_p0.pt", S09=None, S20=None)
import glob
for key in ("S09", "S20"):
    m = sorted(glob.glob(os.path.join(ROOT, "starts", f"{key}_*.pt")))
    starts[key] = os.path.basename(m[0]) if m else None
out = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), cases={})
def blocks_of(case):
    r = case.r; blk = {}
    npde = 3 * case.model.Nr * case.model.Na
    for i, nm in enumerate(case.group_names):
        m = case.row_group == i
        if nm.startswith("far(") and hasattr(case, "anchor_mask"):
            m = m & ~case.anchor_mask
        if m.any():
            blk[nm] = m
    blk["far_anchor_block"] = case.anchor_mask
    return blk
def run_case(name, case):
    prob = case.prob; z = case.z_full
    prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
    r0, aux0 = prob.objective_at(z)
    blk = blocks_of(case)
    # fp64 noise estimate: second differences along two random coefficient directions at h = 1e-6
    rng = np.random.default_rng(3); noise = {k: [] for k in blk}
    with torch.no_grad():
        for t in range(2):
            e = torch.tensor(rng.normal(size=case.z_phys.numel()), device=dev); e[-2:] = 0; e = e / e.norm(); h = 1e-6
            rp = prob.objective_at(case.to_full_phys(case.z_phys + h * e), need_aux=False)[0]; rm = prob.objective_at(case.to_full_phys(case.z_phys - h * e), need_aux=False)[0]
            d2 = rp - 2 * r0 + rm
            for k, m in blk.items():
                noise[k].append(float(d2[m].norm() / max(float(r0[m].norm()), 1e-300)))
    prob.source_precision = "dd"; prob.pressure.chain_precision = "dd"
    r1, aux1 = prob.objective_at(z)
    prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
    rec = dict(O1_fp64=0.5 * float(r0 @ r0), O1_dd=0.5 * float(r1 @ r1), O1_rel_change=abs(float(r1 @ r1) - float(r0 @ r0)) / float(r0 @ r0), blocks={})
    for k, m in blk.items():
        rec["blocks"][k] = dict(rel_change=float((r1[m] - r0[m]).norm() / max(float(r0[m].norm()), 1e-300)), norm=float(r0[m].norm()), n_rows=int(m.sum()),
                                fp64_noise_second_difference_h1e6=max(noise[k]), within_2x_noise=bool(float((r1[m] - r0[m]).norm() / max(float(r0[m].norm()), 1e-300)) <= 2 * max(noise[k])))
    summ = {}
    for k, v in rec["blocks"].items():
        tag = "ok" if v["rel_change"] <= 1e-12 else ("noise-level" if v["within_2x_noise"] else "EXCEEDS")
        summ[k] = ("%.2e" % v["rel_change"], "noise %.2e" % v["fp64_noise_second_difference_h1e6"], tag)
    print(name, json.dumps(summ), "O1 rel %.2e" % rec["O1_rel_change"], flush=True)
    return rec
for key in ("S01", "S05", "S09", "S20"):
    if starts[key] is None:
        continue
    case = Case(key, dev, start=os.path.join(ROOT, "starts", starts[key]))
    out["cases"][key] = dict(start=starts[key], **run_case(key, case))
    del case; torch.cuda.empty_cache()
# the V027 input (verifier's manufactured_geometric_even at (0.42, 0.3), 20 x 38, Nr_source 48)
inp = "RUN_ROOT/verifier/artifacts/inputs/manufactured_geometric_even"
d = np.load(os.path.join(inp, "coeffs.npz"), allow_pickle=True); T = lambda a: torch.tensor(np.asarray(a, dtype=float))
arrays = dict(A=T(d["A"]), C=T(d["C"]), B=T(d["B"]), D=T(d["D"]), E=T(d["E"]), channels=json.loads(str(d["channels"])), m_parity=str(d["m_parity"]), R0=float(d["R0"]), Nk=int(d["Nk"]), Nr=48, desc="V027 input")
case = Case("V027", dev, arrays=arrays, pair=(0.42, 0.3), align=False, grid=(20, 38))
out["cases"]["V027_input"] = dict(start=inp, **run_case("V027_input", case))
out["all_blocks_ok_or_noise_level"] = all(all(v["rel_change"] <= 1e-12 or v["within_2x_noise"] for v in c["blocks"].values()) for c in out["cases"].values())
out["all_O1_within_1e-13"] = all(c["O1_rel_change"] <= 1e-13 for c in out["cases"].values())
json.dump(out, open(os.path.join(MYROOT, "validation", "d1_invariance.json"), "w"), indent=1)
print("DONE", out["all_blocks_ok_or_noise_level"], out["all_O1_within_1e-13"])
