# Independent check (lead) of a referee answer, section 2: at A = 2 the j = 5 axis equation T_5 has a log term
# H_5 log x with coefficient Res_0 [F_5/(w H_5)], built directly from the axis hierarchy of 6.3.1 (a), parts (b)-(d).
import sympy as sp
x,eps=sp.symbols('x epsilon')
A=2; cl=sp.Rational(3,2)
def chain(w,g,order):
    h=2*cl-sp.diff(w,x)
    a2=(sp.diff(g,x)-sp.diff(w,x,2))/2
    b3=-sp.diff(a2,x)/3
    F3=-a2*sp.diff(g,x)-b3*g
    # check the referee's (8): G_3 = g a2/(3 w) solves T_3
    G3=g*a2/(3*w)
    T3=sp.simplify(w*sp.diff(G3,x)+(3*h-1)*G3-F3)
    W14=(sp.diff(b3,x)+sp.diff(G3,x))/4
    W25=-sp.diff(W14,x)/5
    F5=-a2*sp.diff(G3,x)-3*b3*G3-W14*sp.diff(g,x)-W25*g
    H5=4*g**7/w**2
    I5=F5/(w*H5)
    return T3,I5
# (1) R12 at A = 2, L = 2
u=x/2
w=-A*x*(1-u**2)/(1+u**2); g=x**2/(1+u**2)
print('R12 axis eq check:',sp.simplify(sp.diff(w/g,x)-A/g))
T3,I5=chain(w,g,0)
print('T3 residual for G3=g a/(3w):',sp.simplify(T3))
I5s=sp.factor(sp.simplify(I5)); print('I5 =',I5s)
print('Res_0 I5 =',sp.residue(I5s,x,0))
# (2) sine pair
w=-2*sp.sin(x); g=2*(1-sp.cos(x))
print('sine axis eq:',sp.simplify(sp.diff(w/g,x)-A/g))
T3,I5=chain(w,g,0); print('sine T3:',sp.simplify(T3),' I5:',sp.simplify(I5))
# (3) w = -2x + eps x^15, to first order in eps, as series
N=40
w=-2*x+eps*x**15
lg=sp.integrate(sp.series(sp.diff(w,x)-A,x,0,N).removeO()/w - 2/x,x)  # not exact; do series instead
r=sp.series((sp.diff(w,x)-A)/w-2/x,eps,0,2).removeO()
r=sp.expand(sp.series(r,x,0,N).removeO())
g=sp.expand(x**2*sp.series(sp.exp(sp.integrate(r,x)),eps,0,2).removeO())
g=sp.expand(sp.series(g,x,0,N).removeO())
T3,I5=chain(w,g,0)
I5e=sp.series(I5,eps,0,2).removeO()
I5e=sp.series(I5e,x,0,2).removeO()
print('Res_0 I5 (w=-2x+eps x^15) =',sp.simplify(sp.expand(I5e).coeff(x,-1)))
