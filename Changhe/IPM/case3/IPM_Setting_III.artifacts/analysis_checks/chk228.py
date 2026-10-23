# Lead check of the verifier's real-integral proof: odd Laplace solution O, A_O, relation (14), E' < 0, ODE residuals.
# Derivatives in q from the Gauss derivative formula, then the chain rule in z (no numerical differentiation).
from mpmath import mp, mpf, gamma, hyp2f1, quad, exp, sqrt, pi, inf, rf
mp.dps = 20


def Fder(eps, p, lam, q, kmax=3):
    d = 1/(p+1); r = p-2*d; a = (eps-p)/2; g = (eps-r)/2; c = eps+mpf(1)/2
    out = []
    for k in range(kmax+1):
        co = (-1)**k*rf(a, k)*rf(a-1, k)/rf(c, k)
        f = lambda t: exp(-t)*t**(g-1+k)*hyp2f1(a+k, a-1+k, c+k, -t*q)
        # t = u^(1/g) on [0, 1] removes the endpoint singularity t^(g-1): dt = (1/g) u^(1/g - 1) du
        f0 = lambda u: exp(-u**(1/g))*u**(k/g)*hyp2f1(a+k, a-1+k, c+k, -u**(1/g)*q)/g
        out.append(co*(quad(f0, [0, mpf(1)/4, 1]) + quad(f, [1, 10, 40, inf]))/gamma(g))
    return out


def hder(eps, p, lam, z, kmax=3):
    q = z**2/lam; F = Fder(eps, p, lam, q, kmax); q1 = 2*z/lam; q2 = 2/lam
    F = F + [0]*(4-len(F))
    G = [F[0], F[1]*q1, F[2]*q1**2+F[1]*q2, F[3]*q1**3+3*F[2]*q1*q2]
    if eps == 0:
        return G
    return [z*G[0], G[0]+z*G[1], 2*G[1]+z*G[2], 3*G[2]+z*G[3]]


for p in [mpf('0.25'), mpf('0.5'), mpf('0.75')]:
    K = 1; lam = 4*p**2*K/((p+1)**2*(1-p)); d = 1/(p+1); r = p-2*d
    AE = sqrt(pi)*gamma(1+d)*lam**(-(p+2)/2)/(gamma(-p/2)*gamma(d-p/2)*gamma((p+3)/2))
    AO = (sqrt(pi)/2)*gamma(1+d)*lam**(-(p+1)/2)/(gamma((1-p)/2)*gamma(d+(1-p)/2)*gamma((p+4)/2))
    CE = gamma(-p/2)*gamma(d-p/2)*gamma(mpf(1)/2)/gamma(2+p/2)
    CO = gamma((1-p)/2)*gamma(d+(1-p)/2)*gamma(-mpf(1)/2)/gamma(2-(1-p)/2)
    z = mpf(10)**4
    rO = hder(1, p, lam, z, 0)[0]/(AO*z**(p+2)); rE = hder(0, p, lam, z, 0)[0]/(AE*z**(p+2))
    s1 = 2*p+r+2; s2 = p*(p+2)+2*r*(p+1); s3 = p*r*(p+2)
    res = []
    for eps in (0, 1):
        for z0 in [mpf('0.3'), mpf('0.7'), mpf(3)]:
            h = hder(eps, p, lam, z0)
            th1 = z0*h[1]; th2 = z0**2*h[2]+z0*h[1]; th3 = z0**3*h[3]+3*z0**2*h[2]+z0*h[1]
            R = th3-s1*th2+s2*th1-s3*h[0]+2*lam*h[2]
            res.append(abs(R)/max(abs(th3), abs(2*lam*h[2]), abs(s3*h[0])))
    Ep = [hder(0, p, lam, mpf(x), 1)[1] for x in ['0.1', '0.5', '2', '10']]
    Oz = [hder(1, p, lam, mpf(x), 0)[0]/mpf(x) for x in ['0.1', '0.5', '2', '10']]
    print(float(p), 'AE', mp.nstr(AE, 12), 'AO', mp.nstr(AO, 12), 'O ratio', mp.nstr(rO, 8), 'E ratio', mp.nstr(rE, 8),
          '(14) diff', mp.nstr(-AE/AO-(CO/CE)/sqrt(lam), 3), 'CE<0', CE < 0, 'CO<0', CO < 0,
          'max rel ODE res', mp.nstr(max(res), 3), "E'<0", all(e < 0 for e in Ep),
          'O/z increasing', all(Oz[i] < Oz[i+1] for i in range(3)), flush=True)
