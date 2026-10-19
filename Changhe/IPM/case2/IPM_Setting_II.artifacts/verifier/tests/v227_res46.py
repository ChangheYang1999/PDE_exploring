"""V227: own checks of referee result 46 (Theorem D, Propositions A-C, E).
(1) exponent algebra on random rational parameters (exact Fractions);
(2) manufactured flow V = AX + B, B = grad^perp phi, |B| ~ (1+r)^q, B(0)=DB(0)=0, no symmetry:
    Y(X) = lim e^(-beta s) y(s): bound (3.2), flow property, Step 4 bound (incl. resonance a = beta q);
(3) identity (A1) through the variational equation; matrix identity M^-T J = J M / det M."""
import numpy as np, random
from fractions import Fraction as Fr
from scipy.integrate import solve_ivp
random.seed(7); rng = np.random.default_rng(7)

# ---------- (1) exponent algebra ----------
bad = {}
def flag(k): bad[k] = bad.get(k, 0) + 1
N = 0
for _ in range(60000):
    g = Fr(1) + Fr(random.randint(0, 999), 1000)            # gamma in [1, 2)
    d = Fr(random.randint(1, 1000), 1000)                    # delta in (0, 1]
    b = 1 / g + Fr(random.randint(0, 4000), 500)             # beta >= 1/gamma
    p = 1 / b; q = 1 - d; Q = max(p / 2, q); ka = (g - 1 - d) / 2; th = (3 - g - d) / 2
    N += 1
    if not (0 < th < 1): flag('theta')
    if q - th != ka or th + g - 2 != ka: flag('kappa')         # r^q/h = h r^(g-2) = r^kappa
    nu = min(b - Fr(1, 2), b * d)
    if (p > Q + g - 1) != (b * g < 1 + nu): flag('C0<->C5')
    if (p > Q + ka) != (g < p + 1 + d and g < 2 * p - 1 + 3 * d): flag('C1<->C6')
    if (g < 2 * d + (1 - d) * p) != (q < (2 - g) / (2 - p)): flag('7.1')
    if not ((2 - g) / (2 - p) <= 1): flag('k<=1')
    D1 = g < min(2 * d + (1 - d) * p, 3 * d + 2 * p - 1)
    if D1 and not (p > Q + ka): flag('D1=>C1')
    if D1:
        kk = (q + (2 - g) / (2 - p)) / 2                      # a k in the window (7.2)
        if not (q < kk < 1 and kk * p > g - 2 + 2 * kk): flag('7.2/7.4')
    if d >= (g + 1) / 3 and not D1: flag('D2')
    if d == 1 and not D1: flag('D3')
    if not (Fr(4) / g > 4 - g): flag('4/g>4-g')
    if not (Q < 1): flag('Q<1')
    # (C8) exponent positive for every q<k<1
    kk = q + (1 - q) * Fr(random.randint(1, 999), 1000)
    if not ((2 - p) * (2 / p - kk) > 0): flag('C8exp')
    if (2 - p) * (2 / p - kk) != 4 * b - 2 - kk * (2 - p): flag('C8form')
# D4, D5, D6 on exact grids
for i in range(1, 4000):
    b = Fr(i, 500); p = 1 / b
    g, d = Fr(3, 2), Fr(1, 2)
    if b >= 1 / g and (g < min(2 * d + (1 - d) * p, 3 * d + 2 * p - 1)) != (b < 1): flag('D4')
    g, d = Fr(1), Fr(1, 2)
    if b >= 1 / g and (g < min(2 * d + (1 - d) * p, 3 * d + 2 * p - 1)) != (b < 4): flag('D5')
for _ in range(20000):
    g = Fr(1) + Fr(random.randint(0, 999), 1000); d = Fr(random.randint(1, 1000), 1000); p = g
    if not (g < min(2 * d + (1 - d) * p, 3 * d + 2 * p - 1)): flag('D6')
print('(1) exponent algebra: %d random cases, failures %s' % (N, bad if bad else 'none'))

# ---------- (3a) matrix identity ----------
J = np.array([[0., -1.], [1., 0.]]); err = 0
for _ in range(1000):
    M = rng.normal(size=(2, 2))
    err = max(err, np.abs(np.linalg.inv(M).T @ J - J @ M / np.linalg.det(M)).max() / (1 + np.abs(J @ M / np.linalg.det(M)).max()))
print('(3a) max rel |M^-T J - J M/det M| over 1000 random M: %.2e' % err)

