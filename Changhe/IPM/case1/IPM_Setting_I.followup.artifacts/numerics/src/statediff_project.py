"""Is the two-grid difference of the stagnation states a displacement along the valley? (verifier 'rate' (4): project, do not argue by signs.)
Interpolate the coarse state to the fine grid (ipm_newton.project_state, same c_l; C kept), form delta z = z_fine - z_coarse->fine in fine node
coordinates (delta b at i = 1..N, delta c_l, delta C), and report |delta z|, its components, and the fraction of its norm in the span of the k softest
Ritz vectors (k = 1, 2, 3, 10) and of the 24 stored directions Q of the fine Ritz file.
Usage: python3 src/statediff_project.py runs/<coarse>.npz runs/<fine>.npz runs/ritz_<fine_tag>.pt"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

cpath, fpath, rpath = sys.argv[1:4]
mc, xc, dc = ipn.load_state(cpath); mf, xf, df = ipn.load_state(fpath)
xp = ipn.project_state(mc, xc, mf); bp, clp = mf.unpack(xp); bf, clf = mf.unpack(xf)
dz = torch.cat([(bf - bp)[1:].reshape(-1), torch.tensor([float(clf) - float(clp), float(df['C']) - float(dc['C'])], device=bf.device, dtype=torch.float64)])
R = torch.load(rpath); Q = R['Q'].cuda().double(); Wv = R['Wv'].cuda().double(); kk = Wv.shape[1]
nz = dz.norm().item()
print(f'coarse {cpath} -> fine {fpath}: |delta z| {nz:.4e}; delta c_l {dz[-2].item():+.4e}; delta C {dz[-1].item():+.4e}; |delta b| {dz[:-2].norm().item():.4e}, max |delta b| {dz[:-2].abs().max().item():.3e}')
for k in (1, 2, 3, 6, 10):
    W = Wv[:, kk - k:]; c = W.T @ dz; print(f'  fraction of |delta z| in the span of the {k:2d} softest Ritz vectors: {c.norm().item() / nz:.4f}  (coefficients ' + ' '.join(f'{x:+.3e}' for x in c.cpu().numpy()[::-1][:3]) + ' ...)')
c = Q.T @ dz; print(f'  fraction in the span of all {Q.shape[1]} stored directions: {c.norm().item() / nz:.4f}')
# the same for the shape part only and for the parameter part only
dzs = dz.clone(); dzs[-2:] = 0; c = Wv[:, kk - 3:].T @ dzs; print(f'  shape part only (|.| {dzs.norm().item():.3e}): fraction in the 3 softest {c.norm().item() / dzs.norm().item():.4f}')
# interpolation error control: project fine -> coarse -> fine and measure
xcf = ipn.project_state(mf, xf, mc); xff = ipn.project_state(mc, xcf, mf); bff, _ = mf.unpack(xff)
e = (bf - bff)[1:].reshape(-1); print(f'  interpolation round-trip error fine->coarse->fine: |e| {e.norm().item():.3e} (max {e.abs().max().item():.3e}); its fraction in the 3 softest {((Wv[:, kk-3:].T @ torch.cat([e, torch.zeros(2, device=e.device, dtype=e.dtype)])).norm() / e.norm()).item():.4f}')
