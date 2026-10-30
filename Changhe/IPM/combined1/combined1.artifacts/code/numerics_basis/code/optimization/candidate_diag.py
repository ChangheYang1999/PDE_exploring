"""FLOAT diagnostics of a candidate (exact generator JSON): objectives on a chosen angular rule, far parts beyond R via exact sectors,
largest |F| points with |V| and |grad rho|, per-octave profile. argv: candidate_json ANG rule(mid|gauss) RMAX [out_json]"""
import sys, json, math, os, numpy as np, torch
sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/lib')
import ipm_exact as X, ipm_eval as EV, ipm_opt as OPT, ipm_farpart as FP
path = sys.argv[1]; ANG = int(sys.argv[2]); rule = sys.argv[3]; RMAX = float(sys.argv[4]); outp = sys.argv[5] if len(sys.argv) > 5 else None
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
c, gens, coefs, J = OPT.load_candidate_json(path)
cf = X.qfloat(c); a = np.array([X.qfloat(v) for v in coefs])
s, ws, bl = EV.whole_axis_radial(); th, wth = (EV.angular_midpoint(ANG) if rule == 'mid' else EV.angular_gauss(ANG))
mesh = EV.Mesh(s, ws, th, wth, dev)
evg = [EV.Generator(g['m'], X.qfloat(OPT.gen_p(g, c)), tuple(g['spec'])) for g in gens]
B = EV.Basis(evg, mesh, cf)
Rf, Fd = B.residual_Rf(torch.as_tensor(a, dtype=torch.float64, device=dev))
r = mesh.r[:, None]; sn = mesh.sin[None, :]; cs = mesh.cos[None, :]
F = r*sn*Rf
mask = ((r >= 0.02) & (r <= RMAX)).to(torch.float64)*torch.ones_like(Rf)
W = mesh.W
def integ(q): return float(torch.sum(W*q*mask))
res = {'candidate': os.path.basename(path), 'sha256': __import__('hashlib').sha256(open(path,'rb').read()).hexdigest(), 'rule': f'{rule}{ANG}', 'r_range': [0.02, RMAX],
       'Jabs_mesh': integ(Rf*Rf)/(math.pi*EV.A_REF**2), 'F2_mesh': integ(4*r**4*sn**2*Rf*Rf), 'rF2_mesh': integ(4*r**6*sn**2*Rf*Rf)}
# far part via exact sectors
terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs)])
far = FP.report_far(c, terms, RMAX, qmax=6)
res['far'] = far
res['G0_total_float'] = math.sqrt(res['F2_mesh']+(far['F2_far'] or float('inf')))
res['rF_total_float'] = math.sqrt(res['rF2_mesh']+(far['rF2_far'] or float('inf')))
# point diagnostics
Vx = cf*r*cs-Fd['psiy']; Vy = cf*r*sn+Fd['psix']; Vn = torch.sqrt(Vx**2+Vy**2)
rhox = r*sn*Fd['fx']; rhoy = Fd['f']+r*sn*Fd['fy']; gradrho = torch.sqrt(rhox**2+rhoy**2)
Fm = (F*mask).abs(); flat = torch.argsort(Fm.reshape(-1), descending=True)[:8]
pts = []
for idx in flat.tolist():
    i, j = divmod(idx, mesh.Nt)
    pts.append({'r': float(mesh.r[i]), 'theta': float(mesh.theta[j]), 'F': float(F[i, j]), 'absV': float(Vn[i, j]), 'absgradrho': float(gradrho[i, j]), 'rho_y': float(rhoy[i, j])})
res['largest_F_points'] = pts
res['sup_F_mesh'] = pts[0]['F']
# octave profile of sup|F| and of F2 contribution
prof = []
rr = mesh.r.cpu().numpy()
for k in range(-6, 14):
    lo, hi = 2.0**k, 2.0**(k+1); sel = (rr >= lo) & (rr < hi)
    if sel.any() and lo >= 0.02 and lo < RMAX:
        prof.append({'octave': [lo, hi], 'sup_F': float(F[sel].abs().max()), 'F2': float(torch.sum((W*4*r**4*sn**2*Rf*Rf)[sel]))})
res['octaves'] = prof
res['a0_float'] = float(Fd['f'][0, 0])
print(json.dumps({k: v for k, v in res.items() if k not in ('octaves',)}, indent=1))
for p in prof: print(f"  r in [{p['octave'][0]:.3g},{p['octave'][1]:.3g}): sup|F| {p['sup_F']:.3e}  F2 {p['F2']:.3e}")
if outp: json.dump(res, open(outp, 'w'), indent=1)
