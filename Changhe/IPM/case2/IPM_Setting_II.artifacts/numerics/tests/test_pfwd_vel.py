"""Validation of code/pfwd.py: (1) finite-difference derivative; (2) canonical velocity against the Chebyshev collocation inverse
(code/ipm2polar.py, two-term tail) on the family-A density rho_a = x^2 (1 + a y/sqrt(1+r^2))^2 (1+r^2)^{-3/4} (p = 1/2), whose
central strain is exactly c = a (R5b benchmark); (3) node matrix from the ring fit: DV(0) = diag(c_l - c, c_l + c) = diag(0.5, 3.5)
for a = 1.5, c_l = 2; (4) the lead's steady state runs/pf_cos2_p05_deep.npz: node matrix (lead: diag(0.6085, 3.3915)) and
stationarity residual with my velocity."""
import sys, math, json, time; sys.path.insert(0, 'code')
import numpy as np, torch
from scipy.interpolate import CubicSpline
from pfwd import PFwd, fd_dlr
from ipm2polar import Disc
torch.set_default_dtype(torch.float64)
dev = 'cuda'
# (1) derivative test
lr = torch.linspace(-3, 2, 301, device=dev); d = float(lr[1] - lr[0])
F = torch.sin(1.7 * lr) * torch.exp(0.3 * lr); Fe = 1.7 * torch.cos(1.7 * lr) * torch.exp(0.3 * lr) + 0.3 * F
print("fd_dlr max error (301 pts, d=%.3f): %.2e" % (d, float((fd_dlr(F[:, None], d)[:, 0] - Fe).abs().max())))

a, p = 1.5, 0.5
def rho_a(x, y):
    r2 = x * x + y * y
    return x * x * (1 + a * y / torch.sqrt(1 + r2)) ** 2 * (1 + r2) ** ((p - 2) / 2)

for (Nr, Nth, lo, hi) in ((661, 256, -12.0, 10.0), (1321, 256, -12.0, 10.0), (661, 128, -12.0, 10.0)):
    S = PFwd(Nr, Nth, lo, hi, p, dev=dev)
    X = S.r[:, None] * S.cos[None, :]; Y = S.r[:, None] * S.sin[None, :]
    rho = rho_a(X, Y)
    t0 = time.time(); Wr, Wt, psi_m, Wr_m, Wt_m = S.velocity(rho, return_modes=True); torch.cuda.synchronize(); tv = time.time() - t0
    g = rho / S.r[:, None] ** p
    dg = S.diagnostics(g, Wr, Wt, krings=(8, 20, 40, 80))
    print("pfwd (Nr %d, Nth %d, lo %g, hi %g): velocity %.3fs; c_moment %.6f (tail %.2e), d_moment %.2e (exact c = %.1f, d = 0)" %
          (Nr, Nth, lo, hi, tv, dg['c_moment'], dg['c_moment_tail'], dg['d_moment'], a))
    for k in (8, 20, 40, 80):
        rr = dg['ring%d' % k]
        print("   ring r=%.2e: M=%s  m1=%.6f m2=%.6f e1=%.3f deg  (exact diag(%.1f, %.1f))" % (rr['r'], rr['M'], rr['m1'], rr['m2'], rr['e1_deg'], 1 / p - a, 1 / p + a))
    # Chebyshev inverse on the same density, R = 1000 and 3000, two-term tail with p = 0.5
    for (NrC, NthC, R) in ((64, 48, 1000.0), (80, 48, 3000.0)):
        dC = Disc(NrC, NthC, R, K=2, tail='power2', tail_alpha=p, device=dev)
        TH = dC.theta_p[:, None]; RR = dC.r[None, :]
        rhoC = rho_a(RR * torch.cos(TH), RR * torch.sin(TH))
        rho_m = dC.to_modes(rhoC); q = rho_m / dC.rk
        rho_m2, drho_m, tth_m = dC.rho_modes(q); f_m = dC.dx_modes(drho_m, tth_m)
        pp = dC.poisson(f_m, rho_m2, None); psiC, UrC, UtC = dC.velocity_modes(pp)
        # compare modes m = 0..5 on the Chebyshev radii inside [e^lo, min(R, e^hi)]
        rC = dC.r_np; msk = (rC > math.exp(lo) * 10) & (rC < min(R, math.exp(hi)) * 0.999)
        errs = []
        for mm in range(0, 6):
            for (mine, theirs, name) in ((Wr_m[mm], UrC[mm], 'Wr'), (Wt_m[mm], UtC[mm], 'Wt')):
                sp_re = CubicSpline(S.lr.cpu().numpy(), mine.real.cpu().numpy()); sp_im = CubicSpline(S.lr.cpu().numpy(), mine.imag.cpu().numpy())
                mine_at = sp_re(np.log(rC[msk])) + 1j * sp_im(np.log(rC[msk]))
                th_at = theirs.cpu().numpy()[msk]
                sc = np.abs(UrC[1].cpu().numpy()[msk]).max()
                errs.append((mm, name, float(np.abs(mine_at - th_at).max() / sc)))
        worst = max(e[2] for e in errs)
        print("   vs Chebyshev (Nr %d, Nth %d, R %g): max relative mode error over m<=5 (scale max|W_r,1|): %.2e; per mode: %s" %
              (NrC, NthC, R, worst, ' '.join('%d%s:%.1e' % e for e in errs)))
        # physical-space comparison: evaluate the Chebyshev modes at my (r, theta) grid points inside the box
        c_C = dC.taylor_psi(pp)
        print("   Chebyshev taylor psi:", {k: (round(float(v.real), 6) if torch.is_tensor(v) else v) for k, v in c_C.items()} if isinstance(c_C, dict) else c_C)

# (4) the lead's state
fn = 'runs/pf_cos2_p05_deep.npz'
dd = np.load(fn); g = torch.tensor(dd['g'], device=dev); lrL = dd['lr']; argsL = json.loads(str(dd['args']))
Nr, Nth = g.shape; S = PFwd(Nr, Nth, float(lrL[0]), float(lrL[-1]), argsL['p'], dev=dev)
dg = S.diagnostics(g, krings=(8, 20, 40, 80))
print("lead state %s (p=%g, %d x %d): c_moment %.5f (target %.5f), d_moment %.2e" % (fn.split('/')[-1], argsL['p'], Nr, Nth, dg['c_moment'], dg['c_target'], dg['d_moment']))
for k in (8, 20, 40, 80):
    rr = dg['ring%d' % k]; print("   ring r=%.2e: M=%s m1=%.5f m2=%.5f e1=%.2f" % (rr['r'], rr['M'], rr['m1'], rr['m2'], rr['e1_deg']))
print("   stationarity residual |V.grad rho - rho| / max_th|rho| by band:", dg['R_rel_bands'])
