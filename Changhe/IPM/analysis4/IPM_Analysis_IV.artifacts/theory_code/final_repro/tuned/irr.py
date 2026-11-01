import sympy as sp
b=sp.symbols('b')
O6num=176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936
print(sp.factor_list(O6num))
print('content', sp.Poly(O6num,b).content())
pp=sp.Poly(O6num,b)
print('irreducible over Q:', pp.is_irreducible)
print('discriminant sign', sp.sign(sp.discriminant(O6num,b)))
for r in sp.Poly(O6num,b).intervals():
    print(r)
