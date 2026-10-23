#!/usr/bin/env python3
"""Offline audit of a checkpoint on fresh independent point sets (EQUATIONS.md 7.3, 11).

Usage: python3 evaluate.py <ckpt.pt> [--device cuda:0] [--out report.json] [--seed 999] [--n 4096]
Computes R_m, R_div, R_omega (third derivatives), R_P with term-normalized relative residuals on radial shells,
an independent cylindrical finite-difference cross-check, symmetry/parity defects, group-average and ring Fourier
non-axisymmetry, affine fit, vorticity maximum and stretching identity, stagnation set, tail slopes along rays,
Laplacian (viscous) diagnostic, and residual sensitivity to c_l at fixed fields. Writes JSON (and prints a summary).
"""
import argparse, json, math, os, sys, time
import numpy as np
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
torch.set_default_dtype(torch.float64)
from euler_ss.model import ProfileModel, apply_Q
from euler_ss import physics as ph
from euler_ss import diagnostics as dg
from euler_ss.losses import nonaxi_ratio
from euler_ss.sampling import Sampler

SHELLS = [(0.0, 0.25), (0.25, 1.0), (1.0, 2.0), (2.0, 4.0), (4.0, 8.0), (8.0, 16.0), (16.0, 64.0), (64.0, 256.0), (256.0, 1024.0), (1024.0, 4096.0)]


def wl2(v, w):
    v = v if v.dim() == 1 else (v ** 2).sum(-1).sqrt()
    return torch.sqrt((w * v ** 2).sum()).item()


