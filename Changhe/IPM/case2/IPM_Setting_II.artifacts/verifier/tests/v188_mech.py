# V188 manufactured test of the mechanism of FR 4.17(f) / 9.13 Step 11 (candidate 7efa7fd9) in an explicit model:
# V_0 = (x/2, a y) (= DV_0(0) X with a = 2l - 1/2), xi = x (V_0.grad xi = xi/2), flow Phi_s(x, y) = (x e^{s/2}, y e^{a s}),
# orbit invariant z = y x^{-2a} on x > 0. phi_n = n^{-2-alpha} b sin(n z), h_n = -Lap phi_n, W[h_n] = (-phi_xy, phi_xx),
# f_n = W[h_n].grad xi = -phi_xy, B eta_n(X) = int_{-inf}^0 e^{-s/2} f_n(Phi_s X) ds. This model is not a profile;
# it tests the algebra and the powers of n in Step 11 (sup |B eta_n| ~ n^-alpha, Holder quotient bounded below,
# ||eta_n||_{C^alpha} bounded, lower bound b_* from g = -(1/2) b kappa^2 V_2 xi).
import numpy as np, sympy as sp
l = 1.5; a = 2*l - 0.5; al = 0.5
x, y, n = sp.symbols('x y n', positive=True)
x0b, y0b, rb = 1.0, 0.4, 0.25
q = ((x - x0b)**2 + (y - y0b)**2)/rb**2
bump = sp.exp(-1/(1 - q))            # used only where q < 1
z = y*x**(-2*a)
phi = n**(-2-al)*bump*sp.sin(n*z)
fx = sp.lambdify((x, y, n), -sp.diff(phi, x, y), 'numpy')
hx = sp.lambdify((x, y, n), -(sp.diff(phi, x, 2) + sp.diff(phi, y, 2)), 'numpy')
bx = sp.lambdify((x, y), bump, 'numpy')
def masked(F, X, Y, *args):
    Q = ((X - x0b)**2 + (Y - y0b)**2)/rb**2
    out = np.zeros(np.broadcast(X, Y).shape)
    m = Q < 1 - 1e-9
    Xb, Yb = np.broadcast_arrays(X, Y)
    if m.any(): out[m] = F(Xb[m], Yb[m], *args)
    return out
S = np.linspace(-6.0, 0.0, 24001); ds = S[1] - S[0]
wS = np.full(S.size, 2.0); wS[1::2] = 4.0; wS[0] = wS[-1] = 1.0; wS *= ds/3*np.exp(-S/2)
def Beta(X, Y, nn):
    Xs = X[..., None]*np.exp(S/2); Ys = Y[..., None]*np.exp(a*S)
    return (masked(fx, Xs, Ys, nn)*wS).sum(-1)
def gfun(X, Y):  # g = -(1/2) b kappa^2 V_2 xi with kappa = 2 x^{-2a-1}, V_2 = a y, xi = x
    Q = ((X - x0b)**2 + (Y - y0b)**2)/rb**2
    out = np.zeros(np.broadcast(X, Y).shape); m = Q < 1 - 1e-9
    Xb, Yb = np.broadcast_arrays(X, Y)
    out[m] = -2*a*bx(Xb[m], Yb[m])*Yb[m]*Xb[m]**(-4*a - 1)
    return out
def bstar(X, Y):
    Xs = X[..., None]*np.exp(S/2); Ys = Y[..., None]*np.exp(a*S)
    return (gfun(Xs, Ys)*wS).sum(-1)
xd = 1.5                                 # downstream line x = xd; X = (xd, z xd^{2a})
zc = y0b*x0b**(-2*a)
gx, gy = np.meshgrid(np.linspace(0.3, 2.0, 60), np.linspace(-0.5, 25.0, 120))
print('a = %.2f alpha = %.2f, downstream x = %.2f, central orbit z = %.4f' % (a, al, xd, zc))
print('   n   sup_grid|B eta_n|   n^al*sup   Holder quotient Q_n   predicted 2|b*|(xd^{2a} pi)^-al   [h_n]_alpha(line)')
for nn in [8, 16, 32, 64, 128, 256]:
    sup = np.abs(Beta(gx, gy, nn)).max()
    k = np.ceil(nn*zc/(2*np.pi) - 0.25); zz = (2*np.pi*k + np.pi/2)/nn; zp = zz + np.pi/nn
    X1 = np.array([xd]); Y1 = np.array([zz*xd**(2*a)]); Y2 = np.array([zp*xd**(2*a)])
    B1 = Beta(X1, Y1, nn)[0]; B2 = Beta(X1, Y2, nn)[0]
    dist = abs(Y2[0] - Y1[0])
    Qn = abs(B1 - B2)/dist**al
    pred = (abs(bstar(X1, Y1)[0]) + abs(bstar(X1, Y2)[0]))*nn**(-al)/dist**al
    # Holder seminorm of h_n along a transversal segment through the bump centre (pairs at several separations)
    yy = np.linspace(y0b - rb, y0b + rb, 20001); hh = masked(hx, np.full(yy.size, x0b), yy, nn)
    hs = 0.0
    for sh in [1, 3, 10, 30, 100, 300, 1000, 3000]:
        hs = max(hs, (np.abs(hh[sh:] - hh[:-sh])/((yy[1] - yy[0])*sh)**al).max())
    print('%4d   %.4e        %.4f      %.4e           %.4e                  %.4f' % (nn, sup, sup*nn**al, Qn, pred, hs))
