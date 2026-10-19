import numpy as np, sys
sys.path.insert(0, 'scripts')
from lp_core import LP

def phi_of(L, rho_fun):
    r = L.r[:, None]; th = L.th[None, :]
    return rho_fun(r * np.cos(th), r * np.sin(th)) / np.exp(L.lw)[:, None]

for (Nu, M) in ((301, 12), (601, 16), (1201, 24)):
    L = LP(u0=-8, u1=4, Nu=Nu, M=M, k0=0.6)
    phi = phi_of(L, lambda x, y: x**2 * y * np.exp(-(x**2 + y**2)))
    psit, dpsit, c, h = L.velocity(phi, k=0.6)
    s = L.r**2
    p2 = (np.exp(-s) * (s**2 + s + 1) - 1) / (8 * s)
    p4 = (np.exp(-s) * (s**3 + 3 * s**2 + 6 * s + 6) - 6) / (16 * s**2)
    # psi = p2 sin2t + p4 sin4t (verifier convention); check sign/normalization
    e2 = np.max(np.abs(psit[:, 0] * s - p2)) / np.max(np.abs(p2))
    ok = L.u > -4
    e4 = np.max(np.abs(psit[ok, 1] * s[ok] - p4[ok])) / np.max(np.abs(p4[ok]))
    print(f"gauss Nu={Nu} M={M}: c={c:.12f} (exact 0.125)  rel err psi_2 {e2:.2e}, psi_4 {e4:.2e}, max other {np.max(np.abs(psit[:,2:])):.1e}")
for (Nu, M) in ((601, 12), (1201, 16), (2401, 24)):
    k = 0.6
    L = LP(u0=-6, u1=12, Nu=Nu, M=M, k0=k)
    phi = phi_of(L, lambda x, y: x**2 * y * (1 + x**2 + y**2) ** ((k - 3) / 2))
    psit, dpsit, c, h = L.velocity(phi, k=k)
    print(f"growing Nu={Nu} M={M}: c={c:.12f} exact {1/(4*(1-k)):.12f}  err {abs(c-1/(4*(1-k))):.1e}; 2 psit_1(u0) = {2*psit[0,0]:.10f}")
