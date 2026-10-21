"""Response of B_3 (natural units, original and ibp forms of R10, one configuration) to localized perturbations of the
axis velocity w on X3 (run-1 verifier traces). Perturbations: delta w = eps * A * x * phi(u), u = log x,
phi = exp(-(u - u0)^2 / (2 s^2)); central differences at eps and eps/2 (linearity check). Also one-sided
lambda-type perturbations delta w = -eps * A * x* * ((x* - x)/x*)_+^(mu + 1) * chi(x) with chi a smooth cutoff.
Usage: python3 infl.py traces.npz out.npz"""
import sys, json
import numpy as np
from b3core import b3_one, load, CFG

x, w, wp, wpp, cl = load(sys.argv[1])
A = 2 * cl - 1
u = np.log(x)
B0o, B0i, d0 = b3_one(x, w, wp, wpp, cl, both=True)
xs = d0['xs']


def resp(dw, dwp, dwpp, eps, cfg=CFG):
    Bp = b3_one(x, w + eps * dw, wp + eps * dwp, wpp + eps * dwpp, cl, cfg, both=True)
    Bm = b3_one(x, w - eps * dw, wp - eps * dwp, wpp - eps * dwpp, cl, cfg, both=True)
    return (Bp[0] - Bm[0]) / (2 * eps), (Bp[1] - Bm[1]) / (2 * eps)


def bump(u0, s):
    t = (u - u0) / s
    ph = np.exp(-t ** 2 / 2)
    phu = -t / s * ph
    phuu = (t ** 2 - 1) / s ** 2 * ph
    dw = A * x * ph
    dwp = A * (ph + phu)
    dwpp = A * (phu + phuu) / x
    return dw, dwp, dwpp


rows = []
for s in (0.1, 0.05):
    for u0 in np.linspace(np.log(0.05), np.log(xs) - 3 * s, 40):
        dw, dwp, dwpp = bump(u0, s)
        r1 = resp(dw, dwp, dwpp, 1e-4)
        r2 = resp(dw, dwp, dwpp, 5e-5)
        rows.append([s, np.exp(u0), r1[0], r1[1], r2[0], r2[1], np.trapz(dw, x)])
rows = np.array(rows)
print('bumps: s, x0, dB_orig, dB_ibp (eps 1e-4), dB_orig, dB_ibp (eps 5e-5), int dw dx')
for r in rows[::3]:
    print('  %.2f %8.4f  %+.4e %+.4e  %+.4e %+.4e  %.3e' % tuple(r))

# one-sided lambda-type perturbations at x*, several exponents
lam = []
xl = 0.5 * xs
for mu in (2.0, 2.5, 2.93077, 3.5, 4.0):
    q = np.clip((xs - x) / xs, 0, None)
    tt = np.clip((x - 0.25 * xs) / (xl - 0.25 * xs), 0, 1)
    chi = np.where(x < 0.25 * xs, 0.0, np.where(x > xl, 1.0, tt ** 3 * (10 - 15 * tt + 6 * tt ** 2)))
    dchi = np.where((x > 0.25 * xs) & (x < xl), 30 * tt ** 2 * (1 - tt) ** 2 / (xl - 0.25 * xs), 0.0)
    ddchi = np.where((x > 0.25 * xs) & (x < xl), 60 * tt * (1 - tt) * (1 - 2 * tt) / (xl - 0.25 * xs) ** 2, 0.0)
    p = mu + 1
    f = q ** p
    fp = -p * q ** (p - 1) / xs
    fpp = p * (p - 1) * q ** (p - 2) / xs ** 2
    dw = -A * xs * f * chi
    dwp = -A * xs * (fp * chi + f * dchi)
    dwpp = -A * xs * (fpp * chi + 2 * fp * dchi + f * ddchi)
    out = []
    for cfg in (CFG, dict(CFG, mode='spline'), dict(CFG, xe=0.85)):
        out.append(resp(dw, dwp, dwpp, 1e-4, cfg) + resp(dw, dwp, dwpp, 5e-5, cfg))
    lam.append([mu] + list(np.array(out).ravel()))
    print('lambda-type mu = %.4f: (orig, ibp, orig/2, ibp/2) for cfg poly / spline / xe .85:' % mu)
    for o in out:
        print('    %+.5e %+.5e %+.5e %+.5e' % tuple(o))
np.savez(sys.argv[2], rows=rows, lam=np.array(lam), B0=[B0o, B0i], xs=xs, A=A)
