"""
Lead's request 15:09Z item 4 (weaker-variant exploration, separately labelled): unforced solve with c_l free in a class
that allows a C^{1,alpha} origin term.  Representation

    b(r, theta) = b_s(r, theta) + C s(r)^(d-1) ,      s(r) = r / sqrt(L^2 + r^2),

so that rho = y w b contains the explicit non-smooth term  C y w s^(d-1) ~ C a r^d sin(theta)  near 0 (d > 1 free) and the
term stays bounded at infinity.  Unknowns: b_s on the grid, c_l, C, d.  Extra rows (the smooth part is smooth to first
order at the centre, in the map r ~ (1+t)):  d/dt bhat_s,0 (t=-1) = 0  and  d/dt bhat_s,1 (t=-1) = 0  (no linear-in-r term
in the sin(theta) and sin(3 theta) modes of the smooth part).  The whole b (smooth + explicit term) is pushed through the
standard pipeline (fields, residual); the Jacobian columns for C and d are finite differences of the full system.
Newton on the square system of size (N+1)M + 3.
"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3

torch.set_default_dtype(torch.float64)
dev = 'cuda'


class NS:
    def __init__(self, mdl, fixcl=False):
        self.mdl = mdl; self.fixcl = fixcl
        rad = mdl.rad
        self.s = torch.sqrt(rad.s2R)                           # r/sqrt(L^2 + r^2) on Radau nodes
        # d/dt at t = -1 of the Radau interpolant: first row of DR
        self.D0 = rad.DR[0, :]
        self.A_EE = mdl.ang.A['EE']

    def b_full(self, bs, C, d):
        return bs + C * (self.s ** (d - 1))[:, None]

    def system(self, bs, cl, C, d, gauge_value):
        mdl = self.mdl
        mdl.set_gamma(1.0 / cl)
        b = self.b_full(bs, C, d)
        F0, E, flds = mdl.system(b, cl, gauge_value=gauge_value)           # (N+1)M + 1 rows: continuity, identity, interior, gauge
        bhat_s = bs @ self.A_EE.T                                          # (N+1, M) mode coefficients of the smooth part
        r1 = (self.D0 @ bhat_s[:, 0])
        r2 = (self.D0 @ bhat_s[:, 1])
        if self.fixcl:
            return torch.cat([F0, r1.unsqueeze(0)]), E, flds              # (N+1)M + 2 rows; unknowns (bs, C, d)
        return torch.cat([F0, torch.stack([r1, r2])]), E, flds

    def newton(self, bs, cl, C, d, gauge_value, maxit=60, tol=1e-11, log=None):
        mdl = self.mdl; N, M = mdl.N, mdl.M; nb = (N + 1) * M
        F, E, flds = self.system(bs, cl, C, d, gauge_value); nF = F.abs().max().item()
        for it in range(maxit):
            # Jacobian: b-part and c_l column from the model (couple_gamma handles gamma), extra rows by FD, C and d columns by FD
            Jb = mdl.jacobian(self.b_full(bs, C, d), cl, flds)             # (nb+1, nb+1) w.r.t. (b, c_l) at gamma = 1/cl
            if self.fixcl:
                J = torch.zeros(nb + 2, nb + 2, device=dev)
                J[:nb + 1, :nb] = Jb[:, :nb]
                row = torch.outer(self.D0, self.A_EE[0, :]); J[nb + 1, :nb] = row.reshape(-1)
                for j, (dC, dd) in enumerate([(1e-6, 0.0), (0.0, 1e-6)]):
                    Fp, _, _ = self.system(bs, cl, C + dC, d + dd, gauge_value)
                    Fm, _, _ = self.system(bs, cl, C - dC, d - dd, gauge_value)
                    J[:, nb + j] = (Fp - Fm) / (2 * (dC + dd))
                du = torch.linalg.solve(J, -F)
                du = torch.cat([du[:nb], torch.zeros(1, device=dev), du[nb:]])   # insert zero c_l step
            else:
                J = torch.zeros(nb + 3, nb + 3, device=dev)
                J[:nb + 1, :nb + 1] = Jb                                       # d/d(bs) = d/d(b) for the first nb+1 rows
                for k in (0, 1):
                    row = torch.zeros(N + 1, M, device=dev)
                    row += torch.outer(self.D0, self.A_EE[k, :])
                    J[nb + 1 + k, :nb] = row.reshape(-1)
                for j, (dC, dd) in enumerate([(1e-6, 0.0), (0.0, 1e-6)]):
                    Fp, _, _ = self.system(bs, cl, C + dC, d + dd, gauge_value)
                    Fm, _, _ = self.system(bs, cl, C - dC, d - dd, gauge_value)
                    J[:, nb + 1 + j] = (Fp - Fm) / (2 * (dC + dd))
                mdl.set_gamma(1.0 / cl)
                du = torch.linalg.solve(J, -F)
            lam = 1.0
            for _ in range(25):
                bs_n = bs + lam * du[:nb].reshape(N + 1, M); cl_n = cl + lam * du[nb].item()
                C_n = C + lam * du[nb + 1].item(); d_n = d + lam * du[nb + 2].item()
                if d_n <= 1.01 or cl_n <= 1.0:
                    lam *= 0.5; continue
                Fn, En, fn = self.system(bs_n, cl_n, C_n, d_n, gauge_value); nFn = Fn.abs().max().item()
                if nFn < (1 - 1e-4 * lam) * nF or not math.isfinite(nF):
                    break
                lam *= 0.5
            msg = f"  ns-newton it {it}: |F| {nF:.3e} -> {nFn:.3e} lam={lam:.3g} cl={cl_n:.8f} C={C_n:+.6f} d={d_n:.6f} a0={bs_n[0,0].item()+0:.6f}"
            if log: log.write(msg + "\n"); log.flush()
            print(msg, flush=True)
            bs, cl, C, d, F, E, flds, nF = bs_n, cl_n, C_n, d_n, Fn, En, fn, nFn
            if nF < tol or lam < 1e-6: break
        return bs, cl, C, d, dict(F=F, E=E, flds=flds, nF=nF, J=J)


if __name__ == '__main__':
    start = sys.argv[1]; tag = sys.argv[2]; d0 = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5; C0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.1
    st = torch.load(start); N, M, L = st['N'], st['M'], st['L']
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# nonsmooth-term unforced solve from {start} d0={d0} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev, couple_gamma=True); mdl.gauge = 'inf'
    b = st['b'].to(dev); cl = st['cl']; beta = (mdl.rad.ext1_R @ b).mean().item()
    fixcl = (len(sys.argv) > 5 and sys.argv[5] == 'fixcl')
    ns = NS(mdl, fixcl=fixcl)
    bs, cl, C, d, info = ns.newton(b.clone(), cl, C0, d0, beta, maxit=100, log=log)
    flds = info['flds']; c = mdl.psi_xy0(flds).item(); bfull = ns.b_full(bs, C, d); a0 = bfull[0, 0].item()
    bhat = mdl.ang.to_coef(bfull, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0] * torch.cos(math.pi * torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L ** (1 - 1 / cl) * bK; Lcan = (K / a0) ** (cl / (cl - 1)) if K / a0 > 0 else float('nan')
    sv = torch.linalg.svdvals(info['J'])
    # between-node residual (unforced)
    tR = mdl.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(bfull, cl, flds, RR, TT); q = np.abs(ev['R']) / ev['Nf']
    og = [q[(RR >= lo) & (RR < hi)].max() for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e30)]]
    # Chebyshev tail of the smooth part
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(N + 1))); ck = np.linalg.lstsq(V, (bs @ ns.A_EE.T)[:, 0].cpu().numpy(), rcond=None)[0]
    msg = (f"RESULT {start}: |F|={info['nF']:.1e} cl={cl:.10f} c={c:+.10f} cl+c-1={cl+c-1:+.1e} a0={a0:.8f} C={C:+.6f} d={d:.6f} K={K:.5f} Lcan={Lcan:.5g} "
           f"smin={sv[-1].item():.1e} offgrid|R|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}] cheb tail of smooth part |c_N/2|={abs(ck[N//2]):.1e} |c_N-3|={abs(ck[N-3]):.1e}")
    print(msg, flush=True); log.write(msg + "\n")
    torch.save(dict(bs=bs.cpu(), b=bfull.cpu(), cl=cl, C=C, d=d, gamma=1 / cl, N=N, M=M, L=L, p=mdl.p, beta=beta, rep='nonsmooth-term'), f'runs/{tag}.pt')
