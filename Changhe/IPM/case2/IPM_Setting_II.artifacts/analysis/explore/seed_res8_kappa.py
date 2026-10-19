# kappa and c of the referee result 8 trial seed (25): f = x^2 (1+r^2/L^2)^{(p-2)/2} [(1 + a y/sqrt(L^2+r^2))^2 + eps x y/(L^2+r^2)]
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D, qdiag as QD
Nt = int(sys.argv[1]) if len(sys.argv) > 1 else 551; Nth = int(sys.argv[2]) if len(sys.argv) > 2 else 256
for cl in [3.0, 4.0, 6.0, 10.0]:
    p0 = 1/cl; L = 4*(1-p0)*(1-p0/2); a = 0.5
    G = D.Grid(-10, 12, Nt, Nth, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
    for eps in [0.0, 0.25]:
        f = X**2*(1 + r**2/L**2)**((p0-2)/2)*((1 + a*Y/np.sqrt(L**2 + r**2))**2 + eps*X*Y/(L**2 + r**2))
        Q, c, cm = QD.Qfun(G, f/G.w, p0)
        print('cl', cl, 'eps', eps, 'c', round(c, 5), 'target', round(1-p0/2, 5), 'kappa', round(Q/np.pi/c**2, 5), 'target', round(2*(1-p0)/(2-p0), 5))
