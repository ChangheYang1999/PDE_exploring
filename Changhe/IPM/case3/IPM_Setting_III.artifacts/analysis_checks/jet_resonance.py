"""Degree-(2j+1) jet solvability at the source for the y-leading branch.
Linear part of the degree-n equations (n = 2j+1) in the unknowns rho^(n) (coeffs of x^{2i} y^{n-2i}) and
psi^(n+1) (coeffs of x^{2i+1} y^{n-2i}), with the nonlocal harmonic datum H (coefficient of Im z^{n+1}) given:
   transport: (A x d_x + y d_y - 1) rho^(n) + a0 d_x psi^(n+1)        (= known lower-order terms)
   Poisson:   Lap psi^(n+1) + d_x rho^(n)                              (= 0)
We fix H by requiring psi^(n+1) to be L2(circle)-orthogonal to Im z^{n+1}, i.e. remove the harmonic direction,
and compute the determinant of the remaining square system as a function of (A, a0)."""
import sympy as sp
x, y = sp.symbols('x y', real=True); A, a0 = sp.symbols('A a0')
def system(j):
    n = 2*j + 1
    R = sp.symbols(f'r0:{j+1}'); S = sp.symbols(f's0:{j+1}')
    rho = sum(R[i]*x**(2*i)*y**(n-2*i) for i in range(j+1))
    psi = sum(S[i]*x**(2*i+1)*y**(n-2*i) for i in range(j+1))
    tr = sp.expand(A*x*sp.diff(rho, x) + y*sp.diff(rho, y) - rho + a0*sp.diff(psi, x))
    po = sp.expand(sp.diff(psi, x, 2) + sp.diff(psi, y, 2) + sp.diff(rho, x))
    eqs = []
    P = sp.Poly(tr, x, y); eqs += [P.coeff_monomial(x**(2*i)*y**(n-2*i)) for i in range(j+1)]
    if j >= 1:
        P = sp.Poly(po, x, y); eqs += [P.coeff_monomial(x**(2*i+1)*y**(n-2-2*i)) for i in range(j)]
    # harmonic direction: Im (x + i y)^(n+1), odd-odd
    h = sp.expand(sp.im(sp.expand((x + sp.I*y)**(n+1))))
    Ph = sp.Poly(h, x, y); hv = [Ph.coeff_monomial(x**(2*i+1)*y**(n-2*i)) for i in range(j+1)]
    unk = list(R) + list(S)
    M = sp.Matrix([[sp.diff(e, u) for u in unk] for e in eqs])
    return M, hv, unk
for j in range(1, 7):
    M, hv, unk = system(j)
    # parametrize psi = particular + t*h: replace one S unknown direction. Square system: add equation "H = 0"
    # implemented as: the S-vector is orthogonal (in coefficient space, weighted later) -> instead, solve with
    # psi harmonic part prescribed: add row picking the component along h using a complement basis.
    # Simplest exact route: the kernel of the full (2j+1) x (2j+2) matrix with harmonic coefficient set to zero.
    # Unknown change: S = S_perp + t*hv where S_perp spans a complement; we use t as the nonlocal datum and drop it.
    j1 = j + 1
    # choose complement: drop the S coordinate with largest |hv| coefficient index k, write S_k = t*hv_k/... simpler:
    # build basis of S-space: hv and unit vectors e_i (i != k)
    # complement of the nonlocal harmonic direction Im z^{n+1} = r^{n+1} sin((n+1)th): the polar modes
    # r^{n+1} sin(2k th) = (x^2+y^2)^{j+1-k} Im z^{2k}, k = 1..j (these coefficients are fixed locally)
    n = 2*j + 1
    cols = []
    for i in range(j1):
        v = sp.zeros(2*j1, 1); v[i] = 1; cols.append(v)
    for kk in range(1, j1):
        q = sp.expand((x**2 + y**2)**(j1 - kk) * sp.im(sp.expand((x + sp.I*y)**(2*kk))))
        Pq = sp.Poly(q, x, y)
        v = sp.zeros(2*j1, 1)
        for i in range(j1):
            v[j1 + i] = Pq.coeff_monomial(x**(2*i+1)*y**(n-2*i))
        cols.append(v)
    T = sp.Matrix.hstack(*cols)
    Msq = M * T
    d = sp.factor(Msq.det())
    print(f"j={j} (degree {2*j+1}): det = {d}", flush=True)
