# Lead check of the checker's exact cusp kernel: C_p of r^p sin(th) cos(2k th) by direct quadrature of the definition
# lim_S [int_0^S t f_xx(1, t) dt - Q S^p/p] (exact tail by the series (6)) against F_p * w_k; strain invariance of eta.
from mpmath import mp, mpf, quad, beta, binomial, rf, diff, sqrt, atan2, sin, cos, inf
mp.dps = 30
def hk(t, p, k):
    return t*(1+t*t)**((p-1)/2-k)*sum((-1)**j*binomial(2*k, 2*j)*t**(2*j) for j in range(k+1))
def Hk(x, p, k):
    # f(x, 1)
    return (1+x*x)**((p-1)/2-k)*sum((-1)**(k-m)*binomial(2*k, 2*m)*x**(2*m) for m in range(k+1))
def q(t, p, k):
    # f_xx(1, t) = p (p - 1) h - 2 (p - 1) t h' + t^2 h''
    h0 = hk(t, p, k); h1 = diff(lambda u: hk(u, p, k), t); h2 = diff(lambda u: hk(u, p, k), t, 2)
    return p*(p-1)*h0-2*(p-1)*t*h1+t*t*h2
def Cp_direct(p, k):
    Q = diff(lambda X: Hk(X, p, k), 0, 2)
    S = mpf(20)
    I = quad(lambda t: t*q(t, p, k), [0, 1, 5, S]) - Q*S**p/p
    # tail by homogeneity: t f_xx(1, t) - Q t^(p-1) = t^(p-1) (f_xx(1/t, 1) - Q); u = 1/t
    tail = quad(lambda u: u**(-p-1)*(diff(lambda X: Hk(X, p, k), u, 2)-Q), [0, 1/S])
    return I+tail
def Cp_kernel(p, k):
    b = (p+2)/2; a = (1-p)/2
    w = sum((-1)**j*binomial(2*k, 2*j)*rf(mpf(3)/2, j)*rf(-b, k-j) for j in range(k+1))/rf(a, k)
    return (p+1)*(p+2)/2*beta(mpf(3)/2, -b)*w
for p in [mpf('0.25'), mpf(1)/3, mpf('0.6')]:
    for k in [0, 1, 2]:
        d = Cp_direct(p, k); e = Cp_kernel(p, k)
        print(float(p), k, mp.nstr(d, 15), mp.nstr(e, 15), mp.nstr(abs(d-e)/abs(e), 3), flush=True)
    eps = 1
    F = lambda s: s*(1+s)**(p-2)
    st = quad(lambda y: 2*eps*y*diff(F, y*y), [0, 1, 10, inf])
    print('eta strain integral', mp.nstr(st, 5))
