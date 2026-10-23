"""dr_vis_lift.py -- for the leading eigenpairs (lambda, w) of the compressed Jacobian J_vis = V^T J V (verifier 171): lift v = V w and report the FULL residual
r = J v - lambda v in the coefficient norm and in the field norm (density on the fine grid), relative to |lambda| |v|; also the localisation fractions in
two metrics: unweighted node sum of |rho_eig|^2 (as in dr_vis_modes.py) and the b-metric (relative density rho/(y w), unweighted nodes).
usage: python3 src/dr_vis_lift.py state.pt|const N M C [thr=1e-6 top=4]"""
import sys, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import dr, ipm3ql
torch.set_default_dtype(torch.float64)
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
src, N, M, C = args[0], int(args[1]), int(args[2]), float(args[3]); thr = float(kw.get('thr', 1e-6)); top = int(kw.get('top', 4)); dev = 'cuda'
m = dr.DR(N, M, C, device=dev, basis=kw.get('basis', 'local'))
if src == 'const':
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = 1.0; u = m.beta_to_u(beta0)
else:
    st = torch.load(src, weights_only=False); qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=1.0, gamma=1 / st['cl'], device=dev, Lf=st['Lf'])
    u = m.project(((qo.rad.sigR[:, None] ** qo.kk[None, :]) * st['beta'].to(dev)) @ m.C_f.T)
du, info = m.rhs(u, want=True); a0 = m.jets(u)[0].item()
J = m.jacobian_dr(u); Vs = []
for k in range(M):
    A = (m.rad.sigR[:, None] ** k) * m.Ext[k]; U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); keep = S_ >= thr * S_[0]
    Vk = torch.zeros(m.nu, int(keep.sum()), device=dev); Vk[m.offs[k]:m.offs[k + 1], :] = Vh_[keep].T; Vs.append(Vk)
V = torch.cat(Vs, 1); Jv = V.T @ J @ V; ev, W = torch.linalg.eig(Jv); order = torch.argsort(-ev.real)
r = m.rad.rR; w = m.rad.wR; sinf = m.angf.sin
def fields(vc):
    be = m.beta_full(vc.real) + 1j * m.beta_full(vc.imag); bk = (m.rad.sigR[:, None] ** m.kk[None, :]) * be
    b = bk @ m.C_f.T.to(bk.dtype); return b, (r * w)[:, None] * sinf[None, :] * b
Jc = J.to(torch.complex128)
print(f"# {src} {N}x{M} C={C} thr {thr:.0e}: a0 {a0:.5f}; compressed dim {V.shape[1]} of {m.nu}")
print("#  lambda                 | full residual |Jv - lambda v| / (|lambda||v|): coef   field(rho)   field(b) | fractions of |rho_eig|^2 (unweighted nodes) r<.1 .1-1 1-10 10-100 >100 | same in the b metric")
seen = set(); n = 0
for i in order.tolist():
    key = (round(ev[i].real.item(), 5), round(abs(ev[i].imag.item()), 5))
    if key in seen: continue
    seen.add(key); n += 1
    if n > top: break
    lam = ev[i]; v = V.to(torch.complex128) @ W[:, i]; res = Jc @ v - lam * v
    bv, fv = fields(v); br, fr = fields(res)
    rc = (res.norm() / (lam.abs() * v.norm())).item(); rf = (fr.abs().pow(2).sum().sqrt() / (lam.abs() * fv.abs().pow(2).sum().sqrt())).item(); rb = (br.abs().pow(2).sum().sqrt() / (lam.abs() * bv.abs().pow(2).sum().sqrt())).item()
    def fracs(f):
        p = f.abs() ** 2; tot = p.sum().item(); return [p[(r > lo) & (r <= hi)].sum().item() / tot for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e300)]]
    f1 = fracs(fv); f2 = fracs(bv)
    print(f"  {lam.real.item():+.4e} {lam.imag.item():+.4e}j | {rc:.2e}  {rf:.2e}  {rb:.2e} | " + ' '.join(f'{x:.3f}' for x in f1) + ' | ' + ' '.join(f'{x:.3f}' for x in f2))
