# d = 23, type (III) (5; 2, 2, 2, 1, 1, 1): own check that the external Lambda (= my R / (c T^11), see cmp3.py) and my
# Res(N1, N0) have coefficients of one sign in powers of x - 25 (lead)
import json
from flint import fmpz_poly
c = json.load(open('../../../referee/x3q/d23/certificates/5_2_2_2_1_1_1.json'))
E = fmpz_poly([int(t) for t in c['Lambda']['coefficients_low_to_high']])
B = fmpz_poly([694477066567680, -3401339085619200, 6898555503083520, -7584246411264000, 4013344694108160, -1068170681548800, 139453747200000, -7134842880000])
def shift(P, a):
    X = fmpz_poly([a, 1]); out = fmpz_poly([0]); 
    for k in range(P.degree(), -1, -1): out = out*X + P[k]
    return out
for nm, P in (('Lambda70', E), ('Res(N1,N0)', B)):
    Q = shift(P, 25); cs = [int(t) for t in Q.coeffs()]
    print(nm, 'degree', P.degree(), 'one sign in powers of x - 25:', all(t > 0 for t in cs) or all(t < 0 for t in cs), 'zero coeffs:', sum(1 for t in cs if t == 0))
