"""Dynamic rescaling (time marching) on the same polar-modal basis: an independent route to a self-similar state.
   Omega_s + (c_l X + U).grad Omega = c_w Omega + Theta_x,   Theta_s + (c_l X + U).grad Theta = (c_l + 2 c_w) Theta,
   c_w = Psi_xy(0)/2 (keeps Theta_y(0) fixed), c_l from keeping tau(x*) = Theta_y(x*,0) fixed (SPEC sec. 4):
   tau_s = -(c_l x + U1) tau_x + (2 c_w - d_y U2) tau  =>  c_l = [ -U1 tau_x + (2 c_w - d_y U2) tau + kappa (tau - tau0) ] / (x* tau_x) at x*.
   Steady state with c_w < 0: beta = c_l/(-c_w); profile of (P): Omega/lambda, Theta/lambda^2, lambda = -c_w.
Method of lines: fields on the collocation grid from the basis matrices, RHS projected back on the basis by least squares
(pseudo-inverse), RK4 in s. Basis far-field exponents are frozen at beta_basis (reported; refine later)."""
import argparse, json, math, os, sys, time, numpy as np, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *

ap = argparse.ArgumentParser()
ap.add_argument('--init', required=True); ap.add_argument('--out', required=True)
ap.add_argument('--beta-basis', type=float, default=None); ap.add_argument('--Nr', type=int, default=300); ap.add_argument('--Nth', type=int, default=48)
ap.add_argument('--qmax', type=float, default=0.99); ap.add_argument('--dt', type=float, default=2e-3); ap.add_argument('--smax', type=float, default=20.0)
ap.add_argument('--xstar', type=float, default=4.0); ap.add_argument('--kappa', type=float, default=1.0); ap.add_argument('--every', type=int, default=200)
ap.add_argument('--rcond', type=float, default=1e-9); ap.add_argument('--filt', type=float, default=36.0, help='exp filter strength (0 = off)'); ap.add_argument('--filt-p', type=int, default=16); ap.add_argument('--fixed-beta', type=float, default=None, help='if set, c_l = beta*(-c_w) (fixed-beta DR)')
args = ap.parse_args()
device = dev()
d = np.load(args.init, allow_pickle=True)
NT, NO, K = int(d['NT']), int(d['NO']), int(d['K']); L = float(d['L'])
beta_b = args.beta_basis if args.beta_basis is not None else float(d['beta'])
P = Params(beta_b, L=L)
cT = torch.tensor(d['cT'], dtype=DT, device=device).reshape(NT, K); cO = torch.tensor(d['cO'], dtype=DT, device=device).reshape(NO, K)
# grid
j = torch.arange(args.Nr, dtype=DT, device=device); q = args.qmax * 0.5 * (1 - torch.cos(math.pi * (j + 0.5) / args.Nr)); r, _ = torch.sort(P.u_of_q(q) * P.L)
ix = int((r - args.xstar).abs().argmin()); xs = float(r[ix])
xg, wg = np.polynomial.legendre.leggauss(args.Nth); th = torch.tensor((xg + 1) * 0.25 * math.pi, dtype=DT, device=device)
N, M = args.Nr, args.Nth
# radial matrices per mode
HT = []; dHT = []
for n in range(NT):
    H, dH = radial_basis(P, r, 2 * n + 1, P.gamma_T, K); HT.append(H); dHT.append(dH)
HT = torch.stack(HT); dHT = torch.stack(dHT)                       # (NT, N, K)
HO = []; dHO = []
for n in range(1, NO + 1):
    H, dH = radial_basis(P, r, 2 * n, P.gamma_O, K); HO.append(H); dHO.append(dH)
