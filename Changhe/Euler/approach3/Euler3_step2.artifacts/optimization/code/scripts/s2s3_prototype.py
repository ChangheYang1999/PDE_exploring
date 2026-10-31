#!/usr/bin/env python
"""Stage II S2/S3 prototypes (lead 2026-10-25T03:17Z item 1, 02:54Z item 8) on saved states.
  s2s3_prototype.py jvp    <start.pt> [--tag T]      (a) d(U) = U + G N(U) at the state, G L U = U identity, two routes for d, JVP vs finite differences
  s2s3_prototype.py newton <start.pt> [--tag T]      (b) bordered Newton system: dense Jacobian by forward-mode AD, GMRES count to 1e-3, sigma_min/max, one damped step
  s2s3_prototype.py s3     <start.pt> [--iters 5]    (c) stabilized fixed point U <- S[P_n m^2 T], plain normalized control, change ratios, holdout rho_u per iterate
Writes reports/s2s3_<mode>_<tag>.json."""
import sys, os, json, time, math, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.optimization.tail_constraints import TailConstraints
from src.optimization.backward_defect import BackwardDefect
from src.optimization.lm import jacobian_fwd

ap = argparse.ArgumentParser(); ap.add_argument("mode"); ap.add_argument("zfile"); ap.add_argument("--tag", default=None); ap.add_argument("--iters", type=int, default=5)
ap.add_argument("--device", default="cuda:0"); ap.add_argument("--n_per_octave", type=int, default=16); ap.add_argument("--chunk", type=int, default=64)
a = ap.parse_args()
dev = a.device
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(dev)
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
              free_params=False, channels=cfg.get("channels"), device=dev, extra_r=cfg.get("far_radii") if cfg.get("far_merged", True) else None)
if S.get("free_params", False):
    z = z[:-2]
prob = Problem(model, formulation="mom"); prob.pivot = S.get("pivot") or prob.choose_pivot(z)
tc = TailConstraints(model) if cfg.get("tail_constraints", False) else None
tag = a.tag or os.path.basename(os.path.dirname(os.path.dirname(a.zfile)))
t0 = time.time()
bd = BackwardDefect(prob, tc=tc, n_per_octave=a.n_per_octave)
zc = tc.reduce(z) if tc is not None else z
z_rt = bd.to_full(zc)
info = dict(state=os.path.relpath(a.zfile, ROOT), c_l=cfg["c_l"], omega=cfg["omega"], L=cfg["L"], Nk=cfg["Nk"], n_reduced=bd.n_red, n_train_rows=int(bd.B.shape[0]),
            dense_radii=len(bd.radii), build_seconds=time.time() - t0, projection_cond=bd.proj_cond, roundtrip_rel=float((z_rt - z).norm() / z.norm()))
print("build:", json.dumps(info)); sys.stdout.flush()
out_path = os.path.join(ROOT, "reports", f"s2s3_{a.mode}_{tag}.json")

def norm_train(x):
    return float((x * bd.wv).norm())

if a.mode == "jvp":
    t1 = time.time(); D = bd.defect(z_rt); t_def = time.time() - t1
    U, d, LU, N = D["U"], D["d"], D["LU"], D["N"]
    GLU = bd.apply_G(LU); GRu = bd.apply_G(D["Ru"])
    msk = bd.r > model.R0 * 2.0 ** -5
    def rel(X, Y):
        num = ((X - Y) ** 2).sum(0)[msk].sum(); den = (Y ** 2).sum(0)[msk].sum()
        return float((num / den).sqrt())
    Utr = model.fields_grid(z_rt, need_vort=False)['U']; interp_err = float((bd.to_train(U) - Utr).norm() / Utr.norm())
    res_ = dict(G_LU_vs_U=rel(GLU, U), d_two_routes=rel(GRu, d), d_over_U=float((d ** 2).sum().sqrt() / (U ** 2).sum().sqrt()), seconds_defect=t_def, interp_dense_to_train_rel=interp_err)
    dt = bd.defect_train(zc); zp, pdef = bd.project(dt)
    res_.update(projection_defect_rel=pdef, Pn_d_field_over_U_field_weighted=float(((bd.B @ zp) * bd.wv).norm() / ((bd.B @ zc) * bd.wv).norm()), d_field_over_U_field_weighted=float((dt * bd.wv).norm() / ((bd.B @ zc) * bd.wv).norm()))
    torch.manual_seed(0); v = torch.randn_like(zc); v /= v.norm()
    t1 = time.time(); _, jv = torch.func.jvp(bd.defect_train, (zc,), (v,)); t_jvp = time.time() - t1
    fd = {}
    for h in (1e-4, 1e-5, 1e-6):
        dp = bd.defect_train(zc + h * v); dm = bd.defect_train(zc - h * v)
        fd[str(h)] = float(((dp - dm) / (2 * h) - jv).norm() / jv.norm())
    res_.update(jvp_vs_fd_rel=fd, seconds_jvp=t_jvp, jvp_norm=float(jv.norm()))
    print("jvp:", json.dumps(res_)); info.update(res_)

