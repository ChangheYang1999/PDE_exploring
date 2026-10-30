"""I_k of a candidate on the reduced rules MID = 16 (and optionally others) against the MID 32 reference; argv: exact_json ANG MID[,MID...]"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt3 as O3, time
path = sys.argv[1]; ANG = int(sys.argv[2]); MIDS = [int(x) for x in sys.argv[3].split(',')]
dev = torch.device('cpu'); c, gens, coefs_q, _ = OPT.load_candidate_json(path); a = np.array([X.qfloat(v) for v in coefs_q])
KL = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
for MID in MIDS:
    s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
    th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
    t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=1.0, pair_k=KL, r_cut=0.02, r_max=1e4, hw=20/21, wlog=2.**18*100, wkap=3e6)
    parts, comp, _ = prob.objective_parts(a); I = prob.pairings(comp[(0, 0)])
    r = mesh.r[:, None]; base = 4*mesh.W*r**2; G0 = math.sqrt(float(torch.sum(base*comp[(0, 0)]**2)))
    print(f'MID {MID} mesh {mesh.Nr}x{mesh.Nt} build+eval {time.time()-t0:.0f}s G0 {G0:.6f}:', ' '.join(f'k{k}:{v:+.5e}' for k, v in zip(KL, I)), flush=True)
print('reference MID 32: k0 +1.5510e-04 k1 +9.6383e-05 k2 +7.4115e-05 k4 +5.7487e-05 k8 +4.5236e-05 k16 +3.3472e-05 k32 +2.3435e-05 k64 +1.2983e-05 k128 +2.6914e-06 k256 4.3886e-07 k512 3.7093e-07 k1024 1.3917e-07 k2048 3.4831e-07 k4096 1.0642e-08 (abs); G0 0.376689')