HO = torch.stack(HO); dHO = torch.stack(dHO)
PSI, DPSI, CROW = inverse_matrices(P, r, NO, K)                    # (NO, N, K)
mT = torch.tensor([2 * n + 1 for n in range(NT)], dtype=DT, device=device); mO = torch.tensor([2 * n for n in range(1, NO + 1)], dtype=DT, device=device)
sT = torch.sin(mT[:, None] * th[None, :]); cTh = torch.cos(mT[:, None] * th[None, :])     # (NT, M)
sO = torch.sin(mO[:, None] * th[None, :]); cO_ = torch.cos(mO[:, None] * th[None, :])
cs = torch.cos(th)[None, :]; sn = torch.sin(th)[None, :]; R = r[:, None]; X = R * cs; Y = R * sn
# projection: least squares onto basis on the grid (field values (N,M) -> coefficients (Nmodes,K)); per mode via angular quadrature
# angular Gauss-Legendre weights on (0, pi/2): modes are orthogonal on (0, pi/2) for sin((2n+1)th) and sin(2n th)
wth = torch.tensor(wg * 0.25 * math.pi, dtype=DT, device=device)
normT = (sT * sT * wth[None, :]).sum(1); normO = (sO * sO * wth[None, :]).sum(1)      # = pi/4 each
pinvT = torch.linalg.pinv(HT, rcond=args.rcond); pinvO = torch.linalg.pinv(HO, rcond=args.rcond)   # (NT, K, N)
def project(F, which):
    if which == 'T':
        radial = torch.einsum('nm,am->na', F, sT * wth[None, :]) / normT[None, :]        # (N, NT) radial profiles per mode
        return torch.einsum('akn,na->ak', pinvT, radial)                                # (NT, K)
    radial = torch.einsum('nm,am->na', F, sO * wth[None, :]) / normO[None, :]
    return torch.einsum('akn,na->ak', pinvO, radial)
def fields(cT, cO):
    f = torch.einsum('ank,ak->an', HT, cT); df = torch.einsum('ank,ak->an', dHT, cT)
    g = torch.einsum('ank,ak->an', HO, cO); dg = torch.einsum('ank,ak->an', dHO, cO)
    psi = torch.einsum('ank,ak->an', PSI, cO); dpsi = torch.einsum('ank,ak->an', DPSI, cO)
    Th = f.T @ sT; Thr = df.T @ sT; Thth_r = ((mT[:, None] * f) / r[None, :]).T @ cTh
    Om = g.T @ sO; Omr = dg.T @ sO; Omth_r = ((mO[:, None] * g) / r[None, :]).T @ cO_
    Psir = dpsi.T @ sO; Psith_r = ((mO[:, None] * psi) / r[None, :]).T @ cO_
    Thx = cs * Thr - sn * Thth_r; Thy = sn * Thr + cs * Thth_r; Omx = cs * Omr - sn * Omth_r; Omy = sn * Omr + cs * Omth_r
    U1 = -(sn * Psir + cs * Psith_r); U2 = cs * Psir - sn * Psith_r
    c = float(CROW @ cO[0])
    # x-axis quantities at x*: tau = sum m f_n/x, tau_x = sum m (f_n'/x - f_n/x^2); U1(x*,0) = -Psi_y = -(Psith_r at th=0) = -sum m psi_n/x ; d_y U2 = sum m (psi_n'/x - psi_n/x^2) ... (U2/y limit)
    tau = float((mT * f[:, ix]).sum() / xs); taux = float((mT * (df[:, ix] / xs - f[:, ix] / xs ** 2)).sum())
    U1s = -float((mO * psi[:, ix]).sum() / xs); U2ys = float((mO * (dpsi[:, ix] / xs - psi[:, ix] / xs ** 2)).sum())
    return dict(Th=Th, Thx=Thx, Thy=Thy, Om=Om, Omx=Omx, Omy=Omy, U1=U1, U2=U2, c=c, tau=tau, taux=taux, U1s=U1s, U2ys=U2ys, f=f, g=g)
