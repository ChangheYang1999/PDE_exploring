"""dr_vis_refine.py -- the compressed leading eigenvalue of the DR linearisation about ONE fixed background (the 64x16 stall state) transferred to other
discretisations (N, M, M2 varied independently), with the full-lift b-field residual: tests whether the ~0.73 a0 growth rate is a discretisation artifact
(referee dr1 item 15, first and second checks).  The transfer is through the field (regrid_fit on mode values, then projection), so the background is the
same density up to the transfer error (reported as the change of a0 and of the initial |rho_tau|).  usage: python3 src/dr_vis_refine.py state.pt C"""
import sys, torch, math
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import dr, ipm3ql, q_free
torch.set_default_dtype(torch.float64); dev = 'cuda'
src, C = sys.argv[1], float(sys.argv[2]); st = torch.load(src, weights_only=False)
qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=1.0, gamma=1 / st['cl'], device=dev, Lf=st['Lf']); beta_old = st['beta'].to(dev)
print(f"# background {src} ({st['N']}x{st['M']}); compressed Jacobian (thr 1e-6), velocity feedback on / off; lift residual in the b-field norm")
print("#  N    M    M2   a0        |rho_tau|0 (r<=1)   max Re (full)   /a0     lift res (b)   max Re (no feedback)   dim")
for (N, M, M2) in [(64, 16, 48), (64, 16, 96), (96, 16, 48), (128, 16, 48), (64, 24, 72), (64, 32, 96), (96, 24, 72), (128, 32, 96)]:
    m = dr.DR(N, M, C, device=dev, M2=M2, basis='local', rcond=1e-8)
    if (N, M) == (st['N'], st['M']):
        bk = (qo.rad.sigR[:, None] ** qo.kk[None, :]) * beta_old; u = m.project(bk @ m.C_f.T)
    else:
        beta_new, _ = q_free.regrid_fit(qo, beta_old, m); u = m.project(((m.rad.sigR[:, None] ** m.kk[None, :]) * beta_new) @ m.C_f.T)
    du, info = m.rhs(u, want=True); a0 = m.jets(u)[0].item(); r = m.rad.rR; w = m.rad.wR
    rt = ((r * w)[:, None] * m.angf.sin[None, :] * info['Fp']).abs(); rt1 = rt[r <= 1].max().item()
    Vs = []
    for k in range(M):
        A = (m.rad.sigR[:, None] ** k) * m.Ext[k]; U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); keep = S_ >= 1e-6 * S_[0]
        Vk = torch.zeros(m.nu, int(keep.sum()), device=dev); Vk[m.offs[k]:m.offs[k + 1], :] = Vh_[keep].T; Vs.append(Vk)
    V = torch.cat(Vs, 1)
    out = []
    for fb in [True, False]:
        J = m.jacobian_dr(u, feedback=fb); Jv = V.T @ J @ V; ev, W = torch.linalg.eig(Jv); i = torch.argmax(ev.real); lam = ev[i]
        if fb:
            v = V.to(torch.complex128) @ W[:, i]; res = J.to(torch.complex128) @ v - lam * v
            def bfield(x):
                be = m.beta_full(x.real) + 1j * m.beta_full(x.imag); return ((m.rad.sigR[:, None] ** m.kk[None, :]) * be) @ m.C_f.T.to(torch.complex128)
            rb = (bfield(res).abs().pow(2).sum().sqrt() / (lam.abs() * bfield(v).abs().pow(2).sum().sqrt())).item()
            out += [lam.real.item(), rb]
        else:
            out += [lam.real.item()]
    print(f"  {N:3d}  {M:3d}  {M2:4d}  {a0:.5f}  {rt1:.3e}          {out[0]:+.4f}        {out[0]/a0:.3f}   {out[1]:.3f}          {out[2]:+.4f}               {V.shape[1]}", flush=True)
