"""Gamma-slaved exit map and unprojected Newton-GMRES (notes of the lead analyst 2026-10-18T12:31Z (b), (c)).
Datum with movable zeros: A(th) = 4 sin^2((th - th_1)/2) sin^2((th - th_2)/2) exp(F(th))  (= cos^2 th e^F at th_1 = 90, th_2 = 270 deg), F free in
both parities (Fourier modes sin n th, cos n th, n = 1..K: x-even modes sin(odd n), cos(even n); x-odd modes cos(odd n), sin(even n)).
The zero angles are SLAVED to the current velocity: th_1, th_2 = exit angles of the two branches of the strong unstable manifold Gamma of the node
(forward orbits from (r = e^lr_g, th = 90 / 270 deg); the angular offset from Gamma decays like (r_g/r)^((m2 - m1)/m2) along the orbit, so the exit
angle is Gamma's to e^-20).  Then Ttilde(g) = T(g; F, p, th(g)) has no Gamma mismatch at any iterate (specification Theorems 3.2 / 3.13: in S^+ the zeros of A
are where Gamma reaches infinity), which removes the cusp mechanism of numerical record R19(f).
Newton-GMRES on R(g) = g - Ttilde(g) (matrix-free: J v = (R(g + e v) - R(g))/e), unprojected, with a backtracking line search on |R|; the Arnoldi
Hessenberg matrix gives Ritz / singular-value information about I - DTtilde on the Krylov space (upper bounds only).  Diagnostics per Newton
iterate: |R| (rms and max relative to row max), x-odd part of g (rms relative), DW(0) from the angular modes of W/r on the ring lr -12 (psi_yy(0) = -DW_12),
zero angles th_1, th_2, m1 (core-corrected moment), c.
"""
import sys, json, math, time, os
import numpy as np
import torch
sys.path.insert(0, 'code')
from pfwd_batch import PFwdB
torch.set_default_dtype(torch.float64)


