import sympy as sp
x,b=sp.symbols('x beta')
N=8
V=[sp.Symbol('v%d'%(2*i+3)) for i in range(N)]
Fs=[sp.Symbol('f%d'%(2*i+2)) for i in range(N)]
v=-(b+2)*x+sum(V[i]*x**(2*i+3) for i in range(N))
F=sum(Fs[i]*x**(2*i+2) for i in range(N))
e1=sp.expand(v*sp.diff(F,x)+(b+2-sp.diff(v,x))*F)      # (T): even powers
e2=sp.expand(sp.diff(F,x)-(v*sp.diff(v,x,3)+(2*b+1-sp.diff(v,x))*sp.diff(v,x,2)))  # (V): odd powers
# coefficient checks
print('e1 x^2:',sp.factor(e1.coeff(x,2)))
print('e2 x^1:',sp.factor(e2.coeff(x,1)))
for m in range(2,N):
    c1=e1.coeff(x,2*m); c2=e2.coeff(x,2*m-1)
    print(m,'d e1/d f%d ='%(2*m),sp.factor(sp.diff(c1,Fs[m-1])),' e1 uses v up to',max([int(s.name[1:]) for s in c1.free_symbols if s.name[0]=='v'] or [0]),
          '| d e2/d v%d ='%(2*m+1),sp.factor(sp.diff(c2,V[m-1])),' e2 uses f up to',max([int(s.name[1:]) for s in c2.free_symbols if s.name[0]=='f'] or [0]))
# solve recursively and compare with sin / sinh families
sol={}
sol[Fs[0]]=sp.solve(e2.coeff(x,1),Fs[0])[0]
for m in range(2,N):
    sol[Fs[m-1]]=sp.solve(e1.coeff(x,2*m).subs(sol),Fs[m-1])[0]
    sol[V[m-1]]=sp.solve(e2.coeff(x,2*m-1).subs(sol),V[m-1])[0]
B=b+2
for name,vv,FF in [('sin',-(B/2)*sp.sin(2*x),2*B*(2*b+1)*sp.sin(x)**2),('sinh',-(B/2)*sp.sinh(2*x),-2*B*(2*b+1)*sp.sinh(x)**2)]:
    sv=sp.series(vv,x,0,2*N+1).removeO(); sF=sp.series(FF,x,0,2*N).removeO()
    v3v=sv.coeff(x,3)
    ok=all(sp.simplify(sol[V[m-1]].subs(V[0],v3v)-sv.coeff(x,2*m+1))==0 for m in range(2,N))
    okF=all(sp.simplify(sol[Fs[m]].subs(V[0],v3v)-sF.coeff(x,2*m+2))==0 for m in range(N-1))
    print(name,'v3=',sp.factor(v3v),'series matches recursion:',ok,okF)
