# e = 3, nodes: real singletons a (weight wa), b (weight wb) and a real-coefficient quadratic V = X^2 - hX + j whose two
# nodes have weight wq; m = A0 + wa + wb + 2 wq (lead, 2026-10-21). Necessary conditions only: (X) and g(u_*) = 0 give
# (wa - wq)/(r - a) + (wb - wq)/(r - b) = -T/r (solved for b); M_1, M_2 give h, j; then M_3 = 0, (X) and (A7) are
# polynomials in a over Q[n]; their resultants in a must vanish at the actual n.
import sys, sympy as sp
n,X,a,b,h,j=sp.symbols('n X a b h j')
A0,wa,wb,wq=[int(x) for x in sys.argv[1].split(',')]
m=A0+wa+wb+2*wq; D=2*n+m; r=D/(D-1); T=A0*D-m
def num(e): return sp.numer(sp.together(sp.simplify(e)))
bs=sp.solve(sp.Eq((wa-wq)/(r-a)+(wb-wq)/(r-b),-T/r),b)[0]
hs=sp.solve(A0+wa*a+wb*b+wq*h,h)[0]
js=sp.solve(A0+wa*a**2+wb*b**2+wq*(h**2-2*j),j)[0].subs(h,hs)
p3=h**3-3*h*j; p4=h**4-4*h**2*j+2*j**2
sub=lambda e_: e_.subs(j,js).subs(h,hs).subs(b,bs)
E3=num(sub(A0+wa*a**3+wb*b**3+wq*p3))
V=X**2-h*X+j
EX=num(sub(1/(r-a)+1/(r-b)+sp.diff(V,X).subs(X,r)/V.subs(X,r)))
E7=num(sub((A0+wa*a**4+wb*b**4+wq*p4)*r+m*a*b*j))
print('pattern A0=%d weights a %d, b %d, pair %d, m=%d'%(A0,wa,wb,wq,m),flush=True)
polys=[sp.Poly(sp.factor(q),a) for q in (E3,EX,E7)]
for P_ in polys: print('deg_a',P_.degree(),flush=True)
for (i1,i2) in [(0,1),(0,2)]:
    R=sp.factor(sp.resultant(polys[i1].as_expr(),polys[i2].as_expr(),a))
    if R==0: print('Res%d%d identically 0'%(i1,i2)); continue
    out=[]
    for f,k in sp.factor_list(R)[1]:
        if sp.Poly(f,n).degree()==0: continue
        rts=sp.real_roots(sp.Poly(f,n))
        out.append((sp.Poly(f,n).degree(),[round(float(x),4) for x in rts],[x for x in rts if x.is_integer and x>=1]))
    print('Res%d%d factors (deg, real roots, integer roots >= 1):'%(i1,i2),out,flush=True)
