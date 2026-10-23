# d = 23, (1; 3, 3, 1, 1, 1, 1, 1) = two(23, 1, 6, 2, 5): recompute the real configuration at non-integer n
# (lead, 2026-10-21T22:3xZ): real root eta in (25, 26) of the resultant, common root p, nodes, and all conditions in
# the original variables v = zeta/(eta - 1), z = eta/(eta - 1), including (A7); numerical (mpmath, 80 digits)
import sys, time
src = open('../d81/gen21.py').read().split('CASES = ')[0]
exec(src)
import mpmath as mp
mp.mp.dps = 80
args = tuple(map(int, sys.argv[1:])) or (1, 6, 2, 5)
A0, al, be, m = args; d = 23
t0 = time.time()
F, G = two(d, *args)
R = s.Poly(s.resultant(F.as_expr(), G.as_expr(), p), x)
print('resultant degree', R.degree(), '%.0f s' % (time.time() - t0), flush=True)
ivs = s.Poly(R, x).intervals(eps=s.Rational(1, 10**6))
cand = [(a, b) for (a, b), k in ivs if b > d + 2 and a < d + 4]
print('real root intervals in (25, 27):', [(float(a), float(b)) for a, b in cand], flush=True)
for a, b in cand:
    a2, b2 = s.Poly(R, x).refine_root(a, b, eps=s.Rational(1, 10**75))
    eta = (mp.mpf(a2.p)/a2.q + mp.mpf(b2.p)/b2.q)/2
    print('eta =', mp.nstr(eta, 50), 'n =', mp.nstr((eta - d)/2, 50))
    Fe = [sum(mp.mpf(int(c))*eta**j for (i, j), c in F.terms() if i == k) for k in range(F.degree(p) + 1)]
    Ge = lambda pp: sum(mp.mpf(int(c))*pp**i*eta**j for (i, j), c in G.terms())
    pr = mp.polyroots(Fe[::-1], maxsteps=500, extraprec=400)
    pc = min(pr, key=lambda r: abs(Ge(r)))
    print('p =', mp.nstr(pc, 40), '|G(p)| =', mp.nstr(abs(Ge(pc)), 5), 'others:', sorted(mp.nstr(abs(Ge(r)), 3) for r in pr if r != pc))
    T = A0*eta - d; dl = al - be
    q = (-dl*eta*(2*eta - pc) + T*pc*eta - T*eta**2)/T
    U = [1, -pc, q]
    # V from the moments by Newton's identities is replaced by a direct solve: power sums of V are fixed by M_1..M_{m-1}
    # and the relation for V at eta; recompute them as in two()
    zU = mp.polyroots(U, maxsteps=200, extraprec=200)
    psU = lambda k: sum(r**k for r in zU)
    PV = [None] + [-(A0*(eta - 1)**k + al*psU(k))/be for k in range(1, m)]
    # elementary symmetric e_1..e_{m-1} of V from power sums, e_m from dl eta V'(eta) = T V(eta)
    E = [mp.mpf(1)]
    for k in range(1, m):
        E.append(sum((-1)**(i - 1)*E[k - i]*PV[i] for i in range(1, k + 1))/k)
    em = mp.mpf('0')
    def Vco(em):
        return [E[k]*(-1)**k for k in range(m)] + [em*(-1)**m]
    def rel(em):
        c = Vco(em); V = mp.polyval(c, eta); dV = mp.polyval([c[k]*(m - k) for k in range(m)], eta)
        return dl*eta*dV - T*V
    em = mp.findroot(rel, 1)
    zV = mp.polyroots(Vco(em), maxsteps=500, extraprec=400)
    zs = [(r, al) for r in zU] + [(r, be) for r in zV]
    z = eta/(eta - 1); vs = [(r/(eta - 1), w) for r, w in zs]
    e = len(vs) - 1
    Ml = [A0 + sum(w*v**l for v, w in vs) for l in range(1, e + 2)]
    print('max |M_l|, l <= e:', mp.nstr(max(abs(t) for t in Ml[:e]), 5))
    pi = lambda t: mp.fprod([t - v for v, w in vs])
    dpi = mp.diff(pi, z)
    print("pi'(z):", mp.nstr(abs(dpi), 5), ' log sum:', mp.nstr(abs(A0/(z - 1) + sum(w/(z - v) for v, w in vs) - d/z), 5))
    print('(A7):', mp.nstr(abs(Ml[e]*z - (-1)**e*d*mp.fprod([v for v, w in vs])), 5), ' M_{e+1} =', mp.nstr(Ml[e], 10))
    md = min(abs(vs[i][0] - vs[j][0]) for i in range(len(vs)) for j in range(i))
    print('min distance between nodes', mp.nstr(md, 5), ' min |v|, |v - 1|, |v - z|:',
          [mp.nstr(min(abs(v - c) for v, w in vs), 5) for c in (0, 1, z)])
    print('nodes (value, v):', [(w, mp.nstr(v, 12)) for v, w in vs])
print('%.0f s' % (time.time() - t0))
