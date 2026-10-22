"""Tests of the t-map model: (1) Green inverse vs direct scipy quadrature of the mode formula for a field
in the basis class; (2) derivatives/velocity/residual assembly vs sympy for fields in the basis class, using the
velocity from the model itself for the sympy side (Psi reconstructed from the computed modes is not elementary), so
(2) checks a, a_x, a_y, G_x, G_y and the algebraic assembly; (3) convergence of c with N."""
import sys, numpy as np, torch, sympy as sp
sys.path.insert(0, 'code')
from a2core_t import A2ModelT
from a2core import DT, cheb_T, cheb_gauss_nodes
from scipy.integrate import quad
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
beta, L = 3.0, 2.0
e_G = 2 * beta * (1 + 1 / (2 * beta)); e_a = 2 * beta * (1 + 1 / beta)
tfun = lambda r: (1 + r**2 / L**2) ** (-1 / (2 * beta))
# G = t^{e_G} (1 + 0.5 eta) + 0.7 (1-t^{2b}) t^{e_G} cos 2th,  eta = 2t-1
p0 = lambda t: 1 + 0.5 * (2 * t - 1); p1 = lambda t: 0.7 + 0 * t
gamma0 = lambda r: tfun(r) ** e_G * p0(tfun(r)); gamma1 = lambda r: (1 - tfun(r) ** (2 * beta)) * tfun(r) ** e_G * p1(tfun(r))
# Omega = (r^2/4) [gamma_0 (2 sin2th) + gamma_1 (sin4th - sin0)]  => b_2 = r^2 gamma_0 /2, b_4 = r^2 gamma_1 / 4
b2 = lambda s: s**2 * gamma0(s) / 2; b4 = lambda s: s**2 * gamma1(s) / 4
def h_ref(k, b, r_e):
    I_in = quad(lambda s: s**(k + 1) * b(s), 0, r_e, limit=400, epsabs=0, epsrel=1e-12)[0]
    I_out = quad(lambda s: s**(1 - k) * b(s), r_e, np.inf, limit=400, epsabs=0, epsrel=1e-12)[0]
    return (r_e**(-k) * I_in + r_e**k * I_out) / (2 * k)
c_ref = 0.5 * quad(lambda s: b2(s) / s, 0, np.inf, limit=400, epsrel=1e-12)[0]
r_test = np.array([0.05, 0.3, 1.0, 3.0, 10.0, 100.0, 1e4])
for N in [12, 20, 32]:
    M = 4
    m = A2ModelT(N, M, L, beta, device=dev, eta_eval=2 * tfun(r_test) - 1, th_eval=np.array([0.3, 1.0]))
    cG = torch.zeros((M, N), dtype=DT, device=dev); ca = torch.zeros((M, N), dtype=DT, device=dev)
    cG[0, 0] = 1.0; cG[0, 1] = 0.5; cG[1, 0] = 0.7
    ca[0, 0] = 1.0
    f = m.fields(ca, cG, beta)
    h2 = f['h'][0].cpu().numpy(); h4 = f['h'][1].cpu().numpy()
    h2r = np.array([h_ref(2, b2, r) for r in r_test]); h4r = np.array([h_ref(4, b4, r) for r in r_test])
    print(f"N={N}: c={float(f['c']):.12f} (ref {c_ref:.12f}); rel err h2: {np.abs(h2/h2r-1).max():.2e}; rel err h4: {np.abs(h4/h4r-1).max():.2e}; other modes max {f['h'][2:].abs().max().item():.1e}")
    # derivative check: h' by finite differences of the reference
    hd2 = f['hd'][0].cpu().numpy()
    dd = np.array([(h_ref(2, b2, r * (1 + 1e-5)) - h_ref(2, b2, r * (1 - 1e-5))) / (2e-5 * r) for r in r_test])
    print(f"      rel err h2': {np.abs(hd2/dd-1).max():.2e}")
# (2) sympy check of field derivatives and residual assembly for a, G in the class, with U taken from the model
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
t_s = (1 + r2 / L**2) ** (-sp.Rational(1, 6))     # beta = 3
eta_s = 2 * t_s - 1
rho2_s = 1 - t_s ** 6
a_s = t_s ** e_a * (1 + sp.Rational(3, 10) * eta_s) + sp.Rational(1, 5) * rho2_s * t_s ** e_a * (x**2 - y**2) / r2
G_s = t_s ** e_G * (1 + sp.Rational(1, 2) * eta_s) + sp.Rational(7, 10) * rho2_s * t_s ** e_G * (x**2 - y**2) / r2
fa = {k: sp.lambdify((x, y), v, 'numpy') for k, v in dict(a=a_s, a_x=sp.diff(a_s, x), a_y=sp.diff(a_s, y), G=G_s, G_x=sp.diff(G_s, x), G_y=sp.diff(G_s, y)).items()}
N, M = 24, 4
m = A2ModelT(N, M, L, beta, device=dev, eta_eval=np.linspace(-0.9, 0.95, 15), th_eval=np.linspace(0.1, 1.4, 6))
ca = torch.zeros((M, N), dtype=DT, device=dev); cG = torch.zeros((M, N), dtype=DT, device=dev)
ca[0, 0] = 1.0; ca[0, 1] = 0.3; ca[1, 0] = 0.2; cG[0, 0] = 1.0; cG[0, 1] = 0.5; cG[1, 0] = 0.7
f = m.fields(ca, cG, beta)
X = f['x'].cpu().numpy(); Y = f['y'].cpu().numpy()
for k, fn in fa.items():
    ex = fn(X, Y); got = f[k].cpu().numpy()
    print(f"  {k:4s} max rel err = {np.abs(got-ex).max()/np.abs(ex).max():.2e}")
# residual assembly: recompute Ra, RG in numpy from the model's own U and the sympy derivatives
U1 = f['U1'].cpu().numpy(); U2 = f['U2'].cpu().numpy()
W1 = beta * X + U1; W2 = beta * Y + U2; w1 = beta + U1 / X; w2 = beta + U2 / Y
Ra = W1 * fa['a_x'](X, Y) + W2 * fa['a_y'](X, Y) + (2 * w1 + w2 - beta + 2) * fa['a'](X, Y)
RG = W1 * fa['G_x'](X, Y) + W2 * fa['G_y'](X, Y) + (w1 + w2 + 1) * fa['G'](X, Y) - 2 * fa['a'](X, Y) - X * fa['a_x'](X, Y)
print(f"  Ra assembly rel err {np.abs(f['Ra'].cpu().numpy()-Ra).max()/np.abs(Ra).max():.2e}, RG {np.abs(f['RG'].cpu().numpy()-RG).max()/np.abs(RG).max():.2e}")
# velocity consistency: U from Psi by finite differences of the model's Psi at shifted points (central differences in r and th)
