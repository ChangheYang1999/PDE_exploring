import sympy as sp, mpmath as mp
A, z = sp.symbols('A z')
P = 1248*A**4 - 548*A**3 + 297*A**2 - 178*A + 84
print('P(1+z) =', sp.expand(P.subs(A, 1+z)))
mp.mp.dps = 30
f = lambda a: (1248*a**4 - 548*a**3 + 297*a**2 - 178*a + 84)*mp.beta(-4-2/a, 4/a)/(15*a*(2*a-1)*(3*a-2)*(4*a-3)*(8*a-1)*mp.sqrt(6*a*(4*a-3)/(8*a-1))**(10+4/a))
for a in ['1.0001', '1.1', '1.3', '1.5', '1.7', '1.9', '1.99', '1.9999', '1.999999']:
    print(a, mp.nstr(f(mp.mpf(a)), 12))
print('-11/1474560 =', mp.nstr(mp.mpf(-11)/1474560, 12))
