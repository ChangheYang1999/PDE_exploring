"""Exact quotient basis (theory_v03 R9(b), N4-158/N4-175/N4-178): remove the exact zero-potential directions of a generator list.
The canonical term expansion (ipm_exact.generators_to_terms) of a non-legqs generator is a vector over keys (m, k, p); generators of different blocks
(m, p) have disjoint keys, so the redundancy is block-diagonal.  For each block the exact rank and a set of pivot generators (leftmost independent
columns, exact rational rref via python-flint) are computed; the candidate's coefficients are re-expressed exactly on the pivot generators (same
potential, hence identical sector table and residual).  legqs generators (series terms) are kept unchanged.  Writes a new exact JSON and verifies
that the merged canonical terms of the old and the new list coincide exactly.  argv: exact_json out_json"""
import sys, os, json, hashlib, time
sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/lib')
import ipm_exact as X, ipm_opt as OPT
import flint
from gmpy2 import mpq
path, outp = sys.argv[1], sys.argv[2]
c, gens, coefs, J = OPT.load_candidate_json(path)
t0 = time.time()
blocks = {}
for i, g in enumerate(gens):
    if g['spec'][0] == 'legqs': continue
    p = X.Q(g['p']) if 'p' in g else X.p_branch(c, int(g['j']))
    blocks.setdefault((int(g['m']), p), []).append(i)
def fq(v): return flint.fmpq(int(v.numerator), int(v.denominator))
def gq(v): return mpq(int(v.p), int(v.q))
keep = set(i for i, g in enumerate(gens) if g['spec'][0] == 'legqs'); newcoef = {i: coefs[i] for i in keep}
nred = 0
for (m, p), idx in blocks.items():
    idx = sorted(idx, key=lambda i: (0 if gens[i]['spec'][0] in ('leg', 'legq') else 1, i))   # Legendre generators preferred as pivots (as N4-175)
    cols = []
    for i in idx:
        T = X.generators_to_terms(c, [dict(gens[i], coef=mpq(1))]); cols.append({(t['m'], t['k'], t['p']): t['coef'] for t in T})
    keys = sorted({k for col in cols for k in col})
    M = flint.fmpq_mat(len(keys), len(idx))
    for jcol, col in enumerate(cols):
        for k, v in col.items(): M[keys.index(k), jcol] = fq(v)
    R, rank = M.rref()
    piv = []
    for r in range(rank):
        for jcol in range(len(idx)):
            if R[r, jcol] != 0: piv.append(jcol); break
    assert len(piv) == rank
    # exact re-expression: M[:, piv] a' = M a  (solve on the pivot rows of the rref system: use least squares free exact solve via rref of augmented matrix)
    rhs = flint.fmpq_mat(len(keys), 1)
    for jcol, col in enumerate(cols):
        cj = coefs[idx[jcol]]
        if cj == 0: continue
        for k, v in col.items(): rhs[keys.index(k), 0] += fq(v*cj)
    Aug = flint.fmpq_mat(len(keys), rank+1)
    for r in range(len(keys)):
        for jj, jcol in enumerate(piv): Aug[r, jj] = M[r, jcol]
        Aug[r, rank] = rhs[r, 0]
    RA, rA = Aug.rref()
    assert rA == rank, f'inconsistent re-expression in block m={m}: rank {rA} vs {rank}'
    sol = [gq(RA[r, rank]) for r in range(rank)]      # since the pivot columns are independent, rref gives the identity on them
    for jj, jcol in enumerate(piv):
        assert RA[jj, jj] == 1
        keep.add(idx[jcol]); newcoef[idx[jcol]] = sol[jj]
    nred += len(idx)-rank
kept = sorted(keep)
print(f'generators {len(gens)} -> kept {len(kept)} (removed {nred} exact zero-potential directions) in {time.time()-t0:.1f} s', flush=True)
# verification: merged canonical terms identical
T_old = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs)])
T_new = X.generators_to_terms(c, [dict(gens[i], coef=newcoef[i]) for i in kept])
def canon(T): return sorted(((t['m'], t['k'], t['p'], t['coef']) for t in T if t.get('kind') != 'series'))
assert canon(T_old) == canon(T_new), 'canonical terms differ'
print('exact check passed: identical canonical monomial terms (%d)' % len(canon(T_new)), flush=True)
out = dict(J); out['generators'] = []
for i in kept:
    g = gens[i]; d = {'m': int(g['m']), 'spec': list(g['spec']), 'coef': X.qstr(newcoef[i]), 'coef_float': X.qfloat(newcoef[i])}
    if 'j' in g: d['j'] = int(g['j'])
    else: d['p'] = g['p']
    out['generators'].append(d)
out['n_free'] = len(kept); out['n_fixed'] = 0
out['meta'] = dict(J.get('meta', {}), quotient_of=os.path.basename(path), quotient_of_sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(), removed_zero_potential_directions=nred, kept_indices=kept)
json.dump(out, open(outp, 'w'))
print('written', outp, hashlib.sha256(open(outp, 'rb').read()).hexdigest())
