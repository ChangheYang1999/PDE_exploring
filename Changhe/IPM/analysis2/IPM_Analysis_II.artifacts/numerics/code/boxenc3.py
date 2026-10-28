"""Rigorous field enclosures over boxes, version 3 (T1 representation for the crude derivative bounds).

Center Taylor polynomial of degree K (exact point jet of phi, cancellations exact) + remainder:
  |R_K| <= sum_{|beta|=K+1} sup_B |d^beta f| hx^b1 hy^b2 / beta!,
with sup_B |d^gamma phi| (|gamma| = |alpha| + K + 1) bounded termwise:
  d^gamma [H_m G_m(q)] = sum_{beta<=gamma} C(gamma,beta) d^beta H_m . sum_l G_m^{(l)}(q) P_{gamma-beta,l}(x,y)   (all factors in absolute value),
  G_m = sum_j g_{mj},  g_{mj}(q) = R^{beta_j} L_{mj}(t), beta_j = p_j - m, t = 1 - u, u = 1/R, R = 1 + q,
  L_{mj}(t) = sum_{h<=4-m} c_{mhj} t^h + t^{w} sum_n g_{mnj} N_n P_n(2t - 1), w = max(5 - m, 0)   (T1 coordinates, O(1) coefficients).
Bounds over the q-interval I of the box:
  |L^{(k)}(t)| <= Lambda_k := sum_h |c_h| (h)_k t_hi^{h-k} + sum_{i<=min(k,w)} C(k,i) (w)_i t_hi^{w-i} 2^{k-i} sum_n |g_n| N_n Pi_{n,k-i},
     Pi_{n,s} := sup_{z in [z_lo,z_hi]} |P_n^{(s)}(z)| <= sum_{k<=n-s} |P_n^{(s+k)}(z_mid)| (dz/2)^k / k!   (exact finite Taylor expansion of a polynomial),
  |d^a/dq^a L(t(q))| <= D_a := sum_{k=1}^a Lambda_k Lah(a,k) u_hi^{a+k}  (Faa di Bruno; t^{(j)}(q) = (-1)^{j+1} j! u^{j+1}; Lah(a,k) = C(a-1,k-1) a!/k!), D_0 = Lambda_0,
  |g^{(l)}| <= Gamma_l := sum_a C(l,a) |(beta)_{l-a}| max_I R^{beta-l+a} D_a.
All sums have nonnegative terms: no dependency problem. Every bound is an arb upper bound.
"""
import math, sys, os, json
def _fup(x):
    """binary64 >= the upper bound of the arb x (outward rounding of a radius conversion)."""
    return math.nextafter(float(x.upper()), math.inf)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, acb, ctx, fmpq
from ipm_arb import State
from boxenc2 import P_gamma, FIELDS, HESS

def _arb_fr(fr): return arb(fmpq(fr.numerator, fr.denominator))
def falling(b, n):
    out = arb(1)
    for i in range(n): out *= (b - i)
    return out
def lah(a, k): return math.comb(a-1, k-1)*math.factorial(a)//math.factorial(k) if 1 <= k <= a else 0

