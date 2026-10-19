"""Exact finite-box form of the forced moment law, for states of code/forced_char.py and code/forced_pal.py.
On the disc r < L the computed state solves V.grad rho = rho with V = c_l X + h W + (1-h) E, div V = 2 c_l, and
phi = r^-3 sin 3th has X.grad phi = -3 phi, so div(rho phi V) = (1 - c_l) rho phi + rho (h W + (1-h) E).grad phi.
Integrating over eps < r < L (the r = eps term is O(eps)) and using int_{r<L} rho phi = pi c_in,
   (1 - c_l) pi c_in + h Q_in + (1-h) Q_E = oint_{r=L} rho phi V_r L dth
       = c_l L^-1 oint rho sin3th + h L^-2 oint rho W_r sin3th          (E_r(L) = 0 to rounding)
       = pi (c_l - 1) c_tail + h B_W,
since -2 Im rho_3(L)/L = (1-p) c_tail and c_l (1-p) = c_l - 1 when p = 1/c_l. Hence, with c = c_in + c_tail,
   (c_l - 1) pi c = h (Q_in - B_W) + (1-h) Q_E,     B_W = L^-2 oint_{r=L} rho W_r sin 3th dth.
No far-field model enters except through the computed c_tail and W (which the solver uses consistently).
Prints lhs, the old rhs (no boundary term) and the box rhs, with relative defects."""
import sys, glob, math, torch
sys.path.insert(0, 'code')
from forced_char import ForcedSolver

def check(f, S=None):
    D = torch.load(f, weights_only=False); A = D['args']
    if S is None or S.Nr != len(D['edges'])*0 + (len(D['edges']) - 1)*D['q'] or S.nt != D['nt'] or S.L != D['edges'][-1]:
        S = ForcedSolver(D['edges'], D['q'], D['nt'], D['r1'], 'cuda')
    S.set_forcing(D['h'], A['mu'], A['LE'])
    d = D['d']; p = d['p']; h = D['h']; xi = D['xi'].cuda(); rho = xi**2
    lhs, rhs_old, Q, QE = S.qlaw(xi, d)
    W1, W2 = S.velocity(rho, p)
    Wr = W1*S.cs + W2*S.sn
    e = S.ext_last
    rhoL = torch.einsum('k,kj->j', e, rho[-S.q:]); WrL = torch.einsum('k,kj->j', e, Wr[-S.q:])
    BW = float(torch.sum(rhoL*WrL*torch.sin(3*S.th))*(2*math.pi/S.nt))/S.L**2
    rhs_box = h*(Q - BW) + (1 - h)*QE
    sc = max(abs(lhs), abs(rhs_box), 1e-300)
    print('%-36s h=%.5f c=%+.5e cl=%.5f p=%.4f  lhs=%+.6e  rhs_old=%+.6e (rel %.1e)  rhs_box=%+.6e (rel %.1e)  hB_W=%+.3e' % (
        f.split('/')[-1], h, d['c'], d['cl'], p, lhs, rhs_old, abs(lhs - rhs_old)/sc, rhs_box, abs(lhs - rhs_box)/sc, h*BW))
    return S

if __name__ == '__main__':
    S = None
    for pat in sys.argv[1:]:
        for f in sorted(glob.glob(pat)):
            S = check(f, S)
