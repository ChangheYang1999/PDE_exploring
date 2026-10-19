# Pointwise comparison of the B_3 integrand q(x) = J(x) x^(p3-1): lead pipeline (b3_wonly_export on my traces) against
# my vb3w traces (closed form (1/3N)(a2/g^3)' m^beta and -F3/(wH) with my H).
import sys, io, contextlib, warnings
warnings.simplefilter("ignore")
import numpy as np
sys.path.insert(0, 'code')
L = 'b3_wonly_export.py'
field, Mmax, lf = sys.argv[1], int(sys.argv[2]), sys.argv[3]
argv0 = sys.argv
sys.argv = ['x', lf]
ns = {'__file__': L, '__name__': 'lead'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(L).read(), ns)
sys.argv = argv0
d = ns['d_w']
import vb3w
from vcand import load_modes
from vb3 import find_xstar, local_fit
from scipy.interpolate import CubicSpline
dd, g, ms, F = load_modes(field, Mmax)
c, cl, k, p, dp, ns2 = vb3w.inverse(g, F, Mmax)
A = 2 * cl - 1; p3 = 6 + 2 / A
tr = vb3w.w_traces(g, F, ms, p, dp, ns2, cl)
x, w = tr['x'], tr['w']
xs = find_xstar(x, w)
mu1 = float(local_fit(x, w, xs, 0.1 * xs).deriv()(0.0))
ax = vb3w.wonly(g, tr, cl, xs, mu1, 'wpp_fd')
be = 2 / A - 1; Nn = A ** (2 / A)
qd = ax['a2p'] / ax['G1'] ** 3 - 3 * ax['W1_2'] * ax['G1p'] / ax['G1'] ** 4
m = np.abs(w) / ax['G1']
q_cf = qd * m ** be * x ** (p3 - 1) / (3 * Nn)
print('lead xs %.10f p3 %.9f beta %.6f | mine xs %.10f p3 %.9f' % (d.xs, d.p3, d.beta, xs, p3))
print('   x       Phi_lead(u)        q_closed(mine)     ratio      lead g/mine g-1   lead a2 - mine a2    lead F3/mine F3-1')
for t in (0.02, 0.05, 0.1, 0.15, 0.3, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 7.5, 8.2):
    j = np.argmin(abs(x - t)); xx = x[j]
    u = xx / d.xs
    Phi = (1 - u) ** (d.beta - 1) * d.phi_x(xx)
    F3l = d.F3(xx)
    print('%7.4f  %16.10e  %16.10e  %10.7f  %10.2e  %12.3e  %12.3e' % (xx, Phi, q_cf[j], Phi / q_cf[j], d.g1(xx) / ax['G1'][j] - 1,
          d.a2(xx) - ax['W1_2'][j], F3l / ax['F3'][j] - 1))

# cross-feed: (a) my f.p. code on the lead's Phi, (b) the lead's fp_ls on my q
from numpy.polynomial import chebyshev as C
from scipy.special import roots_jacobi
nat = xs ** (p3 - 2)
def my_fp(qfun, lo, tc, K, xe_frac=0.999):
    # f.p. int_0^{x*} x^{1-p3} q(x) dx: even LS fit on grid points in [lo x*, tc x*], then Gauss-Legendre on [tc x*, xe]
    sel = (x >= lo * xs) & (x <= tc * xs)
    tt = x[sel]; qq = qfun(tt)
    M = np.stack([(tt / xs) ** (2 * kk) for kk in range(K + 1)], 1)
    ck, *_ = np.linalg.lstsq(M, qq, rcond=None)
    fit = np.abs(M @ ck - qq).max() / np.abs(qq).max()
    fp0 = sum(ck[kk] * tc ** (2 * kk + 2 - p3) / (2 * kk + 2 - p3) for kk in range(K + 1))   # natural (u) units
    tj, wj = roots_jacobi(200, be, 0.0)   # weight (1-u)^be on [tc, 1]; q has (1-u)^be? use plain GL instead
    gx, gw = np.polynomial.legendre.leggauss(400)
    ub = xe_frac
    uu = tc + (ub - tc) * (gx + 1) / 2
    mid = np.sum(gw * uu ** (1 - p3) * qfun(xs * uu)) * (ub - tc) / 2
    return fp0 + mid, fit
