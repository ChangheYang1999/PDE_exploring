# two weight classes, any e (lead, 2026-10-21): A_0 at v = 1, k nodes of weight al (monic real polynomial U with
# elementary symmetric functions s_1..s_k), l nodes of weight be (V, t_1..t_l), e + 1 = k + l, m = A_0 + k al + l be.
# Necessary conditions: (X) and (A8) <=> (al - be) z U'(z) + T U(z) = 0 and (al - be) z V'(z) - T V(z) = 0 (T = A_0 D - m);
# M_1..M_e = 0; (A7) M_{e+1} z = (-1)^e m prod v_j. Solve linearly for all unknowns except s_1, then take resultants in
# s_1 of the three remaining equations (they must vanish at the actual n; Sylvester null-vector argument).
import sys, sympy as sp
n,X=sp.symbols('n X')
A0,al,k,be,l=[int(x) for x in sys.argv[1].split(',')]
e=k+l-1; m=A0+k*al+l*be; D=2*n+m; r=D/(D-1); T=A0*D-m
s=sp.symbols('s1:%d'%(k+1)); t=sp.symbols('t1:%d'%(l+1))
def poly(el,deg): return sum((-1)**i*(el[i-1] if i else 1)*X**(deg-i) for i in range(deg+1))
def psums(el,deg,N):
    E=lambda i: (el[i-1] if 1<=i<=deg else 0)
    P=[deg]
    for j in range(1,N+1):
        P.append(sum((-1)**(i-1)*E(i)*P[j-i] for i in range(1,j))+(-1)**(j-1)*j*E(j))
    return P
U=poly(s,k); V=poly(t,l); PU=psums(s,k,e+1); PV=psums(t,l,e+1)
M=[A0+al*PU[j]+be*PV[j] for j in range(e+2)]
assert sp.expand(M[0]-m)==0
L1=(al-be)*r*sp.diff(U,X).subs(X,r)+T*U.subs(X,r)
L2=(al-be)*r*sp.diff(V,X).subs(X,r)-T*V.subs(X,r)
prod=s[k-1]*t[l-1]
A7=M[e+1]*r-(-1)**e*m*prod
sol={}
def S(x): return sp.together(sp.sympify(x).subs(sol))
sol[s[k-1]]=sp.solve(L1,s[k-1])[0]
sol[t[l-1]]=sp.solve(S(L2),t[l-1])[0]
rest=[]
for j in range(1,e+1):
    eq=S(M[j])
    if j<l and t[j-1] not in sol: v=t[j-1]
    elif 2<=j<k and s[j-1] not in sol: v=s[j-1]
    else: rest.append(eq); continue
    sv=sp.solve(eq,v); assert len(sv)==1,(j,v,sv); sol[v]=sv[0]
    for kk in list(sol): sol[kk]=sp.together(sol[kk].subs(v,sv[0]))
rest.append(S(A7))
rest=[sp.together(S(x)) for x in rest]
print('pattern A0=%d, %d nodes of weight %d, %d of weight %d; e=%d m=%d; free s1; remaining %d'%(A0,k,al,l,be,e,m,len(rest)),flush=True)
assert len(rest)==3
polys=[sp.Poly(sp.factor(sp.numer(x)),s[0]) for x in rest]
for P_ in polys: print('deg_s1',P_.degree(),'free symbols',P_.free_symbols,flush=True)
for (i1,i2) in [(0,1),(0,2)]:
    R=sp.factor(sp.resultant(polys[i1].as_expr(),polys[i2].as_expr(),s[0]))
    if R==0: print('Res%d%d identically 0'%(i1,i2)); continue
    out=[]
    for f,kk in sp.factor_list(R)[1]:
        if sp.Poly(f,n).degree()==0: continue
        rts=sp.real_roots(sp.Poly(f,n))
        out.append((sp.Poly(f,n).degree(),[round(float(x),4) for x in rts],[x for x in rts if x.is_integer and x>=1]))
    print('Res%d%d factors (deg, real roots, integer roots >= 1):'%(i1,i2),out,flush=True)
