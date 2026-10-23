import pickle, time, sympy as s, flint
a, x = s.symbols('a x'); tag = 't6g_23_1_6_4_2_4'
R = {st: s.Poly(pickle.load(open(tag + '_' + st + '.pkl', 'rb')), a, x) for st in ('r01', 'r02')}
def cols(F):
    m = F.degree(a); E = F.as_expr()
    return [[int(c) for c in s.Poly(E.coeff(a, m - kk), x).all_coeffs()[::-1]] for kk in range(m + 1)]
C1, C2 = cols(R['r01']), cols(R['r02']); m1, m2 = len(C1) - 1, len(C2) - 1
print('max coefficient bits', max(abs(c).bit_length() for C in C1 + C2 for c in C))
fC1 = [flint.fmpz_poly(c) for c in C1]; fC2 = [flint.fmpz_poly(c) for c in C2]
B = m2*R['r01'].degree(x) + m1*R['r02'].degree(x); print('m1 m2 B', m1, m2, B)
def syl(x0):
    p = [int(c(x0)) for c in fC1]; q = [int(c(x0)) for c in fC2]; Nn = m1 + m2; rows = []
    for i in range(m2): rows.append([0]*i + p + [0]*(Nn - i - m1 - 1))
    for i in range(m1): rows.append([0]*i + q + [0]*(Nn - i - m2 - 1))
    return int(flint.fmpz_mat(rows).det())
for x0 in (100, 2000, 4000):
    t0 = time.time(); v = syl(x0); print(x0, 'bits', v.bit_length(), '%.2f s' % (time.time() - t0), flush=True)
pr = 2**61 - 1
fm1 = [flint.nmod_poly([c % pr for c in C], pr) for C in C1]; fm2 = [flint.nmod_poly([c % pr for c in C], pr) for C in C2]
t0 = time.time()
for x0 in range(200):
    p = [int(c(x0)) for c in fm1]; q = [int(c(x0)) for c in fm2]; Nn = m1 + m2; rows = []
    for i in range(m2): rows.append([0]*i + p + [0]*(Nn - i - m1 - 1))
    for i in range(m1): rows.append([0]*i + q + [0]*(Nn - i - m2 - 1))
    int(flint.nmod_mat(rows, pr).det())
print('mod p per evaluation %.4f s' % ((time.time() - t0)/200))
