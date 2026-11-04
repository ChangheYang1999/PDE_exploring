"""eval_bg2.py (lane numerics_agent_1): second background screen of an exact candidate (theory_v01 T4.4, T5 BG-3/BG-8, T6.4 items 2, 4, 5; coordinator 20:28Z 3d). FLOAT on
the product mesh (GPU): (1) BG-3 margin beta = -max lambda_max(q Sym DV + Kmat - (c + 1 + sigma V.X/(r0^2 + |X|^2)) I) of the candidate's OWN background at
P-S1 = (21/10, 1, 1/2), P-BG1 = (13/5, 7/5, 1/4), P-BG2 = (5/2, 7/5, 1/2), P-S1b = (21/10, 7/5, 1), with the location; (2) the weighted derivative family
A_j = sup <X>^(gamma_9 + j) (|D^j grad rho_bar| + |D^j D u_bar|), j = 0, 1, 2 (ordered Frobenius tensors; j = 3 needs fourth derivatives, not in these tables);
(3) ||F||_inf, ||grad F||_inf, ||<X>^sigma grad F||_inf for sigma in {1, 7/5, 7/4}; (4) C_9 components at R_ext in {4, 8}: sup over |X| >= R_ext of
<X>^gamma_9 |u_bar|/|X|, <X>^gamma_9 |D u_bar|, <X>^gamma_9 |D^2 u_bar| (the Hoelder seminorm [D u_bar]_(C^alpha(B_1(X))) is bounded by the interpolation
form (2 sup|D u_bar|)^(1-alpha) (sup |D^2 u_bar|)^alpha over the ball) and C_9' components <X>^gamma_9 |grad rho_bar|, |D^2 rho_bar|, |D^3 rho_bar|;
(5) mu_R = q_0(R) - (1 + alpha) L_R, q_0(R) = inf_{|X| >= R} (1 + sigma_9 V.X/(1 + |X|^2)), L_R = sup_{|X| >= R} ||DV||_op (T4.4) at (sigma_9, alpha) in
{(7/4, 1/2), (7/4, 1/4)} and R in {4, 8, 16}.  argv: cand.json out.json [ANG=180] [MID=32] [R=8356.474846731926]"""
import sys, os, json, time, math
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_optn1 as ON1
path = sys.argv[1]; outp = sys.argv[2]; ANG = int(sys.argv[3]) if len(sys.argv) > 3 else 180; MID = int(sys.argv[4]) if len(sys.argv) > 4 else 32
R = float(sys.argv[5]) if len(sys.argv) > 5 else 8356.474846731926
dev = torch.device(os.environ.get('IPM_DEVICE', 'cuda')); t00 = time.time()
c, gens, coefs_q, J = OPT.load_candidate_json(path); coefs = np.array([X.qfloat(v) for v in coefs_q]); cf = X.qfloat(c); g9 = 1-1/cf
mesh = build_mesh(MID, ANG, 0.02, R, dev)
prob = ON1.ProblemN1(gens, c, mesh, r_cut=0.02, r_max=R, wF=1.0)
Fd = prob.fields(coefs); comp = prob.F_components(Fd, ON1.DERIVS)
r = mesh.r[:, None]*torch.ones_like(mesh.W); sn = mesh.sin[None, :]*torch.ones_like(mesh.W); cs = mesh.cos[None, :]*torch.ones_like(mesh.W); Xw = torch.sqrt(1+r**2)
P = lambda i, j: Fd[('psi', (i, j))]; Rh = lambda i, j: Fd[('rho', (i, j))]
u1, u2 = -P(0, 1), P(1, 0); u1x, u1y, u2x, u2y = -P(1, 1), -P(0, 2), P(2, 0), P(1, 1)
def supat(T):
    idx = int(torch.argmax(T)); i, jj = divmod(idx, mesh.Nt); return {'value': float(T.max()), 'r': float(mesh.r[i]), 'theta': float(mesh.theta[jj])}
def infat(T):
    idx = int(torch.argmin(T)); i, jj = divmod(idx, mesh.Nt); return {'value': float(T.min()), 'r': float(mesh.r[i]), 'theta': float(mesh.theta[jj])}
