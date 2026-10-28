"""Rigorous field enclosures over boxes: center Taylor polynomial (point jet, exact cancellations) + remainder from crude ball jets (RTM).

For a linear field f = sum_alpha c_alpha d^alpha phi (|alpha| <= 4) over the box B = X_c + [-hx,hx] x [-hy,hy]:
  f(X) = sum_{|beta|<=K} d^beta f(X_c) (X-X_c)^beta / beta!  +  sum_{|beta|=K+1} d^beta f(xi) (X-X_c)^beta / beta!,  xi in B,
so  f(B) subset  P_K(dx, dy) [ball arithmetic with dx = [-hx,hx], dy = [-hy,hy]]  +  [+- sum_{|beta|=K+1} sup_B |d^beta f| hx^b1 hy^b2 / beta!],
where sup_B |d^beta f| is bounded by the crude RTM ball jets (rtm.RTMState.box_jet) at order |alpha| + K + 1.
"""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, ctx, fmpq
from rtm import RTMState, _arb_fr

FIELDS = {'phi': {(0, 0): 1}, 'psi': {(1, 1): 1}, 'U1': {(1, 2): -1}, 'U2': {(2, 1): 1},
          'rho': {(2, 1): -1, (0, 3): -1}, 'rho_x': {(3, 1): -1, (1, 3): -1}, 'rho_y': {(2, 2): -1, (0, 4): -1},
          'DU11': {(2, 2): -1}, 'DU12': {(1, 3): -1}, 'DU21': {(3, 1): 1}, 'DU22': {(2, 2): 1}}

class BoxEnclosure(RTMState):
    def enclose(self, x_c, y_c, hx, hy, K=5, D=60, fields=None, with_hessian=False):
        """Return dict name -> ball enclosing the field over the box, plus 'x','y' balls and derived F, K_bar, V."""
        ctx.prec = self.prec
        fields = dict(FIELDS) if fields is None else fields
        if with_hessian:
            fields.update({'rho_xx': {(4, 1): -1, (2, 3): -1}, 'rho_xy': {(3, 2): -1, (1, 4): -1}, 'rho_yy': {(2, 3): -1, (0, 5): -1}})
        amax = max(a+b for f in fields.values() for (a, b) in f)
        order = amax + K + 1
        xc = _arb_fr(Fr(x_c)); yc = _arb_fr(Fr(y_c)); hxa = Fr(hx); hya = Fr(hy)
        Jc = self.phi_jet(xc, yc, order)                      # point jet at the center (cap set inside)
        if ctx.cap < max(order+1, D+1): ctx.cap = max(order+1, D+1)
        Jb, xb, yb = self.box_jet(x_c, y_c, hx, hy, N=order, D=D)   # crude ball jet over the box
        dx = arb(0, float(_arb_fr(hxa).upper())); dy = arb(0, float(_arb_fr(hya).upper()))
        hxA = _arb_fr(hxa); hyA = _arb_fr(hya)
        out = {'x': xb, 'y': yb}
        for name, comb in fields.items():
            poly = arb(0); rem = arb(0)
            for b1 in range(K+2):
                for b2 in range(K+2-b1):
                    if b1+b2 <= K:
                        coef = sum((c*Jc[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                        poly += coef*dx**b1*dy**b2/(math.factorial(b1)*math.factorial(b2))
                    elif b1+b2 == K+1:
                        coef = sum((c*Jb[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                        rem += arb(abs(coef).upper())*hxA**b1*hyA**b2/(math.factorial(b1)*math.factorial(b2))
            out[name] = poly + arb(0, float(rem.upper()))
            out[name+'_remainder'] = float(rem.upper())
        out['V1'] = self.cl*xb + out['U1']; out['V2'] = self.cl*yb + out['U2']
        out['F'] = out['V1']*out['rho_x'] + out['V2']*out['rho_y'] - out['rho']
        out['K'] = out['rho'] - xb*out['rho_x'] - yb*out['rho_y']
        return out

def Mmin(out, cl):
    M11 = 2*cl + 1 + out['DU11'] + out['rho_y']; M22 = 2*cl + 1 + out['DU22']; M12 = (out['DU12'] + out['DU21'])/2 - out['rho_x']/2
    tr = M11 + M22; det = M11*M22 - M12*M12; disc = (tr/2)**2 - det
    # lambda_min = tr/2 - sqrt(disc); disc >= 0 for symmetric matrices; use nonneg part
    return tr/2 - (disc if disc.lower() >= 0 else arb(disc.mid(), disc.rad()).abs_upper()).sqrt() if False else tr/2 - disc.sqrt_pos() if hasattr(disc, 'sqrt_pos') else tr/2 - abs(disc).sqrt()

if __name__ == '__main__':
    import time
    S = BoxEnclosure(sys.argv[1], prec=256)
    cl = S.cl
    for (x0, y0, hx, hy, K) in [(0, 0, 0.05, 0.05, 5), (0, 0, 0.2, 0.2, 5), (0.5, 0.5, 0.03, 0.03, 5), (0.5, 0.5, 0.08, 0.08, 5), (3, 3, 0.2, 0.2, 5), (0, 30, 1.5, 1.5, 5), (300, 300, 20, 20, 5), (0, 1e4, 500, 500, 5), (1e6, 1e6, 5e4, 5e4, 5)]:
        t0 = time.time()
        try:
            o = S.enclose(x0, y0, hx, hy, K=K)
            lm = Mmin(o, cl)
            print('box (%g,%g) h=(%g,%g) K=%d: lam_min in %s width %.2e | rho %s (rem %.1e) | rho_y %s | F %s | K_bar %s  t=%.2fs' % (x0, y0, hx, hy, K, lm.str(7), 2*float(lm.rad()), o['rho'].str(6), o['rho_remainder'], o['rho_y'].str(6), o['F'].str(4), o['K'].str(5), time.time()-t0))
        except ValueError as e:
            print('box (%g,%g) h=(%g,%g): %s' % (x0, y0, hx, hy, e))
