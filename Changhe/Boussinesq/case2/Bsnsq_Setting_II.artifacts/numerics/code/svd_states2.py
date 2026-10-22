"""Repairs requested in the analysis and by the verifier to the Jacobian analysis of code/svd_states.py:
 s_beta = ||(I - P_A) J_beta|| (distance of the beta column from the span A of the coefficient columns), its ratio to
 ||J_beta|| and to the median column norm; fixed-beta optimality via ||F - P_A F||/||F|| (coefficient columns only) and
 ||A^T F||/(||F|| max_j ||A_j||); full (a, G, beta) energy split of the three smallest singular vectors; unit-step velocity
 change relative to max(|U1|, |U2|)."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import LMProblem, load_state, dev, DT
for path in sys.argv[1:]:
    d = load_state(path)
    N, M, L = int(d['N']), int(d['M']), float(d['L'])
    prob = LMProblem(N, M, L, float(d['beta_map']), float(d['sigma_a']), float(d['sigma_G']), float(d['a0_target']), 30.0, None, ov=2.0, mapname=str(d['mapname']), Rw=30.0)
    z = prob.pack(torch.tensor(d['ca'], dtype=DT, device=dev), torch.tensor(d['cG'], dtype=DT, device=dev), float(d['beta']))
    F = prob.F(z); J = prob.jac(z)
    A = J[:, :-1]; Jb = J[:, -1]
    coef = torch.linalg.lstsq(A, Jb.unsqueeze(1)).solution.squeeze(1)
    s_beta = float((Jb - A @ coef).norm())
    colnorms = torch.linalg.norm(A, dim=0)
    cF = torch.linalg.lstsq(A, F.unsqueeze(1)).solution.squeeze(1)
    fracF = float((F - A @ cF).norm() / F.norm())
    gA = (A.T @ F); g_rel = float(gA.norm() / (F.norm() * colnorms.max()))
    U_, S_, Vh = torch.linalg.svd(J, full_matrices=False); S = S_.cpu().numpy(); V = Vh.cpu().numpy()
    n_a = sum(prob.na); n_G = sum(prob.nG)
    print(f"=== {path}: N={N} beta={float(d['beta'])} |F|={float(F.norm()):.4e}")
    print(f"  s_beta = ||(I-P_A) J_beta|| = {s_beta:.4e}; ||J_beta|| = {float(Jb.norm()):.3e}; s_beta/||J_beta|| = {s_beta/float(Jb.norm()):.3e}; median coefficient column norm {float(colnorms.median()):.3e}; sv_min(J) = {S[-1]:.3e}")
    for j in range(1, 4):
        v = V[-j]; print(f"  sv[-{j}] = {S[-j]:.3e}: energy a {np.sum(v[:n_a]**2):.4f}  G {np.sum(v[n_a:n_a+n_G]**2):.4f}  beta {v[-1]**2:.4f}")
    print(f"  fixed-beta optimality: ||F - P_A F||/||F|| = {fracF:.5f};  ||A^T F|| / (||F|| max||A_j||) = {g_rel:.3e}")
    ca, cG, beta = prob.unpack(z); f0 = prob.model.fields(ca, cG, beta)
    v = torch.tensor(V[-1], dtype=DT, device=dev); ca1, cG1, b1 = prob.unpack(z + v); f1 = prob.model.fields(ca1, cG1, b1)
    Umax = float(torch.maximum(f0['U1'].abs(), f0['U2'].abs()).max()); dU = float(torch.maximum((f1['U1']-f0['U1']).abs(), (f1['U2']-f0['U2']).abs()).max())
    print(f"  unit step along sv[-1]: max|dU| / max(|U1|,|U2|) = {dU/Umax:.3e}; dbeta = {float(b1-beta):+.3e}; |F| -> {float(prob.F(z+v).norm()):.4e}", flush=True)
