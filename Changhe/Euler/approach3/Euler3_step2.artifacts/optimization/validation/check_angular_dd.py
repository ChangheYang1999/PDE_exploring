"""D6FP G5(c): double-double angular tables vs the verifier's 70-digit reference (binary64-rounded) at all 2812 training nodes of the nest6
representation (modes to degree 15; value, 3 gradient and 9 Hessian entries) and vs the frozen float64 tables; SPEC normalization
max(|ref|, 1e-13 x max |ref| of the same degree and derivative order)."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.bases.solid_harmonics import eval_solid_fp64, eval_solid as eval_solid_production
from src.bases.solid_harmonics_dd import eval_solid_dd
z = np.load("RUN_ROOT/verifier/artifacts/angular_tables_nest_v1.npz", allow_pickle=True)
pts = torch.tensor(z["points"]); modes = [tuple(int(v) for v in m) for m in z["modes"]]; ref = z["reference_float64"]; prod_v = z["production"]
L = max(m[0] for m in modes); dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z if torch.cuda.is_available() else "cpu"
def table(A0, A1, A2):
    return np.concatenate([A0.cpu().numpy()[:, :, None], A1.permute(1, 2, 0).cpu().numpy(), A2.permute(2, 3, 0, 1).cpu().numpy().reshape(A0.shape[0], len(modes), 9)], axis=2)
t0 = time.time(); A = eval_solid_fp64(pts.to(dev), modes, L, 2); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_fp = time.time() - t0
C = eval_solid_production(pts.to(dev), modes, L, 2, path="dd"); (torch.cuda.synchronize() if torch.cuda.is_available() else None)
t0 = time.time(); B = eval_solid_dd(pts.to(dev), modes, L, 2); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_dd = time.time() - t0
T_fp = table(*A); T_dd = table(*B); T_pr = table(*C)
print(f"frozen float64 tables: {t_fp:.2f}s; double-double tables: {t_dd:.2f}s; shapes {T_dd.shape}; frozen == verifier production copy: {np.array_equal(T_fp, prod_v)} (max diff {np.abs(T_fp - prod_v).max():.2e})")
deg = np.array([m[0] for m in modes]); order = np.array([0] + [1] * 3 + [2] * 9)
def normalized(T):
    """SPEC G5 (c) normalization max(|ref|, 1e-13 x max |ref| of the same degree and derivative order); identically zero blocks (e.g. second
    derivatives of degree-1 modes) are excluded (entries undefined; reported separately)."""
    err = np.abs(T - ref); out = np.full_like(err, np.nan)
    for l in np.unique(deg):
        for o in (0, 1, 2):
            mm = np.broadcast_to((deg == l)[None, :, None] & (order == o)[None, None, :], err.shape)
            scale = np.abs(ref[:, deg == l][:, :, order == o]).max()
            if scale == 0:
                continue
            out[mm] = (err / np.maximum(np.abs(ref), 1e-13 * scale))[mm]
    return out
def summarize(nrm, T):
    defined = ~np.isnan(nrm); zero_block = (~defined).sum()
    return dict(max_normalized=float(np.nanmax(nrm)), fails=int((nrm[defined] > 1e-13).sum()), defined_entries=int(defined.sum()), zero_block_entries=int(zero_block),
                zero_block_exact=bool(np.all(T[~defined] == ref[~defined])), max_abs=float(np.abs(T - ref).max()))
n_fp = normalized(T_fp); n_dd = normalized(T_dd); n_pv = normalized(prod_v); n_pr = normalized(T_pr)
s_fp, s_dd, s_pv, s_pr = summarize(n_fp, T_fp), summarize(n_dd, T_dd), summarize(n_pv, prod_v), summarize(n_pr, T_pr)
print("eval_solid_fp64 (frozen float64 path, this GPU):", s_fp); print("verifier's production copy (CPU float64):", s_pv); print("eval_solid_dd:", s_dd); print("production eval_solid (path dd):", s_pr)
print(f"exact matches dd vs reference: {(T_dd == ref).mean() * 100:.3f} per cent; frozen GPU vs verifier CPU copy max diff {np.abs(T_fp - prod_v).max():.2e} (float64 evaluation order differs between devices)")
json.dump(dict(t_fp=t_fp, t_dd=t_dd, eval_solid_fp64_gpu=s_fp, verifier_production_copy_cpu_fp64=s_pv, eval_solid_dd=s_dd, production_eval_solid=s_pr, entries=int(n_dd.size), note_verifier_V020_fail_count=3696,
               reference="d6-ver artifacts/angular_tables_nest_v1.npz (70-digit exact polynomials, rounded once)"), open(os.path.join(os.path.dirname(__file__), "check_angular_dd.json"), "w"), indent=1)
