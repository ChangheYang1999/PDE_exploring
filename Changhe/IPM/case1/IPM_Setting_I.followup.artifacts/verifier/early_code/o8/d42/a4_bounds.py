# D42 item 3: symbolic check of the hand bounds for the A = 4, L = 4 rational reference of fred15 03 section 6.
import sympy as sp
x, t, s = sp.symbols('x t s', nonnegative=True)
w0 = -4*x*(1 - (x/4)**2)/(1 + (x/4)**2)
a0 = sp.simplify(-w0/(4 - x))   # tail quotient a_0 = -w_0/(L - x), L = 4
print('a0 =', sp.factor(a0), ' check 4t(1+t)/(1+t^2):', sp.simplify(a0 - (4*t*(1 + t)/(1 + t**2)).subs(t, x/4)))
print('a0 - x =', sp.factor(sp.simplify(a0 - x)))
print("a0' =", sp.factor(sp.diff(a0, x)), ' check:', sp.simplify(sp.diff(a0, x) - ((1 + 2*t - t**2)/(1 + t**2)**2).subs(t, x/4)))
w1 = sp.diff(w0, x); w2 = sp.diff(w0, x, 2); w3 = sp.diff(w0, x, 3)
print("w0' check:", sp.simplify(w1 - (-4*(256 - 64*x**2 - x**4)/(16 + x**2)**2)),
      ' bracket check:', sp.simplify((256 - 64*s - s**2)/(16 + s)**2 - ((512 - 32*s)/(16 + s)**2 - 1)))
print("d/ds (512-32s)/(16+s)^2 =", sp.factor(sp.diff((512 - 32*s)/(16 + s)**2, s)))
print("w0'' check:", sp.simplify(w2 - 256*x*(48 - x**2)/(16 + x**2)**3))
print("w0''' check:", sp.simplify(w3 - (256*(48 - 3*x**2)/(16 + x**2)**3 - 1536*x**2*(48 - x**2)/(16 + x**2)**4)))
print('series:', sp.series(w0, x, 0, 10))
R = sp.simplify(w0 - (-4*x + x**3/2 - x**5/32 + x**7/512))
print('R + x^9/(8192(1+x^2/16)) =', sp.simplify(R + x**9/(8192*(1 + x**2/16))))
import mpmath as mp
xs = [mp.mpf(4)*i/40000 for i in range(40001)]
f = {k: sp.lambdify(x, e, 'mpmath') for k, e in [('w0', w0), ('w1', w1), ('w2', w2), ('w3', w3), ('a0', a0), ('a1', sp.diff(a0, x))]}
for k in f:
    print(k, 'sampled sup on [0,4]:', mp.nstr(max(abs(f[k](u)) for u in xs[1:]), 8))
print('(15/4)^(1/4) =', mp.nstr(mp.mpf(15)/4**mp.mpf(0.25), 8) if False else mp.nstr((mp.mpf(15)/4)**mp.mpf(0.25), 8))
h = 1/(1 + x**2/16)
for i in range(3):
    e = sp.diff(-x**9*h/8192, x, i)*x**(i - 8)
    g = sp.lambdify(x, e, 'mpmath')
    print('weighted remainder i=%d sup on (0,1/4]:' % i, mp.nstr(max(abs(g(mp.mpf(1)/4*j/2000)) for j in range(1, 2001)), 6))
print('h\'\' on (0,1/4] max:', mp.nstr(max(abs(sp.lambdify(x, sp.diff(h, x, 2), 'mpmath')(mp.mpf(1)/4*j/2000)) for j in range(0, 2001)), 6))
q = sp.Rational(1, 256)
print('jet sum', float(4 + sp.Rational(1, 2) + sp.Rational(1, 32) + sp.Rational(1, 512)),
      ' 2q+2q^2+2q^3 =', float(2*q + 2*q**2 + 2*q**3), ' 4q/(1-q)^2 =', float(4*q/(1 - q)**2), ' (3+q)/(4(1-q)^3) =', float((3 + q)/(4*(1 - q)**3)))
y = sp.symbols('y')
print('z0-1 identity:', sp.simplify(-2*y/(1 + y) - (-2*y + 2*y**2 - 2*y**3/(1 + y))))
c = (mp.mpf(15)/4)**mp.mpf(0.25)
print('Hoelder: a0 <=', mp.nstr(8 + 3*c, 6), ' w0pp <=', mp.nstr(12 + 21*c, 6), ' tail <=', mp.nstr((16 + 12*c) + (12 + 12*c) + 12 + 21*c, 6))
