"""Residual F over a box: exact center Taylor polynomial of degree K plus a Cauchy remainder from a bound of |F| on a complex polydisc.

F = rho[phi_L] + U.grad rho (fcert.py identity). Center jets of phi (order K+4) and phi_L (order K+3) are exact point evaluations;
the Taylor coefficients of F at X_c follow by Leibniz. If |F| <= M_F on the polydisc |x'-x_c| <= rho_x, |y'-y_c| <= rho_y, then
|d^beta F(X_c)/beta!| <= M_F rho_x^-b1 rho_y^-b2 and the degree-K tail on the real box is at most
   M_F theta^(K+1) ((K+2) - (K+1) theta) / (1-theta)^2,  theta = max(hx/rho_x, hy/rho_y) < 1.
M_F <= M(rho[phi_L]) + M(U1) M(rho_x) + M(U2) M(rho_y), each M a crude bound of a field (<= 4 derivatives of a potential) on the polydisc:
termwise absolute values with the T1 structure (fcert.FCert.radial_bounds_specs generalized to a complex q-disk: |R'| in [R_c - d, R_c + d],
|u'| <= 1/(R_c - d), |t'| <= 1 + |u'|, |z' - z_mid| <= 2 d /((R_c)(R_c - d)), Legendre bounds by the finite Taylor expansion at z_mid,
Faa di Bruno with |t'^{(j)}| <= j! |u'|^{j+1}), and |x'| <= |x_c| + rho_x, |y'| <= |y_c| + rho_y, |x' + i y'| <= |x'| + |y'|.
"""
import math, sys, os
def _fup(x):
    """binary64 >= the upper bound of the arb x (outward rounding of a radius conversion)."""
    return math.nextafter(float(x.upper()), math.inf)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, ctx
from fcert import FCert
from boxenc3 import FIELDS, _arb_fr, falling, lah
from boxenc2 import P_gamma

