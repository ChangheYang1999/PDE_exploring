"""dr_modes.py -- eigen-decomposition of the DR Jacobian at a saved state (or the constant start) and localisation of the leading eigenvectors:
for the eigenvalues with the largest real parts, the fraction of the perturbation's density norm (node values of rho_eig = y w b_eig on the fine
angular grid, weighted by nothing) in r <= 1, 1 < r <= 10, 10 < r <= 100, r > 100, its dominant angular mode k (of cos 2k theta) and the radius of
its maximum.  Purpose: separate far-end transport pseudo-modes of the compactified polynomial basis (field at r -> infinity) from core modes (candidates
for the Rayleigh-Taylor instability of the unstably stratified core, rate <= a0 k_1^2/|k|^2 in DR time).
usage: python3 src/dr_modes.py state.pt|const N M C [top=12]"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import dr
torch.set_default_dtype(torch.float64)
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
src, N, M, C = args[0], int(args[1]), int(args[2]), float(args[3]); top = int(kw.get('top', 12)); dev = 'cuda'; metric = kw.get('metric', 'rho')
m = dr.DR(N, M, C, device=dev)
if src == 'const':
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = float(kw.get('a0', 1.0)); u = m.beta_to_u(beta0); label = f'constant start a0={kw.get("a0", 1.0)}'
else:
    st = torch.load(src, weights_only=False)
    if 'u' in st and len(st['u']) == m.nu and abs(st['cl'] - C) < 1e-12: u = st['u'].to(dev)
    else:
        import q_free, ipm3ql
        qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=st.get('L', 1.0), gamma=1 / st['cl'], device=dev, Lf=st.get('Lf', 1.0)); _, u = q_free.regrid_fit(qo, st['beta'].to(dev), m)
    label = src
du, info = m.rhs(u, want=True); a0 = m.jets(u)[0].item(); cw = info['cw'].item(); cx = info['cx'].item()
J = m.jacobian_dr(u); ev, V = torch.linalg.eig(J)
order = torch.argsort(-ev.real); ev = ev[order]; V = V[:, order]
r = m.rad.rR; w = m.rad.wR; sinf = m.angf.sin
print(f"# {label}: {N}x{M} C={C} metric {metric}: a0 {a0:.6f} c_w {cw:.6f} c_x {cx:.6f} a0* {a0/cw:.4f} |rho_tau|inf {((r*w)[:,None]*sinf[None,:]*info['F']).abs().max().item():.3e}; "
      f"eigenvalues with Re > 1e-10: {(ev.real > 1e-10).sum().item()} of {len(ev)}; spectral radius {ev.abs().max().item():.3e}")
print("#  Re(lambda)    Im(lambda)   | frac of |rho_eig|^2 in r<=1  1-10   10-100  >100 | dominant k (share) | r of max | lambda/a0")
seen = set()
for i in range(len(ev)):
    if len(seen) >= top: break
    lam = ev[i]
    key = (round(lam.real.item(), 6), round(abs(lam.imag.item()), 6))
    if key in seen: continue
    seen.add(key)
    v = V[:, i]
    beta_eig = m.beta_full(v.real) + 1j * m.beta_full(v.imag)                                # complex (N+1, M)
    bk = (m.rad.sigR[:, None] ** m.kk[None, :]) * beta_eig                                   # mode values
    rho_eig = (r * w)[:, None] * (sinf[None, :] * (bk @ m.C_f.T.to(bk.dtype))) if metric == 'rho' else (bk @ m.C_f.T.to(bk.dtype))   # (N+1, M2) complex field (metric rho or b)
    p = rho_eig.abs() ** 2; tot = p.sum().item()
    fr = [p[(r > lo) & (r <= hi)].sum().item() / tot for lo, hi in [(0, 1), (1, 10), (10, 100), (100, 1e300)]]
    kpow = (bk.abs() ** 2 * ((r * w)[:, None] ** 2)).sum(0); kdom = kpow.argmax().item(); kshare = (kpow[kdom] / kpow.sum()).item()
    imax = p.sum(1).argmax().item()
    print(f"{lam.real.item():+12.4e} {lam.imag.item():+12.4e} | {fr[0]:.3f} {fr[1]:.3f} {fr[2]:.3f} {fr[3]:.3f} | k={kdom:2d} ({kshare:.2f}) | {r[imax].item():9.3e} | {lam.real.item()/a0:+.3f}")
# core-restricted summary: among eigenvalues with Re > 0, those with >= 50 percent of the norm in r <= 10
core = []
for i in range(len(ev)):
    if ev[i].real.item() <= 1e-10: break
    v = V[:, i]; beta_eig = m.beta_full(v.real) + 1j * m.beta_full(v.imag); bk = (m.rad.sigR[:, None] ** m.kk[None, :]) * beta_eig
    rho_eig = (r * w)[:, None] * (sinf[None, :] * (bk @ m.C_f.T.to(bk.dtype))) if metric == 'rho' else (bk @ m.C_f.T.to(bk.dtype)); p = rho_eig.abs() ** 2
    if p[r <= 10].sum().item() / p.sum().item() >= 0.5: core.append(ev[i].real.item())
print(f"# positive-Re eigenvalues with >= 50 percent of |rho_eig|^2 in r <= 10: {len(core)}; largest {max(core) if core else float('nan'):.4e} (= {max(core)/a0 if core else float('nan'):.3f} a0); RT bound a0 = {a0:.4f}")
