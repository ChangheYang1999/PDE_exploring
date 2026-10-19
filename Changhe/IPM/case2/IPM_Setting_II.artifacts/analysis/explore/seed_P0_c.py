# Lead exploratory: strain c[f] = (1/pi) int f sin(3 th) r^-3 dZ for bounded "fan" seeds of the p -> 0 limit problem.
# f(x,y) = F(x / D(y)), D(y) = 1 + alpha sp(y) + beta sp(-y), F(s) = FE tanh(s^2/FE).  Validation: rho_a benchmark.
import numpy as np, sys
def sp(y, eps=0.3):
    return 0.5*(y + np.sqrt(y*y + eps*eps) - eps)
def make_f(alpha, beta, FE):
    def f(x, y):
        s = x/(1.0 + alpha*sp(y) + beta*sp(-y))
        return FE*np.tanh(s*s/FE)
    return f
def strain(f, nr=4000, nt=2048, rmin=1e-5, rmax=1e7, p=0.0):
    # polar quadrature in log r; tail beyond rmax with r^p far field
    u = np.linspace(np.log(rmin), np.log(rmax), nr); du = u[1]-u[0]
    th = (np.arange(nt)+0.5)*2*np.pi/nt; dth = 2*np.pi/nt
    s3 = np.sin(3*th)
    tot = 0.0
    for k in range(nr):
        r = np.exp(u[k]); w = du*(0.5 if k in (0, nr-1) else 1.0)
        vals = f(r*np.cos(th), r*np.sin(th))
        tot += w * np.sum(vals*s3)*dth / r   # f sin3 r^-2 dr = f sin3 r^-1 du
    # tail: f ~ r^p A(th), A from rmax
    A = f(rmax*np.cos(th), rmax*np.sin(th))/rmax**p
    tail = np.sum(A*s3)*dth * rmax**(p-1)/(1-p)
    return (tot + tail)/np.pi
if __name__ == '__main__':
    # benchmark: rho_a = x^2 (1 + a y/<r>)^2 <r>^{-3/2}, c = a exactly
    a = 0.7
    fa = lambda x, y: x*x*(1 + a*y/np.sqrt(1+x*x+y*y))**2*(1+x*x+y*y)**(-0.75)
    print('benchmark c (exact 0.7):', strain(fa, p=0.5))
    for alpha, beta, FE in [(1,1,1),(2,0.2,1),(4,0.2,1),(4,0.1,2),(8,0.1,2),(2,0.5,1),(0.2,2,1)]:
        print(alpha, beta, FE, 'c =', round(strain(make_f(alpha, beta, FE), nr=1500, nt=1024), 5))