class GammaMap:
    def __init__(self, Nr, Nth, lo, hi, p, F_even, F_odd=None, dt=0.01, dev='cuda', orbit_cap=3000, lr_g=-12.0):
        self.SB = PFwdB(Nr, Nth, lo, hi, p, dev=dev); S = self.SB.S; self.S = S; self.dev = dev
        self.p = float(p); self.pB = torch.tensor([self.p], device=dev); self.dt = float(dt); self.orbit_cap = int(orbit_cap); self.lr_g = float(lr_g)
        self.F_even = np.asarray(F_even, float); self.F_odd = np.zeros(0) if F_odd is None else np.asarray(F_odd, float)
        self.LR = S.lr[:, None].expand(Nr, Nth).reshape(1, -1).clone(); self.TH = S.th[None, :].expand(Nr, Nth).reshape(1, -1).clone()
        self.scale = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - self.p / 2))[:, None]
        j = torch.arange(Nth, device=dev); self.flip = torch.remainder(Nth // 2 - j, Nth)
        self.th12 = (math.pi / 2, 3 * math.pi / 2)

    def Fexp(self, t):
        F = torch.zeros_like(t)
        for j, a in enumerate(self.F_even):
            n = j + 1; F = F + float(a) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))          # x-even modes
        for j, a in enumerate(self.F_odd):
            n = j + 1; F = F + float(a) * (torch.cos(n * t) if n % 2 == 1 else torch.sin(n * t))          # x-odd modes
        return F

    def Afun(self, t, th12=None):
        th1, th2 = self.th12 if th12 is None else th12
        return 4.0 * torch.sin(0.5 * (t - th1)) ** 2 * torch.sin(0.5 * (t - th2)) ** 2 * torch.exp(self.Fexp(t))

    def velocity(self, g):
        rho = self.S.r[:, None] ** self.p * g
        Wr, Wt = self.SB.velocity(rho[None], self.pB)
        return Wr, Wt, rho

    def _fields(self, Wr, Wt):
        S, SB = self.S, self.SB
        ar = (1 / self.p) + Wr / S.r[None, :, None]; at = Wt / S.r[None, :, None]
        top = lambda F: F[:, -1:].expand(-1, 2, -1)
        arE = SB.extend(ar, top(ar)); atE = SB.extend(at, top(at)); Car = SB.prefilter(arE); Cat = SB.prefilter(atE)
        def rhs(l_, t_):
            ci = (l_ - S.lo) / S.d; cj = t_ / S.dth
            return SB.eval_bs(Car, arE, ci, cj), SB.eval_bs(Cat, atE, ci, cj)
        return rhs

    def _orbits(self, rhs, LR, TH, cap):
        S = self.S; Tt = torch.zeros_like(LR); live = LR < S.hi - 1e-12; dt = self.dt; it = 0
        while bool(live.any()) and it < cap:
            k1 = rhs(LR, TH); k2 = rhs(LR + 0.5 * dt * k1[0], TH + 0.5 * dt * k1[1]); k3 = rhs(LR + 0.5 * dt * k2[0], TH + 0.5 * dt * k2[1]); k4 = rhs(LR + dt * k3[0], TH + dt * k3[1])
            dl = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); dth = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            over = live & (LR + dl >= S.hi)
            frac = torch.where(over, (S.hi - LR) / torch.clamp(dl, min=1e-300), torch.ones_like(dl))
            LR = torch.where(live, LR + frac * dl, LR); TH = torch.where(live, TH + frac * dth, TH); Tt = torch.where(live, Tt + frac * dt, Tt)
            live = live & ~over; it += 1
        return LR, TH, Tt, live, it

    def gamma_angles(self, rhs):
        """exit angles of the two branches of the strong unstable manifold (forward orbits from (e^lr_g, 90 / 270 deg))."""
        LR = torch.full((1, 2), self.lr_g, device=self.dev); TH = torch.tensor([[math.pi / 2, 3 * math.pi / 2]], device=self.dev)
        LR, TH, Tt, live, it = self._orbits(rhs, LR, TH, 20000)
        th1 = float(torch.remainder(TH[0, 0], 2 * math.pi)); th2 = float(torch.remainder(TH[0, 1], 2 * math.pi))
        return th1, th2, bool(~live.any())

    def T(self, g, return_all=False):
        """Gamma-slaved exit map on g [Nr, Nth]."""
        S = self.S
        Wr, Wt, rho = self.velocity(g)
        rhs = self._fields(Wr, Wt)
        th1, th2, ok = self.gamma_angles(rhs)
        LR, TH, Tt, live, it = self._orbits(rhs, self.LR.clone(), self.TH.clone(), self.orbit_cap)
        Tg = (torch.exp(-Tt) * math.exp(self.p * S.hi) * self.Afun(TH, (th1, th2))).reshape(S.Nr, S.Nth) / S.r[:, None] ** self.p
        info = dict(th1_deg=math.degrees(th1), th2_deg=math.degrees(th2), gamma_ok=ok, orbit_its=it, unfinished=int(live.sum()))
        if return_all:
            return Tg, info, Wr, Wt, rho
        return Tg, info

    # ---------------------------------------------------------------- diagnostics
    def diag(self, g, Wr=None, Wt=None):
        S = self.S; Nth = S.Nth
        if Wr is None:
            Wr, Wt, rho = self.velocity(g)
        rho = S.r[:, None] ** self.p * g
        godd = 0.5 * (g - g[:, self.flip]); geven = 0.5 * (g + g[:, self.flip])
        out = dict(godd_rel_rms=float(torch.sqrt((godd ** 2).mean() / (geven ** 2).mean())), godd_max_rel=float((godd.abs() / g.max(dim=1, keepdim=True).values.clamp(min=1e-300)).max()))
        lrn = S.lr.cpu().numpy()
        for L in (-12.0, -10.0):
            i = int(np.argmin(np.abs(lrn - L))); r = float(S.r[i])
            vr = (Wr[0, i] / r).cpu().numpy(); vt = (Wt[0, i] / r).cpu().numpy()
            fr = np.fft.rfft(vr) / Nth; ft = np.fft.rfft(vt) / Nth
            alpha0 = fr[0].real; alpha2 = 2 * fr[2].real; beta2 = -2 * fr[2].imag; gamma0 = ft[0].real
            out['DW_lr%g' % L] = dict(DW11=float(alpha0 + alpha2), DW22=float(alpha0 - alpha2), DW12=float(beta2 - gamma0), DW21=float(beta2 + gamma0), psi_yy0=float(-(beta2 - gamma0)), div=float(2 * alpha0), rot=float(gamma0))
        A = self.Afun(S.th[None, :])
        cm, core = self.SB.c_moment(rho[None], self.pB, A); out['m1'] = 1.0 / self.p - float(cm[0]); out['c'] = float(cm[0]); out['core'] = float(core[0])
        return out

    def resid_norms(self, g, Tg):
        rowmax = g.max(dim=1, keepdim=True).values
        msk = g > 1e-3 * rowmax
        d = torch.where(msk, (Tg - g).abs() / rowmax, torch.zeros_like(g))
        return float(d.max()), float(torch.sqrt((d ** 2).sum() / msk.sum()))


