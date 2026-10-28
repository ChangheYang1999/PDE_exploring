"""Rigorous field enclosures over boxes by radial Taylor models (RTM).

phi(x,y) = sum_{m,j} H_m(x,y) g_{mj}(q), q = x^2 + y^2, g_{mj}(q) = sum_{k=m}^{25} a_{mkj} q^{k-m} (1+q)^{p_j-k}.
For a box B = [x_c +- hx] x [y_c +- hy] with q_c = x_c^2 + y_c^2 and |q - q_c| <= delta on B:
  g(q_c + eps) = sum_{d<=D} g_d eps^d + T(eps),  g_d from an arb power series at the exact point q_c (no interval dependency),
  Cauchy bound on |eps| = rho (rho < 1 + q_c, the distance to the branch point q = -1):
     M_rho = sum_k |a_k| (q_c+rho)^{k-m} (1+q_c+rho)^{max(p-k,0)} (1+q_c-rho)^{min(p-k,0)},  |g_d| <= M_rho rho^-d,
     |T^{(n)}(eps)| <= tau_n := M_rho rho^{-n} (D+1)^n x^{D+1-n} / (1 - x e^{n/(D+1)}),  x = delta/rho  (requires x e^{n/(D+1)} < 1).
The directional series s -> phi(X0 + s(u,v)) for X0 in B is built with ball coordinates; the radial part is P(eps(s)) + Tail(eps(s)),
Tail(eps0 + Delta) = sum_{n<=N} [T^{(n)}(eps0)/n!] Delta^n with T^{(n)}(eps0) in [+-tau_n]. The mixed partials up to order N are solved
exactly from N+1 directions. Every returned ball contains the exact value for every X0 in B.
"""
import math
def _fup(x):
    """binary64 >= the upper bound of the arb x (outward rounding of a radius conversion)."""
    return math.nextafter(float(x.upper()), math.inf)

from fractions import Fraction as Fr
from flint import arb, arb_series, fmpq, fmpq_mat, ctx
from ipm_arb import State, canon

def _arb_fr(fr): return arb(fmpq(fr.numerator, fr.denominator))

