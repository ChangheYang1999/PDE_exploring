# c1-t1 check for R1-044 (REVIEWS_v42): the T4-410 campaign obstruction for every starting radius R in [L0, r_beta],
# without the inner amplitude A_in, with any outer factor >= 1, and for constant or radius-dependent use in the CI test.
# Inputs: data/T4380_inputs.json (copied from c1-t4 T4-380 result.json; B, H_point, G_lower_exact, V_lower_exact).
# Main checks use V >= 0 only. The variant with V >= v0 (V_lower_exact) needs the leading-velocity asymptotic of T4-380
# section 3 and is printed as a conditional line.
# Ball arithmetic only (python-flint arb, 200 bits); no FLOAT step. No other lane's code is run or imported.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_R1044.py > check_R1044.out
import json
from fractions import Fraction as Fr
import flint

flint.ctx.prec = 200
arb = flint.arb
RES = []


def check(name, ok):
    RES.append((name, bool(ok)))
    print('%s %s' % ('PASS' if ok else 'FAIL', name))


def A_(fr):
    return arb(fr.numerator) / fr.denominator


def arbint(sv):
    body = sv.strip()[1:-1]
    mid, rad = body.split('+/-')
    return Fr(mid.strip()) - Fr(rad.strip()), Fr(mid.strip()) + Fr(rad.strip())


def lo(x):
    return (x - x.rad()).str(7, radius=False)


def hi(x):
    return (x + x.rad()).str(7, radius=False)


inp = json.load(open('data/T4380_inputs.json'))
cF = Fr(4076476460239181, 2251799813685248)
qF, dF = Fr(inp['q']), Fr(inp['delta'])
check('C0 inputs: q = 1/c - 4, delta = 1 - 1/c, D = 5c - 1 (exact)',
      qF == 1 / cF - 4 and dF == 1 - 1 / cF and Fr(inp['D']) == 5 * cF - 1)
qA, dA, DA = A_(qF), A_(dF), A_(Fr(inp['D']))
two = arb(2)
kap = 5 - 1 / A_(cF)
fac = kap / (kap + dA)
lam1 = arb(1) / 2 + 5 * two ** (1 - qA)
Sig = arb(1) / 2 + two ** (3 - qA) + two ** (1 - qA) + two ** (2 - qA) / (qA + 5)
print('     lam1 = 1/2 + 5 2^(1-q) = %s; Sigma (T4-421) = %s; kap/(kap + delta) = %s' % (
    lam1.str(10), Sig.str(10), fac.str(10)))
check('C1 lam1 > 109.6 and kap/(kap + delta) > 0.908', lam1 > arb('109.6') and fac > arb('0.908'))

BETAS = (('sharpw', Fr(28496, 10 ** 10)), ('TB', Fr(3793, 10 ** 9)), ('graded', Fr(25, 54684)),
         ('fixed', Fr(1351, 1024000000)))
