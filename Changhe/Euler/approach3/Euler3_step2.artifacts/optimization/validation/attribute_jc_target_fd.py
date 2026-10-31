"""D6FP (lead 23:29Z item 1): attribution of the J_c closure-block error (z_c 5.4e-6 in test_jc_assembly, 2.5e-5 in V067) to the finite
differences of closure_target_correction. On S01_own: for the c_l and omega inputs and the five tail-amplitude inputs with the largest weight in
the test's coefficient direction coef_dir_0, compare centered differences of G_required and of N = ||G|| at h = 1e-3, 1e-4, 1e-5 with the
five-point stencil at the same steps; reference = five-point at 1e-4 (checked against five-point at 1e-3). Also the analytic dN = <G, dG>_w / N
against the differences. The G_of emulation is the one of closure_target_correction (tail amplitudes set through A[0], C[0])."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.far_field.correction import first_correction
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model = case.prob, case.model
z = case.z_full; cl = prob.closure
aT, aS, c_l, omega = model.unpack(z); t0_, s0_ = prob.tail_amplitudes(aT, aS, c_l); Nq = model.Nq
def G_of(t_vec, s_vec, c_val, w_val):
    d = model.unpack_all(z.detach()); alpha_v = (1.0 - c_val) / c_val; R0 = model.R0; l = model.l_arr
    A = d["A"].clone(); C = d["C"].clone(); sA = A.sum(0); sC = C.sum(0)
    A[0] = A[0] + (t_vec / (R0 ** (alpha_v + l)) - sA); C[0] = C[0] + (s_vec / (R0 ** (alpha_v + l - 1)) - sC)
    zz = model.pack(A, C, c_val, w_val, extra={k: d[k] for k in ("B", "D", "E") if d[k].numel() > 0})
    fc = first_correction(prob, zz.detach(), ntheta=cl["grid"].ntheta, nphi=cl["grid"].nphi)
    G_of.w_fc = fc["w"]
    return fc["G"].reshape(-1), fc["G_norm"]
base_G, base_N = G_of(t0_.detach(), s0_.detach(), float(c_l), float(omega))
w = G_of.w_fc; wflat = w[:, None].expand(-1, 3).reshape(-1)                 # the weights of first_correction's l2 (lead 23:54Z item 2), not cl["w"]
print(f"N check: {float(torch.sqrt((wflat * base_G * base_G).sum())):.15e} vs G_norm {base_N:.15e}")
# weights of the inputs in coef_dir_0 of test_jc_assembly (seed 5, direction 0): |du_dz . v|
rng = np.random.default_rng(5)
zo = case.z_opt; n = zo.numel()
v = torch.tensor(rng.normal(size=n), device=dev); v[-2:] = 0; v = v / v.norm()
zz = zo.detach().clone().requires_grad_(True); zf = case.to_full_opt(zz); aT_, aS_, c_, w_ = model.unpack(zf); t_, s_ = prob.tail_amplitudes(aT_, aS_, c_)
u = torch.cat([t_, s_, c_[None], w_[None]]); n_in = 2 * Nq + 2
du_dz = torch.zeros(n_in, n, device=dev)
for i in range(n_in):
    g, = torch.autograd.grad(u[i], zz, retain_graph=True); du_dz[i] = g
proj = (du_dz @ v).abs()
tail_rank = torch.argsort(proj[: 2 * Nq], descending=True)[:5].tolist()
inputs = [("c_l", 2 * Nq), ("omega", 2 * Nq + 1)] + [(("t" if i < Nq else "s") + f"[{i % Nq}] |amp| {float(u[i]):.3e}", i) for i in tail_rank]
out = {}
for name, i in inputs:
    def pert(step, h):
        t_ = t0_.detach().clone(); s_ = s0_.detach().clone(); cv = float(c_l); wv = float(omega)
        if i < Nq:
            hk = h * max(1.0, abs(float(t_[i]))); t_[i] += step * hk
        elif i < 2 * Nq:
            hk = h * max(1.0, abs(float(s_[i - Nq]))); s_[i - Nq] += step * hk
        elif i == 2 * Nq:
            hk = h; cv += step * hk
        else:
            hk = h * max(1.0, abs(wv)); wv += step * hk
        return G_of(t_, s_, cv, wv), hk
    rec = {}
    D2 = {}; D4 = {}; N2 = {}; N4 = {}
    for h in (1e-3, 1e-4, 1e-5):
        (Gp, Np), hk = pert(1.0, h); (Gm, Nm), _ = pert(-1.0, h); (Gp2, Np2), _ = pert(2.0, h); (Gm2, Nm2), _ = pert(-2.0, h)
        D2[h] = (Gp - Gm) / (2 * hk); D4[h] = (8 * (Gp - Gm) - (Gp2 - Gm2)) / (12 * hk); N2[h] = (Np - Nm) / (2 * hk); N4[h] = (8 * (Np - Nm) - (Np2 - Nm2)) / (12 * hk)
    ref = D4[1e-4]; refN = N4[1e-4]
    dN_an = float(((wflat * base_G) @ ref) / base_N)
    rec["ref_check_five_point_1e-3_vs_1e-4"] = float((D4[1e-3] - ref).norm() / ref.norm()); rec["ref_check_N"] = abs(N4[1e-3] - refN) / max(abs(refN), 1e-300)
    rec["centered_dG_error"] = {f"{h:.0e}": float((D2[h] - ref).norm() / ref.norm()) for h in D2}; rec["five_point_dG_error"] = {f"{h:.0e}": float((D4[h] - ref).norm() / ref.norm()) for h in D4}
    rec["centered_dN_error"] = {f"{h:.0e}": abs(N2[h] - refN) / max(abs(refN), 1e-300) for h in N2}; rec["five_point_dN_error"] = {f"{h:.0e}": abs(N4[h] - refN) / max(abs(refN), 1e-300) for h in N4}
    rec["analytic_dN_vs_ref"] = abs(dN_an - refN) / max(abs(refN), 1e-300); rec["dN_ref"] = refN; rec["dN_analytic"] = dN_an
    e = rec["centered_dG_error"]; rec["h2_scaling_ratio_1e-3_over_1e-4"] = (e["1e-03"] / e["1e-04"]) if e["1e-04"] > 0 else None
    rec["weight_in_coef_dir_0"] = float(proj[i]); rec["dG_norm"] = float(ref.norm())
    out[name] = rec
    print(name, json.dumps({k: (v if not isinstance(v, float) else f"{v:.3e}") for k, v in rec.items()}), flush=True)
out['_note'] = 'analytic dN = <G, dG>_w / N with the quadrature weights of first_correction (fc w); dG reference = five-point at h 1e-4'
json.dump(out, open(os.path.join(ROOT, "validation", "attribute_jc_target_fd.json"), "w"), indent=1)
