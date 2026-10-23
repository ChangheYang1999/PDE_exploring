# Enumerate patterns (A0; mu_1 >= mu_2 >= ...) with e >= 2 and apply the lemmas of the d79 text.
import sys
from collections import Counter
def parts(nn, k, mx=None):
    if mx is None: mx = nn
    if k == 0:
        if nn == 0: yield ()
        return
    for f in range(min(nn - (k - 1), mx), 0, -1):
        for r in parts(nn - f, k - 1, f):
            yield (f,) + r
def classify(A0, mus):
    vals = [2*m for m in mus]; e = len(vals) - 1
    cnt = Counter(vals)
    if len(cnt) == 1: return 'equal'
    rmin = sum(1 for c in cnt.values() if c % 2)
    if rmin >= 3: return 'real-nodes'
    if len(cnt) == 2 and min(cnt.values()) == 1:
        a1 = [v for v, c in cnt.items() if c == 1][0]; b = [v for v, c in cnt.items() if c > 1][0]
        if a1 > b: return 'exc-higher'
        if A0 >= 3 or b - a1 <= 2: return 'exc-lower-excluded'
        return 'EXC-LOWER n<%d/2' % (b - a1)
    if e == 3 and sorted(cnt.values()) == [2, 2]:
        al, be = sorted(cnt)
        if A0 >= 3 or min(al, be) == 2: return 'two-pairs'
        return 'TWO-PAIRS-small'
    return 'OPEN'
for d in map(int, sys.argv[1:]):
    tally = Counter(); opens = []
    for A0 in range(1, d + 1, 2):
        for k in range(3, (d - A0)//2 + 1):
            for mus in parts((d - A0)//2, k):
                c = classify(A0, mus); tally[c.split()[0]] += 1
                if c[0].isupper(): opens.append((A0, mus, c))
    print('d =', d, dict(tally))
    for o in opens: print('   ', o)
