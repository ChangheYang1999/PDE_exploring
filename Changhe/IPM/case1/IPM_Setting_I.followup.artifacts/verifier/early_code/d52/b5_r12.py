# B_5 on the compatible data of R12 at the zero L^2 = S_A of B_3 (D52 (e)). Own code.
# R12: w = -A x (1 - x^2/L2)/(1 + x^2/L2), g = x^2/(1 + x^2/L2), x* = L.  H_j = A^q g^j m^(-q), m = -w/g, q = (j-1)/A,
# so H_j = x^q h_j(x), h_j = g^j (1 - x^2/L2)^(-q) (analytic at 0).
# G_3 = -H_3 int_x^L I_3 (l_3 = 0), I_j = F_j/(w H_j); a_2 = (g' - w'')/2, a_4 = (G_3' - a_2''/3)/4,
# F_3 = -a_2 g' + g a_2'/3, F_5 = a_2' G_3 - a_2 G_3' + g a_4'/5 - a_4 g'.  B_j = -f.p. int_0^L I_j.
# [delta, L]: mpmath tanh-sinh (nested for G_3); [0, delta]: Laurent series of x^q I_j (the fractional power x^(-q)
# factored out), integrated termwise in the finite-part sense. Test: A = 2, L = 2 gives B_5 = 11/1474560 (D38).
import sys, time
T0 = time.time()
import sympy as sp, mpmath as mp
mp.mp.dps = 30
x = sp.Symbol('x', positive=True)

