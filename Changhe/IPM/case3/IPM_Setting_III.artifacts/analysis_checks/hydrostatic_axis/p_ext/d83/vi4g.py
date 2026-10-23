import json, flint
pr = 2**61 - 1
c = json.load(open('../../../referee/x3q/d23/certificates/1_3_2_2_1_1_1_1.json'))
def P(Fi):
    co = [0]*(max(t[0][2] for t in Fi) + 1)
    for e, v in Fi: co[e[2]] = int(v)
    return flint.fmpz_poly(co)
F1, F2 = [P(f) for f in c['final_resultants']]
E = flint.fmpz_poly([int(t) for t in c['Lambda']['coefficients_low_to_high']])
f1 = flint.nmod_poly([int(t) % pr for t in F1.coeffs()], pr); f2 = flint.nmod_poly([int(t) % pr for t in F2.coeffs()], pr)
g = f1.gcd(f2)
def strip(f, r):
    lin = flint.nmod_poly([(-r) % pr, 1], pr); m = 0
    while True:
        q, rem = divmod(f, lin)
        if rem.degree() >= 0: return f, m
        f = q; m += 1
g1, mx = strip(g, 0); g2, m23 = strip(g1, 23)
mon = lambda f: f*pow(int(f.coeffs()[-1]), -1, pr)
Ep = mon(flint.nmod_poly([int(t) % pr for t in E.coeffs()], pr))
Er = mon(flint.nmod_poly([int(t) % pr for t in E.coeffs()[::-1]], pr))
print('gcd mod p degree', g.degree(), 'x^%d (x-23)^%d rest %d' % (mx, m23, g2.degree()), 'rest == E:', mon(g2) == Ep, 'rest == reversed E:', mon(g2) == Er)
print('E | F1 mod p', (f1 % Ep).degree() < 0, "reversed", (f1 % Er).degree() < 0)
print('gcd(rest, E) degree', mon(g2).gcd(Ep).degree())
lc = c['Lambda']['coefficients_low_to_high']; print('E low coeffs', [t[:20] for t in lc[:3]], 'high', [t[:20] for t in lc[-2:]])
# what are the stated gcd_removed, and the Lambda key list
print(c['gcd_removed'])
