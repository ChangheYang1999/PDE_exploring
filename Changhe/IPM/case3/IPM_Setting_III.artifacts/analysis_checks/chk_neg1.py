# s = -1 (negative slopes): leading inner problem of the near-axis layer; X = +lambda/z^2.
# u_alg = G^{2,2}_{2,3}(X | 1-a1, 1-a2 ; 0, 1-b1 | 1-b2): check ODE, small-X content, large-X algebraic coefficients.
import mpmath as mp
mp.mp.dps=40
def pars(p):
    a1=-p/2; a2=(1-p)/2; b1=mp.mpf(p)/(p+1); b2=2
    return a1,a2,b1,b2
def G(X,p):
    a1,a2,b1,b2=pars(p)
    return mp.meijerg([[1-a1,1-a2],[]],[[0,1-b1],[1-b2]],X)
def T(f,X,k):  # (X d/dX)^k f
    if k==0: return f(X)
    g=lambda x: x*mp.diff(f,x)
    return T(g,X,k-1) if k>1 else X*mp.diff(f,X)
def ode_res(p,X):
    a1,a2,b1,b2=pars(p); f=lambda x:G(x,p)
    # [T(T+b1-1)(T+b2-1) - X(T+a1)(T+a2)] u, expanded via derivatives
    u=f(X); d=[mp.diff(f,X,k) for k in range(4)]
    Tu=X*d[1]; T2u=X*d[1]+X**2*d[2]; T3u=X*d[1]+3*X**2*d[2]+X**3*d[3]
    lhs=T3u+(b1-1+b2-1)*T2u+(b1-1)*(b2-1)*Tu
    rhs=X*(T2u+(a1+a2)*Tu+a1*a2*u)
    return (lhs-rhs)/max(abs(lhs),abs(rhs),abs(u))
for p in [mp.mpf('0.25'),mp.mpf(1)/3,mp.sqrt(2)-1,mp.mpf('0.5'),mp.mpf('0.75')]:
    a1,a2,b1,b2=pars(p)
    print('p=%s'%mp.nstr(p,8))
    for X in [mp.mpf('0.3'),mp.mpf(3),mp.mpf(30)]:
        print('  ode residual X=%s: %s'%(X,mp.nstr(ode_res(p,X),3)))
    # large X: G ~ cE X^{-a1}(1+...) + cO X^{-a2}(1+...)
    cE=mp.gamma(a1)*mp.gamma(1-b1+a1)*mp.gamma(a2-a1)/mp.gamma(b2-a1)
    cO=mp.gamma(a2)*mp.gamma(1-b1+a2)*mp.gamma(a1-a2)/mp.gamma(b2-a2)
    # numerical check of cO: fit G(X) - cE X^{-a1} series? use subtraction of the X^{-a1} series to 3 terms
    def ser(X,a,k):  # asymptotic series of the residue sum at sigma=-a-k (exact residues)
        s=0
        for j in range(k):
            sig=-a-j
            # residue of Gamma(a+sigma) at sigma=-a-j is (-1)^j/j!
            other=[x for x in (a1,a2) if x!=a][0]
            num=mp.gamma(-sig)*mp.gamma(1-b1-sig)*mp.gamma(other+sig)
            s+=(-1)**j/mp.factorial(j)*num/mp.gamma(b2+sig)*X**sig
        return s
    for X in [mp.mpf(200),mp.mpf(800)]:
        g=G(X,p); approx=ser(X,a1,6)+ser(X,a2,6)
        print('  X=%s: G=%s, two-series sum=%s, rel diff %s'%(X,mp.nstr(g,12),mp.nstr(approx,12),mp.nstr((g-approx)/g,3)))
    print('  cE=%s cO=%s'%(mp.nstr(cE,10),mp.nstr(cO,10)))
    # small X: no X^{-1} term (z^{p+2} branch): X*G(X) -> 0
    for X in [mp.mpf('1e-6'),mp.mpf('1e-9')]:
        print('  small X=%s: G=%s, X*G=%s'%(X,mp.nstr(G(X,p),12),mp.nstr(X*G(X,p),3)))
