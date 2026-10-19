# V221: checks for item 49 (Proposition 2.5(d), (e); Section 9.22, Step 7). Own code, no lead code used.
import numpy as np
from scipy.integrate import quad, solve_ivp
rng = np.random.default_rng(221)
ok = []
# (1) |k - d| <= (2d/3) z^2 with k = d sin z cos z / z
z = np.linspace(-np.pi/3, np.pi/3, 200001); z = z[z != 0]
ok.append(('k-d bound', bool(np.all(np.abs(np.sin(2*z)/(2*z) - 1) <= (2/3)*z**2 + 1e-15))))
# (2) I(s) = int_{s2}^s e^{-d(s-t)} e^{-bd t} dt bounds
good = True
for _ in range(400):
    d = rng.uniform(0.01, 3); bd = rng.uniform(0.01, 3); s2 = rng.uniform(1, 5); s = s2 + rng.uniform(0, 30)
    I = quad(lambda t: np.exp(-d*(s-t) - bd*t), s2, s, limit=200)[0]
    nu = min(d, bd)
    B = (s - s2)*np.exp(-nu*s) if d >= bd else (s - s2)*np.exp(-d*s)*np.exp((d - bd)*s2)
    good &= I <= B*(1 + 1e-9) + 1e-300
    good &= B <= (1 + s)*np.exp(-nu*s)*np.exp(abs(d - bd)*0) * max(1, np.exp((d - bd)*s2 + (bd - d)*0)) + 1e-300
ok.append(('I(s) bounds', bool(good)))
# (3) exponent: for beta > 0, 1/beta > gamma - m nu/beta  <=>  beta gamma < 1 + m nu
good = True
for _ in range(20000):
    beta = rng.uniform(0.5, 6); gam = rng.uniform(1, 2); dl = rng.uniform(0.01, 2); m = rng.integers(1, 3)
    nu = min(beta - 0.5, beta*dl)
    good &= ((1/beta > gam - m*nu/beta) == (beta*gam < 1 + m*nu))
ok.append(('exponent equivalence', bool(good)))
# (4) ranges (iv): (d) <=> (gam-1) beta < 1/2 and (gam - dl) beta < 1 ; (e) <=> (gam - 2 dl) beta < 1 (gam < 2)
good = True; good_int = True
for _ in range(4000):
    gam = rng.uniform(1, 1.999); dl = rng.uniform(0.01, 2)
    betas = np.linspace(1/gam, 40, 4000)
    nu = np.minimum(betas - 0.5, betas*dl)
    dset = betas*gam < 1 + nu; eset = betas*gam < 1 + 2*nu
    good &= np.all(dset == (((gam - 1)*betas < 0.5) & ((gam - dl)*betas < 1)))
    good &= np.all(eset == ((gam - 2*dl)*betas < 1))
    for S in (dset, eset):   # interval [1/gamma, b) containing 1/gamma
        good_int &= bool(S[0]) and not np.any(np.diff(S.astype(int)) > 0)
    if dl >= gam/2: good &= bool(np.all(eset))
    if dl >= gam and gam == 1: good &= bool(np.all(dset))
gam = 1.0; dl = 1.0; betas = np.linspace(1, 1000, 100000); nu = np.minimum(betas - 0.5, betas*dl)
good &= bool(np.all(betas*gam < 1 + nu))
ok.append(('ranges (iv)', bool(good))); ok.append(('intervals [1/gamma, b)', bool(good_int)))
# (5) manufactured flow: V = AX + W2 with bounded W2 (delta = 1), A = diag(1/2, beta); along an e_2 orbit
#     |z| r^(nu/beta) / (1 + log r) stays bounded, nu = min(beta - 1/2, beta) = beta - 1/2.
for beta in (0.8, 1.0, 1.5, 2.5):
    W2 = lambda x, y: np.array([0.7*np.tanh(0.1*y) + 0.2*np.cos(np.log(1 + x*x + y*y)), 0.5/(1 + 0.01*x*x) - 0.3*np.sin(np.log(1 + x*x + y*y))])
    def rhs(s, X):
        return np.array([0.5*X[0], beta*X[1]]) + W2(X[0], X[1])
    sol = solve_ivp(rhs, (0, 22/beta), [3.0, 5.0], rtol=1e-11, atol=1e-12, dense_output=True)
    ss = np.linspace(4/beta, 22/beta, 400); X = sol.sol(ss); r = np.hypot(X[0], X[1])
    zz = np.arctan2(X[1], X[0]) - np.pi/2
    nu = min(beta - 0.5, beta)
    q = np.abs(zz)*r**(nu/beta)/(1 + np.log(r))
    ok.append((f'flow beta={beta}: max |z| r^(nu/b)/(1+log r) = {q.max():.3g}, last = {q[-1]:.3g}, r_end = {r[-1]:.3g}', bool(q[-1] <= 2*q.max())))
for name, v in ok: print(('OK  ' if v else 'FAIL'), name)
print('ALL OK' if all(v for _, v in ok) else 'SOME FAIL')
