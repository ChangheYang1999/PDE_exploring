# Own-initiative check of 6.4 "The frozen kernel at P", item (iv) (growth): for an uncut packet v,
#   |v(X)| <= C (1+|X|)^(1/A) with optimal exponent, and (1+|X|)|grad v| is not O((1+|X|)^gamma) for gamma < 1.
# Representation (Phi real odd: 'odd'; Phi = i phi, phi even, beta1 - beta2: 'even'):
#   v(s,y) = -(1/pi^2) int_0^inf r^-2 sin(y r) int phi(t) (1+t^2 r^q)^-b T(s t r^A) dt dr,  T = sin ('odd'), cos ('even').
# Exact rescaling: v(mu^A s0, mu y0) = mu V_lam(s0, y0), lam = mu^(-q), q = 2A-2, where V_lam has the factor
# (1 + lam t^2 r^q)^-b; dy v(mu^A s0, mu y0) = dy V_lam(s0, y0). V_0 (lam -> 0) is the degree-1 leading part v_0.
# The eta grid resolves every phase rate (eta_grid below); res = 2 is the refinement check.
# Points with |X| = R are put on the unit quasi-circle s0^(2/A) + y0^2 = 1 with mu solving mu^(2A) s0^2 + mu^2 y0^2 = R^2.
# Bounds proved by hand (the verification record D50): |v_0(s,y)| <= C0 |s|^(1/A), C0 = (1/(A pi^2)) int_0^inf u^(-1/A-1) |f(u)| du,
# f(u) = int phi(t) T(t u) dt, and |v - v_0| <= C (1 + |y|^max(0, 3-2A)).
import sys, json, numpy as np, torch
sys.path.insert(0, 'code/frozen')
import vpacket as V
dev, DT = V.dev, V.DT

def bump(t, a):
    return torch.where((t > a) & (t < a+1), torch.exp(-1/((t-a).clamp(min=1e-300)*(a+1-t).clamp(min=1e-300))), torch.zeros_like(t))

class Pk(V.Packet):
    def __init__(self, A, g, kind, lam, res=1.0):
        super().__init__(A, g, lam=max(lam, 1e-150), tol=1e-24, res=res)
        self.kind = kind
        self.tmax = 2.0 if kind == 'odd' else 3.0

    def F(self, s, eta):
        A, b, lam = self.A, self.b, self.lam
        e_all = torch.tensor(eta, dtype=DT, device=dev)
        Fv = torch.zeros_like(e_all)
        nb = 2048
        for i0 in range(0, len(eta), nb):
            e = e_all[i0:i0+nb]
            om = abs(s)*self.tmax*float(e.max())**A
            P = int(max(8, np.ceil(min(om, 2*V.OMC)*(self.tmax-1)/4.0)))
            tt, tw = V.comp_gl(np.linspace(1, self.tmax, P+1))
            t = torch.tensor(tt, dtype=DT, device=dev); w = torch.tensor(tw, dtype=DT, device=dev)
            ph = (bump(t, 1.0) if self.kind == 'odd' else bump(t, 1.0) - bump(t, 2.0))*w
            X = torch.exp(np.log(lam) + 2*torch.log(t)[None, :] + (2*A-2)*torch.log(e)[:, None])
            sig = torch.exp(-b*torch.log1p(X))
            arg = s*t[None, :]*e[:, None]**A
            Tm = torch.sin(arg) if self.kind == 'odd' else torch.cos(arg)
            Fv[i0:i0+nb] = (sig*Tm) @ ph
            if om > 4*V.OMC:
                cut = (abs(s)*e**A > V.OMC)
                Fv[i0:i0+nb] = torch.where(cut, torch.zeros_like(e), Fv[i0:i0+nb])
        return Fv

    def eta_grid(self, s, ymax):
        # own grid (the vpacket grid puts a geometric block below eta_tr = lam^(-1/q), which is too coarse for lam << 1):
        # panels of width min(0.2, 3/rate)/res with rate = A |s| tmax eta^(A-1) + ymax, up to the cutoff of vpacket
        A, g = self.A, self.g
        eamp = (self.lam**(-self.b)*V.I0/np.pi**2/(self.tol*(1+g)))**(1/(1+g))
        ee = min(eamp, (V.OMC/abs(s))**(1/A))
        edges = [0.0]; x = 0.0
        while x < ee:
            rate = A*abs(s)*self.tmax*max(x, 1e-300)**(A-1) + ymax
            x = min(x + min(0.2, 3.0/rate)/self.res, ee)
            edges.append(x)
        return V.comp_gl(edges), ee

    def vdy(self, s, y):
        (eta, w), ee = self.eta_grid(s, abs(y))
        Fv = self.F(s, eta)
        e = torch.tensor(eta, dtype=DT, device=dev); W = torch.tensor(w, dtype=DT, device=dev)
        v = -float(torch.sum(W*Fv/e**2*torch.sin(e*y)))/np.pi**2
        dy = -float(torch.sum(W*Fv/e*torch.cos(e*y)))/np.pi**2
        return v, dy

def C0_bound(A, kind):
    # (1/(A pi^2)) int_0^inf u^(-1/A-1) |f(u)| du, f(u) = int phi(t) T(t u) dt
    x, w = np.polynomial.legendre.leggauss(64)
    tt, tw = V.comp_gl(np.linspace(1, 2 if kind == 'odd' else 3, 801))
    def bmp(t, a):
        o = np.zeros_like(t); m = (t > a) & (t < a+1); o[m] = np.exp(-1/((t[m]-a)*(a+1-t[m]))); return o
    ph = (bmp(tt, 1.0) if kind == 'odd' else bmp(tt, 1.0) - bmp(tt, 2.0))*tw
    ue = np.concatenate([[0.0], np.geomspace(1e-8, 1, 80), np.linspace(1, V.OMC, 4800)[1:]])
    ux, uw = V.comp_gl(ue)
    T = torch.sin if kind == 'odd' else torch.cos
    tq = torch.tensor(tt, dtype=DT, device=dev); pq = torch.tensor(ph, dtype=DT, device=dev)
    uq = torch.tensor(ux, dtype=DT, device=dev)
    f = torch.cat([(T(uq[i:i+4096, None]*tq[None, :]) @ pq) for i in range(0, len(ux), 4096)]).cpu().numpy()
    return float(np.sum(uw*ux**(-1/A-1)*np.abs(f)))/(A*np.pi**2)

