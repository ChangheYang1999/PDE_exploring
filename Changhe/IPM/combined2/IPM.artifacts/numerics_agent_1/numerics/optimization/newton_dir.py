"""newton_dir.py (lane numerics_agent_1): the Galerkin least-squares correction h_N of a candidate in its own basis (coordinator 2026-11-02T19:26Z item 4a).
delta = argmin ||F + J delta||_2 over the coefficient directions in the null space of the exact linear rows (421 rows; option --taylor adds the
linearized five Taylor rows), computed from the normal equations with an eigenvalue cutoff (several cutoffs reported: the undamped limit is
the smallest cutoff).  h_N = rho[delta] (the density perturbation), U[h_N] = (-psi_y[delta], psi_x[delta]).
Exact quadratic structure: F(a + t delta) = F0 + t J delta + t^2 Q(delta), so F0 + J delta = F0 + (F(a+delta) - F(a-delta))/2 exactly.
Reported (FLOAT, mesh radial Gauss MID/panel x midpoint ANG, 0.02 <= r <= R): ||F + J delta||_2 (linearized residual), ||F(a + delta)||_2 (full
nonlinear residual after the step), ||h_N||_2, ||grad h_N||_inf, ||DU[h_N]||_(inf,op) (pointwise operator norm), sup <X>^sigma |grad h_N| at sigma
= 1 and 7/5, and the BG-q matrix value lambda_max(q Sym D(V + U[h_N]) + K - (c + 1 + a_W) I) with K = [[-rho_y, rho_x/2],[rho_x/2, 0]] from the
background and a_W = sigma (V + U[h_N]).X/(r0^2 + |X|^2) (theory_agent_1 screen_bgq.py convention), at the tuples (q, sigma, r0) given.
argv: cand.json out.json [ANG=180] [MID=16] [R=1e4] [--taylor] [--cutoffs 1e-6,1e-8,1e-10,1e-12]"""
import sys, os, json, time, math, argparse
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_optn1 as ON1
ap = argparse.ArgumentParser(); ap.add_argument('cand'); ap.add_argument('out'); ap.add_argument('--ang', type=int, default=180); ap.add_argument('--mid', type=int, default=16)
ap.add_argument('--R', type=float, default=1e4); ap.add_argument('--taylor', action='store_true'); ap.add_argument('--cutoffs', default='1e-4,1e-6,1e-8,1e-10,1e-12,1e-14')
ap.add_argument('--tuples', default='2.6,1.4,0.25;2.4,1.0,0.25;2.5,1.4,0.5;2.5,1.4,0.25'); ap.add_argument('--device', default=os.environ.get('IPM_DEVICE', 'cuda'))
args = ap.parse_args(); dev = torch.device(args.device); t00 = time.time()
J131, c131, terms131 = load131()
c, gens, coefs_q, J = OPT.load_candidate_json(args.cand); cf = X.qfloat(c); a = np.array([X.qfloat(v) for v in coefs_q]); JMAX = max(int(g['j']) for g in gens if 'j' in g)
mesh = build_mesh(args.mid, args.ang, 0.02, args.R, dev)
prob = ON1.ProblemN1(gens, c, mesh, r_cut=0.02, r_max=args.R, wF=1.0)
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=(0, 1, 2), branch_targets=stationary_targets(JMAX))
A, b = prob.constraint_matrix(); print('rows', len(prob.lin_rows), 'viol', np.abs(A@a-b).max(), 'build', time.time()-t00, flush=True)
if args.taylor:
    Jt = prob.taylor_jacobian(a)[1:]; A = np.vstack([A, Jt])
At = torch.as_tensor(A, dtype=torch.float64, device=dev)
U_, S_, Vh = torch.linalg.svd(At, full_matrices=True); rank = int((S_ > S_.max()*1e-13).sum()); Z = Vh[rank:].T
G, g, phi0 = prob.normal_equations(a)
GZ = Z.T@(G@Z); gZ = Z.T@g
colnorm = torch.sqrt(torch.diagonal(GZ).clamp(min=0)); colnorm[colnorm == 0] = 1
GZs = GZ/colnorm[:, None]/colnorm[None, :]; gZs = gZ/colnorm
evals, evecs = torch.linalg.eigh(GZs); emax = float(evals.max())
print('reduced dimension', GZ.shape[0], 'eigenvalues of the column-scaled normal matrix: max %.3e, min %.3e, #<1e-12*max %d' % (emax, float(evals.min()), int((evals < 1e-12*emax).sum())), flush=True)
base = prob.base; r = mesh.r[:, None]; sn = mesh.sin[None, :]; cs = mesh.cos[None, :]; Xw = torch.sqrt(1+r**2)*torch.ones_like(base)
F0 = prob.F_components(prob.fields(a))[(0, 0)]; G0 = math.sqrt(float(torch.sum(base*F0**2)))
Fd_bg = prob.fields(a); Pb = lambda i, j: Fd_bg[('psi', (i, j))]; Rb = lambda i, j: Fd_bg[('rho', (i, j))]
def l2(f): return math.sqrt(float(torch.sum(base*f**2)))
def opnorm2x2(a11, a12, a21, a22):
    S = a11**2+a12**2+a21**2+a22**2; D = a11*a22-a12*a21
    return torch.sqrt((S+torch.sqrt((S*S-4*D*D).clamp(min=0)))/2)
