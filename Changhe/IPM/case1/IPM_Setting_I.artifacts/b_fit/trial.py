"""Direct evaluation of the saved global density and its analytic derivatives."""
import numpy as np
from numpy.polynomial.chebyshev import chebval, chebder
from scipy.interpolate import BSpline


class Trial:
    def __init__(self, path):
        z = np.load(path)
        self.k, self.L = float(z["k"]), float(z["L"])
        self.degree, self.angular = int(z["degree"]), int(z["angular"])
        self.origin = float(z["origin_radius"])
        self.order = int(z["spline_order"])
        assert str(z["radial_basis"]) == "spline"
        assert str(z["compact"]) == "matched"
        self.knots = z["spline_knots"] if "spline_knots" in z and len(z["spline_knots"]) else np.r_[np.zeros(self.order+1),
                           np.linspace(0, 1, self.degree-self.order+2)[1:-1]**1.3,
                           np.ones(self.order+1)]
        c = z["z"][1:1+(self.angular+1)*self.degree].reshape(self.angular+1, self.degree)
        self.spline = BSpline(self.knots, np.vstack([np.zeros(self.angular+1), c.T]), self.order)
        self.singular = z["z"][-int(z["singular"]):]
        self.p3 = 6+2*self.k/(2-self.k)

    def fields(self, r, theta, second=False):
        r, theta = np.broadcast_arrays(np.asarray(r, float), np.asarray(theta, float))
        shape = r.shape; rr = r.ravel()/self.L; th = theta.ravel()
        r2 = rr*rr
        s = r2/(1+r2)
        q = -np.expm1(-(1-self.k)/2*np.log1p(r2))
        qt = (1-self.k)*s*(1-q)
        qtt = (1-self.k)*(1-q)*(2*s*(1-s)-(1-self.k)*s*s)
        b = self.spline(q); bt = self.spline(q, nu=1)*qt[:, None]
        if second:
            btt = self.spline(q, nu=2)*qt[:, None]**2+self.spline(q, nu=1)*qtt[:, None]
        m = np.arange(self.angular+1)
        j = np.maximum(m-1, 0)
        chi = r2/(r2+self.origin**2)
        mult = chi[:, None]**j
        lt = 2*j*(1-chi[:, None])
        ltt = -4*j*chi[:, None]*(1-chi[:, None])
        if second: btt = mult*(btt+2*lt*bt+(lt*lt+ltt)*b)
        bt = mult*(bt+lt*b)
        b = mult*b
        cos = np.cos(2*th[:, None]*m); sin = np.sin(2*th[:, None]*m)
        H = (self.k-3)/2*np.log1p(r2)+np.sum(b*cos, axis=1)
        Ht = (self.k-3)*s+np.sum(bt*cos, axis=1)
        Ha = np.sum(b*(-2*m*sin), axis=1)
        if second:
            Htt = 2*(self.k-3)*s*(1-s)+np.sum(btt*cos, axis=1)
            Haa = np.sum(b*(-4*m*m*cos), axis=1)
            Htaa = np.sum(bt*(-4*m*m*cos), axis=1)
        ct = np.maximum(np.cos(th), 0.); st = np.sin(th); a = self.p3-2
        angular = ct**a*st**2
        angular_t = 2*ct**(a+1)*st-a*ct**(a-1)*st**3
        pref = s**(self.p3/2)
        c = self.singular
        poly = chebval(2*q-1, c)
        pd = chebval(2*q-1, chebder(c))
        sg = pref*poly
        sgt = self.p3*(1-s)*sg+2*pref*pd*qt
        H += sg*angular; Ht += sgt*angular; Ha += sg*angular_t
        answer = [H, Ht, Ha]
        if second:
            pdd = chebval(2*q-1, chebder(c, 2))
            sgtt = ((self.p3**2*(1-s)**2-2*self.p3*s*(1-s))*sg
                    +4*self.p3*(1-s)*pref*pd*qt+4*pref*pdd*qt*qt+2*pref*pd*qtt)
            angular_aa = a*(a-1)*ct**(a-2)*st**4-(5*a+2)*ct**a*st**2+2*ct**(a+2)
            Htt += sgtt*angular; Haa += sg*angular_aa; Htaa += sgt*angular_aa
            answer.extend([Htt, Haa, Htaa])
        return tuple(v.reshape(shape) for v in answer)

    def rho(self, x, y):
        x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
        r = np.hypot(x, y); theta = np.arctan2(abs(y), abs(x))
        H = self.fields(r, theta)[0]
        return x*x*y*np.exp(H)

    def axis(self, r, side=0):
        H, ht, ha, htt, haa, htaa = self.fields(r, np.full_like(r, side*np.pi/2), second=True)
        c = ht+haa; eh = np.exp(H)
        if side == 0:
            return dict(H=H, G1=r*r*eh, G1_prime=r*eh*(2+ht), G3=eh*c/2,
                        G3_prime=eh/(2*r)*(ht*c+htt+htaa))
        return dict(H=H, K2=r*eh, K2_prime=eh*(1+ht), K4=eh*c/(2*r),
                    K4_prime=eh/(2*r*r)*((ht-1)*c+htt+htaa))

    def d9(self, xp, n=32):
        qmax = -np.expm1(-(1-self.k)/2*np.log1p((xp/self.L)**2))
        knots = np.unique(self.knots[(self.knots > 0) & (self.knots < qmax)])
        breaks = np.r_[0., self.L*np.sqrt(np.expm1(-2/(1-self.k)*np.log1p(-knots))), xp]
        nodes, weights = np.polynomial.legendre.leggauss(n)
        mid = (breaks[1:]+breaks[:-1])/2; half = np.diff(breaks)/2
        x = (mid[:, None]+half[:, None]*nodes).ravel()
        H = self.fields(x, np.zeros_like(x))[0]
        integrand = (np.expm1(-H)/x**2).reshape(-1, n)
        value = np.sum(half*(integrand@weights))
        return dict(points_per_interval=n, intervals=len(mid), integral=float(value),
                    target=float(1/xp), absolute_defect=float(value-1/xp),
                    relative_defect=float(value*xp-1))
