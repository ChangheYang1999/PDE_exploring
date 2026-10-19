#!/usr/bin/env python3
"""Direct evaluation of the two residuals of the PROMPT on a saved forward / exit-map state (2026-10-19):
     R = (c_l X + W) . grad rho - rho   (W = U - U(0) from the class-S per-mode law, as used by the solver),
     E = -Lap psi - d_x rho             (psi from the same per-mode law; Laplacian by 6th-order finite differences in log r,
                                         spectral in theta: an evaluation independent of the solver's characteristic iteration).
Reports absolute and normalised norms by radial band and in / outside 3-degree neighbourhoods of the datum zeros (strong exits).
Band rms values weight the cells equally in (log r, theta) (not area-weighted); the global L2 norms carry the area weight.  angderiv=local replaces the
spectral theta-derivative in R by a 6th-order centred periodic stencil (test of the Gibbs sensitivity of the core residual; referee audit, 2026-10-19).
Usage: python3 tests/pfwd_direct_resid.py runs/pfwd/par/ES512_base.npz [zero_deg=90,270] [halfwidth_deg=3] [dev=cuda]
"""
import sys, json, math
import numpy as np, torch
sys.path.insert(0, 'code')
from pfwd import PFwd, fd_dlr
from pfwd_batch import PFwdB

