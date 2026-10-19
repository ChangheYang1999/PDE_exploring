# Independent numerical checks of referee result 38 (Section 9.14 draft), verifier.
# N1: compact Biot-Savart of x^2 1_{|Y|<R} by direct circular-p.v. quadrature (not via the potential F_R).
# N2: the log-kernel mode identity of Step 11.
# N3: twice-subtracted W_2 of the layers f_gamma(x) (gamma = 1, 1.5) by direct 2D quadrature; Step 8 says (0, -f(x)).
# N4: Step 4 lower bound |K(X - Y) - K(-Y)| >= |X|/(2 pi s^3) for large s.
import numpy as np, sympy as sp, sys
z1, z2, X1, X2 = sp.symbols('z1 z2 X1 X2', real=True)
r2 = z1**2 + z2**2
Ks = [(-2*z1*z2)/(2*sp.pi*r2**2), (z1**2 - z2**2)/(2*sp.pi*r2**2)]
K = sp.lambdify((z1, z2), Ks, 'numpy')
# directional derivatives of order j of K at Z in direction X, divided by j!
def dirder(j):
    out = []
    for comp in Ks:
        e = comp
        for _ in range(j):
            e = X1*sp.diff(e, z1) + X2*sp.diff(e, z2)
        out.append(sp.simplify(e)/sp.factorial(j))
    return sp.lambdify((z1, z2, X1, X2), out, 'numpy')
P = {j: dirder(j) for j in (1, 2, 3, 4, 5)}
res = {}
# ---------- N1
def U_direct(x, y, R, nphi=4096):
    ph = 2*np.pi*np.arange(nphi)/nphi
    c, s_ = np.cos(ph), np.sin(ph)
    Xe = x*c + y*s_
    T = -Xe + np.sqrt(Xe**2 + R**2 - x*x - y*y)
    J = 2*x*c*T + c*c*T*T/2 + x*x*np.log(T)
    A1 = np.mean(-np.sin(2*ph)*J)  # (1/2pi) int dphi
    A2 = np.mean(np.cos(2*ph)*J)
    return np.array([A1, A2 - x*x/2])
for (x, y, R) in [(0.3, 0.2, 1.0), (0.5, -0.6, 2.0), (-1.1, 0.7, 1.5)]:
    Ud = U_direct(x, y, R)
    Uc = np.array([x*y/4, R*R/8 - (7*x*x + y*y)/8])
    res[f'N1 U_R direct vs claim at ({x},{y}), R={R}'] = (Ud, Uc, float(np.max(np.abs(Ud - Uc))))
# ---------- N2
from scipy.integrate import quad
for (r, s, th) in [(0.4, 0.9, 0.7), (1.3, 0.5, 2.1), (2.0, 2.5, -1.0)]:
    f = lambda p: np.log(np.hypot(r*np.cos(th) - s*np.cos(p), r*np.sin(th) - s*np.sin(p)))*np.cos(p)**2
    v = quad(f, 0, 2*np.pi, limit=400)[0]/(2*np.pi)
    a, b = min(r, s), max(r, s)
    res[f'N2 mode identity r={r} s={s}'] = (v, 0.5*np.log(b) - (a/b)**2*np.cos(2*th)/8,
                                           abs(v - (0.5*np.log(b) - (a/b)**2*np.cos(2*th)/8)))
# ---------- N3
def fgam(u, g):
    return u*u*(1 + u*u)**((g - 2)/2)
def step(u):  # smooth 1 -> 0 on [0.5, 1]
    u = np.clip((u - 0.5)/0.5, 0, 1)
    a = np.where(u > 0, np.exp(-1/np.maximum(u, 1e-300)), 0.0)
    b = np.where(u < 1, np.exp(-1/np.maximum(1 - u, 1e-300)), 0.0)
    return b/(a + b)
def kern2(Xv, Y1, Y2, big):
    # combined kernel K(X - Y) - K(-Y) - DK(-Y) X; Taylor form for |Y| >> |X|
    x, y = Xv
    k = [np.empty_like(Y1), np.empty_like(Y1)]
    m = ~big
    a = K(x - Y1[m], y - Y2[m]); b0 = K(-Y1[m], -Y2[m]); b1 = P[1](-Y1[m], -Y2[m], x, y)
    for i in range(2):
        k[i][m] = a[i] - b0[i] - b1[i]
    if big.any():
        tot = [0.0, 0.0]
        for j in (2, 3, 4, 5):
            pj = P[j](-Y1[big], -Y2[big], x, y)
            tot = [tot[i] + pj[i] for i in range(2)]
        for i in range(2):
            k[i][big] = tot[i]
    return k
