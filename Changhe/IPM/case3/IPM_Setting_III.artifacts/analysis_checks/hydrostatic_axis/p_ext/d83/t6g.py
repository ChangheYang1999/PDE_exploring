# Type (VI) generalized (lead, 2026-10-21T20:5xZ; from ../d81/t6*.py): a singleton a of value wa, a pair
# U = v^2 + u1 v + u2 of value wu and a class V = v^k + c1 v^(k-1) + ... + ck of k nodes of value wv; e = k + 2.
# al = 1/(x - a), be = U'(x)/U(x), om = V'(x)/V(x): al + be + om = 0, wa al + wu be + wv om = -T/x.
# Regular branch (be om != 0): u2 from be, c1..c_{k-1} from M_1..M_{k-1}, ck from om; M_k, M_{k+1}, M_{k+2} remain.
# usage: python3 t6g.py d A0 wa wu wv k stage   (stage: s1 | r01 | r02 | r12 | L | p)
import sys, os, pickle, time, sympy as s, flint
d, A0, wa, wu, wv, k = [int(t) for t in sys.argv[1:7]]; stage = sys.argv[7]
tag = 't6g_%d_%d_%d_%d_%d_%d' % (d, A0, wa, wu, wv, k)
x, a, u1, u2, v = s.symbols('x a u1 u2 v'); cs = s.symbols('c1:%d' % (k + 1))
T = A0*x - d
def psums(cf, kmax):
    r = len(cf); P = []
    for l in range(1, kmax + 1):
        t = -sum(cf[i-1]*P[l-i-1] for i in range(1, min(l-1, r) + 1))
        if l <= r: t -= l*cf[l-1]
        P.append(s.expand(t))
    return P
U = v**2 + u1*v + u2; V = v**k + sum(c*v**(k - 1 - i) for i, c in enumerate(cs))
pU = psums([u1, u2], k + 2); pV = psums(list(cs), k + 2)
M = lambda l: A0*(x - 1)**l + wa*a**l + wu*pU[l-1] + wv*pV[l-1]
def num(e, *vars_):
    n_ = s.fraction(s.cancel(s.together(e)))[0]
    return s.Poly(n_, *vars_).primitive()[1]
def full(e, sub):
    for _ in range(k + 3): e = e.subs(sub)
    return e
al = 1/(x - a); be = (-T/x - (wa - wv)*al)/(wu - wv); om = -al - be
assert s.simplify(wa*al + wu*be + wv*om + T/x) == 0
known = [x, T, x - a, s.fraction(s.cancel(be))[0], s.fraction(s.cancel(om))[0]]
t0 = time.time()
if stage == 's1':
    sub = {u2: s.cancel(s.solve(s.diff(U, v).subs(v, x) - be*U.subs(v, x), u2)[0])}
    for l in range(1, k):
        sl = s.solve(s.cancel(full(M(l), sub)), cs[l-1]); assert len(sl) == 1; sub[cs[l-1]] = s.cancel(sl[0])
    Vs = full(V, sub)
    sl = s.solve(s.diff(Vs, v).subs(v, x) - om*Vs.subs(v, x), cs[k-1]); assert len(sl) == 1; sub[cs[k-1]] = s.cancel(sl[0])
    N = [num(full(M(l), sub), u1, a, x) for l in (k, k + 1, k + 2)]
    for l, P in zip((k, k + 1, k + 2), N):
        fl = s.factor_list(P.as_expr())[1]
        print('M_%d numerator: deg u1 %d, deg a %d, deg x %d, terms %d; factors (deg u1, deg a, deg x, mult):' % (l, P.degree(u1), P.degree(a), P.degree(x), len(P.terms())),
              [(s.Poly(f, u1, a, x).degree(u1), s.Poly(f, u1, a, x).degree(a), s.Poly(f, u1, a, x).degree(x), m) for f, m in fl], '%.0f s' % (time.time() - t0), flush=True)
    pickle.dump({'N': [P.as_expr() for P in N]}, open(tag + '_s1.pkl', 'wb'))
elif stage in ('r01', 'r02', 'r12', 'r03'):
    # r03: Res_u1(N_0, N_1 + N_2), a second partner for r01 when Res_u1(N_1, N_2) is too slow
    N = pickle.load(open(tag + '_s1.pkl', 'rb'))['N']; N.append(s.expand(N[1] + N[2])); i, j = int(stage[1]), int(stage[2])
    r = s.resultant(N[i], N[j], u1)
    print('Res_u1(N_%d, N_%d) computed %.0f s' % (i + k, j + k, time.time() - t0), flush=True)
    if os.environ.get('DIV'):
        # remove the known factors by exact division (no factorization), then take the primitive part
        R_ = s.Poly(r, a, x)
        for kn in known:
            K_ = s.Poly(kn, a, x)
            if K_.is_ground: continue
            mlt = 0
            while True:
                q_, r_ = R_.div(K_)
                if not r_.is_zero: break
                R_ = q_; mlt += 1
            print('   known factor', kn, 'removed with multiplicity', mlt, '%.0f s' % (time.time() - t0), flush=True)
        out = R_.primitive()[1].as_expr()
    else:
        c, fl = s.factor_list(r); keep = []
        for f, m in fl:
            P = s.Poly(f, a, x); isk = any(s.simplify(f/kn).is_number for kn in known)
            print('   factor deg a %d deg x %d mult %d known %s' % (P.degree(a), P.degree(x), m, isk), flush=True)
            if not isk: keep.append(f**m)
        out = s.expand(s.prod(keep))
    print('   kept: deg a %d deg x %d, %.0f s' % (s.Poly(out, a, x).degree(a), s.Poly(out, a, x).degree(x), time.time() - t0), flush=True)
    pickle.dump(out, open(tag + '_' + stage + os.environ.get('SUF', '') + '.pkl', 'wb'))
