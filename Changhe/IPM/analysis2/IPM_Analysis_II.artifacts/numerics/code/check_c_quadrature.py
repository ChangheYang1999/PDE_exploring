"""N1 check: c[rho_bar] = (1/pi) int_{R^2} x y r^-4 d_x rho dX (SPEC S3.2), evaluated WITHOUT the center relation:
inner disk r <= R_cut by Gauss-Legendre in (log r, theta) on the quadrant (x4 by parity) with the arb evaluator (midpoints),
tail r > R_cut analytically from the exact far-field density sectors (rho_x from the polar rules), truncated at q <= qmax with the next
omitted sector as an error indicator. Floating-point diagnostic (not yet certified)."""
import sys, os, math, json
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipm_arb import State
from flint import arb

def dx_sine_series(S, sigma):
    """d_x [r^sigma sum_k s_k sin(k theta)] = r^(sigma-1) sum ... : returns sine dict and exponent sigma-1.
    d_x[r^s sin k] = r^(s-1)[ ((s-k)/2) sin((k+1)th) + ((s+k)/2) sin((k-1)th) ]."""
    out = {}
    for k, v in S.items():
        for kk, c in ((k+1, v*(sigma-k)/2), (k-1, v*(sigma+k)/2)):
            if kk < 0: kk, c = -kk, -c
            if kk == 0 or c == 0: continue
            out[kk] = out.get(kk, 0) + c
    return out

def main(state_json, farfield_json, R_cut=20.0, ns=400, nth=64):
    S = State(state_json, prec=128)
    ff = json.load(open(farfield_json))
    # Gauss-Legendre in s = log r on [log r_min, log R_cut], r_min small (integrand ~ r^2 near 0 in these variables: x y r^-4 rho_x dX = sin cos rho_x r^-1 dr dth = sin cos rho_x ds dth)
    s_lo, s_hi = math.log(1e-6), math.log(R_cut)
    xs, ws = np.polynomial.legendre.leggauss(ns); xt, wt = np.polynomial.legendre.leggauss(nth)
    svals = 0.5*(s_hi-s_lo)*xs + 0.5*(s_hi+s_lo); ws = 0.5*(s_hi-s_lo)*ws
    th = 0.25*math.pi*(xt+1); wt = 0.25*math.pi*wt
    total = 0.0
    for s, w in zip(svals, ws):
        r = math.exp(s)
        for t, wth in zip(th, wt):
            x, y = r*math.cos(t), r*math.sin(t)
            f = S.fields(x, y, order=4)
            total += w*wth*math.sin(t)*math.cos(t)*float(f['rho_x'].mid())
    inner = 4*total/math.pi
    # tail: rho_x = sum_sectors r^(alpha-1) D_sector(theta); int_{R}^{inf} r^(alpha-1) r^-1 dr = R^(alpha-1)/(1-alpha) for alpha < 1; angular int_0^{pi/2} sin cos sin(k th) dth
    def ang(k):   # int_0^{pi/2} sin(th) cos(th) sin(k th) dth = (1/2) int sin(2th) sin(k th)
        if k == 2: return math.pi/8
        return 0.5*((math.sin((2-k)*math.pi/2)/(2-k)) - (math.sin((2+k)*math.pi/2)/(2+k)))/2*2/2  # (1/2)[sin((2-k)x)/(2(2-k)) - sin((2+k)x)/(2(2+k))] at pi/2
    tail = 0.0; last = 0.0
    secs = sorted(ff['density_sectors_G'].items(), key=lambda kv: -float(Fr(kv[1]['exponent'])))
    for name, sec in secs:
        alpha = float(Fr(sec['exponent'])); Sdict = {int(k): float(v['float']) for k, v in sec['series'].items()}
        D = dx_sine_series(Sdict, alpha)
        contrib = sum(c*ang(k) for k, c in D.items())*R_cut**(alpha-1)/(1-alpha)
        tail += contrib; last = contrib
    tail *= 4/math.pi
    omitted_exp = float(Fr(ff['gamma'])) - 2*(ff['qmax']+1)
    print('R_cut=%g ns=%d nth=%d: inner=%.15f tail=%.15f total c=%.15f ; 1-c_l=%.15f ; diff=%.3e ; last sector contrib=%.2e ; omitted exponent %.2f' % (R_cut, ns, nth, inner, tail, inner+tail, 1-float(Fr(ff['cl'])), inner+tail-(1-float(Fr(ff['cl']))), last*4/math.pi, omitted_exp))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
