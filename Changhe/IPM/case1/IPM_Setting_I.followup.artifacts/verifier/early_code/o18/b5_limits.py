# (o18)(a): limits of the closed form (21) at A -> 1+ and A -> 2 (both sides), against the exact values derived by hand:
# A -> 1+: B(a, q) -> -1/60, B_5 -> -(43/300)(7/6)^7, natural units -2107/10800; A -> 2: B(a, q) -> -1/20, B_5 -> -11/1474560.
import mpmath as mp
mp.mp.dps = 50
def closed(A):
    L = mp.sqrt(6*A*(4*A - 3)/(8*A - 1))
    P = 1248*A**4 - 548*A**3 + 297*A**2 - 178*A + 84
    B = mp.beta(-4 - 2/A, 4/A)
    return P*B/(15*A*(2*A - 1)*(3*A - 2)*(4*A - 3)*(8*A - 1)*L**(10 + 4/A)), B, L
for e in ['1e-10', '1e-20']:
    A = 1 + mp.mpf(e); b5, B, L = closed(A)
    print('A = 1 + %s: B = %s, B_5 = %s (target %s), natural %s (target %s)' % (e, mp.nstr(B, 15), mp.nstr(b5, 15),
          mp.nstr(-mp.mpf(43)/300*(mp.mpf(7)/6)**7, 15), mp.nstr(b5*L**(10 + 4/A - 4), 15), mp.nstr(-mp.mpf(2107)/10800, 15)))
for e in ['-1e-20', '1e-20']:
    A = 2 + mp.mpf(e); b5, B, L = closed(A)
    print('A = 2 + (%s): B = %s, B_5 = %s, -11/1474560 = %s' % (e, mp.nstr(B, 15), mp.nstr(b5, 20), mp.nstr(-mp.mpf(11)/1474560, 20)))
