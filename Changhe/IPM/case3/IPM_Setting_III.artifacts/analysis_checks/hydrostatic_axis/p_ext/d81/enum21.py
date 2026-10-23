# Enumeration of the patterns (A_0; mu_1, ...) with e >= 2 and the filters of A.3.80 (lead; own check of the counts
# 0, 1, 3, 7, 14, 25, 42, 67 for d <= 19 and of the external count 103 / 29 for d = 21).
from collections import Counter
def parts(n, k, mx):
    # partitions of n into exactly k positive parts, nonincreasing, each <= mx
    if k == 0:
        if n == 0: yield ()
        return
    for p in range(min(n - (k - 1), mx), 0, -1):
        for r in parts(n - p, k - 1, p): yield (p,) + r
def pats(d):
    for A0 in range(1, d + 1, 2):
        s = (d - A0)//2
        for k in range(3, s + 1):
            for mu in parts(s, k, s): yield (A0, mu)
def excluded(A0, mu):
    c = Counter(mu)
    if len(c) == 1: return 'equal'
    if len(c) == 2:
        (v1, n1), (v2, n2) = sorted(c.items(), key=lambda t: t[1])
        if n1 == 1:
            b, a1 = 2*v2, 2*v1
            if a1 > b: return 'one larger'
            if A0 >= 3 or b - a1 == 2: return 'one smaller'
            if n2 == 1: pass
    if sum(1 for v, m in c.items() if m % 2) >= 3: return 'three odd'
    if len(mu) == 4 and len(c) == 2 and all(m == 2 for m in c.values()) and min(c) == 1: return 'two pairs with 2'
    return None
for d in range(5, 23, 2):
    P = list(pats(d)); R = [p for p in P if excluded(*p) is None]
    print(d, len(P), len(R))
    if d >= 15: print('   ', ['(%d; %s)' % (A0, ', '.join(map(str, mu))) for A0, mu in R])
