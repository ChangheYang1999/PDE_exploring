"""eval_candidate.py (lane numerics_agent_1): FLOAT diagnostics of an exact candidate JSON on the product mesh (GPU), with the exact far-field sector
table and exact-formula far parts beyond R.  Everything here is FLOAT (float64 quadrature on the stated rule); nothing is a bound.
Reported: G0 = ||F||_2 (inner + far), rF, G1, P2, sup|F| (mesh), dyadic profile of ||F||_2^2, a0 (FLOAT from the exact Taylor jets), the
(B-L2) screening quantities theta and kappa_inner (c1-n1 diag2 formulas), and the background screening quantities of the new framework
(prompt R9, R10): sup |u|/|X|, sup |Du|, sup |D^2 u|, sup |grad rho|, sup |D^2 rho|, sup |D^3 rho|, their <X>^gamma-weighted suprema with
gamma = 1 - 1/c_l, the flow coefficient nu = inf (V.X)/|X|^2 with V = c X + u, and <X>^sigma-weighted grid suprema of F, grad F, D^2 F (sigma = 7/4).
argv: candidate_json out_json [ANG=180] [MID=32] [R=8356.474846731926] [sigma=1.75]"""
import sys, os, json, time, math, hashlib
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_optn1 as ON1
path = sys.argv[1]; outp = sys.argv[2]; ANG = int(sys.argv[3]) if len(sys.argv) > 3 else 180; MID = int(sys.argv[4]) if len(sys.argv) > 4 else 32
R = float(sys.argv[5]) if len(sys.argv) > 5 else 8356.474846731926; SIG = float(sys.argv[6]) if len(sys.argv) > 6 else 1.75
dev = torch.device(os.environ.get('IPM_DEVICE', 'cuda'))
t00 = time.time()
c, gens, coefs_q, J = OPT.load_candidate_json(path); coefs = np.array([X.qfloat(v) for v in coefs_q]); cf = X.qfloat(c); gamma = 1-1/cf
mesh = build_mesh(MID, ANG, 0.02, R, dev)
t0 = time.time(); prob = ON1.ProblemN1(gens, c, mesh, r_cut=0.02, r_max=R, wF=1.0); tb = time.time()-t0
Fd = prob.fields(coefs); comp = prob.F_components(Fd, ON1.DERIVS)
r = mesh.r[:, None]; sn = mesh.sin[None, :]; cs = mesh.cos[None, :]; base = prob.base; om2 = (1+4*r**2)**0.8
F = comp[(0, 0)]; Fx, Fy = comp[(1, 0)], comp[(0, 1)]; Fxx, Fxy, Fyy = comp[(2, 0)], comp[(1, 1)], comp[(0, 2)]
dens = {'F2': base*F**2, 'rF2': base*r**2*F**2, 'G12': base*(Fx**2+Fy**2), 'P22': base*om2*(Fxx**2+2*Fxy**2+Fyy**2)}
rr = mesh.r.cpu().numpy(); annuli = []
for j in range(-5, 15):
    sel = torch.as_tensor((rr < 2.0**-4) if j == -5 else ((rr >= 2.0**j) & (rr < 2.0**(j+1))), device=dev)
    if not bool(sel.any()): continue
    annuli.append({'j': j, 'range': [0 if j == -5 else 2.0**j, 2.0**(j+1)], 'L2': math.sqrt(float(dens['F2'][sel].sum())), 'rF': math.sqrt(float(dens['rF2'][sel].sum())),
                   'gradF': math.sqrt(float(dens['G12'][sel].sum())), 'omD2F': math.sqrt(float(dens['P22'][sel].sum())), 'supF': float(F[sel].abs().max())})
terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs_q)])
t0 = time.time(); E, dsec, ssec, mom = X.residual_sectors(c, terms, 3, exp_min=X.mpq(-6)); tsec = time.time()-t0
far = FP.far_parts(E, R); F2_far = float(far[0]) if far[0] != float('inf') else None; rF2_far = float(far[1]) if far[1] != float('inf') else None
G0_in = math.sqrt(float(dens['F2'].sum())); G0 = math.sqrt(G0_in**2+(F2_far or 0)); rF = math.sqrt(float(dens['rF2'].sum())+(rF2_far or 0))
G1 = math.sqrt(float(dens['G12'].sum())); P2 = math.sqrt(float(dens['P22'].sum()))
rows = []
for ex in sorted(E.keys(), reverse=True):
    S = E[ex]
    if ex < 1/c-10*(1-1/c): continue
    rows.append({'exponent': X.qfloat(ex), 'exponent_exact': X.qstr(ex), 'zero': not S, 'quarter_L2': X.quarter_norm(S), 'full_L2': 2*X.quarter_norm(S), 'max_harmonic': max(S) if S else 0})
first = next((rw for rw in rows if not rw['zero']), None)
# background fields: u = (-psi_y, psi_x); rho derivatives
P = lambda i, j: Fd[('psi', (i, j))]; Rh = lambda i, j: Fd[('rho', (i, j))]
u1, u2 = -P(0, 1), P(1, 0); absu = torch.sqrt(u1**2+u2**2)
Du = torch.sqrt(P(1, 1)**2+P(0, 2)**2+P(2, 0)**2+P(1, 1)**2)             # |Du| Frobenius: entries -psi_xy, -psi_yy, psi_xx, psi_xy
D2u = torch.sqrt(3*P(2, 1)**2+3*P(1, 2)**2+P(0, 3)**2+P(3, 0)**2)        # ordered tensor D^2 u: entries (-psi_xxy, -psi_xyy, -psi_xyy, -psi_yyy, psi_xxx, psi_xxy, psi_xxy, psi_xyy)
grho = torch.sqrt(Rh(1, 0)**2+Rh(0, 1)**2); D2rho = torch.sqrt(Rh(2, 0)**2+2*Rh(1, 1)**2+Rh(0, 2)**2); D3rho = torch.sqrt(Rh(3, 0)**2+3*Rh(2, 1)**2+3*Rh(1, 2)**2+Rh(0, 3)**2)
Xw = torch.sqrt(1+r**2)*torch.ones_like(F)
def supat(T):
    idx = int(torch.argmax(T)); i, jj = divmod(idx, mesh.Nt); return {'value': float(T.max()), 'r': float(mesh.r[i]), 'theta': float(mesh.theta[jj])}