def W2_layer(Xv, g, delta=0.3, nt=48, nph=512, ns_pan=60, ns_g=16, nph_far=16384, nv=400):
    x, y = Xv
    rX = np.hypot(x, y)
    # Part A: polar about X on B(X, delta), omega = step(t/delta)
    tg, tw = np.polynomial.legendre.leggauss(nt)
    t = delta*(tg + 1)/2; tw = tw*delta/2
    ph = 2*np.pi*np.arange(nph)/nph
    T, PH = np.meshgrid(t, ph, indexing='ij')
    Y1 = x + T*np.cos(PH); Y2 = y + T*np.sin(PH)
    om = step(T/delta)
    gval = om*fgam(Y1, g)
    ang = [-np.sin(2*PH), np.cos(2*PH)]
    fx = fgam(x, g)
    A = np.zeros(2)
    b0 = K(-Y1, -Y2); b1 = P[1](-Y1, -Y2, x, y)
    for i in range(2):
        I1 = ang[i]*(gval - fx)/(2*np.pi*T)              # K(X-Y) part, cancellation, measure dt dphi
        I2 = -(b0[i] + b1[i])*gval*T                     # subtracted kernels, measure t dt dphi
        A[i] = np.sum(tw[:, None]*(I1 + I2))*(2*np.pi/nph)
    # Part B inner: polar about 0, s in (0, s1), weight (1 - omega)
    s1 = rX + delta + 1.0
    edges = np.linspace(0, s1, ns_pan + 1)
    sg, sw = np.polynomial.legendre.leggauss(ns_g)
    sv = np.concatenate([(edges[k] + edges[k+1])/2 + (edges[k+1] - edges[k])/2*sg for k in range(ns_pan)])
    swv = np.concatenate([(edges[k+1] - edges[k])/2*sw for k in range(ns_pan)])
    phB = 2*np.pi*np.arange(2048)/2048
    S, PB = np.meshgrid(sv, phB, indexing='ij')
    Y1 = S*np.cos(PB); Y2 = S*np.sin(PB)
    w = 1 - step(np.hypot(Y1 - x, Y2 - y)/delta)
    k = kern2(Xv, Y1, Y2, np.zeros_like(Y1, dtype=bool))
    B = np.array([np.sum(swv[:, None]*k[i]*fgam(Y1, g)*w*S)*(2*np.pi/2048) for i in range(2)])
    # Part B far: s = s1 / v^2, v in (0, 1)
    vg, vw = np.polynomial.legendre.leggauss(nv)
    v = (vg + 1)/2; vw = vw/2
    phF = 2*np.pi*(np.arange(nph_far) + 0.5)/nph_far
    C = np.zeros(2)
    for i0 in range(0, nv, 20):
        vv = v[i0:i0+20]; ww = vw[i0:i0+20]
        S = (s1/vv**2)[:, None]*np.ones((1, nph_far))
        PF = np.ones((len(vv), 1))*phF[None, :]
        Y1 = S*np.cos(PF); Y2 = S*np.sin(PF)
        big = S > 1e3*rX
        k = kern2(Xv, Y1, Y2, big)
        jac = (2*s1/vv**3)[:, None]
        for i in range(2):
            C[i] += np.sum(ww[:, None]*k[i]*fgam(Y1, g)*S*jac)*(2*np.pi/nph_far)
    W = A + B + C - np.array([0.0, fx/2])
    return W, fx
for g in (1.0, 1.5):
    for Xv in [(0.7, 0.4), (-1.2, 0.9)]:
        W, fx = W2_layer(Xv, g)
        W2, _ = W2_layer(Xv, g, nt=64, nph=1024, ns_pan=90, ns_g=20, nph_far=32768, nv=600)
        res[f'N3 W_2 layer gamma={g} X={Xv}'] = (W, W2, np.array([0.0, -fx]), float(np.max(np.abs(W2 - np.array([0, -fx])))),
                                                float(np.max(np.abs(W - W2))))
# ---------- N4
rng = np.random.default_rng(0)
worst = np.inf
for _ in range(2000):
    Xv = rng.normal(size=2); rX = np.hypot(*Xv)
    s = rX*10**rng.uniform(1.3, 3); ph = rng.uniform(0, 2*np.pi)
    Y = s*np.array([np.cos(ph), np.sin(ph)])
    d = np.array(K(Xv[0] - Y[0], Xv[1] - Y[1])) - np.array(K(-Y[0], -Y[1]))
    worst = min(worst, np.hypot(*d)/(rX/(2*np.pi*s**3)))
res['N4 min ratio |K(X-Y)-K(-Y)| / (|X|/(2 pi s^3)) for s >= 20|X|'] = worst
for kk, vv in res.items():
    print(kk, ':', vv)
sys.stdout.flush()