elif stage == 'L':
    def cols(F):
        m = F.degree(a); E = F.as_expr()
        return [[int(c) for c in s.Poly(E.coeff(a, m - kk), x).all_coeffs()[::-1]] for kk in range(m + 1)]
    def elim(F1, F2):
        C1, C2 = cols(F1), cols(F2); m1, m2 = len(C1) - 1, len(C2) - 1
        fC1 = [flint.fmpz_poly(c) for c in C1]; fC2 = [flint.fmpz_poly(c) for c in C2]
        def syl(x0):
            p = [int(c(x0)) for c in fC1]; q = [int(c(x0)) for c in fC2]; Nn = m1 + m2; rows = []
            for i in range(m2): rows.append([0]*i + p + [0]*(Nn - i - m1 - 1))
            for i in range(m1): rows.append([0]*i + q + [0]*(Nn - i - m2 - 1))
            return int(flint.fmpz_mat(rows).det())
        B = m2*F1.degree(x) + m1*F2.degree(x)
        vals = [syl(x0) for x0 in range(B + 3)]
        D = []; row = vals[:]
        while row:
            D.append(row[0]); row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        assert all(t == 0 for t in D[B + 1:]), 'degree bound violated'
        deg = max(kk for kk in range(B + 1) if D[kk] != 0)
        f = flint.fmpq_poly([0]); bk = flint.fmpq_poly([1])
        for kk in range(deg + 1):
            if kk: bk = bk*flint.fmpq_poly([-(kk - 1), 1])/kk
            if D[kk]: f += D[kk]*bk
        assert f.denom() == 1
        L = flint.fmpz_poly([int(c) for c in f.numer().coeffs()])
        assert all(L(x0) == vals[x0] for x0 in range(0, B + 3, 97))
        print('Sylvester size', m1 + m2, 'degree bound', B, 'degree', L.degree(), '%.0f s' % (time.time() - t0), flush=True)
        return L
    R = {st: s.Poly(pickle.load(open(tag + '_' + st + '.pkl', 'rb')), a, x) for st in ('r01', 'r02', 'r12')}
    def onesign(L, nm):
        # every irreducible factor of L, in powers of x - (d + 2)
        okL = True
        for h, m in L.factor()[1]:
            G = s.Poly([int(t) for t in h.coeffs()[::-1]], x)
            sh = s.Poly(G.as_expr().subs(x, x + d + 2), x).all_coeffs()
            one = all(t > 0 for t in sh) or all(t < 0 for t in sh); okL = okL and one
            print('  %s factor degree %d mult %d one sign in powers of x - %d: %s' % (nm, h.degree(), m, d + 2, one), flush=True)
        print('RESULT %s alone has no root x >= %d:' % (nm, d + 2), okL, flush=True)
    if os.environ.get('PART') in ('1', '2'):
        # one of the two eliminations only (saved), with the sign check of all its factors
        pr = os.environ['PART']; L = elim(R['r01'], R['r02'] if pr == '1' else R['r12'])
        pickle.dump([int(t) for t in L.coeffs()], open(tag + '_L%s.pkl' % pr, 'wb'))
        onesign(L, 'Lambda_' + pr); sys.exit(0)
    if os.environ.get('PART') == 'm':
        # Lambda_2 modulo primes pr (Sylvester determinants mod pr at B + 3 points, forward differences), and the
        # degree of its gcd mod pr with every irreducible factor h of Lambda_1 (saved by PART=1). If pr does not
        # divide the leading coefficient of h and the gcd mod pr is 1, then h and Lambda_2 are coprime over Q.
        L1 = flint.fmpz_poly(pickle.load(open(tag + '_L1.pkl', 'rb'))); fac = L1.factor()[1]
        C1, C2 = cols(R['r01']), cols(R['r12']); m1, m2 = len(C1) - 1, len(C2) - 1
        fC1 = [flint.fmpz_poly(c) for c in C1]; fC2 = [flint.fmpz_poly(c) for c in C2]
        B = m2*R['r01'].degree(x) + m1*R['r12'].degree(x)
        for pr in (2**61 - 1, 2**31 - 1):
            def sylm(x0):
                pp = [int(c(x0)) % pr for c in fC1]; qq = [int(c(x0)) % pr for c in fC2]; Nn = m1 + m2; rows = []
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
            print('Lambda_2 mod %d: degree %d (bound %d), %.0f s' % (pr, f.degree(), B, time.time() - t0), flush=True)
            for h, mh in fac:
                hm = flint.nmod_poly([int(c) % pr for c in h.coeffs()], pr)
                assert int(h.coeffs()[-1]) % pr != 0
                print('   factor of Lambda_1 of degree %d (mult %d): gcd with Lambda_2 mod p has degree %d' % (h.degree(), mh, hm.gcd(f).degree()), flush=True)
        sys.exit(0)
    if os.environ.get('PART') == 'g':
        L1, L2 = [flint.fmpz_poly(pickle.load(open(tag + '_L%s.pkl' % pr, 'rb'))) for pr in '12']
    else:
        L1 = elim(R['r01'], R['r02']); L2 = elim(R['r01'], R['r12'])
    for nm, L in (('Lambda_1', L1), ('Lambda_2', L2)):
        print(nm, 'factors (degree, multiplicity):', sorted([(g.degree(), m) for g, m in L.factor()[1]]), flush=True)
    g = L1.gcd(L2); cg, flg = g.factor()
    print('gcd degree', g.degree(), 'factors:', sorted([(h.degree(), m) for h, m in flg]), [str(h) for h, m in flg if h.degree() <= 1], flush=True)
    ok = True
    for h, m in flg:
        G = s.Poly([int(t) for t in h.coeffs()[::-1]], x)
        sh = s.Poly(G.as_expr().subs(x, x + d + 2), x).all_coeffs()
        one = all(t > 0 for t in sh) or all(t < 0 for t in sh); ok = ok and one
        print('  factor degree', h.degree(), 'mult', m, 'coefficients in powers of x - %d one sign' % (d + 2), one, 'least |c|', min(abs(t) for t in sh), flush=True)
    print('RESULT gcd has no root x >= %d:' % (d + 2), ok, flush=True)
    pickle.dump({'L1': [int(t) for t in L1.coeffs()], 'L2': [int(t) for t in L2.coeffs()], 'g': [int(t) for t in g.coeffs()]}, open(tag + '_L.pkl', 'wb'))
