"""Independent recomputation of the A.3.8 enclosures and outward-rounded decimal endpoints (rep4 item 4).

Reads the four serialized inputs (exact rational angular means, binary64 map power q and length L_g) read-only,
recomputes in 256-bit ball arithmetic P_N'(t_0) for the Radau nodes t_j = -cos(2 pi j/(2N+1)) and the
physical derivative 2^q P_N'(t_0)/L_g, compares with the recorded balls, and prints closed intervals whose decimal
endpoints are rounded outward (floor of the lower end, ceiling of the upper end) to 20 significant digits.
"""
import json
from fractions import Fraction
from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_CEILING
from flint import arb, fmpq, ctx

ctx.prec = 256
base = 'verification/research/regularity/verification/'
names = ['coupled_N48_a1', 'res_p23_N96M16', 'res_p23_N192M24', 'res_p23_N256M32']
recorded = {row['input'].split('/')[-1].replace('_input.json', ''): row
            for row in json.load(open(base + 'arb_first_jets.json'))}


def exact(a):
    m, e = a.man_exp()
    return Fraction(int(m)) * (Fraction(2) ** int(e))


def endpoints(ball, digits=20):
    mid = exact(ball.mid())
    rad = exact(ball.rad())
    lo, hi = mid - rad, mid + rad
    getcontext().prec = 120
    def rnd(fr, mode):
        d = Decimal(fr.numerator) / Decimal(fr.denominator)
        q = Decimal(1).scaleb(d.adjusted() - digits + 1)
        return d.quantize(q, rounding=mode)
    return rnd(lo, ROUND_FLOOR), rnd(hi, ROUND_CEILING), lo, hi


for nm in names:
    cert = json.load(open(base + nm + '_input.json'))
    N, M = cert['N'], cert['M']
    vals = [arb(fmpq(int(a), int(b))) for a, b in cert['mean_radial_values']]
    assert len(vals) == N + 1
    nodes = [-(2 * arb.pi() * j / (2 * N + 1)).cos() for j in range(N + 1)]
    lam = []
    for j in range(N + 1):
        prod = arb(1)
        for k in range(N + 1):
            if k != j:
                prod *= nodes[j] - nodes[k]
        lam.append(1 / prod)
    der = arb(0)
    for j in range(1, N + 1):
        der += lam[j] / lam[0] / (nodes[0] - nodes[j]) * (vals[j] - vals[0])
    q = Fraction(float.fromhex(cert['map_power_hex']))
    L = Fraction(float.fromhex(cert['length_hex']))
    phys = der * (arb(fmpq(q.numerator, q.denominator)) * arb(2).log()).exp() / arb(fmpq(L.numerator, L.denominator))
    rec = recorded[nm]
    rec_phys = arb(rec['mean_dr_b_at_zero'].strip('[]').split(' +/- ')[0], rec['mean_dr_b_at_zero'].strip('[]').split(' +/- ')[1])
    rec_der = arb(rec['mean_dt_b_at_minus1'].strip('[]').split(' +/- ')[0], rec['mean_dt_b_at_minus1'].strip('[]').split(' +/- ')[1])
    lo, hi, flo, fhi = endpoints(phys)
    lo2, hi2, _, _ = endpoints(der)
    print(f'(N, M) = ({N}, {M}); q = {cert["map_power_hex"]} = {float.fromhex(cert["map_power_hex"])!r}; '
          f'L_g = {cert["length_hex"]}')
    print('   recomputed d/dr kappa_0 at 0 :', phys.str(30, radius=True))
    print('   overlaps recorded ball       :', phys.overlaps(rec_phys), ' derivative ball overlaps:', der.overlaps(rec_der))
    print('   radius (physical)            :', phys.rad().str(3))
    print('   outward interval (physical)  : [%s, %s]' % (lo, hi))
    print('   outward interval kappa_0\'(-1): [%s, %s]' % (lo2, hi2))
    print('   excludes 0:', flo > 0, ' lower endpoint check:', Fraction(str(lo)) <= flo, Fraction(str(hi)) >= fhi)
