import sys, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; N, M, L = 48, 10, 1.0; cl = 2.0; gamma = 1/cl
m = ipm1.IPM1(N=N, M=M, L=L, gamma=gamma, device=dev); nw = solve.Newton(m, verbose=False)
r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
s2 = r**2/(L**2+r**2) + 0*th; one = torch.ones_like(s2)
c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item(); A = (3*cl-1-c1)/cs
b0 = one + A*s2
F, fl = nw.residual_full(b0, cl); J = nw.jacobian(b0, cl, fl)
U, S, Vh = torch.linalg.svd(J)
print("smallest singular values:", S[-6:].cpu().numpy())
rr = m.rad.rR.cpu().numpy(); thh = m.ang.theta_np
for k in range(1, 4):
    v = Vh[-k, :-1].reshape(N+1, M).cpu().numpy(); dcl = Vh[-k, -1].item()
    u = U[:-1, -k].reshape(N+1, M).cpu().numpy()
    i, j = np.unravel_index(np.argmax(np.abs(v)), v.shape)
    iu, ju = np.unravel_index(np.argmax(np.abs(u)), u.shape)
    # energy distribution of v over radial zones and angular rows
    rad_prof = (v**2).sum(1); ang_prof = (v**2).sum(0)
    print(f"right sing. vec {k}: sigma={S[-k].item():.3e}, d c_l component={dcl:+.3e}; peak at r={rr[i]:.4g}, theta={thh[j]:.3f}; radial energy: r<0.1 {rad_prof[rr<0.1].sum():.2f}, 0.1-1 {rad_prof[(rr>=0.1)&(rr<1)].sum():.2f}, 1-10 {rad_prof[(rr>=1)&(rr<10)].sum():.2f}, >10 {rad_prof[rr>=10].sum():.2f}; angular energy {np.array2string(ang_prof, precision=2)}")
    print(f"   left sing. vec {k}: peak residual row at r={rr[iu]:.4g}, theta={thh[ju]:.3f}; radial energy: r<0.1 {(u**2).sum(1)[rr<0.1].sum():.2f}, 0.1-1 {(u**2).sum(1)[(rr>=0.1)&(rr<1)].sum():.2f}, 1-10 {(u**2).sum(1)[(rr>=1)&(rr<10)].sum():.2f}, >10 {(u**2).sum(1)[rr>=10].sum():.2f}")
