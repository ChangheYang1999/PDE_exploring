"""dr_vis_modes.py -- spectrum of the DR Jacobian restricted to the visible coefficient directions (sigma >= thr of the largest per mode), with and without the
perturbation's own velocity (feedback), and the localisation of the leading eigenvectors (fraction of |rho_eig|^2 by radial shell, dominant angular index).
usage: python3 src/dr_vis_modes.py state.pt|const N M C [thr=1e-6 top=6 basis=local]"""
import sys, math, torch
sys.path.insert(0, 'numerics/src'); import dr, ipm3ql
torch.set_default_dtype(torch.float64)
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
src, N, M, C = args[0], int(args[1]), int(args[2]), float(args[3]); thr = float(kw.get('thr', 1e-6)); top = int(kw.get('top', 6)); dev = 'cuda'
m = dr.DR(N, M, C, device=dev, basis=kw.get('basis', 'local'))
if src == 'const':
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = float(kw.get('a0', 1.0)); u = m.beta_to_u(beta0)
else:
    st = torch.load(src, weights_only=False); qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=1.0, gamma=1 / st['cl'], device=dev, Lf=st['Lf'])
    u = m.project(((qo.rad.sigR[:, None] ** qo.kk[None, :]) * st['beta'].to(dev)) @ m.C_f.T)
du, info = m.rhs(u, want=True); a0 = m.jets(u)[0].item(); cw = info['cw'].item(); cx = info['cx'].item()
Vs = []
for k in range(M):
    A = (m.rad.sigR[:, None] ** k) * m.Ext[k]; U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); keep = S_ >= thr * S_[0]
    Vk = torch.zeros(m.nu, int(keep.sum()), device=dev); Vk[m.offs[k]:m.offs[k + 1], :] = Vh_[keep].T; Vs.append(Vk)
V = torch.cat(Vs, 1)
r = m.rad.rR; w = m.rad.wR; sinf = m.angf.sin
print(f"# {src} {N}x{M} C={C} basis {m.basis} thr {thr:.0e} (visible dim {V.shape[1]} of {m.nu}): a0 {a0:.5f} c_w {cw:.5f} c_x {cx:.5f}")
for fb in [True, False]:
    J = m.jacobian_dr(u, feedback=fb); Jv = V.T @ J @ V; ev, W = torch.linalg.eig(Jv); order = torch.argsort(-ev.real); ev = ev[order]; W = W[:, order]
    print(f"# {'FULL linearisation' if fb else 'TRANSPORT-ONLY (no velocity feedback)'}: max Re {ev.real.max().item():+.4e} (= {ev.real.max().item()/a0:+.3f} a0), #Re > 1e-10: {(ev.real > 1e-10).sum().item()}, #Re > 0.5 c_w: {(ev.real > 0.5*cw).sum().item()}, radius {ev.abs().max().item():.3e}")
    seen = set(); n = 0
    for i in range(len(ev)):
        key = (round(ev[i].real.item(), 5), round(abs(ev[i].imag.item()), 5))
        if key in seen: continue
        seen.add(key); n += 1
        if n > top: break
        v = (V.to(torch.complex128) @ W[:, i]); beta_eig = m.beta_full(v.real) + 1j * m.beta_full(v.imag)
        bk = (m.rad.sigR[:, None] ** m.kk[None, :]) * beta_eig; rho_eig = (r * w)[:, None] * (sinf[None, :] * (bk @ m.C_f.T.to(bk.dtype)))
        p = rho_eig.abs() ** 2; tot = p.sum().item(); fr = [p[(r > lo) & (r <= hi)].sum().item() / tot for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e300)]]
        kpow = (bk.abs() ** 2 * ((r * w)[:, None] ** 2)).sum(0); kd = kpow.argmax().item(); i_max = p.sum(1).argmax().item()
        print(f"   lambda {ev[i].real.item():+.4e} {ev[i].imag.item():+.4e}j | |rho_eig|^2 fractions r<.1 .1-1 1-10 10-100 >100: {fr[0]:.3f} {fr[1]:.3f} {fr[2]:.3f} {fr[3]:.3f} {fr[4]:.3f} | dominant k {kd} ({(kpow[kd]/kpow.sum()).item():.2f}) | r of max {r[i_max].item():.3e}")
