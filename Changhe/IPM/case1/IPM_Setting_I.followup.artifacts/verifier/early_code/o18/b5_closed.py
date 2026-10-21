# (o18)(a): fred31 closed form (21) for B_5 on R12 at L^2 = S_A, against the own series code (code/series_bj.py),
# plus the referee's G_3 (23) and F_5 (25) against the own hierarchy series, at A in (1, 2) and in (2, 4).
import sys
sys.path.insert(0, 'verifier/early_code')
import mpmath as mp
from series_bj import Bj, r12
mp.mp.dps = 40
n = 200

def closed(A):
    L = mp.sqrt(6*A*(4*A - 3)/(8*A - 1))
    P = 1248*A**4 - 548*A**3 + 297*A**2 - 178*A + 84
    return P*mp.beta(-4 - 2/A, 4/A)/(15*A*(2*A - 1)*(3*A - 2)*(4*A - 3)*(8*A - 1)*L**(10 + 4/A)), L

def closed26(A):
    # (26) before the beta recurrence
    L = mp.sqrt(6*A*(4*A - 3)/(8*A - 1)); q = 4/A
    c = [2076*A**2 + 741*A - 36, -3060*A**2 + 305*A - 70, 1400*A**2 - 950*A + 50]
    return mp.fsum(c[k]*mp.beta(k - 4 - q/2, q) for k in range(3))/(30*A*(4*A - 3)*(8*A - 1)*L**(10 + q))

As = sys.argv[1].split(',') if len(sys.argv) > 1 else ['1.05', '1.25', '1.5', '1.8', '1.95', '2.5', '3', '3.5', '3.9']
for a in As:
    A = mp.mpf(a)
    Bc, L = closed(A)
    B26 = closed26(A)
    wn, wd, gn, gd = r12(A, L)
    xe = [L*mp.mpf(k)/10 for k in (3, 5)]
    res, s0, sP = Bj(wn, wd, gn, gd, A, L, n, xe, jmax=5)
    Bs = res[5][0]['B']; Bs2 = res[5][1]['B']
    p5 = 10 + 4/A
    nat = L**(p5 - 4)
    # G_3 and F_5 closed forms at x = 0.3 L, 0.5 L (series at 0) and x = 0.7 L, 0.9 L (series at P)
    errG = []; errF = []
    for k, ser, sh in [(3, s0, 0), (5, s0, 0), (7, sP, L), (9, sP, L)]:
        x = L*mp.mpf(k)/10; u = x/L
        G3c = 10*A*u**2/((8*A - 1)*(1 + u**2)**3)
        c = [2076*A**2 + 741*A - 36, -3060*A**2 + 305*A - 70, 1400*A**2 - 950*A + 50]
        F5c = u**2*(c[0] + c[1]*u**2 + c[2]*u**4)/(15*(4*A - 3)*(8*A - 1)*(1 + u**2)**6)
        errG.append(abs(ser['G3'](x - sh) - G3c)/abs(G3c)); errF.append(abs(ser['F5'](x - sh) - F5c)/abs(F5c))
    print('A = %s: closed (21) %s  (26) %s  series %s (x = 0.3L), %s (x = 0.5L)' % (
        a, mp.nstr(Bc, 20), mp.nstr(B26, 20), mp.nstr(Bs, 20), mp.nstr(Bs2, 20)))
    print('   rel diff (21)/series %s, (26)/(21) %s; natural units %s; G3 (23) rel err max %s; F5 (25) rel err max %s'
          % (mp.nstr(abs(Bc/Bs - 1), 3), mp.nstr(abs(B26/Bc - 1), 3), mp.nstr(Bc*nat, 12), mp.nstr(max(errG), 3),
             mp.nstr(max(errF), 3)), flush=True)
