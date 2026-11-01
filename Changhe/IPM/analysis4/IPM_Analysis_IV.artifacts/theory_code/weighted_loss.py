"""Realized product-loss ratio rho_n^(sigma) of theory Section 14.14 at delta=2/3, f1=sin(theta).

rho_n^(sigma) = ||S_n||_{!,sigma} / sum_{i+j=n} w_ij ||G_i||_{!,sigma} ||F_j||_{!,sigma},
S_n = (lambda_n - c D) F_n, lambda_n = 2(n-1), c = 3, w_ij = 2j(|P_i|+1) + 2i(|p_j|+1),
||H||_{!,sigma} = sum_q q! sigma^q ||[t^q]H||_l1 (sine amplitudes).
Input: a pickled checkpoint of the canonical log recursion with packed dyadic midpoints (m, e, r).
Only midpoints are used; S_n columns are formed exactly in integers before taking absolute values.
Usage: weighted_loss.py CHECKPOINT OUT.json [sigma ...]
"""
import sys, json, pickle, time
from fractions import Fraction
import mpmath as mp
mp.mp.prec = 96
t0 = time.time()
ck, out = sys.argv[1], sys.argv[2]
sigmas = [int(x) for x in sys.argv[3:]] or [1, 3, 12]
state = pickle.load(open(ck, 'rb'))
assert (state['A'], state['B']) == ('2', '3')
N = max(state['f'])

def ival(rec):
    m, e, r = rec
    return int(m), int(e)

def absnorm(col):
    return mp.fsum(mp.ldexp(abs(mp.mpf(m)), e) for m, e in col)

def colnorms_F(cols):
    return [absnorm([ival(z) for z in col]) for col in cols]

def forcing_norms(cols, n):
    # [t^q] S = 2(n-1) F_q - 3(q+1) F_{q+1}, exact in integers
    res = []
    for q in range(len(cols)):
        a = [ival(z) for z in cols[q]]
        b = [ival(z) for z in cols[q+1]] if q+1 < len(cols) else []
        terms = []
        for j in range(max(len(a), len(b))):
            x = (2*(n-1)*a[j][0], a[j][1]) if j < len(a) else (0, 0)
            y = (3*(q+1)*b[j][0], b[j][1]) if j < len(b) else (0, 0)
            e = min(x[1], y[1])
            v = (x[0] << (x[1]-e)) - (y[0] << (y[1]-e))
            terms.append((v, e))
        res.append(absnorm(terms))
    return res

fac = [mp.factorial(q) for q in range(N+2)]
def fnorm(norms, s):
    return mp.fsum(fac[q]*mp.mpf(s)**q*v for q, v in enumerate(norms))

Fn, Gn, Sn = {}, {}, {}
for n in sorted(state['f']):
    Fn[n] = colnorms_F(state['f'][n])
    Gn[n] = colnorms_F(state['g'][n])
    if n >= 2:
        Sn[n] = forcing_norms(state['f'][n], n)
del state
rows = []
for s in sigmas:
    nf = {n: fnorm(Fn[n], s) for n in Fn}
    ng = {n: fnorm(Gn[n], s) for n in Gn}
    for n in sorted(Sn):
        num = fnorm(Sn[n], s)
        den = mp.fsum((2*(n-i)*(abs(2-mp.mpf(2*i)/3)+1) + 2*i*(abs(1-mp.mpf(2*(n-i))/3)+1))*ng[i]*nf[n-i]
                      for i in range(1, n))
        rows.append(dict(sigma=s, n=n, rho=float(num/den),
                         log10_F=float(mp.log10(nf[n])) if nf[n] > 0 else None,
                         log10_G=float(mp.log10(ng[n])) if ng[n] > 0 else None,
                         G_over_F=float(ng[n]/nf[n]) if nf[n] > 0 else None))
cols = {'F': {n: [float(mp.log10(v)) if v > 0 else None for v in Fn[n]] for n in Fn},
        'G': {n: [float(mp.log10(v)) if v > 0 else None for v in Gn[n]] for n in Gn},
        'S': {n: [float(mp.log10(v)) if v > 0 else None for v in Sn[n]] for n in Sn}}
json.dump(cols, open(out.replace('.json', '_cols.json'), 'w'))
json.dump(dict(checkpoint=ck.split('/')[-1], N=N, sigmas=sigmas, rows=rows,
               elapsed_s=time.time()-t0, note='midpoints only; not certified'), open(out, 'w'))
print('done', N, time.time()-t0)