def newton_gmres(GM, g0, maxit=6, kmax=20, gtol=1e-6, eps_rel=1e-4, log=print, tag='gn', outdir='runs/pfwd/gn'):
    """Newton-GMRES on R(u) = u - Ttilde(u) in the scaled variable u = g / scale (no parity projection).
    J v by forward differences with step e = eps_rel |u| / |v|.  GMRES (Arnoldi, modified Gram-Schmidt) with kmax vectors; the Hessenberg matrix H is saved.
    Backtracking line search on |R|_2 (factors 1, 1/2, 1/4, 1/8)."""
    os.makedirs(outdir, exist_ok=True)
    S = GM.S; N = S.Nr * S.Nth
    g = g0.clone(); u = (g / GM.scale).reshape(-1)
    def R_of(u_):
        g_ = (u_.reshape(S.Nr, S.Nth) * GM.scale).clamp(min=0.0)
        Tg_, info_ = GM.T(g_)
        return u_ - (Tg_ / GM.scale).reshape(-1), g_, Tg_, info_
    R, g, Tg, info = R_of(u); nT = 1
    hist = []
    for it in range(maxit + 1):
        dmax, drms = GM.resid_norms(g, Tg); dg = GM.diag(g)
        rec = dict(it=it, R2=float(R.norm()), defect_max=dmax, defect_rms=drms, nT=nT, **{k: v for k, v in info.items()}, godd_rel_rms=dg['godd_rel_rms'], godd_max_rel=dg['godd_max_rel'],
                   psi_yy0_lr12=dg['DW_lr-12']['psi_yy0'], psi_yy0_lr10=dg['DW_lr-10']['psi_yy0'], DW12_lr12=dg['DW_lr-12']['DW12'], rot_lr12=dg['DW_lr-12']['rot'], m1=dg['m1'], c=dg['c'])
        hist.append(rec); log(json.dumps(rec))
        np.savez('%s/%s_it%d.npz' % (outdir, tag, it), g=g.cpu().numpy(), Tg=Tg.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), info=json.dumps(rec),
                 args=json.dumps(dict(p=GM.p, kind='gammamap', par=GM.F_even.tolist(), F_odd=GM.F_odd.tolist(), th12_deg=[info['th1_deg'], info['th2_deg']])))
        if drms < gtol or it == maxit:
            break
        # GMRES for J d = -R
        b = -R; beta = float(b.norm()); V = [b / beta]; H = np.zeros((kmax + 1, kmax)); kk = 0; resid_hist = []
        for k in range(kmax):
            v = V[k]; e = eps_rel * float(u.norm()) / max(float(v.norm()), 1e-300)
            Rp, _, _, _ = R_of(u + e * v); nT += 1
            w = (Rp - R) / e
            for i in range(k + 1):
                H[i, k] = float(torch.dot(V[i], w)); w = w - H[i, k] * V[i]
            H[k + 1, k] = float(w.norm()); kk = k + 1
            # least-squares residual of the GMRES iterate
            y, *_ = np.linalg.lstsq(H[:kk + 1, :kk], np.concatenate([[beta], np.zeros(kk)]), rcond=None)
            rres = float(np.linalg.norm(H[:kk + 1, :kk] @ y - np.concatenate([[beta], np.zeros(kk)]))) / beta; resid_hist.append(round(rres, 5))
            if H[k + 1, k] < 1e-14 or rres < 1e-3:
                break
            V.append(w / H[k + 1, k])
        Hk = H[:kk + 1, :kk]
        y, *_ = np.linalg.lstsq(Hk, np.concatenate([[beta], np.zeros(kk)]), rcond=None)
        d = sum(float(y[i]) * V[i] for i in range(kk))
        svH = np.linalg.svd(Hk, compute_uv=False)
        np.savez('%s/%s_H%d.npz' % (outdir, tag, it + 1), H=Hk, beta=beta, y=y)
        # line search
        accepted = False
        for fac in (1.0, 0.5, 0.25, 0.125):
            Rn, gn, Tgn, infon = R_of(u + fac * d); nT += 1
            if float(Rn.norm()) < float(R.norm()) and infon['unfinished'] == 0:
                u = u + fac * d; R, g, Tg, info = Rn, gn, Tgn, infon; accepted = True; break
        log(json.dumps(dict(it=it + 1, gmres_k=kk, gmres_resid=resid_hist, H_sv=[float('%.4g' % v) for v in svH], H_sv_min=float(svH[-1]), H_sv_max=float(svH[0]), step_fac=(fac if accepted else None), d_norm=float(d.norm()), R2_new=float(R.norm()), accepted=accepted, nT=nT)))
        if not accepted:
            log(json.dumps(dict(it=it + 1, note='no decrease in the line search; stopping')))
            break
    return g, hist