class FCert2(FCert):
    def radial_bounds_disk(self, specs, q_c, d, order):
        """sup over the complex disk |q' - q_c| <= d of |g^{(l)}(q')| for each spec (same algebra as radial_bounds_specs, moduli bounds)."""
        R_c = 1 + q_c; R_lo = R_c - d; R_hi = R_c + d
        if not R_lo > 0: raise ValueError('disk reaches the branch point')
        u_hi = 1/R_lo; t_hi = 1 + u_hi
        hz = 2*d/(R_c*R_lo); z_mid = 1 - 2/R_c
        PD = self.legendre_derivs(z_mid, 26)
        nmax = 25
        Pi = [[arb(0)]*(nmax+2) for _ in range(nmax+1)]
        hzp = [arb(1)]
        for k in range(1, nmax+2): hzp.append(hzp[-1]*hz)
        for n in range(nmax+1):
            for s in range(n+2):
                acc = arb(0)
                for k in range(max(n-s, 0)+1): acc += abs(PD[n][s+k])*hzp[k]/math.factorial(k)
                Pi[n][s] = acc
        t_hi_p = [arb(1)]
        for k in range(1, 32): t_hi_p.append(t_hi_p[-1]*t_hi)
        u_hi_p = [arb(1)]
        for k in range(1, 2*order+4): u_hi_p.append(u_hi_p[-1]*u_hi)
        out = []
        for (m, beta, lows, highs, c0, mode) in specs:
            w = max(5-m, 0)
            Lam = []
            for k in range(order+1):
                acc = arb(0)
                for h, c in lows.items():
                    if h >= k: acc += c*math.perm(h, k)*t_hi_p[h-k]
                for i in range(min(k, w)+1):
                    s = k - i; inner = arb(0)
                    for n, g in highs.items():
                        if mode == 'plain':
                            if s <= n: inner += g*(2**s)*Pi[n][s]
                        else:
                            inner += g*(c0*(2**s)*Pi[n][s] + 2*(t_hi*(2**(s+1))*Pi[n][s+1] + s*(2**s)*Pi[n][s]))
                    acc += math.comb(k, i)*math.perm(w, i)*t_hi_p[w-i]*inner
                Lam.append(acc)
            Dq = [Lam[0]]
            for a in range(1, order+1):
                acc = arb(0)
                for k in range(1, a+1): acc += Lam[k]*lah(a, k)*u_hi_p[a+k]
                Dq.append(acc)
            G = []
            for l in range(order+1):
                acc = arb(0)
                for a in range(l+1):
                    e = beta - (l-a)
                    Rmax = R_hi**e if e >= 0 else R_lo**e
                    acc += math.comb(l, a)*abs(falling(beta, l-a))*Rmax*Dq[a]
                G.append(acc)
            out.append((m, G))
        return out

    def base_specs(self):
        specs = []
        for (m, j) in self.A:
            specs.append((m, self.p[j] - m, dict(self.lowabs.get((m, j), {})), dict(self.highabs.get((m, j), {})), None, 'plain'))
        return specs

    def polydisc_field_bounds(self, kind, x_c, y_c, rho_x, rho_y, order):
        """Crude sup bounds on the polydisc of |d^gamma phi_kind| for all |gamma| <= order (dict gamma -> arb)."""
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); rx = _arb_fr(Fr(rho_x)); ry = _arb_fr(Fr(rho_y))
        xabs = abs(xc) + rx; yabs = abs(yc) + ry
        q_c = xc*xc + yc*yc
        d = 2*(abs(xc)*rx + abs(yc)*ry) + rx*rx + ry*ry        # |q' - q_c| <= d on the polydisc
        specs = self.base_specs() if kind == 'base' else self.radial_specs(kind)
        GB = self.radial_bounds_disk(specs, q_c, d, order)
        Gm = {m: [arb(0)]*(order+1) for m in range(10)}
        for (m, G) in GB:
            for l in range(order+1): Gm[m][l] = Gm[m][l] + G[l]
        xp = [arb(1)]; yp = [arb(1)]
        for i in range(order+1): xp.append(xp[-1]*xabs); yp.append(yp[-1]*yabs)
        zabs = xabs + yabs; zp = [arb(1)]
        for i in range(19): zp.append(zp[-1]*zabs)
        out = {}
        for o in range(order+1):
            for a in range(o+1):
                b = o - a; total = arb(0)
                for m in range(10):
                    n = 2*m
                    for b1 in range(min(a, n)+1):
                        for b2 in range(min(b, n-b1)+1):
                            k = b1 + b2; dH = math.perm(n, k)*zp[n-k]
                            s = arb(0)
                            for l, poly in P_gamma((a-b1, b-b2)).items():
                                pv = arb(0)
                                for (i, jj), c in poly.items(): pv += abs(c)*xp[i]*yp[jj]
                                s += Gm[m][l]*pv
                            total += dH*s*(math.comb(a, b1)*math.comb(b, b2))
                out[(a, b)] = total
        return out

    def enclose_F_cauchy(self, x_c, y_c, hx, hy, K=10, c=4):
        ctx.prec = self.prec
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
        rho_x = Fr(hx)*c; rho_y = Fr(hy)*c
        # center jets
        J = self.phi_jet(xc, yc, K + 4)
        JL = self.jet_branches(self.branches('L'), xc, yc, K + 3)
        def lin(Jd, comb, order):
            return {(i, j): sum((cc*Jd[(i+a, j+b)] for (a, b), cc in comb.items()), arb(0)) for i in range(order+1) for j in range(order+1-i)}
        rhoL = lin(JL, FIELDS['rho'], K); U1 = lin(J, FIELDS['U1'], K); U2 = lin(J, FIELDS['U2'], K); rx = lin(J, FIELDS['rho_x'], K); ry = lin(J, FIELDS['rho_y'], K)
        def mul(A, B):
            out = {}
            for (i, j), u in A.items():
                for (k, l), v in B.items():
                    if i+k+j+l <= K:
                        key = (i+k, j+l); out[key] = out.get(key, arb(0)) + u*v*(math.comb(i+k, i)*math.comb(j+l, j))
            return out
        P1 = mul(U1, rx); P2 = mul(U2, ry)
        Fj = {k: rhoL[k] + P1.get(k, arb(0)) + P2.get(k, arb(0)) for k in rhoL}
        dx = arb(0, _fup(hxA)); dy = arb(0, _fup(hyA))
        dxp = [arb(1)]; dyp = [arb(1)]
        for i in range(K+1): dxp.append(dxp[-1]*dx); dyp.append(dyp[-1]*dy)
        poly = arb(0)
        for (i, j), cc in Fj.items(): poly += cc*dxp[i]*dyp[j]/(math.factorial(i)*math.factorial(j))
        # polydisc bounds (orders <= 4 of phi, <= 3 of phi_L)
        B = self.polydisc_field_bounds('base', x_c, y_c, rho_x, rho_y, 4)
        BL = self.polydisc_field_bounds('L', x_c, y_c, rho_x, rho_y, 3)
        def crude(Bd, comb): return sum((abs(cc)*Bd[(a, b)] for (a, b), cc in comb.items()), arb(0))
        M_F = crude(BL, FIELDS['rho']) + crude(B, FIELDS['U1'])*crude(B, FIELDS['rho_x']) + crude(B, FIELDS['U2'])*crude(B, FIELDS['rho_y'])
        theta = arb(1)/c
        tail = M_F*theta**(K+1)*((K+2) - (K+1)*theta)/(1-theta)**2
        return {'F': poly + arb(0, _fup(tail)), 'F_center': Fj[(0, 0)], 'tail': _fup(tail), 'M_F': float(M_F.upper()), 'poly_width': 2*float(poly.rad())}

if __name__ == '__main__':
    import time
    from cert_M import cell_box
    S = FCert2(sys.argv[1], sys.argv[2], prec=256)
    p2 = float(2/S.cl - 1)
    for (r_lo, t_lo) in [(0.01, 1.5), (0.3, 1.0), (3.0, 0.3), (30.0, 1.5), (300.0, 0.7), (1000.0, 0.7), (9000.0, 1.55)]:
        xc, yc, hx, hy = cell_box(r_lo, r_lo*1.02, t_lo, t_lo + math.pi/160)
        t0 = time.time(); o = S.enclose_F_cauchy(xc, yc, hx, hy, K=10, c=4); dt = time.time()-t0
        print('cell r=%g th=%.2f: F in %s (center %s; poly width %.2e; Cauchy tail %.2e; M_F %.3g) -> |F| r^-p2 <= %.5g   t=%.2fs' % (r_lo, t_lo, o['F'].str(6), o['F_center'].str(6), o['poly_width'], o['tail'], o['M_F'], float(abs(o['F']).upper())/r_lo**p2, dt))
