"""Identity-preserving homotopy with pseudo-arclength, dealiased code, logging smin(J) and sign(det J) (lead request 19:09Z item 5)."""
import sys, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; base = ''
for cl0, tag in [(2.0, 'arc2_cl2'), (3.0, 'arc2_cl3')]:
    m = ipm1.IPM1(N=48, M=10, L=1.0, gamma=1 / cl0, device=dev); nw = solve.Newton(m, verbose=False)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
    c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
    b0 = one + (3 * cl0 - 1 - c1) / cs * s2; b0[0, :] = 1.0
    F0, fl0 = nw.residual_full(b0, cl0); E0 = m.residual(b0, cl0, fl0); S0 = E0.clone(); S0[0, :] = 0
    log = open(base + f'runs/{tag}.dat', 'w'); log.write("# eps cl max|b| b(inf)max smin ds tau_eps sign_detJ\n")
    out, (b, cl, eps) = solve.arclength(nw, b0, cl0, 0.0, S0, 0.0, ds=0.05, nsteps=250, amp_stop=1e5, log=log, verbose=False)
    emax = max(o[0] for o in out)
    print(f"{tag}: eps_max = {emax:.5f}, steps {len(out)}, final eps {eps:.4f} c_l {cl:.5f}", flush=True)
