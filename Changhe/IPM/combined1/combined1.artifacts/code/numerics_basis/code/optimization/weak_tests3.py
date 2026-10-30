"""weak_tests3.py: FLOAT weak probes for an exact candidate over the N4-160 angular family phi_(n,K) = r v^2 t^K sin(n theta) (v = 1/(1+r^2),
t = r^2/(1+r^2); n odd, K >= (n-1)/2) plus the first-mode list of weak_tests2.  For each probe: pairing I (mesh, signed; far correction from the exact
sectors for n = 1 only, negligible otherwise at these K), A = ||(2c+1) phi + c r d_r phi||_2 (mesh), B <= || v^2 t^K sqrt(d_K(t)^2 + n^2) |u| ||_2 with
d_K(t) = 2K(1-t) + 1 - 4t (= r d_r(r v^2 t^K)/(v^2 t^K)... computed exactly on the mesh as |grad phi| bound), C <= || r v^2 t^K |grad rho| ||_2,
H >= sup |grad phi| (mesh maximum times 1.05), m = 2|I|/(D + sqrt(D^2 + 4 H |I|)).  argv: candidate_json ANG R out_json [MID]
Labels: FLOAT; the formulas follow c1-n4 research/angular_weak_probes/PROOF.md (N4-160); the n = 1 values coincide with weak_tests2 up to the H bound."""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt2 as O2, time, hashlib
path = sys.argv[1]; ANG = int(sys.argv[2]); R = float(sys.argv[3]); outp = sys.argv[4]; MID = int(sys.argv[5]) if len(sys.argv) > 5 else 32
dev = torch.device('cpu')
c, gens, coefs_q, _ = OPT.load_candidate_json(path)
coefs = np.array([X.qfloat(v) for v in coefs_q]); cf = X.qfloat(c)
s, ws, bl = EV.whole_axis_radial(origin_order=48, middle_order=MID); keep = (np.exp(s) >= 0.02) & (s <= math.log(R)+1e-9); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh, r_cut=0.02, r_max=R); tb = time.time()-t0
parts, comp, Fd = prob.objective_parts(coefs); F = comp[(0, 0)]
r = mesh.r[:, None]; base = 4*mesh.W*r**2; theta = mesh.theta[None, :]
v = 1/(1+r**2); t = r**2*v
Ux, Uy = -Fd[('psi', (0, 1))], Fd[('psi', (1, 0))]; Un = torch.sqrt(Ux**2+Uy**2)
rx, ry = Fd[('rho', (1, 0))], Fd[('rho', (0, 1))]; Dr = torch.sqrt(rx**2+ry**2)
NMAX = int(os.environ.get('IPM_NMAX', '31'))      # IPM_NMAX > 31 extends the N4-160-type sweep to higher odd modes (same K0 offsets; held-out, never objective rows)
probes = [(n, (n-1)//2+K0) for n in range(1, NMAX+1, 2) for K0 in (0, 8, 32, 128, 512)]           # N4-160's 80 probes (n <= 31)
probes += [(1, k) for k in (1, 2, 3, 4, 5, 6, 7, 12, 16, 24, 48, 64, 96, 192, 256, 384, 768, 1024, 1536, 2048, 3072, 4096) if (1, k) not in probes]
probes += [(n, K) for n in (19, 23, 25, 29, 31) for K in (600, 900, 1200, 1800, 2400)]      # theory_v04 section 6 item 2 held-out set (never in any objective of this lane)
res = {}
for n, K in probes:
    phi = r*v**2*t**K*torch.sin(n*theta)
    rad = r*v**2*t**K                                   # radial factor g(r); r g'(r) = g (1 + 2K(1-t) - 4t)   since r d_r t = 2t(1-t), r d_r v = -2 t
    rdphi = rad*(1+2*K*(1-t)-4*t)*torch.sin(n*theta)   # r d_r phi
    I = float(torch.sum(base*F*phi))
    A = math.sqrt(float(torch.sum(base*((2*cf+1)*phi+cf*rdphi)**2)))
    gradphi_bound = v**2*t**K*torch.sqrt((1+2*K*(1-t)-4*t)**2+n*n)      # |grad phi| <= v^2 t^K sqrt(d_K^2 + n^2)  (polar components)
    B = math.sqrt(float(torch.sum(base*(gradphi_bound*Un)**2)))
    C = math.sqrt(float(torch.sum(base*(rad*Dr)**2)))
    H = 1.05*float(gradphi_bound.max())
    D = A+B+C; m = 2*abs(I)/(D+math.sqrt(D*D+4*H*abs(I)))
    res[f'{n}:{K}'] = {'n': n, 'K': K, 'I_signed_mesh': I, 'A': A, 'B_bound': B, 'C_bound': C, 'H_bound_mesh': H, 'D': D, 'm_lower_bound': m, 'I_over_phi_norm': I/math.sqrt(float(torch.sum(base*phi**2)))}
best = max(res, key=lambda q: res[q]['m_lower_bound'])
by_mode = {n: max((res[q]['m_lower_bound'] for q in res if res[q]['n'] == n), default=0) for n in range(1, NMAX+1, 2)}
out = {'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= {R:g}; no far correction (negligible for K >= 1 at these radii; n = 1, K = 0 far part is 2e-13 for these candidates)',
       'label': 'FLOAT (not bounds); probe family of N4-160 (80 probes) plus first-mode k list plus the theory_v04 held-out set n in {19,23,25,29,31} x K in {600,...,2400}; H from the mesh maximum of the gradient bound', 'probes': res,
       'best_probe': best, 'best_m': res[best]['m_lower_bound'], 'best_m_by_mode': by_mode, 'build_s': tb}
json.dump(out, open(outp, 'w'), indent=1)
print(json.dumps({k: out[k] for k in ('candidate', 'best_probe', 'best_m', 'best_m_by_mode')}, indent=1))
for q in sorted(res, key=lambda q: -res[q]['m_lower_bound'])[:12]:
    x = res[q]; print(f"  probe n={x['n']:2d} K={x['K']:4d}: I {x['I_signed_mesh']:+.4e} A {x['A']:.3e} B {x['B_bound']:.2e} C {x['C_bound']:.2e} H {x['H_bound_mesh']:.2e} m>= {x['m_lower_bound']:.4e}")