elif a.mode == "newton":
    def r_proj(zc_):
        return bd.project_differentiable(bd.defect_train(zc_))
    t1 = time.time(); r0 = r_proj(zc); t_r = time.time() - t1
    t1 = time.time(); Jd = jacobian_fwd(r_proj, zc, chunk=a.chunk); t_J = time.time() - t1          # (n, n)
    ZD, ZR = bd.generators(z_rt)
    cD = bd.project_differentiable(bd.to_train(ZD).reshape(-1)); cR = bd.project_differentiable(bd.to_train(ZR).reshape(-1))
    g = bd.gauge_rows(zc); Jg = torch.autograd.functional.jacobian(bd.gauge_rows, zc)                # (2, n)
    n = zc.numel()
    J = torch.zeros(n + 2, n + 2, dtype=DT, device=dev) if False else torch.zeros(n + 2, n + 2, dtype=torch.float64, device=dev)
    J[:n, :n] = Jd; J[:n, n] = cD; J[:n, n + 1] = cR; J[n:, :n] = Jg
    rhs = torch.cat([r0, g])
    Jn = J.cpu().numpy(); bn = rhs.cpu().numpy()
    sv = np.linalg.svd(Jn, compute_uv=False); svd_d = np.linalg.svd(Jd.cpu().numpy(), compute_uv=False)
    import scipy.sparse.linalg as spla
    cnt = {"n": 0}
    def cb(xk): cnt["n"] += 1
    try:
        x, flag = spla.gmres(Jn, -bn, rtol=1e-3, restart=50, maxiter=40, callback=cb, callback_type="pr_norm")
    except TypeError:
        x, flag = spla.gmres(Jn, -bn, tol=1e-3, restart=50, maxiter=40, callback=cb, callback_type="pr_norm")
    gm_res = float(np.linalg.norm(Jn @ x + bn) / np.linalg.norm(bn))
    # with a Jacobi (diagonal) preconditioner for comparison
    dg = np.abs(np.diag(Jn)); Dinv = 1.0 / np.maximum(dg, 1e-8 * dg.max())
    cnt2 = {"n": 0}
    def cb2(xk): cnt2["n"] += 1
    Mpre = spla.LinearOperator(Jn.shape, matvec=lambda v_: Dinv * v_)
    try:
        x2, flag2 = spla.gmres(Jn, -bn, rtol=1e-3, restart=50, maxiter=40, callback=cb2, callback_type="pr_norm", M=Mpre)
    except TypeError:
        x2, flag2 = spla.gmres(Jn, -bn, tol=1e-3, restart=50, maxiter=40, callback=cb2, callback_type="pr_norm", M=Mpre)
    # the same system in column-scaled coefficients a_s = cs a (cs = weighted column norms of the basis, so the scaled basis has unit columns and
    # cond(R) is the basis conditioning): J_s = diag(cs, 1, 1) J diag(1/cs, 1, 1); separates the operator's conditioning from the coefficient scaling
    csn = np.concatenate([bd.cs.cpu().numpy(), [1.0, 1.0]])
    Js = (csn[:, None] * Jn) / csn[None, :]; bs = csn * bn
    svs = np.linalg.svd(Js, compute_uv=False)
    cnt3 = {"n": 0}
    def cb3(xk): cnt3["n"] += 1
    try:
        x3, flag3 = spla.gmres(Js, -bs, rtol=1e-3, restart=50, maxiter=40, callback=cb3, callback_type="pr_norm")
    except TypeError:
        x3, flag3 = spla.gmres(Js, -bs, tol=1e-3, restart=50, maxiter=40, callback=cb3, callback_type="pr_norm")
    scaled = dict(sigma_max=float(svs[0]), sigma_min=float(svs[-1]), cond=float(svs[0] / svs[-1]), gmres_iterations_tol1e3=cnt3["n"], gmres_flag=int(flag3),
                  gmres_final_rel_residual=float(np.linalg.norm(Js @ x3 + bs) / np.linalg.norm(bs)), basis_cond=bd.proj_cond, Pn_d_field_over_U_field_weighted=float(((bd.B @ r0) * bd.wv).norm() / ((bd.B @ zc) * bd.wv).norm()))
    # field-norm coordinates (verifier 2026-10-25T05:29Z, lead 05:36Z item 3): J_field = diag(R, I_2) J_s diag(R, I_2)^-1 with R the QR factor of the
    # weighted unit-column basis (so coefficient perturbations are measured by the weighted field norm of the basis combination); the two border
    # unknowns and the two gauge rows keep the Euclidean scalar norm (stated convention)
    Rm = bd.R.cpu().numpy(); n_ = Rm.shape[0]
    Dl = np.zeros((n_ + 2, n_ + 2)); Dl[:n_, :n_] = Rm; Dl[n_, n_] = 1.0; Dl[n_ + 1, n_ + 1] = 1.0
    Dli = np.linalg.inv(Dl)
    Jf = Dl @ Js @ Dli; bf = Dl @ bs
    svf = np.linalg.svd(Jf, compute_uv=False)
    cnt4 = {"n": 0}
    def cb4(xk): cnt4["n"] += 1
    try:
        x4, flag4 = spla.gmres(Jf, -bf, rtol=1e-3, restart=50, maxiter=40, callback=cb4, callback_type="pr_norm")
    except TypeError:
        x4, flag4 = spla.gmres(Jf, -bf, tol=1e-3, restart=50, maxiter=40, callback=cb4, callback_type="pr_norm")
    Jd_f = Rm @ (np.diag(bd.cs.cpu().numpy()) @ Jd.cpu().numpy() @ np.diag(1.0 / bd.cs.cpu().numpy())) @ np.linalg.inv(Rm)
    svdf = np.linalg.svd(Jd_f, compute_uv=False)
    field_norm = dict(convention="J_field = diag(R, I) J_s diag(R, I)^-1; R from QR of the weighted unit-column basis (fixed-gauge weights (1 + r^2/R0^2)^alpha x angular Gauss, training nodes); border unknowns and gauge rows Euclidean",
                      sigma_max=float(svf[0]), sigma_min=float(svf[-1]), cond=float(svf[0] / svf[-1]), smallest_5_singular=[float(v) for v in svf[-5:]],
                      unbordered_sigma_max=float(svdf[0]), unbordered_sigma_min=float(svdf[-1]), unbordered_cond=float(svdf[0] / svdf[-1]),
                      gmres_iterations_tol1e3=cnt4["n"], gmres_flag=int(flag4), gmres_final_rel_residual=float(np.linalg.norm(Jf @ x4 + bf) / np.linalg.norm(bf)),
                      cond_R=float(np.linalg.cond(Rm)))
    np.savez_compressed(os.path.join(ROOT, "reports", f"s2s3_newton_matrices_{tag}.npz"), J=Jn, Jd=Jd.cpu().numpy(), R=Rm, cs=bd.cs.cpu().numpy(), gauge_rows=Jg.cpu().numpy(),
                        border_cols=np.stack([cD.cpu().numpy(), cR.cpu().numpy()], 1), rhs=bn, Js=Js, Jf=Jf,
                        note="J: raw coefficient coordinates (reduced tail-constrained coefficients + 2 border scalars); Js column-scaled; Jf field-norm; weights/basis as in src/optimization/backward_defect.py")
    s_dir = np.linalg.solve(Jn, -bn)
    s = torch.tensor(s_dir[:n], dtype=torch.float64, device=dev)
    # damped step: backtracking on ||P_n d|| + gauge rows
    def merit(zc_):
        return float(torch.cat([r_proj(zc_), bd.gauge_rows(zc_)]).norm())
    m0 = merit(zc); line = []
    for t in (1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125):
        line.append((t, merit(zc + t * s)))
    tbest, mbest = min(line, key=lambda p: p[1])
    res_ = dict(seconds_residual=t_r, seconds_jacobian=t_J, n_unknowns=n + 2, residual_norm=float(rhs.norm()), Pn_d_norm=float(r0.norm()), gauge_rows=[float(v) for v in g],
                gmres_iterations_tol1e3=cnt["n"], gmres_flag=int(flag), gmres_final_rel_residual=gm_res, gmres_jacobi_iterations=cnt2["n"], gmres_jacobi_flag=int(flag2),
                sigma_max=float(sv[0]), sigma_min=float(sv[-1]), cond=float(sv[0] / sv[-1]), sigma_min_unbordered=float(svd_d[-1]), smallest_5_singular=[float(v) for v in sv[-5:]],
                newton_step_norm_rel=float(s.norm() / zc.norm()), border_scalars=[float(s_dir[n]), float(s_dir[n + 1])], merit_before=m0, line_search=line, best_step=tbest, merit_after=mbest,
                merit_reduction=mbest / m0, column_scaled=scaled, field_norm=field_norm, matrices_file=f"reports/s2s3_newton_matrices_{tag}.npz")
    print("newton:", json.dumps(res_)); info.update(res_)
    # holdout rho_u of the stepped state (information only)
    try:
        from src.validation.spec_diagnostics import spec_diagnostics
        from src.validation.holdout import HoldoutGrid
        hg = HoldoutGrid(model, r_core=model.R0, n_per_shell=6)
        for name, zz in (("start", bd.to_full(zc)), ("after_step", bd.to_full(zc + tbest * s))):
            sd = spec_diagnostics(prob, zz, holdout=hg, extras=False)
            info[f"holdout_rho_u_max_{name}"] = sd["global_"]["rho_u_max"]; info[f"holdout_sigma_u_max_{name}"] = sd["global_"]["sigma_u_max"]
        print("holdout:", {k: info[k] for k in info if k.startswith("holdout")})
    except Exception as e:
        info["holdout_error"] = repr(e)

