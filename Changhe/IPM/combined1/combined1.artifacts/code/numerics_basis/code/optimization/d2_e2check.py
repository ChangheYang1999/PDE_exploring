import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt2 as O2, time
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
d2 = json.load(open('external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json'))
c = X.Q(d2['cl']) if isinstance(d2['cl'], str) else X.Q(float(d2['cl']))
gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec']} for g in d2['generators']]; coefs = np.array([X.qfloat(X.Q(g['coef'])) for g in d2['generators']])
print('d2 generators', len(gens), 'max m', max(g['m'] for g in gens), flush=True)
s, ws, bl = EV.whole_axis_radial(); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(160); mesh = EV.Mesh(s, ws, th, wth, dev)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh); print('build', time.time()-t0, flush=True)
parts, comp, Fd = prob.objective_parts(coefs)
r = mesh.r[:, None]; base = 4*mesh.W*r**2; om2 = (1+4*r**2)**0.8
P2 = math.sqrt(float(torch.sum(base*om2*(comp[(2,0)]**2+2*comp[(1,1)]**2+comp[(0,2)]**2)))); G1 = math.sqrt(float(torch.sum(base*(comp[(1,0)]**2+comp[(0,1)]**2)))); G0 = math.sqrt(float(torch.sum(base*comp[(0,0)]**2))); rF = math.sqrt(float(torch.sum(base*r**2*comp[(0,0)]**2)))
print(f'd2 FLOAT on 0.02<=r<=1e4 midpoint160: P2 {P2:.10f} (N3 VALIDATED 20.53676513985447)  G1 {G1:.10f} (1.029141871453669)  G0 {G0:.10f} (4.988817004568025)  rF {rF:.6f} (whole plane 2331.566; far part beyond 1e4 = 1696.23 -> inner sqrt(2331.566^2-1696.23^2) = {math.sqrt(2331.566**2-1696.232**2):.3f})', flush=True)
print('sup|F| on mesh', float(comp[(0,0)].abs().max()), '(analysis2 FLOAT 0.1051 at r=30.4)', flush=True)
