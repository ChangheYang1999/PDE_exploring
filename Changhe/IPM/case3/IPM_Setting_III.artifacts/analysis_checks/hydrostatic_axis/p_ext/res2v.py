# three weight classes: a real singleton a (weight wa) and two classes with real monic polynomials U (k nodes, weight wu)
# and V (l nodes, weight wv) (lead, 2026-10-21; draft tool). (C2), (C3) give U'/U(z) = L_U(a), V'/V(z) = L_V(a)
# (linear system); these fix the constant terms of U, V; M_1.. fix further coefficients linearly; the remaining four
# equations are in (a, s_1); double resultant (first in s_1, then in a) must vanish at the actual n.
import sys, sympy as sp
n,X,a,LU,LV=sp.symbols('n X a LU LV')
A0,wa,wu,k,wv,l=[int(x) for x in sys.argv[1].split(',')]
e=k+l; m=A0+wa+k*wu+l*wv; D=2*n+m; r=D/(D-1); T=A0*D-m
s=sp.symbols('s1:%d'%(k+1)); t=sp.symbols('t1:%d'%(l+1))
def poly(el,deg): return sum((-1)**i*(el[i-1] if i else 1)*X**(deg-i) for i in range(deg+1))
def psums(el,deg,N):
    E=lambda i: (el[i-1] if 1<=i<=deg else 0)
    P=[deg]
    for j in range(1,N+1): P.append(sum((-1)**(i-1)*E(i)*P[j-i] for i in range(1,j))+(-1)**(j-1)*j*E(j))
    return P
U=poly(s,k); V=poly(t,l); PU=psums(s,k,e+1); PV=psums(t,l,e+1)
M=[A0+wa*a**j+wu*PU[j]+wv*PV[j] for j in range(e+2)]
Ls=sp.solve([sp.Eq(1/(r-a)+LU+LV,0),sp.Eq(wa/(r-a)+wu*LU+wv*LV,-T/r)],[LU,LV])
sol={}
def S(x): return sp.together(sp.sympify(x).subs(sol))
sol[s[k-1]]=sp.solve(sp.diff(U,X).subs(X,r)-Ls[LU]*U.subs(X,r),s[k-1])[0]
sol[t[l-1]]=sp.solve(S(sp.diff(V,X).subs(X,r)-Ls[LV]*V.subs(X,r)),t[l-1])[0]
rest=[]
for j in range(1,e+1):
    eq=S(M[j])
    if j<l and t[j-1] not in sol: v=t[j-1]
    elif 2<=j<k and s[j-1] not in sol: v=s[j-1]
    else: rest.append(eq); continue
    sv=sp.solve(eq,v); assert len(sv)==1; sol[v]=sv[0]
    for kk in list(sol): sol[kk]=sp.together(sol[kk].subs(v,sv[0]))
rest.append(S(M[e+1]*r-(-1)**e*m*a*s[k-1]*t[l-1]))
rest=[sp.factor(sp.numer(sp.cancel(sp.together(S(x))))) for x in rest]
print('pattern A0=%d, a weight %d, %d of weight %d, %d of weight %d; e=%d m=%d; remaining %d'%(A0,wa,k,wu,l,wv,e,m,len(rest)),flush=True)
for x in rest: print(' degs s1,a', sp.Poly(x,s[0]).degree(), sp.Poly(x,a).degree(), flush=True)
R1=sp.Poly(sp.resultant(rest[0],rest[1],s[0]),a); print('R1 deg_a',R1.degree(),flush=True)
R2=sp.Poly(sp.resultant(rest[0],rest[2],s[0]),a); print('R2 deg_a',R2.degree(),flush=True)
g=sp.gcd(R1.as_expr(),R2.as_expr()); print('gcd deg_a',sp.Poly(g,a).degree(),flush=True)
R=sp.factor(sp.resultant(R1.as_expr(),R2.as_expr(),a))
if R==0: print('RR identically 0')
else:
    out=[]
    for f,kk in sp.factor_list(R)[1]:
        if sp.Poly(f,n).degree()==0: continue
        rts=sp.real_roots(sp.Poly(f,n)); out.append((sp.Poly(f,n).degree(),[round(float(x),4) for x in rts]))
    print('RR factors (deg, real roots):',out,flush=True)
