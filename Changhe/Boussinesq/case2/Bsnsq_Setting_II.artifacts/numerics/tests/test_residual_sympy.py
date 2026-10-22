"""End-to-end check of A2Model.fields against exact sympy expressions.
Choose L=1, G = 1.5(1-xi)^4 (so Psi = xy/(1+r^2)^2 exactly), a = (1-xi)^2 (1 + 0.5 xi) + 0.3 rho^2 (1-xi)^2 cos 2th.
Compare a, a_x, a_y, G_x, G_y, U1, U2, Ra, RG, c, a0, G0 at grid points and at between-node points."""
import sys, numpy as np, torch, sympy as sp
sys.path.insert(0, 'code')
from a2core import A2Model, DT
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
beta = 0.7
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
xi = (r2 - 1) / (r2 + 1)
a_ex = (1 - xi)**2 * (1 + sp.Rational(1, 2) * xi) + sp.Rational(3, 10) * (x**2 - y**2) / (1 + r2) * (1 - xi)**2
G_ex = sp.Rational(3, 2) * (1 - xi)**4
Psi_ex = x * y / (1 + r2)**2
Om_ex = -(sp.diff(Psi_ex, x, 2) + sp.diff(Psi_ex, y, 2))
assert sp.simplify(Om_ex - x * y * G_ex) == 0
U1 = -sp.diff(Psi_ex, y); U2 = sp.diff(Psi_ex, x)
W1 = beta * x + U1; W2 = beta * y + U2
w1 = beta + U1 / x; w2 = beta + U2 / y
ax = sp.diff(a_ex, x); ay = sp.diff(a_ex, y); Gx = sp.diff(G_ex, x); Gy = sp.diff(G_ex, y)
Ra = W1 * ax + W2 * ay + (2 * w1 + w2 - beta + 2) * a_ex
RG = W1 * Gx + W2 * Gy + (w1 + w2 + 1) * G_ex - 2 * a_ex - x * ax
fns = {k: sp.lambdify((x, y), v, 'numpy') for k, v in dict(a=a_ex, a_x=ax, a_y=ay, G=G_ex, G_x=Gx, G_y=Gy, U1=U1, U2=U2, Ra=Ra, RG=RG).items()}

def check(N, M, xi_eval=None, th_eval=None, tag=''):
    m = A2Model(N, M, 1.0, 2.0, 3.0, device=dev, xi_eval=xi_eval, th_eval=th_eval)
    ca = torch.zeros((M, N), dtype=DT, device=dev); cG = torch.zeros((M, N), dtype=DT, device=dev)
    ca[0, 0] = 1.0; ca[0, 1] = 0.5; ca[1, 0] = 0.3
    cG[0, 0] = 1.5; cG[0, 1] = -1.5
    f = m.fields(ca, cG, beta)
    X = f['x'].cpu().numpy(); Y = f['y'].cpu().numpy()
    print(f"-- N={N} M={M} {tag}: c={float(f['c']):.15f} (exact 1), a0={float(f['a0']):.15f} (exact 4), G0={float(f['G0']):.15f} (exact 24)")
    for k, fn in fns.items():
        ex = fn(X, Y); got = f[k].cpu().numpy()
        print(f"   {k:4s} max|err| = {np.abs(got-ex).max():.2e}   (max|exact| = {np.abs(ex).max():.2e})")
check(24, 8)
check(40, 12, xi_eval=np.linspace(-0.95, 0.95, 21), th_eval=np.linspace(0.05, np.pi/2-0.05, 9), tag='between-node')
