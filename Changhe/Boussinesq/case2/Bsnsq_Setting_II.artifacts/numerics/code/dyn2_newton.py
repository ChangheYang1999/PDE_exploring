"""Newton-Krylov (GMRES, matrix-free) search for fixed points of the pseudo-time flow map Phi_T of dynres2.
A fixed point of Phi_T (T = n_sub ds) with the a0-normalization (c_l = (c-2)/2 each step) is a stationary state of the
discrete dynamic-rescaling scheme, i.e. a discrete approximation of a profile with beta = c_l, whether dynamically
stable or not. Unknowns: interior rows of A, B on the transport grid and the origin value G0 (a0 = 1 fixed); the
infinity row is extrapolated. Scaled unknowns u = D z (D = 1/(|z_init| + delta)) so that the far field does not
dominate the Krylov norm. Jacobian-vector products by finite differences of the flow map; damped Newton (halving).
"""
import sys, time, math, argparse, json
import numpy as np, torch
sys.path.insert(0, 'code')
from a2core import DT
from lm_solve import LMProblem, load_state, save_state, dev
from dynres2 import DynResGrid, grid_from_state, grid_gaussian


class FlowMap:
    def __init__(self, dyn, A0, B0, T, ds):
        self.dyn, self.T, self.ds = dyn, T, ds
        self.nsub = int(round(T / ds))
        self.Ni, self.Nj = dyn.Ni, dyn.Nj
        self.n_int = (self.Ni - 1) * self.Nj
        self.A_tmpl = A0.clone(); self.B_tmpl = B0.clone()

    def pack(self, A, B):
        return torch.cat([A[1:-1].reshape(-1), B[1:-1].reshape(-1), B[0, :1]])

    def unpack(self, z):
        A = self.A_tmpl.clone(); B = self.B_tmpl.clone()
        A[1:-1] = z[:self.n_int].reshape(self.Ni - 1, self.Nj); B[1:-1] = z[self.n_int:2 * self.n_int].reshape(self.Ni - 1, self.Nj)
        A[0] = 1.0; B[0] = z[-1]
        A[-1] = 3 * A[-2] - 3 * A[-3] + A[-4]; B[-1] = 3 * B[-2] - 3 * B[-3] + B[-4]
        return A, B

    def flow(self, z):
        A, B = self.unpack(z)
        dyn = self.dyn
        for _ in range(self.nsub):
            cG = dyn.fit(B); dyn.set_velocity(cG)
            A, B = dyn.step(A, B, self.ds)
        return self.pack(A, B)

    def F(self, z):
        return self.flow(z) - z


