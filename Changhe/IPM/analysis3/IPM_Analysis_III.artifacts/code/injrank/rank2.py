# NUMERICAL phase-space estimate (float64 grid data; not a bound): local rank of a finite-rank split when the
# real-energy error at frequencies >= Lambda is second order, [S2mat(B) + S2(b_eta)]/(2 Lambda^2) (V096), compared
# with the first-order rule Lambda = 4 |grad B| / m used in local_rank.py. Local proxy: S2 ~ |D^2 B|_F + |D^2 b_eta|.
# Rule: error <= m/4, i.e. Lambda^2 = 2 (|D^2 B| + |D^2 b_eta|) / m. Count N = (1/(16 pi)) int Lambda^2 dt dtheta
# (same normalization as local_rank.py, so the two numbers are directly comparable).
import numpy as np, json, sys
z = np.load(sys.argv[1]); eta = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1
t = z['t']; th = z['th']; gx = z['rho_x']; gy = z['rho_y']
c = np.cos(th)[None, :]; s = np.sin(th)[None, :]
B11 = -gy * c * c + gx * c * s; B22 = -gy * s * s - gx * c * s; B12 = gy * c * s + 0.5 * gx * (c * c - s * s)
beta = 0.5 * (np.sqrt(gx**2 + gy**2 + eta**2) - gy)
dt = t[1] - t[0]; dth = th[1] - th[0]
def hess2(f):
    ft = np.gradient(f, dt, axis=0); fh = np.gradient(f, dth, axis=1)
    ftt = np.gradient(ft, dt, axis=0); fth = np.gradient(ft, dth, axis=1); fhh = np.gradient(fh, dth, axis=1)
    return ftt**2 + 2 * fth**2 + fhh**2, ft**2 + fh**2
H2 = np.zeros_like(gx); G2 = np.zeros_like(gx)
for Bij, mult in [(B11, 1), (B22, 1), (B12, 2)]:
    h, g = hess2(Bij); H2 += mult * h; G2 += mult * g
D2B = np.sqrt(H2); D1B = np.sqrt(G2); D2b = np.sqrt(hess2(beta)[0])
I4 = lambda f: 4 * np.trapezoid(np.trapezoid(f, th, axis=1), t)
out = dict(t_range=[float(t[0]), float(t[-1])], eta=eta, sup_D1B=float(D1B.max()), sup_D2B=float(D2B.max()),
           sup_D2b=float(D2b.max()), t_at_sup_D2B=float(t[np.unravel_index(D2B.argmax(), D2B.shape)[0]]))
for m in [2.5, 2.871539, 3.0]:
    L2_first = 16 * D1B**2 / m**2
    L2_second = 2 * (D2B + D2b) / m
    out['m=%g' % m] = dict(N_first=float(I4(L2_first) / (16 * np.pi)), N_second=float(I4(L2_second) / (16 * np.pi)),
                           Lambda_first_max=float(np.sqrt(L2_first.max())), Lambda_second_max=float(np.sqrt(L2_second.max())),
                           N_second_global=float(11.5 * L2_second.max() / 8))
# radial profile of the second-order cutoff (max over theta), for placing local cutoffs
L2s = 2 * (D2B + D2b) / 2.5
prof = [(float(t[i]), float(np.sqrt(L2s[i].max()))) for i in range(0, len(t), 50)]
out['profile_t_Lambda2_m2.5'] = prof
print(json.dumps(out, indent=1))