bg = {'sup_u_over_r': supat(absu/r), 'sup_Du': supat(Du), 'sup_D2u': supat(D2u), 'sup_grad_rho': supat(grho), 'sup_D2rho': supat(D2rho), 'sup_D3rho': supat(D3rho),
      'sup_Xg_u_over_r': supat(Xw**gamma*absu/r), 'sup_Xg_Du': supat(Xw**gamma*Du), 'sup_Xg_D2u': supat(Xw**gamma*D2u),
      'sup_Xg_grad_rho': supat(Xw**gamma*grho), 'sup_Xg_D2rho': supat(Xw**gamma*D2rho), 'sup_Xg_D3rho': supat(Xw**gamma*D3rho), 'gamma': gamma}
# flow geometry: V = c X + u; V.X/|X|^2 = c + (u.X)/r^2 = c + (u1 cos + u2 sin)/r
nu_field = cf+(u1*cs+u2*sn)/r
idx = int(torch.argmin(nu_field)); i, jj = divmod(idx, mesh.Nt)
flow = {'nu_min': float(nu_field.min()), 'at': {'r': float(mesh.r[i]), 'theta': float(mesh.theta[jj])}, 'sup_u_over_r_bound': cf-float((absu/r).max()), 'note': 'nu = inf (V.X)/|X|^2 over the mesh, V = c X + u (k = 0); the second entry is the cruder bound c - sup|u|/|X|'}
# (B-L2) screening (c1-n1 diag2 formulas, FLOAT)
rx, ry = Rh(1, 0), Rh(0, 1); rxx, rxy, ryy = Rh(2, 0), Rh(1, 1), Rh(0, 2)
theta_field = (torch.sqrt(rx**2+ry**2)-ry)/2
Drx2 = float(torch.sum(base*(rxx**2+rxy**2))); Dry2 = float(torch.sum(base*(rxy**2+ryy**2)))
kappa = math.sqrt(((math.log(2)-0.5)*Drx2+(3*math.log(2)-2)*Dry2)/(16*math.pi))
bl2 = {'theta_inner_sup': supat(theta_field), 'kappa_inner': kappa, 'beta0_float': cf+1-float(theta_field.max())-kappa, 'note': 'FLOAT, mesh 0.02<=r<=R; theta = sup(|grad rho| - rho_y)/2; kappa = c1-n1 diag2 formula (Hilbert-Schmidt route); beta0 = c+1-theta-kappa'}
# strong-norm grid proxies (NOT the Hölder norm): <X>^sigma |F|, <X>^sigma |grad F|, <X>^sigma |D^2 F|
Xs = Xw**SIG
strong = {'sigma': SIG, 'sup_Xs_F': supat(Xs*F.abs()), 'sup_Xs_gradF': supat(Xs*torch.sqrt(Fx**2+Fy**2)), 'sup_Xs_D2F': supat(Xs*torch.sqrt(Fxx**2+2*Fxy**2+Fyy**2)), 'note': 'grid maxima of weighted derivatives; a proxy for the size of S_F, not the Hölder seminorm'}
a0 = X.qfloat(prob._OJ.a0(prob._flat_coefs(coefs)))
tay = prob.taylor_values(coefs)
res = {'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= {R:g}; far parts from the exact sectors (q <= 3, exponents >= -6)',
       'n_generators': len(gens), 'G0': G0, 'G0_inner': G0_in, 'F2_far': F2_far, 'rF': rF, 'rF2_far': rF2_far, 'G1': G1, 'P2': P2, 'supF': float(F.abs().max()), 'supF_at': supat(F.abs()),
       'a0_float': a0, 'taylor_values': [float(v) for v in tay], 'BL2': bl2, 'background': bg, 'flow': flow, 'strong_proxy': strong, 'dyadic': annuli, 'sectors': rows, 'first_nonzero': first,
       'build_s': tb, 'sector_s': tsec, 'total_s': time.time()-t00, 'note': 'FLOAT (float64 GPU quadrature on the stated rule); not bounds'}
json.dump(res, open(outp, 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('dyadic', 'sectors', 'background', 'strong_proxy', 'BL2', 'flow')}, indent=1))
print('BL2', json.dumps(bl2)); print('flow', json.dumps(flow)); print('strong', json.dumps(strong))
for k, v in bg.items(): print('  bg', k, v)
tot = sum(a['L2']**2 for a in annuli)
for a in annuli: print(f"  A_{a['j']:3d} [{a['range'][0]:.4g},{a['range'][1]:.4g}): L2 {a['L2']:.3e} frac {a['L2']**2/tot:.4f} gradF {a['gradF']:.3e} sup|F| {a['supF']:.3e}")
for rw in rows[:12]: print(f"  sector e={rw['exponent']:+.4f} {'ZERO' if rw['zero'] else 'nonzero'} full {rw['full_L2']:.5e} maxharm {rw['max_harmonic']}")
