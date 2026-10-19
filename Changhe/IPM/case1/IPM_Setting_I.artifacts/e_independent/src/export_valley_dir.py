"""Export the cheapest c_l direction as a perturbation field of the construct1 projection, for the verifier's own evaluator:
project construct1 onto (N, M), R, run a few LSQ iterations (state S0, near the candidate), compute v_cl = argmin |J v| s.t. dc_l . v = 1,
scale to dc_l = +1e-3, and export S0 and S0 +- delta (rho, psi, U, W, c_l) as plain arrays on my grid, plus my own between-node residual
bands for the three states. If the verifier's N_v / N_f residuals of S0 +- delta equal those of S0 while c_l differs by 1e-3 (and the
same with 1e-2), the discretised equations do not determine c_l at this residual level, independently of my solver.
Usage: python3 src/export_valley_dir.py N M R L [its] [ovs] [tag]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, ipm1lsq, charac
from scipy.interpolate import RegularGridInterpolator
dev = 'cuda'; base = ''
N, M, R, L = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
its = int(sys.argv[5]) if len(sys.argv) > 5 else 6; ovs = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0; tag = sys.argv[7] if len(sys.argv) > 7 else f'valley_N{N}M{M}R{int(R)}'
cand = np.load('final_candidate.npz', allow_pickle=True)
cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev); m.k_tail = 1 / cl
interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
ls = ipm1lsq.LSQ(m, Qr=int(round(ovs * N)), Qth=2 * M + 1, chunk=256, verbose=False)
cl0, c0, fl0 = ls.cl_of_b(b, cl); ls.set_weights(b, cl0)
b0, cl0, info = ls.solve(b, cl0, maxit=its, lam=1e-6, svd_at_end=False, rel_stop=1e-9)
F, E, q = ls.F(b0, cl0); J = ls.jacobian(b0, cl0, q); a = ls.dcl_db
Rf = torch.linalg.qr(J, mode='r')[1]; del J
y = torch.linalg.solve_triangular(Rf.T, a[:, None], upper=False)[:, 0]
v_cl = torch.linalg.solve_triangular(Rf, y[:, None], upper=True)[:, 0] / (y @ y); del Rf
cost = 1 / y.norm().item()
print(f"[valley] S0: c_l {cl0:.8f}, PDE rms {math.sqrt((F[:ls.Q]**2).mean().item()):.3e}; cheapest c_l cost {cost:.3e} per unit c_l; |v_cl| {v_cl.norm().item():.3e}", flush=True)
rq = ls.rq.cpu().numpy()
def bands(bb, cll):
    cll, _, fl = ls.cl_of_b(bb, cll); E_, q_ = ls.residual_q(bb, cll, fl); den = ls.denominators(bb, cll, q_); rel = (E_ / den)
    fe = charac.FieldEval(m, bb, cll); Pi = fe.find_P()
    out = {}
    for name, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items():
        mk = (rq > a_) & (rq <= b_); vv = rel[mk]; out[name] = (math.sqrt((vv ** 2).mean().item()), vv.abs().max().item())
    Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]; dP = torch.sqrt((Xq - Pi['x_star']) ** 2 + Yq ** 2); mk = dP < 2
    out['|X-P|<2'] = (math.sqrt((rel[mk] ** 2).mean().item()), rel[mk].abs().max().item())
    return cll, Pi, out, fl
def export(bb, cll, fl, name):
    rho = m.rho_from_b(bb); psi = m.psi(fl); U1, U2 = m.velocity(fl); r_ = m.rad.rR; th_ = m.ang.theta
    np.savez(base + f'runs/{name}.npz', r=r_.cpu().numpy(), theta=th_.cpu().numpy(), rho=rho.cpu().numpy(), a=(m.wR[:, None] * bb).cpu().numpy(), psi=psi.cpu().numpy(), U1=U1.cpu().numpy(), U2=U2.cpu().numpy(),
             W1=(cll*r_[:, None]*torch.cos(th_)[None, :] + U1).cpu().numpy(), W2=(cll*r_[:, None]*torch.sin(th_)[None, :] + U2).cpu().numpy(), c_l=cll, c=m.psi_xy0(fl).item(), R=R, N=N, M=M, L=L, gamma=m.gamma, k_tail=1/cll,
             note='disk closure (SPEC N3a); grid = Chebyshev-Radau radii x midpoint angles on (0, pi/2); rho = x^2 y a; see NUM_REPORT 3.16 and NOTES_FOR_LEAD 02:1xZ')
for eps in [1e-3, 1e-2]:
    for sgn in [+1, -1]:
        bb = b0.clone(); bb.reshape(-1)[M:] += sgn * eps * v_cl
        cll, Pi, out, fl = bands(bb, cl0)
        print(f"[valley] S0 {'+' if sgn>0 else '-'} {eps:g} v_cl: c_l {cll:.8f} (dc_l {cll-cl0:+.3e}), x* {Pi['x_star']:.5f}, h(P)-1 {Pi['h']-1:+.2e}; between-node |E|/den (rms, max): " + "; ".join(f"{k} {v[0]:.2e}/{v[1]:.2e}" for k, v in out.items()), flush=True)
        export(bb, cll, fl, f'fields_{tag}_{"p" if sgn>0 else "m"}{eps:g}')
cll, Pi, out, fl = bands(b0, cl0)
print(f"[valley] S0: c_l {cll:.8f}, x* {Pi['x_star']:.5f}, h(P)-1 {Pi['h']-1:+.2e}; between-node |E|/den (rms, max): " + "; ".join(f"{k} {v[0]:.2e}/{v[1]:.2e}" for k, v in out.items()), flush=True)
export(b0, cl0, fl, f'fields_{tag}_S0')
vb = torch.zeros(N + 1, M, device=dev); vb[1:] = v_cl.reshape(N, M)
np.savez(base + f'runs/{tag}_direction.npz', r=m.rad.rR.cpu().numpy(), theta=m.ang.theta_np, delta_b_per_unit_cl=vb.cpu().numpy(), delta_rho_per_unit_cl=(m.rho_from_b(vb)).cpu().numpy(), note='v_cl: min |J v| s.t. dc_l.v = 1; rho perturbation = x^2 y w delta_b; multiply by dc_l (e.g. 1e-3)')
print(f"[valley] exported runs/fields_{tag}_S0.npz, _p0.001, _m0.001, _p0.01, _m0.01 and runs/{tag}_direction.npz", flush=True)
