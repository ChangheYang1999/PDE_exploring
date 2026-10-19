"""Independent stationary solver for the lead's forward route (specification M22) -- independent verifier, 2026-10-18.

Problem: given p in (0,1), l = 1/p and a far-field datum A(theta), find rho on r < L with
    V.grad rho = rho,  V = l X + W[rho],  rho(L, theta) = L^p A(theta)   (inflow at r = L),
W = canonical once-subtracted Biot-Savart field of rho, with rho = r^p A beyond L (same convention as the lead's
pforward.py inflow g = A at r_max). Stationary states of the lead's evolution d_s g = V.grad g + p (W_r/r) g are
exactly the solutions of this problem.

Method (different from the lead's semi-Lagrangian time stepping with repeated interpolation of g):
  * rho is evaluated POINTWISE by the exact characteristic formula rho(X) = e^{-tau(X)} L^p A(theta_exit(X)),
    tau = exit time of the forward V-orbit from X through r = L (requires V_r > 0, checked);
    orbits are integrated with RK4 in t = log r (same number of steps for every point), V interpolated with
    tensor cubic Lagrange interpolation from a uniform (t, theta) grid that is filled from the Gauss-panel nodes
    by exact panel polynomial interpolation;
  * W from code/charsolve.py (dense per-mode exact radial Green's function on Gauss-Legendre panels, own code);
  * the fixed point rho = T(rho) is found by Anderson-accelerated Picard iteration;
  * diagnostics: c = psi_xy(0) and b = psi_yy(0) from the exact moment functionals, DV(0) = l I + [[-c,-b],[-b,c]],
    m1 = l - sqrt(c^2 + b^2); identities (S1) Q = pi (l-1)(l-m1) and (S2) int rho W_r r^{-p-3} = -l/(p+2) int A
    with their exact finite-L boundary terms.
No symmetry is imposed (V79: optional x-even projection, attribute xsym or FWD_XSYM=1).
"""
import numpy as np, torch, sys, math, json, time
sys.path.insert(0, 'code')
from charsolve import CharSolver, lagrange_eval

DT = torch.float64


def cubic_w(u):
    """Lagrange cubic weights for nodes -1, 0, 1, 2 at local coordinate u in [0, 1]."""
    return torch.stack([-u*(u-1)*(u-2)/6, (u+1)*(u-1)*(u-2)/2, -(u+1)*u*(u-2)/2, (u+1)*u*(u-1)/6], -1)


