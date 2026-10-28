"""Ball-arithmetic evaluation of the explicit upper bound of Theorem 1.4 (ii) for the complex-input norm N_alpha of
S = T_xx + i T_xy at the exponents of Table 1:
  Q_1 = 1, Q_2 = 2/sqrt(2-a) ((1-a)/(2-a))^((1-a)/2), Q_3 = 6/(3-a) (3(1-a)/(4(3-a)))^((1-a)/2), b_n = 2^(a-1)/Q_n,
  B = 2 b_3/(1-a) + min((b_3+b_1)/2, 2^a/pi), s = (1-a) B/(2 b_2), N_alpha <= 2 b_2 s^a/(a(1-a)).
Writes complex_upper.json with the ball and its upper endpoint rounded up at 4 decimals."""
from flint import arb, fmpq, ctx
import json, math
from decimal import Decimal, ROUND_CEILING
ctx.prec = 200
out = []
for t in ['1/1000', '1/100', '1/20', '1/10', '1/5', '3/10', '1/2', '3/4', '9/10', '99/100']:
    p, q = map(int, t.split('/')); a = arb(fmpq(p, q)); pi = arb.pi()
    Q2 = 2 / (2 - a).sqrt() * ((1 - a) / (2 - a)) ** ((1 - a) / 2)
    Q3 = 6 / (3 - a) * (3 * (1 - a) / (4 * (3 - a))) ** ((1 - a) / 2)
    b1 = arb(2) ** (a - 1); b2 = b1 / Q2; b3 = b1 / Q3
    c = arb.min((b3 + b1) / 2, arb(2) ** a / pi)
    B = 2 * b3 / (1 - a) + c; s = (1 - a) * B / (2 * b2); F = 2 * b2 * s ** a / (a * (1 - a))
    up = Decimal(F.upper().str(30, radius=False)).quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
    out.append(dict(alpha=t, upper_ball=F.str(30, more=True), safe_upper_4_places=str(up)))
    print(t, F.str(15), up)
json.dump(dict(precision_bits=ctx.prec, rows=out), open('complex_upper.json', 'w'), indent=1)
