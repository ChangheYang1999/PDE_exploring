"""Independent-differentiation residual of forced states: R = V.grad rho - rho, V = c_l X + h W + (1-h) E, with grad by
PolarGrid.grad (q-point Gauss panel polynomial, no left edge; the marching uses the (q+1)-point polynomial with the edge)
and Fourier in theta. Prints, per radial decade, max|R| / max|rho| and the angular-tail ratio of xi (max |xi_m|, |m| >=
nt/2 - 6, over max |xi_m|), to locate under-resolution."""
import sys, math, numpy as np, torch
sys.path.insert(0, 'code')
from forced_char import ForcedSolver
for f in sys.argv[1:]:
    D = torch.load(f, weights_only=False); A = D['args']
    S = ForcedSolver(D['edges'], D['q'], D['nt'], D['r1'], 'cuda'); S.set_forcing(D['h'], A['mu'], A['LE'])
    d = D['d']; h = D['h']; xi = D['xi'].cuda(); rho = xi**2
    W1, W2 = S.velocity(rho, d['p'])
    V1 = d['cl']*S.X + h*W1 + (1 - h)*S.E1; V2 = d['cl']*S.Y + h*W2 + (1 - h)*S.E2
    gx, gy = S.G.grad(rho.cpu().numpy())
    R = (V1*torch.tensor(gx, device='cuda') + V2*torch.tensor(gy, device='cuda') - rho).abs().amax(1).cpu().numpy()
    rm = rho.abs().amax(1).cpu().numpy()
    xm = torch.fft.fft(xi, dim=1).abs().cpu().numpy(); m = np.abs(np.fft.fftfreq(S.nt, 1/S.nt))
    tail = xm[:, m >= S.nt//2 - 6].max(1)/np.maximum(xm.max(1), 1e-300)
    r = S.r.cpu().numpy()
    print(f.split('/')[-1], 'h=%.5f c=%.4f cl=%.4f' % (h, d['c'], d['cl']))
    for lo in [1e-6, 1e-3, 1e-1, 1, 10, 1e2, 1e3, 1e4, 1e6, 1e8]:
        i = (r >= lo) & (r < lo*(10 if lo >= 1 else 100))
        if i.any(): print('   r in [%.0e, %.0e): max|R|/max|rho| = %.2e   angular tail %.2e' % (lo, lo*(10 if lo >= 1 else 100), R[i].max()/rm[i].max(), tail[i].max()))
