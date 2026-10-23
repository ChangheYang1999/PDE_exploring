# the d = 21 pattern (7; 2, 2, 1, 1, 1) of type (I), omitted from the list of gen21.py (lead)
import sys; sys.argv = ['gen21.py']
exec(open('gen21.py').read())
t0 = time.time()
F, G = two(21, 7, 4, 2, 3)
print(21, 'two', (7, 4, 2, 3), 'degF_p', F.degree(p), 'degG_p', G.degree(p), cert(F, G, 21), '%.0f s' % (time.time() - t0), flush=True)
