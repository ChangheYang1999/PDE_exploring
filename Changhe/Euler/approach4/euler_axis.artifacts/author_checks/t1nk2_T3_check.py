# Lead check of the referee's far-axis transport coefficients T1, T2, T3 (t1nk2 answer): with y = z^-k (k = 1/c_l),
# w = c z + 2 phi(0, z) = z (c + b y + d y^2 + ...), h = H y (1 + h1 y + h2 y^2), solve w h' = (w' - 1 - c) h order by order and
# expand e = 2 h (h - 1)/w; eta = K^2 e = z^(-1) y (T1 + T2 y + T3 y^2 + ...). Terms with extra powers z^-2 are a separate
# exponent family and are dropped.
import sympy as sp
c,b,d,H,K,y,h1,h2=sp.symbols('c b d H K y h1 h2')
k=1/c
# z d/dz acting on y^n gives -n k y^n
def zD(expr):
    p=sp.Poly(sp.expand(expr),y); return sum(coef*(-m[0]*k)*y**m[0] for m,coef in zip(p.monoms(),p.coeffs()))
h=H*y*(1+h1*y+h2*y**2)
wz=c+b*y+d*y**2                      # w/z
wp=c+b*(1-k)*y+d*(1-2*k)*y**2        # w'
eq=sp.expand(wz*zD(h)-(wp-1-c)*h)
sol=sp.solve([sp.expand(eq).coeff(y,n) for n in (2,3)],[h1,h2],dict=True)[0]
hs=h.subs(sol)
e_times_z=sp.series(2*hs*(hs-1)/wz,y,0,4).removeO()
eta=sp.expand(K**2*e_times_z)
T=[sp.simplify(eta.coeff(y,n)) for n in (1,2,3)]
a=2*K**2*H/c
claims=[-a, a*(H+(1+k)*b), a*((1+k)/2*(d-(1+2*k)*b**2)-(2+k)*b*H)]
for n,(Tn,cl) in enumerate(zip(T,claims),1):
    print('T%d'%n, sp.factor(Tn), ' claim matches:', sp.simplify(Tn-cl)==0)
print('h1,h2 =',sp.factor(sol[h1]),';',sp.factor(sol[h2]))