def quant(v, q):
    return torch.quantile(v, q).item() if v.numel() > 0 else float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ckpt"); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--out", default=None); ap.add_argument("--seed", type=int, default=999); ap.add_argument("--n", type=int, default=2048)
    ap.add_argument("--chunk", type=int, default=512)
    a = ap.parse_args()
    dev = torch.device(a.device)
    ck = torch.load(a.ckpt, map_location="cpu", weights_only=False)
    cfg = ck["cfg"]
    model = ProfileModel(cfg).to(dev)
    missing, unexpected = model.load_state_dict(ck["model"], strict=False)
    model.eval()
    cl = model.cl().item(); C = model.C; d = 1 - 1 / cl
    rep = {"ckpt": os.path.abspath(a.ckpt), "exp_id": ck.get("exp_id"), "saved": ck.get("saved"), "state": {k: v for k, v in ck.get("state", {}).items() if k != "interruptions"},
           "cl": cl, "d": d, "C": C, "missing_keys": list(missing), "unexpected_keys": list(unexpected), "audit_seed": a.seed, "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    f = lambda p: model.fields(p)
    # ---- fresh audit points: uniform-in-volume in each shell (physical weights), axis tube
    g = torch.Generator(); g.manual_seed(a.seed)
    pts, wts, tags = [], [], []
    for (lo, hi) in SHELLS:
        n = a.n if hi <= 16 else a.n // 2
        u = torch.rand(n, generator=g, dtype=torch.float64)
        R = (lo ** 3 + u * (hi ** 3 - lo ** 3)) ** (1 / 3)
        v = torch.randn(n, 3, generator=g, dtype=torch.float64); v = v / v.norm(dim=-1, keepdim=True)
        pts.append(R.unsqueeze(-1) * v); wts.append(torch.full((n,), 4 / 3 * math.pi * (hi ** 3 - lo ** 3) / n, dtype=torch.float64)); tags += ["shell_%g_%g" % (lo, hi)] * n
    s = Sampler({"R_core": 4.0, "R_max": 1000.0, "r_tube": 0.1, "z_min": 0.01, "R_origin": 0.5}, a.seed + 1)
    ya, wa = s.sample_region("axis", a.n); pts.append(ya); wts.append(wa); tags += ["axis_tube"] * a.n
    y = torch.cat(pts).to(dev); w = torch.cat(wts).to(dev); tags = np.array(tags)
    # ---- derivatives to third order (chunked)
    F, J, H, T = ph.derivs(f, y, order=3, chunk=a.chunk)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Rm, V, conv = ph.momentum_residual(y, U, gU, gP, cl, C)
    div = ph.divergence(gU)
    Rom, Om, gOm = ph.vorticity_residual(y, U, gU, T, cl, C)
    RP, lapP, src = ph.pressure_residual(gU, HP)
    terms = ph.momentum_terms(y, U, gU, gP, cl, C)
    VgOm = torch.einsum("nil,nl->ni", gOm, V); OmgU = torch.einsum("nik,nk->ni", gU, Om)
    # Laplacian of U from third derivatives of A: lapU_i = sum_l d_l d_l U_i
    TA = T[:, :3]
    HU = torch.stack([TA[..., 2, 1, :, :] - TA[..., 1, 2, :, :], TA[..., 0, 2, :, :] - TA[..., 2, 0, :, :], TA[..., 1, 0, :, :] - TA[..., 0, 1, :, :]], dim=-3)
    lapU = HU[..., 0, 0] + HU[..., 1, 1] + HU[..., 2, 2]
    Tn = ph.term_scale(y, cl, lam=1.0, l_env=model.l_env)
    regions = {}
    for tg in sorted(set(tags.tolist()), key=lambda t: tags.tolist().index(t)):
        m = torch.tensor(tags == tg, device=dev)
        ww = w[m]
        den_m = wl2(terms["lin"][m], ww) + wl2(terms["cl_ygradU"][m], ww) + wl2(terms["C_dzU"][m], ww) + wl2(terms["UgradU"][m], ww) + wl2(gP[m], ww)
        den_nl = wl2(terms["UgradU"][m], ww) + wl2(gP[m], ww)
        den_om = wl2(Om[m], ww) + wl2(VgOm[m], ww) + wl2(OmgU[m], ww)
        den_P = wl2(lapP[m], ww) + wl2(src[m], ww)
        rn = Rm[m].norm(dim=-1)
        regions[tg] = {"n": int(m.sum().item()),
                       "eps_m": wl2(Rm[m], ww) / den_m if den_m > 0 else None, "eps_nl": wl2(Rm[m], ww) / den_nl if den_nl > 0 else None,
                       "eps_div": wl2(div[m], ww) / wl2(gU[m].reshape(-1, 9), ww), "eps_omega": wl2(Rom[m], ww) / den_om if den_om > 0 else None,
                       "eps_P": wl2(RP[m], ww) / den_P if den_P > 0 else None,
                       "Rm_rms_nlscale": (rn / Tn[m]).pow(2).mean().sqrt().item(), "Rm_q99_nlscale": quant(rn / Tn[m], 0.99), "Rm_q999_nlscale": quant(rn / Tn[m], 0.999), "Rm_max_nlscale": (rn / Tn[m]).max().item(),
                       "Rm_abs_rms": rn.pow(2).mean().sqrt().item(), "Rm_abs_max": rn.max().item(), "div_abs_max": div[m].abs().max().item(),
                       "lapU_over_terms": wl2(lapU[m], ww) / den_m if den_m > 0 else None,
                       "den_m": den_m, "den_nl": den_nl}
    rep["regions"] = regions
    # ---- independent cylindrical finite-difference cross-check (derivatives in (r,theta,z) by 4th-order central FD)
    gc = torch.Generator(); gc.manual_seed(a.seed + 2)
    nc = 512
    r = 0.3 + 3.0 * torch.rand(nc, generator=gc, dtype=torch.float64); th = 2 * math.pi * torch.rand(nc, generator=gc, dtype=torch.float64); z = 3.0 * (2 * torch.rand(nc, generator=gc, dtype=torch.float64) - 1)
    def cyl_pt(r_, th_, z_):
        return torch.stack([r_ * torch.cos(th_), r_ * torch.sin(th_), z_], -1).to(dev)
    def UP(r_, th_, z_):
        yy = cyl_pt(r_, th_, z_)
        FF, JJ = ph.derivs(f, yy, order=1, chunk=a.chunk)
        UU = ph.curl_from_jac(JJ[:, :3, :]); PP = FF[:, 3]
        er = torch.stack([torch.cos(th_), torch.sin(th_), torch.zeros_like(th_)], -1).to(dev); et = torch.stack([-torch.sin(th_), torch.cos(th_), torch.zeros_like(th_)], -1).to(dev)
        return torch.stack([(UU * er).sum(-1), (UU * et).sum(-1), UU[:, 2], PP], -1)  # (n,4): Ur, Ut, Uz, P
    h = 1e-3
    def fd(fun, var):
        out = 0
        for k, c_ in ((-2, 1 / 12), (-1, -8 / 12), (1, 8 / 12), (2, -1 / 12)):
            args = {"r": r.clone(), "th": th.clone(), "z": z.clone()}; args[var] = args[var] + k * h
            out = out + c_ * fun(args["r"], args["th"], args["z"])
        return out / h
    Q0 = UP(r, th, z); Qr = fd(UP, "r"); Qt = fd(UP, "th"); Qz = fd(UP, "z")
    rd, zd = r.to(dev), z.to(dev)
    Ur, Ut, Uz, Pc = Q0.unbind(-1)
    Br = cl * rd + Ur; Bz = cl * zd + C + Uz
    D = lambda k: Br * Qr[:, k] + (Ut / rd) * Qt[:, k] + Bz * Qz[:, k]
    e_r = (1 - cl) * Ur + D(0) - Ut * Ut / rd + Qr[:, 3]
    e_t = (1 - cl) * Ut + D(1) + Ur * Ut / rd + Qt[:, 3] / rd
    e_z = (1 - cl) * Uz + D(2) + Qz[:, 3]
    e_div = Qr[:, 0] + Ur / rd + Qt[:, 1] / rd + Qz[:, 2]
    yy = cyl_pt(r, th, z)
    FF, JJ, HH = ph.derivs(f, yy, order=2, chunk=a.chunk); UU, gUU, PP, gPP, _ = ph.velocity_and_grad(FF, JJ, HH)
    Rmc, _, _ = ph.momentum_residual(yy, UU, gUU, gPP, cl, C)
    er = torch.stack([torch.cos(th), torch.sin(th), torch.zeros_like(th)], -1).to(dev); et = torch.stack([-torch.sin(th), torch.cos(th), torch.zeros_like(th)], -1).to(dev)
    cart = torch.stack([(Rmc * er).sum(-1), (Rmc * et).sum(-1), Rmc[:, 2]], -1); cylr = torch.stack([e_r, e_t, e_z], -1)
    rep["cyl_fd_check"] = {"n": nc, "h": h, "max_abs_diff_cart_vs_cylFD": (cart - cylr).abs().max().item(), "max_abs_Rm": cart.abs().max().item(),
                           "rel_diff": ((cart - cylr).norm() / cart.norm()).item(), "cyl_div_fd_max": e_div.abs().max().item(), "gradU_scale": gUU.abs().max().item()}
    # ---- symmetry, parity, non-axisymmetry, Fourier
    core = y.norm(dim=-1) < 4.0
    yc = y[core][:2048]
    rep["Qsym_defect"] = dg.symmetry_defect(model, yc[:512])
    inv, zr = dg.parity_defects(model, yc); rep["inversion_defect_core"] = inv; rep["zrefl_defect_core"] = zr
    for K in (8, 16, 32):
        en, et_, _, _ = nonaxi_ratio(model, yc[:1024], K=K); rep["nonaxi_ratio_core_K%d" % K] = (en / et_).item()
    rep["ring_fourier_core"] = dg.ring_fourier_energy(model, [0.25, 0.5, 1.0, 2.0], [-1.0, -0.5, 0.0, 0.5, 1.0], K=64)
    rep["ring_fourier_far"] = dg.ring_fourier_energy(model, [10.0, 100.0, 1000.0], [-0.5, 0.0, 0.5], K=64)
    # ---- affine fit on core balls, vorticity variation, curvature
    for L in (0.5, 1.0, 2.0):
        m = y.norm(dim=-1) < L
        yl, Ul, wl, Oml = y[m], U[m], w[m], Om[m]
        X = torch.cat([yl, torch.ones_like(yl[:, :1])], 1); W = wl.sqrt().unsqueeze(-1)
        sol = torch.linalg.lstsq(X * W, Ul * W).solution; res = Ul - X @ sol
        rep["affine_B%g" % L] = {"resid_frac": (wl2(res, wl) / wl2(Ul, wl)), "vort_var_frac": wl2(Oml - (wl.unsqueeze(-1) * Oml).sum(0) / wl.sum(), wl) / wl2(Oml, wl),
                                 "curv_L_over_gradU": L * wl2(HU[m].reshape(-1, 27), wl) / wl2(gU[m].reshape(-1, 9), wl)}
    # ---- vorticity maximum, stretching, 3D dependence, origin values
    On = Om.norm(dim=-1); i = int(On.argmax().item()); om = Om[i]
    rep["vorticity"] = {"max_sampled": On.max().item(), "argmax": y[i].tolist(), "stretch_ratio_at_max": (om @ (gU[i] @ om) / (om @ om)).item(),
                        "XiSXi_core_mean": ((Om[core] * torch.einsum("nik,nk->ni", 0.5 * (gU[core] + gU[core].transpose(1, 2)), Om[core])).sum(-1) / (On[core] ** 2).clamp_min(1e-300)).mean().item(),
                        "vort_frac_core": (w[core] * On[core] ** 2).sum().item() / (w[core] * (gU[core] ** 2).sum((-1, -2))).sum().item()}
    rep["dz_frac_core"] = dg.three_d_dependence(gU[core], w[core])
    F0, J0, H0 = ph.derivs(f, torch.zeros(1, 3, dtype=torch.float64, device=dev), order=2); U0, gU0, P0, gP0, _ = ph.velocity_and_grad(F0, J0, H0)
    rep["origin"] = {"U": U0[0].tolist(), "gradU": gU0[0].tolist(), "P": P0[0].item(), "max_U_sampled": U.norm(dim=-1).max().item()}
    # ---- stagnation set
    gs = torch.Generator(); gs.manual_seed(a.seed + 3)
    zeros, nconv, nfail = dg.find_stagnation_points(model, dg.stagnation_starts(512, 4.0, gs, dev), cl, C, R_max=40.0)
    rep["stagnation"] = {"n_zeros": len(zeros), "starts_converged": nconv, "zeros": zeros}
    # ---- tail slopes along rays
    gd = torch.Generator(); gd.manual_seed(a.seed + 4)
    dirs = torch.randn(24, 3, generator=gd, dtype=torch.float64); dirs = dirs / dirs.norm(dim=-1, keepdim=True)
    dirs = torch.cat([dirs, torch.tensor([[0.0, 0.0, 1.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])]).to(dev)
    Rs = [1e2, 3e2, 1e3, 3e3, 1e4]
    vals = {}
    for Rr in Rs:
        FF, JJ, HH = ph.derivs(f, Rr * dirs, order=2); UU, gUU, PP, gPP, _ = ph.velocity_and_grad(FF, JJ, HH)
        RmR, _, _ = ph.momentum_residual(Rr * dirs, UU, gUU, gPP, cl, C)
        vals[Rr] = (UU.norm(dim=-1), gUU.reshape(len(dirs), 9).norm(dim=-1), PP.abs(), RmR.norm(dim=-1), torch.einsum("nik,nk->ni", gUU, UU).norm(dim=-1) + gPP.norm(dim=-1))
    def slopes(k):
        out = []
        for R1, R2 in zip(Rs[:-1], Rs[1:]):
            out.append(((torch.log(vals[R2][k].clamp_min(1e-300)) - torch.log(vals[R1][k].clamp_min(1e-300))) / math.log(R2 / R1)))
        return torch.stack(out)  # (nR-1, ndirs)
    rep["tail"] = {"expected_d": d, "expected_gradU": d - 1, "expected_P": 2 * d, "expected_nonlinear": 2 * d - 1,
                   "slope_U_median_per_interval": slopes(0).median(dim=1).values.tolist(), "slope_U_min": slopes(0).min().item(), "slope_U_max": slopes(0).max().item(),
                   "slope_gradU_median": slopes(1).median(dim=1).values.tolist(), "slope_P_median": slopes(2).median(dim=1).values.tolist(),
                   "slope_Rm_median": slopes(3).median(dim=1).values.tolist(),
                   "Rm_over_nonlinear_terms_by_R": {str(Rr): (vals[Rr][3] / vals[Rr][4].clamp_min(1e-300)).max().item() for Rr in Rs},
                   "Rm_over_U_by_R": {str(Rr): (vals[Rr][3] / vals[Rr][0].clamp_min(1e-300)).max().item() for Rr in Rs}}
    # ---- c_l sensitivity at fixed fields (not a refit)
    sens = {}
    for dc in (-0.01, -0.005, -0.0025, 0.0, 0.0025, 0.005, 0.01):
        Rm2, _, _ = ph.momentum_residual(y, U, gU, gP, cl + dc, C)
        m = core
        sens["%+.4f" % dc] = wl2(Rm2[m], w[m]) / regions["shell_1_2"]["den_m"]
    rep["cl_sensitivity_core_eps_m_fixed_fields"] = sens
    # ---- summary
    rep["summary"] = {"worst_eps_m_region": max(((k, v["eps_m"]) for k, v in regions.items() if v["eps_m"] is not None), key=lambda kv: kv[1]),
                      "worst_eps_nl_region": max(((k, v["eps_nl"]) for k, v in regions.items() if v["eps_nl"] is not None), key=lambda kv: kv[1]),
                      "core_eps_m_shell_1_2": regions["shell_1_2"]["eps_m"], "eps_omega_shell_1_2": regions["shell_1_2"]["eps_omega"], "eps_P_shell_1_2": regions["shell_1_2"]["eps_P"]}
    out = a.out or (os.path.splitext(a.ckpt)[0] + "_audit.json")
    json.dump(rep, open(out, "w"), indent=1, default=float)
    print(json.dumps({"exp_id": rep["exp_id"], "cl": cl, "summary": rep["summary"], "cyl_fd_rel_diff": rep["cyl_fd_check"]["rel_diff"], "Qsym": rep["Qsym_defect"],
                      "nonaxi_K16": rep["nonaxi_ratio_core_K16"], "ring_n2": rep["ring_fourier_core"]["n2"], "n_zeros": rep["stagnation"]["n_zeros"], "stretch": rep["vorticity"]["stretch_ratio_at_max"],
                      "tail_slope_U": rep["tail"]["slope_U_median_per_interval"]}, indent=1, default=float))
    print("wrote", out)


if __name__ == "__main__":
    main()
