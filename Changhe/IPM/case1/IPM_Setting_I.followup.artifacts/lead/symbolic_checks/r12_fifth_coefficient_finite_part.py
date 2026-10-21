# Lead check of a referee answer, section 6: B_5 on R12 at L^2 = S_A, 1 < A < 2, from the axis hierarchy of 6.3.1 (a)
# (same formulas as resonant_fifth_order_log_residue_A2.py), finite part at 0 by subtracting the singular Puiseux terms.
import sympy as sp, mpmath as mp
mp.mp.dps = 40
x = sp.symbols('x', positive=True)
def run(A):
    A = sp.nsimplify(A); q = 4/A; p5 = 10 + q
    S = 6*A*(4*A-3)/(8*A-1); L = sp.sqrt(S); u = x/L
    w = -A*x*(1-u**2)/(1+u**2); g = x**2/(1+u**2)
    assert sp.simplify(sp.diff(w/g, x) - A/g) == 0          # axis constraint w g' = (w' - A) g
    h = A + 1 - sp.diff(w, x)
    a2 = (sp.diff(g, x) - sp.diff(w, x, 2))/2
    b3 = -sp.diff(a2, x)/3
    F3 = -a2*sp.diff(g, x) - b3*g
    G3 = 10*A*u**2/((8*A-1)*(1+u**2)**3)                     # referee (23)
    r3 = sp.simplify(w*sp.diff(G3, x) + (3*h-1)*G3 - F3)
    W14 = (sp.diff(b3, x) + sp.diff(G3, x))/4
    W25 = -sp.diff(W14, x)/5
    F5 = -a2*sp.diff(G3, x) - 3*b3*G3 - W14*sp.diff(g, x) - W25*g
    H5 = L**p5*u**p5*(1+u**2)**(-5)*(1-u**2)**(-q)           # referee's normalized H5
    r5 = sp.simplify((w*sp.diff(H5, x) + (5*h-1)*H5)/H5)
    # integrand I = F5/(w H5) = x^(1-p5) * E(x), E analytic even near 0
    E = sp.simplify(F5/w * (1+u**2)**5 * (1-u**2)**q * x**(-1)) # I = x^(1-p5) * E, check below
    N = 36
    Es = sp.series(E, x, 0, 2*N+1).removeO()
    c = [sp.nsimplify(Es.coeff(x, 2*n)) for n in range(N+1)]
    odd = [Es.coeff(x, 2*n+1) for n in range(N)]
    Lf = mp.sqrt(mp.mpf(sp.N(S, 50))); p5f = mp.mpf(sp.N(p5, 50)); d = Lf/4
    In = sp.lambdify(x, F5/(w*H5), 'mpmath')
    # check: the series reproduces the integrand at x = d/2
    chk = In(d/2) - sum(mp.mpf(sp.N(c[n], 50))*(d/2)**(1-p5f+2*n) for n in range(N+1))
    fp0 = sum(mp.mpf(sp.N(c[n], 50))*d**(2-p5f+2*n)/(2-p5f+2*n) for n in range(N+1))
    fp = fp0 + mp.re(mp.quad(In, [d, Lf/2, Lf*0.9, Lf]))
    print('   series check at d/2 (relative):', mp.nstr(chk/In(d/2), 5), ' tail coeff', mp.nstr(mp.mpf(sp.N(c[N],30))*d**(2*N), 5))
    B5 = -fp
    PA = 1248*A**4 - 548*A**3 + 297*A**2 - 178*A + 84
    B21 = PA*sp.beta(-4-2/A, 4/A)/(15*A*(2*A-1)*(3*A-2)*(4*A-3)*(8*A-1)*L**(10+4/A))
    print('A =', A, ' T3 residual:', r3, ' T5 hom residual:', r5, ' odd coeffs zero:', all(o == 0 for o in odd))
    print('   B5 (lead, fp quad) =', mp.nstr(B5, 20), '  referee (21) =', sp.N(B21, 20))
for A in ['5/4', '3/2', '9/5']: run(A)
