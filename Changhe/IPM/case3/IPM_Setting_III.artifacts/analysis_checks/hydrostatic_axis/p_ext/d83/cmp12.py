# d = 23, types (I) and (II) (gen23 cases): my exact resultant R against the external Lambda: does Lambda divide R,
# and what is R/Lambda (powers of x and T times what)? (lead, 2026-10-21T22:4xZ)
import sys, time, json
src = open('gen23.py').read().split('sel = ')[0]
exec(src)
from flint import fmpz_poly
C = '../../../referee/x3q/d23/certificates/'
def pid(kind, a):
    if kind == 'two':
        A0, al, be, m = a; mu = [al//2]*2 + [be//2]*m
    else:
        A0, wa, wb, wq = a[:4]; k = a[4] if len(a) > 4 else 2; mu = [wa//2, wb//2] + [wq//2]*k
    return '%d_%s' % (A0, '_'.join(map(str, sorted(mu, reverse=True))))
def fz(P):
    return fmpz_poly([int(c) for c in s.Poly(P, x).all_coeffs()[::-1]])
for i in [int(a) for a in sys.argv[1:]]:
    kind, args = C23[i]; t0 = time.time()
    F, G = (three if kind == 'three' else two)(23, *args)
    R = fz(s.resultant(F.as_expr(), G.as_expr(), p))
    c = json.load(open(C + pid(kind, args) + '.json'))
    E = fmpz_poly([int(t) for t in c['Lambda']['coefficients_low_to_high']])
    q, r = divmod(R, E)
    out = [i, kind, args, pid(kind, args), 'deg R', R.degree(), 'deg ext', E.degree(), 'divides', r == 0]
    if r == 0:
        T = fmpz_poly([-23, args[0]]); X = fmpz_poly([0, 1]); a = b = 0
        while q.degree() > 0 and divmod(q, X)[1] == 0: q = divmod(q, X)[0]; a += 1
        while q.degree() > 0 and divmod(q, T)[1] == 0: q = divmod(q, T)[0]; b += 1
        q2, r2 = divmod(q, E)
        out += ['x^%d T^%d' % (a, b), 'rest deg', q.degree(), 'rest = c Lambda:', q.degree() == E.degree() and r2 == 0 and q2.degree() == 0]
        if q.degree() > 0:
            from flint import fmpz_poly as FP
            sh = q(fmpz_poly([25, 1])); co = [int(t) for t in sh.coeffs()]
            out += ['rest one-signed at x - 25:', all(t > 0 for t in co) or all(t < 0 for t in co)]
    print(*out, '%.0f s' % (time.time() - t0), flush=True)
