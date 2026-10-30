"""FLOAT diagnostics per theory_v01 for an exact candidate JSON: NORM-T-DYADIC-v1 profile, G0/G1/P2 (+ far parts), rF, Hdot^-1 (exact far terms),
X3 proxy (raw components; gamma_i >= (G1, G0)), NORM-T-PTNEC-v1 / PTSYM-v1 point tests on the mesh, sector table summary.
argv: candidate_json ANG R out_json [MID]"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt2 as O2, ipm_hminus1 as HM, ipm_farpart as FP, time, hashlib, os
path = sys.argv[1]; ANG = int(sys.argv[2]); R = float(sys.argv[3]); outp = sys.argv[4]; MID = int(sys.argv[5]) if len(sys.argv) > 5 else 32
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
if 'nb_' in os.path.basename(path):
    dd = json.load(open(path)); c = X.Q(dd['cl']) if isinstance(dd['cl'], str) else X.Q(float(dd['cl']))
    gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec']} for g in dd['generators']]; coefs_q = [X.Q(g['coef']) for g in dd['generators']]
else:
    c, gens, coefs_q, _ = OPT.load_candidate_json(path)
coefs = np.array([X.qfloat(v) for v in coefs_q]); cf = X.qfloat(c)
s, ws, bl = EV.whole_axis_radial(origin_order=48, middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= R); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh, r_cut=0.02, r_max=R); tb = time.time()-t0
parts, comp, Fd = prob.objective_parts(coefs)
r = mesh.r[:, None]; sn = mesh.sin[None, :]; cs = mesh.cos[None, :]; base = 4*mesh.W*r**2; om2 = (1+4*r**2)**0.8
F = comp[(0, 0)]; Fx, Fy = comp[(1, 0)], comp[(0, 1)]; Fxx, Fxy, Fyy = comp[(2, 0)], comp[(1, 1)], comp[(0, 2)]
dens = {'F2': base*F**2, 'rF2': base*r**2*F**2, 'G12': base*(Fx**2+Fy**2), 'P22': base*om2*(Fxx**2+2*Fxy**2+Fyy**2)}
rr = mesh.r.cpu().numpy()
annuli = []
jmin = -5
for j in range(-5, 15):
    if j == -5: sel = rr < 2.0**-4
    else: sel = (rr >= 2.0**j) & (rr < 2.0**(j+1))
    if not sel.any(): continue
    annuli.append({'j': j, 'range': [0 if j == -5 else 2.0**j, 2.0**(j+1)], 'L2': math.sqrt(float(dens['F2'][sel].sum())), 'rF': math.sqrt(float(dens['rF2'][sel].sum())),
                   'gradF': math.sqrt(float(dens['G12'][sel].sum())), 'omD2F': math.sqrt(float(dens['P22'][sel].sum())), 'supF': float(F[sel].abs().max())})
# exact sectors and far parts
terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs_q)])
t0 = time.time(); E, dsec, ssec, mom = X.residual_sectors(c, terms, 3, exp_min=X.mpq(-6)); tsec = time.time()-t0   # sectors to exponent -6, descendants q<=3 (far parts beyond R=8356 are dominated by exponents >= -3.5)
far = FP.far_parts(E, R)
F2_far = float(far[0]) if far[0] != float('inf') else None; rF2_far = float(far[1]) if far[1] != float('inf') else None
G0 = math.sqrt(float(dens['F2'].sum())+(F2_far or 0)); rF = math.sqrt(float(dens['rF2'].sum())+(rF2_far or 0))
G1 = math.sqrt(float(dens['G12'].sum())); P2 = math.sqrt(float(dens['P22'].sum()))
hm = HM.hminus1(F, mesh, R, E)
# sector summary
gamma = 1/c
rows = []
for ex in sorted(E.keys(), reverse=True):
    S = E[ex]
    if ex < gamma-10*(1-gamma): continue
    rows.append({'exponent': X.qfloat(ex), 'exponent_exact': X.qstr(ex), 'zero': not S, 'quarter_L2': X.quarter_norm(S), 'full_L2': 2*X.quarter_norm(S), 'max_harmonic': max(S) if S else 0,
                 'sum_pi_am2_over_m_plus_sigma_sq': (float(sum(math.pi*X.qfloat(v)**2/(k+(-2-X.qfloat(ex)))**2 for k, v in S.items())) if S and X.qfloat(ex) < -2 else None)})
first = next((rw for rw in rows if not rw['zero']), None)
# exact exterior Hdot^-1 of each surviving sector beyond R (closed form, FLOAT evaluation) and their sum
Hfar = {}
for ex_, S in E.items():
    if S and X.qfloat(ex_) < -2:
        Hfar[X.qstr(ex_)] = float(FP.hminus1_far_sector(S, ex_, R))
H_far_sectors_sq_sum = sum(Hfar.values())
# point tests (FLOAT, mesh points): PTNEC and PTSYM
Vx = cf*r*cs-Fd[('psi', (0, 1))]; Vy = cf*r*sn+Fd[('psi', (1, 0))]; Vn = torch.sqrt(Vx**2+Vy**2)
grho = torch.sqrt(Fd[('rho', (1, 0))]**2+Fd[('rho', (0, 1))]**2)
pt = {}
for sname, sv in (('2^-18', 2.**-18), ('2^-17', 2.**-17), ('2^-16', 2.**-16), ('5*2^-18', 5*2.**-18)):
    C0 = 1/(2*math.sqrt(math.pi*(1+sv))); C1 = (8*math.pi*sv*(1+sv))**-0.5; B = C0*C1
    A = C1*Vn+C0*(1+grho); rn = 2*F.abs()/(A+torch.sqrt(A*A+4*B*F.abs()))
    idx = int(torch.argmax(rn)); i, jj = divmod(idx, mesh.Nt)
    # PTSYM at axis points: our theta grid does not contain theta = pi/2 exactly; use the node closest to the axis
    jax = int(torch.argmin((mesh.theta-math.pi/2).abs())); C1s = (16*math.pi*sv*(1+sv))**-0.5; Bs = C0*C1s
    Aax = C1s*Vn[:, jax]+C0*(1+grho[:, jax]); rs = 2*F[:, jax].abs()/(Aax+torch.sqrt(Aax*Aax+4*Bs*F[:, jax].abs()))
    selax = mesh.r >= 0.5; ia = int(torch.argmax(rs*selax))
    pt[sname] = {'R_nec': float(rn.max()), 'at': {'r': float(mesh.r[i]), 'theta': float(mesh.theta[jj]), 'F': float(F[i, jj]), 'absV': float(Vn[i, jj]), 'absgradrho': float(grho[i, jj])},
                 'R_sym_axis': float(rs[ia]), 'axis_point': {'r': float(mesh.r[ia]), 'theta': float(mesh.theta[jax]), 'F': float(F[ia, jax])}}
# (B-L2) quantities (FLOAT, mesh): theta = sup (|grad rho| - rho_y)/2 ; kappa^2 = [(ln2-1/2)||D rho_x||^2 + (3ln2-2)||D rho_y||^2]/(16 pi), integrals over R^2 (4 quadrants), inner region only
rx, ry = Fd[('rho', (1, 0))], Fd[('rho', (0, 1))]; rxx, rxy, ryy = Fd[('rho', (2, 0))], Fd[('rho', (1, 1))], Fd[('rho', (0, 2))]
theta_field = (torch.sqrt(rx**2+ry**2)-ry)/2; it_ = int(torch.argmax(theta_field)); ti, tj = divmod(it_, mesh.Nt)
Drx2 = float(torch.sum(base*(rxx**2+rxy**2))); Dry2 = float(torch.sum(base*(rxy**2+ryy**2)))
kappa = math.sqrt(((math.log(2)-0.5)*Drx2+(3*math.log(2)-2)*Dry2)/(16*math.pi))
bl2 = {'theta_inner_sup': float(theta_field.max()), 'theta_at': {'r': float(mesh.r[ti]), 'theta': float(mesh.theta[tj])}, 'kappa_inner': kappa, 'D_rho_x_L2_inner': math.sqrt(Drx2), 'D_rho_y_L2_inner': math.sqrt(Dry2),
       'margin_c_plus_1_minus_theta_minus_kappa_minus_2': cf+1-float(theta_field.max())-kappa-2, 'required': 'theta + kappa <= c_l - 1 = %.6f' % (cf-1), 'note': 'FLOAT on the mesh 0.02<=r<=R; sup over R^2 may be larger (origin and far field not sampled)'}
# weak probe (c1-n4 N4-053 / T2-R3 Proposition W), p = 2: pairing <F, phi_2>, phi_2 = y/(1+r^2)^2; N_2, A_2 closed forms; B_2 = ||u^2 U||_2, C_2 = ||r u^2 grad rho||_2 (mesh + exact far part for the pairing)
import mpmath as mp
u_ = 1/(1+r**2); y_ = r*sn; pp = 2
pair_mesh = float(torch.sum(base*F*y_*u_**pp))
pair_far = 0.0
for ex_, S in E.items():
    if 1 in S and S[1] != 0:
        al = X.qfloat(ex_); e1 = X.qfloat(S[1])
        pair_far += math.pi*e1*float(mp.quad(lambda rr_: rr_**(al+2)/(1+rr_**2)**pp, [R, mp.inf]))
Ux, Uy = -Fd[('psi', (0, 1))], Fd[('psi', (1, 0))]
B2 = math.sqrt(float(torch.sum(base*u_**(2*pp)*(Ux**2+Uy**2)))); C2 = math.sqrt(float(torch.sum(base*r**2*u_**(2*pp)*(rx**2+ry**2))))
N2 = math.sqrt(math.pi/(2*(2*pp-1)*(2*pp-2)))
A2 = math.sqrt(math.pi/2*float(mp.quad(lambda t: t*(1-t)**(2*pp-3)*((3*cf+1)-2*cf*pp*t)**2, [0, 1])))
D2 = A2+(1+2*pp)*B2+C2
weak = {'p': pp, 'pairing': pair_mesh+pair_far, 'pairing_mesh': pair_mesh, 'pairing_far_exact_sectors': pair_far, 'A_p': A2, 'B_p_inner': B2, 'C_p_inner': C2, 'N_p': N2, 'denominator_A+5B+C': D2,
        'm_min_if_d_zero': abs(pair_mesh+pair_far)/D2, 'note': 'FLOAT; necessary condition |<F,phi_p>| <= m [A_p + (1+2p) B_p + C_p + d N_p] for any correction with ||h||_2 <= m, ||grad h||_inf <= d at fixed c (N4-053, Proposition W); d2 reference values N4-053: pairing -0.028802, A 1.65953, B 0.481917, C 6.51819, N 0.511663'}
res = {'candidate': os.path.basename(path), 'BL2': bl2, 'weak_probe_p2': weak, 'H_far_sector_sq_by_exponent': Hfar, 'H_far_sectors_sq_sum_no_cross': H_far_sectors_sq_sum, 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= {R:g}', 'build_s': tb, 'sector_s': tsec,
       'G0': G0, 'G0_inner': math.sqrt(float(dens['F2'].sum())), 'F2_far': F2_far, 'G1': G1, 'P2': P2, 'rF': rF, 'rF2_far': rF2_far, 'H': hm['H'] if hm else None, 'H_parts': ({k: hm[k] for k in ('inner', 'cross', 'outer')} if hm else None),
       'X3_proxy_raw': math.sqrt(P2**2+2**14*G1**2+2**18*G0**2), 'E2_proxy_raw_with_H': (math.sqrt(P2**2+2**14*G1**2+2**18*G0**2+2**18*(20/21)*hm['H']**2) if hm else None),
       'supF': float(F.abs().max()), 'a0_float': float(Fd[('rho', (0, 1))][0, 0]) if False else None, 'dyadic': annuli, 'sectors': rows, 'first_nonzero': first, 'point_tests': pt,
       'note': 'FLOAT (float64 GPU, quadrature on the stated rule, exact sector far parts beyond R); not bounds'}
json.dump(res, open(outp, 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('dyadic', 'sectors')}, indent=1))
for a in annuli: print(f"  A_{a['j']:3d} [{a['range'][0]:.4g},{a['range'][1]:.4g}): L2 {a['L2']:.3e} rF {a['rF']:.3e} gradF {a['gradF']:.3e} omD2F {a['omD2F']:.3e} sup|F| {a['supF']:.3e}")
for rw in rows[:12]: print(f"  sector e={rw['exponent']:+.4f} {'ZERO' if rw['zero'] else 'nonzero'} full {rw['full_L2']:.5e} maxharm {rw['max_harmonic']}")
