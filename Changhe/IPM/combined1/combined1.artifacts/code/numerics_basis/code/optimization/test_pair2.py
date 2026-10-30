"""Problem3 checks: (1) finite-difference check of the pairing-row contribution to the GN gradient on a coarse mesh; (2) I_k on the reduced
optimization rule (MID 8, ANG 180) against the diagnostic rule (MID 32) for the 007 candidate.  argv: exact_json WPAIR"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt3 as O3, time
path = sys.argv[1]; WPAIR = float(sys.argv[2])
dev = torch.device('cpu')
c, gens, coefs_q, _ = OPT.load_candidate_json(path); a = np.array([X.qfloat(v) for v in coefs_q])
KL = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
def build(ANG, MID, wpair):
    s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
    th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
    t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=wpair, pair_k=KL, r_cut=0.02, r_max=1e4, hw=20/21, wlog=2.**18*100, wkap=3e6)
    print(f'build ANG {ANG} MID {MID}: {time.time()-t0:.1f}s mesh {mesh.Nr}x{mesh.Nt}', flush=True); return prob
# (1) FD check on the coarse mesh
prob = build(60, 4, WPAIR)
G, g, phi = prob.normal_equations(a); Ik = list(prob.last_Ik)
prob.pair = []; G0, g0, phi0 = prob.normal_equations(a); prob.pair = [(ph, WPAIR) for ph in [p for p, _ in []]]  # placeholder
prob = build(60, 4, WPAIR)   # rebuild to restore the pair rows cleanly
rng = np.random.default_rng(1)
for trial in range(3):
    v = rng.standard_normal(prob.n); v /= np.linalg.norm(v); eps = 1e-6
    _, cp, _ = prob.objective_parts(a+eps*v); Ip = prob.pairings(cp[(0, 0)])
    _, cm, _ = prob.objective_parts(a-eps*v); Im = prob.pairings(cm[(0, 0)])
    dI = [(p-m)/(2*eps) for p, m in zip(Ip, Im)]
    lhs = float((g-g0)@torch.as_tensor(v)); rhs = sum(WPAIR*I*d for I, d in zip(Ik, dI))
    print(f'trial {trial}: (g_pair . v) {lhs:+.6e}  vs  sum_k w I_k dI_k/dv (FD) {rhs:+.6e}  rel diff {abs(lhs-rhs)/max(abs(rhs),1e-300):.2e}', flush=True)
    # also the Gauss-Newton matrix part: v^T (G-G0) v = sum_k w (dI_k/dv)^2
    lhs2 = float(torch.as_tensor(v)@((G-G0)@torch.as_tensor(v))); rhs2 = sum(WPAIR*d*d for d in dI)
    print(f'          v^T G_pair v {lhs2:+.6e}  vs  sum_k w (dI_k/dv)^2 (FD) {rhs2:+.6e}  rel diff {abs(lhs2-rhs2)/max(abs(rhs2),1e-300):.2e}', flush=True)
print('phi with pairs', phi, 'without', phi0, 'difference', phi-phi0, 'sum w I^2', sum(WPAIR*I*I for I in Ik), flush=True)
# (2) I_k on the reduced optimization rule
prob8 = build(180, 8, WPAIR); _, comp8, _ = prob8.objective_parts(a); I8 = prob8.pairings(comp8[(0, 0)])
print('I_k (MID 8, ANG 180):', ' '.join(f'k{k}:{v:+.5e}' for k, v in zip(KL, I8)), flush=True)
print('reference (MID 32, ANG 180, weak_tests2 of 007): k0 +1.5510e-04 k1 +9.6383e-05 k2 +7.4115e-05 k4 +5.7487e-05 k8 +4.5236e-05 k16 +3.3472e-05 k32 +2.3435e-05 k64 +1.2983e-05 k128 +2.6914e-06 k256 4.3886e-07 k512 3.7093e-07 k1024 1.3917e-07 k2048 3.4831e-07 k4096 1.0642e-08 (abs values)')
