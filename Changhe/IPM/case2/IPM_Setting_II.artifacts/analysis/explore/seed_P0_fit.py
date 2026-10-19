# Lead exploratory: fit beta so that the large-l fan seed has the compatible strain c[f_p] = 1 - p/2.
# f_p(Z) = FE tanh(s^2/FE) (1 + |Z|^2)^{p/2}, s = x/(1 + alpha sp(y) + beta sp(-y)); original variables rho(X) = l^2 f_p(X/l).
import numpy as np, sys
sys.path.insert(0, 'explore')
from seed_P0_c import strain, make_f
def cfun(alpha, beta, FE, p):
    f0 = make_f(alpha, beta, FE)
    f = lambda x, y: f0(x, y)*(1 + x*x + y*y)**(p/2)
    return strain(f, nr=1500, nt=1024, p=p)
for p in [0.5, 0.25, 1.0/6, 0.1]:
    for FE, alpha in [(2.0, 0.2), (4.0, 0.0)]:
        target = 1 - p/2
        b0, b1 = 2.0, 4.0
        c0, c1 = cfun(alpha, b0, FE, p) - target, cfun(alpha, b1, FE, p) - target
        for it in range(8):
            b2 = b1 - c1*(b1 - b0)/(c1 - c0)
            b0, c0 = b1, c1
            b1, c1 = b2, cfun(alpha, b2, FE, p) - target
            if abs(c1) < 1e-7: break
        # check with finer quadrature
        cf = None
        f0 = make_f(alpha, b1, FE); f = lambda x, y: f0(x, y)*(1 + x*x + y*y)**(p/2)
        cf = strain(f, nr=3000, nt=2048, p=p)
        print('p = %.4f  c_l = %.3f  FE = %.1f alpha = %.2f  beta = %.6f  c = %.6f (fine %.6f, target %.6f)' % (p, 1/p, FE, alpha, b1, c1 + target, cf, target), flush=True)
