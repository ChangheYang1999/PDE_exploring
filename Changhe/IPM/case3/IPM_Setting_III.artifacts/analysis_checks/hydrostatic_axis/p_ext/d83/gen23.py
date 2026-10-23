# d = 23, types (I) and (II): the functions two() and three() and cert() of ../d81/gen21.py (lead, 2026-10-21T20:4xZ)
import sys, time
src = open('../d81/gen21.py').read().split('CASES = ')[0]
exec(src)
C23 = [('two', (1, 8, 2, 3)), ('two', (1, 2, 6, 3)), ('two', (5, 6, 2, 3)), ('two', (7, 2, 4, 3)), ('two', (9, 4, 2, 3)),
       ('two', (3, 6, 2, 4)), ('two', (3, 2, 4, 4)), ('two', (7, 4, 2, 4)),
       ('three', (1, 14, 4, 2)), ('three', (1, 12, 6, 2)), ('three', (1, 12, 2, 4)), ('three', (1, 10, 8, 2)),
       ('three', (1, 4, 2, 8)), ('three', (1, 8, 2, 6)), ('three', (1, 8, 6, 4)), ('three', (3, 12, 4, 2)),
       ('three', (3, 10, 6, 2)), ('three', (3, 10, 2, 4)), ('three', (5, 10, 4, 2)), ('three', (5, 8, 6, 2)),
       ('three', (5, 8, 2, 4)), ('three', (5, 4, 2, 6)), ('three', (7, 8, 4, 2)), ('three', (7, 6, 2, 4)),
       ('three', (9, 6, 4, 2)),
       ('two', (1, 6, 2, 5)), ('two', (5, 4, 2, 5)), ('two', (3, 4, 2, 6)), ('two', (1, 4, 2, 7)),
       ('three', (1, 10, 4, 2, 4)), ('three', (1, 8, 6, 2, 4)), ('three', (3, 8, 4, 2, 4)), ('three', (5, 6, 4, 2, 4)),
       ('three', (1, 6, 4, 2, 6))]
assert len(C23) == 34
sel = sys.argv[1:] and [int(a) for a in sys.argv[1:]] or range(len(C23))
for i in sel:
    kind, args = C23[i]
    t0 = time.time()
    F, G = (three if kind == 'three' else two)(23, *args)
    print(23, i, kind, args, 'degF_p', F.degree(p), 'degG_p', G.degree(p), cert(F, G, 23), '%.0f s' % (time.time() - t0), flush=True)
