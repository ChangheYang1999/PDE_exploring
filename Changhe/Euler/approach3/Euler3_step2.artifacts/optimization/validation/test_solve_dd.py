"""D6FP D1: solve_dd (double-double pressure chain) against solve (float64) and against a 40-digit mpmath evaluation of the same chain on a
few far-anchor entries; cost of both paths. Run on S01 (nest6 configuration)."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch, numpy as np, mpmath as mp
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.equations import residuals as res
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model = case.prob, case.model
ps = prob.pressure
with torch.no_grad():
    F = model.fields_grid(case.z_full, need_vort=False); f = res.pressure_source(F["GU"])
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); P, G, Plm, dPlm = ps.solve(f); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t64 = time.time() - t0
    t0 = time.time(); Pd, Gd, Plmd, dPlmd = ps.solve_dd(f); (torch.cuda.synchronize() if torch.cuda.is_available() else None); tdd = time.time() - t0
    for _ in range(2):
        t0 = time.time(); ps.solve_dd(f); (torch.cuda.synchronize() if torch.cuda.is_available() else None); tdd = min(tdd, time.time() - t0)
out = dict(t_fp64=t64, t_dd=tdd, n_eval_radii=int(P.shape[0]), anchors=ps.anchor_radii)
r = ps.eval_model.r
def rel(a, b, mask):
    return float((a[mask] - b[mask]).norm() / max(float(b[mask].norm()), 1e-300))
near = r <= 2 * model.R0; core = (r > 2 * model.R0) & (r <= 100 * model.R0); far = (r > 100 * model.R0) & (~ps.anchor_rows); anc = ps.anchor_rows
out["P_rel_diff"] = dict(near=rel(P, Pd, near), core=rel(P, Pd, core), far=rel(P, Pd, far), anchors=rel(P, Pd, anc))
out["gradP_rel_diff"] = dict(near=rel(G, Gd, near[None].expand(3, -1)[..., None].expand(-1, -1, G.shape[-1])), core=rel(G, Gd, core[None].expand(3, -1)[..., None].expand(-1, -1, G.shape[-1])),
                            far=rel(G, Gd, far[None].expand(3, -1)[..., None].expand(-1, -1, G.shape[-1])), anchors=rel(G, Gd, anc[None].expand(3, -1)[..., None].expand(-1, -1, G.shape[-1])))
out["Plm_rel_diff_per_anchor"] = {f"{float(r[i]):.4e}": float((Plm[i] - Plmd[i]).norm() / Plmd[i].norm()) for i in range(len(r)) if bool(anc[i])}
out["Plm_rel_diff_l_le_1_per_anchor"] = {}
l_arr = ps.pl
for i in range(len(r)):
    if bool(anc[i]):
        m = l_arr <= 1
        out["Plm_rel_diff_l_le_1_per_anchor"][f"{float(r[i]):.4e}"] = float((Plm[i][m] - Plmd[i][m]).norm() / max(float(Plmd[i][m].norm()), 1e-300))
# mpmath check of the chain on one anchor radius for the l = 0 and the first l = 1 mode (same float64 inputs, exact arithmetic)
mp.mp.dps = 40
T = ps.tables
i_anchor = int(torch.nonzero(anc)[-1]); fnp = f[: ps.Nr_src].cpu().numpy(); A0pw = ps.A0pw.cpu().numpy(); cosb = T["cosb"].cpu().numpy(); sinb = T["sinb"].cpu().numpy()
sfac = T["sfac"].cpu().numpy(); lfac = ps.lfac.cpu().numpy(); partner = ps.partner.cpu().numpy(); sign = ps.sign.cpu().numpy()
Qc = T["Qc"][ps.pl_long, ps.pm].cpu().numpy(); Qs = T["Qs"][ps.pl_long, ps.pm].cpu().numpy()
Nr, Nqp = fnp.shape[0], A0pw.shape[1]
def mpf(x): return mp.mpf(float(x))
checks = {}
for q in [int(torch.nonzero(l_arr == 0)[0]), int(torch.nonzero(l_arr == 1)[0])]:
    flm = [mp.fsum(mpf(fnp[k, a]) * mpf(A0pw[a, q]) for a in range(fnp.shape[1])) for k in range(Nr)]
    flp = [mp.fsum(mpf(fnp[k, a]) * mpf(A0pw[a, partner[q]]) for a in range(fnp.shape[1])) for k in range(Nr)]
    cb = cosb if cosb.ndim == 2 else np.broadcast_to(cosb, (Nr, Nqp)); sb = sinb if sinb.ndim == 2 else np.broadcast_to(sinb, (Nr, Nqp))
    ftw = [(flm[k] * mpf(cb[k, q]) - mpf(sign[q]) * flp[k] * mpf(sb[k, q])) * mpf(sfac[k]) * mpf(lfac[k, q]) for k in range(Nr)]
    # partner's own twisted value
    flpp = [mp.fsum(mpf(fnp[k, a]) * mpf(A0pw[a, partner[partner[q]]]) for a in range(fnp.shape[1])) for k in range(Nr)]
    ftw_p = [(flp[k] * mpf(cb[k, partner[q]]) - mpf(sign[partner[q]]) * flpp[k] * mpf(sb[k, partner[q]])) * mpf(sfac[k]) * mpf(lfac[k, partner[q]]) for k in range(Nr)]
    t1 = mp.fsum(mpf(Qc[q, 0, i_anchor, k]) * ftw[k] for k in range(Nr)) + mpf(sign[q]) * mp.fsum(mpf(Qs[q, 0, i_anchor, k]) * ftw_p[k] for k in range(Nr))
    t2 = mp.fsum(mpf(Qc[q, 1, i_anchor, k]) * ftw[k] for k in range(Nr)) + mpf(sign[q]) * mp.fsum(mpf(Qs[q, 1, i_anchor, k]) * ftw_p[k] for k in range(Nr))
    ref = t1 + t2
    scale = mp.fsum(abs(mpf(Qc[q, j, i_anchor, k]) * ftw[k]) for k in range(Nr) for j in (0, 1))
    checks[f"l={int(l_arr[q])} q={q} r={float(r[i_anchor]):.3e}"] = dict(mp=float(ref), fp64=float(Plm[i_anchor, q]), dd=float(Plmd[i_anchor, q]), abs_scale=float(scale),
                                                                     err_fp64_rel_to_abs=float(abs(mpf(Plm[i_anchor, q]) - ref) / scale), err_dd_rel_to_abs=float(abs(mpf(Plmd[i_anchor, q]) - ref) / scale),
                                                                     err_fp64_rel=float(abs(mpf(Plm[i_anchor, q]) - ref) / abs(ref)), err_dd_rel=float(abs(mpf(Plmd[i_anchor, q]) - ref) / abs(ref)))
out["mpmath_checks"] = checks
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(ROOT, "validation", "test_solve_dd_S01.json"), "w"), indent=1)