def main():
    f = sys.argv[1]
    kw = dict(a.split('=', 1) for a in sys.argv[2:])
    dev = kw.get('dev', 'cuda' if torch.cuda.is_available() else 'cpu')
    zeros = [float(v) for v in kw.get('zero_deg', '90,270').split(',')]
    hw = float(kw.get('halfwidth_deg', '3'))
    d = np.load(f, allow_pickle=True)
    g = torch.tensor(d['g'], device=dev, dtype=torch.float64)
    lr = d['lr']; Nr, Nth = g.shape
    args = json.loads(str(d['args'])) if 'args' in d.files else {}
    info = json.loads(str(d['info'])) if 'info' in d.files else {}
    p = float(args.get('p', kw.get('p', 0.5)))
    cl = 1.0 / p
    S = PFwd(Nr, Nth, float(lr[0]), float(lr[-1]), p, dev=dev)
    SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p, dev=dev)
    r = S.r; th = S.th
    rho = (r[:, None] ** p) * g
    # velocity: the solver's (PFwdB) and the single-state class (PFwd, with psi modes); they must agree to roundoff at p = p_kernel
    WrB, WtB = SB.velocity(rho[None], torch.tensor([p], device=dev, dtype=torch.float64))
    WrB, WtB = WrB[0], WtB[0]
    Wr, Wt, psi, Wrm, Wtm = S.velocity(rho, return_modes=True)
    dvel = float(max((Wr - WrB).abs().max(), (Wt - WtB).abs().max()) / max(Wr.abs().max(), Wt.abs().max()))
    # ---- R
    rho_lr = fd_dlr(rho, S.d)
    angderiv = kw.get('angderiv', 'spectral')
    if angderiv == 'local':
        def dth_local(F):
            return (torch.roll(F, -3, 1) - 9 * torch.roll(F, -2, 1) + 45 * torch.roll(F, -1, 1) - 45 * torch.roll(F, 1, 1) + 9 * torch.roll(F, 2, 1) - torch.roll(F, 3, 1)) / (60 * S.dth)
        rho_t = dth_local(rho)
    else:
        rho_t = S.d_theta(rho)
    Vr = cl * r[:, None] + Wr; Vt = Wt
    adv = Vr * rho_lr / r[:, None] + Vt * rho_t / r[:, None]
    R = adv - rho
    # ---- E per mode
    F = S.to_modes(S.dx_rho(rho))                               # [Mm, Nr] modes of d_x rho
    psi_lr = fd_dlr(psi.T, S.d).T; psi_lrlr = fd_dlr(psi_lr.T, S.d).T
    m2 = (S.m ** 2)[:, None]
    lap = (psi_lrlr - m2 * psi) / (r ** 2)[None, :]
    # m = 0: -Lap psi_0 = -(1/r^2) d_lr (r W_theta,0)   (W_theta,0 = psi_0')
    Wt0 = Wtm[0]
    lap0 = fd_dlr((r * Wt0)[:, None], S.d)[:, 0] / r ** 2
    lap = lap.clone(); lap[0] = lap0
    Em = -lap - F
    E = S.to_phys(Em)
    dxrho = S.to_phys(F)
    # ---- norms by band
    lrn = torch.tensor(lr, device=dev)
    bands = [(-14, -8), (-8, -6), (-6, -2), (-2, 2), (2, 6), (6, 10.01)]
    if 'bands' in kw:                       # e.g. bands=-14,-12,-10,-8,-6,-4,-2,2,6,10.01
        e = [float(v) for v in kw['bands'].split(',')]
        bands = list(zip(e[:-1], e[1:]))
    thd = (th * 180 / math.pi).cpu().numpy()
    near = np.zeros(Nth, bool)
    for z in zeros:
        dd = np.abs((thd - z + 180) % 360 - 180)
        near |= dd <= hw
    near_t = torch.tensor(near, device=dev)
    interior = (lrn >= lr[0] + 3 * S.d - 1e-12) & (lrn <= lr[-1] - 3 * S.d + 1e-12)     # R: drop the 3 one-sided rows at each end
    interiorE = (lrn >= lr[0] + 6 * S.d - 1e-12) & (lrn <= lr[-1] - 6 * S.d + 1e-12)    # E: the second derivative uses the one-sided rows twice (referee audit): drop 6
    scale_rho = rho.abs().amax(dim=1, keepdim=True) + 1e-300
    scale_adv = adv.abs() + rho.abs() + 1e-300
    scale_dx = dxrho.abs().amax(dim=1, keepdim=True) + 1e-300
    out = dict(file=f, p=p, cl=cl, Nr=Nr, Nth=Nth, lr0=float(lr[0]), lr1=float(lr[-1]), velocity_PFwdB_vs_PFwd_reldiff=dvel, angderiv=angderiv,
               info_defect=dict(D_ax=info.get('D_ax'), m1=info.get('m1'), normF=info.get('normF')), zeros_deg=zeros, halfwidth_deg=hw)
    def stats(X, msk_r, msk_t):
        M = msk_r[:, None] & msk_t[None, :]
        v = X[M]
        return dict(max=float(v.abs().max()), rms=float(torch.sqrt((v ** 2).mean())), n=int(M.sum()))
    rows = []
    for lo, hi in bands:
        mr = (lrn >= lo) & (lrn < hi) & interior
        if not bool(mr.any()):
            continue
        row = dict(band=[lo, hi], r_range=[float(math.exp(lo)), float(math.exp(min(hi, lr[-1])))])
        row['rho_max'] = float(rho[mr].abs().max())
        row['R_abs'] = stats(R, mr, ~near_t); row['R_abs_nearzeros'] = stats(R, mr, near_t)
        row['R_over_maxrho_ring'] = stats(R / scale_rho, mr, ~near_t); row['R_over_maxrho_ring_nearzeros'] = stats(R / scale_rho, mr, near_t)
        row['R_over_adv_plus_rho'] = stats(R / scale_adv, mr, ~near_t); row['R_over_adv_plus_rho_nearzeros'] = stats(R / scale_adv, mr, near_t)
        mrE = (lrn >= lo) & (lrn < hi) & interiorE
        row['E_abs'] = stats(E, mrE, ~near_t); row['E_abs_nearzeros'] = stats(E, mrE, near_t)
        row['E_over_maxdxrho_ring'] = stats(E / scale_dx, mrE, ~near_t); row['E_over_maxdxrho_ring_nearzeros'] = stats(E / scale_dx, mrE, near_t)
        # angular localisation: weak-axis sectors (within wa_deg of 0 / 180) vs the rest; angle of the maximum
        wa = float(kw.get('weakaxis_deg', '10'))
        dd0 = np.abs((thd + 180) % 360 - 180); dd180 = np.abs((thd - 180 + 180) % 360 - 180)
        weak_t = torch.tensor((dd0 <= wa) | (dd180 <= wa), device=dev)
        Rn = (R / scale_rho); En = (E / scale_dx)
        M = mr[:, None] & torch.ones(Nth, dtype=torch.bool, device=dev)[None, :]
        idx = torch.argmax((Rn.abs() * M).reshape(-1)); i0, j0 = int(idx) // Nth, int(idx) % Nth
        row['R_max_location'] = dict(lr=float(lr[i0]), theta_deg=float(thd[j0]), value=float(Rn[i0, j0]))
        ME = mrE[:, None] & torch.ones(Nth, dtype=torch.bool, device=dev)[None, :]
        idx = torch.argmax((En.abs() * ME).reshape(-1)); i0, j0 = int(idx) // Nth, int(idx) % Nth
        row['E_max_location'] = dict(lr=float(lr[i0]), theta_deg=float(thd[j0]), value=float(En[i0, j0]))
        row['R_over_maxrho_weakaxis'] = stats(Rn, mr, weak_t & ~near_t); row['R_over_maxrho_elsewhere'] = stats(Rn, mr, ~weak_t & ~near_t)
        row['E_over_maxdxrho_weakaxis'] = stats(En, mrE, weak_t & ~near_t); row['E_over_maxdxrho_elsewhere'] = stats(En, mrE, ~weak_t & ~near_t)
        row['R_over_maxrho_offaxis_offzero_rms'] = stats(Rn, mr, ~weak_t & ~near_t)['rms']
        row['frac_cells_R_above_1e-2'] = float(((Rn.abs() > 1e-2) & M).sum() / M.sum())
        rows.append(row)
    out['bands'] = rows
    # global normalised L2 norms (interior rows): ||R|| / ||rho||, ||E|| / ||d_x rho||, with the area weight r^2 dlr dth
    w = (r ** 2)[:, None] * interior[:, None]; wE = (r ** 2)[:, None] * interiorE[:, None]
    out['global_L2'] = dict(R_over_rho=float(torch.sqrt((w * R ** 2).sum() / (w * rho ** 2).sum())),
                            E_over_dxrho=float(torch.sqrt((wE * E ** 2).sum() / (wE * dxrho ** 2).sum())),
                            R_over_rho_weighted_rinv2=float(torch.sqrt((interior[:, None] * R ** 2 / (r ** 2)[:, None]).sum() / (interior[:, None] * rho ** 2 / (r ** 2)[:, None]).sum())))
    # the three one-sided rows at each end, reported separately (inner closure below e^-14 + outer tail)
    ends = ~interior
    out['end_rows'] = dict(R_over_maxrho_ring_max=float((R / scale_rho)[ends].abs().max()), E_over_maxdxrho_ring_max=float((E / scale_dx)[~interiorE].abs().max()))
    print(json.dumps(out))
    # human table
    print('\nband(lr)      r-range             max|rho|   R/maxrho(max,rms) away | near    R/(adv+rho) rms away | near   E/maxdxrho(max,rms) away | near')
    for row in rows:
        print('%-13s %-19s %9.2e  %8.1e %8.1e | %8.1e %8.1e   %8.1e | %8.1e   %8.1e %8.1e | %8.1e %8.1e' % (
            str(row['band']), '%.1e-%.1e' % tuple(row['r_range']), row['rho_max'],
            row['R_over_maxrho_ring']['max'], row['R_over_maxrho_ring']['rms'], row['R_over_maxrho_ring_nearzeros']['max'], row['R_over_maxrho_ring_nearzeros']['rms'],
            row['R_over_adv_plus_rho']['rms'], row['R_over_adv_plus_rho_nearzeros']['rms'],
            row['E_over_maxdxrho_ring']['max'], row['E_over_maxdxrho_ring']['rms'], row['E_over_maxdxrho_ring_nearzeros']['max'], row['E_over_maxdxrho_ring_nearzeros']['rms']))
    print('\nlocalisation (R/maxrho): band, max at (lr, theta deg), weak-axis sectors (+-%g deg of 0/180) rms | elsewhere rms | fraction of cells above 1e-2;  E/maxdxrho: max at, weak rms | elsewhere rms' % float(kw.get('weakaxis_deg', '10')))
    for row in rows:
        print('%-13s R max %8.1e at (%.2f, %6.1f)  weak %8.1e | else %8.1e | frac %6.3f   E max %8.1e at (%.2f, %6.1f)  weak %8.1e | else %8.1e' % (
            str(row['band']), row['R_max_location']['value'], row['R_max_location']['lr'], row['R_max_location']['theta_deg'], row['R_over_maxrho_weakaxis']['rms'], row['R_over_maxrho_elsewhere']['rms'], row['frac_cells_R_above_1e-2'],
            row['E_max_location']['value'], row['E_max_location']['lr'], row['E_max_location']['theta_deg'], row['E_over_maxdxrho_weakaxis']['rms'], row['E_over_maxdxrho_elsewhere']['rms']))
    print('global L2: ||R||/||rho|| = %.3e (area weight), %.3e (weight r^-2); ||E||/||d_x rho|| = %.3e; velocity PFwdB vs PFwd rel diff %.1e; end rows: R %.1e, E %.1e' % (
        out['global_L2']['R_over_rho'], out['global_L2']['R_over_rho_weighted_rinv2'], out['global_L2']['E_over_dxrho'], dvel,
        out['end_rows']['R_over_maxrho_ring_max'], out['end_rows']['E_over_maxdxrho_ring_max']))

if __name__ == '__main__':
    main()