def run(A, L2, N=20, dfrac=sp.Rational(1, 3)):
    q3, q5 = 2/A, 4/A
    w = -A*x*(1 - x**2/L2)/(1 + x**2/L2); g = x**2/(1 + x**2/L2)
    a2 = (sp.diff(g, x) - sp.diff(w, x, 2))/2
    F3 = -a2*sp.diff(g, x) + g*sp.diff(a2, x)/3
    h3 = g**3*(1 - x**2/L2)**(-q3); h5 = g**5*(1 - x**2/L2)**(-q5)
    # Laurent series of i3 = x^q3 I_3 = F_3/(w h3) and the series of G_3 = h3 * sum t_k x^(2k-7+1)/(2k-6-q3) (C_0 = 0)
    i3 = sp.series(sp.cancel(F3/w)*(1 - x**2/L2)**q3/g**3, x, 0, 2*N).removeO()
    i3 = sp.expand(i3)
    Zs = 0
    for e in range(-7, 2*N):
        c = i3.coeff(x, e)
        if c != 0:
            Zs += c*x**(e + 1)/(e + 1 - q3)        # times x^(-q3); Z = x^(-q3) Zs
    G3s = sp.expand(sp.series(h3, x, 0, 2*N + 8).removeO()*Zs)
    G3s = sum(G3s.coeff(x, e)*x**e for e in range(0, 2*N))
    a4s = (sp.diff(G3s, x) - sp.diff(a2, x, 3)/3)/4
    F5s = sp.diff(a2, x)*G3s - a2*sp.diff(G3s, x) + g*sp.diff(a4s, x)/5 - a4s*sp.diff(g, x)
    i5 = sp.expand(sp.series(F5s*(1 - x**2/L2)**q5/(w*g**5), x, 0, 2*N - 12).removeO())
    print('  symbolic series done %.0f s' % (time.time() - T0), flush=True)
    # numerical parts
    Lf = mp.sqrt(mp.mpf(sp.Rational(L2).p)/sp.Rational(L2).q) if sp.Rational(L2) == L2 else mp.mpf(L2)**0.5
    A_ = mp.mpf(sp.Rational(A).p)/sp.Rational(A).q
    q3f, q5f = 2/A_, 4/A_
    fw = sp.lambdify(x, w, 'mpmath'); fg = sp.lambdify(x, g, 'mpmath')
    fa2 = [sp.lambdify(x, sp.diff(a2, x, k), 'mpmath') for k in range(4)]
    fg1 = sp.lambdify(x, sp.diff(g, x), 'mpmath')
    sS = 1 - x**2/L2
    I3e = F3*(1 + x**2/L2)*sS**(q3 - 1)/(-A*x**(1 + q3)*g**3)          # = F_3/(w H_3), no 0/0 at P
    fI3 = sp.lambdify(x, I3e, 'mpmath'); fI3d = sp.lambdify(x, sp.diff(I3e, x), 'mpmath')
    H3e = x**q3*g**3*sS**(-q3)
    fh3 = [sp.lambdify(x, sp.diff(H3e, x, k), 'mpmath') for k in range(3)]
    fwh5 = sp.lambdify(x, -A*x**(1 + q5)*g**5*sS**(1 - q5)/(1 + x**2/L2), 'mpmath')   # w H_5
    I3 = fI3
    def I5(t):
        Z = -mp.quad(I3, [t, Lf])
        i3v = I3(t); i3d = fI3d(t)
        G = fh3[0](t)*Z
        G1 = fh3[1](t)*Z + fh3[0](t)*i3v
        G2 = fh3[2](t)*Z + 2*fh3[1](t)*i3v + fh3[0](t)*i3d
        a4 = (G1 - fa2[2](t)/3)/4
        a4d = (G2 - fa2[3](t)/3)/4
        F5 = fa2[1](t)*G - fa2[0](t)*G1 + fg(t)*a4d/5 - a4*fg1(t)
        return F5/fwh5(t), G
    d = Lf*mp.mpf(dfrac.p)/dfrac.q
    # check: G_3 from quadrature against the series at delta, and C_0 = -f.p. int_0^L I_3 (should be B_3 = 0 at S_A)
    G3q = I5(d)[1]
    G3ser = sp.lambdify(x, G3s, 'mpmath')(d)
    fpint = lambda ser, q, dd: sum(mp.mpf(sp.Rational(ser.coeff(x, e)).p)/sp.Rational(ser.coeff(x, e)).q
                                   * dd**(e + 1 - q)/(e + 1 - q) if sp.Rational(ser.coeff(x, e)) == ser.coeff(x, e)
                                   else mp.mpf(sp.N(ser.coeff(x, e), 45))*dd**(e + 1 - q)/(e + 1 - q)
                                   for e in range(-13, 2*N - 13) if ser.coeff(x, e) != 0 and e + 1 - q != 0)
    q3s, q5s = mp.mpf(sp.N(q3, 45)), mp.mpf(sp.N(q5, 45))
    C0 = -(mp.quad(I3, [d, Lf]) + fpint(i3, q3s, d))
    print('  series and C_0 done', flush=True)
    res5 = i5.coeff(x, -1) if q5 == int(q5) else None
    rho = mp.mpf('1e-6')
    tail = mp.quad(lambda t: I5(t)[0], [d, (d + Lf - rho)/2, Lf - rho])
    tg, wg = [mp.mpf(v) for v in __import__('numpy').polynomial.legendre.leggauss(24)[0]], [mp.mpf(v) for v in __import__('numpy').polynomial.legendre.leggauss(24)[1]]
    # last piece r in [0, rho], r = rho tau^3 (Gauss-Legendre in tau, nodes in double precision: enough at this size)
    tail += sum(wgk/2*3*((tk + 1)/2)**2*rho*I5(Lf - rho*((tk + 1)/2)**3)[0] for tk, wgk in zip(tg, wg))
    B5 = -(tail + fpint(i5, q5s, d))
    return dict(B3=C0, G3_quad=G3q, G3_series=G3ser, res5=res5, B5=B5)

cases = [(sp.Integer(2), sp.Integer(4))]
for Av in [sp.Rational(5, 4), sp.Rational(3, 2), sp.Rational(9, 5)]:
    cases.append((Av, 6*Av*(4*Av - 3)/(8*Av - 1)))
for (Av, L2) in cases:
    r = run(Av, L2)
    print('A = %s, L^2 = %s: B_3 (C_0) = %s; G_3(delta) quad %s series %s; x^-1 coefficient (A = 2 only) %s; B_5 = %s'
          % (Av, L2, mp.nstr(r['B3'], 6), mp.nstr(r['G3_quad'], 20), mp.nstr(r['G3_series'], 20), r['res5'], mp.nstr(r['B5'], 20)),
          flush=True)
    if Av == 2:
        print('   11/1474560 =', mp.nstr(mp.mpf(11)/1474560, 20))