class BoxEnclosure3(State):
    def __init__(self, exact_json, checkpoint_json, prec=256):
        super().__init__(exact_json, prec)
        d = json.load(open(checkpoint_json))
        low = [Fr(float.fromhex(h)) for h in d['P_hex']]
        num, den = d['input_exact_for_checkpoint']['a000_exact'].split('/'); low[0] = Fr(int(num), int(den))
        high = [Fr(float.fromhex(h)) for h in d['high_hex']]
        NN = [Fr(float.fromhex(h)) for h in d['frozen_Nn_hex']]
        LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]
        HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]
        ctx.prec = prec
        self.lowabs = {}; self.highabs = {}
        for v, (m, k, j) in zip(low, LOW): self.lowabs.setdefault((m, j), {})[k-m] = abs(_arb_fr(v))
        for v, (m, n, j) in zip(high, HIGH): self.highabs.setdefault((m, j), {})[n] = abs(_arb_fr(v*NN[n]))
        # consistency of the T1 reading with the canonical coefficients is checked separately (ipm_arb T1 test)

    def legendre_derivs(self, z, nmax=25):
        """P_n^{(k)}(z) for n, k <= nmax (arb point z) via (n+1) P_{n+1}^{(k)} = (2n+1)[z P_n^{(k)} + k P_n^{(k-1)}] - n P_{n-1}^{(k)}."""
        P = [[arb(0)]*(nmax+1) for _ in range(nmax+1)]
        P[0][0] = arb(1)
        if nmax >= 1: P[1][0] = z; P[1][1] = arb(1)
        for n in range(1, nmax):
            for k in range(nmax+1):
                term = z*P[n][k] + (k*P[n][k-1] if k else 0)
                P[n+1][k] = ((2*n+1)*term - n*P[n-1][k])/(n+1)
        return P

    def radial_bounds(self, q_lo, q_hi, order):
        """Gamma[(m,j)][l] upper bounds of sup_{q in [q_lo,q_hi]} |g_{mj}^{(l)}(q)| for l <= order."""
        R_lo = 1 + q_lo; R_hi = 1 + q_hi; u_hi = 1/R_lo; u_lo = 1/R_hi
        t_lo = 1 - u_hi; t_hi = 1 - u_lo
        z_lo = 2*t_lo - 1; z_hi = 2*t_hi - 1; z_mid = (z_lo + z_hi)/2; hz = arb((z_hi - z_lo).upper())/2
        PD = self.legendre_derivs(z_mid)
        nmax = 25
        Pi = [[arb(0)]*(nmax+1) for _ in range(nmax+1)]
        hzp = [arb(1)]
        for k in range(1, nmax+1): hzp.append(hzp[-1]*hz)
        for n in range(nmax+1):
            for s in range(n+1):
                acc = arb(0)
                for k in range(n-s+1): acc += abs(PD[n][s+k])*hzp[k]/math.factorial(k)
                Pi[n][s] = acc
        t_hi_p = [arb(1)]
        for k in range(1, 30): t_hi_p.append(t_hi_p[-1]*t_hi)
        u_hi_p = [arb(1)]
        for k in range(1, 2*order+3): u_hi_p.append(u_hi_p[-1]*u_hi)
        Gam = {}
        for (m, j) in self.A:
            beta = self.p[j] - m; w = max(5-m, 0)
            lows = self.lowabs.get((m, j), {}); highs = self.highabs.get((m, j), {})
            Lam = []
            for k in range(order+1):
                acc = arb(0)
                for h, c in lows.items():
                    if h >= k: acc += c*math.perm(h, k)*t_hi_p[h-k]
                for i in range(min(k, w)+1):
                    s = k - i
                    inner = arb(0)
                    for n, g in highs.items():
                        if s <= n: inner += g*Pi[n][s]
                    acc += math.comb(k, i)*math.perm(w, i)*t_hi_p[w-i]*(2**s)*inner
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
            Gam[(m, j)] = G
        return Gam

    def crude_phi(self, xabs, yabs, q_lo, q_hi, order):
        """Upper bounds of sup_B |d^gamma phi| for |gamma| = order, with |x| <= xabs, |y| <= yabs on the box."""
        Gam = self.radial_bounds(q_lo, q_hi, order)
        Gm = {m: [sum((Gam[(m, j)][l] for j in range(4)), arb(0)) for l in range(order+1)] for m in range(10)}
        xp = [arb(1)]; yp = [arb(1)]
        for i in range(order+1): xp.append(xp[-1]*xabs); yp.append(yp[-1]*yabs)
        rabs = (xabs*xabs + yabs*yabs).sqrt()
        rp = [arb(1)]
        for i in range(19): rp.append(rp[-1]*rabs)
        out = {}
        for a in range(order+1):
            b = order - a
            total = arb(0)
            for m in range(10):
                n = 2*m
                for b1 in range(min(a, n)+1):
                    for b2 in range(min(b, n-b1)+1):
                        k = b1 + b2
                        dH = math.perm(n, k)*rp[n-k]            # |d^beta H_m| <= (2m)!/(2m-k)! r^{2m-k}
                        Pl = P_gamma((a-b1, b-b2))
                        s = arb(0)
                        for l, poly in Pl.items():
                            pv = arb(0)
                            for (i, jj), c in poly.items(): pv += abs(c)*xp[i]*yp[jj]
                            s += Gm[m][l]*pv
                        total += dH*s*(math.comb(a, b1)*math.comb(b, b2))
            out[(a, b)] = total
        return out

    def enclose(self, x_c, y_c, hx, hy, K=8, fields=None, with_hessian=False):
        ctx.prec = self.prec
        fields = dict(FIELDS) if fields is None else dict(fields)
        if with_hessian: fields.update(HESS)
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
        xb = xc + arb(0, _fup(hxA)); yb = yc + arb(0, _fup(hyA))
        xabs = abs(xc) + hxA; yabs = abs(yc) + hyA
        xmin = (abs(xc) - hxA); ymin = (abs(yc) - hyA)
        xmin = xmin if xmin > 0 else arb(0); ymin = ymin if ymin > 0 else arb(0)
        q_lo = xmin*xmin + ymin*ymin; q_hi = xabs*xabs + yabs*yabs
        amax = max(a+b for f in fields.values() for (a, b) in f)
        Jc = self.phi_jet(xc, yc, amax + K)
        orders = sorted(set(a+b for f in fields.values() for (a, b) in f))
        crude = {}
        for o in orders: crude.update(self.crude_phi(xabs, yabs, q_lo, q_hi, o + K + 1))
        dx = arb(0, _fup(hxA)); dy = arb(0, _fup(hyA))
        dxp = [arb(1)]; dyp = [arb(1)]; hxp = [arb(1)]; hyp = [arb(1)]
        for i in range(K+2): dxp.append(dxp[-1]*dx); dyp.append(dyp[-1]*dy); hxp.append(hxp[-1]*hxA); hyp.append(hyp[-1]*hyA)
        out = {'x': xb, 'y': yb, 'q_lo': q_lo, 'q_hi': q_hi}
        for name, comb in fields.items():
            poly = arb(0)
            for b1 in range(K+1):
                for b2 in range(K+1-b1):
                    coef = sum((c*Jc[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                    poly += coef*dxp[b1]*dyp[b2]/(math.factorial(b1)*math.factorial(b2))
            rem = arb(0)
            for b1 in range(K+2):
                b2 = K+1-b1
                coef = sum((abs(c)*crude[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                rem += coef*hxp[b1]*hyp[b2]/(math.factorial(b1)*math.factorial(b2))
            out[name] = poly + arb(0, _fup(rem))
            out[name+'_rem'] = _fup(rem)
        if all(k in out for k in ('U1', 'U2', 'rho', 'rho_x', 'rho_y')):
            out['V1'] = self.cl*xb + out['U1']; out['V2'] = self.cl*yb + out['U2']
            out['F'] = out['V1']*out['rho_x'] + out['V2']*out['rho_y'] - out['rho']
            out['K'] = out['rho'] - xb*out['rho_x'] - yb*out['rho_y']
        return out

def Mmin(out, cl):
    M11 = 2*cl + 1 + out['DU11'] + out['rho_y']; M22 = 2*cl + 1 + out['DU22']; M12 = (out['DU12'] + out['DU21'])/2 - out['rho_x']/2
    half = (M11 - M22)/2; disc = half*half + M12*M12        # stable form, disc >= 0 without cancellation
    return (M11 + M22)/2 - disc.sqrt(), (M11, M22, M12)

if __name__ == '__main__':
    import time
    S = BoxEnclosure3(sys.argv[1], sys.argv[2], prec=256)
    cl = S.cl
    tests = [(0, 0, 0.05, 0.05, 8), (0, 0, 0.1, 0.1, 8), (0.3, 0.3, 0.005, 0.005, 8), (0.3, 0.3, 0.01, 0.01, 8), (0.5, 0.5, 0.005, 0.005, 8), (0.5, 0.5, 0.01, 0.01, 8), (1, 1, 0.01, 0.01, 8), (1, 1, 0.02, 0.02, 8), (3, 3, 0.05, 0.05, 8), (3, 3, 0.1, 0.1, 8), (0, 30, 0.5, 0.5, 8), (0, 30, 1, 1, 8), (300, 300, 5, 5, 8), (300, 300, 10, 10, 8), (0, 1e4, 200, 200, 8)]
    for (x0, y0, hx, hy, K) in tests:
        t0 = time.time()
        o = S.enclose(x0, y0, hx, hy, K=K)
        lm, _ = Mmin(o, cl)
        print('box (%g,%g) h=(%g,%g) K=%d: lam_min %s w=%.1e | rho %s rem %.1e | rho_y %s rem %.1e | DU22 rem %.1e | F %s | t=%.2fs' % (x0, y0, hx, hy, K, lm.str(7), 2*float(lm.rad()), o['rho'].str(6), o['rho_rem'], o['rho_y'].str(6), o['rho_y_rem'], o['DU22_rem'], o['F'].str(4), time.time()-t0))

# ---------------- exact center-jet enclosure of the residual F and of K_bar (products handled at the jet level) ----------------
def _jet_shift(J, a, b, order):
    """jet of d^a_x d^b_y phi as a dict beta -> arb for |beta| <= order."""
    return {(i, j): J[(i+a, j+b)] for i in range(order+1) for j in range(order+1-i)}

def _jet_lin(J, comb, order):
    out = {}
    for i in range(order+1):
        for j in range(order+1-i):
            out[(i, j)] = sum((c*J[(i+a, j+b)] for (a, b), c in comb.items()), arb(0))
    return out

def _jet_mul(A, B, order):
    out = {}
    for (i, j), u in A.items():
        if u.is_zero(): continue
        for (k, l), v in B.items():
            if i+k+j+l <= order and not v.is_zero():
                key = (i+k, j+l); out[key] = out.get(key, arb(0)) + u*v*(math.comb(i+k, i)*math.comb(j+l, j))
    return out      # Taylor-coefficient jets would multiply without binomials; here jets are DERIVATIVES, hence the binomial factors (Leibniz)

def _jet_coord(xc, which, order):
    """jet of the coordinate function x (which=0) or y (which=1) at the center."""
    out = {(i, j): arb(0) for i in range(order+1) for j in range(order+1-i)}
    out[(0, 0)] = xc; out[(1, 0) if which == 0 else (0, 1)] = arb(1)
    return out

def _crude_lin(crude, comb, a, b):
    return sum((abs(c)*crude[(a+i, b+j)] for (i, j), c in comb.items()), arb(0))

def enclose_F(self, x_c, y_c, hx, hy, K=8):
    """Balls containing F = V.grad rho - rho and K_bar = rho - X.grad rho over the box (exact center jets of F, K_bar; crude Leibniz remainders)."""
    ctx.prec = self.prec
    xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
    xb = xc + arb(0, _fup(hxA)); yb = yc + arb(0, _fup(hyA))
    xabs = abs(xc) + hxA; yabs = abs(yc) + hyA
    xmin = abs(xc) - hxA; ymin = abs(yc) - hyA
    xmin = xmin if xmin > 0 else arb(0); ymin = ymin if ymin > 0 else arb(0)
    q_lo = xmin*xmin + ymin*ymin; q_hi = xabs*xabs + yabs*yabs
    order = K + 4
    J = self.phi_jet(xc, yc, order)
    rho = _jet_lin(J, FIELDS['rho'], K); rx = _jet_lin(J, FIELDS['rho_x'], K); ry = _jet_lin(J, FIELDS['rho_y'], K)
    U1 = _jet_lin(J, FIELDS['U1'], K); U2 = _jet_lin(J, FIELDS['U2'], K)
    X = _jet_coord(xc, 0, K); Y = _jet_coord(yc, 1, K)
    V1 = {k: self.cl*X[k] + U1[k] for k in X}; V2 = {k: self.cl*Y[k] + U2[k] for k in Y}
    Fj = _jet_mul(V1, rx, K); t2 = _jet_mul(V2, ry, K)
    Fj = {k: Fj.get(k, arb(0)) + t2.get(k, arb(0)) - rho[k] for k in rho}
    Kx = _jet_mul(X, rx, K); Ky = _jet_mul(Y, ry, K)
    Kj = {k: rho[k] - Kx.get(k, arb(0)) - Ky.get(k, arb(0)) for k in rho}
    # polynomial parts over the box
    dx = arb(0, _fup(hxA)); dy = arb(0, _fup(hyA))
    dxp = [arb(1)]; dyp = [arb(1)]; hxp = [arb(1)]; hyp = [arb(1)]
    for i in range(K+2): dxp.append(dxp[-1]*dx); dyp.append(dyp[-1]*dy); hxp.append(hxp[-1]*hxA); hyp.append(hyp[-1]*hyA)
    def poly(jet):
        s = arb(0)
        for (i, j), c in jet.items(): s += c*dxp[i]*dyp[j]/(math.factorial(i)*math.factorial(j))
        return s
    # crude bounds of all phi derivatives of orders 3..K+5 over the box
    crude = {}
    for o in range(3, K+6): crude.update(self.crude_phi(xabs, yabs, q_lo, q_hi, o))
    def cr(comb, i, j): return _crude_lin(crude, comb, i, j)
    def cr_coord(which, i, j):
        if i+j == 0: return xabs if which == 0 else yabs
        if (i, j) == ((1, 0) if which == 0 else (0, 1)): return arb(1)
        return arb(0)
    remF = arb(0); remK = arb(0)
    for b1 in range(K+2):
        b2 = K+1-b1
        # |d^beta F| <= sum_gamma C(beta,gamma) |d^gamma V1| |d^(beta-gamma) rho_x| + same with V2, rho_y + |d^beta rho|
        accF = cr(FIELDS['rho'], b1, b2); accK = cr(FIELDS['rho'], b1, b2)
        for g1 in range(b1+1):
            for g2 in range(b2+1):
                cb = math.comb(b1, g1)*math.comb(b2, g2)
                v1 = self.cl*cr_coord(0, g1, g2) + cr(FIELDS['U1'], g1, g2); v2 = self.cl*cr_coord(1, g1, g2) + cr(FIELDS['U2'], g1, g2)
                accF += cb*(v1*cr(FIELDS['rho_x'], b1-g1, b2-g2) + v2*cr(FIELDS['rho_y'], b1-g1, b2-g2))
                accK += cb*(cr_coord(0, g1, g2)*cr(FIELDS['rho_x'], b1-g1, b2-g2) + cr_coord(1, g1, g2)*cr(FIELDS['rho_y'], b1-g1, b2-g2))
        w = hxp[b1]*hyp[b2]/(math.factorial(b1)*math.factorial(b2))
        remF += accF*w; remK += accK*w
    out = {'x': xb, 'y': yb, 'F': poly(Fj) + arb(0, _fup(remF)), 'F_rem': _fup(remF), 'K': poly(Kj) + arb(0, _fup(remK)), 'K_rem': _fup(remK),
           'F_center': Fj[(0, 0)], 'K_center': Kj[(0, 0)]}
    return out
BoxEnclosure3.enclose_F = enclose_F
