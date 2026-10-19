"""Joint density-only test (lead, 2026-10-17): on x-even S^+_even-compatible test densities
rho = x^2 exp(2F) (1+r^2)^{(p0-2)/2} (F bounded, x-even, degree-0 features; zero set exactly x = 0) compute
  kappa   = Q/(pi c^2)                       (profile value 2(1-p0)/(2-p0), moment law)
  3 kw/c  with kw = int h w' dy / int h dy  (profile value 2(1-p0)/(2-p0) as well, wall identity)
where h = rho_xx(0,y), w'(y) = d_y W_2(0,y) = d_r W_r on the axis.  Both ratios are invariant under the
jet-preserving rescaling.  Question: can both be met simultaneously (no density-only obstruction from the pair)?"""
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D, qdiag as QD
p0 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
nsamp = int(sys.argv[2]) if len(sys.argv) > 2 else 40
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
G = D.Grid(-10, 12, 551, 256, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
iu, idn = G.Nth//4, 3*G.Nth//4
tgt = 2*(1-p0)/(2-p0)
rng = np.random.default_rng(seed)
def feats(L):
    R = np.sqrt(L**2 + r**2)
    return [Y/R, (X**2 - Y**2)/R**2, X**2*Y/R**3, Y**3/R**3, np.tanh(Y/L), X**2*Y**2/R**4]
def wall(F):
    rho = X**2*np.exp(2*F)*(1+r**2)**((p0-2)/2)
    q = rho/G.w
    Wr_r, Wt_r, c, bp, _, _, _ = D.velocity(G, q, p0)
    Q, c2, cm = QD.Qfun(G, q, p0)
    rr = G.r
    out = []
    for i in (iu, idn):
        f = Wr_r[:, i]
        wp = f + np.gradient(f, G.t)          # d_r W_r = Wr/r + d_t(Wr/r)
        h = 2*np.exp(2*F[:, i])*(1+rr**2)**((p0-2)/2)
        out.append((np.trapz(h*wp*rr, G.t), np.trapz(h*rr, G.t), wp[0]))
    num = out[0][0] + out[1][0]; den = out[0][1] + out[1][1]
    return c, Q/np.pi/c**2 if c > 0 else np.nan, 3*(num/den)/c if c > 0 else np.nan, out[0][2], out[1][2]
print(f"p0={p0} target (both) = {tgt:.4f}", flush=True)
# validation: rho = x^2 (1 + a y/<r>)^2 <r>^{p0-2} as F = log(1 + a y/<r>)
for a in [0.3, 0.6, 0.9]:
    F = np.log(1 + a*Y/np.sqrt(1+r**2))
    c, k, kw3, w0u, w0d = wall(F)
    print(f"val a={a}: c={c:.5f} w'(0+)={w0u:.5f} w'(0-)={w0d:.5f} kappa={k:.4f} 3kw/c={kw3:.4f} kw/c={kw3/3:.4f}", flush=True)
for i in range(nsamp):
    F = 0*r
    for L in [1.0, 4.0]:
        for f in feats(L*np.exp(rng.uniform(-1, 1.5))):
            F = F + rng.uniform(-1.5, 1.5)*f
    c, k, kw3, _, _ = wall(F)
    if not c > 0:
        print(f"{i}: c={c:.4f} <= 0", flush=True); continue
    print(f"{i}: c={c:.4f} kappa={k:.4f} 3kw/c={kw3:.4f} (target {tgt:.4f})", flush=True)
