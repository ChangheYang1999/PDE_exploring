import numpy as np, sys
from indicial_rec import coeffs
def G(d, A, a0, n=20000):
    """row-0 residual of the backward (minimal) solution, normalized by the l2 norm of the vector; no poles."""
    D, Ms, Mp = coeffs(d, A, a0, n)
    c = np.zeros(n); c[n-1] = 1e-300; c[n-2] = -D[n-1]*c[n-1]/Ms[n-2] if Ms[n-2] != 0 else 1.0
    # backward: row i: Ms[i-1] c_{i-1} + D[i] c_i + Mp[i+1] c_{i+1} = 0  -> c_{i-1}
    c = np.zeros(n); c[n-1] = 0.0; c[n-2] = 1.0
    for i in range(n-2, 0, -1):
        c[i-1] = -(D[i]*c[i] + (Mp[i+1]*c[i+1] if i+1 < n else 0))/Ms[i-1]
        if abs(c[i-1]) > 1e100: c /= 1e100
    nrm = np.sqrt(np.sum(c**2))
    return (D[0]*c[0] + Mp[1]*c[1])/nrm, c/nrm
if __name__ == "__main__":
    eps = float(sys.argv[1]) if len(sys.argv) > 1 else 0.05
    A = 1+2*eps; a0 = 4*eps
    for n in [2000, 20000]:
        prev = None
        for t in np.linspace(0.05, 3.0, 60):
            d = 1 + t*eps
            g, c = G(d, A, a0, n)
            print(f"n={n} t={t:.3f} G={g:+.4e} c0={c[0]:+.3e} c1={c[1]:+.3e}")
