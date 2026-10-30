# TP-6 (c1-t1, nonlinear_closure/REVIEWS_v35.md): screening margins, the velocity-constant threshold for the
# T4-351 endpoint test, and the radius threshold for frameworks whose norm dominates H_qstar.
# Exact rational arithmetic for (a) and (d); mpmath interval arithmetic (iv, 80 digits) for (c).
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_TP6.py > check_TP6.out
from fractions import Fraction as Fr
import mpmath
from decimal import Decimal
from mpmath import iv
iv.dps = 80
ok = []
def _dec(v, n, rnd):
    # decimal string of the positive mpf v with n significant digits, rounded up (rnd = 1) or down (rnd = 0)
    with mpmath.workdps(100):
        e = int(mpmath.floor(mpmath.log10(v))) - n + 1
        m = (mpmath.ceil if rnd else mpmath.floor)(v / mpmath.mpf(10) ** e)
        return str(Decimal(int(m)).scaleb(e))
up = lambda x, n: _dec(mpmath.mpf(x.b.a), n, 1)  # upper endpoint, rounded up
lo = lambda x, n: _dec(mpmath.mpf(x.a.a), n, 0)  # lower endpoint, rounded down
def check(name, cond):
    ok.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name)

# (a) Screening margins m_j(b) = d_j - b: d_j certified lower bounds (as cited, decimal strings), b ceilings rounded up.
D = [('005', '0.02436463'), ('007', '0.004769166867'), ('008', '0.0363233974'), ('009', '0.016967603955'),
     ('010', '0.022479506978'), ('012', '0.018641021006'), ('013', '0.00199234339'), ('014', '0.00198301351067'),
     ('015', '0.001232449584356253'), ('016', '0.001470360924'), ('017', '0.001671830698'),
     ('018', '0.001655825792'), ('019', '0.001661806967'), ('020', '0.001855374677')]
B_UP = [('TB-sharp', Fr('3.7930e-6')), ('sharpw', Fr('2.8496e-6')), ('graded', Fr(25, 54684))]
def down(x, n=6):
    # round a positive Fraction down to n significant digits, returned as a decimal string
    e = 0
    while x >= 10: x /= 10; e += 1
    while x < 1: x *= 10; e -= 1
    m = int(x * 10 ** (n - 1)) / Fr(10 ** (n - 1))
    return '%se%d' % (format(float(m), '.%df' % (n - 1)), e)
print('(a) margins d_j - b (lower bounds, rounded down to 6 digits)')
print('candidate | d_j > | ' + ' | '.join(n for n, _ in B_UP))
for j, d in D:
    ms = [Fr(d) - b for _, b in B_UP]
    assert all(m > 0 for m in ms)
    print(j, '|', d, '|', ' | '.join(down(m) for m in ms))
check('every margin positive', True)
m015 = Fr('0.001232449584356253') - Fr(25, 54684)
check('smallest graded margin is 015: 7.75277e-4 < m < 7.75278e-4', Fr('7.75277e-4') < m015 < Fr('7.75278e-4'))

# (c) Necessary condition for beta_cap = B r_sep^(q+1)/sqrt(-2q-2) > b (T4-351 (1)), with B < 85020,
# r_sep = (E G/D_delta)^(1/delta), G >= Theta'(0) > 285227/10000, D_delta = 1 - c(q - delta) = 5c - 1.
c = Fr(4076476460239181, 2251799813685248)
g = 1 / c; dl = 1 - g; q = g - 4
check('D_delta = 1 - c(q - delta) equals 5c - 1 exactly', 1 - c * (q - dl) == 5 * c - 1)
check('1 - c q equals 4c exactly', 1 - c * q == 4 * c)
cI = iv.mpf(c.numerator) / c.denominator
gI = 1 / cI; dI = 1 - gI; qI = gI - 4
s2 = iv.sqrt(-2 * qI - 2)
Bup = iv.mpf(85020); Th = iv.mpf(285227) / 10000; Dd = 5 * cI - 1
B_LOW = [('TB-sharp', '3.7929e-6'), ('sharpw', '2.8495e-6'), ('graded', Fr(25, 54684))]
print('(c) beta_cap > b needs r_sep < Rmax(b) and E < Emax(b); upper bounds of the intervals, b rounded down')
E_low = iv.mpf(133)
rlow = (E_low * Th / Dd) ** (1 / dI)
cap = Bup * rlow ** (qI + 1) / s2
print('  check of T4-351: 85020 r_low^(q+1)/sqrt(-2q-2) <', up(cap, 12), '(T4-351: < 9.28e-11)')
check('T4-351 cap below 928/10^13', cap.b < iv.mpf(928) / 10 ** 13)
res = {}
for n, b in B_LOW:
    bI = iv.mpf(b.numerator) / b.denominator if isinstance(b, Fr) else iv.mpf(b)
    Rmax = (Bup / (bI * s2)) ** (1 / (-qI - 1))
    Emax = Dd / Th * Rmax ** dI
    res[n] = (Rmax, Emax)
    print('  %-8s b >= %-11s Rmax < %s  Emax < %s  133/Emax > %s' % (
        n, str(b) if not isinstance(b, Fr) else '25/54684', up(Rmax, 8), up(Emax, 8),
        lo(E_low / Emax, 6)))
check('graded: Emax < 7.95', res['graded'][1].b < 7.95)
check('sharpw: Emax < 20.11', res['sharpw'][1].b < 20.11)
check('TB-sharp: Emax < 19.09', res['TB-sharp'][1].b < 19.09)
check('graded: Rmax < 1730', res['graded'][0].b < 1730)
check('sharpw: Rmax < 13765', res['sharpw'][0].b < 13765)
# With an a priori budget H_qstar(k) <= H_max (H_max >= B/sqrt(2 pi)), the support threshold of (CI) at H = H_max is
# (sqrt(2 pi) H_max/B)^(1/delta) r_sep, so the necessary condition becomes E sqrt(2 pi) H_max/B < Emax(b); since
# B/sqrt(2 pi) < 85020/sqrt(2 pi) < 33919 it implies E H_max < 33919 Emax(b).
tp = iv.sqrt(2 * iv.pi)
check('85020/sqrt(2 pi) < 33919', (Bup / tp).b < 33919)
for n, _ in B_LOW:
    print('  %-8s E H_max < 33919 Emax(b) < %s' % (n, up(33919 * res[n][1], 8)))

# (d) Frameworks in a norm Y with ||k||_Y >= H_qstar(k): every stationary correction of R3 has H_qstar(k) >
# B/sqrt(2 pi) > 33917 (T4-351), so a contraction ball needs radius > 33917, and a Kantorovich theorem with
# solution radius t* <= 2 eta needs eta > 33917/2 and K <= 1/(2 eta) < 1/33917.
Kmax = Fr(1, 33917)
check('1/33917 < 2.9484e-5', Kmax < Fr('2.9484e-5'))
print('(d) eta > 16958.5, K < 1/33917 =', float(Kmax))
print('ALL PASS' if all(ok) else 'SOME FAIL', len(ok), 'checks')
