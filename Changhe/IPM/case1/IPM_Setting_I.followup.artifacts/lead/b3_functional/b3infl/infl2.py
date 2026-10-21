"""B_3 response to localized perturbations of w on X3, with the finite part at 0 computed from a fit window that the
perturbation does not touch. Configurations: W1 = run-1 window (xlo, xc) = (0.02, 0.35) x*, W2 = (0.005, 0.06) x*.
A bump centred at x0 is used only with a window ending below x0 e^(-4 s) (otherwise the polynomial extrapolation of
the finite part sees the bump; such responses are artefacts of the estimator, not of B_3).
Usage: python3 infl2.py traces.npz out.npz"""
import sys
import numpy as np
from b3core import b3_one, load, CFG

x, w, wp, wpp, cl = load(sys.argv[1])
A = 2 * cl - 1
u = np.log(x)
W1 = dict(CFG)
W2 = dict(CFG, xlo=0.005, xc=0.06, K=6)
for nm, cf in (('W1', W1), ('W2', W2), ('W2 K8', dict(W2, K=8)), ('W2 xc.1', dict(W2, xc=0.1))):
    Bo, Bi, d0 = b3_one(x, w, wp, wpp, cl, cf, both=True)
    print('base %-8s orig %.6f ibp %.6f' % (nm, Bo, Bi))
xs = d0['xs']


def resp(dw, dwp, dwpp, eps, cfg):
    Bp = b3_one(x, w + eps * dw, wp + eps * dwp, wpp + eps * dwpp, cl, cfg, both=True)
    Bm = b3_one(x, w - eps * dw, wp - eps * dwp, wpp - eps * dwpp, cl, cfg, both=True)
    return (Bp[0] - Bm[0]) / (2 * eps), (Bp[1] - Bm[1]) / (2 * eps)


def bump(u0, s):
    t = (u - u0) / s
    ph = np.exp(-t ** 2 / 2)
    phu = -t / s * ph
    phuu = (t ** 2 - 1) / s ** 2 * ph
    return A * x * ph, A * (ph + phu), A * (phu + phuu) / x


rows = []
for s in (0.1, 0.05):
    for u0 in np.linspace(np.log(0.8), np.log(xs) - 3 * s, 30):
        cf = W1 if np.exp(u0 - 4 * s) > 0.36 * xs else W2
        if np.exp(u0 - 4 * s) < 0.065 * xs:
            continue
        dw, dwp, dwpp = bump(u0, s)
        r1 = resp(dw, dwp, dwpp, 1e-4, cf)
        r2 = resp(dw, dwp, dwpp, 5e-5, cf)
        r3 = resp(dw, dwp, dwpp, 1e-4, dict(cf, mode='spline', xe=0.85))
        rows.append([s, np.exp(u0), r1[0], r1[1], r2[0], r3[0], r3[1], np.trapz(dw * x ** 0, x), cf is W1])
rows = np.array(rows)
print('bumps: s, x0, dB orig, dB ibp, dB orig (eps/2), dB orig/ibp (spline end, xe .85), int dw, window W1?')
for r in rows:
    print('  %.2f %8.4f  %+.4e %+.4e  %+.4e  %+.4e %+.4e  %.3e %d' % tuple(r))

lam = []
for mu in (2.0, 2.5, 2.93077, 3.5, 4.0):
    a0, a1 = 0.45 * xs, 0.7 * xs
    q = np.clip((xs - x) / xs, 0, None)
    tt = np.clip((x - a0) / (a1 - a0), 0, 1)
    ins = (x > a0) & (x < a1)
    chi = np.where(x <= a0, 0.0, np.where(x >= a1, 1.0, tt ** 3 * (10 - 15 * tt + 6 * tt ** 2)))
    dchi = np.where(ins, 30 * tt ** 2 * (1 - tt) ** 2 / (a1 - a0), 0.0)
    ddchi = np.where(ins, 60 * tt * (1 - tt) * (1 - 2 * tt) / (a1 - a0) ** 2, 0.0)
    p = mu + 1
    f, fp, fpp = q ** p, -p * q ** (p - 1) / xs, p * (p - 1) * q ** np.maximum(p - 2, 0) / xs ** 2
    dw = -A * xs * f * chi
    dwp = -A * xs * (fp * chi + f * dchi)
    dwpp = -A * xs * (fpp * chi + 2 * fp * dchi + f * ddchi)
    out = [resp(dw, dwp, dwpp, e, cf) for cf in (W1, dict(W1, mode='spline'), dict(W1, xe=0.85)) for e in (1e-4, 5e-5)]
    lam.append([mu] + list(np.array(out).ravel()))
    print('lambda-type mu = %.4f (orig, ibp) poly eps, eps/2 | spline end | xe .85:' % mu)
    print('   ' + '  '.join('%+.5e %+.5e' % o for o in out))
np.savez(sys.argv[2], rows=rows, lam=np.array(lam), xs=xs, A=A)
