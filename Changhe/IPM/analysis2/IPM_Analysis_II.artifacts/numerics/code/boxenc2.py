"""Rigorous field enclosures over boxes, version 2.

f(X) over B = X_c + [-hx,hx]x[-hy,hy]:  f(X) = sum_{|beta|<=K} d^beta f(X_c) dX^beta/beta!  +  R_K,
  |R_K| <= sum_{|beta|=K+1} sup_B |d^beta f| hx^b1 hy^b2 / beta!.
Center jet d^beta f(X_c): exact point evaluation (ipm_arb directional series, mixed partials solved exactly; radii ~1e-60).
Crude sup_B |d^gamma phi| for |gamma| = |alpha| + K + 1 by the Leibniz / chain rule, termwise over the 10 harmonics:
  d^gamma [H_m(x,y) G_m(q)] = sum_{beta<=gamma} C(gamma,beta) d^beta H_m . sum_l G_m^{(l)}(q) P_{gamma-beta,l}(x,y),
  G_m = sum_j g_{mj} (branches summed first), G_m^{(l)} over the q-interval from the radial Taylor models (rtm.radial_model:
  Taylor coefficients at q_c plus Cauchy tail derivative bounds), d^beta H_m = (2m)!/(2m-|beta|)! Re(i^{b2} z^{2m-|beta|}),
  P_{gamma,l} universal integer polynomials: P_{gamma+e_x,l} = 2x P_{gamma,l-1} + d_x P_{gamma,l} (same for y), P_{0,0} = 1.
"""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, acb, ctx, fmpq
from rtm import RTMState, _arb_fr

FIELDS = {'phi': {(0, 0): 1}, 'psi': {(1, 1): 1}, 'U1': {(1, 2): -1}, 'U2': {(2, 1): 1},
          'rho': {(2, 1): -1, (0, 3): -1}, 'rho_x': {(3, 1): -1, (1, 3): -1}, 'rho_y': {(2, 2): -1, (0, 4): -1},
          'DU11': {(2, 2): -1}, 'DU12': {(1, 3): -1}, 'DU21': {(3, 1): 1}, 'DU22': {(2, 2): 1}}
HESS = {'rho_xx': {(4, 1): -1, (2, 3): -1}, 'rho_xy': {(3, 2): -1, (1, 4): -1}, 'rho_yy': {(2, 3): -1, (0, 5): -1}}

# ---------- universal polynomials P_{gamma,l} ----------
_PCACHE = {(0, 0): {0: {(0, 0): 1}}}
def _padd(P, k, v):
    if v == 0: return
    P[k] = P.get(k, 0) + v
    if P[k] == 0: del P[k]
def P_gamma(gamma):
    """dict l -> polynomial dict {(i,j): int} with d^gamma[g(q)] = sum_l g^{(l)}(q) P_l(x,y)."""
    if gamma in _PCACHE: return _PCACHE[gamma]
    a, b = gamma
    if a > 0: prev = P_gamma((a-1, b)); var = 0
    else: prev = P_gamma((a, b-1)); var = 1
    out = {}
    for l, poly in prev.items():
        # 2x P_{l} -> contributes to l+1 ; d_var P_l -> contributes to l
        for (i, j), c in poly.items():
            key = (i+1, j) if var == 0 else (i, j+1)
            _padd(out.setdefault(l+1, {}), key, 2*c)
            if var == 0 and i > 0: _padd(out.setdefault(l, {}), (i-1, j), i*c)
            if var == 1 and j > 0: _padd(out.setdefault(l, {}), (i, j-1), j*c)
    out = {l: p for l, p in out.items() if p}
    _PCACHE[gamma] = out
    return out

def poly_eval(poly, xpows, ypows):
    s = arb(0)
    for (i, j), c in poly.items(): s += xpows[i]*ypows[j]*c
    return s

