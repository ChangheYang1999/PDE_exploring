"""Independent check of the modal inverse: velocity at sample points X by direct 2D quadrature of the Biot-Savart kernel
   U(X) = int K(X-Y) Omega(Y) dY,  K(Z) = -(1/2pi) Z^perp/|Z|^2,  Z^perp = (-Z2, Z1)   (SPEC sec. 3),
in polar coordinates centred at X, Y = X + s e_a, Z = X - Y = -s e_a (the kernel is then smooth: K dY = (1/2pi) (-sin a, cos a) ds da), over |Y-X| < S,
plus the exterior contribution of |Y - X| > S: the strain of the vorticity outside the origin-centred disc |Y| > S,
(-c_ext x, c_ext y) with c_ext = (1/2) int_S^inf g_1(s)/s ds, minus the first-order shell correction for the shift of the disc
centre, (g_1(S)/4)(-x, y) (derived from the boundary integral (1/2pi) oint (X.n) n^perp Omega(S n) dphi); so
U_ext = (-c' x, c' y), c' = c_ext - g_1(S)/4, with remaining error O(|X|^2 |g_1'(S)|) + O(|X|^3 S^-2-1/beta).
Omega is evaluated from the stored basis (no inverse involved). Compared with U from the modal Green formula (polarlib)."""
import sys, math, torch, numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs, radial_profiles, fields_at
device = dev()
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); beta = P.beta; cO = cO.to(device)
S = float(sys.argv[2]) if len(sys.argv) > 2 else 1e6
def omega_at(x, y):
    r = torch.sqrt(x * x + y * y).clamp(min=1e-300); ph = torch.atan2(y, x)
    out = torch.zeros_like(r)
    for n in range(1, NO + 1):
        H, _ = radial_basis(P, r.reshape(-1), 2 * n, P.gamma_O, K, deriv=False)
        out += (H @ cO[n - 1]).reshape(r.shape) * torch.sin(2 * n * ph)
    return out
def direct_U(X, Ns, Na, S):
    x0, y0 = X
    # radial panels in s: geometric from 1e-6 to S, GL 8 nodes per panel
    edges = torch.logspace(-6, math.log10(S), Ns + 1, dtype=DT, device=device); edges = torch.cat([torch.zeros(1, dtype=DT, device=device), edges])
    xg, wg = np.polynomial.legendre.leggauss(8); xg = torch.tensor(xg, dtype=DT, device=device); wg = torch.tensor(wg, dtype=DT, device=device)
    mid = 0.5 * (edges[1:] + edges[:-1]); half = 0.5 * (edges[1:] - edges[:-1])
    s = (mid[:, None] + half[:, None] * xg[None, :]).reshape(-1); ws = (half[:, None] * wg[None, :]).reshape(-1)
    a = torch.arange(Na, dtype=DT, device=device) * (2 * math.pi / Na); wa = 2 * math.pi / Na
    Sg, Ag = torch.meshgrid(s, a, indexing='ij')
    Om = omega_at(x0 + Sg * torch.cos(Ag), y0 + Sg * torch.sin(Ag))
    U1 = (1 / (2 * math.pi)) * torch.einsum('s,sa->', ws, -torch.sin(Ag) * Om) * wa
    U2 = (1 / (2 * math.pi)) * torch.einsum('s,sa->', ws, torch.cos(Ag) * Om) * wa
    # exterior strain correction
    rS = torch.tensor([S], dtype=DT, device=device)
    tail = basis_tail(P, rS[0], 2, P.gamma_O, K)        # J_out(S) = S^2 int_S^inf g_1/s ds  (for basis coefficients)
    c_ext = float(tail @ cO[0]) / (2 * S * S)
    H1, _ = radial_basis(P, rS, 2, P.gamma_O, K, deriv=False); g1S = float(H1[0] @ cO[0])
    cp = c_ext - g1S / 4
    return float(U1) - cp * x0, float(U2) + cp * y0, cp
pts = [(0.5, 0.3), (1.0, 1.0), (2.0, 0.7), (0.2, 3.0), (5.0, 5.0), (0.05, 0.02)]
rr = torch.tensor(sorted(set([math.hypot(*p) for p in pts])), dtype=DT, device=device)
prof = radial_profiles(P, cT, cO, rr, NT, NO, K)
print('point            modal U1        modal U2    |  direct U1       direct U2     | diff1      diff2     (c_ext)   [Ns,Na]')
for (x0, y0) in pts:
    r0 = math.hypot(x0, y0); th0 = math.atan2(y0, x0)
    F = fields_at(prof, rr, torch.tensor([th0], dtype=DT, device=device), beta, NT, NO)
    i = int((rr - r0).abs().argmin()); mU1 = float(F['U1'][i, 0]); mU2 = float(F['U2'][i, 0])
    for Sx in (1e4, 1e6, 1e8):
        d1, d2, ce = direct_U((x0, y0), 600, 384, Sx)
        print('(%.2f,%.2f)  %14.9f %14.9f | %14.9f %14.9f | %.2e  %.2e  (c\'=%.5f) S=%.0e' % (x0, y0, mU1, mU2, d1, d2, abs(d1 - mU1), abs(d2 - mU2), ce, Sx))
