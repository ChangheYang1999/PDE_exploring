#!/usr/bin/env python
"""Bitwise comparison of two all-m table captures (lead 13:56:28Z item 3 (a)): the GPU capture (frozen copy) against the CPU capture: for every distinct
call tag the points, modes and the production tables A0/A1/A2 must be bitwise equal (uint64 view). Usage:
python validation/g5c_allm_gpu_vs_cpu.py <gpu capture json> <cpu capture json>   -> validation/g5c_allm_gpu_vs_cpu_<case>.json"""
import sys, os, json, hashlib
import numpy as np

def bits_equal(a, b):
    a = np.ascontiguousarray(a); b = np.ascontiguousarray(b)
    if a.shape != b.shape or a.dtype != b.dtype:
        return False
    return bool(np.array_equal(a.view(np.uint8), b.view(np.uint8)))

def main():
    gj, cj = sys.argv[1], sys.argv[2]
    G = json.load(open(gj)); C = json.load(open(cj))
    zg = np.load(G["arrays_npz"]); zc = np.load(C["arrays_npz"])
    out = dict(case=G["case"], gpu_capture=dict(json=gj, sha256=hashlib.sha256(open(gj, "rb").read()).hexdigest(), npz=G["arrays_npz"], npz_sha256=G["arrays_sha256"], device=G["device"]),
               cpu_capture=dict(json=cj, sha256=hashlib.sha256(open(cj, "rb").read()).hexdigest(), npz=C["arrays_npz"], npz_sha256=C["arrays_sha256"], device=C["device"]), sets={})
    tags_g = sorted({k.split("_")[0] for k in zg.files if k.startswith("call")}); tags_c = sorted({k.split("_")[0] for k in zc.files if k.startswith("call")})
    out["same_tags"] = (tags_g == tags_c); allok = out["same_tags"]
    # match sets by (points, modes) content rather than by tag order
    for tg in tags_g:
        pg, mg = zg[f"{tg}_points"], zg[f"{tg}_modes"]; match = None
        keys_g = {nm for nm in ("A0", "A1", "A2") if f"{tg}_{nm}" in zg.files}
        for tc in tags_c:
            keys_c = {nm for nm in ("A0", "A1", "A2") if f"{tc}_{nm}" in zc.files}
            if keys_g == keys_c and bits_equal(pg, zc[f"{tc}_points"]) and bits_equal(mg, zc[f"{tc}_modes"]):      # same points, modes and derivative order (table keys)
                match = tc; break
        rec = dict(matched_cpu_tag=match, n_points=int(pg.shape[0]), n_modes=int(mg.shape[0]))
        if match is None:
            rec["points_modes_match"] = False; allok = False
        else:
            rec["points_modes_match"] = True
            for nm in ("A0", "A1", "A2"):
                kg, kc = f"{tg}_{nm}", f"{match}_{nm}"
                if kg in zg.files or kc in zc.files:
                    eq = (kg in zg.files and kc in zc.files) and bits_equal(zg[kg], zc[kc]); rec[f"{nm}_bitwise"] = bool(eq); allok = allok and bool(eq)
                    if not eq and kg in zg.files and kc in zc.files and zg[kg].shape == zc[kc].shape:
                        d = np.abs(zg[kg] - zc[kc]); rec[f"{nm}_max_abs_diff"] = float(d.max()); rec[f"{nm}_n_diff"] = int((d > 0).sum())
        out["sets"][tg] = rec
    out["all_bitwise_equal"] = bool(allok); out["npz_sha256_equal"] = (G["arrays_sha256"] == C["arrays_sha256"])
    outp = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"g5c_allm_gpu_vs_cpu_{G['case']}.json")
    json.dump(out, open(outp, "w"), indent=1); print("all bitwise equal:", out["all_bitwise_equal"], "| npz sha equal:", out["npz_sha256_equal"], json.dumps(out["sets"])[:600]); print("DONE", outp)

if __name__ == "__main__":
    main()
