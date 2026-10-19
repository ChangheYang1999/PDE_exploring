"""kappa scan on S^+-compatible data (lead, 2026-10-17): rho = x^2 exp(2F) (1+r^2)^{(p0-2)/2}, F bounded random
combination of smooth degree-0 functions (so rho >= 0 with zero set exactly the y axis, growth r^p0).
Optional x-odd terms (rho not x-even; zero set still x = 0).  Reports c, kappa = Q/(pi c^2), the profile target
2(1-p0)/(2-p0), and min V_r/r for V = X/p0 + lam W, lam = (1/p0 - 1/2)/c (amplitude rescaled so that c = 1/p0 - 1/2).
Question: does kappa < target hold on such data (a density-only obstruction for S^+), or not?"""
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D, qdiag as QD
p0 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
nsamp = int(sys.argv[2]) if len(sys.argv) > 2 else 40
xodd = int(sys.argv[3]) if len(sys.argv) > 3 else 0
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
G = D.Grid(-10, 12, 551, 256, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
tgt = 2*(1-p0)/(2-p0)
rng = np.random.default_rng(seed)
def feats(L):
    R = np.sqrt(L**2 + r**2)
    f = [Y/R, (X**2 - Y**2)/R**2, X**2*Y/R**3, Y**3/R**3, np.tanh(Y/L), X**2*Y**2/R**4]
    if xodd: f += [X*Y/R**2, X/R, X**3/R**3]
    return f
print(f"p0={p0} target kappa={tgt:.4f} xodd={xodd}", flush=True)
best = -1e9
for i in range(nsamp):
    F = 0*r
    for L in [1.0, 4.0]:
        for f in feats(L*np.exp(rng.uniform(-1, 1.5))):
            F = F + rng.uniform(-1.5, 1.5)*f
    rho0 = X**2*np.exp(2*F)*(1+r**2)**((p0-2)/2)
    q = rho0/G.w
    Wr_r, Wt_r, c, bp, _, _, _ = D.velocity(G, q, p0)
    Q, c2, cm = QD.Qfun(G, q, p0)
    if c <= 0:
        print(f"{i}: c={c:.4f} <= 0", flush=True); continue
    lam = (1/p0 - 0.5)/c
    vr = (1/p0 + lam*Wr_r).min()
    k = Q/np.pi/c**2
    best = max(best, k)
    print(f"{i}: c={c:.4f} kappa={k:.4f} target={tgt:.4f} minVr/r={vr:.3f} psi_xx0={bp:.2e}", flush=True)
print("max kappa", best)
