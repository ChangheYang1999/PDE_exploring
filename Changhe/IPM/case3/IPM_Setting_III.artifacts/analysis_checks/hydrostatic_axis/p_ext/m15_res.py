# m = 15, A_0 = 1: the two patterns left by scan_sym (TIMEOUT): e = 3 (3,2,1,1) and e = 4 (2,2,1,1,1).
# Method of the external answer for e = 3, m = 13: (X) and g(u_*) = 0 give the log-derivatives of the weight classes at r
# (linear relations), the first moments are linear; the rest by resultants in the remaining unknowns (necessary
# conditions only; no division by a non-constant factor that could vanish on a solution, apart from n, r, r - 1, r - v_k,
# which are nonzero on any configuration).
import sys, sympy as sp
n,X=sp.symbols('n X')
D=2*n+15; r=D/(D-1); m=15
def psums(coeffs,L):
    # monic poly X^k - c1 X^{k-1} + c2 X^{k-2} - ... ; coeffs = [c1..ck]; Newton
    k=len(coeffs); p=[None]
    for l in range(1,L+1):
        v=sum((-1)**(i-1)*coeffs[i-1]*p[l-i] for i in range(1,min(l-1,k)+1))
        if l<=k: v+=(-1)**(l-1)*l*coeffs[l-1]
        p.append(sp.expand(v))
    return p
def num(e): return sp.numer(sp.together(sp.simplify(e)))
which=sys.argv[1]
if which=='A':
    a,b,h,j=sp.symbols('a b h j')
    # 2/(r-a) + 1/(r-b) = -n/r  (from (X) and g(u_*) = 0)
    bs=sp.solve(sp.Eq(2/(r-a)+1/(r-b),-n/r),b)[0]
    hs=sp.solve(1+6*a+4*b+2*h,h)[0]
    js=sp.solve(1+6*a**2+4*b**2+2*(h**2-2*j),j)[0].subs(h,hs)
    pV=psums([h,j],4)
    def M(l): return 1+6*a**l+4*b**l+2*pV[l]
    sub=lambda e_: e_.subs(j,js).subs(h,hs).subs(b,bs)
    E3=num(sub(M(3)))
    V=X**2-h*X+j
    EX=num(sub(1/(r-a)+1/(r-b)+sp.diff(V,X).subs(X,r)/V.subs(X,r)))
    E7=num(sub(M(4)*r+15*a*b*j))
    polys=[sp.Poly(sp.factor(q),a) for q in (E3,EX,E7)]
else:
    p,q,s1,s2,s3=sp.symbols('p q s1 s2 s3')
    qs=((n+1)*p*r-(n+2)*r**2)/n
    s1s=sp.solve(1+4*p+2*s1,s1)[0]
    pU=psums([p,q],5); pW=psums([s1,s2,s3],5)
    def M(l): return 1+4*pU[l]+2*pW[l]
    s2s=sp.solve(M(2).subs(q,qs).subs(s1,s1s),s2)[0]
    W=X**3-s1*X**2+s2*X-s3
    s3s=sp.solve(sp.Eq(r*sp.diff(W,X).subs(X,r),n*W.subs(X,r)),s3)[0]
    sub=lambda e_: e_.subs(s3,s3s).subs(s2,s2s).subs(s1,s1s).subs(q,qs)
    E3=num(sub(M(3))); E4=num(sub(M(4))); E7=num(sub(M(5)*r-15*q*s3))
    a=p; polys=[sp.Poly(sp.factor(x),p) for x in (E3,E4,E7)]
for P_ in polys: print('deg',P_.degree(),'factors',[ (sp.Poly(f,a).degree(),k) for f,k in sp.factor_list(P_.as_expr())[1]],flush=True)
R1=sp.factor(sp.resultant(polys[0].as_expr(),polys[1].as_expr(),a)); print('Res01',R1,flush=True)
R2=sp.factor(sp.resultant(polys[0].as_expr(),polys[2].as_expr(),a)); print('Res02 factors',[(sp.Poly(f,n).degree(),k) for f,k in sp.factor_list(R2)[1]],flush=True)
G=sp.gcd(sp.Poly(R1,n),sp.Poly(R2,n)); print('gcd',G.as_expr())
for f,k in sp.factor_list(R1)[1]:
    rts=[x for x in sp.real_roots(sp.Poly(f,n))]; print('factor deg',sp.Poly(f,n).degree(),'real roots',[float(x) for x in rts],'integer>=1',[x for x in rts if x.is_integer and x>=1])
