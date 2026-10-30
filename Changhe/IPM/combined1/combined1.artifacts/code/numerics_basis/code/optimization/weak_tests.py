"""theory_v02 cheap tests (FLOAT, CPU) for an exact candidate: NORM-T-WEAK-v1 (a = 0, k = 0..8), NORM-T-WL2-v1[a], NORM-T-WLAP-v1[a] with the
NC-T-DYADIC-LAP cell test, and the weak pairing per dyadic annulus. argv: candidate_json ANG R out_json [MID]"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt2 as O2, ipm_farpart as FP, time, hashlib, mpmath as mp
path = sys.argv[1]; ANG = int(sys.argv[2]); R = float(sys.argv[3]); outp = sys.argv[4]; MID = int(sys.argv[5]) if len(sys.argv) > 5 else 32
dev = torch.device('cpu')
if 'nb_' in os.path.basename(path):
    dd = json.load(open(path)); c = X.Q(dd['cl']) if isinstance(dd['cl'], str) else X.Q(float(dd['cl']))
    gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec']} for g in dd['generators']]; coefs_q = [X.Q(g['coef']) for g in dd['generators']]
else:
    c, gens, coefs_q, _ = OPT.load_candidate_json(path)
coefs = np.array([X.qfloat(v) for v in coefs_q]); cf = X.qfloat(c)
s, ws, bl = EV.whole_axis_radial(origin_order=48, middle_order=MID); keep = (np.exp(s) >= 0.02) & (s <= math.log(R)+1e-9); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh, r_cut=0.02, r_max=R); tb = time.time()-t0
parts, comp, Fd = prob.objective_parts(coefs); F = comp[(0, 0)]
r = mesh.r[:, None]; sn = mesh.sin[None, :]; base = 4*mesh.W*r**2            # dX over R^2
u0 = 1/(1+r**2); t = r**2*u0; y = r*sn
Ux, Uy = -Fd[('psi', (0, 1))], Fd[('psi', (1, 0))]; Un = torch.sqrt(Ux**2+Uy**2)
rx, ry = Fd[('rho', (1, 0))], Fd[('rho', (0, 1))]; Dr = torch.sqrt(rx**2+ry**2)
terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs_q)])
E, dsec, ssec, mom = X.residual_sectors(c, terms, 3, exp_min=X.mpq(-6))
def S(a, b): return a**a*b**b/(a+b)**(a+b)
weak = {}
for k in range(9):
    phi = y*t**k*u0**2
    Lk = 3*cf+1+2*cf*k*u0-4*cf*t; Gk = 1+2*k*u0+4*t
    I_mesh = float(torch.sum(base*F*phi))
    I_far = 0.0
    for ex_, Sd in E.items():
        if 1 in Sd and Sd[1] != 0:
            al = X.qfloat(ex_); e1 = X.qfloat(Sd[1])
            I_far += math.pi*e1*float(mp.quad(lambda rr_: rr_**(al+2)/(1+rr_**2)**2*(rr_**2/(1+rr_**2))**k, [R, mp.inf]))
    Ik = abs(I_mesh+I_far)
    Ak = math.sqrt(float(torch.sum(base*(phi*Lk)**2))); Bk = math.sqrt(float(torch.sum(base*(t**k*u0**2*Gk*Un)**2))); Ck = math.sqrt(float(torch.sum(base*(r*t**k*u0**2*Dr)**2)))
    Dk = Ak+Bk+Ck; Hk = 1.0 if k == 0 else S(k, 2)+2*k*S(k, 3)+4*S(k+1, 2)
    mk = 2*Ik/(Dk+math.sqrt(Dk*Dk+4*Hk*Ik))
    weak[k] = {'I_k': Ik, 'I_k_signed_mesh': I_mesh, 'I_k_far': I_far, 'A_k': Ak, 'B_k': Bk, 'C_k': Ck, 'D_k': Dk, 'H_k': Hk, 'm_lower_bound': mk}
dist = max(v['m_lower_bound'] for v in weak.values())
# per-annulus signed pairing for k = 0 (where the distance is created)
phi0 = y*u0**2; rr = mesh.r.cpu().numpy(); pair_ann = []
for j in range(-5, 15):
    sel = (rr < 2.0**-4) if j == -5 else ((rr >= 2.0**j) & (rr < 2.0**(j+1)))
    if sel.any(): pair_ann.append({'j': j, 'range': [0 if j == -5 else 2.0**j, 2.0**(j+1)], 'pairing_k0': float(torch.sum((base*F*phi0)[sel]))})
# weighted L2 and weighted Laplacian
wl2 = {str(a): math.sqrt(float(torch.sum(base*(1+r**2)**(-a)*F**2))) for a in (0.5, 0.75, 1.0, 1.2)}
lap = comp[(2, 0)]+comp[(0, 2)]
cover = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1+1/cf]
Na = {}
for a in cover:
    N = math.sqrt(float(torch.sum(base*(1+r**2)**(2-a)*lap**2)))
    B = math.sqrt(8*math.pi)*(1+cf-cf*a)**2/(1+a) if (1+cf-cf*a) > 0 else float('nan')
    Na[f'{a:.6f}'] = {'N_a': N, 'test_lhs_5^((a-2)/2)N_a': 5**((a-2)/2)*N, 'ceiling_B(a)': B, 'passes': bool(5**((a-2)/2)*N < B) if B == B else None}
# mode-1 and mode-3 contributions to N_a (lower bounds per mode)
Fn_lap = (4/math.pi)*(lap*mesh.wth[None, :])@torch.stack([torch.sin(n*mesh.theta) for n in (1, 3)]).T
Na_modes = {str(a): {n: math.sqrt(float(torch.sum((math.pi*mesh.ws*mesh.r**2*(1+mesh.r**2)**(2-a)*Fn_lap[:, i]**2)))) for i, n in enumerate((1, 3))} for a in (0.5, 1.0)}
res = {'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= {R:g}; far parts of I_k from the exact sectors (sin theta coefficients)',
       'label': 'FLOAT (not bounds): I_k far part exact-formula, mesh quadrature elsewhere; B_k, C_k, WL2, N_a restricted to the mesh region',
       'NORM-T-WEAK-v1_a0': weak, 'weak_distance_lower_bound_FLOAT': dist, 'pairing_k0_per_annulus': pair_ann,
       'NORM-T-WL2-v1': wl2, 'NORM-T-WLAP-v1': Na, 'N_a_modes_1_3': Na_modes, 'build_s': tb}
json.dump(res, open(outp, 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('NORM-T-WEAK-v1_a0', 'pairing_k0_per_annulus')}, indent=1))
for k, v in weak.items(): print(f"  k={k}: I {v['I_k']:.4e} D {v['D_k']:.4f} H {v['H_k']:.4f} m>= {v['m_lower_bound']:.4e}")
for p in pair_ann: print(f"  annulus [{p['range'][0]:.4g},{p['range'][1]:.4g}): pairing_k0 {p['pairing_k0']:+.4e}")
