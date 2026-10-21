"""verifier: exact first-order response of the w-only B_3 functional (form F1) on R12 axis data (A = 10.150725,
L = x* = 8.6) to w -> w (1 + eps b chi), b = exp(-(ln(x/x0)/sig)^2), chi a C^infinity cutoff (1 on x < 0.8 x*, 0 on
x > 0.95 x*), as in lead notes S-8 (h).  The f.p. window is placed below the bump (b < e^-81 there), so the finite part
at 0 is identical for +eps and -eps and cancels in the central difference; the response is an ordinary integral.
usage: python3 t_b3_bump.py x0 sig xlo xc eps1 eps2"""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
import jets as J
from manual_axis import ManualAxis, r12_family
from vaxis import B3
A, L = 10.150725, 8.6
x0, sig, xlo, xc = [float(v) for v in sys.argv[1:5]]
epss = [float(v) for v in sys.argv[5:]]
a_, b_ = 0.8 * L, 0.95 * L
f0, cl, xs = r12_family(A, L)


def bumpchi(x, K):
    X = J.var(x, K)
    lg = J.log(X / x0) / sig
    bb = J.exp(-J.mul(lg, lg))
    out = bb.clone()
    one = J.const(torch.ones_like(x), K)
    mid = (x > a_) & (x < b_)
    if mid.any():
        Xm = X[:, mid]
        o = one[:, mid]
        s = (b_ * o - Xm) / (b_ - a_)          # scalar - jet must act on the constant term only
        e1 = J.exp(-J.recip(s))
        e2 = J.exp(-J.recip(o - s))
        S = J.mul(e1, J.recip(e1 + e2))
        out[:, mid] = J.mul(bb[:, mid], S)
    out[:, x >= b_] = 0.0
    return out


def make(eps):
    def f(x, K):
        d = f0(x, K)
        one = J.const(torch.ones_like(x), K)
        d['w'] = J.mul(d['w'], one + eps * bumpchi(x, K))
        return d
    return f


eb = [math.log(a_), math.log(b_)]
vals = {}
for eps in [0.0] + [e for e in epss] + [-e for e in epss]:
    import os
    ad = ManualAxis(make(eps), cl, xs, K=6, xmin=min(1e-4, xlo / 2), hmax=float(os.environ.get("HMAX", 0.05)),
                    q=int(os.environ.get("QQ", 20)), extra_breaks=eb)
    b3 = B3(ad, cl)
    r = b3.fp('F1', xlo, xc, deg=8)
    vals[eps] = r['Bnat']
print('x0 %.2f sig %.2f window [%g, %g]: B_nat(0) = %.8f' % (x0, sig, xlo, xc, vals[0.0]))
for e in epss:
    print('  eps %.1e: dB_nat/deps (central) = %.6e   (one-sided + %.6e, - %.6e)' %
          (e, (vals[e] - vals[-e]) / (2 * e), (vals[e] - vals[0.0]) / e, (vals[0.0] - vals[-e]) / e))

# ---- second evaluation: integrate the pointwise difference (J(+eps) - J(-eps)) / (2 eps) over [xc, x*] (mid part by
# Gauss-Legendre on the axis panels, end part by Gauss-Jacobi in t), so that the large cancelling totals of the f.p.
# never enter (the finite part on [0, xc] is identical for +-eps and is omitted)
from numpy.polynomial import legendre as Lg
from scipy.special import roots_jacobi


def dresp(e, key='F1', nend=60):
    ads = [ManualAxis(make(s * e), cl, xs, K=6, xmin=min(1e-4, xlo / 2), hmax=float(os.environ.get("HMAX", 0.05)),
                      q=int(os.environ.get("QQ", 20)), extra_breaks=eb) for s in (1, -1)]
    bs = [B3(a, cl) for a in ads]
    ad, be = ads[0], bs[0].be
    tc, b = math.log(xc), ad.b
    jlast = ad.P - 1
    brk = np.concatenate([[tc], b[(b > tc) & (b < b[jlast])], [b[jlast]]])
    gq, wq = Lg.leggauss(ad.q + 10)
    mid = 0.0
    for j in range(len(brk) - 1):
        tt = brk[j] + (gq + 1) * (brk[j + 1] - brk[j]) / 2
        xx = np.exp(tt)
        d = bs[0].integrands(xx)[key] - bs[1].integrands(xx)[key]
        mid += float(np.sum(wq * d * xx) * (brk[j + 1] - brk[j]) / 2)
    ts, ta = b[-1], b[jlast]
    tj_, wj_ = roots_jacobi(nend, be - 1, 0.0)
    tt = ta + (tj_ + 1) * (ts - ta) / 2
    xx = np.exp(tt)
    d = (bs[0].integrands(xx)[key] - bs[1].integrands(xx)[key]) * xx * (ts - tt) ** (1 - be)
    endp = float(np.sum(wj_ * d) * ((ts - ta) / 2) ** be)
    return (mid + endp) * xs ** (bs[0].p3 - 2) / (2 * e)


for e in epss:
    print('  eps %.1e: dB_nat/deps (pointwise difference, [xc, x*]) = %.6e' % (e, dresp(e)))
