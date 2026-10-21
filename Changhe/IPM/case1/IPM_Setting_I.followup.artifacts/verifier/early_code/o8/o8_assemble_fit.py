# Own exact-rational assembly of fred22 02 (19)-(26) for the fitted reference, from the fred23 02-radius inventory
# (inventory values checked separately by sampling in fit_inv.py; parameter constants against the interval enclosures
# of certify.py), then the quadratic budgets P + D t + R_vv t^2 of fred23 02 at t = 4.5e-6 (h = 0.06, h' = 3e-4)
# and t = 5e-6 (h = h' = 0).  Compared with radius_certificate.json.
from fractions import Fraction as Fr
import json
C = json.load(open('fred23/02-radius/verification/radius_certificate.json'))
I = {k: Fr(v) for k, v in C['inventory_exact'].items()}

def assemble(h, hp, tau=Fr(1), r=Fr(1, 2), sig=Fr(1), th=Fr(9, 10)):
    A0 = Fr('10.150725'); e0 = 1 / Fr('8.6000638') ** 2
    l = 1 - r; R = r * r
    Am, AM = A0 - h - tau, A0 + h + tau
    Aminus = A0 - h
    bm, bp = 2 / AM, 2 / Am
    ep = abs(e0) + hp
    assert sig > bp and th + bm > 1 and Am > 2 and e0 - hp > 0
    Z, n, D, Jn, Eo = I['Z'], I['n'], I['D'], I['J'], I['Eo']
    G0 = 1 - (2 + bp) * Eo; assert G0 > 0
    a_s, Ha, K0, Hk, Sw, Hw = I['astar'], I['Ha'], I['K0'], I['Hk'], I['w2S'], I['w2H']
    Sp = {2: I['g2S'], 3: I['g3S']}; Hp = {2: I['g2H'], 3: I['g3H']}
    gs, w2s, W0 = I['gs'], I['w2star'], I['W0']
    Z1 = max(R, R ** 2, R ** 3, R ** 3 / ((6 + sig) * (7 + sig))) / A0
    D1 = max(2 * R, 4 * R ** 2, 6 * R ** 3, (8 + sig) * R ** 3 / ((6 + sig) * (7 + sig))) / A0
    J1 = max(Fr(6), 20 * R, 42 * R ** 2, R ** 2) / A0
    ED = Fr(2, 3) * n * n * Z1
    KD = 2 / a_s * (1 + K0 * l / 2)
    Hg = Fr(4, 3) * n * Z1 + ED + l * KD
    aD = 2 * l / (3 * a_s)
    WD = (2 + bp) * aD + (1 + bp) * Hg
    d = min(Fr(1), 1 / (4 * n * Z1), a_s / (2 * l), 1 / (12 * Hg), 1 / (4 * WD), G0 / (2 * (2 + bp) * ED))
    rho = A0 / Aminus; delta0 = d / (2 * rho)
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
    DA, De, KAA, KAe, b0 = I['DA'], I['De'], I['KAA'], I['KAe'], I['B_lower']
    Pb = DA * h + De * hp + KAA * h * h / 2 + KAe * h * hp
    Dl = DN + KAv * h + Kev * hp
    return dict(d=d, delta0=delta0, M=M, Me=Me, DN=DN, KAv=KAv, Kev=Kev, Rvv=Rvv, par=Pb, linear=Dl, b0=b0, Qstar=Qs, QH=QH, KH=KH, Te=Te)

for name, (h, hp, t) in {'varying_parameters': (Fr('0.06'), Fr('0.0003'), Fr('4.5e-6')),
                         'fixed_parameters': (Fr(0), Fr(0), Fr('5e-6'))}.items():
    o = assemble(h, hp)
    ex = C['cases'][name]['exact']
    print(name)
    for k, v in o.items():
        if k in ex:
            print('  %-8s own %-22.12g json %-22.12g exact equal %s' % (k, float(v), float(Fr(ex[k])), v == Fr(ex[k])))
        else:
            print('  %-8s own %-22.12g (not in json)' % (k, float(v)))
    budget = o['par'] + o['linear'] * t + o['Rvv'] * t * t
    print('  t = %s <= delta0: %s; budget P + D t + R_vv t^2 = %.13f < b0/2 = %s: %s; B > b0 - budget >= %.10f' %
          (float(t), t <= o['delta0'], float(budget), float(o['b0'] / 2), budget < o['b0'] / 2, float(o['b0'] - budget)))
    m = o['b0'] / 2 - o['par']
    eps32 = min(o['delta0'], m / (2 * (o['linear'] + o['Rvv'] * o['delta0'])))
    print('  formula (32) radius %.6e; largest t with budget < b0/2 (root of R_vv t^2 + D t - m = 0) %.6e' %
          (float(eps32), float(2 * m / (o['linear'] + (o['linear'] ** 2 + 4 * o['Rvv'] * m) ** 0.5 * 1))))
