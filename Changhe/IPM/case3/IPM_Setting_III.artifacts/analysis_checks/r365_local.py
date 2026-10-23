# Lead check of the local exact-transport construction (external analysis projN): own implementation.
# (i) Poisson for the homogeneous inverse (1); (ii) projected matrix of L_n vs (4)-(5), weighted form (8), margins,
# determinant vs recursion (6); (iii) jets of the FULL equation R = 0 solved degree by degree for numeric (c, a, H),
# cubic coefficients vs (24), binomial norms of the jets.
import sympy as s, sys, itertools
x,y,th=s.symbols('x y th',real=True)
c,a,lam=s.symbols('c a lam')
def S(n,p):  # r^n sin(p th) as a polynomial
    return s.expand(s.im(s.expand((x+s.I*y)**p))*(x**2+y**2)**((n-p)//2))
def P(n,p):  # homogeneous inverse (1)
    e=-S(n+1,p+1)/(2*(n+p+2))
    if p>1: e+=-S(n+1,p-1)/(2*(n-p+2))
    return s.expand(e)
lap=lambda e: s.diff(e,x,2)+s.diff(e,y,2)
ok=all(s.expand(-lap(P(n,p))-s.diff(S(n,p),x))==0 for n in range(1,12,2) for p in range(1,n+1,2))
print('(2) Poisson for (1), n <= 11:',ok)
def sinproj(e,n,p):  # coefficient of r^n sin(p th) in homogeneous degree-n e
    return s.simplify(s.integrate(s.expand(s.expand_trig(e.subs({x:s.cos(th),y:s.sin(th)})*s.sin(p*th))),(th,0,2*s.pi))/s.pi)
D=c-1; A=2*c-1
def Ln(n,p):
    h=S(n,p); return s.expand(A*x*s.diff(h,x)+y*s.diff(h,y)-h+a*s.diff(P(n,p),x))
def Amat(j,d):
    n=2*j+1
    M=s.zeros(d,d)
    for col in range(d):
        e=Ln(n,2*col+1)
        for row in range(d): M[row,col]=sinproj(e,n,2*row+1)
    return M
def A5(l,d):
    M=s.zeros(d,d)
    for i in range(d):
        M[i,i]=(c+1)*l/2-a/4 if i==0 else c*l+D-a/2
    for i in range(d-1):
        M[i,i+1]=(l+2*i+4)*(2*D*(l-2*i)-a)/(4*(l-2*i)); M[i+1,i]=(l-2*i)*(2*D*(l+2*i+4)-a)/(4*(l+2*i+4))
    return M
def Prec(l,d):
    Pl=[s.Integer(1),(c+1)*l/2-a/4]
    for k in range(2,d+1):
        Q=((2*D*(l+2)-a)**2-16*D**2*(k-1)**2)/16
        Pl.append(s.expand((c*l+D-a/2)*Pl[k-1]-Q*Pl[k-2]))
    return Pl[d]
for j in range(1,5):
    d=j+1; M=Amat(j,d)
    # full operator: no mode above 2j+1 at degree 2j+1, so the full matrix is the d = j+1 one
    diff=(M-A5(2*j,d)).applyfunc(s.simplify)
    W=s.diag(*[s.binomial(2*j+1,j-i) for i in range(d)])
    Mt=(W.inv()*M*W).applyfunc(s.simplify)
    off=all(s.simplify(Mt[i,i+1]-(2*D*(2*j-2*i)-a)/4)==0 and s.simplify(Mt[i+1,i]-(2*D*(2*j+2*i+4)-a)/4)==0 for i in range(d-1))
    M0=Mt.subs(a,0); marg=[s.simplify(M0[i,i]-sum(M0[i,q] for q in range(d) if q!=i)) for i in range(d)]
    G=Mt.diff(a); rs=[sum(abs(G[i,q]) for q in range(d)) for i in range(d)]
    dets=[s.simplify(Amat(j,dd).det()-Prec(2*j,dd)) for dd in range(1,d+1)]
    print('j=%d: A_d vs (5):'%j,diff==s.zeros(d,d),' (8):',off,' margins at a=0:',marg,' |d/da| row sums:',rs,' det=P_d (d<=j+1):',all(x==0 for x in dets))
print('leading coefficient of P_4 in a:',s.Poly(Prec(lam,4),a).LC())
# (iii) full-equation jets
cc=s.Rational(sys.argv[1]) if len(sys.argv)>1 else s.Integer(2)
aa=s.Rational(sys.argv[2]) if len(sys.argv)>2 else s.Integer(30)+s.Rational(1,7)
Nj=int(sys.argv[3]) if len(sys.argv)>3 else 5
H=s.Integer(1); Dn=cc-1
coef={}  # (j,i) -> symbol
h=0; Ph=0
psi0=-Dn*x*y+H/2*S(4,4)
def hom(e,n):
    p=s.Poly(e,x,y); return s.Integer(0)+sum(cf*x**i*y**k for (i,k),cf in p.terms() if i+k==n)
sol={}
for j in range(1,Nj+1):
    n=2*j+1
    cs=[s.Symbol('c_%d_%d'%(j,i)) for i in range(j+1)]
    h=h+sum(cs[i]*S(n,2*i+1) for i in range(j+1)); Ph=Ph+sum(cs[i]*P(n,2*i+1) for i in range(j+1))
    rho=aa*y+h; psi=psi0+Ph
    R=s.expand((cc*x-s.diff(psi,y))*s.diff(rho,x)+(cc*y+s.diff(psi,x))*s.diff(rho,y)-rho)
    Rn=hom(R.subs(sol),n)
    eqs=[sinproj(Rn,n,2*i+1) for i in range(j+1)]
    # Rn must be in the span of the sine modes 1..n (parity): check the full polynomial afterwards
    sj=s.solve(eqs,cs,dict=True); assert len(sj)==1
    sol.update({k:s.nsimplify(v) for k,v in sj[0].items()})
    chk=s.expand(hom(R.subs(sol),n))
    assert chk==0, ('degree',n,'not solved')
Fa=aa**2-(4*cc+20)*aa+128*cc-64
b=sol[s.Symbol('c_1_0')]+3*sol[s.Symbol('c_1_1')]/4*0  # placeholder replaced below
h3=s.expand(hom(h.subs(sol),3)); pb=s.Poly(h3,x,y)
bb=pb.coeff_monomial(x**2*y); ee=pb.coeff_monomial(y**3)
print('c=%s a=%s: b vs (24):'%(cc,aa),s.simplify(bb+192*H*aa/Fa),' e vs (24):',s.simplify(ee+32*H*aa*(aa-4*cc+2)/Fa))
w,v=s.symbols('w v')
def bnorm(e,n):
    e2=s.expand(e.subs({x:(w+v)/2,y:(w-v)/(2*s.I)}))
    pp=s.Poly(e2,w,v); return max(abs(pp.coeff_monomial(w**k*v**(n-k)))/s.binomial(n,k) for k in range(n+1))
print('binomial norms ||h_n||, n = 3, 5, ...:',[float(bnorm(hom(h.subs(sol),2*j+1),2*j+1)) for j in range(1,Nj+1)])
print('full residual vanishes through degree',2*Nj+1,':',all(hom(s.expand(((cc*x-s.diff(psi0+Ph,y))*s.diff(aa*y+h,x)+(cc*y+s.diff(psi0+Ph,x))*s.diff(aa*y+h,y)-aa*y-h).subs(sol)),n)==0 for n in range(1,2*Nj+2)))