elif stage == 'p':
    for name in ('be = 0', 'om = 0'):
        if name == 'be = 0':
            aa = s.cancel(x*(1 + s.Rational(wa - wv)/T)); al0 = 1/(x - aa); om0 = -al0
            assert s.simplify(wa*al0 + wv*om0 + T/x) == 0
            sub = {u1: -2*x, a: aa}
            for l in range(1, k):
                sl = s.solve(s.cancel(full(M(l), sub)), cs[l-1]); assert len(sl) == 1; sub[cs[l-1]] = s.cancel(sl[0])
            Vs = full(V, sub); sl = s.solve(s.diff(Vs, v).subs(v, x) - om0*Vs.subs(v, x), cs[k-1]); assert len(sl) == 1
            sub[cs[k-1]] = s.cancel(sl[0]); var = u2; rest = (k, k + 1, k + 2)
        else:
            aa = s.cancel(x*(1 + s.Rational(wa - wu)/T)); al0 = 1/(x - aa); be0 = -al0
            assert s.simplify(wa*al0 + wu*be0 + T/x) == 0
            sub = {a: aa}
            sl = s.solve(s.diff(U, v).subs(v, x) - be0*U.subs(v, x), u2); assert len(sl) == 1; sub[u2] = s.cancel(sl[0])
            for l in range(1, k - 1):
                sl = s.solve(s.cancel(full(M(l), sub)), cs[l-1]); assert len(sl) == 1; sub[cs[l-1]] = s.cancel(sl[0])
            sl = s.solve(full(s.diff(V, v).subs(v, x), sub), cs[k-2]); assert len(sl) == 1; sub[cs[k-2]] = s.cancel(sl[0])
            sl = s.solve(s.cancel(full(M(k), sub)), cs[k-1]); assert len(sl) == 1; sub[cs[k-1]] = s.cancel(sl[0])
            var = u1; rest = (k - 1, k + 1, k + 2)
        Ns = [num(full(M(l), sub), var, x) for l in rest]
        print(name, ': a =', aa, '; numerators of M_%d, M_%d, M_%d have degrees' % rest, [P.degree(var) for P in Ns], 'in', var, flush=True)
        r1 = s.Poly(s.resultant(Ns[0].as_expr(), Ns[1].as_expr(), var), x)
        r2 = s.Poly(s.resultant(Ns[0].as_expr(), Ns[2].as_expr(), var), x)
        g = s.Poly(s.gcd(r1, r2), x)
        rr = g.count_roots(d + 2, None) if g.degree() > 0 else 0
        print('   resultants of degrees', r1.degree(), r2.degree(), '; gcd', s.factor(g.as_expr()), '; roots x >= %d:' % (d + 2), rr, flush=True)
