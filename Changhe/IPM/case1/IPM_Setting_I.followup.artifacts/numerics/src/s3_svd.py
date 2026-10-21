"""SPEC S3 (a)-(c): singular values of the collocation Jacobian at a state, in stated norms, with the softest vectors' diagnostics.
Norms: domain = grid L2 norm of delta H = delta rho / rho = delta b / b with weights w_q(i) (Clenshaw-Curtis in q) x w_s(j)
(uniform in the mapped angle s, times theta'(s) so that it is the L2 norm in theta); the c_l column is divided by the same
norm of X.grad rho / rho (the relative size of the c_l term).  Rows: Ehat rows weighted by sqrt(w_q w_s); identity row weight 1.
Usage: python3 src/s3_svd.py runs/state.npz tag [nsoft]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

def cc_weights01(N):
    th = np.pi * np.arange(N + 1) / N
    w = np.zeros(N + 1)
    for j in range(N + 1):
        s = 0.0
        for kk in range(0, N + 1, 2):
            fac = 0.5 if (kk == 0 or kk == N) else 1.0
            ck = 2.0 / (1.0 - kk * kk) if kk != 1 else 0.0
            s += fac * ck * np.cos(kk * th[j])
        w[j] = 2.0 * s / N
    w[0] *= 0.5; w[-1] *= 0.5
    return 0.5 * w[::-1]      # increasing q

def main():
    path, tag = sys.argv[1], sys.argv[2]; nsoft = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    Npsi = int(sys.argv[4]) if len(sys.argv) > 4 else None
    model, x, d = ipn.load_state(path); b, cl = model.unpack(x); clf = float(cl)
    if Npsi is not None and Npsi != model.Npsi:
        model = ipn.Model(model.N, model.M, model.L, device='cuda', beta=model.beta, nmodes=model.nmodes, Mq=model.Mq, Npsi=Npsi)
        x = model.pack(b, clf)
    N, M = model.N, model.M; n = N * M + 1
    r, w, v = model.radii(clf); th = model.ang.theta_np; dth = model.ang.dtheta_ds_np
    wq = cc_weights01(N)[1:]; ws = (np.pi / (2 * M)) * dth
    Wgt = np.sqrt(np.outer(wq, ws))                                   # (N, M)
    t0 = time.time(); J = model.jacobian(x)
    F = model.F(x)
    bn = b[1:].cpu().numpy()
    Dcol = torch.tensor((bn / Wgt).ravel(), device=J.device)          # delta b = (b / sqrt(w)) y with |y| = |delta H|_w  (ERRATUM 09:33Z: was Wgt * bn, inverted)
    g = model.geom(torch.tensor(clf, device=model.dev))
    Xgrad_over_rho = (3.0 + g['omega_w'])[1:, None] + g['S'][1:, None] * (model.Dq @ b)[1:] / b[1:]
    ccl = float(torch.sqrt((torch.tensor(Wgt, device=J.device) ** 2 * Xgrad_over_rho ** 2).sum()))
    Drow = torch.tensor(np.r_[Wgt.ravel(), 1.0], device=J.device)
    Js = Drow[:, None] * J * torch.cat([Dcol, torch.tensor([1.0 / ccl], device=J.device)])[None, :]   # (ERRATUM 09:33Z: was ccl)
    Fs = Drow * F
    t1 = time.time(); S = torch.linalg.svdvals(Js); t2 = time.time()
    S = S.cpu().numpy()
    out = dict(tag=tag, N=N, M=M, beta=model.beta, L=model.L, Npsi=model.Npsi, n=n, c_l=clf, F_norm_scaled=float(Fs.norm()), F_inf=float(F.abs().max()),
               smax=float(S[0]), smallest20=[float(s) for s in S[-20:][::-1]], svd_time=t2 - t1,
               counts={'below_1e-10_smax': int((S < 1e-10 * S[0]).sum()), 'below_1e-11_smax': int((S < 1e-11 * S[0]).sum()),
                       'below_1e-8': int((S < 1e-8).sum()), 'below_1e-6': int((S < 1e-6).sum()), 'below_1e-4': int((S < 1e-4).sum()), 'below_1e-3': int((S < 1e-3).sum())})
    # softest vectors by block inverse iteration on the scaled matrix
    LU = torch.linalg.lu_factor(Js); V = torch.randn(n, nsoft + 4, device=J.device)
    for _ in range(40):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y); V, _ = torch.linalg.qr(Z)
    JV = Js @ V; Uk, sk, Wk = torch.linalg.svd(JV, full_matrices=False); Vk = V @ Wk.T; idx = torch.argsort(sk)
    sk = sk[idx].cpu().numpy(); Vk = Vk[:, idx]
    # fields for the streamline alignment: W and grad(delta rho) on the grid
    fl = model.fields(b, torch.tensor(clf, device=model.dev), g)
    rho = (torch.tensor(r[1:], device=J.device) ** 3 * torch.tensor(w[1:], device=J.device))[:, None] * (model.ang.cos ** 2 * model.ang.sin)[None, :] * b[1:]
    rho = torch.nan_to_num(rho, nan=0.0, posinf=0.0, neginf=0.0); rho[-1, :] = 0.0     # r = infinity row excluded from the alignment
    vv = torch.tensor(v[1:], device=J.device)[:, None]
    Ur = torch.tensor(r[1:], device=J.device)[:, None] * vv * fl['Ur'][1:]; Uth = torch.tensor(r[1:], device=J.device)[:, None] * vv * fl['Uth'][1:]
    Wr = clf * torch.tensor(r[1:], device=J.device)[:, None] + Ur; Wth = Uth
    soft = []
    thd = th * 180 / np.pi
    for kk in range(nsoft):
        vec = Vk[:, kk]; dH = (vec[:-1] / Dcol).reshape(N, M)                 # delta H = delta b / b on the grid
        drho = rho * dH
        # gradient of delta rho: radial via D_q (r d/dr = S d/dq), angular via D_theta
        drho_full = torch.cat([torch.zeros(1, M, device=J.device), drho], 0)
        r_drho_r = (g['S'][:, None] * (model.Dq @ drho_full))[1:]
        drho_th = model.ang.dtheta(drho, 'EE' if False else 'EO')          # delta rho has class EO
        rr = torch.tensor(r[1:], device=J.device)[:, None]
        Wgrad = (Wr * r_drho_r / rr + Wth * drho_th / rr)
        Wn = torch.sqrt(Wr ** 2 + Wth ** 2); gn = torch.sqrt((r_drho_r / rr) ** 2 + (drho_th / rr) ** 2)
        wt = torch.tensor(Wgt ** 2, device=J.device); wt[-1, :] = 0.0                       # exclude r = infinity
        fin = torch.isfinite(Wgrad) & torch.isfinite(Wn * gn)
        s_align = float(torch.sqrt((wt * torch.where(fin, Wgrad, torch.zeros_like(Wgrad)) ** 2).sum() / (wt * torch.where(fin, Wn * gn, torch.zeros_like(Wn))  ** 2).sum()))
        en = (vec[:-1] ** 2).reshape(N, M).cpu().numpy(); tot = float((vec ** 2).sum())
        rr1 = r[1:]
        radial = {k_: float(en[m_].sum() / tot) for k_, m_ in [('r<1', rr1 < 1), ('1-10', (rr1 >= 1) & (rr1 < 10)), ('10-100', (rr1 >= 10) & (rr1 < 100)), ('>100', rr1 >= 100)]}
        X, Y = np.outer(rr1, np.cos(th)), np.outer(rr1, np.sin(th)); nearP = (X - 8.6) ** 2 + Y ** 2 < 4
        radial['|X-P|<2'] = float(en[nearP].sum() / tot)
        ang = {f'{lo}-{lo+10}': float(en[:, (thd >= lo) & (thd < lo + 10)].sum() / tot) for lo in range(0, 90, 10)}
        # oscillation measures: sign changes along r = 5 (interpolated row) and along theta = 45 deg
        i5 = int(np.argmin(np.abs(rr1 - 5.0))); j45 = int(np.argmin(np.abs(thd - 45)))
        row5 = dH[i5].cpu().numpy(); col45 = dH[:, j45].cpu().numpy()
        sc_r5 = int(np.sum(np.sign(row5[:-1]) != np.sign(row5[1:]))); sc_t45 = int(np.sum(np.sign(col45[:-1]) != np.sign(col45[1:])))
        soft.append(dict(sigma=float(sk[kk]), cl_component=float(vec[-1]), radial=radial, angular=ang, streamline_alignment=s_align,
                         sign_changes_r5=sc_r5, sign_changes_theta45=sc_t45))
    out['soft'] = soft
    json.dump(out, open(f'./runs/s3_{tag}.json', 'w'), indent=1)
    print(f'{tag}: n {n} smax {S[0]:.3e} smallest {" ".join("%.2e" % s for s in S[-8:][::-1])}  counts(<1e-6,<1e-4,<1e-3) {out["counts"]["below_1e-6"]} {out["counts"]["below_1e-4"]} {out["counts"]["below_1e-3"]}  |F|s {out["F_norm_scaled"]:.2e}  ({time.time()-t0:.0f}s)')
    for kk, s_ in enumerate(soft):
        print(f'  v{kk}: sigma {s_["sigma"]:.3e} cl {s_["cl_component"]:+.3e} align {s_["streamline_alignment"]:.3f} sc(r5,t45) {s_["sign_changes_r5"]},{s_["sign_changes_theta45"]} radial {s_["radial"]}')

if __name__ == '__main__':
    main()
