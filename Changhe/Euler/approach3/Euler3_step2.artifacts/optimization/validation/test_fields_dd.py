"""D6FP D1 v2: fields_dd (double-double accumulation of DU and tr(DU^2)) on S01: (1) fh + fl against the float64 source; (2) exact reference at
three grid nodes from the same float64 inputs (radial arrays, angular tables, r, n) in 40-digit mpmath; (3) forward-mode tangent of source_dd
in a coefficient direction against the float64 tangent and against double-double differences (linear map); parameter direction against the float64
tangent; (4) vmap over jvp; (5) reverse mode against float64; (6) timings; (7) the full residual with source_precision = "dd" against fp64."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch, numpy as np, mpmath as mp
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.equations import residuals as res
from src.equations import fields_dd as FD
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model = case.prob, case.model
z = case.z_full; out = {}
with torch.no_grad():
    F = model.fields_grid(z, need_vort=False); f64 = res.pressure_source(F["GU"])
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); fh, fl = FD.pressure_source_dd(model, z); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_source_dd"] = time.time() - t0
    t0 = time.time(); model.fields_grid(z, need_vort=False); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_fields_fp64"] = time.time() - t0
out["f_rel_diff_dd_vs_fp64"] = float((fh + fl - f64).norm() / f64.norm()); out["f_max_rel_entry_diff"] = float(((fh + fl - f64).abs() / f64.abs().clamp_min(1e-300)).median())
# (2) mpmath reference at three nodes: GU from the float64 radial arrays and tables exactly
mp.mp.dps = 40
d = model.unpack_all(z)
with torch.no_grad():
    (gTh, gTl), (gSh, gSl) = FD.radial_derivs_dd(model, d)
    gT64, gS64 = model.radial_derivs(d["A"], d["C"], d["c_l"], d["omega"], K=4, extra=d)
out["radial_dd_vs_fp64_rel"] = dict(gT=float((gTh + gTl - gT64).norm() / gT64.norm()), gS=float((gSh + gSl - gS64).norm() / gS64.norm()))
# exact reference of the twisted radial arrays at one node and two modes from the float64 tables (contraction and twist in 40 digits)
import math as _math
from src.equations.fields import alpha_of
with torch.no_grad():
    alpha_t = alpha_of(d["c_l"]); R0t = torch.tensor(model.R0, dtype=torch.float64, device=dev); ch = model.channels
    BT = model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, 4, shift=0.0).cpu().numpy(); BS = model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, 4, shift=1.0).cpu().numpy()
    BB = model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, 4, power=lambda l: 2 * alpha_t + 1 + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkB"]).cpu().numpy() if ch["NkB"] > 0 else None
    BD = model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, 4, power=lambda l: 2 * alpha_t + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkD"]).cpu().numpy() if ch["NkD"] > 0 else None
    BE = model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, 4, power=lambda l: torch.as_tensor(2.0 * l + 1.0, dtype=torch.float64, device=dev), core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkE"], lmask=[0, 1]).cpu().numpy() if ch["NkE"] > 0 else None
    Ct, St = model.rb.twist_tables(model.rho, d["omega"], d["c_l"], R0t, model.Mmax, 4); Ct = Ct.cpu().numpy(); St = St.cpu().numpy()
A_np = d["A"].cpu().numpy(); C_np = d["C"].cpu().numpy(); B_np = d["B"].cpu().numpy(); D_np = d["D"].cpu().numpy(); E_np = d["E"].cpu().numpy()
lidx = model.l_idx.cpu().numpy(); marr = model.m_arr.cpu().numpy(); partner = model.partner.cpu().numpy(); tws = model.tw_sign.cpu().numpy()
def M(x): return mp.mpf(float(x))
def untw(q, j, which):
    if which == "T":
        g = [mp.fsum(M(BT[lidx[q], n, j, k]) * M(A_np[k, q]) for k in range(A_np.shape[0])) for n in range(5)]
        if BB is not None: g = [g[n] + mp.fsum(M(BB[lidx[q], n, j, k]) * M(B_np[k, q]) for k in range(B_np.shape[0])) for n in range(5)]
    else:
        g = [mp.fsum(M(BS[lidx[q], n, j, k]) * M(C_np[k, q]) for k in range(C_np.shape[0])) for n in range(5)]
        if BD is not None: g = [g[n] + mp.fsum(M(BD[lidx[q], n, j, k]) * M(D_np[k, q]) for k in range(D_np.shape[0])) for n in range(5)]
    return g
def twisted(q, j, which):
    g = untw(q, j, which); gp = untw(int(partner[q]), j, which); m = int(marr[q])
    outg = []
    for n in range(5):
        t = mp.mpf(0)
        for k in range(n + 1):
            t += _math.comb(n, k) * (g[k] * M(Ct[m, n - k, j]) + gp[k] * M(St[m, n - k, j]) * M(tws[q]))
        outg.append(t)
    if which == "S" and BE is not None:
        outg = [outg[n] + mp.fsum(M(BE[lidx[q], n, j, k]) * M(E_np[k, q]) for k in range(E_np.shape[0])) for n in range(5)]
    return outg
mp.mp.dps = 40
rad_checks = {}
for (q, j) in [(3, 5), (40, 24), (7, 47)]:
    gTq = twisted(q, j, "T"); gSq = twisted(q, j, "S")
    rad_checks[f"q={q} j={j}"] = dict(gT_err_dd=max(float(abs(M(gTh[n, j, q]) + M(gTl[n, j, q]) - gTq[n]) / (abs(gTq[n]) + mp.mpf(1e-300))) for n in range(5)),
                                     gT_err_fp64=max(float(abs(M(gT64[n, j, q]) - gTq[n]) / (abs(gTq[n]) + mp.mpf(1e-300))) for n in range(5)),
                                     gS_err_dd=max(float(abs(M(gSh[n, j, q]) + M(gSl[n, j, q]) - gSq[n]) / (abs(gSq[n]) + mp.mpf(1e-300))) for n in range(5)),
                                     gS_err_fp64=max(float(abs(M(gS64[n, j, q]) - gSq[n]) / (abs(gSq[n]) + mp.mpf(1e-300))) for n in range(5)))
out["radial_mpmath_checks"] = rad_checks
# the node checks below use the DOUBLE-DOUBLE radial arrays (hi + lo in 40 digits) as inputs
gT_np = None; gS_np = None
gTdd = [[[M(gTh[n, j, q]) + M(gTl[n, j, q]) for q in range(gTh.shape[2])] for j in range(gTh.shape[1])] for n in range(5)]
gSdd = [[[M(gSh[n, j, q]) + M(gSl[n, j, q]) for q in range(gSh.shape[2])] for j in range(gSh.shape[1])] for n in range(5)]
A0 = model.A0.cpu().numpy(); A1 = model.A1.cpu().numpy(); A2 = model.A2.cpu().numpy()
r_np = model.r.cpu().numpy(); n_np = model.n.cpu().numpy(); l_np = model.l_arr.cpu().numpy(); rl_np = model.rl.cpu().numpy(); rho_np = model.rho.cpu().numpy()
eps = model.eps.cpu().numpy()
def M(x): return mp.mpf(float(x))
checks = {}
for (j, a) in [(5, 17), (24, 600), (47, 1200)]:
    Nq = len(l_np); r = M(r_np[j]); nn = [M(v) for v in n_np[a]]
    def sets(g):
        # (h0, h1, h2) per mode as mp lists (g: nested mp lists [n][j][q])
        T = [[g[k][j][q] for q in range(Nq)] for k in range(3)]
        return T
    # K and D sets
    def KD(g):
        K = [[(M(l_np[q]) + 1) * g[0][j][q] + 2 * M(rho_np[j]) * g[1][j][q] for q in range(Nq)],
             [(M(l_np[q]) + 3) * g[1][j][q] + 2 * M(rho_np[j]) * g[2][j][q] for q in range(Nq)],
             [(M(l_np[q]) + 5) * g[2][j][q] + 2 * M(rho_np[j]) * g[3][j][q] for q in range(Nq)]]
        D = [[(6 + 4 * M(l_np[q])) * g[1][j][q] + 4 * M(rho_np[j]) * g[2][j][q] for q in range(Nq)],
             [(10 + 4 * M(l_np[q])) * g[2][j][q] + 4 * M(rho_np[j]) * g[3][j][q] for q in range(Nq)],
             [(14 + 4 * M(l_np[q])) * g[3][j][q] + 4 * M(rho_np[j]) * g[4][j][q] for q in range(Nq)]]
        return K, D
    T = sets(gTdd); K, D = KD(gSdd)
    def ev(h, hess=True):
        rl = [M(rl_np[j, q]) for q in range(Nq)]
        f = mp.fsum(rl[q] * h[0][q] * M(A0[a, q]) for q in range(Nq))
        G1 = mp.fsum(rl[q] * r * h[1][q] * M(A0[a, q]) for q in range(Nq)); Gm1 = [rl[q] / r * h[0][q] for q in range(Nq)]
        grad = [2 * G1 * nn[i] + mp.fsum(Gm1[q] * M(A1[i, a, q]) for q in range(Nq)) for i in range(3)]
        if not hess:
            return f, grad, None
        G2 = mp.fsum(rl[q] * r * r * h[2][q] * M(A0[a, q]) for q in range(Nq)); H1 = [rl[q] * h[1][q] for q in range(Nq)]
        H1A0 = mp.fsum(H1[q] * M(A0[a, q]) for q in range(Nq)); H1A1 = [mp.fsum(H1[q] * M(A1[i, a, q]) for q in range(Nq)) for i in range(3)]
        Hm2 = [rl[q] / (r * r) * h[0][q] for q in range(Nq)]
        hs = [[4 * G2 * nn[i] * nn[k] + 2 * ((H1A0 if i == k else 0) + H1A1[k] * nn[i] + H1A1[i] * nn[k]) + mp.fsum(Hm2[q] * M(A2[i, k, a, q]) for q in range(Nq)) for k in range(3)] for i in range(3)]
        return f, grad, hs
    _, gT_, hT_ = ev(T); _, _, hK = ev(K); dD, gD, _ = ev(D, False)
    y = [r * nn[i] for i in range(3)]
    GU = [[hK[m][i] - mp.fsum(M(eps[i, m, k]) * gT_[k] for k in range(3)) - mp.fsum(M(eps[i, jj, k]) * y[jj] * hT_[m][k] for jj in range(3) for k in range(3)) - (dD if m == i else 0) - y[i] * gD[m] for i in range(3)] for m in range(3)]
    fref = mp.fsum(GU[m][i] * GU[i][m] for m in range(3) for i in range(3))
    scale = mp.fsum(abs(GU[m][i] * GU[i][m]) for m in range(3) for i in range(3))
    checks[f"node r={float(r_np[j]):.3e} a={a}"] = dict(ref=float(fref), fp64=float(f64[j, a]), dd=float(fh[j, a]) , err_fp64_rel=float(abs(M(f64[j, a]) - fref) / abs(fref)), err_dd_rel=float(abs(M(fh[j, a]) + M(fl[j, a]) - fref) / abs(fref)),
                                                       cancellation_ratio=float(abs(fref) / scale))
out["mpmath_checks"] = checks
# (3) tangents
rng = np.random.default_rng(7); n = z.numel()
e = torch.tensor(rng.normal(size=n), device=dev); e[-2:] = 0; e = e / e.norm()
fun_dd = lambda zz: (lambda o: o[0] + o[1])(FD.source_dd(model, zz))
fun_64 = lambda zz: res.pressure_source(model.fields_grid(zz, need_vort=False)["GU"])
_, t_dd = torch.func.jvp(fun_dd, (z,), (e,)); _, t_64 = torch.func.jvp(fun_64, (z,), (e,))
with torch.no_grad():
    h = 1e-2
    oP = FD.pressure_source_dd(model, z + h * e); oM = FD.pressure_source_dd(model, z - h * e)
    Dh = ((oP[0] - oM[0]) + (oP[1] - oM[1])) / (2 * h)                     # exact up to roundoff for a quadratic form (centered difference of a quadratic)
out["coef_tangent_dd_vs_fp64"] = float((t_dd - t_64).norm() / t_64.norm()); out["coef_tangent_dd_vs_dd_difference"] = float((t_dd - Dh).norm() / Dh.norm()); out["coef_tangent_fp64_vs_dd_difference"] = float((t_64 - Dh).norm() / Dh.norm())
ep = torch.zeros(n, device=dev); ep[-2] = 1.0
_, tp_dd = torch.func.jvp(fun_dd, (z,), (ep,)); _, tp_64 = torch.func.jvp(fun_64, (z,), (ep,))
out["param_tangent_dd_vs_fp64"] = float((tp_dd - tp_64).norm() / tp_64.norm())
# (4) vmap
E = torch.stack([e, torch.roll(e, 3)], 0)
try:
    tv = torch.func.vmap(lambda ee: torch.func.jvp(fun_dd, (z,), (ee,))[1])(E)
    out["vmap_jvp"] = dict(ok=True, rel_diff_first=float((tv[0] - t_dd).norm() / t_dd.norm()))
except Exception as ex:
    out["vmap_jvp"] = dict(ok=False, error=repr(ex)[:400])
# (5) reverse
zg = z.detach().clone().requires_grad_(True); w = torch.randn_like(f64)
g1, = torch.autograd.grad((fun_dd(zg) * w).sum(), zg); zg2 = z.detach().clone().requires_grad_(True); g2, = torch.autograd.grad((fun_64(zg2) * w).sum(), zg2)
out["reverse_rel_diff"] = float((g1 - g2).norm() / g2.norm())
# (6) timings of the jvp
(torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); torch.func.jvp(fun_dd, (z,), (e,)); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_jvp_dd"] = time.time() - t0
t0 = time.time(); torch.func.jvp(fun_64, (z,), (e,)); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_jvp_fp64"] = time.time() - t0
# (7) full residual with the dd source and chain
r0 = case.r
prob.source_precision = "dd"; prob.pressure.chain_precision = "dd"
(torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); r1, aux = prob.objective_at(z); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_objective_dd"] = time.time() - t0
prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
t0 = time.time(); r2, _ = prob.objective_at(z); (torch.cuda.synchronize() if torch.cuda.is_available() else None); out["t_objective_fp64"] = time.time() - t0
anc = case.anchor_mask
out["residual_rel_diff_dd_vs_fp64"] = dict(all=float((r1 - r2).norm() / r2.norm()), anchors=float((r1[anc] - r2[anc]).norm() / r2[anc].norm()), O1_rel=abs(float(r1 @ r1) - float(r2 @ r2)) / float(r2 @ r2))
print(json.dumps(out, indent=1))
json.dump(out, open(os.path.join(ROOT, "validation", "test_fields_dd_S01.json"), "w"), indent=1)
