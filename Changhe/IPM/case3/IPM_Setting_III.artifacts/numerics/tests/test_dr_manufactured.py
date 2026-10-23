"""Exact manufactured test of the DR right-hand side (verifier result 151 field): psi = -xy/[4(1+r^2)], rho = y (r^2+2)/[2(1+r^2)^2],
a = 1, c = -1/4; at target C = 3: c_w = 1/8, c_x = 3/8, a_tau = 0, b_tau (x^2 y) = 9/8, e_tau (y^3) = 1/8; rho_tau(1/7, 4/21) = 110374593/23578364168.
Compares the discrete DR right-hand side (dr.py, LS and square projections) with the exact rho_tau at off-grid points, checks the mass-map
round trip and the analytic Jacobian against finite differences."""
import sys, math, time, numpy as np, torch, sympy as sp
sys.path.insert(0, 'numerics/src'); import dr
torch.set_default_dtype(torch.float64)
dev = sys.argv[1] if len(sys.argv) > 1 else 'cuda'
# ---- exact ----
x, y = sp.symbols('x y', real=True); s = x**2 + y**2
psi = -x*y/(4*(1+s)); rho = y*(s+2)/(2*(1+s)**2)
U1, U2 = -sp.diff(psi, y), sp.diff(psi, x)
assert sp.simplify(-sp.diff(psi, x, 2) - sp.diff(psi, y, 2) - sp.diff(rho, x)) == 0
C = sp.Integer(3); c = sp.Rational(-1, 4); cw = -c/(C-1); cx = C*cw
rho_tau = sp.simplify(cw*rho - (cx*x + U1)*sp.diff(rho, x) - (cx*y + U2)*sp.diff(rho, y))
v = rho_tau.subs({x: sp.Rational(1, 7), y: sp.Rational(4, 21)}); print('exact rho_tau(1/7,4/21) =', v, '(verifier: 110374593/23578364168)', v == sp.Rational(110374593, 23578364168))
ser = sp.series(sp.series(rho_tau, x, 0, 4).removeO(), y, 0, 4).removeO(); poly = sp.Poly(sp.expand(ser), x, y)
print('exact Taylor of rho_tau: y:', poly.coeff_monomial(y), ' x^2y:', poly.coeff_monomial(x**2*y), ' y^3:', poly.coeff_monomial(y**3))
f_rt = sp.lambdify((x, y), rho_tau, 'numpy'); f_rho = sp.lambdify((x, y), rho, 'numpy')
pts_r = np.array([0.01, 0.05, 0.1, 0.3, 0.7, 1.0, 1.5, 2.3, 4.0, 7.0, 15.0, 40.0]); pts_th = np.array([0.15, 0.6, 1.0, 1.4])
RR, TT = np.meshgrid(pts_r, pts_th, indexing='ij'); XX, YY = RR*np.cos(TT), RR*np.sin(TT)
exact = f_rt(XX, YY); exact_rho = f_rho(XX, YY)
for proj in ['ls', 'sq']:
    for (N, M) in [(32, 8), (48, 12), (64, 16)]:
        m = dr.DR(N, M, 3.0, L=1.0, device=dev, proj=proj)
        r = m.rad.rR; w = m.rad.wR
        h = (r**2 + 2)/(2*(1 + r**2)**2)                 # rho/y
        beta0 = torch.zeros(N+1, M, device=dev); beta0[:, 0] = h/w
        u = m.beta_to_u(beta0)                            # exact interpolation of beta_0 at all nodes (mode 0 uses all N+1 nodes)
        du, info = m.rhs(u, want=True)
        c_d = info['c'].item(); cw_d = info['cw'].item(); cx_d = info['cx'].item()
        ev = m.evaluate(info['beta'], cx_d, info['flds'], RR, TT)
        rt_d = (cw_d - 1) * ev['rho'] - ev['R']           # rho_tau = c_w rho - [(c_x X + U).grad rho] = (c_w - 1) rho - R_{c_x}
        err = np.abs(rt_d - exact).max(); errrho = np.abs(ev['rho'] - exact_rho).max()
        # centre jets of the coefficient derivative: rho_tau = y [a' + b' x^2 + e' y^2 + ...]
        a_t, b_t, e_t = [z.item() for z in m.jets(du)]
        # via the projected field: compare du (coefficients) with the field F at nodes
        beta_t = m.beta_full(du); Fk = (info['F'] @ m.Af.T)                  # mode coefficients of the field derivative
        bk_t = (m.rad.sigR[:, None] ** m.kk[None, :]) * beta_t                 # mode values of the projected derivative
        projerr = (bk_t - Fk).abs().max().item()
        print(f"{proj} {N}x{M}: c {c_d:+.12f} cw {cw_d:.12f} cx {cx_d:.12f} | max|rho_d - rho| {errrho:.1e} | max|rho_tau_d - exact| {err:.2e} (max|exact| {np.abs(exact).max():.2e}) "
              f"| jets of rho_tau: a' {a_t:+.3e} b' {b_t:.10f} (9/8) e' {e_t:.10f} (1/8) | projection defect at nodes {projerr:.1e}", flush=True)
# mass-map round trip: random coefficients -> field -> coefficients
m = dr.DR(48, 12, 3.0, L=1.0, device=dev, proj='ls'); torch.manual_seed(0)
u0 = torch.randn(m.nu, device=dev); beta = m.beta_full(u0); bkv = (m.rad.sigR[:, None] ** m.kk[None, :]) * beta            # mode values
Ffine = bkv @ m.C_f.T                                                                                                      # field on the fine grid
u1 = m.project(Ffine); print('mass-map round trip (ls, 48x12): max|u1 - u0| =', (u1 - u0).abs().max().item(), ' (invisible directions excluded by the cutoff would show here)')
m2 = dr.DR(48, 12, 3.0, L=1.0, device=dev, proj='sq'); u2 = m2.project(Ffine); print('mass-map round trip (sq, 48x12): max|u2 - u0| =', (u2 - u0).abs().max().item())
# Jacobian: analytic vs finite differences at 32x8 on the manufactured state
m = dr.DR(32, 8, 3.0, L=1.0, device=dev, proj='ls'); r = m.rad.rR; w = m.rad.wR; h = (r**2 + 2)/(2*(1 + r**2)**2)
beta0 = torch.zeros(33, 8, device=dev); beta0[:, 0] = h/w; u = m.beta_to_u(beta0)
t0 = time.time(); Ja = m.jacobian_dr(u); ta = time.time() - t0; t0 = time.time(); Jf = m.jacobian_fd(u, h=1e-6); tf = time.time() - t0
print(f"Jacobian 32x8: max|Ja - Jf| = {(Ja - Jf).abs().max().item():.2e}, max|Ja| = {Ja.abs().max().item():.2e} (analytic {ta:.1f}s, FD {tf:.1f}s)")
ev = torch.linalg.eigvals(Ja); print(f"spectrum at the manufactured state 32x8: radius {ev.abs().max().item():.3e}, max Re {ev.real.max().item():+.3e}, #Re>0 {(ev.real>1e-10).sum().item()}")