# ---------- (2) manufactured flow ----------
def make(beta, q, eps=0.6):
    a = 0.5; m = (3 - q) / 2
    def phi_grad(x, y):
        P = x**3 * y + 0.7 * x * y**3 + 0.5 * x**2 * y**2 - 0.3 * x**4
        Px = 3 * x**2 * y + 0.7 * y**3 + x * y**2 - 1.2 * x**3
        Py = x**3 + 2.1 * x * y**2 + x**2 * y
        w = 1 + x * x + y * y
        return eps * (Px * w**-m - P * m * w**(-m - 1) * 2 * x), eps * (Py * w**-m - P * m * w**(-m - 1) * 2 * y)
    def B(x, y):
        px, py = phi_grad(x, y); return -py, px
    def V(X):
        b1, b2 = B(X[0], X[1]); return np.array([a * X[0] + b1, beta * X[1] + b2])
    def DV(X, h=1e-6):
        s = max(1.0, np.hypot(*X)) * h
        c1 = (V(X + [s, 0]) - V(X - [s, 0])) / (2 * s); c2 = (V(X + [0, s]) - V(X - [0, s])) / (2 * s)
        return np.column_stack([c1, c2])
    return a, B, V, DV

def Yof(X0, beta, B, a, S):
    # integrate w = e^{-beta s} y and u = e^{-a s} x (bounded variables)
    def f(s, z):
        x = z[0] * np.exp(a * s); y = z[1] * np.exp(beta * s); b1, b2 = B(x, y)
        return [np.exp(-a * s) * b1, np.exp(-beta * s) * b2]
    sol = solve_ivp(f, [0, S], [X0[0], X0[1]], rtol=1e-11, atol=1e-13, dense_output=True, method='DOP853')
    return sol

for beta, q, tag in [(1.5, 0.5, 'beta q = 0.75 > a'), (1.0, 0.5, 'resonance beta q = a'), (0.8, 0.25, 'beta q < a')]:
    a, B, V, DV = make(beta, q); Q = max(1 / (2 * beta), q)
    S = 60 / (beta * (1 - q))
    ratios = []; flows = []; st4 = []
    for R in [1, 3, 10, 30, 100, 300, 1000, 3000, 10000]:
        for th in np.linspace(0, 2 * np.pi, 13)[:-1] + 0.1:
            X0 = np.array([R * np.cos(th), R * np.sin(th)])
            sol = Yof(X0, beta, B, a, S); Y = sol.y[1, -1]
            ratios.append((R, abs(Y - X0[1]) / (1 + R)**q))
            # flow property: Y(Phi_t X) = e^{beta t} Y(X) for t = 2
            z2 = sol.sol(2.0); Xt = np.array([z2[0] * np.exp(2 * a), z2[1] * np.exp(2 * beta)])
            Yt = Yof(Xt, beta, B, a, S).y[1, -1]
            flows.append(abs(Yt - np.exp(2 * beta) * Y) / (abs(np.exp(2 * beta) * Y) + 1))
            if abs(Y) > 1e-3 * R:  # vertical orbit: Step 4 bound along s in [5, S/3]
                for s in np.linspace(5, S / 3, 12):
                    z = sol.sol(s); x = z[0] * np.exp(a * s); y = z[1] * np.exp(beta * s)
                    st4.append(abs(x) / ((1 + s) * abs(y)**Q) / max(1.0, R))
    rr = {}
    for R, v in ratios: rr[R] = max(rr.get(R, 0), v)
    print('(2) %s: beta %.2f q %.2f Q %.3f | sup_th |Y-y|/(1+R)^q by R: %s' % (tag, beta, q, Q,
          ' '.join('%g:%.3f' % (R, rr[R]) for R in sorted(rr))))
    print('    flow property max rel err %.2e | Step 4: max |x|/((1+s)|y|^Q) / max(1,R) = %.3f over %d samples'
          % (max(flows), max(st4), len(st4)))

# ---------- (3b) identity (A1) along a weak (e_1-type) and a general orbit ----------
a, B, V, DV = make(1.2, 0.4)
beta = 1.2
for X0 in [np.array([0.7, -0.2]), np.array([-1.1, 0.9])]:
    def f(s, z):
        X = z[:2]; M = z[2:].reshape(2, 2)
        return np.concatenate([V(X), (DV(X) @ M).ravel()])
    S = 6.0
    sol = solve_ivp(f, [0, S], np.concatenate([X0, np.eye(2).ravel()]), rtol=1e-11, atol=1e-12, method='DOP853')
    X = sol.y[:2, -1]; M = sol.y[2:, -1].reshape(2, 2)
    lhs = np.exp(a * S) * np.linalg.inv(M).T @ (J @ V(X0)); rhs = np.exp(-beta * S) * (J @ V(X))
    print('(3b) X0 %s: det M / e^{(a+beta)S} = %.10f, |lhs - rhs| / |rhs| = %.2e, |M V(X0) - V(X)|/|V(X)| = %.2e'
          % (X0, np.linalg.det(M) / np.exp((a + beta) * S), np.abs(lhs - rhs).max() / np.abs(rhs).max(),
             np.abs(M @ V(X0) - V(X)).max() / np.abs(V(X)).max()))
