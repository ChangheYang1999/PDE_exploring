# Verifier evaluator for the frozen packet of request (o2) (own code, GPU float64).
#   v(s,y)   = -(1/pi^2) int_0^inf eta^-2 Fv(eta) sin(y eta) d eta,
#   U2[v]    = -(1/pi^2) int_0^inf eta^-2 FU(eta) sin(y eta) d eta,
#   Fv(eta)  = int_1^2 phi(t) sig sin(s t eta^A) dt,  FU = int_1^2 phi(t) sig (-X/(1+X)) sin(s t eta^A) dt,
#   X = lam t^2 eta^(2A-2), sig = (1+X)^-b, b = g/(2(A-1)); lam = 1 is the plain packet; phi = exp(-1/((t-1)(2-t))).
# t: composite 16-point Gauss-Legendre with panel count set by the largest s t eta^A in an eta block; the t-integral
# is set to zero where s eta^A > OMC (there the Fourier transform of the bump is below 1e-20 of its mass).
# eta: composite 16-point Gauss-Legendre panels whose width resolves the phase rates 2 A |s| eta^(A-1) and y.
import numpy as np, torch
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
DT = torch.float64
GX16, GW16 = np.polynomial.legendre.leggauss(16)
OMC = 1200.0
I0 = 0.007029858406609657   # int phi

def comp_gl(edges):
    e = np.asarray(edges, float); a = e[:-1]; b = e[1:]
    x = (0.5*(b-a))[:, None]*GX16[None, :] + (0.5*(b+a))[:, None]
    w = (0.5*(b-a))[:, None]*GW16[None, :]
    return x.ravel(), w.ravel()

class Packet:
    def __init__(self, A, g, lam=1.0, tol=1e-21, res=1.0):
        self.A, self.g, self.lam, self.tol, self.res = A, g, lam, tol, res
        self.b = g/(2*(A-1))
        self.eta_tr = lam**(-1/(2*A-2))

    def eta_grid(self, s, ymax):
        A, g = self.A, self.g
        eamp = (self.lam**(-self.b)*I0/np.pi**2/(self.tol*(1+g)))**(1/(1+g))
        ecut = (OMC/abs(s))**(1/A) if s != 0 else np.inf
        ee = min(eamp, ecut)
        edges = [0.0]
        et = self.eta_tr
        hmax = 0.2*min(1.0, et)/self.res
        x = 0.0
        # geometric start around the transition scale
        geo = [z for z in np.geomspace(1e-3*et, et, 25) if z < ee]
        for z in geo:
            edges.append(z)
        x = edges[-1]
        while x < ee:
            rate = 2*A*abs(s)*max(x, 1e-300)**(A-1) + ymax
            h = min(max(hmax, 0.2*x/self.res) if x > et else hmax, 3.0/(rate*self.res))
            x = min(x + h, ee)
            edges.append(x)
        return comp_gl(edges), ee

    def F(self, s, eta):
        A, b, lam = self.A, self.b, self.lam
        eta_t = torch.tensor(eta, dtype=DT, device=dev)
        Fv = torch.zeros_like(eta_t); FU = torch.zeros_like(eta_t)
        nb = 2048
        for i0 in range(0, len(eta), nb):
            e = eta_t[i0:i0+nb]
            om = abs(s)*2*float(e.max())**A
            P = int(max(8, np.ceil(min(om, 2*OMC)*self.res/4.0)))
            tt, tw = comp_gl(np.linspace(1, 2, P+1))
            t = torch.tensor(tt, dtype=DT, device=dev); w = torch.tensor(tw, dtype=DT, device=dev)
            ph = torch.exp(-1/((t-1)*(2-t)))*w
            lX = np.log(lam) + 2*torch.log(t)[None, :] + (2*A-2)*torch.log(e)[:, None]
            X = torch.exp(lX)
            sig = torch.exp(-b*torch.log1p(X))
            arg = s*t[None, :]*e[:, None]**A
            sn = torch.sin(arg)
            M = (sig*sn)
            Fv[i0:i0+nb] = M @ ph
            FU[i0:i0+nb] = -(M*(X/(1+X))) @ ph
            if om > 4*OMC:   # beyond the cutoff the t-integral is set to zero
                cut = (abs(s)*e**A > OMC)
                Fv[i0:i0+nb] = torch.where(cut, torch.zeros_like(e), Fv[i0:i0+nb])
                FU[i0:i0+nb] = torch.where(cut, torch.zeros_like(e), FU[i0:i0+nb])
        return Fv, FU

    def eval(self, s, ys):
        ys = np.atleast_1d(np.asarray(ys, float))
        if s == 0:
            z = np.zeros_like(ys); return z, z.copy(), 0.0
        (eta, w), ee = self.eta_grid(s, float(np.max(np.abs(ys))))
        Fv, FU = self.F(s, eta)
        e = torch.tensor(eta, dtype=DT, device=dev); W = torch.tensor(w, dtype=DT, device=dev)
        y = torch.tensor(ys, dtype=DT, device=dev)
        S = torch.sin(e[:, None]*y[None, :])
        kv = (W*Fv/e**2)
        kU = (W*FU/e**2)
        v = -(kv @ S)/np.pi**2
        U = -(kU @ S)/np.pi**2
        G3 = float(torch.sum(W*e*Fv))/(6*np.pi**2)
        return v.cpu().numpy(), U.cpu().numpy(), G3
