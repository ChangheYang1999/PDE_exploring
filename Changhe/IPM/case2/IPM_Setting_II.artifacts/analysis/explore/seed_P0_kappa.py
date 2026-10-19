# Lead exploratory: c and kappa = Q/(pi c^2) for the large-l fan seed on the dynres log-polar grid (rescaled variables).
# f_p = FE tanh(s^2/FE) (1+r^2)^{p/2}, s = x/(1 + alpha sp(y) + beta sp(-y)).  Targets: c = 1 - p/2, kappa = 2(1-p)/(2-p).
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D, qdiag as QD
p0 = float(sys.argv[1]); Nt = int(sys.argv[2]) if len(sys.argv) > 2 else 551; Nth = int(sys.argv[3]) if len(sys.argv) > 3 else 256
G = D.Grid(-10, 12, Nt, Nth, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
def sp(y, eps=0.3):
    return 0.5*(y + np.sqrt(y*y + eps*eps) - eps)
def ev(FE, alpha, beta):
    s = X/(1 + alpha*sp(Y) + beta*sp(-Y))
    rho = FE*np.tanh(s*s/FE)*(1 + r**2)**(p0/2)
    Q, c, cm = QD.Qfun(G, rho/G.w, p0)
    return c, cm, Q/np.pi/c**2
tc, tk = 1 - p0/2, 2*(1 - p0)/(2 - p0)
print('p0 = %.4f targets c = %.5f kappa = %.5f' % (p0, tc, tk), flush=True)
for FE, alpha, beta in [(2.0, 0.2, 2.6264), (2.0, 0.2, 1.502827), (4.0, 0.0, 1.196507), (1.0, 0.0, 4.0), (1.0, 0.5, 6.0), (8.0, 0.2, 1.0), (2.0, 1.0, 4.0)]:
    c, cm, k = ev(FE, alpha, beta)
    print('FE %.2f alpha %.2f beta %.4f : c = %.5f (moment %.5f) kappa = %.5f' % (FE, alpha, beta, c, cm, k), flush=True)
