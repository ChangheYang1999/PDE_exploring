"""verifier: the family v_d of fred8 03 (FINAL_REPORT 6.3.1 (g)) near d = 2 (correction to D19 (i4) (a)).
c_- from (8) has sin(pi d) in the denominator, which vanishes at d = 2 as well as at d = 3; the coefficient (13) of G_3
carries the factor (d - 2). Both routes of check_fred8 near d = 2 (X3 parameters)."""
import sys
sys.argv = ['x']
import mpmath as mp
mp.mp.dps = 30
src = open('verifier/early_code/symb/check_fred8.py').read()
start, stop = src.index('def fam('), src.index('for tag, Av, gv in [(\'fred8 rounded\', \'10.1507\', \'29.749\'), (\'X3\', \'10.150725221\', \'29.7494907\')]:\n    C, cm')
exec(src[start:stop])
out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
Av, gv = '10.150725221', '29.7494907'
for dv in ['1.9', '1.99', '1.9999', '2.0001', '2.01', '2.1']:
    C, cm, Cb, K = g3_ode(Av, gv, dv)
    Cp = g3_phys(Av, gv, dv)
    P('d = %s: c_- %s, (d - 2) c_- %s, G_3 ODE %s physical %s rel diff %s' % (dv, mp.nstr(cm, 10), mp.nstr((mp.mpf(dv) - 2) * cm, 10),
      mp.nstr(C, 14), mp.nstr(Cp, 14), mp.nstr(abs(C / Cp - 1), 3)))
P('d = 2 exactly: G_3 physical route %s (finite); c_- has a simple pole (residue above), so U_1(s, 0) = c_- |s|^d fails at d = 2' % mp.nstr(g3_phys(Av, gv, 2), 14))
open('verifier/early_runs/check_vd2.log', 'w').write('\n'.join(out) + '\n')
