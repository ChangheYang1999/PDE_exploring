"""Check of analysis.md 9.3 (audit3 constructive claim) with the verifier's B_3 tool vb3.b3:
compatible axis data w = -A x (1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L; h = 2 c_l - w', a2 = (g' - w'')/2, b3 = -a2'/3,
F3 = -a2 g' - b3 g. Claim: B_3(L) = C_A L^{-4-2/A} (1 - S_A/L^2), S_A = 6A(4A-3)/(8A-1); at A = 2, (L^2 - 4)/(3 L^7)."""
import numpy as np, sympy as sp, warnings
warnings.simplefilter("ignore")
from vb3 import b3
xs_, A_, L_ = sp.symbols('x A L', positive=True)
u = xs_ / L_
w = -A_ * xs_ * (1 - u ** 2) / (1 + u ** 2)
g = xs_ ** 2 / (1 + u ** 2)
cl = (A_ + 1) / 2
h = 2 * cl - sp.diff(w, xs_)
a2 = (sp.diff(g, xs_) - sp.diff(w, xs_, 2)) / 2
b3s = -sp.diff(a2, xs_) / 3
F3 = -a2 * sp.diff(g, xs_) - b3s * g
fw, fh, fF = (sp.lambdify((xs_, A_, L_), e, 'numpy') for e in (w, h, F3))
# compatibility check: w g' = (1 - h) g
chk = sp.lambdify((xs_, A_, L_), w * sp.diff(g, xs_) - (1 - h) * g, 'numpy')
for A in (1.6, 2.0, 3.4):
    S = 6 * A * (4 * A - 3) / (8 * A - 1)
    rows = []
    for L in (1.0, 1.5, np.sqrt(S), 3.0, 5.0):
        x = np.exp(np.linspace(np.log(1e-4 * L), np.log(1.5 * L), 2400))
        ax = dict(x=x, w=fw(x, A, L), h=fh(x, A, L), F3=fF(x, A, L), G3=np.full_like(x, 1e-300))
        o = b3(ax)
        rows.append((L, o['B3'], o['B3'] * L ** (4 + 2 / A), float(np.abs(chk(x, A, L)).max())))
    print('A = %.2f  S_A = %.6f  (sqrt %.6f)' % (A, S, np.sqrt(S)))
    for L, B, Bs, c in rows:
        extra = ('  exact (L^2-4)/(3L^7) = %.10f' % ((L ** 2 - 4) / (3 * L ** 7))) if A == 2.0 else ''
        print('   L %.6f  B3 %.10e  B3 L^(4+2/A) %.8f  compat %.1e%s' % (L, B, Bs, c, extra))
    # linearity of B3 L^{4+2/A} in 1/L^2: fit on L = 1, 3, 5 and predict the root
    Ls = np.array([rows[0][0], rows[3][0], rows[4][0]]); Ys = np.array([rows[0][2], rows[3][2], rows[4][2]])
    c1, c0 = np.polyfit(1 / Ls ** 2, Ys, 1)
    print('   fit C_A = %.8f, S_A(fit) = %.8f, residual of the 3-point line fit at L=1.5: %.2e'
          % (c0, -c1 / c0, rows[1][2] - (c0 + c1 / rows[1][0] ** 2)))
