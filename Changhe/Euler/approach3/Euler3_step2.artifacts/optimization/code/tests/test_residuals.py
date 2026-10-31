"""Residual identities and covariances:
 1. curl R_u0 = R_Omega (4th-order finite differences of the point evaluator) and div W = 3 c_l.
 2. Exact spiral tail U_0 = r^-alpha F(theta, chi), chi = phi + (omega/c_l) log r (seed family), built in sympy,
    annihilates the linear operator (1-c_l)U + ((c_l I - omega J) y . grad) U + omega J U: tests all rotation signs.
    Also checks that flipping the sign of either rotation term breaks the identity.
 3. Dilation covariance: U_L(y) = L U(y/L) via coefficient rescaling (a -> L^(1-l) a, b -> L^(2-l) b, R0 -> L R0),
    R_u0[U_L](y) = L R_u0[U](y/L).
 4. Rotation covariance about the z axis and two-fold equivariance for even m."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch, sympy as sp
from src.equations.fields import Model
from src.equations import residuals as res
torch.set_default_dtype(torch.float64)

def fields_at(model, z, pts):
    F = model.fields_points(z, pts)
    return F

def test_curl_identity():
    torch.manual_seed(1)
    model = Model(L=4, Nk=6, m_parity="even", R0=1.1, Nr=10, c_l=0.44, omega=1.3)
    z = torch.randn(model.n_z) * 0.3
    pts = torch.tensor([[0.4, -0.3, 0.6], [1.5, 0.7, -0.2], [0.0, 0.0, 0.9], [2.5, -1.0, 1.7]])
    F = fields_at(model, z, pts)
    ROm = res.vorticity_terms(F)['sum']
    h = 1e-3
    curl = torch.zeros_like(ROm)
    def Ru0(p):
        return res.momentum_terms(fields_at(model, z, p))['sum']
    for m in range(3):
        e = torch.zeros(3); e[m] = h
        d = (8 * (Ru0(pts + e) - Ru0(pts - e)) - (Ru0(pts + 2 * e) - Ru0(pts - 2 * e))) / (12 * h)   # d_m R_i
        # (curl R)_i = eps_ijk d_j R_k
        for i in range(3):
            for k in range(3):
                e_ijk = res.torch.tensor(0.0)
                from src.equations.fields import EPS
                if EPS[i, m, k] != 0:
                    curl[i] += EPS[i, m, k] * d[k]
    err = ((curl - ROm).abs() / (1 + ROm.abs())).max().item()
    dw = (res.div_W(F) - 3 * 0.44).abs().max().item()
    print(f"curl R_u0 vs R_Omega (FD h={h}): rel err {err:.2e}; div W - 3 c_l: {dw:.2e}")
    assert err < 1e-7 and dw < 1e-11

def test_spiral_tail():
    x, y, z = sp.symbols('x y z', real=True)
    c_l, om, eps_ = sp.Rational(45, 100), sp.Rational(7, 10), sp.Rational(3, 10)
    alpha = (1 - c_l) / c_l
    r = sp.sqrt(x**2 + y**2 + z**2); th = sp.acos(z / r); ph = sp.atan2(y, x)
    chi = ph + (om / c_l) * sp.log(r)
    # seed family: F_r = 0, F_theta = 2 eps sin th sin 2chi, F_phi = sin th + 2 eps sin th cos th cos 2chi
    Fth = 2 * eps_ * sp.sin(th) * sp.sin(2 * chi)
    Fph = sp.sin(th) + 2 * eps_ * sp.sin(th) * sp.cos(th) * sp.cos(2 * chi)
    eth = sp.Matrix([sp.cos(th) * sp.cos(ph), sp.cos(th) * sp.sin(ph), -sp.sin(th)])
    eph = sp.Matrix([-sp.sin(ph), sp.cos(ph), 0])
    U = r ** (-alpha) * (Fth * eth + Fph * eph)
    GU = sp.Matrix(3, 3, lambda m, i: sp.diff(U[i], [x, y, z][m]))
    f = sp.lambdify((x, y, z), [U, GU], "mpmath")
    import mpmath; mpmath.mp.dps = 30
    pts = np.array([[0.8, -0.5, 1.2], [3.0, 2.0, -0.7], [1e-2, 5.0, 0.3]])
    worst = 0.0; worst_flip = 1e9
    for p in pts:
        Um, GUm = f(*[mpmath.mpf(float(v)) for v in p])
        Ut = torch.tensor(np.array(Um.tolist(), dtype=float).reshape(3))
        GUt = torch.tensor(np.array(GUm.tolist(), dtype=float))
        yv = torch.tensor(p)
        for sJU, sJy in [(1, 1), (-1, 1), (1, -1)]:
            cl, omg = 0.45, 0.7
            W = cl * yv - sJy * omg * res.Jvec(yv)
            R = (1 - cl) * Ut + torch.einsum('m,mi->i', W, GUt) + sJU * omg * res.Jvec(Ut)
            val = R.abs().max().item() / Ut.abs().max().item()
            if (sJU, sJy) == (1, 1):
                worst = max(worst, val)
            else:
                worst_flip = min(worst_flip, val)
        divU = (GUt[0, 0] + GUt[1, 1] + GUt[2, 2]).item()
        assert abs(divU) < 1e-12 * GUt.abs().max().item()
    print(f"exact spiral tail: linear residual rel {worst:.2e} (correct signs); with a flipped rotation sign {worst_flip:.2e}")
    assert worst < 1e-12 and worst_flip > 1e-2

def test_dilation_covariance():
    torch.manual_seed(2)
    L_ = 1.7
    m1 = Model(L=3, Nk=5, m_parity="even", R0=0.9, Nr=8, c_l=0.47, omega=-0.8)
    m2 = Model(L=3, Nk=5, m_parity="even", R0=0.9 * L_, Nr=8, c_l=0.47, omega=-0.8)
    z1 = torch.randn(m1.n_z) * 0.4
    aT, aS, _, _ = m1.unpack(z1)
    lq = m1.l_arr
    z2 = m2.pack(aT * L_ ** (1 - lq)[None, :], aS * L_ ** (2 - lq)[None, :])
    pts = torch.tensor([[0.4, -0.3, 0.6], [1.5, 0.7, -0.2], [0.0, 0.0, 0.9]])
    F1 = m1.fields_points(z1, pts); F2 = m2.fields_points(z2, pts * L_)
    eU = (F2['U'] - L_ * F1['U']).abs().max().item()
    eOm = (F2['Om'] - F1['Om']).abs().max().item()       # curl U_L (y) = Omega(y/L)
    R1 = res.momentum_terms(F1)['sum']; R2 = res.momentum_terms(F2)['sum']
    eR = (R2 - L_ * R1).abs().max().item() / R1.abs().max().item()
    V1 = res.vorticity_terms(F1)['sum']; V2 = res.vorticity_terms(F2)['sum']
    eV = (V2 - V1).abs().max().item() / V1.abs().max().item()
    print(f"dilation covariance: U {eU:.2e}, Omega {eOm:.2e}, R_u0 {eR:.2e}, R_Omega (dilation invariant) {eV:.2e}")
    assert max(eU, eOm, eR, eV) < 1e-12

def test_rotation_and_twofold():
    torch.manual_seed(3)
    model = Model(L=4, Nk=4, m_parity="even", R0=1.0, Nr=8, c_l=0.43, omega=2.0)
    z = torch.randn(model.n_z) * 0.4
    pts = torch.tensor([[0.4, -0.3, 0.6], [1.5, 0.7, -0.2], [-0.3, 1.1, 0.9]])
    gam = 0.6
    Q = torch.tensor([[math.cos(gam), -math.sin(gam), 0], [math.sin(gam), math.cos(gam), 0], [0, 0, 1.0]])
    # rotated coefficients: Y_m^c, Y_m^s pair rotates by m*gam (field U'(y) = Q U(Q^T y))
    aT, aS, _, _ = model.unpack(z)
    aT2, aS2 = aT.clone(), aS.clone()
    for q, (l, m, t) in enumerate(model.modes):
        if m > 0 and t == 0:
            c, s_ = math.cos(m * gam), math.sin(m * gam)
            # (f(phi - gam)): cos(m(phi-gam)) = cos m phi cos m gam + sin m phi sin m gam
            aT2[:, q] = c * aT[:, q] - s_ * aT[:, q + 1]; aT2[:, q + 1] = s_ * aT[:, q] + c * aT[:, q + 1]
            aS2[:, q] = c * aS[:, q] - s_ * aS[:, q + 1]; aS2[:, q + 1] = s_ * aS[:, q] + c * aS[:, q + 1]
    z2 = model.pack(aT2, aS2)
    F1 = model.fields_points(z, (Q.T @ pts.T).T); F2 = model.fields_points(z2, pts)
    eU = (F2['U'] - Q @ F1['U']).abs().max().item()
    R1 = res.momentum_terms(F1)['sum']; R2 = res.momentum_terms(F2)['sum']
    eR = (R2 - Q @ R1).abs().max().item() / R1.abs().max().item()
    # two-fold: U(exp(pi J) y) = exp(pi J) U(y)
    Qpi = torch.diag(torch.tensor([-1.0, -1.0, 1.0]))
    Fa = model.fields_points(z, pts); Fb = model.fields_points(z, (Qpi @ pts.T).T)
    e2 = (Fb['U'] - Qpi @ Fa['U']).abs().max().item()
    rc = res.rotation_content(Fa).abs().max().item()
    print(f"rotation covariance: U {eU:.2e}, R_u0 {eR:.2e}; two-fold equivariance {e2:.2e}; |JU - (Jy.grad)U| max {rc:.2e} (nonzero expected)")
    assert eU < 1e-12 and eR < 1e-12 and e2 < 1e-13 and rc > 1e-3

if __name__ == "__main__":
    test_curl_identity(); test_spiral_tail(); test_dilation_covariance(); test_rotation_and_twofold()
    print("ALL RESIDUAL TESTS PASSED")
