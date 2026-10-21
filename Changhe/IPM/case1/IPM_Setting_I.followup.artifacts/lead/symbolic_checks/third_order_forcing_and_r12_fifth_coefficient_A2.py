# Lead checks of a referee's claims: (a) the forcing F of (D + 2 b_y - 1) K = F; (b) B_5 and G_5 on R12 at A = 2, L = 2.
import sympy as sp
x,y,A=sp.symbols('x y A')
# (a) generic a(x,y); b with b_y = A + 1 - a_x; f with a f_x + b f_y = f imposed by elimination of f_x
a=sp.Function('a')(x,y); bb=sp.Function('b')(x,y); f=sp.Function('f')(x,y)
fx_expr=(f-bb*sp.diff(f,y))/a
def elim(e):
    # replace any derivative of f containing x by derivatives of fx_expr (repeat), and b_y by A + 1 - a_x
    for _ in range(6):
        reps={}
        for d in e.atoms(sp.Derivative):
            if d.expr==f:
                vs=list(d.variables)
                if x in vs:
                    vs.remove(x)
                    t=fx_expr
                    for v in vs: t=sp.diff(t,v)
                    reps[d]=t
            if d.expr==bb:
                vs=list(d.variables)
                if y in vs:
                    vs.remove(y)
                    t=A+1-sp.diff(a,x)
                    for v in vs: t=sp.diff(t,v)
                    reps[d]=t
        if not reps: break
        e=e.subs(reps)
    return e
D=lambda u: a*sp.diff(u,x)+bb*sp.diff(u,y)
fy=sp.diff(f,y); ay=sp.diff(a,y)
K=sp.diff(f,y,2)-fy/a*ay
c=2*sp.diff(bb,y)-1
F=(ay**2/a-sp.diff(a,y,2))*(sp.diff(f,x)+bb*fy/a)-2*ay*sp.diff(f,x,y)+(sp.diff(a,x)-sp.diff(bb,y))*fy/a*ay
E=elim(D(K)+c*K-F)
print('(a) (D+c)K - F after imposing transport and div W = A + 1:', sp.simplify(E))
E2=elim(D(fy/a)-(-A*fy/a-(ay/a)*(sp.diff(f,x)+bb*fy/a)))
print('(a) D(f_y/a) identity:', sp.simplify(E2))
# (b) R12 at A = 2, L = 2
A2=2; h=lambda w: 2*sp.Rational(3,2)-sp.diff(w,x)
u=x/2; w=-A2*x*(1-u**2)/(1+u**2); g=x**2/(1+u**2)
hh=h(w)
a2=(sp.diff(g,x)-sp.diff(w,x,2))/2; b3=-sp.diff(a2,x)/3
F3=-a2*sp.diff(g,x)-b3*g; G3=g*a2/(3*w)
W14=(sp.diff(b3,x)+sp.diff(G3,x))/4; W25=-sp.diff(W14,x)/5
F5=-a2*sp.diff(G3,x)-3*b3*G3-W14*sp.diff(g,x)-W25*g
H5=4*g**7/w**2
I5=sp.apart(sp.simplify(F5/(w*H5)),x)
print('(b) I5 =',I5)
claim=(25*x**-5-412*x**-7+2288*x**-9-4160*x**-11)/3840
print('(b) I5 - claimed:',sp.simplify(I5-claim))
# finite part of int_0^2 of a Laurent polynomial in x (no x^-1 term)
P=sp.Poly(sp.expand(I5*x**11),x)
fp=0
for (k,),cf in P.terms():
    p=k-11
    assert p!=-1
    fp+=cf*sp.Integer(2)**(p+1)/(p+1)
print('(b) B5 = -fp int_0^2 I5 =',-fp,' claim 11/1474560 =',sp.Rational(11,1474560))
G5=x**2*(11*x**6+88*x**4-1872*x**2+9984)/(90*(x**2+4)**5)
print('(b) T5 residual w G5\' + (5h - 1) G5 - F5:',sp.simplify(w*sp.diff(G5,x)+(5*hh-1)*G5-F5))
print('(b) G5 at x = 2:',G5.subs(x,2),' H5 at 2:',sp.limit(H5,x,2))
