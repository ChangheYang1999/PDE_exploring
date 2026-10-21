# Independent check of the verifier's higher-source-cone theorem (odd m >= 3, A > 1, g > 0, C != 0, kappa^2 < 1/(1+b)).
# Exact rationals for the coefficients; floats for the norms, the majorant and PDE residuals of the summed series.
from fractions import Fraction as Fr
import math
def run(m, A, b, C, kap, J=110, N=8):
    q = Fr(m - 1) / A; p = m - q; g = 2 * b * (A - 1)
    pn = [1 + (n + 1) * (p - 1) for n in range(N + 1)]
    Jn = [m + n * (m - 1) for n in range(N + 1)]; Mn = [m + n * (m + 1) for n in range(N + 1)]
    def solve(pp, H, lead=None):
        phi = [Fr(0)] * (J + 3); al = [Fr(0)] * (J + 3); be = [Fr(0)] * (J + 3)
        for j in range(1, J + 1, 2):
            c = A * pp - 1 - (A - 1) * j
            if c == 0:
                assert H[j] - g * be[j] == 0, ('resonance forced', j)
                phi[j] = lead if lead is not None else Fr(0)
            else:
                phi[j] = (H[j] - g * be[j]) / c
            al[j + 1] = (j - pp) * (be[j] + phi[j]) / (j + 1)
            be[j + 2] = -(pp - j) * (pp - j - 1) * (be[j] + phi[j]) / ((j + 1) * (j + 2))
        return phi[:J + 1], al[:J + 1], be[:J + 1]
    PHI, AL, BE, Hs = [], [], [], [None]
    t = solve(pn[0], [Fr(0)] * (J + 1), lead=C); PHI.append(t[0]); AL.append(t[1]); BE.append(t[2])
    for n in range(1, N + 1):
        H = [Fr(0)] * (J + 1)
        for i in range(n):
            jj = n - 1 - i
            for e in range(J + 1):
                if AL[i][e]:
                    for l in range(J + 1 - e):
                        if PHI[jj][l]: H[e + l] += AL[i][e] * (pn[jj] - l) * PHI[jj][l]
                if BE[i][e]:
                    for l in range(1, J + 2 - e):
                        if PHI[jj][l]: H[e + l - 1] -= BE[i][e] * l * PHI[jj][l]
        t = solve(pn[n], H); PHI.append(t[0]); AL.append(t[1]); BE.append(t[2]); Hs.append(H)
        assert Jn[n] < Mn[n] and c_ok(A, pn[n], Jn[n]) if False else True
    o = lambda L: min([k for k, x in enumerate(L) if x] or [10 ** 6])
    for n in range(N + 1):
        assert o(PHI[n]) >= Mn[n] and o(AL[n]) >= Mn[n] + 1 and o(BE[n]) >= Mn[n] + 2, (n, o(PHI[n]))
        if n: assert all(x == 0 for x in Hs[n][:Mn[n]])
    out = {}
    out['G_m'] = PHI[0][m] == C
    out['G_m+2 ok'] = PHI[0][m + 2] == -b * q * (q + 1) * C / ((m + 1) * (m + 2))
    out['(6) ok'] = AL[0][m + 1] == q * C / (m + 1) and BE[0][m + 2] == -q * (q + 1) * C / ((m + 1) * (m + 2))
    out['(13) ok'] = PHI[1][2 * m + 1] == -q * (m - 2 * q) * C ** 2 / (2 * (A - 1) * (m + 1) * (m + 2))
    out['first phi1 order'] = o(PHI[1])
    # (5) closed form
    rf = lambda x, k: math.prod([x + i for i in range(k)]) if k else 1
    out['(5) ok'] = all(PHI[0][m + 2 * l] == C * (-1) ** l * rf(Fr(b), l) * rf(q, 2 * l) * math.factorial(m) /
                        (math.factorial(l) * math.factorial(m + 2 * l)) for l in range((J - m) // 2 + 1))
    k = kap; B = k * k / (1 - k * k); bf = float(b)
    nrm = lambda L: sum(abs(float(x)) * k ** j for j, x in enumerate(L))
    a = [nrm(x) for x in PHI]
    abar = abs(float(C)) * k ** m / (1 - max(1, bf) * k * k)
    K = (2 * m + 1) * k / ((float(A) - 1) * (1 - k * k) * (1 - bf * B))
    out['a0/abar'] = a[0] / abar
    out['max beta/(B phi)'] = max(nrm(BE[n]) / (B * a[n]) for n in range(N + 1))
    out['max alpha/(k phi/(1-k^2))'] = max(nrm(AL[n]) / (k / (1 - k * k) * a[n]) for n in range(N + 1))
    out['max a_n/(K conv)'] = max(a[n] / (K * sum(a[i] * a[n - 1 - i] for i in range(n))) for n in range(1, N + 1) if a[n])
    R = (1 / (4 * K * abar)) ** (1 / (float(p) - 1))
    res = []
    for (rr, zf) in [(0.3, 0.5), (0.6, -0.8), (0.9, 0.9)]:
        r = rr * R; z = zf * k; y = z * r; s = -r
        S = {x: 0.0 for x in ['v', 'vs', 'vy', 'V1', 'V2', 'V1s', 'V1y', 'V2s', 'V2y']}; sc = 0.0
        for n in range(N + 1):
            P = float(pn[n])
            ev = lambda L: sum(float(c) * z ** j for j, c in enumerate(L) if c)
            dv = lambda L: sum(j * float(c) * z ** (j - 1) for j, c in enumerate(L) if c and j)
            f, fp, al, alp, be, bep = ev(PHI[n]), dv(PHI[n]), ev(AL[n]), dv(AL[n]), ev(BE[n]), dv(BE[n])
            S['v'] += r ** P * f; S['vs'] += -r ** (P - 1) * (P * f - z * fp); S['vy'] += r ** (P - 1) * fp
            S['V1'] += r ** P * al; S['V2'] += r ** P * be
            S['V1s'] += -r ** (P - 1) * (P * al - z * alp); S['V1y'] += r ** (P - 1) * alp
            S['V2s'] += -r ** (P - 1) * (P * be - z * bep); S['V2y'] += r ** (P - 1) * bep
            sc = max(sc, abs(r ** P * f), abs(float(g) * r ** P * be))
        T = float(A) * s * S['vs'] + y * S['vy'] - S['v'] + float(g) * S['V2'] + S['V1'] * S['vs'] + S['V2'] * S['vy']
        res.append('%.0e/%.0e/%.0e' % (abs(T) / sc, abs(S['V1s'] + S['V2y']) * r / sc, abs(S['V2s'] - S['V1y'] + S['vs']) * r / sc))
    out['residuals'] = res
    out['p'] = str(p)
    return out
c_ok = None
cases = [(3, Fr(3), Fr(7, 4), Fr(1), 0.25), (5, Fr(3, 2), Fr(3), Fr(-2), 0.45), (5, Fr(2), Fr(1, 2), Fr(1), 0.6),
         (7, Fr(12, 7), Fr(1), Fr(1), 0.5), (5, Fr(5, 3), Fr(10), Fr(3, 2), 0.25), (9, Fr(4), Fr(1, 3), Fr(-1), 0.7)]
for cs in cases:
    print('m, A, b, C, kappa =', cs)
    for kk, vv in run(*cs).items(): print('   ', kk, vv)
