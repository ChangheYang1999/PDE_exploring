"""Sampled elliptic defect E = -Lap Psi - Omega of saved states on the common 10000-point grid of code/common_grid_resid.py (200 radii
geomspace(0.02, 2000) * (1 + 1e-3 sin k), 50 interior angles (j + 0.37) (pi/2)/50), region-wise (r < 1, 1-10, 10-100, >= 100).
Method: -Lap Psi = -curl U with U = (-Psi_y, Psi_x) (curl U = d_x U_2 - d_y U_1 = Lap Psi), evaluated in polar form
curl U = (1/r) d_r (r U_theta) - (1/r) d_theta U_r from the state's modal velocity (code/diag_state.eval_state, the same Green inverse as
the fit) by fourth-order central differences: fractional radial step h_r = hr * r (five radii per sample radius, angles unchanged), angular
step h_th = hth radians (five angles per sample angle, radii unchanged). The paired fractional radial steps hr and angular steps hth are 1e-3,
3e-4 and 1e-4; their reported maxima provide a step-sensitivity check, not a bound on differentiation or field-evaluation error (regional maxima
are compared, not pointwise differences). For exact, well-conditioned velocity samples rounded at scale eps |U|, the curl roundoff scales like
eps |U| / (h r); field-evaluation errors (modal cancellation, Green quadrature) must be assessed separately. E is compared with Omega = x y G
from the basis. Reported per region: max |E|, max of the pointwise ratio |E| / N_E with N_E = |Omega| + |(1/r) d_r(r U_theta)| +
|(1/r) d_theta U_r| (formed where N_E > 0, undefined ratios counted, no floor), max |E| / max_region |Omega|, and the sampled maximum of
|R_Theta| in the region for scale (a scale comparison, not an error estimate). Sampled values of fitted states on a finite grid: no regional
bound. Code reviewed by an external referee; its repairs applied. Usage: python3 code/elliptic_defect.py [--sub K] state1.npz [state2.npz ...]"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def eval_chunked(d, R, T, keys, nr_chunk):
    out = {k: [] for k in keys}
    for i in range(0, len(R), nr_chunk):
        m, f = eval_state(d, R[i:i + nr_chunk], T)
        for k in keys: out[k].append(f[k].detach().cpu().numpy())
        del m, f; torch.cuda.empty_cache()
    return {k: np.concatenate(out[k], axis=0) for k in keys}

def main(paths, steps=(1e-3, 3e-4, 1e-4), sub=1):
    if sub < 1: raise ValueError("sub must be a positive integer")
    k = np.arange(200); R = np.geomspace(0.02, 2000, 200) * (1 + 1e-3 * np.sin(k)); T = (np.arange(50) + 0.37) * (np.pi / 2) / 50
    if sub > 1: R = R[::sub]; T = T[::sub]   # quick test only (every sub-th radius and angle; all statistics then refer to this smaller set)
    nR, nT = len(R), len(T); c5 = np.array([1.0, -8.0, 0.0, 8.0, -1.0]) / 12.0   # f'(0) ~ sum c5[j] f(j h) / h, j = -2..2
    print(f"common grid: {nR} radii in [{R.min():.3g}, {R.max():.4g}] x {nT} interior angles ({nR*nT} points); E = -Lap Psi - Omega = -curl U - Omega")
    print("state                     N   M  beta   hr=hth   region   max|E|     max(|E|/N_E) nundef  max|E|/max|Om|  max|Om|    max|R_T|   max|E|/max|R_T|")
    for p in paths:
        d = load_state(p); beta = float(d['beta']); name = p.split('/')[-1].replace('.npz', '')
        base = eval_chunked(d, R, T, ('a', 'G', 'Ra'), 50)
        X = R[:, None] * np.cos(T)[None, :]; Y = R[:, None] * np.sin(T)[None, :]; RR = np.hypot(X, Y)
        Om = X * Y * base['G']; RT = X**2 * Y * base['Ra']
        for h in steps:
            Rj = np.concatenate([R * (1 + j * h) for j in (-2, -1, 0, 1, 2)])          # block j has the radii R (1 + j h), angles T
            fA = eval_chunked(d, Rj, T, ('U1', 'U2'), 50)
            cT, sT = np.cos(T)[None, :], np.sin(T)[None, :]
            Uth = (-sT * fA['U1'] + cT * fA['U2']).reshape(5, nR, nT) * Rj.reshape(5, nR)[:, :, None]   # r U_theta at the stencil radii
            d_r_rUth = sum(c5[j] * Uth[j] for j in range(5)) / (h * R)[:, None]
            Tl = np.concatenate([T + l * h for l in (-2, -1, 0, 1, 2)])                 # block l has the angles T + l h, radii R
            fB = eval_chunked(d, R, Tl, ('U1', 'U2'), 10)
            cL, sL = np.cos(Tl)[None, :], np.sin(Tl)[None, :]
            Ur = (cL * fB['U1'] + sL * fB['U2']).reshape(nR, 5, nT)
            d_th_Ur = sum(c5[j] * Ur[:, j, :] for j in range(5)) / h
            curl = (d_r_rUth - d_th_Ur) / R[:, None]
            E = -curl - Om
            NE = np.abs(Om) + np.abs(d_r_rUth / R[:, None]) + np.abs(d_th_Ur / R[:, None])
            if not all(np.isfinite(v).all() for v in (E, NE, RT)): raise ValueError("nonfinite elliptic diagnostic")
            with np.errstate(divide='ignore', invalid='ignore'):
                rE = np.where(NE > 0, np.abs(E) / NE, np.nan)
            for lab, msk in (('r<1', RR < 1), ('1-10', (RR >= 1) & (RR < 10)), ('10-100', (RR >= 10) & (RR < 100)), ('>=100', RR >= 100)):
                if not msk.any(): print(f"{name} {lab}: no samples"); continue
                mE = np.abs(E[msk]).max(); mO = np.abs(Om[msk]).max(); mT = np.abs(RT[msk]).max()
                vals = rE[msk]; defined = vals[~np.isnan(vals)]
                max_rE = defined.max() if defined.size else np.nan
                qO = mE / mO if mO > 0 else np.nan; qT = mE / mT if mT > 0 else np.nan
                print(f"{name:25s} {int(d['N']):3d} {int(d['M']):3d} {beta:5.3f}  {h:7.0e}  {lab:7s} {mE:9.3e}  {max_rE:9.3e}    {int(np.isnan(vals).sum()):4d}   {qO:9.3e}      {mO:9.3e}  {mT:9.3e}  {qT:9.3e}", flush=True)

if __name__ == '__main__':
    args = sys.argv[1:]; sub = 1
    if args and args[0] == '--sub':
        if len(args) < 3: raise SystemExit("usage: elliptic_defect.py [--sub K] state.npz ...")
        sub = int(args[1]); args = args[2:]
    if not args: raise SystemExit("provide at least one state file")
    main(args, sub=sub)