class FwdStat:
    def __init__(self, p, Afun, tmin=-12.0, tmax=10.0, ppu=4, q=8, nt=256, dti=0.01, nstep=800, dev='cuda',
                 mkeep=None):
        self.p = p; self.l = 1.0/p; self.Afun = Afun; self.dev = dev
        self.tmin, self.tmax = tmin, tmax
        P = int(round((tmax - tmin)*ppu))
        edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tmax, P + 1))])
        self.S = S = CharSolver(edges, q, nt, math.exp(tmin), dev, mkeep=mkeep)
        self.L = S.L; self.nt = nt; self.q = q
        self.r = S.r; self.th = S.th; self.R = S.R; self.TH = S.TH
        self.cs, self.sn = S.cs, S.sn
        self.t_nodes = torch.log(self.r)
        # uniform interpolation grid in t (fields at t < tmin are clamped to tmin: linear node regime)
        self.dti = dti
        Nu = int(round((tmax - tmin)/dti)) + 1
        self.tu = torch.linspace(tmin, tmax, Nu, dtype=DT, device=dev); self.Nu = Nu
        # interpolation matrix Gauss nodes -> uniform t (panel Lagrange; panels in t are uniform except panel 0)
        xg = np.polynomial.legendre.leggauss(q)[0]
        Nr = S.Nr
        Imat = np.zeros((Nu, Nr))
        tu = self.tu.cpu().numpy(); ru = np.exp(tu)
        for i, rr in enumerate(ru):
            k = np.searchsorted(edges, rr, side='right') - 1
            k = min(max(k, 1), len(edges) - 2)
            a, b = edges[k], edges[k + 1]
            x = 2*(rr - a)/(b - a) - 1
            Imat[i, k*q:(k + 1)*q] = lagrange_eval(xg, x)
        self.Imat = torch.tensor(Imat, dtype=DT, device=dev)
        self.nstep = nstep
        self.AL = torch.tensor(Afun(self.th.cpu().numpy()), dtype=DT, device=dev)
        # V74: arclength orbits by default if FWD_SMODE=1 in the environment (hs, nmax from FWD_HS, FWD_NMAX)
        import os
        self.smode = os.environ.get('FWD_SMODE', '0') == '1'
        self.hs = float(os.environ.get('FWD_HS', '0.03')); self.nmax = int(os.environ.get('FWD_NMAX', '6000'))
        # V79: optional x-even projection of the exit map (x-even data only); th_j = 2 pi j / nt, pi - th_j = th_(nt/2 - j)
        self.xsym = os.environ.get('FWD_XSYM', '0') == '1'
        self.xidx = torch.tensor((nt//2 - np.arange(nt)) % nt, device=dev)

    # ---------- velocity fields ----------
    def fields(self, rho):
        W1, W2 = self.S.velocity(rho, self.p)
        Wr = self.cs*W1 + self.sn*W2; Wt = -self.sn*W1 + self.cs*W2
        alpha = self.l + Wr/self.R; beta = Wt/self.R
        return alpha, beta, W1, W2

    def interp(self, Fu, t, th):
        """tensor cubic interpolation of Fu (Nu x nt) at points (t, th) (flat tensors)."""
        Nu, nt = self.Nu, self.nt
        it = (torch.clamp(t, self.tmin, self.tmax) - self.tmin)/self.dti
        i0 = torch.clamp(torch.floor(it).long(), 1, Nu - 3)
        u = it - i0
        jt = torch.remainder(th, 2*math.pi)/(2*math.pi/nt)
        j0 = torch.floor(jt).long()
        v = jt - j0
        wi = cubic_w(u); wj = cubic_w(v)
        out = torch.zeros_like(t)
        for a in range(4):
            ii = i0 - 1 + a
            for b in range(4):
                jj = torch.remainder(j0 - 1 + b, nt)
                out = out + wi[:, a]*wj[:, b]*Fu[ii, jj]
        return out

    def trace(self, alpha, beta, t0, th0, nstep=None):
        """RK4 in t from t0 to tmax for d th/dt = beta/alpha, d s/dt = 1/alpha. Returns exit angle and exit time."""
        nstep = self.nstep if nstep is None else nstep
        au = self.Imat @ alpha; bu = self.Imat @ beta
        if float(au.min()) <= 0:
            raise RuntimeError('V_r <= 0 on the interpolation grid: characteristic formula in t not valid')
        h = (self.tmax - t0)/nstep
        th = th0.clone(); s = torch.zeros_like(t0); t = t0.clone()
        def f(t, th):
            a = self.interp(au, t, th); b = self.interp(bu, t, th)
            return b/a, 1.0/a
        for n in range(nstep):
            k1t, k1s = f(t, th)
            k2t, k2s = f(t + h/2, th + h/2*k1t)
            k3t, k3s = f(t + h/2, th + h/2*k2t)
            k4t, k4s = f(t + h, th + h*k3t)
            th = th + h/6*(k1t + 2*k2t + 2*k3t + k4t)
            s = s + h/6*(k1s + 2*k2s + 2*k3s + k4s)
            t = t + h
        return th, s

    def trace_s(self, alpha, beta, t0, th0, hs=0.03, nmax=6000):
        """V74: orbits parametrised by arclength sigma in the (t, th) plane, d(t, th)/dsigma = (alpha, beta)/|(alpha, beta)|,
        ds/dsigma = 1/|(alpha, beta)|, so V_r <= 0 lobes are allowed (|V|/r > 0 required). RK4 with step hs; the step that
        crosses t = tmax is redone as one RK4 step in t from the old t to tmax (alpha > 0 there). Returns exit angle, exit
        time and the number of points that did not exit within nmax steps (their exit data are those of the last point)."""
        au = self.Imat @ alpha; bu = self.Imat @ beta
        if float(torch.sqrt(au**2 + bu**2).min()) <= 1e-8:
            raise RuntimeError('|V|/r = 0 on the interpolation grid')
        th = th0.clone(); s = torch.zeros_like(t0); t = t0.clone()
        done = t >= self.tmax
        def f(t, th):
            a = self.interp(au, t, th); b = self.interp(bu, t, th); w = torch.sqrt(a*a + b*b)
            return a/w, b/w, 1.0/w
        def ft(t, th):
            a = self.interp(au, t, th); b = self.interp(bu, t, th)
            return b/a, 1.0/a
        h = hs
        for n in range(nmax):
            idx = torch.nonzero(~done).squeeze(1)
            if idx.numel() == 0:
                break
            tt, hh, ss = t[idx], th[idx], s[idx]
            k1 = f(tt, hh)
            k2 = f(tt + h/2*k1[0], hh + h/2*k1[1])
            k3 = f(tt + h/2*k2[0], hh + h/2*k2[1])
            k4 = f(tt + h*k3[0], hh + h*k3[1])
            tn = tt + h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
            hn = hh + h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
            sn = ss + h/6*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
            cross = tn >= self.tmax
            if bool(cross.any()):
                ht = self.tmax - tt[cross]; tc = tt[cross]; thc = hh[cross]
                q1 = ft(tc, thc); q2 = ft(tc + ht/2, thc + ht/2*q1[0]); q3 = ft(tc + ht/2, thc + ht/2*q2[0])
                q4 = ft(tc + ht, thc + ht*q3[0])
                hn[cross] = thc + ht/6*(q1[0] + 2*q2[0] + 2*q3[0] + q4[0])
                sn[cross] = ss[cross] + ht/6*(q1[1] + 2*q2[1] + 2*q3[1] + q4[1])
                tn[cross] = self.tmax
            t[idx] = tn; th[idx] = hn; s[idx] = sn
            done[idx] = cross
        self.last_trace = dict(steps=n + 1, not_exited=int((~done).sum()), max_s=float(s.max()))
        return th, s, int((~done).sum())

    def trace_partial(self, alpha, beta, t0, th0, dT, nstep):
        """RK4 in t from t0 to t1 = min(t0 + dT, tmax). Returns t1, angle and elapsed time s."""
        au = self.Imat @ alpha; bu = self.Imat @ beta
        if float(au.min()) <= 0:
            raise RuntimeError('V_r <= 0 on the interpolation grid')
        t1 = torch.clamp(t0 + dT, max=self.tmax)
        h = (t1 - t0)/nstep
        th = th0.clone(); s = torch.zeros_like(t0); t = t0.clone()
        def f(t, th):
            a = self.interp(au, t, th); b = self.interp(bu, t, th)
            return b/a, 1.0/a
        for n in range(nstep):
            k1t, k1s = f(t, th)
            k2t, k2s = f(t + h/2, th + h/2*k1t)
            k3t, k3s = f(t + h/2, th + h/2*k2t)
            k4t, k4s = f(t + h, th + h*k3t)
            th = th + h/6*(k1t + 2*k2t + 2*k3t + k4t)
            s = s + h/6*(k1s + 2*k2s + 2*k3s + k4s)
            t = t + h
        return t1, th, s

    def T_partial(self, rho, dT=4.0, nstep=100):
        """finite advance in log r along the frozen-velocity characteristics: rho_new(X) = e^{-s} rho(t1, th1), with the
        inflow data where t1 = tmax. Fixed points are stationary states."""
        alpha, beta, W1, W2 = self.fields(rho)
        t0 = self.t_nodes[:, None].expand_as(self.R).reshape(-1)
        th0 = self.TH.reshape(-1)
        t1, th1, s = self.trace_partial(alpha, beta, t0, th0, dT, nstep)
        ru = self.Imat @ rho
        inner = self.interp(ru, t1, th1)
        Ae = torch.tensor(self.Afun(th1.cpu().numpy()), dtype=DT, device=self.dev)*self.L**self.p
        out = torch.where(t1 >= self.tmax - 1e-12, Ae, inner)
        return (torch.exp(-s)*out).reshape(self.R.shape), dict(minalpha=float(alpha.min()))

    def T(self, rho, nstep=None):
        alpha, beta, W1, W2 = self.fields(rho)
        t0 = self.t_nodes[:, None].expand_as(self.R).reshape(-1)
        th0 = self.TH.reshape(-1)
        if getattr(self, 'smode', False):          # V74: arclength orbits (V_r <= 0 lobes allowed)
            the, s, nbad = self.trace_s(alpha, beta, t0, th0, self.hs, self.nmax)
            if nbad > 0:
                raise RuntimeError('%d orbits did not exit within nmax steps' % nbad)
        else:
            the, s = self.trace(alpha, beta, t0, th0, nstep)
        Ae = torch.tensor(self.Afun(the.cpu().numpy()), dtype=DT, device=self.dev)
        rho_new = (torch.exp(-s)*self.L**self.p*Ae).reshape(self.R.shape)
        if getattr(self, 'xsym', False):          # V79: x-even projection rho(th) <- (rho(th) + rho(pi - th)) / 2
            rho_new = 0.5*(rho_new + rho_new[:, self.xidx])
        return rho_new, dict(minalpha=float(alpha.min()))

    def initial(self):
        r = self.R
        return (r**2/(1 + r**2))**(1 - self.p/2)*r**self.p*self.AL[None, :]

    def solve(self, rho=None, iters=60, tol=1e-11, m_and=6, beta_mix=1.0, verbose=True, nstep=None, dT=None, aerr=float('inf')):
        rho = self.initial() if rho is None else rho
        scale = self.R**self.p
        Xh, Fh = [], []
        hist = []
        best = (float('inf'), rho)
        last_ok = None; nfail = 0
        for k in range(iters):
            try:
                # dT: pseudo-time map (advance dT in log r along frozen characteristics) instead of the full exit map;
                # same fixed points, slower but stable where the full Picard map is not
                Tr, info = self.T(rho, nstep) if not dT else self.T_partial(rho, dT, max(50, int(round(25*dT))))
            except RuntimeError as e:
                # an extrapolated (Anderson) iterate left the admissible set (V_r <= 0 somewhere): restart from the last
                # admissible iterate with a Picard step damped by 2^-nfail and an empty history
                nfail += 1
                if last_ok is None or nfail > 6:
                    raise
                x0, F0 = last_ok
                Xh, Fh = [], []
                rho = (x0 + 0.5**(nfail - 1)*F0).reshape(self.R.shape)*scale
                hist.append(dict(it=k, restart=nfail, msg=str(e)[:30]))
                if verbose: print(json.dumps(hist[-1]), flush=True)
                continue
            F = ((Tr - rho)/scale).reshape(-1)
            x = (rho/scale).reshape(-1)
            last_ok = (x, F)
            err = float(F.abs().max())
            if err < best[0]:
                best = (err, rho)
            c, b = self.S.moments(rho, self.p)
            rec = dict(it=k, err=err, c=float(c), b=float(b), m1=self.l - math.hypot(float(c), float(b)),
                       minalpha=info['minalpha'])
            hist.append(rec)
            if verbose: print(json.dumps(rec), flush=True)
            if err < tol:
                break
            if err > aerr:                      # far from the fixed point: plain (damped) Picard, no Anderson extrapolation
                Xh, Fh = [], []
            Xh.append(x); Fh.append(F)
            if len(Xh) > m_and + 1:
                Xh.pop(0); Fh.pop(0)
            if len(Xh) >= 2:
                dX = torch.stack([Xh[i + 1] - Xh[i] for i in range(len(Xh) - 1)], 1)
                dF = torch.stack([Fh[i + 1] - Fh[i] for i in range(len(Fh) - 1)], 1)
                gam = torch.linalg.lstsq(dF, F[:, None]).solution[:, 0]
                xn = x + beta_mix*F - (dX + beta_mix*dF) @ gam
            else:
                xn = x + beta_mix*F
            rho = xn.reshape(self.R.shape)*scale
        # return the iterate with the smallest fixed-point defect (Anderson iterates are not monotone)
        return best[1], hist

    # ---------- diagnostics ----------
    def node(self, rho):
        c, b = self.S.moments(rho, self.p); c = float(c); b = float(b)
        M = np.array([[self.l - c, -b], [-b, self.l + c]])
        ev, evec = np.linalg.eigh(M)
        return dict(c=c, b=b, M=M.tolist(), m1=float(ev[0]), m2=float(ev[1]),
                    e1_deg=float(np.degrees(np.arctan2(evec[1, 0], evec[0, 0])) % 180))

    def identities(self, rho, m1):
        """(S1) Q = int rho W.grad phi (phi = r^-3 sin 3th) vs pi (l-1)(l-m1) and (S2) with finite-L boundary terms:
        int_{r<L} div(rho phi V) = flux at L (inner flux at r -> 0 neglected, O(r^(delta-1)))."""
        S = self.S; l, p = self.l, self.p
        _, _, W1, W2 = self.fields(rho)
        Wr = self.cs*W1 + self.sn*W2; Wt = -self.sn*W1 + self.cs*W2
        wA = (S.w*S.r)[:, None]*(2*math.pi/self.nt)          # area weights r dr dth
        th = self.TH; r = self.R
        phi = r**-3*torch.sin(3*th)
        gphi_r = -3*r**-4*torch.sin(3*th); gphi_t = 3*r**-4*torch.cos(3*th)   # (1/r) d_th phi
        Q = float(torch.sum(wA*rho*(Wr*gphi_r + Wt*gphi_t)))
        I = float(torch.sum(wA*rho*phi))
        # boundary flux at L: int rho phi V_r L dth with rho = L^p A, V_r = l L + W_r(L)
        L = self.L
        WrL = (S.ext_last[:, None]*Wr[-self.q:]).sum(0)
        dth = 2*math.pi/self.nt
        AL = self.AL
        flux1 = float(torch.sum(L**p*AL*L**-3*torch.sin(3*self.th)*(l*L + WrL)*L)*dth)
        # (1 - l) I + Q = flux1
        S2 = float(torch.sum(wA*rho*Wr*r**(-p - 3)))
        flux2 = float(torch.sum(L**p*AL*L**(-p - 2)*(l*L + WrL)*L)*dth)
        # -(p+2) S2 = flux2
        return dict(c_from_I=I/math.pi, Q=Q, Q_pred=math.pi*(l - 1)*(l - m1), S1_defect=(1 - l)*I + Q - flux1,
                    flux1=flux1, S2=S2, S2_pred_inf=-l/(p + 2)*float(torch.sum(AL)*dth),
                    S2_defect=-(p + 2)*S2 - flux2, flux2=flux2)