class BoxEnclosure2(RTMState):
    def crude_phi_derivatives(self, xb, yb, q_c, delta, order, D):
        """Balls containing d^gamma phi over the box for all |gamma| = order (dict gamma -> arb)."""
        ctx.cap = max(ctx.cap, D+1, order+2)
        # radial models and G_m^{(l)} over the interval eps in [-delta, delta]
        eps = arb(0, float(delta.upper()))
        epow = [arb(1)]
        for d in range(1, D+1): epow.append(epow[-1]*eps)
        Gm = {}
        for m in range(10):
            Gl = [arb(0)]*(order+1)
            for j in range(4):
                gd, taus = self.radial_model(m, j, q_c, delta, D, order)
                for l in range(order+1):
                    s = arb(0)
                    for d in range(l, D+1):
                        s += gd[d]*(math.factorial(d)//math.factorial(d-l))*epow[d-l]
                    Gl[l] = Gl[l] + s + arb(0, float(taus[l].upper()))
            Gm[m] = Gl
        # powers of x, y balls and complex powers for harmonics
        xpows = [arb(1)]; ypows = [arb(1)]
        for i in range(order+1): xpows.append(xpows[-1]*xb); ypows.append(ypows[-1]*yb)
        z = acb(xb, yb); zpows = [acb(1)]
        for n in range(1, 19): zpows.append(zpows[-1]*z)
        def dH(m, b1, b2):
            n = 2*m; k = b1+b2
            if k > n: return arb(0)
            val = zpows[n-k]*(acb(0, 1)**b2)*(math.factorial(n)//math.factorial(n-k))
            return val.real
        out = {}
        for a in range(order+1):
            gamma = (a, order-a)
            total = arb(0)
            for m in range(10):
                for b1 in range(min(a, 2*m)+1):
                    for b2 in range(min(gamma[1], 2*m-b1)+1):
                        dHm = dH(m, b1, b2)
                        if dHm.is_zero(): continue
                        rest = (a-b1, gamma[1]-b2)
                        Pl = P_gamma(rest)
                        s = arb(0)
                        for l, poly in Pl.items(): s += Gm[m][l]*poly_eval(poly, xpows, ypows)
                        total += dHm*s*(math.comb(a, b1)*math.comb(gamma[1], b2))
            out[gamma] = total
        return out

    def enclose(self, x_c, y_c, hx, hy, K=6, D=60, fields=None, with_hessian=False):
        ctx.prec = self.prec
        fields = dict(FIELDS) if fields is None else dict(fields)
        if with_hessian: fields.update(HESS)
        amax = max(a+b for f in fields.values() for (a, b) in f)
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
        xb = xc + arb(0, float(hxA.upper())); yb = yc + arb(0, float(hyA.upper()))
        q_c = xc*xc + yc*yc
        eps0 = xb*xb + yb*yb - q_c; delta = arb(abs(eps0).upper())
        Jc = self.phi_jet(xc, yc, amax + K)
        crude = {}
        for amin_order in sorted(set(a+b for f in fields.values() for (a, b) in f)):
            crude.update(self.crude_phi_derivatives(xb, yb, q_c, delta, amin_order + K + 1, D))
        dx = arb(0, float(hxA.upper())); dy = arb(0, float(hyA.upper()))
        dxp = [arb(1)]; dyp = [arb(1)]
        for i in range(K+1): dxp.append(dxp[-1]*dx); dyp.append(dyp[-1]*dy)
        hxp = [arb(1)]; hyp = [arb(1)]
        for i in range(K+2): hxp.append(hxp[-1]*hxA); hyp.append(hyp[-1]*hyA)
        out = {'x': xb, 'y': yb, 'q_c': q_c, 'delta': delta}
        for name, comb in fields.items():
            poly = arb(0)
            for b1 in range(K+1):
                for b2 in range(K+1-b1):
                    coef = sum((c*Jc[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                    poly += coef*dxp[b1]*dyp[b2]/(math.factorial(b1)*math.factorial(b2))
            rem = arb(0)
            for b1 in range(K+2):
                b2 = K+1-b1
                coef = sum((c*crude[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                rem += arb(abs(coef).upper())*hxp[b1]*hyp[b2]/(math.factorial(b1)*math.factorial(b2))
            out[name] = poly + arb(0, float(rem.upper()))
            out[name+'_rem'] = float(rem.upper())
        out['V1'] = self.cl*xb + out['U1']; out['V2'] = self.cl*yb + out['U2']
        out['F'] = out['V1']*out['rho_x'] + out['V2']*out['rho_y'] - out['rho']
        out['K'] = out['rho'] - xb*out['rho_x'] - yb*out['rho_y']
        return out

def Mmin(out, cl):
    M11 = 2*cl + 1 + out['DU11'] + out['rho_y']; M22 = 2*cl + 1 + out['DU22']; M12 = (out['DU12'] + out['DU21'])/2 - out['rho_x']/2
    tr = M11 + M22; det = M11*M22 - M12*M12; disc = (tr/2)**2 - det
    return tr/2 - abs(disc).sqrt(), (M11, M22, M12)

if __name__ == '__main__':
    import time
    S = BoxEnclosure2(sys.argv[1], prec=256)
    cl = S.cl
    for (x0, y0, hx, hy, K) in [(0, 0, 0.05, 0.05, 6), (0, 0, 0.2, 0.2, 8), (0.5, 0.5, 0.03, 0.03, 6), (0.5, 0.5, 0.08, 0.08, 8), (3, 3, 0.2, 0.2, 6), (3, 3, 0.4, 0.4, 8), (0, 30, 1.5, 1.5, 6), (300, 300, 20, 20, 6), (0, 1e4, 500, 500, 6), (1e6, 1e6, 5e4, 5e4, 6)]:
        t0 = time.time()
        try:
            o = S.enclose(x0, y0, hx, hy, K=K)
            lm, _ = Mmin(o, cl)
            print('box (%g,%g) h=(%g,%g) K=%d: lam_min %s width %.1e | rho %s rem %.1e | rho_y %s rem %.1e | F %s | K_bar %s  t=%.2fs' % (x0, y0, hx, hy, K, lm.str(7), 2*float(lm.rad()), o['rho'].str(6), o['rho_rem'], o['rho_y'].str(6), o['rho_y_rem'], o['F'].str(4), o['K'].str(5), time.time()-t0))
        except ValueError as e:
            print('box (%g,%g) h=(%g,%g): %s' % (x0, y0, hx, hy, e))
