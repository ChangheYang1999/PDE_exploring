"""
charac.py -- characteristic-integrated check (second method, independent of the collocation residual).

For a saved state (b, c_l), W = c_l X + U[rho].  Backward characteristics dX/dtau = -W(X) from sample points X in the
open first quadrant are integrated with RK4 (fixed step) until |X| < delta; near the source W = (A x, y) + O(r^2) with
A = 2c_l - 1 when c_l + c = 1, and eta(X) = lim e^tau y(tau) = e^(tau_delta) y(tau_delta) (1 + O(delta^2)).  Any C^1
solution of W.grad rho = rho that is odd in y with rho_y(0) = a_0 equals a_0 eta on the basin of the source, so
    D(X) := rho(X) - a_0 eta(X)
is a characteristic-integrated residual: zero for an exact solution; for a forced state it is nonzero.  Trajectories
that do not reach |X| < delta within tau_max are reported (they would indicate another equilibrium or an escape).

Velocity evaluation at arbitrary points is a torch re-implementation of IPM3.evaluate (barycentric interpolation of the
mode functions Psi~_n(t) and of b), vectorised over points.
"""
import math
import numpy as np
import torch
import ipm3

torch.set_default_dtype(torch.float64)


class FieldEval:
    def __init__(self, mdl, b, cl, flds):
        self.mdl, self.cl = mdl, cl
        rad = mdl.rad
        self.dev = mdl.dev
        self.tR = rad.tR; self.wR = torch.tensor(rad.wR_np, device=self.dev)
        self.tL = rad.tL; self.wL = torch.tensor(rad.wL_np, device=self.dev)
        self.bhat = mdl.ang.to_coef(b, 'EE')               # (N+1, M) cos(2k th) coefficients of b on Radau
        self.kk = torch.tensor(mdl.ang.n_EE, dtype=torch.float64, device=self.dev)   # 2k
        self.PsiC = flds['PsiC']                           # (N+1, M2) Lobatto
        self.PsiC_t = rad.DL @ self.PsiC
        self.nf = mdl.nf
        self.gamma, self.p, self.L = mdl.gamma, mdl.p, mdl.L
        self.a0 = b[0, 0].item()

    def bary(self, tn, wn, tq):
        """(P, N+1) barycentric interpolation matrix from nodes tn (weights wn) to query points tq."""
        d = tq[:, None] - tn[None, :]
        hit = d.abs() < 1e-14
        d = torch.where(hit, torch.ones_like(d), d)
        W = wn[None, :] / d
        W = torch.where(hit.any(1, keepdim=True), hit.to(W.dtype), W)
        return W / W.sum(1, keepdim=True)

    def t_of_r(self, r):
        """inverse map by bisection in torch (r > 0)."""
        lo = -torch.ones_like(r); hi = torch.ones_like(r) - 1e-16
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            rm = self.L * (1 + mid) / (1 - mid) ** self.p
            big = rm > r
            hi = torch.where(big, mid, hi); lo = torch.where(big, lo, mid)
        return 0.5 * (lo + hi)

    def fields_at(self, X):
        """X: (P, 2) points (any quadrant).  Returns rho, U1, U2 at X (parities applied)."""
        x, y = X[:, 0], X[:, 1]
        sx = torch.sign(x); sy = torch.sign(y)
        xa, ya = x.abs(), y.abs()
        r = torch.sqrt(xa ** 2 + ya ** 2).clamp_min(1e-300)
        th = torch.atan2(ya, xa)
        t = self.t_of_r(r)
        PR = self.bary(self.tR, self.wR, t); PL = self.bary(self.tL, self.wL, t)
        Q = (1 - t) + self.p * (1 + t); g = (1 - t ** 2) / Q
        s2 = self.mdl.rad.s2_of_t(t); om = (self.gamma - 1) * s2; w = self.mdl.rad.w_of_t(t, self.gamma)
        C = torch.cos(th[:, None] * self.kk[None, :])
        bp = ((PR @ self.bhat) * C).sum(1)
        Sn = torch.sin(th[:, None] * self.nf[None, :]); Cn = torch.cos(th[:, None] * self.nf[None, :])
        Psi = ((PL @ self.PsiC) * Sn).sum(1)
        rPsi_r = g * ((PL @ self.PsiC_t) * Sn).sum(1)
        Psi_th = ((PL @ self.PsiC) * self.nf[None, :] * Cn).sum(1)
        cos, sin = torch.cos(th), torch.sin(th)
        G = (2 + om) * Psi + rPsi_r
        U1 = r * w * (-(sin * G + cos * Psi_th))
        U2 = r * w * (cos * G - sin * Psi_th)
        rho = r * w * sin * bp
        # parities: rho even in x odd in y; U1 odd in x even in y; U2 even in x odd in y
        return rho * sy, U1 * sx, U2 * sy

    def W(self, X):
        rho, U1, U2 = self.fields_at(X)
        return torch.stack([self.cl * X[:, 0] + U1, self.cl * X[:, 1] + U2], 1)

    def eta(self, X0, delta=1e-3, dtau=5e-3, tau_max=60.0):
        """Backward characteristics from X0 (P, 2): returns eta (P,), tau at exit, and a flag for trajectories that did
        not reach |X| < delta."""
        X = X0.clone(); P = X.shape[0]
        tau = torch.zeros(P, device=X.device)
        done = torch.zeros(P, dtype=torch.bool, device=X.device)
        eta = torch.full((P,), float('nan'), device=X.device)
        nsteps = int(tau_max / dtau)
        for it in range(nsteps):
            act = ~done
            if not act.any():
                break
            Xa = X[act]
            k1 = -self.W(Xa); k2 = -self.W(Xa + 0.5 * dtau * k1); k3 = -self.W(Xa + 0.5 * dtau * k2); k4 = -self.W(Xa + dtau * k3)
            Xn = Xa + dtau / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            rn = Xn.norm(dim=1); ra = Xa.norm(dim=1)
            cross = rn < delta
            # exit time by log-linear interpolation of r in tau (r decays exponentially)
            frac = torch.where(cross, (torch.log(ra) - math.log(delta)) / (torch.log(ra) - torch.log(rn)).clamp_min(1e-300), torch.zeros_like(rn))
            Xe = Xa + frac[:, None] * (Xn - Xa)          # linear interpolation of the position (error O(dtau^2) in position)
            tau_e = tau[act] + frac * dtau
            idx = torch.nonzero(act).squeeze(1)
            ci = idx[cross]
            eta[ci] = torch.exp(tau_e[cross]) * Xe[cross, 1]
            done[ci] = True
            X[idx[~cross]] = Xn[~cross]
            tau[idx[~cross]] = tau[act][~cross] + dtau
        return eta, tau, ~done


