"""Verifier scratch (shift 9): rows 54, 55, 58, 59 against the candidate X3 (c6g) on the same audit files as
scratch/read5859.py (whole-box N_f A5 and all columns, N_f within 0.5 of P, N_v r <= 1000 A5, N_v r > 1000 A5 at
N11250 q384 and N16875 q512; 857-label J at N16875 q384, eps 0.03 / 0.01). Usage: python3 scratch/cmp_x3.py"""
import sys
sys.argv = ['read5859']
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    exec(open('scratch/read5859.py').read())
X = {c: aud('c6g', c) for c in cfgs}; XJ = jay('c6g')
for c in cfgs:
    a = X[c]; print('X3 %s wbA5 %.4e all %.4e nearP %.4e Nv<=1000 %.4e Nv>1000 %.4e' % (c, a['wbA'], a['wb'], a['nP'], a['nv'], a['far']))
print('X3 J %.4e / %.4e' % XJ)
for tag, k in rows:
    A = {c: aud(tag, c) for c in cfgs}; J = jay(tag)
    s = '%s %s /X3:' % (k, tag)
    for c in cfgs:
        if A[c]: s += ' %s wbA5 %.4f all %.4f nearP %.4f Nv<=1000 %.4f Nv>1000 %.4f;' % (c, A[c]['wbA'] / X[c]['wbA'], A[c]['wb'] / X[c]['wb'], A[c]['nP'] / X[c]['nP'], A[c]['nv'] / X[c]['nv'], A[c]['far'] / X[c]['far'])
        else: s += ' %s missing;' % c
    if J: s += ' J %.4f / %.4f' % (J[0] / XJ[0], J[1] / XJ[1])
    print(s)
