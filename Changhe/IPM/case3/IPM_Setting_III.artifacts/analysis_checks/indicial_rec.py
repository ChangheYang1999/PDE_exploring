"""Indicial roots of the coupled linearization at the source, via the three-term recurrence in the odd sine basis.
delta = r^d Theta(th), Theta = sum_{k odd} c_k sin(k th).
Transport T_d = (A x d_x + y d_y - 1):
  T_d sin k = [d(A+1)/2 - 1] sin k + ((A-1)/4)[(d-k) sin(k+2) + (d+k) sin(k-2)],  sin(-th) = -sin(th).
Nonlocal a0 U_2[delta] with the LOCAL homogeneous inverse: d_x(r^d sin k) = r^{d-1}[(d-k)/2 sin(k+1) + (d+k)/2 sin(k-1)],
  psi_m = -S_m/((d+1)^2 - m^2) r^{d+1} sin m,  d_x(r^{d+1} sin m) = r^d[(d+1-m)/2 sin(m+1) + (d+1+m)/2 sin(m-1)].
Miller backward recurrence selects the minimal solution (|th|^kappa at th=0, regular at th=pi/2).
F(d) = 0 <=> indicial root.
"""
import numpy as np, sys

def coeffs(d, A, a0, n):
    k = 2*np.arange(n) + 1.0
    D = np.full(n, d*(A+1)/2 - 1.0); L = np.zeros(n); U = np.zeros(n)
    q = (A-1)/4
    U += q*(d-k)                      # sin k -> sin(k+2): column i contributes to row i+1 => entry (i+1, i)
    # we store matrix M[row, col]; transport: row k+2 gets q(d-k) c_k ; row k-2 gets q(d+k) c_k
    M_sub = q*(d-k)                   # M[i+1, i]
    M_sup = q*(d+k)                   # M[i-1, i]  (for i >= 1)
    D[0] += -q*(d+1)                  # k=1: (d+1) sin(-th) = -(d+1) sin th
    # nonlocal
    Sp = (d-k)/2                      # source mode m = k+1
    Sm = (d+k)/2                      # source mode m = k-1 (zero for k=1 since sin 0)
    mp = k+1; mm = k-1
    psip = -Sp/((d+1)**2 - mp**2)
    psim = np.where(mm > 0, -Sm/((d+1)**2 - mm**2), 0.0)
    # psi_m r^{d+1} sin m -> U2: sin(m+1) coef (d+1-m)/2, sin(m-1) coef (d+1+m)/2
    # m = k+1: -> sin(k+2) [(d-k)/2] and sin(k) [(d+2+k)/2]
    M_sub = M_sub + a0*psip*(d-k)/2
    D = D + a0*psip*(d+2+k)/2
    # m = k-1 (k>=3): -> sin(k) [(d+2-k)/2] and sin(k-2) [(d+k)/2]
    D = D + a0*psim*(d+2-k)/2
    M_sup = M_sup + a0*psim*(d+k)/2
    return D, M_sub, M_sup

def F(d, A, a0, n=20000):
    D, Ms, Mp = coeffs(d, A, a0, n)
    # row i: Ms[i-1] c_{i-1} + D[i] c_i + Mp[i+1] c_{i+1} = 0
    R = -Ms[n-2]/D[n-1]      # R_{n-1} = c_{n-1}/c_{n-2}
    for i in range(n-2, 0, -1):
        R = -Ms[i-1]/(D[i] + Mp[i+1]*R)
    return D[0] + Mp[1]*R     # row 0: D0 c0 + Mp[1] c1 = 0

def roots(A, a0, dmin=1.0005, dmax=9.0, npts=4000, n=20000):
    ds = np.linspace(dmin, dmax, npts)
    out = []
    vals = [F(d, A, a0, n) for d in ds]
    for i in range(len(ds)-1):
        f1, f2 = vals[i], vals[i+1]
        if np.sign(f1) != np.sign(f2) and np.isfinite(f1) and np.isfinite(f2):
            a, b = ds[i], ds[i+1]
            for _ in range(60):
                m = 0.5*(a+b); fm = F(m, A, a0, n)
                if np.sign(fm) == np.sign(f1): a, f1 = m, fm
                else: b = m
            # reject poles: check |F| small-ish relative to neighbours
            out.append((0.5*(a+b), abs(F(0.5*(a+b), A, a0, n))))
    return out

if __name__ == "__main__":
    for eps in [0.02, 0.05, 0.1]:
        A = 1 + 2*eps; a0 = 4*eps
        for n in [2000, 20000, 200000]:
            r = roots(A, a0, 1.0001, 1.0 + 3*eps, 300, n)
            print(f"eps={eps} n={n} roots near 1:", [(round((x-1)/eps, 5), f"{v:.1e}") for x, v in r])
        sys.stdout.flush()
