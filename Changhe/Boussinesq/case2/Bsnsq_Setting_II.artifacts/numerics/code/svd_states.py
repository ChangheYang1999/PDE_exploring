"""Near-kernel / weak-direction analysis of the LM Jacobian at saved states with beta FREE (prompt Section 4: neutral
scaling directions, weak exponent directions, near-zero singular values). Prints the largest and 10 smallest singular
values, the beta-component and the field support of the 3 smallest singular vectors, the sensitivity of the residual to
beta (|J_beta| and d|F|^2/dbeta) and the effect of a unit step along the smallest singular vector on a, G, U and beta."""
import sys, numpy as np, torch, json
sys.path.insert(0, 'code')
from lm_solve import LMProblem, load_state, dev, DT
for path in sys.argv[1:]:
    d = load_state(path)
    N, M, L = int(d['N']), int(d['M']), float(d['L'])
    prob = LMProblem(N, M, L, float(d['beta_map']), float(d['sigma_a']), float(d['sigma_G']), float(d['a0_target']), 30.0, None, ov=2.0, mapname=str(d['mapname']), Rw=float(d['Rw']))
    z = prob.pack(torch.tensor(d['ca'], dtype=DT, device=dev), torch.tensor(d['cG'], dtype=DT, device=dev), float(d['beta']))
    F = prob.F(z); J = prob.jac(z)
    S = torch.linalg.svdvals(J).cpu().numpy()
    print(f"=== {path}: N={N} M={M} beta={float(d['beta'])}: J {tuple(J.shape)}, |F|={float(F.norm()):.4e}")
    print(f"  sv max {S[0]:.3e}; 10 smallest: " + " ".join(f"{v:.2e}" for v in S[-10:]) + f"; count sv < 1e-6 sv_max: {(S < 1e-6 * S[0]).sum()}, < 1e-4: {(S < 1e-4 * S[0]).sum()}")
    U_, S_, Vh = torch.linalg.svd(J, full_matrices=False)
    V = Vh.cpu().numpy(); n_a = sum(prob.na); n_G = sum(prob.nG)
    for j in range(1, 4):
        v = V[-j]
        print(f"  sv[-{j}]={S[-j]:.3e}: energy a {np.sum(v[:n_a]**2):.3f} G {np.sum(v[n_a:n_a+n_G]**2):.3f} beta {v[-1]**2:.3e}")
    # beta sensitivity
    Jb = J[:, -1]
    g = (J.T @ F).cpu().numpy()
    print(f"  |J_beta| = {float(Jb.norm()):.4e} (compare median column norm {float(torch.linalg.norm(J, dim=0).median()):.3e}); d|F|^2/dbeta = {2*g[-1]:+.4e}; |grad|F|^2| = {2*np.linalg.norm(g):.3e}")
    # projection of F onto the span of J (is the residual orthogonal to the tangent space? i.e., local minimum quality)
    coef = torch.linalg.lstsq(J, F.unsqueeze(1)).solution.squeeze(1)
    print(f"  |F - J (J^+ F)|/|F| = {float((F - J @ coef).norm() / F.norm()):.5f} (fraction of the residual outside the tangent space; 1 = exact local minimum)")
    # unit step along the smallest singular vector
    ca, cG, beta = prob.unpack(z); f0 = prob.model.fields(ca, cG, beta)
    v = torch.tensor(V[-1], dtype=DT, device=dev); ca1, cG1, b1 = prob.unpack(z + v); f1 = prob.model.fields(ca1, cG1, b1)
    print(f"  unit step along sv[-1]: max|da| {float((f1['a']-f0['a']).abs().max()):.3e} max|dG| {float((f1['G']-f0['G']).abs().max()):.3e} max|dU|/max|U| {float(torch.maximum((f1['U1']-f0['U1']).abs(), (f1['U2']-f0['U2']).abs()).max()/f0['U1'].abs().max()):.3e} dbeta {float(b1-beta):+.3e}; |F| changes {float(F.norm()):.4e} -> {float(prob.F(z+v).norm()):.4e}", flush=True)
