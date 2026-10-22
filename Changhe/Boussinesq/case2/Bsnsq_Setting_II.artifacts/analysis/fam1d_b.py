import sympy as sp
x,X,Y,b=sp.symbols('x X Y beta',positive=True)
B=b+2; d=2*b+1
for name,w in [('sin',b*x+(B/2)*sp.sin(2*x)),('sinh',b*x+(B/2)*sp.sinh(2*x))]:
    Psi=w.subs(x,X)*Y
    U1=-sp.diff(Psi,Y); U2=sp.diff(Psi,X)
    Om=sp.diff(U1,Y)-sp.diff(U2,X)
    W1=b*X+U1; W2=b*Y+U2
    # Theta from (V): Theta_x = W.grad Om + Om, Theta = Y*F(X)
    rhs=sp.simplify(W1*sp.diff(Om,X)+W2*sp.diff(Om,Y)+Om)
    Fp=sp.simplify(rhs/Y)
    F=sp.integrate(Fp.subs(X,x),(x,0,X))
    Th=sp.simplify(F*Y)
    T=sp.simplify(W1*sp.diff(Th,X)+W2*sp.diff(Th,Y)-(b-2)*Th)
    print(name,'Theta =',sp.simplify(Th),' (T) residual:',sp.simplify(T.rewrite(sp.exp)),' -LapPsi-Om:',sp.simplify(-sp.diff(Psi,X,2)-sp.diff(Psi,Y,2)-Om))
    print('  W1 on axis:',sp.simplify(W1.subs(Y,0)),' Psi_xy(0)=',sp.simplify(sp.diff(Psi,X,Y).subs({X:0,Y:0})),' a0=',sp.simplify(sp.diff(Th,X,2,Y,1).subs({X:0,Y:0})/2))
# uniqueness of odd/even series: recursion to order 21
N=11
vs=sp.symbols('v3:%d'%(2*N+3))
v=-(b+2)*x+sum(sp.Symbol('v%d'%(2*i+3))*x**(2*i+3) for i in range(N))
F=sum(sp.Symbol('f%d'%(2*i+2))*x**(2*i+2) for i in range(N+1))
e1=sp.expand(v*sp.diff(F,x)+(b+2-sp.diff(v,x))*F)
e2=sp.expand(sp.diff(F,x)-(v*sp.diff(v,x,3)+(2*b+1-sp.diff(v,x))*sp.diff(v,x,2)))
sol={}
v3=sp.Symbol('v3')
for k in range(1,2*N-1):
    for e in (e2,e1):
        c=sp.expand(e.coeff(x,k).subs(sol))
        if c==0: continue
        fr=[s for s in c.free_symbols if s not in (b,v3)]
        tgt=max(fr,key=lambda s:(s.name[0]=='v', int(s.name[1:]))) if fr else None
        if tgt is None: print('constraint on v3 at order',k,c); continue
        sol[tgt]=sp.solve(c,tgt)[0]
print('determined:',sorted([s.name for s in sol],key=lambda n:(n[0],int(n[1:]))))