q_my = CubicSpline(np.log(x), q_cf)
q_myf = lambda t: q_my(np.log(t))
q_ld = lambda t: (1 - t / d.xs) ** (d.beta - 1) * d.phi_x(t)
print('my f.p. code (to u = 0.999, no endpoint piece): my q | lead Phi')
for lo in (0.01, 0.04, 0.06):
    for tc in (0.3, 0.4):
        r1 = [my_fp(q_myf, lo, tc, K)[0] for K in (5, 6, 8)]
        r2 = [my_fp(q_ld, lo, tc, K)[0] for K in (5, 6, 8)]
        print('lo %.2f tc %.1f  mine' % (lo, tc), ' '.join('%7.3f' % v for v in r1), '| lead', ' '.join('%7.3f' % v for v in r2))

print('closed_form pieces (natural units) vs simple code pieces')
for lo, tc, K in ((0.04, 0.3, 6), (0.01, 0.3, 8)):
    cf = vb3w.closed_form(ax, cl, xs, t_lo_frac=lo, t_c_frac=tc, K=K)
    sel = (x >= lo * xs) & (x <= tc * xs)
    tt = x[sel]; qq = q_cf[sel]
    M = np.stack([(tt / xs) ** (2 * kk) for kk in range(K + 1)], 1)
    ck, *_ = np.linalg.lstsq(M, qq, rcond=None)
    fp0 = sum(ck[kk] * tc ** (2 * kk + 2 - p3) / (2 * kk + 2 - p3) for kk in range(K + 1))
    gx, gw = np.polynomial.legendre.leggauss(400)
    uu = tc + (0.96 - tc) * (gx + 1) / 2
    mid = np.sum(gw * uu ** (1 - p3) * q_myf(xs * uu)) * (0.96 - tc) / 2
    print(lo, tc, K, 'closed: fp0 %.4f mid %.4f endp %.4f B %.4f' % (cf['fp0'] * nat, cf['mid'] * nat, cf['endp'] * nat, cf['B3'] * nat),
          '| simple: fp0 %.4f mid %.4f' % (fp0, mid), 'coef', ' '.join('%.4g' % v for v in ck[:4]))
    # closed_form's own polynomial coefficients converted to u units
    qk_phys = np.linalg.lstsq(np.stack([tt ** (2 * kk) for kk in range(K + 1)], 1), (qd * m ** be)[sel] * tt ** (p3 - 1), rcond=None)[0]
    print('    closed-form qk in u units /(3N):', ' '.join('%.4g' % (qk_phys[kk] * xs ** (2 * kk) / (3 * Nn)) for kk in range(4)))

print('endpoint debug')
left = x < xs * (1 - 0.004)
selE = (x > xs * (1 - 2.5 * 0.04)) & left
Qv = qd[selE] * (m[selE] / (xs - x[selE])) ** be
print('  Qv range %.4g %.4g ; qd range %.4g %.4g ; m/(x*-x) range %.4g %.4g' % (Qv.min(), Qv.max(), qd[selE].min(), qd[selE].max(),
      (m[selE] / (xs - x[selE])).min(), (m[selE] / (xs - x[selE])).max()))
for t in (7.8, 8.2, 8.4, 8.5, 8.55, 8.58, 8.59, 8.6):
    j = np.argmin(abs(x - t)); print('   x %.4f qd %.6g m %.6g w %.6g g %.6g I %.6g' % (x[j], qd[j], m[j], w[j], ax['G1'][j], qd[j] * m[j] ** be))
gx, gw = np.polynomial.legendre.leggauss(400)
for a, b in ((0.96, 0.99), (0.99, 0.999)):
    uu = a + (b - a) * (gx + 1) / 2
    print('  int_%.3f^%.3f u^(1-p3) q du = %.5f' % (a, b, np.sum(gw * uu ** (1 - p3) * q_myf(xs * uu)) * (b - a) / 2))
