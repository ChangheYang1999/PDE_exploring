"""D6FP D1 / R3 (lead 23:59Z item 2): split of the far-anchor rows of R_u into (a) the stable linear part, (b) U . grad U, (c) grad P on the
verifier's input (manufactured_geometric_even, (0.42, 0.3), 20 x 38, Nr_source 48) for the coefficient columns 183, 185, 187 (failing under v1)
and 152 (control). For each term: its norm at the anchor rows (production row weights frozen at the base point), the norm of the sum, and the
noise estimate from second differences along the column at h = 1e-5, 1e-6, 1e-7 (term(z + h e) - 2 term(z) + term(z - h e)), relative to the
term's own norm and to the sum's norm; also the centered first differences (derivative share of each term). Variants: fp64 (v0), dd (v1),
dd2 (v2). Output validation/d1_term_split.json."""
import sys, os, json, time, argparse, hashlib
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case
ap = argparse.ArgumentParser(); ap.add_argument("--columns", default="152,183,185,187"); ap.add_argument("--variants", default="fp64,dd,dd2"); ap.add_argument("--tag", default="")
ap.add_argument("--input", default="RUN_ROOT/verifier/artifacts/inputs/manufactured_geometric_even")
args = ap.parse_args()
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
d = np.load(os.path.join(args.input, "coeffs.npz"), allow_pickle=True)
T = lambda a: torch.tensor(np.asarray(a, dtype=float))
arrays = dict(A=T(d["A"]), C=T(d["C"]), B=T(d["B"]), D=T(d["D"]), E=T(d["E"]), channels=json.loads(str(d["channels"])), m_parity=str(d["m_parity"]), R0=float(d["R0"]), Nk=int(d["Nk"]), Nr=48, desc="d6-ver manufactured_geometric_even")
case = Case("V045_input_split", dev, arrays=arrays, pair=(0.42, 0.3), align=False, grid=(20, 38)); prob, model = case.prob, case.model
Nr, Na = model.Nr, model.Na; npde = 3 * Nr * Na
anc_pde = case.anchor_mask[:npde]
out = dict(input=args.input, columns=[int(v) for v in args.columns.split(",")], variants=args.variants.split(","), started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), n_anchor_rows=int(anc_pde.sum()), results={})
hs = [1e-5, 1e-6, 1e-7]
def terms_at(zf):
    ev = prob.evaluate(zf, tables=prob.pressure_tables_at(zf)); mt = ev["mom_terms"]; F = ev["F"]
    adv = torch.einsum('m...,mi...->i...', F["U"], F["GU"])
    t = dict(lin_stable=mt["lin_stable"], U_gradU=adv, gradP=mt["gradP"], sum=mt["sum"])
    return {k: v.reshape(-1)[anc_pde] for k, v in t.items()}
for var in out["variants"]:
    prob.pressure.chain_precision = "dd" if var in ("dd", "dd2") else "fp64"
    prob.source_precision = "dd" if var == "dd2" else "fp64"
    r, aux = prob.objective_at(case.z_full); prob.commit_aux(aux)
    with torch.no_grad():
        base = terms_at(case.z_full)
        Wrow = r[case.anchor_mask] / torch.where(base["sum"].abs() > 0, base["sum"], torch.ones_like(base["sum"]))      # production row weights at the base point
        Wrow = torch.where(base["sum"].abs() > 0, Wrow, torch.zeros_like(Wrow))
    res_var = dict(weight_check=float((Wrow * base["sum"] - r[case.anchor_mask]).norm() / r[case.anchor_mask].norm()), r_anchor_norm=float(r[case.anchor_mask].norm()),
                   base_norms_weighted={k: float((Wrow * v).norm()) for k, v in base.items()}, base_norms_raw={k: float(v.norm()) for k, v in base.items()}, columns={})
    for k in out["columns"]:
        e = torch.zeros_like(case.z_phys); e[k] = 1.0
        rec = {}
        with torch.no_grad():
            for h in hs:
                tp = terms_at(case.to_full_phys(case.z_phys + h * e)); tm = terms_at(case.to_full_phys(case.z_phys - h * e))
                rec[f"{h:.0e}"] = {}
                for nm in base:
                    D2 = Wrow * (tp[nm] - 2 * base[nm] + tm[nm]); D1 = Wrow * (tp[nm] - tm[nm]) / (2 * h)
                    rec[f"{h:.0e}"][nm] = dict(second_difference_norm=float(D2.norm()), rel_to_own=float(D2.norm() / max(float((Wrow * base[nm]).norm()), 1e-300)),
                                             rel_to_sum=float(D2.norm() / max(float((Wrow * base["sum"]).norm()), 1e-300)), first_difference_norm=float(D1.norm()))
        res_var["columns"][str(k)] = rec
        line = " | ".join(f"{nm}: " + " ".join(f"{rec[f'{h:.0e}'][nm]['rel_to_sum']:.1e}" for h in hs) for nm in ("lin_stable", "U_gradU", "gradP", "sum"))
        print(f"[{var}] col {k}: second-difference noise / |sum| at h 1e-5,1e-6,1e-7: {line}; derivative shares (first diff at 1e-5) " + " ".join(f"{nm} {rec['1e-05'][nm]['first_difference_norm']:.2e}" for nm in ("lin_stable", "U_gradU", "gradP", "sum")), flush=True)
    print(f"[{var}] base weighted norms: " + " ".join(f"{k} {v:.3e}" for k, v in res_var["base_norms_weighted"].items()) + f"; weight check {res_var['weight_check']:.1e}", flush=True)
    out["results"][var] = res_var
prob.pressure.chain_precision = "fp64"; prob.source_precision = "fp64"
json.dump(out, open(os.path.join(MYROOT, "validation", f"d1_term_split{args.tag}.json"), "w"), indent=1)
print("DONE")
