# NUMERICAL phase-space estimate (float64 grid data; not a bound) of the rank of a finite-rank split with a
# local cutoff Lambda(t, theta) = 4 |grad_(t,theta) B|(t, theta) / m, from N ~ (1/(16 pi)) int Lambda^2 dt dtheta
# over the full circle (the parity reduction is included in the constant).
import numpy as np, json, sys
z = np.load(sys.argv[1] if len(sys.argv) > 1 else 'field.npz')
t = z['t']; th = z['th']; gx = z['rho_x']; gy = z['rho_y']
c = np.cos(th)[None, :]; s = np.sin(th)[None, :]
B11 = -gy * c * c + gx * c * s; B22 = -gy * s * s - gx * c * s; B12 = gy * c * s + 0.5 * gx * (c * c - s * s)
dt = t[1] - t[0]; dth = th[1] - th[0]
D2 = np.zeros_like(gx)
for Bij, mult in [(B11, 1), (B22, 1), (B12, 2)]:
    D2 += mult * (np.gradient(Bij, dt, axis=0)**2 + np.gradient(Bij, dth, axis=1)**2)
DB = np.sqrt(D2)                                  # Frobenius norm over entries and the two derivatives
out = dict(sup_DB=float(DB.max()), t_at_sup=float(t[np.unravel_index(DB.argmax(), DB.shape)[0]]))
for m in [0.966, 3.0]:
    Lam = 4 * DB / m
    # quadrant integral times 4 = full circle
    I = 4 * np.trapezoid(np.trapezoid(Lam**2, th, axis=1), t)
    out['m=%g' % m] = dict(N_local=float(I / (16 * np.pi)),
                         Lambda_global=float(Lam.max()),
                         N_global_ell11=float(11.5 * Lam.max()**2 / 8))
print(json.dumps(out, indent=1))
# the same with the local grid margin of w_a (a = 17/4, mu_a' = -2a for t < 0, -5/4 for t >= 0) in place of m
a = 4.25; cl = float(z['cl']); b0 = 1 + cl; r = np.exp(t)
bp = (np.hypot(gx, gy) - gy) / 2
q = (z['V1'] * c + z['V2'] * s) / r[:, None]; vth = (-z['V1'] * s + z['V2'] * c) / r[:, None]
J = slice(1, -1)
mup = np.where(t < 0, -2 * a, -1.25)[:, None]
mloc = b0 + 0.5 * mup * q[:, J] + a * np.tan(th[J])[None, :] * vth[:, J] - bp[:, J]
Lam = 4 * DB[:, J] / mloc
I = 4 * np.trapezoid(np.trapezoid(Lam**2, th[J], axis=1), t)
out2 = dict(min_local_margin=float(mloc.min()), N_local_margin=float(I / (16 * np.pi)), Lambda_max=float(Lam.max()))
print(json.dumps(out2, indent=1))
