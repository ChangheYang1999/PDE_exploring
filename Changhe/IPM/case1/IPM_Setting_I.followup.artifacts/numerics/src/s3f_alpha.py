"""SPEC S3 (f): first-order costs on a state, from the dense collocation Jacobian J (rows Ehat + identity, columns b nodes + c_l):
   alpha_cl  = 1 / |J^-T e_cl|          least residual change (2-norm of the row vector) per unit change of c_l,
   alpha_B3  = 1 / |J^-T grad_z B_3|    least residual change per natural unit of B_3 (c_l free),
   alpha_B3|cl = the same with the c_l column removed (c_l held fixed),
plus the deflated versions (the k softest singular triplets of J removed) and the overlaps (v_i . grad B_3) of the softest right
vectors with grad B_3.  grad_b B_3 by central differences of the lead's b3core (ibp and orig forms) along the axis footprint
(delta w, delta w', delta w'') of each unit b-perturbation (linear in b at fixed c_l); the c_l entry by central differences in
c_l.  Norms: node values (rows Ehat, columns b) unless --scaled (then the S3 (a) grid-L2 scaling of src/s3_svd.py).
Usage: python3 src/s3f_alpha.py runs/state.npz tag [ksoft=10] [eps=1e-6]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '../lead/b3_functional/b3infl')
import numpy as np, torch, ipm_newton as ipn
import b3core
from s3_svd import cc_weights01

LANE = '.'


def axis_tables(model, cl):
    """Fixed tables for the axis map: Lagrange matrix at the log grid and the geometric factors (torch)."""
    k = 1.0 / cl; L = model.L
    xs = np.geomspace(7.7e-4, 60.0, 5500)
    q = model.q_of_r(xs, cl)
    Pq = torch.tensor(ipn.interp_matrix(model.qpsi_np, q, model.wqpsi_np), device=model.dev)       # (X, Npsi+1)
    u2 = (xs / L) ** 2; op = 1 + u2
    T = lambda a: torch.tensor(np.asarray(a, float), device=model.dev)
    v = op ** ((k - 1) / 2); vp = (k - 1) * xs / L ** 2 * op ** ((k - 3) / 2)
    vpp = (k - 1) / L ** 2 * op ** ((k - 3) / 2) + (k - 1) * (k - 3) * xs ** 2 / L ** 4 * op ** ((k - 5) / 2)
    qp = (1 - k) * xs / L ** 2 * op ** (-(3 - k) / 2)
    qpp = (1 - k) / L ** 2 * op ** (-(3 - k) / 2) - (1 - k) * (3 - k) * xs ** 2 / L ** 4 * op ** (-(5 - k) / 2)
    return dict(xs=xs, Pq=Pq, x=T(xs), v=T(v), vp=T(vp), vpp=T(vpp), qp=T(qp), qpp=T(qpp), cl=cl)


def axis_from_psit(model, tab, psit):
    """psit: (..., N+1, K) mode tables -> f = x v sum nu psit_nu(q(x)) and its first two x-derivatives (..., X).
    w = c_l x - f, w' = c_l - f', w'' = -f''."""
    Dq = model.Dqpsi
    psq = torch.einsum('ij,...jm->...im', Dq, psit); psqq = torch.einsum('ij,...jm->...im', Dq, psq)
    nf = model.nf
    Ps = torch.einsum('xj,...jm,m->...x', tab['Pq'], psit, nf)
    Psq = torch.einsum('xj,...jm,m->...x', tab['Pq'], psq, nf)
    Psqq = torch.einsum('xj,...jm,m->...x', tab['Pq'], psqq, nf)
    x, v, vp, vpp, qp, qpp = tab['x'], tab['v'], tab['vp'], tab['vpp'], tab['qp'], tab['qpp']
    f = x * v * Ps
    fp = v * Ps + x * vp * Ps + x * v * Psq * qp
    fpp = 2 * vp * Ps + 2 * v * Psq * qp + x * vpp * Ps + 2 * x * vp * Psq * qp + x * v * Psqq * qp ** 2 + x * v * Psq * qpp
    return f, fp, fpp


def main():
    path, tag = sys.argv[1], sys.argv[2]
    ksoft = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    eps_rel = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-6
    model, x, d = ipn.load_state(path); b, cl = model.unpack(x); clf = float(cl)
    N, M = model.N, model.M; n = N * M + 1
    t0 = time.time()
    J = model.jacobian(x); F = model.F(x)
    print(f'J assembled ({time.time()-t0:.0f}s); |F|_2 {F.norm().item():.3e} |F|_inf {F.abs().max().item():.3e}', flush=True)
    # ---- base axis data and B_3
    tab = axis_tables(model, clf)
    g = model.geom(torch.tensor(clf, device=model.dev)); fl = model.fields(b, torch.tensor(clf, device=model.dev), g)
    f0, fp0, fpp0 = axis_from_psit(model, tab, fl['psit_n'])
    xs = tab['xs']; w0 = clf * xs - f0.cpu().numpy(); wp0 = clf - fp0.cpu().numpy(); wpp0 = -fpp0.cpu().numpy()
    Bo0, Bi0, dd = b3core.b3_one(xs, w0, wp0, wpp0, clf, both=True)
    print(f'base B_3: orig {Bo0:.5f} ibp {Bi0:.5f}  x* {dd["xs"]:.6f}', flush=True)
    # ---- axis footprints of the unit b-perturbations (linear in b at fixed c_l): batched fields
    t1 = time.time()
    A = torch.zeros(3, n - 1, len(xs), device=model.dev)
    base_psit = fl['psit_n']
    batch = 256
    for start in range(0, n - 1, batch):
        idx = torch.arange(start, min(start + batch, n - 1), device=model.dev); B = idx.numel()
        Eb = torch.zeros(B, N + 1, M, device=model.dev)
        Eb[torch.arange(B, device=model.dev), idx // M + 1, idx % M] = 1.0
        flb = model.fields(b[None] + Eb, torch.tensor(clf, device=model.dev), g)
        fB, fpB, fppB = axis_from_psit(model, tab, flb['psit_n'])
        A[0, start:start + B] = -(fB - f0[None]); A[1, start:start + B] = -(fpB - fp0[None]); A[2, start:start + B] = -(fppB - fpp0[None])
    A = A.cpu().numpy()
    print(f'axis footprints of {n-1} columns ({time.time()-t1:.0f}s)', flush=True)
    # ---- grad B_3 by central differences along each footprint (ibp and orig), step eps_rel * |w| scale
    t2 = time.time()
    grad_i = np.zeros(n); grad_o = np.zeros(n); lin_check = []
    wscale = np.max(np.abs(w0))
    for j in range(n - 1):
        dw, dwp, dwpp = A[0, j], A[1, j], A[2, j]
        amp = np.max(np.abs(dw)) + 1e-300
        e = eps_rel * wscale / amp
        Bop, Bip, _ = b3core.b3_one(xs, w0 + e * dw, wp0 + e * dwp, wpp0 + e * dwpp, clf, both=True)
        Bom, Bim, _ = b3core.b3_one(xs, w0 - e * dw, wp0 - e * dwp, wpp0 - e * dwpp, clf, both=True)
        grad_i[j] = (Bip - Bim) / (2 * e); grad_o[j] = (Bop - Bom) / (2 * e)
        if j % 977 == 0:
            e2 = e / 2
            Bip2, _ = b3core.b3_one(xs, w0 + e2 * dw, wp0 + e2 * dwp, wpp0 + e2 * dwpp, clf, both=False), None
            lin_check.append((j, float(grad_i[j]), float((b3core.b3_one(xs, w0 + e2 * dw, wp0 + e2 * dwp, wpp0 + e2 * dwpp, clf, both=True)[1] - b3core.b3_one(xs, w0 - e2 * dw, wp0 - e2 * dwp, wpp0 - e2 * dwpp, clf, both=True)[1]) / (2 * e2))))
        if j % 1000 == 0: print(f'   grad B_3 column {j}/{n-1} ({time.time()-t2:.0f}s)', flush=True)
    # c_l entry: B_3(c_l +- h) at fixed b (w changes through c_l x, k in the geometry, A and p_3 in the functional)
    h = 1e-5
    vals = []
    for s_ in (+1, -1):
        clh = clf + s_ * h; tabh = axis_tables(model, clh)
        gh = model.geom(torch.tensor(clh, device=model.dev)); flh = model.fields(b, torch.tensor(clh, device=model.dev), gh)
        fh, fph, fpph = axis_from_psit(model, tabh, flh['psit_n'])
        Boh, Bih, _ = b3core.b3_one(xs, clh * xs - fh.cpu().numpy(), clh - fph.cpu().numpy(), -fpph.cpu().numpy(), clh, both=True)
        vals.append((Boh, Bih))
    grad_o[-1] = (vals[0][0] - vals[1][0]) / (2 * h); grad_i[-1] = (vals[0][1] - vals[1][1]) / (2 * h)
    print(f'grad B_3 done ({time.time()-t2:.0f}s): |grad_ibp| {np.linalg.norm(grad_i):.3e} (c_l entry {grad_i[-1]:+.3e}), |grad_orig| {np.linalg.norm(grad_o):.3e}; linearity checks {lin_check}', flush=True)
    # ---- alpha values
    LU = torch.linalg.lu_factor(J)
    def JmT(vec):
        return torch.linalg.lu_solve(*LU, torch.tensor(vec, device=model.dev)[:, None], adjoint=True)[:, 0]
    e_cl = np.zeros(n); e_cl[-1] = 1.0
    y_cl = JmT(e_cl); y_i = JmT(grad_i); y_o = JmT(grad_o)
    out = dict(tag=tag, N=N, M=M, beta=model.beta, n=n, c_l=clf, F2=float(F.norm()), Finf=float(F.abs().max()),
               B3_orig=float(Bo0), B3_ibp=float(Bi0), grad_norm_ibp=float(np.linalg.norm(grad_i)), grad_norm_orig=float(np.linalg.norm(grad_o)),
               grad_cl_ibp=float(grad_i[-1]), grad_cl_orig=float(grad_o[-1]),
               alpha_cl=float(1 / y_cl.norm()), alpha_B3_ibp=float(1 / y_i.norm()), alpha_B3_orig=float(1 / y_o.norm()), linearity=lin_check)
    # c_l fixed: drop the identity row and the c_l column
    Jb = J[:n - 1, :n - 1]; LUb = torch.linalg.lu_factor(Jb)
    yb = torch.linalg.lu_solve(*LUb, torch.tensor(grad_i[:-1], device=model.dev)[:, None], adjoint=True)[:, 0]
    out['alpha_B3_ibp_clfixed'] = float(1 / yb.norm())
    # softest triplets and deflation
    V = torch.randn(n, ksoft + 4, device=model.dev)
    for _ in range(40):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y); V, _ = torch.linalg.qr(Z)
    JV = J @ V; Uk, sk, Wk = torch.linalg.svd(JV, full_matrices=False); Vk = V @ Wk.T; idx = torch.argsort(sk)
    sk = sk[idx]; Vk = Vk[:, idx]; Uk = Uk[:, idx]
    gi = torch.tensor(grad_i, device=model.dev); go = torch.tensor(grad_o, device=model.dev); ecl = torch.tensor(e_cl, device=model.dev)
    soft = []
    for i in range(ksoft):
        soft.append(dict(sigma=float(sk[i]), v_dot_gradB3_ibp=float(Vk[:, i] @ gi), v_dot_gradB3_orig=float(Vk[:, i] @ go), v_cl=float(Vk[-1, i])))
    out['soft'] = soft
    def deflated_alpha(y, gvec, k):
        yd = y.clone()
        for i in range(k):
            yd = yd - ((Vk[:, i] @ gvec) / sk[i]) * Uk[:, i]
        return float(1 / yd.norm())
    out['alpha_cl_deflated'] = {k: deflated_alpha(y_cl, ecl, k) for k in (3, 5, ksoft)}
    out['alpha_B3_ibp_deflated'] = {k: deflated_alpha(y_i, gi, k) for k in (3, 5, ksoft)}
    out['alpha_B3_orig_deflated'] = {k: deflated_alpha(y_o, go, k) for k in (3, 5, ksoft)}
    json.dump(out, open(f'{LANE}/runs/s3f_{tag}.json', 'w'), indent=1)
    np.savez(f'{LANE}/runs/s3f_{tag}_grad.npz', grad_ibp=grad_i, grad_orig=grad_o)
    print(json.dumps({k_: v_ for k_, v_ in out.items() if k_ not in ('soft', 'linearity')}, indent=1))
    for s_ in soft: print('  soft', s_)


if __name__ == '__main__':
    main()
