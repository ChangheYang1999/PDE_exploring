# three weight classes, any e (lead, 2026-10-21): A_0 at v = 1, real singletons a (weight wa) and b (weight wb), and l nodes
# of weight wq (monic real polynomial V, elementary symmetric t_1..t_l); e + 1 = l + 2, m = A_0 + wa + wb + l wq.
# Necessary conditions: (A8) minus wq (X): (wa - wq)/(z - a) + (wb - wq)/(z - b) = -T/z (solved for b); M_1..M_l give
# t_1..t_l; then M_{l+1}, ..., M_e, (X) and (A7) are polynomials in a; resultants in a must vanish at the actual n.
import sys, sympy as sp
n,X,a,b=sp.symbols('n X a b')
A0,wa,wb,wq,l=[int(x) for x in sys.argv[1].split(',')]
e=l+1; m=A0+wa+wb+l*wq; D=2*n+m; r=D/(D-1); T=A0*D-m
t=sp.symbols('t1:%d'%(l+1))
def psums(el,deg,N):
    E=lambda i: (el[i-1] if 1<=i<=deg else 0)
    P=[deg]
    for j in range(1,N+1):
        P.append(sum((-1)**(i-1)*E(i)*P[j-i] for i in range(1,j))+(-1)**(j-1)*j*E(j))
    return P
V=sum((-1)**i*(t[i-1] if i else 1)*X**(l-i) for i in range(l+1)); PV=psums(t,l,e+1)
M=[A0+wa*a**j+wb*b**j+wq*PV[j] for j in range(e+2)]
sol={b:sp.solve(sp.Eq((wa-wq)/(r-a)+(wb-wq)/(r-b),-T/r),b)[0]}
def S(x): return sp.together(sp.sympify(x).subs(sol))
for j in range(1,l+1):
    sv=sp.solve(S(M[j]),t[j-1]); assert len(sv)==1; sol[t[j-1]]=sv[0]
    for kk in list(sol): sol[kk]=sp.together(sol[kk].subs(t[j-1],sv[0]))
rest=[S(M[j]) for j in range(l+1,e+1)]
rest.append(S(1/(r-a)+1/(r-b)+sp.diff(V,X).subs(X,r)/V.subs(X,r)))
rest.append(S(M[e+1]*r-(-1)**e*m*a*b*t[l-1]))
print('pattern A0=%d weights a %d, b %d, %d nodes of weight %d; e=%d m=%d; remaining %d'%(A0,wa,wb,l,wq,e,m,len(rest)),flush=True)
assert len(rest)==3
polys=[sp.Poly(sp.factor(sp.numer(sp.cancel(sp.together(x)))),a) for x in rest]
for P_ in polys: print('deg_a',P_.degree(),P_.free_symbols,flush=True)
for (i1,i2) in [(0,1),(0,2)]:
    R=sp.factor(sp.resultant(polys[i1].as_expr(),polys[i2].as_expr(),a))
    if R==0: print('Res%d%d identically 0'%(i1,i2)); continue
    out=[]
    for f,kk in sp.factor_list(R)[1]:
        if sp.Poly(f,n).degree()==0: continue
        rts=sp.real_roots(sp.Poly(f,n))
        out.append((sp.Poly(f,n).degree(),[round(float(x),4) for x in rts],[x for x in rts if x.is_integer and x>=1]))
    print('Res%d%d factors (deg, real roots, integer roots >= 1):'%(i1,i2),out,flush=True)
