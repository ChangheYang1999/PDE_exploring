"""Arnoldi eigen-analysis of the linearized pseudo-time flow map Phi_T of dynres2 around a given state.
Eigenvalues mu of D Phi_T give growth rates lam = log|mu| / T of the rescaled dynamics (a0-normalization: c_l = (c-2)/2
each step, so the spatial-scaling mode is removed). The state need not be exactly stationary (the LM states are not), so
the result is indicative. Jacobian-vector products by finite differences of the (D-scaled) flow map; Arnoldi with
modified Gram-Schmidt; Ritz values and the spatial support of the leading Ritz vectors (energy by radial band)."""
import sys, time, math, argparse, json
import numpy as np, torch
sys.path.insert(0, 'code')
from a2core import DT
from lm_solve import load_state, dev
from dynres2 import DynResGrid, grid_from_state, grid_gaussian
from dyn2_newton import FlowMap


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--init', type=str, default=None); ap.add_argument('--grid_init', type=str, default=None)
    ap.add_argument('--Ni', type=int, default=512); ap.add_argument('--Nj', type=int, default=96)
    ap.add_argument('--N', type=int, default=112); ap.add_argument('--M', type=int, default=28)
    ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--beta', type=float, default=2.0)
    ap.add_argument('--T', type=float, default=0.5); ap.add_argument('--ds', type=float, default=0.01)
    ap.add_argument('--K', type=int, default=40); ap.add_argument('--eps', type=float, default=1e-7); ap.add_argument('--delta', type=float, default=0.01)
    ap.add_argument('--name', type=str, default='ARN'); ap.add_argument('--seed', type=int, default=0)
    args = ap.parse_args()
    log = open(f'runs/{args.name}.log', 'a')
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s, flush=True); log.write(s + '\n'); log.flush()
    P(f"# {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} dyn2_arnoldi args: {vars(args)}")
    dyn = DynResGrid(args.Ni, args.Nj, args.N, args.M, args.L, args.beta, mode='a0')
    if args.grid_init:
        g = np.load(args.grid_init); A = torch.tensor(g['A'], dtype=DT, device=dev); B = torch.tensor(g['B'], dtype=DT, device=dev)
    elif args.init:
        A, B = grid_from_state(dyn, load_state(args.init))
    else:
        A, B = grid_gaussian(dyn, args.beta)
    fm = FlowMap(dyn, A, B, args.T, args.ds)
    z = fm.pack(A, B); D = 1.0 / (z.abs() + args.delta * float(z.abs().max()))
    u = D * z
    Phi_u = D * fm.flow(u / D)
    nu = float(u.norm())
    def jv(v):
        e = args.eps * nu / float(v.norm())
        return (D * fm.flow((u + e * v) / D) - Phi_u) / e
    torch.manual_seed(args.seed)
    K = args.K; n = u.numel()
    V = torch.zeros((K + 1, n), dtype=DT, device=dev); H = torch.zeros((K + 1, K), dtype=DT, device=dev)
    v0 = torch.randn(n, dtype=DT, device=dev); V[0] = v0 / v0.norm()
    t0 = time.time()
    for j in range(K):
        w = jv(V[j])
        for i in range(j + 1):
            H[i, j] = torch.dot(w, V[i]); w = w - H[i, j] * V[i]
        H[j + 1, j] = w.norm(); V[j + 1] = w / H[j + 1, j]
        if (j + 1) % 10 == 0 or j == K - 1:
            ev = np.linalg.eigvals(H[:j + 1, :j + 1].cpu().numpy())
            idx = np.argsort(-np.abs(ev))
            P(f"  Arnoldi {j + 1}: leading Ritz |mu| and growth rates lam = log|mu|/T: " +
              ", ".join(f"{abs(ev[i]):.3f}({math.log(max(abs(ev[i]), 1e-300)) / args.T:+.2f}{'c' if abs(ev[i].imag) > 1e-6 else ''})" for i in idx[:8]) + f"  t={time.time() - t0:.0f}s")
    Hk = H[:K, :K].cpu().numpy(); ev, Y = np.linalg.eig(Hk)
    idx = np.argsort(-np.abs(ev))
    P("Leading Ritz pairs (|mu|, arg, growth rate lam) and support of the Ritz vector (fraction of squared norm by radial band, A-part / B-part):")
    r = dyn.r[1:-1].cpu().numpy(); bands = [(0, 1), (1, 5), (5, 12), (12, 15), (15, 30), (30, 100), (100, 1e4), (1e4, 1e12)]
    out = []
    for i in idx[:6]:
        y = torch.tensor(np.real(Y[:, i]), dtype=DT, device=dev)
        vec = (V[:K].T @ y); vec = vec / vec.norm()
        vz = vec / D                                        # back to unscaled fields
        a_part = vz[:fm.n_int].reshape(dyn.Ni - 1, dyn.Nj).abs() ** 2; b_part = vz[fm.n_int:2 * fm.n_int].reshape(dyn.Ni - 1, dyn.Nj).abs() ** 2
        tot = float(a_part.sum() + b_part.sum())
        fr = []
        for lo, hi in bands:
            mk = torch.tensor((r >= lo) & (r < hi), device=dev)
            fr.append((float(a_part[mk].sum() / tot), float(b_part[mk].sum() / tot)))
        lam = math.log(abs(ev[i])) / args.T
        P(f"  |mu|={abs(ev[i]):.4f} arg={np.angle(ev[i]):+.3f} lam={lam:+.3f}: " + " ".join(f"[{lo:g},{hi:g}):{fa:.2f}/{fb:.2f}" for (lo, hi), (fa, fb) in zip(bands, fr)))
        out.append(dict(mu=abs(ev[i]), arg=float(np.angle(ev[i])), lam=lam, bands=fr))
    json.dump(dict(args=vars(args), ritz=out, all_ritz_abs=sorted([abs(e) for e in ev], reverse=True)), open(f'runs/{args.name}.json', 'w'))
    P("done")


if __name__ == '__main__':
    main()
