"""Indicial problem of the coupled linearization at the source (y-leading branch).
delta rho = r^d sum_{k odd} a_k sin(k th).  L_d = (A x d_x + y d_y - 1) + a0 * U_2[.]  on homogeneous functions
(U_2 = d_x psi, -Lap psi = d_x rho, homogeneous particular solution; d non-integer so no resonance with harmonics).
Returns the (truncated) matrix in the basis sin(k th), k = 1,3,...,2K-1."""
import numpy as np
def Lmat(d, A, a0, K):
    ks = 2*np.arange(K) + 1
    idx = {k: i for i, k in enumerate(ks)}
    M = np.zeros((K, K))
    def add(row_k, col_i, val):
        if row_k in idx: M[idx[row_k], col_i] += val
    for i, k in enumerate(ks):
        # transport
        add(k, i, d*(A+1)/2 - 1)
        add(k+2, i, (A-1)/4*(d - k))
        if k - 2 >= 1: add(k-2, i, (A-1)/4*(d + k))
        elif k - 2 == -1:  # sin(-th) = -sin(th)
            add(1, i, -(A-1)/4*(d + k))
        # coupling: d_x(r^d sin k th) = r^{d-1}[ (d-k)/2 sin(k+1)th + (d+k)/2 sin(k-1)th ]
        for m, cm in ((k+1, (d - k)/2), (k-1, (d + k)/2)):
            if m == 0: continue
            # psi = r^{d+1} Psi, Psi = -cm sin(m th)/((d+1)^2 - m^2)   [Lap psi = -d_x rho]
            Pm = -cm/((d+1)**2 - m**2)
            # d_x(r^{d+1} sin m th) = r^d[ (d+1-m)/2 sin(m+1)th + (d+1+m)/2 sin(m-1)th ]
            add(m+1, i, a0*Pm*(d+1-m)/2)
            if m - 1 >= 1: add(m-1, i, a0*Pm*(d+1+m)/2)
    return M
if __name__ == '__main__':
    import sys
    A = float(sys.argv[1]); a0 = float(sys.argv[2])
    ds = np.linspace(1.001, 9.0, 4000)
    for K in (40, 80, 160):
        sm = np.array([np.linalg.svd(Lmat(d, A, a0, K), compute_uv=False)[-1] for d in ds])
        # local minima
        mins = [i for i in range(1, len(ds)-1) if sm[i] < sm[i-1] and sm[i] < sm[i+1] and sm[i] < 1e-2]
        print(f"K={K}: local minima of smin(L_d) below 1e-2 at d =", [f"{ds[i]:.4f}({sm[i]:.1e})" for i in mins])
