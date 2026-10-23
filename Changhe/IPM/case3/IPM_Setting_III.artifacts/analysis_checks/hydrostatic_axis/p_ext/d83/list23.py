# d = 23 survivors grouped by e (the filters of enum21.py plus: two pairs with A_0 >= 3)
from collections import Counter, defaultdict
src = open('../d81/enum21.py').read().split('for d in range(5, 23, 2):')[0]
exec(src)
def excl2(A0, mu):
    r = excluded(A0, mu)
    if r: return r
    c = Counter(mu)
    if len(mu) == 4 and len(c) == 2 and all(m == 2 for m in c.values()) and A0 >= 3: return 'two pairs A0>=3'
    return None
import sys
d = int(sys.argv[1])
P = list(pats(d)); R = [p for p in P if excl2(*p) is None]
print(d, len(P), len(R), [p for p in P if excl2(*p) == 'two pairs A0>=3'])
by = defaultdict(list)
for A0, mu in R: by[len(mu) - 1].append('(%d; %s)' % (A0, ', '.join(map(str, mu))))
for e in sorted(by): print('e = %d (%d):' % (e, len(by[e])), ' '.join(by[e]))