def mu_of(R, s0, y0, A):
    lo, hi = 1e-300, R + 1.0
    for _ in range(200):
        m = np.sqrt(lo*hi) if hi/lo > 4 else 0.5*(lo+hi)
        if m**(2*A)*s0**2 + m**2*y0**2 > R**2: hi = m
        else: lo = m
    return 0.5*(lo+hi)

RES = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
out = {}
cases = [(3.0, 5.5, 'odd'), (3.0, 3.5, 'even'), (10.15, 29.75, 'odd')]
for (A, g, kind) in cases:
    q = 2*A-2
    key = 'A%g_g%g_%s' % (A, g, kind)
    C0 = C0_bound(A, kind)
    print('== %s  q = %g  1/A = %.6f  C0 = %.6e' % (key, q, 1/A, C0), flush=True)
    y0s = np.concatenate([np.linspace(0.02, 0.98, 49), [0.99, 0.995, 0.999]])
    # leading part V_0 on the unit quasi-circle and the ratio |V_0|/s0^(1/A) (must be <= C0)
    P0 = Pk(A, g, kind, 1e-150, res=RES)
    V0 = []; D0 = []
    for y0 in y0s:
        s0 = (1-y0**2)**(A/2)
        a, d = P0.vdy(s0, y0); V0.append(a); D0.append(d)
    V0 = np.array(V0); D0 = np.array(D0); s0s = (1-y0s**2)**(A/2)
    kap = np.abs(V0)/s0s**(1/A)
    i_k = int(np.argmax(kap)); i_d = int(np.argmax(np.abs(D0)))
    print('  sup |V_0|/s0^(1/A) on the quasi-circle = %.6e at y0 = %.3f  (C0 = %.6e)' % (kap[i_k], y0s[i_k], C0))
    print('  max |dy V_0| = %.6e at y0 = %.3f, s0 = %.4e' % (abs(D0[i_d]), y0s[i_d], s0s[i_d]), flush=True)
    rowsM = []
    Rs = [10.0**k for k in (range(1, 13) if A < 5 else range(2, 41, 3))]
    for R in Rs:
        vals = []
        for y0, s0 in zip(y0s, s0s):
            mu = mu_of(R, s0, y0, A)
            P = Pk(A, g, kind, mu**(-q), res=RES)
            a, _ = P.vdy(s0, y0)
            vals.append(mu*a)
        vals = np.abs(np.array(vals)); j = int(np.argmax(vals))
        rowsM.append(dict(R=R, M=float(vals[j]), y0=float(y0s[j]), ratio=float(vals[j]/R**(1/A))))
        print('  R = %.0e  max_{|X|=R} |v| = %.6e (y0 = %.3f)  / R^(1/A) = %.6e' % (R, vals[j], y0s[j], vals[j]/R**(1/A)), flush=True)
    # gradient along X_mu = (mu^A s1, mu y1) at the point of max |dy V_0|
    y1, s1 = float(y0s[i_d]), float(s0s[i_d])
    rowsG = []
    for k in range(0, 13, 2):
        mu = 2.0**k
        P = Pk(A, g, kind, mu**(-q), res=RES)
        a, d = P.vdy(s1, y1)
        Xn = np.hypot(mu**A*s1, mu*y1)
        rowsG.append(dict(mu=mu, absX=float(Xn), dyv=d, dyV0=float(D0[i_d]), w=float((1+Xn)*abs(d)/(1+Xn)**0.99)))
        print('  mu = 2^%-2d |X| = %.3e  dy v = %.10e (dy V_0 = %.10e)  (1+|X|)|dy v|/(1+|X|)^0.99 = %.4e' %
              (k, Xn, d, D0[i_d], (1+Xn)*abs(d)/(1+Xn)**0.99), flush=True)
    # |v - v_0| at fixed physical points with large y (bounded for A >= 3/2), evaluated without rescaling
    rowsD = []
    P1 = Pk(A, g, kind, 1.0, res=RES)
    for (s, y) in [(1.0, 1e2), (1.0, 1e3), (0.1, 1e2), (10.0, 10.0), (100.0, 1.0)]:
        a, _ = P1.vdy(s, y)
        b0, _ = P0.vdy(s, y)
        rowsD.append(dict(s=s, y=y, v=a, v0=b0, diff=a-b0, C0s=C0*abs(s)**(1/A)))
        print('  (s,y) = (%.0e,%.0e)  v = %.6e  v_0 = %.6e  v - v_0 = %.3e   C0 |s|^(1/A) = %.3e' %
              (s, y, a, b0, a-b0, C0*abs(s)**(1/A)), flush=True)
    out[key] = dict(A=A, g=g, kind=kind, C0=C0, sup_ratio_V0=float(kap[i_k]), y0_sup=float(y0s[i_k]),
                    max_dyV0=float(D0[i_d]), y1=y1, s1=s1, rowsM=rowsM, rowsG=rowsG, rowsD=rowsD)
json.dump(out, open('runs/frozen_growth_iv_res%g.json' % RES, 'w'), indent=1)
print('done')