tuples = [tuple(float(x) for x in t.split(',')) for t in args.tuples.split(';')]
def bgq(Fd_d, q, sig, r0):
    """lambda_max of q Sym D(V + U[h]) + K - (c + 1 + a_W) I over the mesh; Fd_d = fields of the perturbation (None for the background alone)"""
    # D u_bar entries: u = (-psi_y, psi_x): u1x = -psi_xy, u1y = -psi_yy, u2x = psi_xx, u2y = psi_xy
    u1x, u1y, u2x, u2y = -Pb(1, 1), -Pb(0, 2), Pb(2, 0), Pb(1, 1); u1, u2 = -Pb(0, 1), Pb(1, 0)
    if Fd_d is not None:
        Pd = lambda i, j: Fd_d[('psi', (i, j))]
        u1x = u1x-Pd(1, 1); u1y = u1y-Pd(0, 2); u2x = u2x+Pd(2, 0); u2y = u2y+Pd(1, 1); u1 = u1-Pd(0, 1); u2 = u2+Pd(1, 0)
    s11 = cf+u1x; s22 = cf+u2y; s12 = 0.5*(u1y+u2x)
    k11 = -Rb(0, 1); k12 = 0.5*Rb(1, 0)
    e = cf+(u1*cs+u2*sn)/r                        # (V+U).X/|X|^2
    aW = sig*e*r**2/(r0**2+r**2)
    a11 = q*s11+k11-(cf+1+aW); a22 = q*s22-(cf+1+aW); a12 = q*s12+k12
    lam = 0.5*(a11+a22)+torch.sqrt((0.5*(a11-a22))**2+a12**2)
    idx = int(torch.argmax(lam)); i, jj = divmod(idx, mesh.Nt)
    return {'lambda_max': float(lam.max()), 'beta': -float(lam.max()), 'at_r': float(mesh.r[i]), 'at_theta': float(mesh.theta[jj])}
res = {'candidate': os.path.basename(args.cand), 'sha256': sha256_file(args.cand), 'rule': f'radial Gauss {args.mid}/panel x midpoint {args.ang}, 0.02 <= r <= {args.R:g}', 'rows': len(prob.lin_rows), 'taylor_rows_linearized': args.taylor,
       'G0_mesh': G0, 'reduced_dim': int(GZ.shape[0]), 'eig_max': emax, 'eig_min': float(evals.min()), 'background_bgq': {f'q{q}_s{s}_r0{r0}': bgq(None, q, s, r0) for q, s, r0 in tuples}, 'cutoffs': [], 'label': 'FLOAT', 'note': 'coordinator 19:26Z item 4a; nothing here is a bound'}
print('background BG-q:', json.dumps(res['background_bgq']), flush=True)
for cut in [float(x) for x in args.cutoffs.split(',')]:
    keep = evals > cut*emax
    eta = -(evecs[:, keep]@((evecs[:, keep].T@gZs)/evals[keep]))
    delta = (Z@(eta/colnorm)).cpu().numpy()
    Fp = prob.F_components(prob.fields(a+delta))[(0, 0)]; Fm = prob.F_components(prob.fields(a-delta))[(0, 0)]
    Flin = F0+(Fp-Fm)/2
    Fd_d = prob.fields(delta); h = Fd_d[('rho', (0, 0))]; hx, hy = Fd_d[('rho', (1, 0))], Fd_d[('rho', (0, 1))]; gh = torch.sqrt(hx**2+hy**2)
    Pd = lambda i, j: Fd_d[('psi', (i, j))]
    DUop = opnorm2x2(-Pd(1, 1), -Pd(0, 2), Pd(2, 0), Pd(1, 1))
    symDUop = opnorm2x2(-Pd(1, 1), 0.5*(-Pd(0, 2)+Pd(2, 0)), 0.5*(-Pd(0, 2)+Pd(2, 0)), Pd(1, 1))      # Sym DU[h] = [[-psi_xy, (psi_xx - psi_yy)/2], [., psi_xy]]
    row = {'cutoff_rel': cut, 'n_kept': int(keep.sum()), 'lin_residual_L2': l2(Flin), 'nonlinear_residual_L2': l2(Fp), 'coef_norm': float(np.linalg.norm(delta)),
           'hN_L2': l2(h), 'grad_hN_inf': float(gh.max()), 'DU_hN_op_inf': float(DUop.max()), 'sup_X1_grad_hN': float((Xw*gh).max()), 'sup_X1p4_grad_hN': float((Xw**1.4*gh).max()),
           'hN_inf': float(h.abs().max()), 'U_hN_inf': float(torch.sqrt(Pd(0, 1)**2+Pd(1, 0)**2).max()), 'ratio_lin_res_over_beta0_2': l2(Flin)/2.0,
           'SymDU_hN_op_inf': float(symDUop.max()), 'A_hN': float(h.abs().max())+float(gh.max()), 'operator': 'A_k = L + U[k].grad at k = h_N (BG-5 matrix of theory_v01 / AT-039)',
           'bgq_corrected': {f'q{q}_s{s}_r0{r0}': bgq(Fd_d, q, s, r0) for q, s, r0 in tuples}}
    res['cutoffs'].append(row)
    print(json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in row.items() if k != 'bgq_corrected'}), flush=True)
    print('   BG-q corrected:', json.dumps({k: round(v['beta'], 5) for k, v in row['bgq_corrected'].items()}), flush=True)
res['total_s'] = time.time()-t00
json.dump(res, open(args.out, 'w'), indent=1); print('written', args.out, flush=True)
