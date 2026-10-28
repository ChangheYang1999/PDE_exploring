"""N5: check L K_bar = R_bar - X.grad R_bar at points, with K_bar = rho_bar - X.grad rho_bar, potential phi_K = 4 phi - X.grad phi,
U[K_bar] = (-d_xyy phi_K, d_xxy phi_K), c[K_bar] = d_xxyy phi_K (0) = 0.
L h = V_bar.grad h - h + (U[h] - c[h] X).grad rho_bar.
Also prints the far-field coefficient of K_bar: (1 - gamma) Theta_0 (from K_bar = rho - r rho_r on r^gamma Theta_0)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipm_arb import State
from flint import arb, ctx

def phiK_jet(J, x, y, order):
    """Jet of phi_K = 4 phi - x phi_x - y phi_y to `order` from a phi jet to order+1."""
    out = {}
    for a in range(order+1):
        for b in range(order+1-a):
            out[(a, b)] = (4-a-b)*J[(a, b)] - x*J[(a+1, b)] - y*J[(a, b+1)]
    return out

def fields_from_jet(J):
    def P(a, b): return J[(a, b)]
    return {'rho': -(P(2, 1)+P(0, 3)), 'rho_x': -(P(3, 1)+P(1, 3)), 'rho_y': -(P(2, 2)+P(0, 4)),
            'U1': -P(1, 2), 'U2': P(2, 1), 'psi_xy': P(2, 2),
            'rho_xx': -(P(4, 1)+P(2, 3)), 'rho_xy': -(P(3, 2)+P(1, 4)), 'rho_yy': -(P(2, 3)+P(0, 5)),
            'DU': [[-P(2, 2), -P(1, 3)], [P(3, 1), P(2, 2)]]}

def check(S, x, y):
    x = arb(x); y = arb(y); cl = S.cl
    J = S.phi_jet(x, y, order=6)          # phi to order 6 -> phi_K to order 5
    f = fields_from_jet(J)
    JK = phiK_jet(J, x, y, 5)
    fK = fields_from_jet(JK)
    V1 = cl*x + f['U1']; V2 = cl*y + f['U2']
    # K_bar directly: rho - x rho_x - y rho_y and its gradient
    K = f['rho'] - x*f['rho_x'] - y*f['rho_y']
    Kx = -x*f['rho_xx'] - y*f['rho_xy']; Ky = -x*f['rho_xy'] - y*f['rho_yy']
    # consistency: K from potential phi_K
    dK = fK['rho'] - K
    # L K_bar  (c[K_bar] = 0, checked at origin separately)
    LK = V1*Kx + V2*Ky - K + fK['U1']*f['rho_x'] + fK['U2']*f['rho_y']
    # R_bar and grad R_bar: F = V.grad rho - rho; grad F = DV^T grad rho + (V.grad) grad rho - grad rho, DV = cl I + DU
    F = V1*f['rho_x'] + V2*f['rho_y'] - f['rho']
    DU = f['DU']
    Fx = (cl + DU[0][0])*f['rho_x'] + DU[1][0]*f['rho_y'] + V1*f['rho_xx'] + V2*f['rho_xy'] - f['rho_x']
    Fy = DU[0][1]*f['rho_x'] + (cl + DU[1][1])*f['rho_y'] + V1*f['rho_xy'] + V2*f['rho_yy'] - f['rho_y']
    RHS = F - x*Fx - y*Fy
    return {'K': K, 'K_from_potential_minus_K': dK, 'LK': LK, 'RHS': RHS, 'LK_minus_RHS': LK - RHS, 'F': F, 'UK': (fK['U1'], fK['U2'])}

if __name__ == '__main__':
    S = State(sys.argv[1], prec=256)
    J0 = S.phi_jet(arb(0), arb(0), order=6)
    JK0 = phiK_jet(J0, arb(0), arb(0), 5)
    print('c[K_bar] = d_xxyy phi_K(0) =', JK0[(2, 2)].str(10), '; d_y K_bar(0) =', fields_from_jet(JK0)['rho_y'].str(10))
    for (x, y) in [(0.3, 0.5), (1.0, 2.0), (0.0, 5.0), (7.0, 1.0), (30.0, 40.0), (0.0, 500.0), (2000.0, 100.0)]:
        r = check(S, x, y)
        print('X=(%g,%g): K=%s  K_pot-K=%s  LK=%s  RHS=%s  LK-RHS=%s  F=%s' % (x, y, r['K'].str(8), r['K_from_potential_minus_K'].str(2), r['LK'].str(10), r['RHS'].str(10), r['LK_minus_RHS'].str(3), r['F'].str(6)))