elif a.mode == "s3":
    from src.validation.spec_diagnostics import spec_diagnostics
    from src.validation.holdout import HoldoutGrid
    hg = HoldoutGrid(model, r_core=model.R0, n_per_shell=6)
    def holdout(zz):
        sd = spec_diagnostics(prob, zz, holdout=hg, extras=False); g_ = sd["global_"]
        return dict(rho_u_max=g_["rho_u_max"], sigma_u_max=g_["sigma_u_max"], a_max=g_["a_max"], max_U=sd["guards"]["N4_max_U"], max_Om=sd["guards"]["N2_max_abs_Omega"])
    runs = {}
    for variant in ("stabilized", "plain"):
        zk, _ = bd.normalize(z_rt.clone()); hist = [dict(k=0, holdout=holdout(zk))]; prev_change = None; zprev = None
        for k in range(1, a.iters + 1):
            D = bd.defect(zk); U = D["U"]; T = -D["GN"]
            uu = bd.inner_eta(U, U); ut = bd.inner_eta(U, T)
            m = uu / ut if abs(ut) > 1e-300 else float("nan")
            Y = (m ** 2 * T) if variant == "stabilized" else T
            zc_new, pdef = bd.project(bd.to_train(Y).reshape(-1))
            znew, ninfo = bd.normalize(bd.to_full(zc_new))
            change = float((znew - zk).norm() / zk.norm())
            ratio = (change / prev_change) if prev_change else None
            rec = dict(k=k, m=m, uT_over_uu=ut / uu, projection_defect_rel=pdef, change_rel=change, change_ratio=ratio, dilation=ninfo["dilation"], refit_defect=ninfo["refit_defect"],
                       d_over_U=float((D["d"] ** 2).sum().sqrt() / (U ** 2).sum().sqrt()), holdout=holdout(znew))
            hist.append(rec); print(variant, json.dumps(rec)); sys.stdout.flush()
            prev_change = change; zk = znew
            if abs(ut / uu) < 1e-3:
                rec["stop"] = "<U,T>_eta within 1e-3 of 0 relative to <U,U>_eta"; break
            if not math.isfinite(change) or change > 1e3:
                rec["stop"] = "diverged"; break
        runs[variant] = hist
    info["runs"] = runs
    # growth direction of the plain iteration (power-iteration reading): dominant (l, m) content and radii of the last change
    try:
        zl = None
    except Exception:
        pass
info["seconds_total"] = time.time() - t0
json.dump(info, open(out_path, "w"), indent=1, default=float)
print("written", os.path.relpath(out_path, ROOT), f"{info['seconds_total']:.0f}s")