def gmres(matvec, b, m=60, tol=1e-3):
    """Right-preconditioner-free GMRES(m), single cycle. Returns x, relative residual history."""
    n = b.numel(); V = torch.zeros((m + 1, n), dtype=DT, device=dev); H = torch.zeros((m + 1, m), dtype=DT, device=dev)
    beta = float(b.norm()); V[0] = b / beta
    g = torch.zeros(m + 1, dtype=DT, device=dev); g[0] = beta
    hist = []
    for j in range(m):
        w = matvec(V[j])
        for i in range(j + 1):
            H[i, j] = torch.dot(w, V[i]); w = w - H[i, j] * V[i]
        H[j + 1, j] = w.norm()
        if float(H[j + 1, j]) > 1e-14 * beta:
            V[j + 1] = w / H[j + 1, j]
        y = torch.linalg.lstsq(H[:j + 2, :j + 1], g[:j + 2].unsqueeze(1)).solution.squeeze(1)
        res = float((H[:j + 2, :j + 1] @ y - g[:j + 2]).norm() / beta)
        hist.append(res)
        if res < tol or float(H[j + 1, j]) <= 1e-14 * beta:
            return (V[:j + 1].T @ y), hist
    return (V[:m].T @ y), hist


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--init', type=str, default=None); ap.add_argument('--grid_init', type=str, default=None, help='runs/<name>_grid.npz from dynres2')
    ap.add_argument('--Ni', type=int, default=512); ap.add_argument('--Nj', type=int, default=96)
    ap.add_argument('--N', type=int, default=112); ap.add_argument('--M', type=int, default=28)
    ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--beta', type=float, default=2.0)
    ap.add_argument('--T', type=float, default=0.5); ap.add_argument('--ds', type=float, default=0.01)
    ap.add_argument('--newton', type=int, default=12); ap.add_argument('--gmres_m', type=int, default=60); ap.add_argument('--gmres_tol', type=float, default=1e-3)
    ap.add_argument('--eps', type=float, default=1e-7); ap.add_argument('--delta', type=float, default=0.01)
    ap.add_argument('--kind', type=str, default='gauss'); ap.add_argument('--name', type=str, default='NK')
    args = ap.parse_args()
    log = open(f'runs/{args.name}.log', 'a')
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s, flush=True); log.write(s + '\n'); log.flush()
    P(f"# {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} dyn2_newton args: {vars(args)}")
    dyn = DynResGrid(args.Ni, args.Nj, args.N, args.M, args.L, args.beta, mode='a0')
    prob = LMProblem(args.N, args.M, args.L, args.beta, dyn.sigma_a, dyn.sigma_G, 1.0, 30.0, None, ov=2.0, mapname='t', Rw=30.0)
    if args.grid_init:
        g = np.load(args.grid_init); A = torch.tensor(g['A'], dtype=DT, device=dev); B = torch.tensor(g['B'], dtype=DT, device=dev)
    elif args.init:
        A, B = grid_from_state(dyn, load_state(args.init))
    else:
        A, B = grid_gaussian(dyn, args.beta, kind=args.kind)
    fm = FlowMap(dyn, A, B, args.T, args.ds)
    z = fm.pack(A, B)
    D = 1.0 / (z.abs() + args.delta * float(z.abs().max()))      # scaling of unknowns and residuals
    def Fs(u):                                                    # scaled residual as a function of scaled unknowns
        return D * fm.F(u / D)
    u = D * z
    t0 = time.time()
    Fu = Fs(u); nF = float(Fu.norm()); n0 = nF
    def report(tag, u, Fu):
        z = u / D; A, B = fm.unpack(z)
        cG = dyn.fit(B); dyn.set_velocity(cG); ca = dyn.fit(A)
        zz = prob.pack(ca, cG, dyn.c_l); dres = prob.diagnostics(zz)
        zx, zy, lam, w2min = dyn.axis_zeros()
        rate = float((fm.F(z) / args.T).abs().max()); rate_in = float(((fm.F(z) / args.T)[:fm.n_int].reshape(dyn.Ni - 1, dyn.Nj)[(dyn.r[1:-1] < 100)]).abs().max())
        P(f"{tag}: |Fs|={float(Fu.norm()):.4e} (rel {float(Fu.norm()) / n0:.3e}) max rate={rate:.3e} (r<100: {rate_in:.3e}) c_l={dyn.c_l:.6f} c={dyn.c:.5f} G0={float(B[0,0]):.5f} "
          f"jetG={(2 * dyn.c_l + 1) * float(B[0,0]) - 2:+.2e} LM RMS={dres['Fnorm']:.3e} Ra/RG={dres['Ra_max']:.2e}/{dres['RG_max']:.2e} x*={[round(v, 3) for v in zx[:2]]} "
          f"lam/(cl+2)={lam / (dyn.c_l + 2):.4f} yz={[round(v, 2) for v in zy[:3]]} w2min={w2min:.3f} t={time.time() - t0:.0f}s")
        return dres
    report("init", u, Fu)
    hist = []
    for it in range(args.newton):
        nu = float(u.norm())
        def matvec(v):
            e = args.eps * nu / float(v.norm())
            return (Fs(u + e * v) - Fu) / e
        du, gh = gmres(matvec, -Fu, m=args.gmres_m, tol=args.gmres_tol)
        P(f"  newton {it}: gmres {len(gh)} its, final rel res {gh[-1]:.3e}, |du|/|u|={float(du.norm()) / nu:.3e}")
        step = 1.0; accepted = False
        for _ in range(6):
            u_try = u + step * du; F_try = Fs(u_try); n_try = float(F_try.norm())
            if n_try < nF:
                u, Fu, nF = u_try, F_try, n_try; accepted = True; break
            step *= 0.5
        if not accepted:
            P("  no decrease along the Newton direction; stopping"); break
        dres = report(f"newton {it} (step {step})", u, Fu)
        hist.append(dict(it=it, Fs=nF, step=step, gmres=len(gh), c_l=dyn.c_l, RMS=dres['Fnorm'], Ra=dres['Ra_max'], RG=dres['RG_max']))
        z = u / D; A, B = fm.unpack(z)
        np.savez(f'runs/{args.name}_grid.npz', A=A.cpu().numpy(), B=B.cpu().numpy(), phi=dyn.phi.cpu().numpy(), th=dyn.th.cpu().numpy(),
                 c_l=dyn.c_l, c=dyn.c, beta_map=dyn.beta_map, L=dyn.L, e_a=dyn.e_a, e_G=dyn.e_G, hist=json.dumps(hist))
        ca = dyn.fit(A); cG = dyn.fit(B); save_state(f'runs/{args.name}.npz', prob, prob.pack(ca, cG, dyn.c_l), hist, extra=dict(vars(args), method='dyn2_newton'))
        if nF < 1e-10 * n0:
            break
    P("done")


if __name__ == '__main__':
    main()