F0 = fields(cT, cO); tau0 = F0['tau']
kk = torch.arange(K, dtype=DT, device=device) / (K - 1); nnT = torch.arange(NT, dtype=DT, device=device) / max(NT - 1, 1); nnO = torch.arange(NO, dtype=DT, device=device) / max(NO - 1, 1)
filtT = torch.exp(-args.filt * kk ** args.filt_p)[None, :] * torch.exp(-args.filt * nnT ** args.filt_p)[:, None] if args.filt > 0 else torch.ones(NT, K, dtype=DT, device=device)
filtO = torch.exp(-args.filt * kk ** args.filt_p)[None, :] * torch.exp(-args.filt * nnO ** args.filt_p)[:, None] if args.filt > 0 else torch.ones(NO, K, dtype=DT, device=device)
def rhs(cT, cO):
    F = fields(cT, cO); cw = F['c'] / 2
    if args.fixed_beta is not None:
        cl = args.fixed_beta * (-cw)
    else:
        cl = (-F['U1s'] * F['taux'] + (2 * cw - F['U2ys']) * F['tau'] + args.kappa * (F['tau'] - tau0)) / (xs * F['taux'])
    W1 = cl * X + F['U1']; W2 = cl * Y + F['U2']
    dTh = -(W1 * F['Thx'] + W2 * F['Thy']) + (cl + 2 * cw) * F['Th']
    dOm = -(W1 * F['Omx'] + W2 * F['Omy']) + cw * F['Om'] + F['Thx']
    return project(dTh, 'T'), project(dOm, 'O'), dict(cl=cl, cw=cw, c=F['c'], tau=F['tau'], a0=float(F['f'][0, 0] / r[0]))
logf = open(args.out + '.log', 'a'); hist = []
def log(s): print(s); logf.write(s + '\n'); logf.flush()
log('# %s args=%s x*=%.4f tau0=%.5f' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), vars(args), xs, tau0))
s = 0.0; step = 0; dt = args.dt
while s < args.smax:
    k1T, k1O, info = rhs(cT, cO)
    k2T, k2O, _ = rhs(cT + 0.5 * dt * k1T, cO + 0.5 * dt * k1O)
    k3T, k3O, _ = rhs(cT + 0.5 * dt * k2T, cO + 0.5 * dt * k2O)
    k4T, k4O, _ = rhs(cT + dt * k3T, cO + dt * k3O)
    cT = cT + dt / 6 * (k1T + 2 * k2T + 2 * k3T + k4T); cO = cO + dt / 6 * (k1O + 2 * k2O + 2 * k3O + k4O)
    cT = cT * filtT; cO = cO * filtO
    s += dt; step += 1
    if not torch.isfinite(cT).all() or not torch.isfinite(cO).all():
        log('# blow-up at s=%.4f' % s); break
    if step % args.every == 0:
        lam = -info['cw']; beta_now = info['cl'] / lam if lam != 0 else float('nan')
        # residual of (P) for the rescaled profile
        rec = dict(s=s, cl=info['cl'], cw=info['cw'], c=info['c'], beta=beta_now, a0=info['a0'], tau=info['tau'], dcT=float((dt * k1T).abs().max() / cT.abs().max()), dcO=float((dt * k1O).abs().max() / cO.abs().max()))
        if lam > 0:
            grid = Grid(r, th); Mx = field_matrices(P, grid, NT, NO, K) if step == args.every else Mx
            Rs = residuals(Mx, grid, (cT / lam ** 2).reshape(-1), (cO / lam).reshape(-1), beta_now)
            rec['maxnormT'] = float((Rs['RT'].abs() / (Rs['NT'] + 1e-300)).max()); rec['maxnormO'] = float((Rs['RO'].abs() / (Rs['NO'] + 1e-300)).max())
            np.savez(args.out + '.npz', cT=(cT / lam ** 2).reshape(-1).cpu().numpy(), cO=(cO / lam).reshape(-1).cpu().numpy(), beta=beta_now, L=L, NT=NT, NO=NO, K=K,
                     gamma_T=P.gamma_T, gamma_O=P.gamma_O, mu=P.mu, umax=0, Nr=N, Nth=M, hist=json.dumps(hist))
        hist.append(rec); log(json.dumps(rec))
log('# done s=%.3f' % s)
