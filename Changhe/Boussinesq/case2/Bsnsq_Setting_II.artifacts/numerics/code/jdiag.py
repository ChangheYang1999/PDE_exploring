"""Lead 16:56Z item 3 (beta = 2): outgoing amplitude J(X) = Omega(X) + lambda(X) int_0^inf e^{-3s} W2(Phi_s X) ds,
lambda = Theta_x/W2 (or -Theta_y/W1 where |W2| is small), on circles r = 5, 20 (8 angles); invariance check
J(Phi_t X) e^t vs J(X) for t = 1, 2; and J_1(y) = lim_{x->0} J/x vs K(y) + (2E/v) int_0^inf e^{-3s} v(y(s)) ds on the
y-axis (K = Omega_x(0,y) = y G(0,y), E = Theta_xx(0,y)/2 = y a(0,y), v = W2(0,y), y(s) the axis trajectory)."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW

def flow_forward(B, X0, Y0, smax=16.0, dt=0.005):
    """RK4 forward trajectories of dX/ds = W, returning arrays of (s, x, y) (vectorized over points)."""
    x, y = X0.copy(), Y0.copy(); s = 0.0; traj = [(s, x.copy(), y.copy())]
    def rhs(x, y):
        o = evalW(B, x, y); return o['W1'], o['W2']
    while s < smax:
        k1x, k1y = rhs(x, y); k2x, k2y = rhs(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
        k3x, k3y = rhs(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y); k4x, k4y = rhs(x + dt * k3x, y + dt * k3y)
        x = x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6; y = y + dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6; s += dt
        traj.append((s, x.copy(), y.copy()))
    return traj

def J_at(B, X0, Y0, smax=16.0, dt=0.005):
    o = evalW(B, X0, Y0, need_fields=True)
    beta = B['beta']
    # lambda = Theta_x / W2 (use -Theta_y/W1 where |W2| < 0.1 |W1|)
    Ty = Y0 * 0  # Theta_y not provided by evalW; compute by finite difference of Theta
    h = 1e-5 * np.maximum(1.0, np.hypot(X0, Y0))
    Ty = (evalW(B, X0, Y0 + h, need_fields=True)['Theta'] - evalW(B, X0, Y0 - h, need_fields=True)['Theta']) / (2 * h)
    lam = np.where(np.abs(o['W2']) >= 0.1 * np.abs(o['W1']), o['Theta_x'] / o['W2'], -Ty / o['W1'])
    traj = flow_forward(B, X0, Y0, smax, dt)
    I = np.zeros_like(X0)
    for (s0, x0, y0), (s1, x1, y1) in zip(traj[:-1], traj[1:]):
        w0 = evalW(B, x0, y0)['W2']; w1 = evalW(B, x1, y1)['W2']
        I += 0.5 * (s1 - s0) * (np.exp(-(beta + 1) * s0) * w0 + np.exp(-(beta + 1) * s1) * w1)
    return o['Omega'] + lam * I, o['Omega'], lam, I, traj

for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-4, rmax=1e8, nr=6000); beta = B['beta']
    print(f"=== {path}: beta={beta}  (exponent beta+1 = {beta+1} in e^{{-(beta+1)s}}; analysis's formula uses 3 for beta = 2)")
    th = np.linspace(0.1, np.pi / 2 - 0.1, 8)
    for r0 in [5.0, 20.0]:
        X0 = r0 * np.cos(th); Y0 = r0 * np.sin(th)
        J, Om, lam, I, traj = J_at(B, X0, Y0)
        print(f"  r = {r0}: J = " + " ".join(f"{v:+.4e}" for v in J))
        print(f"          Omega = " + " ".join(f"{v:+.4e}" for v in Om) + "   lambda = " + " ".join(f"{v:+.3e}" for v in lam))
        # invariance: J(Phi_t X) e^t for t = 1, 2
        for t in [1.0, 2.0]:
            k = int(round(t / 0.005)); s, xt, yt = traj[k]
            Jt, _, _, _, _ = J_at(B, xt, yt, smax=14.0)
            print(f"          t = {t}: |Phi_t X| = " + " ".join(f"{v:.1f}" for v in np.hypot(xt, yt)) + " ;  J(Phi_t X) e^t / J(X) - 1 = " + " ".join(f"{v:+.3e}" for v in (Jt * np.exp(t) / J - 1)))
    # J_1(y) near the y-axis vs formula
    print("  J_1(y) = lim J/x (x = 0.02 y) vs K(y) + (2E/v) int_0^inf e^{-(beta+1)s} v(y(s)) ds:")
    for y0 in [2.0, 5.0, 10.0, 20.0]:
        x0 = np.array([0.02 * y0]); Y = np.array([y0])
        J, Om, lam, I, traj = J_at(B, x0, Y)
        o = evalW(B, np.array([1e-10]), Y, need_fields=True)
        K = y0 * o['G'][0]; E = y0 * o['a'][0]; v = o['W2'][0]
        # axis trajectory integral
        yy = np.array([y0]); s = 0.0; Iax = 0.0; dt = 0.005
        while s < 16.0:
            w = evalW(B, np.array([1e-10]), yy)['W2'][0]; yy = yy + dt * w  # Euler is enough for a 1D monotone flow? use RK2
            w2 = evalW(B, np.array([1e-10]), yy)['W2'][0]; Iax += 0.5 * dt * (np.exp(-(beta + 1) * s) * w + np.exp(-(beta + 1) * (s + dt)) * w2); s += dt
        print(f"    y = {y0:5.1f}: J/x = {J[0]/x0[0]:+.5e}   formula K + (2E/v) I = {K + (2 * E / v) * Iax:+.5e}   (K = {K:+.4e}, 2E/v = {2*E/v:+.4e}, I = {Iax:+.4e})")