def check_state(path, npts=400, delta=1e-3, dtau=5e-3, device='cuda', seed=0, rmin=1e-2, rmax=1e3):
    st = torch.load(path)
    mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=device)
    b = st['b'].to(device); cl = st['cl']; flds = mdl.fields(b)
    fe = FieldEval(mdl, b, cl, flds)
    gen = torch.Generator(device='cpu').manual_seed(seed)
    r = torch.exp(torch.rand(npts, generator=gen) * (math.log(rmax) - math.log(rmin)) + math.log(rmin)).to(device)
    th = (0.02 + 0.96 * torch.rand(npts, generator=gen)).to(device) * (math.pi / 2)
    X0 = torch.stack([r * torch.cos(th), r * torch.sin(th)], 1)
    rho0, _, _ = fe.fields_at(X0)
    eta, tau, fail = fe.eta(X0, delta=delta, dtau=dtau)
    D = rho0 - fe.a0 * eta
    rel = (D.abs() / rho0.abs()).cpu().numpy(); rr = r.cpu().numpy()
    out = dict(cl=cl, a0=fe.a0, nfail=int(fail.sum().item()), rel=rel, r=rr, th=th.cpu().numpy(), tau=tau.cpu().numpy(),
               mu=st.get('mu', None))
    return out


if __name__ == '__main__':
    import sys
    for path in sys.argv[1:]:
        for delta in [3e-3, 1e-3]:
            o = check_state(path, delta=delta)
            rel, rr = o['rel'], o['r']
            msg = f"{path}: cl={o['cl']:.8f} a0={o['a0']:.6f} mu={o['mu']} delta={delta}: failed trajectories {o['nfail']}/{len(rel)}; |rho - a0 eta|/|rho|: median {np.nanmedian(rel):.2e}, 90% {np.nanpercentile(rel, 90):.2e}, max {np.nanmax(rel):.2e}; by r: "
            for lo, hi in [(1e-2, 1e-1), (1e-1, 1), (1, 10), (10, 100), (100, 1e3)]:
                m = (rr >= lo) & (rr < hi)
                msg += f"[{lo:g},{hi:g}) max {np.nanmax(rel[m]) if m.any() else float('nan'):.1e} "
            print(msg, flush=True)
