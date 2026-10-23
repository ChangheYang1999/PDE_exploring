"""dr_transient.py -- optimal TRANSIENT growth of the core norm under the linearised DR flow about a state, with the far-end pseudo-modes removed:
J = V Lambda V^-1 (analytic DR Jacobian); eigenvectors with >= 50 percent of |rho_eig|^2 at r > R_far are 'far-end' and excluded; on the invariant subspace
S of the others, G(tau) = max_{du in S} ||field(e^{J tau} du)||_core / ||field(du)||_core = sigma_max(B_core V_s e^{Lambda_s tau} (B_core V_s)^+) with
B_core the coefficient -> density map on the fine grid restricted to r <= R_core.  Also the structure of the optimal initial perturbation (dominant angular
mode, radius of maximum) and of its image.  If G(tau) ~ e^{a0 tau} the Rayleigh-Taylor transient reading holds; if G stays O(1) the nonlinear explosion from
the chain states is the far-end artifact.  usage: python3 src/dr_transient.py state.pt|const N M C [Rcore=1 Rfar=100 taus=0.1,0.2,...]"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import dr
torch.set_default_dtype(torch.float64)
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
src, N, M, C = args[0], int(args[1]), int(args[2]), float(args[3]); dev = 'cuda'
Rcore = float(kw.get('Rcore', 1.0)); Rfar = float(kw.get('Rfar', 100.0)); metric = kw.get('metric', 'b'); taus = [float(x) for x in kw.get('taus', '0.05,0.1,0.15,0.2,0.3,0.4,0.5,0.75,1.0').split(',')]
m = dr.DR(N, M, C, device=dev)
if src == 'const':
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = 1.0; u = m.beta_to_u(beta0)
else:
    st = torch.load(src, weights_only=False); u = st['u'].to(dev)
du, info = m.rhs(u, want=True); a0 = m.jets(u)[0].item(); cw = info['cw'].item(); cx = info['cx'].item()
J = m.jacobian_dr(u); ev, V = torch.linalg.eig(J)
r = m.rad.rR; w = m.rad.wR; sinf = m.angf.sin; th = m.angf.theta
# coefficient -> density map on the fine grid: rho = (r w) sin th sum_k sigma^k (Ext_k c_k) cos 2k th
cols = []
for k in range(M):
    Ek = (m.rad.sigR[:, None] ** k) * m.Ext[k]                                                   # (N+1, nk)
    cols.append(((r * w)[:, None, None] * Ek[:, :, None]) * (sinf[:, None] * torch.cos(2 * k * th)[:, None]).T[None, None, :].permute(0, 1, 2)[..., :].reshape(N + 1, -1, m.M2).permute(0, 2, 1) if False else None)
# simpler: build B by applying the field map to unit vectors in batches
B = torch.zeros((N + 1) * m.M2, m.nu, device=dev)
for k0 in range(0, m.nu, 512):
    k1 = min(m.nu, k0 + 512); I = torch.zeros(k1 - k0, m.nu, device=dev); I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
    bk = (m.rad.sigR[None, :, None] ** m.kk[None, None, :]) * m.beta_full(I); f = (bk @ m.C_f.T) if metric == 'b' else (r * w)[None, :, None] * sinf[None, None, :] * (bk @ m.C_f.T)
    B[:, k0:k1] = f.reshape(k1 - k0, -1).T
core_mask = (r <= Rcore)[:, None].expand(N + 1, m.M2).reshape(-1); far_mask = (r > Rfar)[:, None].expand(N + 1, m.M2).reshape(-1)
Bc = B.to(torch.complex128)
F = Bc @ V                                                                                   # fields of the eigenvectors (complex)
p = F.abs() ** 2; frac_far = p[far_mask].sum(0) / p.sum(0); frac_core = p[core_mask].sum(0) / p.sum(0)
keep = frac_far < 0.5
mx = lambda t: t.max().item() if t.numel() else float('nan')
print(f"# {src} {N}x{M} C={C}: a0 {a0:.5f} c_w {cw:.5f} c_x {cx:.5f}; metric {metric}; eigenvectors: {len(ev)} total, {int((~keep).sum())} far-end (>= 50 percent of the squared field at r > {Rfar}) removed, "
      f"{int(keep.sum())} kept; kept with Re > 0: {int((ev.real[keep] > 1e-10).sum())}, max Re among kept {mx(ev.real[keep]):+.4e}, max Re removed {mx(ev.real[~keep]):+.4e}")
# distribution of far-end fraction
import numpy as _np; h = _np.histogram(frac_far.cpu().numpy(), bins=[0, 0.01, 0.1, 0.5, 0.9, 0.99, 1.0001])[0]; print('# histogram of far-end fraction [0-.01,.01-.1,.1-.5,.5-.9,.9-.99,.99-1]:', h.tolist())
pos = ev.real > 1e-10; print(f"# positive-Re eigenvalues: {int(pos.sum())}; of these with far-end fraction < 0.5: {int((pos & keep).sum())}; with core fraction (r <= {Rcore}) >= 0.5: {int((pos & (frac_core >= 0.5)).sum())}")
Vs = V[:, keep]; Ls = ev[keep]
Bcore = Bc[core_mask]                                                                          # core field rows
A0 = Bcore @ Vs                                                                                # (ncore, ns): core fields of the kept eigenvectors
U_, S_, Vh_ = torch.linalg.svd(A0, full_matrices=False); keep2 = S_ > 1e-10 * S_[0]
A0p = Vh_[keep2].conj().T @ ((1.0 / S_[keep2])[:, None] * U_[:, keep2].conj().T)              # pseudo-inverse (ns, ncore)
print(f"# core map rank {int(keep2.sum())} of {Vs.shape[1]}; RT bound a0 = {a0:.4f} (rate), c_x = {cx:.4f} (advection)")
print("#   tau     G_core(tau)   ln G/tau   | optimal initial perturbation: dominant k, r of max, theta/(pi/2) | image: dominant k, r of max")
def describe(coef_field):
    f = coef_field.reshape(N + 1, m.M2); pp = f.abs() ** 2; idx = torch.argmax(pp); i, j = idx.item() // m.M2, idx.item() % m.M2
    ak = (f @ m.angf.A['EE'].T.to(f.dtype)).abs().pow(2).sum(0); kd = ak.argmax().item()
    return kd, r[i].item(), th[j].item() / (math.pi / 2)
for tau in taus:
    Et = torch.exp(Ls * tau)
    G = Bcore @ (Vs * Et[None, :]) @ A0p                                                      # core -> core propagator on S
    Ug, Sg, Vhg = torch.linalg.svd(G, full_matrices=False)
    g = Sg[0].item(); vin = Vhg[0].conj(); vout = Ug[:, 0]
    # embed the core-only optimal input into full field for description: input field on core rows only
    fin = torch.zeros((N + 1) * m.M2, dtype=torch.complex128, device=dev); fin[core_mask] = vin
    fout = torch.zeros_like(fin); fout[core_mask] = vout
    ki, ri, ti = describe(fin); ko, ro, to = describe(fout)
    print(f"  {tau:5.2f}  {g:12.4e}  {math.log(g)/tau:+8.3f}   | k={ki:2d} r={ri:9.3e} th={ti:.2f} | k={ko:2d} r={ro:9.3e}", flush=True)