out = {'candidate': os.path.basename(path), 'sha256': sha256_file(path), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= {R:g}', 'gamma_9': g9, 'label': 'FLOAT', 'note': 'numerics_agent_1 eval_bg2.py; nothing here is a bound'}
# (1) BG-3 margins of the own background
s11 = cf+u1x; s22 = cf+u2y; s12 = 0.5*(u1y+u2x); k11 = -Rh(0, 1); k12 = 0.5*Rh(1, 0); e = cf+(u1*cs+u2*sn)/r
bg3 = {}
for name, q, sig, r0 in (('P-S1', 2.1, 1.0, 0.5), ('P-BG1', 2.6, 1.4, 0.25), ('P-BG2', 2.5, 1.4, 0.5), ('P-S1b', 2.1, 1.4, 1.0)):
    aW = sig*e*r**2/(r0**2+r**2); a11 = q*s11+k11-(cf+1+aW); a22 = q*s22-(cf+1+aW); a12 = q*s12+k12
    lam = 0.5*(a11+a22)+torch.sqrt((0.5*(a11-a22))**2+a12**2); m_ = supat(lam)
    bg3[name] = {'q': q, 'sigma': sig, 'r0': r0, 'beta': -m_['value'], 'at_r': m_['r'], 'at_theta': m_['theta'], 'origin_cap': cf+1-q, 'far_cap': 1+cf*(1+sig-q)}
out['BG3_margins'] = bg3
# (2) weighted derivative family A_j, j = 0, 1, 2
grho = torch.sqrt(Rh(1, 0)**2+Rh(0, 1)**2); D2rho = torch.sqrt(Rh(2, 0)**2+2*Rh(1, 1)**2+Rh(0, 2)**2); D3rho = torch.sqrt(Rh(3, 0)**2+3*Rh(2, 1)**2+3*Rh(1, 2)**2+Rh(0, 3)**2)
Du = torch.sqrt(u1x**2+u1y**2+u2x**2+u2y**2); D2u = torch.sqrt(3*P(2, 1)**2+3*P(1, 2)**2+P(0, 3)**2+P(3, 0)**2)
# D^3 u needs fourth derivatives of psi: not available (tables to order 3); report D^2 u for j = 1 and note j = 2 for u omitted
out['A_family'] = {'A0_sup_Xg_(grad_rho+Du)': supat(Xw**g9*(grho+Du)), 'A1_sup_Xg1_(D2rho+D2u)': supat(Xw**(g9+1)*(D2rho+D2u)), 'A2_sup_Xg2_D3rho_only': supat(Xw**(g9+2)*D3rho), 'note': 'A_j = sup <X>^(gamma_9+j)(|D^j grad rho| + |D^j D u|); the D^3 u part of A2 and all of A3 need fourth-order field tables (not in this version)'}
# (3) sup norms of F
F = comp[(0, 0)]; gF = torch.sqrt(comp[(1, 0)]**2+comp[(0, 1)]**2); D2F = torch.sqrt(comp[(2, 0)]**2+2*comp[(1, 1)]**2+comp[(0, 2)]**2)
out['F_sup'] = {'F_inf': supat(F.abs()), 'gradF_inf': supat(gF), 'D2F_inf': supat(D2F)}
for sig in (1.0, 1.4, 1.75):
    out['F_sup'][f'Xs{sig}_F_inf'] = supat(Xw**sig*F.abs()); out['F_sup'][f'Xs{sig}_gradF_inf'] = supat(Xw**sig*gF); out['F_sup'][f'Xs{sig}_D2F_inf'] = supat(Xw**sig*D2F)
# (4) C_9 components beyond R_ext, (5) mu_R
DVop = torch.sqrt(((s11**2+s12**2+s12**2+s22**2)+torch.sqrt(((s11**2+s12**2+s12**2+s22**2))**2-4*(s11*s22-s12*s12)**2).clamp(min=0))/2)   # Sym DV op norm; DV itself:
a_, b_, c_, d_ = cf+u1x, u1y, u2x, cf+u2y; S_ = a_**2+b_**2+c_**2+d_**2; Dt = a_*d_-b_*c_; DVop_full = torch.sqrt((S_+torch.sqrt((S_*S_-4*Dt*Dt).clamp(min=0)))/2)
ext = {}
for Rext in (4.0, 8.0, 16.0):
    sel = (r >= Rext)
    def supsel(T): 
        Tm = torch.where(sel, T, torch.full_like(T, -1e300)); return supat(Tm)
    def infsel(T):
        Tm = torch.where(sel, T, torch.full_like(T, 1e300)); return infat(Tm)
    row = {'C9_u_over_r': supsel(Xw**g9*torch.sqrt(u1**2+u2**2)/r), 'C9_Du': supsel(Xw**g9*Du), 'C9_D2u': supsel(Xw**g9*D2u),
           'C9p_grad_rho': supsel(Xw**g9*grho), 'C9p_D2rho': supsel(Xw**g9*D2rho), 'C9p_D3rho': supsel(Xw**g9*D3rho),
           'L_R_sup_DV_op': supsel(DVop_full)}
    for sig9, al in ((1.75, 0.5), (1.75, 0.25)):
        q0 = infsel(1+sig9*e*r**2/(1+r**2))
        row[f'mu_R_sigma{sig9}_alpha{al}'] = {'q0': q0['value'], 'q0_at_r': q0['r'], 'L_R': row['L_R_sup_DV_op']['value'], 'mu_R': q0['value']-(1+al)*row['L_R_sup_DV_op']['value']}
    ext[f'R_ext_{Rext:g}'] = row
out['exterior'] = ext; out['total_s'] = time.time()-t00
json.dump(out, open(outp, 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k in ('candidate', 'BG3_margins')}, indent=1))
print('A family', {k: (round(v['value'], 4), round(v['r'], 3)) for k, v in out['A_family'].items() if isinstance(v, dict)})
print('F sup', {k: round(v['value'], 5) for k, v in out['F_sup'].items()})
for k, row in ext.items(): print(k, {kk: (round(vv['value'], 4) if isinstance(vv, dict) and 'value' in vv else {k3: round(v3, 4) for k3, v3 in vv.items() if isinstance(v3, float)}) for kk, vv in row.items()})
