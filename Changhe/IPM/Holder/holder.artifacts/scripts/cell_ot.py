# Formal two-scale cell problem for the second term of D_alpha (heuristic derivation, see notes/d0_cell.md).
# W(beta) = min over couplings of mu_+ (density cos 2th on cos2th>0) and mu_- (|cos 2th| on cos2th<0), both
# normalized to probability, of E c_beta(th, th'), with
#   c_beta(th, th') = min_{u>0} [ (1/2) log(1 + u^2 - 2u cos(th-th')) - beta log u ].
# Verifier's asymmetric-cusp construction corresponds to W(beta) >= H(beta) + E1 - log 2, E1 = log2/2 - 1/2.
import numpy as np, sys
from scipy.optimize import linear_sum_assignment
def cbeta(g, beta):
    A = 1 - beta; cg = np.cos(g)
    u = ((A - beta)*cg + np.sqrt((A - beta)**2*cg**2 + 4*A*beta))/(2*A)
    return 0.5*np.log(1 + u*u - 2*u*cg) - beta*np.log(u)
def sector_quantiles(n, centre):
    q = (np.arange(n) + 0.5)/n
    return centre + 0.5*np.arcsin(2*q - 1)
def W(beta, n):
    thp = np.concatenate([sector_quantiles(n, 0.0), sector_quantiles(n, np.pi)])
    thm = np.concatenate([sector_quantiles(n, np.pi/2), sector_quantiles(n, -np.pi/2)])
    C = cbeta(thp[:, None] - thm[None, :], beta)
    r, c = linear_sum_assignment(C)
    return C[r, c].mean()
if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    E1 = np.log(2)/2 - 0.5
    for beta in [0.5, 0.4, 0.3, 0.2, 0.172, 0.1]:
        w = W(beta, n)
        H = -beta*np.log(beta) - (1 - beta)*np.log(1 - beta)
        print(f"beta={beta:.3f} W={w:.5f} verifier={H + E1 - np.log(2):.5f} diff={w - (H + E1 - np.log(2)):.5f}", flush=True)