if __name__ == '__main__':
    # usage: python3 code/pfwd_gnewton.py state.npz tag [Nth=256] [eps_odd=1e-3] [odd_mode=1] [maxit=6] [kmax=20] [eps_rel=1e-4] [dt=0.01] [F_odd="a1,a2,.."]
    fn = sys.argv[1]; tag = sys.argv[2]
    opt = dict(Nth=0, eps_odd=1e-3, odd_mode=1, maxit=6, kmax=20, eps_rel=1e-4, dt=0.01, F_odd='', lr_g=-12.0)
    for s_ in sys.argv[3:]:
        k, v = s_.split('='); opt[k] = v if k == 'F_odd' else (int(v) if k in ('Nth', 'odd_mode', 'maxit', 'kmax') else float(v))
    d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'])
    if a.get('kind') == 'bnewton': coef = coef[:int(a['K'])]          # bnewton iterate files store par = x[:-1] (modes, bumps, [D], [q]); the Fourier modes are the first K
    if opt['Nth'] and g0.shape[1] != opt['Nth']:
        g0 = g0[:, ::g0.shape[1] // opt['Nth']]; th = th[::len(th) // opt['Nth']]
    Nr, Nth = g0.shape
    F_odd = np.array([float(v) for v in opt['F_odd'].split(',')]) if opt['F_odd'] else None
    GM = GammaMap(Nr, Nth, float(lr[0]), float(lr[-1]), p, coef, F_odd=F_odd, dt=opt['dt'], lr_g=opt['lr_g'])
    os.makedirs('runs/pfwd/gn', exist_ok=True); logf = open('runs/pfwd/gn/%s.log' % tag, 'a')
    def log(line):
        print(line, flush=True); logf.write(line + '\n'); logf.flush()
    log(json.dumps(dict(tag=tag, state=fn, p=p, coef=coef.tolist(), F_odd=(F_odd.tolist() if F_odd is not None else None), Nr=Nr, Nth=Nth, opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))))
    g = torch.tensor(g0, device='cuda')
    # x-odd perturbation of g: g (1 + eps_odd phi_odd(th)), phi_odd = cos(n th) (odd n) or sin(n th) (even n)
    n = opt['odd_mode']; thT = torch.tensor(th, device='cuda')
    phi = torch.cos(n * thT) if n % 2 == 1 else torch.sin(n * thT)
    g = g * (1.0 + opt['eps_odd'] * phi[None, :])
    gfin, hist = newton_gmres(GM, g, maxit=opt['maxit'], kmax=opt['kmax'], eps_rel=opt['eps_rel'], log=log, tag=tag)
    log('GNEWTON_DONE')
