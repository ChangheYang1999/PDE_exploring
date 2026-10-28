# Independent numerical checks for the direct periodic Hilbert proof (V184).
import mpmath as mp
mp.mp.dps = 40
def F(a, y): return mp.sin(a)/(mp.cos(y)-mp.cos(a))
worst = 0
for a in [mp.mpf('0.1'), mp.mpf('0.7'), mp.pi/2]:
    b = mp.tan(a/2)
    for y in [mp.mpf('0.03'), mp.mpf('0.5'), mp.mpf('1.3'), mp.mpf('2.9')]:
        if abs(y-a) < 1e-6: continue
        lhs = (mp.cot((a-y)/2) - mp.cot((-a-y)/2))/2
        worst = max(worst, abs(lhs - F(a, y)))
    for s in [mp.mpf('0.05'), mp.mpf('0.4'), mp.mpf('0.93')]:
        u = 2*mp.atan(b*s); r = 2*mp.atan(b/s)
        rho = lambda uu: 2*mp.atan(b**2/mp.tan(uu/2))
        mass = F(a, rho(u))*mp.diff(rho, u) - F(a, u)
        Fdu = F(a, u)*mp.diff(lambda ss: 2*mp.atan(b*ss), s) - 2/(1-s**2)
        Qang = (r-u)/(2*a); Qch = mp.sin((r-u)/2)/mp.sin(a)
        Qch_f = (1+b**2)*(1-s**2)/(2*mp.sqrt((s**2+b**2)*(1+b**2*s**2)))
        bound = (1-s**2)/(2*s)
        worst = max(worst, abs(mass), abs(Fdu), abs(Qch-Qch_f))
        assert 0 < Qang <= bound and 0 < Qch <= bound, (a, s)
print('identity residual max', worst)
for al in [mp.mpf('0.01'), mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.9')]:
    I = mp.quad(lambda s: s**(-al)*(1-s**2)**(al-1), [0, 0.5, 1])
    N1 = 2**(2-al)/mp.pi*I; N2 = 2**(1-al)*mp.beta((1-al)/2, al)/mp.pi; N3 = mp.gamma(al/2)*mp.gamma((1-al)/2)/mp.pi**1.5
    print('alpha', al, N1, N2 - N1, N3 - N1, ' alpha*N*pi/2 =', al*N1*mp.pi/2)
# exact pairing integral (2) at a = pi/2 (angular) versus N
for al in [mp.mpf('0.3'), mp.mpf('0.5')]:
    for a in [mp.mpf('0.2'), mp.pi/2]:
        b = mp.tan(a/2)
        val = 2/mp.pi*mp.quad(lambda s: 2/(1-s**2)*((mp.atan(b/s)-mp.atan(b*s))/(2*mp.atan(b)))**al, [0, 0.5, 1])
        print(' pairing integral alpha=%s a=%s: %s  N=%s' % (al, mp.nstr(a, 5), mp.nstr(val, 15), mp.nstr(mp.gamma(al/2)*mp.gamma((1-al)/2)/mp.pi**1.5, 15)))
