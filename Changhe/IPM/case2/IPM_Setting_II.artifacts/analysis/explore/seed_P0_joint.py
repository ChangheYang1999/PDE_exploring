# Lead exploratory: 2D Newton in (log beta, log FE) at fixed alpha so that the fan seed meets BOTH scalar origin
# conditions of a profile at p = 1/c_l: c = 1 - p/2 (strain) and kappa = 2(1-p)/(2-p) (moment law).  Then re-evaluate
# on a finer grid.  argv: p0 alpha beta0 FE0
import numpy as np, sys
p0 = float(sys.argv[1]); alpha = float(sys.argv[2]); st = np.log([float(sys.argv[3]), float(sys.argv[4])])
sys.argv = [sys.argv[0], sys.argv[1]] + sys.argv[5:7]   # optional Nt Nth for the solve grid
sys.path.insert(0, 'explore')
import seed_P0_kappa as S
def g(st):
    c, cm, k = S.ev(np.exp(st[1]), alpha, np.exp(st[0]))
    return np.array([c - S.tc, k - S.tk])
ok = False
for it in range(20):
    gv = g(st)
    print('it %d beta %.5f FE %.5f G = %+.2e %+.2e' % (it, np.exp(st[0]), np.exp(st[1]), gv[0], gv[1]), flush=True)
    if np.abs(gv).max() < 1e-6: ok = True; break
    Jm = np.zeros((2, 2)); e = 1e-4
    for j in range(2):
        d = np.zeros(2); d[j] = e
        Jm[:, j] = (g(st + d) - gv)/e
    step = np.linalg.solve(Jm, -gv)
    if np.abs(step).max() > 0.3: step *= 0.3/np.abs(step).max()
    st = st + step
if ok:
    beta, FE = np.exp(st)
    import dynres as D, qdiag as QD
    for Nt, Nth, t1 in [(751, 384, 12.0), (551, 256, 14.0), (901, 768, 12.0)]:
        G = D.Grid(-10, t1, Nt, Nth, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
        s = X/(1 + alpha*S.sp(Y) + beta*S.sp(-Y))
        rho = FE*np.tanh(s*s/FE)*(1 + r**2)**(p0/2)
        Q, c, cm = QD.Qfun(G, rho/G.w, p0)
        print('SOLVED p0 %.4f alpha %.3f beta %.6f FE %.6f ; check grid %dx%d t1 %.0f: c = %.6f kappa = %.6f (targets %.6f %.6f)' % (p0, alpha, beta, FE, Nt, Nth, t1, c, Q/np.pi/c**2, S.tc, S.tk), flush=True)
