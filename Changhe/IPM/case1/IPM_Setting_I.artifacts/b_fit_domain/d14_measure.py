"""D14 (SPEC v4) on an export (lead): least-squares Taylor fit at the center of H = log a and psi on r in [r_lo, r_hi]
(physical units, whole quadrant), a = 1 + delta x^2 + gamma y^2 + O(r^4), psi = c xy + alpha x y^3 + beta x^3 y + O(r^7).
Prints c (vs 3 c_l - 1), alpha + beta (vs -1/3), the D14 defects beta - 2 A delta and (4A+2) gamma - 5 alpha and their
relative sizes, for two fit windows (stability check). Usage: python d14_measure.py fields.npz [rlo,rhi ...]"""
import sys
import numpy as np
z = np.load(sys.argv[1])
cl = float(z['c_l']); A = 2 * cl - 1
r, th = z['r'], z['theta']
R, T = np.meshgrid(r, th, indexing='ij')
X, Y = R * np.cos(T), R * np.sin(T)
p3 = 6 + 2 / A
wins = [tuple(map(float, w.split(','))) for w in sys.argv[2:]] or [(0.005, 0.3), (0.01, 0.6), (0.02, 1.0)]
for (rlo, rhi) in wins:
    m = (R >= rlo) & (R <= rhi)
    x, y = X[m], Y[m]
    # H = log a: even-even monomials to degree 8, plus the singular |x|^(p3-2) y^2 term
    colsH = [x**2, y**2, x**4, x**2*y**2, y**4, x**6, x**4*y**2, x**2*y**4, y**6,
             x**8, x**6*y**2, x**4*y**4, x**2*y**6, y**8, np.abs(x)**(p3-2)*y**2]
    MH = np.stack(colsH, 1); sH = np.abs(MH).max(0)
    cH, *_ = np.linalg.lstsq(MH / sH, z['H'][m], rcond=None); cH /= sH
    fitH = np.abs(MH @ cH - z['H'][m]).max()
    delta, gamma = cH[0], cH[1]
    # psi: odd-odd monomials to degree 8, plus singular |x|^(p3+1) sgn(x) y^3-type term
    colsP = [x*y, x*y**3, x**3*y, x*y**5, x**3*y**3, x**5*y, x*y**7, x**3*y**5, x**5*y**3, x**7*y]
    MP = np.stack(colsP, 1); sP = np.abs(MP).max(0)
    cP, *_ = np.linalg.lstsq(MP / sP, z['psi'][m], rcond=None); cP /= sP
    fitP = np.abs(MP @ cP - z['psi'][m]).max() / np.abs(z['psi'][m]).max()
    c, alpha, beta = cP[0], cP[1], cP[2]
    d1 = beta - 2 * A * delta; d2 = (4 * A + 2) * gamma - 5 * alpha
    print(f'r in [{rlo}, {rhi}]: c {c:.7f} (3c_l-1 = {3*cl-1:.7f}), alpha {alpha:.6f}, beta {beta:.6f}, alpha+beta+1/3 {alpha+beta+1/3:.1e}; '
          f'delta {delta:.6f} gamma {gamma:.6f}; fit H {fitH:.1e}, psi rel {fitP:.1e}')
    print(f'   D14: beta - 2A delta = {d1:.5f} (rel {d1/(abs(beta)+2*A*abs(delta)):.2e}); '
          f'(4A+2) gamma - 5 alpha = {d2:.5f} (rel {d2/((4*A+2)*abs(gamma)+5*abs(alpha)):.2e}); '
          f'required delta {beta/(2*A):.6f}, gamma {5*alpha/(4*A+2):.6f}')