s2pi = (2 * arb.pi()).sqrt()
Eu = arb(793) / 1000          # every universal constant in (1) is >= 0.7930365 (T4-381); 0.793 is used
EPROF = (('0', arb(0)), ('93/250', arb(93) / 250), ('583/1000', arb(583) / 1000))
ok2 = ok3 = ok4 = ok3b = True
e3b = None
minratio = None
lammax = {}
lammaxb = {}
for row in inp['rows']:
    Bhi = A_(arbint(row['B'])[1])
    Hlo = A_(arbint(row['H_point'])[0])
    g0 = A_(Fr(row['G_lower_exact']))
    v0 = A_(Fr(row['V_lower_exact']))
    for bn_, bv in BETAS:
        rb = (Bhi / (A_(bv) * (-2 * qA - 2).sqrt())) ** (1 / (-qA - 1))       # upper bound of r_beta
        rbd = arb((rb + rb.rad()).mid()) ** dA                                  # >= r_beta^delta
        KH = DA * Bhi * rbd / (s2pi * g0 * Hlo)                                 # >= Kcrit/H (H >= H_point)
        # C2: lower bound of J(R)/H for every R in [L0, r_beta], every eps in (0, delta], any outer factor >= 1,
        #     A_in dropped: J(R)/H >= lam1 (V + E G) R^-delta / D >= lam1 E g0 / (D r_beta^delta)
        lbE = lam1 * Eu * g0 / (DA * rbd)
        lbV = lam1 * v0 / (DA * rbd)          # conditional: the V term alone, if V >= v0
        # C3: radius-dependent use: Eeff(r) - Eprof >= fac * lam1 E g0 r^-delta / D
        lbEr = fac * lbE
        print('     %s %-6s r_beta^delta <= %s, Kcrit/H <= %s; J/H >= %s (E >= 0.793, V >= 0); radius-dependent >= %s;'
              ' conditional V-term alone (V >= v0) >= %s' % (row['candidate'], bn_, hi(rbd), hi(KH), lo(lbE), lo(lbEr),
                                                            lo(lbV)))
        ok2 = ok2 and lbE > KH
        r_ = lbEr / KH
        minratio = r_ if minratio is None or r_ < minratio else minratio
        ok3 = ok3 and lbEr > KH
        # C3b: radius-dependent use with the universal constant where it is smaller:
        #      E(s) >= m(s) = min(0.793, c s^-delta),
        #      c = lam1 E g0 / D. With s_u = (c/0.793)^(1/delta) >= r_beta, for r <= r_beta
        #      Eeff(r) >= 0.793 [1 - (delta/(kap + delta)) (r_beta/s_u)^kap] (weight kap r^kap s^(-kap-1) on (r, inf))
        cc = lam1 * Eu * g0 / DA
        su = (cc / Eu) ** (1 / dA)
        okb = su > rb
        emin = Eu * (1 - dA / (kap + dA) * (arb((rb + rb.rad()).mid()) / su) ** kap)
        ok3b = ok3b and okb and emin > KH
        e3b = emin if e3b is None or emin < e3b else e3b
        # C4: largest kernel constant Lam with Lam fac E g0/(D r_beta^delta) < Kcrit/H - Eprof (necessary)
        for en, ev in EPROF:
            room = KH - ev
            lm = room * DA * rbd / (fac * Eu * g0) if room > 0 else arb(0)
            # C4b: the same with the universal fallback E(s) = min(Eu, Eprof + Lam E g0 s^-delta / D). With
            #      Y = Lam E g0 r_beta^-delta / D the test fails iff G(Y) >= Kcrit/H, where G(Y) is the mu-average of
            #      min(Eu, Eprof + Y u^-delta), mu = kap u^(-kap-1) du on (1, inf). G(Y) = Eprof + fac Y while
            #      Y <= Eu - Eprof; beyond, G(Y) = Eu - (1 - fac)(Eu - Eprof) u*^-kap with
            #      u* = (Y/(Eu - Eprof))^(1/delta).
            #      Eu = 0.793 is the smallest admissible value and gives the largest (most generous) threshold.
            if room > 0:
                Y0 = room / fac
                if Y0 + ev <= Eu:
                    Ys = Y0
                else:
                    us = ((1 - fac) * (Eu - ev) / (Eu - KH)) ** (1 / kap)
                    Ys = (Eu - ev) * us ** dA
                lmb = Ys * DA * rbd / (Eu * g0)
            else:
                lmb = arb(0)
            lammax[(row['candidate'], bn_, en)] = lm
            lammaxb[(row['candidate'], bn_, en)] = lmb
            ok4 = ok4 and lm * 375 < lam1 * 100 and lmb * 375 < lam1 * 100 and (lmb - lm) > -arb('1e-20')
check('C2 constant use, E >= 0.793, V >= 0: lam1 E g0/(D r_beta^delta) > Kcrit/H for all 12 (reference, target) '
      'pairs', ok2)
check('C3b radius-dependent use with min(universal 0.793, c s^-delta): Eeff >= %s > Kcrit/H for all 12 pairs'
      % lo(e3b), ok3b)
check('C3 radius-dependent use: kap/(kap+delta) times the C2 bound > Kcrit/H for all 12 pairs; min ratio %s'
      % lo(minratio), ok3 and minratio > 4)
for bn_, _ in BETAS:
    print('     Lam_max %-6s (upper bounds over 007/013/014): Eprof 0: %s; 93/250: %s; 583/1000: %s' % (
        bn_, ' / '.join(hi(lammax[(cn, bn_, '0')]) for cn in ('007', '013', '014')),
        ' / '.join(hi(lammax[(cn, bn_, '93/250')]) for cn in ('007', '013', '014')),
        ' / '.join(hi(lammax[(cn, bn_, '583/1000')]) for cn in ('007', '013', '014'))))
for bn_, _ in BETAS:
    print('     Lam_max with universal fallback %-6s: Eprof 0: %s; 93/250: %s; 583/1000: %s' % (
        bn_, ' / '.join(hi(lammaxb[(cn, bn_, '0')]) for cn in ('007', '013', '014')),
        ' / '.join(hi(lammaxb[(cn, bn_, '93/250')]) for cn in ('007', '013', '014')),
        ' / '.join(hi(lammaxb[(cn, bn_, '583/1000')]) for cn in ('007', '013', '014'))))
check('C4 every necessary kernel constant Lam_max, with or without the universal fallback, is below lam1/3.75 (so '
      'T4-410 misses it by more than 3.75 times), and the fallback never lowers it', ok4)
check('C5 Lam_max < 25.3 and with the fallback < 29 for every pair and Eprof >= 0 (the largest: fixed sharpw ball, '
      'Eprof = 0)', all(v < arb('25.3') for v in lammax.values()) and all(v < 29 for v in lammaxb.values()))
print('ALL PASS' if all(o for _, o in RES) else 'SOME FAIL', '(%d checks)' % len(RES))
