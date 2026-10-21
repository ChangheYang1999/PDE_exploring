# sampled N-norms (02 (12), monomial convention) of phi_j = u^j + (j-11)/2 u^9 + (9-j)/2 u^11, against the referee's
# Bernstein upper bounds 1111.75, 633.5, 259.25 (03 section 4) and the resulting lower bound (36) of the dual norm
import sys
sys.argv = ['x']
import mpmath as mp
exec(open('ndist_ver.py').read().split("pairs = [")[0])
DB = {3: mp.mpf('0.82913517178296'), 5: mp.mpf('0.48431395933596'), 7: mp.mpf('0.21490833993007')}
ref = {3: 1111.75, 5: 633.5, 7: 259.25}
for j in (3, 5, 7):
    c = [mp.mpf(0)] * 12
    c[j] = 1; c[9] = mp.mpf(j - 11) / 2; c[11] = mp.mpf(9 - j) / 2
    tot, parts = ndist(c, 'mono')
    print('phi_%d: ||.||_N sampled %s (referee upper bound %s) %s; DB/norm %s, DB/bound %s' % (j, mp.nstr(tot, 8), ref[j], parts,
          mp.nstr(DB[j] / tot, 5), mp.nstr(DB[j] / ref[j], 5)))
