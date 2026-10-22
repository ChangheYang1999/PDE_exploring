"""Transport a generating-function state to another exponent beta (after the authors' reproj.py): least-squares fit of the
jets G_x (physical y), G_x,eta (= A) and G_xx (= B0) of the old state (free-exponent basis at beta0, incl. core patches) at the collocation-type
points of both bases, with relative weights 1/(|target| + 1e-3 |A| (1 + x)) and the heavy row H(0,0) = 1, by chunked normal equations on the GPU
(column-scaled, tiny ridge). The result is a state at beta1 that represents (nearly) the same profile, so a fixed-beta run from it starts
without the reinterpretation shock. Usage: python3 reproj_beta.py old.npz new.npz beta1 [--ridge r] [--Nt n] [--Ns n]"""
import sys, math, numpy as np, torch
torch.set_num_threads(1)
import jets; DEV = jets.DEV
from jets import monos, DT
from model_fb import ModelFB, ts_to_xeta_fb
from model_core_fb import ModelCoreFB
from model_core import as_patches
d = np.load(sys.argv[1]); out = sys.argv[2]; beta1 = float(sys.argv[3])
def opt(name, default, typ=float):
    return typ(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
J, Kw = int(d['J']), int(d['Kw']); beta0 = float(d['beta']) if 'beta' in d.files else 3.0; M = int(d['M']) if 'M' in d.files else 3
alpha = float(d['alpha']); se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
core = as_patches(d['core']) if 'core' in d.files else []
mk = lambda b: (ModelCoreFB(J, Kw, core, beta=b, M=M, alpha=alpha, se=se, gam=gam) if core else ModelFB(J, Kw, beta=b, M=M, alpha=alpha, se=se, gam=gam))
old, new = mk(beta0), mk(beta1)
co = torch.tensor(np.concatenate([d['c'], d['cc']]) if core else d['c'], dtype=DT, device=DEV)
Nt, Ns = opt('--Nt', 2 * J + 8, int), opt('--Ns', 2 * Kw + 8, int); ridge = opt('--ridge', 1e-14)
def pts(b, shift, tmin):
    it = (np.arange(Nt) + 0.5 + shift) / Nt; is_ = (np.arange(Ns) + 0.5 + shift) / Ns
    tau = 0.5 * (1 - np.cos(np.pi * it)); t = tau if alpha <= 0 else 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1)
    t = tmin + (1 - tmin) * t; s = 0.5 * (1 - np.cos(np.pi * is_))
    T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
    x, eta = ts_to_xeta_fb(T, S, b, M, se); k = (x > 1e-12) & (eta > 1e-12)
    return x[k], eta[k]
xa, ea = pts(beta1, 0.0, 3e-3); xb, eb = pts(beta0, 0.21, 3e-3)
# inner points near the centre (as the solver's --inner 64 40 1e-3 2)
rho = np.logspace(-3, np.log10(2.0), 64); th = 0.5 * np.pi * (0.5 * (1 - np.cos(np.pi * (np.arange(40) + 0.5) / 40))); Rr, Th = np.meshgrid(rho, th, indexing='ij')
x = torch.tensor(np.concatenate([xa, xb, (Rr * np.cos(Th)).ravel()]), dtype=DT, device=DEV); e = torch.tensor(np.concatenate([ea, eb, (Rr * np.sin(Th)).ravel()]), dtype=DT, device=DEV)
L, ix = monos(2); nb = new.nb
AtA = torch.zeros(nb, nb, dtype=DT, device=DEV); Atb = torch.zeros(nb, dtype=DT, device=DEV)
keys = [(1, 0), (1, 1), (2, 0)]
with torch.no_grad():
    for ch in torch.split(torch.arange(x.shape[0], device=DEV), 1024):
        Bo = old.basis_matrix(x[ch], e[ch], p=2) @ co; Bn = new.basis_matrix(x[ch], e[ch], p=2)
        for key in keys:
            tgt = Bo[ix[key]]; sc = 1.0 / (tgt.abs() + 1e-3 * Bo[ix[(1, 1)]].abs() * (1 + x[ch]))
            Aw = Bn[ix[key]] * sc[:, None]; bw = tgt * sc
            AtA += Aw.T @ Aw; Atb += Aw.T @ bw
        del Bo, Bn
    h = torch.tensor(new.h00_row(), dtype=DT, device=DEV) * 1e6; AtA += h[:, None] * h[None, :]; Atb += h * 1e6
    D = torch.sqrt(torch.diag(AtA)); D = torch.where(D == 0, torch.ones_like(D), D)
    As = AtA / D[:, None] / D[None, :] + ridge * torch.eye(nb, dtype=DT, device=DEV); bs = Atb / D
    w, V = torch.linalg.eigh(As); keep = w > 1e-15 * w[-1]
    cs = V[:, keep] @ ((V[:, keep].T @ bs) / w[keep]); c = cs / D
    # fit quality by band (relative, per point, max over the three jets) and the init residual proxy
    per = []; rad = []; phd = []
    for ch in torch.split(torch.arange(x.shape[0], device=DEV), 1024):
        Bo = old.basis_matrix(x[ch], e[ch], p=2) @ co; Bn = new.basis_matrix(x[ch], e[ch], p=2) @ c
        errs = []
        for key in keys:
            tgt = Bo[ix[key]]; sc = 1.0 / (tgt.abs() + 1e-3 * Bo[ix[(1, 1)]].abs() * (1 + x[ch])); errs.append(((Bn[ix[key]] - tgt) * sc).abs())
        per.append(torch.stack(errs).max(0).values.cpu().numpy()); rad.append(torch.hypot(x[ch], Bo[ix[(1, 0)]]).cpu().numpy()); phd.append(torch.rad2deg(torch.atan2(Bo[ix[(1, 0)]], x[ch])).cpu().numpy())
per = np.concatenate(per); rad = np.concatenate(rad); phd = np.concatenate(phd)
for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 1e3), (1e3, 1e5), (1e5, 1e12)]:
    row = []
    for plo, phi_ in [(0, 45), (45, 85), (85, 90.1)]:
        m = (rad >= lo) & (rad < hi) & (phd >= plo) & (phd < phi_); row.append('%.1e' % per[m].max() if m.any() else '   -   ')
    print('  r [%g, %g): max rel jet error by angle band (0-45, 45-85, 85-90): %s' % (lo, hi, '  '.join(row)))
print('reproj_beta %s: beta %.6f -> %.6f, %d points, %d unknowns, kept %d eigen-directions; rms rel %.2e max rel %.2e; H00 %.12f; max|c| %.3e' % (
    sys.argv[1], beta0, beta1, x.shape[0], nb, int(keep.sum()), float(np.sqrt(np.mean(per ** 2))), float(per.max()), float(torch.tensor(new.h00_row(), dtype=DT, device=DEV) @ c), float(c.abs().max())))
cn = c.cpu().numpy()
np.savez(out, c=cn[:new.nbo] if core else cn, a0=float(d['a0']), J=J, Kw=Kw, m=3, beta=beta1, M=M, alpha=alpha, se=se, gam=gam, l=float(d['l']) if 'l' in d.files else 1.0, src=sys.argv[1], fb=1,
         **(dict(cc=cn[new.nbo:], core=np.array(core, dtype=float).reshape(-1, 4)) if core else {}))
