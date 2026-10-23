# Independent consistency check of the Case II reduction (NOTES.md): for a real root vs of an eliminant, solve the
# moment equations and the M_{e+1} relation for v_1..v_{e+1} (vs fixed) by Newton from random complex starts, then
# check directly, in the x-coordinate and without the moment form, that Psi(x) = x^{A0} prod (x^2 - u_k)^{mu_k}
# (u_k = 1/v_k - 1) satisfies Psi' R = m s^e (x^2 - u_*) Psi (R the radical, s = 1 + x^2, u_* = -1/(2P),
# 2P = vs/(vs - 1)) and the residue condition R'(b) s(b) + 2 (N - 1 - e) b R(b) = 0 at b^2 = u_*, N = P - 1/2.
import sys, random
import mpmath as mp
mp.mp.dps = 30
def run(m, e, A0, mu, vs, tries=400):
    vs = mp.mpf(vs); A = [2 * x for x in mu]; K = e + 1
    def F(*V):
        out = [A0 + sum(a * x**l for a, x in zip(A, V)) for l in range(1, e + 1)]
        out.append((A0 + sum(a * x**(e + 1) for a, x in zip(A, V))) * vs - (-1)**e * m * mp.fprod(V))
        return out
    random.seed(1); sols = []
    for _ in range(tries):
        x0 = [mp.mpc(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(K)]
        try: V = mp.findroot(F, x0, tol=mp.mpf(10)**-25, maxsteps=60)
        except Exception: continue
        V = [V[i] for i in range(K)]
        if max(abs(f) for f in F(*V)) > mp.mpf(10)**-20: continue
        X = sum(1 / (vs - x) for x in V)
        sols.append((abs(X), V))
    sols.sort(key=lambda t: t[0])
    if not sols: print('no Newton solution'); return
    Xmin, V = sols[0]
    P = vs / (2 * (vs - 1)); us = -1 / (2 * P); N = P - mp.mpf(1) / 2
    u = [1 / x - 1 for x in V]
    # polynomials in x as coefficient lists (mpmath polyval uses highest degree first)
    def mul(p, q):
        r = [mp.mpc(0)] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q): r[i + j] += a * b
        return r
    def der(p):
        n = len(p) - 1; return [a * (n - i) for i, a in enumerate(p[:-1])]
    Psi = [mp.mpc(1)] + [mp.mpc(0)] * A0
    R = [mp.mpc(1), mp.mpc(0)]
    for uk, mk in zip(u, mu):
        f = [mp.mpc(1), mp.mpc(0), -uk]
        for _ in range(mk): Psi = mul(Psi, f)
        R = mul(R, f)
    s = [mp.mpc(1), mp.mpc(0), mp.mpc(1)]
    rhs = [mp.mpc(m)]
    for _ in range(e): rhs = mul(rhs, s)
    rhs = mul(mul(rhs, [mp.mpc(1), mp.mpc(0), -us]), Psi)
    lhs = mul(der(Psi), R)
    d = max(abs(a - b) for a, b in zip(lhs, rhs)) / max(abs(b) for b in rhs)
    b = mp.sqrt(mp.mpc(us))
    res = mp.polyval(der(R), b) * (1 + b**2) + 2 * (N - 1 - e) * b * mp.polyval(R, b)
    print('m %d e %d A0 %d mu %s vs %s: Newton solutions %d, min |sum 1/(vs - v_k)| %.3g; identity rel. defect %.3g; '
          'residue condition |.|/|R(b)| %.3g; P = %s' % (m, e, A0, mu, mp.nstr(vs, 12), len(sols), float(Xmin), float(d),
          float(abs(res) / abs(mp.polyval(R, b))), mp.nstr(P, 10)))
    print('  u_k =', [mp.nstr(x, 8) for x in u])
if __name__ == '__main__':
    m, e, A0 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); mu = tuple(int(x) for x in sys.argv[4].split(','))
    run(m, e, A0, mu, sys.argv[5])
