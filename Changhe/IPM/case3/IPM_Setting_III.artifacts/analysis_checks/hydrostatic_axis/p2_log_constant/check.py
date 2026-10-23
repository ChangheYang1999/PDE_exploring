# Independent check of the P=2 axis constant M (formula (2)) and the normalized residual constant (formula (3)).
# V is computed by direct quadrature in w of k(w) |dy/dw|, not by the series or integration by parts of the source.
from mpmath import mp, mpf, sqrt, log, quad, beta, findroot, diff
mp.dps = 40
def run(C, k, h):
    kk = lambda w: sum(c*w**(j+1) for j, c in enumerate(k))
    HH = lambda w: sum(c*w**(j+1) for j, c in enumerate(h))
    yw = lambda w: C*sqrt(1-w)/w**2
    dyw = lambda w: C*(-(1/(2*sqrt(1-w)))/w**2 - 2*sqrt(1-w)/w**3)
    def wy(y):
        u = sqrt(C/y); return findroot(lambda w: w - u*(1-w)**(mpf(1)/4), u)
    V = lambda y: quad(lambda w: kk(w)*(-dyw(w)), [wy(y), mpf(1)/100, mpf(1)/2, 1])
    kj = lambda j: k[j-1] if j <= len(k) else 0
    hj = lambda j: h[j-1] if j <= len(h) else 0
    K = hj(1)*sqrt(C); Q = kj(1)*sqrt(C)/2; c2 = C*(hj(2)-hj(1)/4); c3 = C**1.5*(hj(3)-hj(2)/2-hj(1)/32)
    B = C*(kj(2)-kj(1)/4)
    M = C*(kj(1)*(-mpf(1)/2-log(2))+kj(2)*(4*log(2)-3)+sum(j*kj(j)*beta(j-2, mpf(3)/2) for j in range(3, len(k)+1)))-B*log(C)
    out = []
    for y in [mpf(10)**6, mpf(10)**8, mpf(10)**10]:
        out.append(V(y)-4*Q*sqrt(y)-B*log(y)-M)
    # residual: G = y H(w(y)), G' by the source's formula and independently by numerical differentiation
    G = lambda y: y*HH(wy(y))
    r2 = -c2+2*K*Q
    res = []
    for y in [mpf(10)**6, mpf(10)**8, mpf(10)**10]:
        Gp = diff(G, y)
        w = wy(y); Gp2 = HH(w) - w*(1-w)*diff(HH, w)/(2-3*w/2)
        R = (2*y+V(y))*Gp-G(y); Nf = abs((2*y+V(y))*Gp)+abs(G(y))
        pred = r2/(2*K)*sqrt(y)+B/4*log(y)+M/4-c3/K-r2*(2*c2+r2)/(4*K**2)
        res.append((mp.nstr(Gp-Gp2, 3), mp.nstr(y*R/Nf-pred, 6)))
    print('C', C, 'k', k, 'h', h, 'M', mp.nstr(M, 12), 'V-asym(1e6,1e8,1e10)', [mp.nstr(x, 4) for x in out])
    print('   (G\' diff, yR/Nf - pred) at 1e6,1e8,1e10:', res)
run(mpf(2), [mpf(1), mpf('0.3'), mpf('-0.7'), mpf('0.2')], [mpf(1), mpf('0.5'), mpf('-0.3')])
run(mpf('0.7'), [mpf('-1.3'), mpf(2), mpf(0), mpf(0), mpf('1.1')], [mpf('2.5'), mpf('-1'), mpf('0.4'), mpf('0.9')])
run(mpf(5), [mpf('0.4')], [mpf(1)])
