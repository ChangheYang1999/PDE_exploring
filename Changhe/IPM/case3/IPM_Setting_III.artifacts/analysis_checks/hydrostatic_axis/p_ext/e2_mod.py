import sympy as sp, itertools
exec(open('e2_integer.py').read().split("num,den")[0])
num,den=sp.fraction(sp.together(sp.simplify(pp)))
P=sp.Poly(sp.expand(num),n,nu,mu); terms=[(int(c),e) for e,c in zip(P.monoms(),P.coeffs())]
def ev(q,a,b,c): return sum(co*pow(a,e[0],q)*pow(b,e[1],q)*pow(c,e[2],q) for co,e in terms)%q
for q in list(range(2,40))+[64,81,125,128,243,256]:
    if q>60:
        # only check zero existence quickly
        pass
    zs=sum(1 for a,b,c in itertools.product(range(q),repeat=3) if ev(q,a,b,c)==0) if q<=40 else None
    if q<=40: print(q,zs,end='; ')
print()
