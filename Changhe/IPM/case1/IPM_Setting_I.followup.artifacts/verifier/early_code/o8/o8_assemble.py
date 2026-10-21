# Own exact-rational assembly of fred22 02-remainder (19)-(26) and 03 (32), (34)-(35) for the two rational references,
# from base inputs derived by hand from the q=0 closed forms (not read from the referee's JSON); compared with the JSON afterwards.
from fractions import Fraction as Fr
import json, sys
PHI = len(sys.argv) > 1 and sys.argv[1] == 'phi'
J = json.load(open('rational_bounds.json'))
if PHI:
    J = json.load(open('fred24/02-remainder/verification/norm_repair.json'))['cases']

def assemble(A0, e0, h, hp, tau, r=Fr(1, 2), sig=Fr(1), th=Fr(9, 10)):
    o = {}
    l = 1 - r; R = r * r
    Am, AM = A0 - h - tau, A0 + h + tau
    Aminus, Aplus = A0 - h, A0 + h
    bm, bp = 2 / AM, 2 / Am
    ep = abs(e0) + hp
    assert sig > bp and th + bm > 1 and Am > 2
    # origin data, q = 0: abs power-series sums in t = u^2 at t = R
    Z = (1 + R) / (1 - R); n = Z; D = 4 * R / (1 - R) ** 2; Jn = 4 * (3 + R) / (1 - R) ** 3; Eo = R / (1 - R)
    G0 = 1 - (2 + bp) * Eo; assert G0 > 0
    # tail data on [r,1]
    a_s = A0 * r * (1 + r) / (1 + R)
    Ha = 2 * A0 / (1 + R) ** 2
    K0 = 2 / (r * (1 + R))
    Hk = 2 * (1 + 3 * R) / (R * (1 + R) ** 2)
    Sw = 4 * A0 * r * (3 - R) / (1 + R) ** 3
    Hw = 12 * A0 * (1 + 6 * R + R * R) / (1 + R) ** 4
    Sp = {p: (1 + R) ** p / R ** p for p in (2, 3)}
    Hp = {p: 2 * p * (1 + R) ** (p - 1) / r ** (2 * p + 1) for p in (2, 3)}
    gs = Fr(1, 2); w2s = A0
    W0 = (1 + R) / (r * (1 + r))
    # (19)-(20), rational majorants r^{6+s} -> r^6, r^{4+s} -> r^4
    Z1 = max(R, R ** 2, R ** 3, R ** 3 / ((6 + sig) * (7 + sig))) / A0
    D1 = max(2 * R, 4 * R ** 2, 6 * R ** 3, (8 + sig) * R ** 3 / ((6 + sig) * (7 + sig))) / A0
    J1 = max(Fr(6), 20 * R, 42 * R ** 2, R ** 2) / A0
    if PHI:   # fred24 (R11): remainder v - sum c_j phi_j; own derivation: algebra norms of phi_j/u, phi_j' - phi_j/u, phi_j''/u
        # phi_j = u^j + (j-11)/2 u^9 + (9-j)/2 u^11; the algebra norm of u^(2k) is r^(2k) for every k (sigma = 1)
        pj = {j: {j: Fr(1), 9: Fr(j - 11, 2), 11: Fr(9 - j, 2)} for j in (3, 5, 7)}
        nz = lambda c: sum(abs(a) * r ** (k - 1) for k, a in c.items())              # || phi/u ||
        nd = lambda c: sum(abs(a * (k - 1)) * r ** (k - 1) for k, a in c.items())    # || phi' - phi/u ||
        nj = lambda c: sum(abs(a * k * (k - 1)) * r ** (k - 3) for k, a in c.items())  # || phi''/u ||
        Z1 = max([nz(pj[j]) for j in pj] + [R ** 3 / ((6 + sig) * (7 + sig))]) / A0
        D1 = max([nd(pj[j]) for j in pj] + [(8 + sig) * R ** 3 / ((6 + sig) * (7 + sig))]) / A0
        J1 = max([nj(pj[j]) for j in pj] + [R ** 2]) / A0
        o['A0Z1'], o['A0D1'], o['A0J1'] = Z1 * A0, D1 * A0, J1 * A0
    ED = Fr(2, 3) * n * n * Z1
    KD = 2 / a_s * (1 + K0 * l / 2)
    Hg = Fr(4, 3) * n * Z1 + ED + l * KD
    aD = 2 * l / (3 * a_s)
    WD = (2 + bp) * aD + (1 + bp) * Hg
    d = min(Fr(1), 1 / (4 * n * Z1), a_s / (2 * l), 1 / (12 * Hg), 1 / (4 * WD), G0 / (2 * (2 + bp) * ED))
    rho = A0 / Aminus; delta0 = d / (2 * rho)
    # section 4
    Nz = n / (1 - n * Z1 * d)
    Gam = 1 - (2 + bp) * (Eo + ED * d); assert Gam > 0
    T = Nz ** 4 / (2 * Gam) * (1 + Z + Z1 * d + D + D1 * d + ep * AM * (Jn + J1 * d))
    Te = Nz ** 4 * AM * (Jn + J1 * d) / (2 * Gam)
    V = Nz / Gam
    F = r ** -5 * max(1 / bm, 1 / (sig - bp))
    Io = 1 / (1 - bp)
    It = 1 / (th + bm - 1)
    cp = (1 + bp) / (3 * Am)
    am = a_s - l * d / 2; Na = 1 / am
    Hai = (Ha + d / 2) / am ** 2
    KH = (1 / (1 + th) + K0 / 2 + Hk * l / 2) * Na + (1 + K0 * l / 2) * Hai
    Ss = {p: Fr(4, 3) * Sp[p] for p in (2, 3)}
    Hs = {p: Fr(4, 3) * (Hp[p] + p * Sp[p] * d * KD) for p in (2, 3)}
    Qs = Fr(2, 3) * (abs(w2s) + d) * (1 / (A0 * gs ** 2) + ep * AM / (A0 * gs ** 3))
    Qes = 2 * AM * (abs(w2s) + d) / (3 * A0 * gs ** 3)
    QH = Fr(1, 2) * ((K0 + d * KD) * Hs[2] + (Hk + d * KH) * Ss[2] + ep * AM / A0 * ((Sw + d) * Hs[3] + (Hw + d) * Ss[3]))
    QeH = AM / (2 * A0) * ((Sw + d) * Hs[3] + (Hw + d) * Ss[3])
    M = cp * (F * T + Qs * Io * V + Fr(4, 3) * W0 * QH * It)
    Me = cp * (F * Te + Qes * Io * V + Fr(4, 3) * W0 * QeH * It)
    DN = M / d; KAv = rho * M / d * (1 / tau + 1 / Aminus); Kev = rho * Me / d; Rvv = 4 * rho ** 2 * M / d ** 2
    # (34)-(35): parameter constants over the real box A in [A-,A+], e in [e0-h', e0+h']
    bl, bh = 2 / Aplus, 2 / Aminus
    def Ib(nn):
        p = nn - 1 - bh / 2
        return 1 / bl, 1 / bl ** 2 + 1 / (p + 1) ** 2 + 1 / (bl + 1), 4 / bl ** 3 + 2 / (p + 1) ** 3 + 2 / (bl + 2)
    I3, I3p, I3pp = Ib(3); I2, I2p, I2pp = Ib(2)
    if len(sys.argv) > 1 and sys.argv[1] == 'tri':
        P5 = 5 / (6 * Aminus) + 5 * ep; P3 = 1 / (2 * Aminus) + ep    # |P5|, |P3| majorants (triangle inequality)
    else:   # exact sup of |P5|, |P3| on the box: both are monotone in A and in e, so the range is spanned by the corners
        P5 = max(abs(Fr(5, 6) / a - 5 * x) for a in (Aminus, Aplus) for x in (e0 - hp, e0 + hp))
        P3 = max(abs(Fr(1, 2) / a + x) for a in (Aminus, Aplus) for x in (e0 - hp, e0 + hp))
    P5A, P3A = Fr(5, 6) / Aminus ** 2, Fr(1, 2) / Aminus ** 2          # |dP/dA|
    P5AA, P3AA = Fr(5, 3) / Aminus ** 3, 1 / Aminus ** 3
    bA, bAA = 2 / Aminus ** 2, 4 / Aminus ** 3                          # |beta'|, |beta''|
    DA = P5A * I3 + P5 * I3p * bA + P3A * I2 + P3 * I2p * bA
    De = 5 * I3 + I2
    KAA = (P5AA * I3 + 2 * P5A * I3p * bA + P5 * (I3pp * bA ** 2 + I3p * bAA)
           + P3AA * I2 + 2 * P3A * I2p * bA + P3 * (I2pp * bA ** 2 + I2p * bAA))
    KAe = 5 * I3p * bA + I2p * bA
    b00 = 2 / A0
    SA = 6 * A0 * (4 * A0 - 3) / (8 * A0 - 1)
    assert 1 - SA * e0 > 0
    b0 = (16 - b00) / (3 * A0 * (4 + b00)) * (1 / (b00 * (1 + b00))) * (1 - SA * e0)
    Pb = DA * h + De * hp + KAA * h * h / 2 + KAe * h * hp
    m = b0 / 2 - Pb
    Dl = DN + KAv * h + Kev * hp
    eps = min(delta0, m / (2 * (Dl + Rvv * delta0))) if m > 0 else Fr(0)
    for k, v in [('d', d), ('delta0', delta0), ('M', M), ('Me', Me), ('DN', DN), ('KAv', KAv), ('Kev', Kev), ('Rvv', Rvv),
                 ('KAA', KAA), ('KAe', KAe), ('DA', DA), ('De', De), ('B_lower', b0), ('parameter_budget', Pb), ('margin', m),
                 ('epsilon_formula', eps), ('T', T), ('QH', QH), ('KH', KH), ('W0', W0), ('Hg', Hg), ('WD', WD)]:
        o[k] = v
    return o

names = ['computed_parameters', 'A4_parameter_widths', 'A4_fixed_parameters'] if PHI else None
cases = {'computed_parameters_r12': (Fr('10.150725'), Fr('0.0135206'), Fr('0.06'), Fr('0.0003'), Fr(1)),
         'earlier_reference_same_parameter_widths': (Fr(4), Fr(1, 16), Fr('0.06'), Fr('0.0003'), Fr(1, 2)),
         'earlier_reference_fixed_parameters': (Fr(4), Fr(1, 16), Fr(0), Fr(0), Fr(1, 2))}
for i, (name, args) in enumerate(cases.items()):
    o = assemble(*args)
    ex = J[names[i] if PHI else name]['exact']
    print(name)
    for k, v in o.items():
        if k in ex:
            jv = Fr(ex[k])
            print('  %-17s own %-22.12g json %-22.12g exact equal %s' % (k, float(v), float(jv), v == jv))
        else:
            print('  %-17s own %-22.12g (not in json)' % (k, float(v)))
