# Quartic type (VI) at d = 23, pattern (1; 3, 2, 2, 1, 1, 1, 1) (lead, 2026-10-21T22:1xZ): cross-check of the external
# degree-300 core modulo primes. Lambda_1 = Res_a(r01, r02), Lambda_2 = Res_a(r01, r03) with r03 = Res_u1(N_4, N_5 + N_6)
# (in place of Res_u1(N_5, N_6)); Sylvester determinants mod p at B + 3 points and forward differences; then the gcd
# mod p with all factors x and x - 23 removed is compared with the external core mod p.
import sys, json, pickle, time, sympy as s, flint
x, a = s.symbols('x a'); t0 = time.time(); tag = 't6g_23_1_6_4_2_4'
R = {st: s.Poly(pickle.load(open(tag + '_' + st + '.pkl', 'rb')), a, x) for st in ('r01', 'r02', 'r03')}
def cols(F):
    m = F.degree(a); E = F.as_expr()
    return [flint.fmpz_poly([int(c) for c in s.Poly(E.coeff(a, m - kk), x).all_coeffs()[::-1]]) for kk in range(m + 1)]
Cs = {st: cols(R[st]) for st in R}
c = json.load(open('../../../referee/x3q/d23/certificates/1_3_2_2_1_1_1_1.json'))['Lambda']
E = flint.fmpz_poly([int(t) for t in c['coefficients_low_to_high']]); assert E.degree() == 300
# exact sign check of the external core in powers of x - 25 (own shift, not the stored list)
Es = s.Poly(s.Poly([int(t) for t in E.coeffs()[::-1]], x).as_expr().subs(x, x + 25), x).all_coeffs()
print('external core: degree 300, coefficients in powers of x - 25 all of one sign:', all(t > 0 for t in Es) or all(t < 0 for t in Es),
      '; agrees with the stored shifted list:', [int(t) for t in c['shifted_coefficients_low_to_high']] == [int(t) for t in Es[::-1]],
      '%.0f s' % (time.time() - t0), flush=True)
def elimp(st1, st2, pr):
    C1, C2 = Cs[st1], Cs[st2]; m1, m2 = len(C1) - 1, len(C2) - 1; Nn = m1 + m2
    B = m2*R[st1].degree(x) + m1*R[st2].degree(x)
    def sylm(x0):
        pp = [int(cc(x0)) % pr for cc in C1]; qq = [int(cc(x0)) % pr for cc in C2]; rows = []
        for i in range(m2): rows.append([0]*i + pp + [0]*(Nn - i - m1 - 1))
        for i in range(m1): rows.append([0]*i + qq + [0]*(Nn - i - m2 - 1))
        return int(flint.nmod_mat(rows, pr).det())
    vals = [sylm(x0) for x0 in range(B + 3)]
    D = []; row = vals[:]
    while row:
        D.append(row[0]); row = [(row[i + 1] - row[i]) % pr for i in range(len(row) - 1)]
    assert all(t == 0 for t in D[B + 1:]), 'degree bound violated mod p'
    f = flint.nmod_poly([0], pr); bk = flint.nmod_poly([1], pr)
    for kk in range(B + 1):
        if kk: bk = bk*flint.nmod_poly([-(kk - 1) % pr, 1], pr)*pow(kk, -1, pr)
        if D[kk]: f += bk*D[kk]
    assert all(int(f(x0)) == vals[x0] for x0 in range(0, B + 3, 89))
    print('  Res_a(%s, %s) mod p: Sylvester size %d, degree bound %d, degree %d, %.0f s' % (st1, st2, Nn, B, f.degree(), time.time() - t0), flush=True)
    return f
def strip(f, r, pr):
    lin = flint.nmod_poly([(-r) % pr, 1], pr); m = 0
    while True:
        q, rem = divmod(f, lin)
        if rem.degree() >= 0: return f, m
        f = q; m += 1
for pr in (2**61 - 1, 2**31 - 1):
    print('p =', pr, flush=True)
    L1 = elimp('r01', 'r02', pr); L2 = elimp('r01', 'r03', pr)
    g = L1.gcd(L2); g1, mx = strip(g, 0, pr); g2, m23 = strip(g1, 23, pr)
    Ep = flint.nmod_poly([int(t) % pr for t in E.coeffs()], pr); Ep = Ep*pow(int(Ep.coeffs()[-1]), -1, pr)
    g2 = g2*pow(int(g2.coeffs()[-1]), -1, pr)
    print('  gcd mod p: degree %d = x^%d (x - 23)^%d times a factor of degree %d; that factor equals the external core mod p: %s'
          % (g.degree(), mx, m23, g2.degree(), g2 == Ep), flush=True)
    print('  external core mod p divides Lambda_1 and Lambda_2 mod p:', (L1 % Ep).degree() < 0, (L2 % Ep).degree() < 0,
          '; leading coefficient of the core nonzero mod p:', int(E.coeffs()[-1]) % pr != 0, flush=True)
if len(sys.argv) > 1:
    pr = 2**61 - 1
    F = c_all = json.load(open('../../../referee/x3q/d23/certificates/1_3_2_2_1_1_1_1.json'))['final_resultants']
    L1 = elimp('r01', 'r02', pr)
    for i, Fi in enumerate(F):
        co = [0]*(max(t[0][2] for t in Fi) + 1)
        for e, v in Fi: co[e[2]] = int(v) % pr
        Fp = flint.nmod_poly(co, pr); Fp = Fp*pow(int(Fp.coeffs()[-1]), -1, pr)
        Ep = flint.nmod_poly([int(t) % pr for t in E.coeffs()], pr)
        L1n = L1*pow(int(L1.coeffs()[-1]), -1, pr)
        print('external final resultant %d: degree %d; equal to my Lambda_1 mod p: %s; core divides it mod p: %s' % (i, Fp.degree(), Fp == L1n, (Fp % Ep).degree() < 0))
        print('   value at x = 0 of my Lambda_1 mod p:', int(L1(0)), '; gcd degree with mine', Fp.gcd(L1n).degree())
