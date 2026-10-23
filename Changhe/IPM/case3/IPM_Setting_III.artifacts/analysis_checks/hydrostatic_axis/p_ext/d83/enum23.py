# Survivors for d = 23, 25 and their class structures (sizes of the value classes), with the d <= 21 type assignment.
import sys; sys.path.insert(0, '../d81')
from collections import Counter, defaultdict
import importlib.util
spec = importlib.util.spec_from_file_location('e21', '../d81/enum21.py')
src = open('../d81/enum21.py').read().split('for d in range(5, 23, 2):')[0]
exec(src)
known = {(2, 'e-1'): 'I', (1, 1, 'e-1'): 'II', (3, 3): 'III', (1, 2, 2): 'IV', (3, 4): 'V', (1, 2, 3): 'VI'}
def struct(mu):
    c = Counter(mu); return tuple(sorted(c.values()))
def typ(mu):
    s = struct(mu); e = len(mu) - 1
    if len(s) == 2 and 2 in s and sorted(s) == sorted((2, e - 1)): return 'I'
    if len(s) == 3 and s.count(1) >= 2 and sorted(s) == sorted((1, 1, e - 1)): return 'II'
    return {(3, 3): 'III', (1, 2, 2): 'IV', (3, 4): 'V', (1, 2, 3): 'VI'}.get(s, 'NEW' + str(s))
for d in (21, 23, 25):
    P = list(pats(d)); R = [p for p in P if excluded(*p) is None]
    print(d, len(P), len(R))
    by = defaultdict(list)
    for A0, mu in R: by[typ(mu)].append('(%d; %s)' % (A0, ', '.join(map(str, mu))))
    for k in sorted(by): print('  ', k, len(by[k]), ' '.join(by[k]))
