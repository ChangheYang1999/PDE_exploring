"""Far-field profile analysis of a saved branch point: b(inf, theta) on a fine angle grid from the EE interpolant,
Theta(theta) = rho/r^gamma at infinity, y-axis amplitude, half-width of the peak near pi/2, amplitude near the x-axis,
and the radial build-up of b along theta = 45 degrees."""
import sys, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1, diag

def analyze(path, device='cuda', verbose=True):
    m, b, cl, d = diag.load(path, device=device)
    C = m.ang.to_coef(b, 'EE'); k = torch.arange(m.M, device=device, dtype=torch.float64)
    binf_coef = (m.rad.ext1_R @ C)[0]
    th = torch.linspace(0, np.pi / 2, 721, device=device)
    sc = m.ang.s_of_theta(th)
    binf = (binf_coef[None, :] * torch.cos(sc[:, None] * (2 * k)[None, :])).sum(1)
    Theta = m.L ** (3 - m.gamma) * torch.cos(th) ** 2 * torch.sin(th) * binf     # rho / r^gamma at infinity
    thd = np.degrees(th.cpu().numpy()); binf_n = binf.cpu().numpy(); Th_n = Theta.cpu().numpy()
    ipk = int(np.argmax(Th_n)); peak = Th_n[ipk]
    half = np.where(Th_n[:ipk] < 0.5 * peak)[0]
    width = thd[ipk] - thd[half[-1]] if len(half) else float('nan')
    out = dict(eps=float(d['eps']) if 'eps' in d.files else None, cl=cl, N=m.N, M=m.M, beta=m.beta,
               b_yaxis=float(binf_n[-1]), b_xaxis=float(binf_n[0]), b_45=float(np.interp(45, thd, binf_n)),
               Theta_peak=float(peak), Theta_peak_deg=float(thd[ipk]), Theta_halfwidth_deg=float(width),
               binf_at=dict(zip([5, 20, 45, 70, 80, 85, 88], np.interp([5, 20, 45, 70, 80, 85, 88], thd, binf_n).round(2).tolist())))
    if verbose:
        print(f"{path}: eps={out['eps']} c_l={cl:.6f} ({m.N},{m.M},beta={m.beta}): b(inf) x-axis {out['b_xaxis']:.1f}, 45deg {out['b_45']:.1f}, y-axis {out['b_yaxis']:.1f}; "
              f"Theta peak {peak:.4g} at {thd[ipk]:.1f} deg, half-width {width:.1f} deg; b(inf) at 5..88 deg: {out['binf_at']}")
    return out

if __name__ == '__main__':
    for p in sys.argv[1:]:
        analyze(p)
