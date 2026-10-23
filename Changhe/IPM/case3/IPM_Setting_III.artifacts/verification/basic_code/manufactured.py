# Manufactured canonical pairs (rho, psi) in closed form, for testing the inverse.
# rho = sum_i P_i(d) F_i(r),  psi = - d_x sum_i P_i(d) H_i(r),  Lap H_i = F_i  (H_i radial),
# P_i odd in d_y, even in d_x. Canonical (psi_xy etc. o(r)) when growth of rho is sublinear.
import sympy as sp
import numpy as np

x, y = sp.symbols('x y', real=True)
R = sp.sqrt(x ** 2 + y ** 2)


def radial_pair(L, beta, amp):
    """F(r) = amp (1 + r^2/L^2)^beta ; H'(r) = (1/r) int_0^r s F ds (closed form)."""
    rr = sp.symbols('rr', positive=True)
    F = amp * (1 + rr ** 2 / L ** 2) ** beta
    Hp = amp * (L ** 2 / (2 * (beta + 1) * rr)) * ((1 + rr ** 2 / L ** 2) ** (beta + 1) - 1)
    return F, Hp, rr


def build(terms):
    """terms: list of (ix, iy, L, beta, amp): contributes d_x^ix d_y^iy F, F=amp(1+r^2/L^2)^beta.
    ix even, iy odd. Returns sympy rho, psi."""
    rho = 0; psi = 0
    for (ix, iy, L, beta, amp) in terms:
        F, Hp, rr = radial_pair(sp.nsimplify(L), sp.nsimplify(beta), sp.nsimplify(amp))
        Fxy = F.subs(rr, R)
        dxH = Hp.subs(rr, R) * x / R  # d_x H
        rho += sp.diff(Fxy, x, ix, y, iy) if ix > 0 else sp.diff(Fxy, y, iy)
        # psi = - d_x P(d) H = - d_x^{ix} d_y^{iy} (d_x H)
        t = dxH
        if ix > 0:
            t = sp.diff(t, x, ix)
        t = sp.diff(t, y, iy)
        psi += -t
    return rho, psi


def lambdified(terms):
    rho, psi = build(terms)
    U1 = -sp.diff(psi, y); U2 = sp.diff(psi, x)
    f = {k: sp.lambdify((x, y), v, 'numpy') for k, v in
         dict(rho=rho, psi=psi, U1=U1, U2=U2, rhox=sp.diff(rho, x), rhoy=sp.diff(rho, y)).items()}
    return f, rho, psi


# default test: gamma = 1/2 growth
GAMMA = 0.5
DEFAULT_TERMS = [
    (0, 1, 1.0, (GAMMA + 1) / 2, 1.0 / (GAMMA + 1)),      # d_y F ~ y (1+r^2)^{(g-1)/2}: a0 = 1
    (0, 3, 2.0, (GAMMA + 3) / 2, 0.3),                     # d_y^3 F : sin(3 th) content, r^g growth
    (2, 1, 1.5, (GAMMA + 3) / 2, -0.2),                    # d_x^2 d_y F
]
