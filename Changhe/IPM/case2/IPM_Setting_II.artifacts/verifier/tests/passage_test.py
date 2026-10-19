"""V19 check of Prop 11.2 (saddle passage exponent q_k = (k b - 1)/sigma) on nonlinear saddle fields that are NOT
linearisable by a smooth chart (resonant b = 2 sigma and Holder remainders). Transport f(Phi_T X) = e^T f(X):
f = eps^k on the section v = v0 at u = eps; record exit height tau at u = u0 and f_out = e^T eps^k; fit the
exponent of f_out against tau on eps in [1e-12, 1e-6]."""
import numpy as np
from scipy.integrate import solve_ivp

def run(b, sig, a, c, k, u0=0.1, v0=0.1):
    def rhs(t, z):
        u, v = z
        return [u*(b + a(u, v)), v*(-sig + c(u, v))]
    ev = lambda t, z: z[0] - u0
    ev.terminal = True; ev.direction = 1
    out = []
    for eps in np.geomspace(1e-12, 1e-6, 7):
        # integrate in log variables for accuracy: U = log u, Vv = log v
        def rl(t, Z):
            u, v = np.exp(Z[0]), np.exp(Z[1])
            return [b + a(u, v), -sig + c(u, v)]
        evl = lambda t, Z: Z[0] - np.log(u0)
        evl.terminal = True; evl.direction = 1
        s = solve_ivp(rl, [0, 1e4], [np.log(eps), np.log(v0)], events=evl, rtol=1e-12, atol=1e-13, max_step=0.05)
        T = s.t_events[0][0]; tau = np.exp(s.y_events[0][0][1])
        out.append((eps, tau, T, k*np.log(eps) + T))
    out = np.array(out)
    slope = np.polyfit(np.log(out[:, 1]), out[:, 3], 1)[0]
    loc = np.diff(out[:, 3])/np.diff(np.log(out[:, 1]))
    return slope, loc[-1], loc[0], (k*b - 1)/sig

cases = [
    ('linear', 2.5, 0.5, lambda u, v: 0*u, lambda u, v: 0*u),
    ('smooth nonlinear', 2.5, 0.5, lambda u, v: 0.7*v + 0.3*u, lambda u, v: -0.4*u + 0.5*v**2),
    ('resonant b = 2 sig + Holder', 3.0, 1.5, lambda u, v: 0.5*np.abs(v)**0.3 + 0.2*u, lambda u, v: np.abs(u)**0.4 - 0.3*v),
    ('IPM-like l = 1.1, sig = 0.9', 2*1.1 + 0.9, 0.9, lambda u, v: 0.4*v - 0.2*u*v, lambda u, v: 0.6*u + 0.3*v),
]
for name, b, sig, a, c in cases:
    for k in (2, 3):
        s, l1, l0, q = run(b, sig, a, c, k)
        print(f'{name:32s} b={b:.2f} sig={sig:.2f} k={k}: fitted exponent {s:.6f} (local {l0:.6f} .. {l1:.6f}), q_k = {q:.6f}')

# convergence of the local exponent for the Holder case (o(1) corrections decay like a power of eps)
import numpy as np
b, sig = 3.0, 1.5
a = lambda u, v: 0.5*np.abs(v)**0.3 + 0.2*u; c = lambda u, v: np.abs(u)**0.4 - 0.3*v
for k in (2,):
    vals = []
    for eps in np.geomspace(1e-60, 1e-4, 15):
        def rl(t, Z):
            u, v = np.exp(Z[0]), np.exp(Z[1]); return [b + a(u, v), -sig + c(u, v)]
        evl = lambda t, Z: Z[0] - np.log(0.1); evl.terminal = True; evl.direction = 1
        s = solve_ivp(rl, [0, 1e4], [np.log(eps), np.log(0.1)], events=evl, rtol=1e-12, atol=1e-13, max_step=0.05)
        vals.append((np.log(np.exp(s.y_events[0][0][1])), k*np.log(eps) + s.t_events[0][0]))
    vals = np.array(vals)
    loc = np.diff(vals[:, 1])/np.diff(vals[:, 0])
    print('Holder case k=2, local exponents from eps=1e-60 upward:', np.round(loc, 5), 'q_2 =', (2*b - 1)/sig)
