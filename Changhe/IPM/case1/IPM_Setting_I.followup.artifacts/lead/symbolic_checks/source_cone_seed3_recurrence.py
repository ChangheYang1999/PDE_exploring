# Independent check of the verifier's third-source-cone construction (recurrence (11), forcing (14)).
# Exact rationals for the recurrence (A, b, lambda rational; C kept symbolic as a scale: C = 1 then rescale), floats for residuals.
from fractions import Fraction as Fr
import math, sys
def run(A, b, J=90, N=10):
    lam = Fr(2) / A; g = 2 * b * (A - 1); d = 3 - lam
    Cn = 1 / (12 * math.sin(math.pi * float(lam)))
    p = [d + n * (2 - lam) for n in range(N + 1)]
    def solve(pp, h, phi3=None):
        phi = [Fr(0)] * (J + 3); al = [Fr(0)] * (J + 3); be = [Fr(0)] * (J + 3)
        for j in range(1, J + 1, 2):
            c = A * pp - 1 - (A - 1) * j
            if c == 0:
                assert h[j] - g * be[j] == 0, ('resonance incompatible', j)
                phi[j] = phi3 if phi3 is not None else Fr(0)
            else:
                phi[j] = (h[j] - g * be[j]) / c
            al[j + 1] = (j - pp) * (be[j] + phi[j]) / (j + 1)
            be[j + 2] = -(pp - j) * (pp - j - 1) * (be[j] + phi[j]) / ((j + 1) * (j + 2))
        return phi[:J + 1], al[:J + 1], be[:J + 1]
    PHI, AL, BE = [], [], []
    ph, a_, b_ = solve(p[0], [Fr(0)] * (J + 1), phi3=Fr(1))   # C = 1; true field scales as C^(n+1)
    PHI.append(ph); AL.append(a_); BE.append(b_)
    for n in range(1, N + 1):
        h = [Fr(0)] * (J + 1)
        for i in range(n):
            jj = n - 1 - i
            for e in range(J + 1):
                if AL[i][e]:
                    for l in range(J + 1 - e):
                        if PHI[jj][l]: h[e + l] += AL[i][e] * (p[jj] - l) * PHI[jj][l]
                if BE[i][e]:
                    for l in range(1, J + 2 - e):
                        if PHI[jj][l]: h[e + l - 1] += -BE[i][e] * l * PHI[jj][l]
        ph, a_, b_ = solve(p[n], h)
        PHI.append(ph); AL.append(a_); BE.append(b_)
        if n == 1: h17 = h[7]
    # orders (15)
    for n in range(N + 1):
        o = lambda L: min([k for k, x in enumerate(L) if x] or [999])
        assert o(PHI[n]) == 4 * n + 3 and o(AL[n]) >= 4 * n + 4 and o(BE[n]) >= 4 * n + 5, (n, o(PHI[n]), o(AL[n]), o(BE[n]))
    k = 0.25
    nrm = lambda L: sum(abs(float(x)) * k ** j for j, x in enumerate(L))
    a = [nrm(PHI[n]) * Cn ** (n + 1) for n in range(N + 1)]
    K = 28 / ((15 - float(b)) * (float(A) - 1))
    cat = lambda n: math.comb(2 * n, n) // (n + 1)
    out = {'a0': a[0], 'C/60': Cn / 60, 'G5coef': float(PHI[0][5]), 'pred5': float(-b * lam * (lam + 1) / 20),
           'phi17': float(PHI[1][7]), 'pred(4)': float(-lam * (3 - 2 * lam) / (40 * (A - 1))), 'h17': float(h17),
           'pred h17': float(lam * (3 - 2 * lam) / 20)}
    out['beta/phi'] = max(nrm(BE[n]) / nrm(PHI[n]) for n in range(N + 1))
    out['alpha/phi'] = max(nrm(AL[n]) / nrm(PHI[n]) for n in range(N + 1))
    out['recur'] = max(a[n] / (K * sum(a[i] * a[n - 1 - i] for i in range(n))) for n in range(1, N + 1))
    out['catalan'] = max(a[n] / (cat(n) * K ** n * a[0] ** (n + 1)) for n in range(N + 1))
    # residuals of (1) at interior points with the summed series (C = Cn)
    R3 = (15 * (15 - float(b)) * (float(A) - 1) / (28 * Cn)) ** (1 / (2 - float(lam)))
    res = []
    for (rf, z) in [(0.3, 0.1), (0.5, 0.2), (0.8, -0.15)]:
        r = rf * R3; y = z * r; s = -r
        v = vs = vy = V1 = V2 = V1s = V1y = V2s = V2y = 0.0; scale = 0.0
        for n in range(N + 1):
            pn = float(p[n]); cf = Cn ** (n + 1)
            P = [float(x) * cf for x in PHI[n]]; Al = [float(x) * cf for x in AL[n]]; Be = [float(x) * cf for x in BE[n]]
            ev = lambda L: sum(c * z ** j for j, c in enumerate(L))
            dv = lambda L: sum(j * c * z ** (j - 1) for j, c in enumerate(L) if j)
            f, fp = ev(P), dv(P); al, alp = ev(Al), dv(Al); be, bep = ev(Be), dv(Be)
            v += r ** pn * f; vs += -r ** (pn - 1) * (pn * f - z * fp); vy += r ** (pn - 1) * fp
            V1 += r ** pn * al; V2 += r ** pn * be
            V1s += -r ** (pn - 1) * (pn * al - z * alp); V1y += r ** (pn - 1) * alp
            V2s += -r ** (pn - 1) * (pn * be - z * bep); V2y += r ** (pn - 1) * bep
            scale = max(scale, abs(r ** pn * f))
        T = float(A) * s * vs + y * vy - v + float(g) * V2 + V1 * vs + V2 * vy
        res.append((rf, z, T / scale, (V1s + V2y) * r / scale, (V2s - V1y + vs) * r / scale))
    out['residuals(rel)'] = [tuple('%.1e' % x if isinstance(x, float) and abs(x) < 1e-3 else x for x in t) for t in res]
    out['R3'] = R3
    return out
for A, b in [(Fr(3), Fr(7, 4)), (Fr(5, 2), Fr(8, 5)), (Fr(6), Fr(19, 10))]:
    print('A =', A, 'b =', b)
    for kk, vv in run(A, b).items(): print('   ', kk, vv)