class RTMState(State):
    def __init__(self, exact_json, prec=256):
        super().__init__(exact_json, prec)
        ctx.prec = prec
        self.absA = {key: [abs(c) for c in coeffs] for key, coeffs in self.A.items()}

    def radial_model(self, m, j, q_c, delta, D, N):
        """Taylor coefficients g_0..g_D (arb) of g_{mj} at q_c (arb, exact point) and tail derivative bounds tau_0..tau_N over |eps| <= delta."""
        p = self.p[j]; coeffs = self.A[(m, j)]
        Q = arb_series([q_c, 1], D+1)
        R = Q + 1; T = Q/R
        logR = R.log()
        # sum_k a_k T^{k-m}  (Horner in T over k-m = 0..25-m)
        G = arb_series([0], D+1)
        for c in reversed(coeffs): G = G*T + c
        g = G*((p-m)*logR).exp()
        gd = [g[d] for d in range(D+1)]
        # Cauchy bound
        rho = (1+q_c)/2
        if not (delta*8 <= 1+q_c): raise ValueError('box too large for the radial model: need delta <= (1+q_c)/8')
        M = arb(0)
        for i, ac in enumerate(self.absA[(m, j)]):
            k = m+i
            if ac.is_zero(): continue
            pk = p-k
            fac = (q_c+rho)**i
            if pk >= 0: fac *= (1+q_c+rho)**pk
            else: fac *= (1+q_c-rho)**pk
            M += ac*fac
        x = delta/rho
        taus = []
        for n in range(N+1):
            denom = 1 - x*arb(n/(D+1)).exp()
            if not (denom > 0): raise ValueError('tail bound requires x e^{n/(D+1)} < 1')
            taus.append(M*rho**(-n)*arb(D+1)**n*x**(D+1-n)/denom)
        return gd, taus

    def box_phi_series(self, xb, yb, u, v, N, models, q_c):
        """Series of phi along (u,v) from ball coordinates xb, yb (covering the box), using precomputed radial models."""
        X = arb_series([xb, arb(u)], N+1); Y = arb_series([yb, arb(v)], N+1)
        q = X*X + Y*Y
        eps = q - q_c
        eps0 = eps[0]
        Delta = eps - eps0           # zero constant term
        re2 = X*X - Y*Y; im2 = 2*X*Y
        H = [arb_series([1], N+1)]
        pre, pim = arb_series([1], N+1), arb_series([0], N+1)
        for m in range(1, 10):
            pre, pim = pre*re2 - pim*im2, pre*im2 + pim*re2
            H.append(pre)
        # powers of Delta for the tail
        Dp = [arb_series([1], N+1)]
        for n in range(1, N+1): Dp.append(Dp[-1]*Delta)
        total = arb_series([0], N+1)
        for (m, j), (gd, taus) in models.items():
            P = arb_series([0], N+1)
            for c in reversed(gd): P = P*eps + c
            Tail = arb_series([0], N+1)
            for n in range(N+1): Tail = Tail + Dp[n]*arb(0, float(taus[n]/math.factorial(n)))
            total = total + H[m]*(P + Tail)
        return total, eps0

    def box_jet(self, x_c, y_c, hx, hy, N=4, D=60):
        """Enclosures {(a,b): ball} of d^a_x d^b_y phi over the box; x_c, y_c, hx, hy as Fractions or floats (converted exactly)."""
        ctx.prec = self.prec
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxa = _arb_fr(Fr(hx)); hya = _arb_fr(Fr(hy))
        xb = arb(xc.mid(), 0) ; yb = arb(yc.mid(), 0)
        xb = xc + arb(0, float(hxa.upper())); yb = yc + arb(0, float(hya.upper()))
        q_c = xc*xc + yc*yc
        eps0 = xb*xb + yb*yb - q_c
        delta = arb(abs(eps0).upper())
        models = {key: self.radial_model(key[0], key[1], q_c, delta, D, N) for key in self.A}
        Dirs = self._directions(N)
        series = [self.box_phi_series(xb, yb, u, v, N, models, q_c)[0] for (u, v) in Dirs]
        coef = [[s[d] for d in range(N+1)] for s in series]
        jet = {(0, 0): coef[0][0]}
        for d in range(1, N+1):
            dirs = Dirs[:d+1]
            Mm = fmpq_mat([[fmpq(uu)**a * fmpq(vv)**(d-a) for a in range(d, -1, -1)] for (uu, vv) in dirs])
            Minv = Mm.inv()
            rhs = [coef[i][d] for i in range(d+1)]
            for row, a in enumerate(range(d, -1, -1)):
                val = arb(0)
                for col in range(d+1): val += arb(Minv[row, col])*rhs[col]
                jet[(a, d-a)] = val*math.factorial(a)*math.factorial(d-a)
        return jet, xb, yb

    def box_fields(self, x_c, y_c, hx, hy, N=4, D=60):
        J, xb, yb = self.box_jet(x_c, y_c, hx, hy, N, D)
        def P(a, b): return J[(a, b)]
        out = {'phi': P(0, 0), 'psi': P(1, 1), 'U1': -P(1, 2), 'U2': P(2, 1), 'psi_xy': P(2, 2),
               'rho': -(P(2, 1)+P(0, 3)), 'rho_x': -(P(3, 1)+P(1, 3)), 'rho_y': -(P(2, 2)+P(0, 4)),
               'DU': [[-P(2, 2), -P(1, 3)], [P(3, 1), P(2, 2)]], 'x': xb, 'y': yb}
        out['V1'] = self.cl*xb + out['U1']; out['V2'] = self.cl*yb + out['U2']
        out['F'] = out['V1']*out['rho_x'] + out['V2']*out['rho_y'] - out['rho']
        if N >= 5:
            out['rho_xx'] = -(P(4, 1)+P(2, 3)); out['rho_xy'] = -(P(3, 2)+P(1, 4)); out['rho_yy'] = -(P(2, 3)+P(0, 5))
        return out

def Mmin_from_fields(f, cl):
    DU = f['DU']
    M11 = 2*cl + 1 + DU[0][0] + f['rho_y']; M22 = 2*cl + 1 + DU[1][1]; M12 = (DU[0][1] + DU[1][0])/2 - f['rho_x']/2
    tr = M11 + M22; det = M11*M22 - M12*M12
    disc = (tr/2)**2 - det
    return tr/2 - disc.sqrt() if disc >= 0 else tr/2 - abs(disc).sqrt()

if __name__ == '__main__':
    import sys, time
    S = RTMState(sys.argv[1], prec=256)
    cl = S.cl
    for (x0, y0, hx, hy) in [(0, 0, 0.05, 0.05), (0, 0, 0.2, 0.2), (0.5, 0.5, 0.03, 0.03), (0.5, 0.5, 0.1, 0.1), (3, 3, 0.1, 0.1), (3, 3, 0.25, 0.25), (0, 30, 1, 1), (0, 30, 2, 2), (300, 300, 10, 10), (300, 300, 25, 25), (0, 1e4, 500, 500), (1e6, 1e6, 5e4, 5e4)]:
        t0 = time.time()
        try:
            f = S.box_fields(x0, y0, hx, hy, N=4, D=60)
            lm = Mmin_from_fields(f, cl)
            fc = S.fields(x0, y0, 4)   # center point for comparison
            print('box (%g,%g) h=(%g,%g): lam_min(M) in %s (width %.2e) center %s | rho in %s (center %s) | F in %s (center %s)  t=%.2fs' % (x0, y0, hx, hy, lm.str(7), 2*float(lm.rad()), Mmin_from_fields(fc, cl).str(7), f['rho'].str(5), fc['rho'].str(5), f['F'].str(4), fc['F'].str(4), time.time()-t0))
        except ValueError as e:
            print('box (%g,%g) h=(%g,%g): %s' % (x0, y0, hx, hy, e))
