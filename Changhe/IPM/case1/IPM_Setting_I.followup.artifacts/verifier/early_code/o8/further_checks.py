# Checks of the 6.4 item "Further statements on the local exclusion of 6.3.1 (o)":
# (a) the directional lower estimate 8.3e-4 for the dual norm of DB at R12 (own sampled N_raw(phi_j) with the
#     ndist_ver.py evaluator; DB(phi_j) from D40 item 2);
# (b) the sampled origin term sup u^(-6) |v''| of the lognormal bump v = w_R12(u) exp(-(log(u/c)/s)^2), c = 1/8.6,
#     s = 0.3 and 1 (own symbolic v'' with sympy, own grid and golden-section refinement in log u);
# (c) the two-constants table of fred23 03 (lambda(d), the bound C(d) M^(1-lambda) delta^lambda, the threshold (10)),
#     and the constants of (11) and of the E_4 bound M_0.
src = open('ndist_ver.py').read().split('\npairs = ')[0]
exec(src)
import sympy as sp
mp.mp.dps = 40
# (a)
DB = {3: mp.mpf('0.82913517178296'), 5: mp.mpf('0.48431395933596'), 7: mp.mpf('0.21490833993007')}
for j in (3, 5, 7):
    c = [mp.mpf(0)]*12; c[j] = mp.mpf(1); c[9] = mp.mpf(j - 11)/2; c[11] = mp.mpf(9 - j)/2
    Nr, pr = ndist(c, 'mono'); Np, pp = ndist(c, 'phi')
    print('phi_%d: N_raw %s %s; N_phi %s; |DB|/N_raw %s, |DB|/(Bernstein bound) %s' % (j, mp.nstr(Nr, 10), pr, mp.nstr(Np, 10),
          mp.nstr(DB[j]/Nr, 6), mp.nstr(DB[j]/{3: mp.mpf('1111.75'), 5: mp.mpf('633.5'), 7: mp.mpf('259.25')}[j], 6)), flush=True)
# (b)
u = sp.Symbol('u', positive=True)
A = sp.Rational('10.150725'); cc = 1/sp.Rational('8.6')
for s in (sp.Rational(3, 10), sp.Integer(1)):
    v = -A*u*(1 - u**2)/(1 + u**2)*sp.exp(-(sp.log(u/cc)/s)**2)
    f = sp.lambdify(u, sp.diff(v, u, 2)/u**6, 'mpmath')
    g = lambda t: abs(f(mp.exp(t)))
    ts = [mp.log(mp.mpf(1)/86) + mp.mpf(i)/200 for i in range(-2400, 801)]
    vals = [g(t) for t in ts]
    i = max(range(len(ts)), key=lambda k: vals[k])
    a, b = ts[i - 1], ts[i + 1]
    for _ in range(80):
        m1, m2 = a + (b - a)*mp.mpf('0.382'), a + (b - a)*mp.mpf('0.618')
        if g(m1) > g(m2): b = m2
        else: a = m1
    print('bump width %s: sampled max %s at u = %s; refined %s at u = %s' % (s, mp.nstr(vals[i], 8), mp.nstr(mp.exp(ts[i]), 6),
          mp.nstr(g((a + b)/2), 8), mp.nstr(mp.exp((a + b)/2), 6)), flush=True)
# (c)
a_, b_ = mp.mpf('0.02'), mp.mpf('0.985'); rho = mp.mpf(4); M = mp.mpf(10); delta = mp.mpf('1e-7')
for d in ('0.05', '0.10', '0.20', '0.30', '0.40'):
    d = mp.mpf(d)
    S = max(a_ + b_, 2 - a_ - b_) + 2*d; vd = S/(b_ - a_); rd = vd + mp.sqrt(vd*vd - 1)
    lam = 1 - mp.log(rd)/mp.log(rho)
    C = d**-3 + d**-5 + d**-7 + 36*d**-9 + 2*d**-2 + 6*mp.mpf(2)**(-mp.mpf(1)/10)*d**-3
    bound = C*M**(1 - lam)*delta**lam
    thr = M*(mp.mpf('4.5e-6')/(C*M))**(1/lam)
    print('d %s: rho_d %s lambda %s bound %s threshold %s' % (mp.nstr(d, 3), mp.nstr(rd, 8), mp.nstr(lam, 8), mp.nstr(bound, 6), mp.nstr(thr, 6)))
h = (b_ - a_)/2; c0 = (a_ + b_)/2
print('E_4: semi-major %s, R_z = c + semi-major %s, semi-minor Y %s' % (h*(rho + 1/rho)/2, c0 + h*(rho + 1/rho)/2, h*(rho - 1/rho)/2))
print('disks d_b = 1/2 inside E_4: max focal sum b - a + 1 = %s < (b - a)(4 + 1/4)/2 = %s' % (b_ - a_ + 1, (b_ - a_)*(rho + 1/rho)/2))
from fractions import Fraction as Fr
print('(11) value', Fr(3, 10**7) + 10*Fr(1, 700)**2/(4*Fr(1, 4)), '= 10147/490000000 ?', Fr(3, 10**7) + 10*Fr(1, 700)**2/(4*Fr(1, 4)) == Fr(10147, 490000000))
