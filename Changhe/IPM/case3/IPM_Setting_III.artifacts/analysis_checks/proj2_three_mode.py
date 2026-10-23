# Lead independent check of the three-mode system (modes 1,3,5) claimed in proj2:
# rho/r = f sin th + g sin 3th + k sin 5th, psi/r^2 = u sin 2th + v sin 4th + w sin 6th,
# u=(T-J)/2, v=(S-K)/2, w=-L/2, Tdot=-g, Sdot=2S-k, Jdot=f-4J, Kdot=g-6K, Ldot=k-8L (t = log r).
import sympy as sp
th,c,a,H=sp.symbols('theta c a H',real=True)
f,fd,fdd,g,gd,gdd,k,kd,kdd,T,S,J,K,L=sp.symbols('f fd fdd g gd gdd k kd kdd T S J K L',real=True)
D=c-1
rules={f:fd,fd:fdd,g:gd,gd:gdd,k:kd,kd:kdd,T:-g,S:2*S-k,J:f-4*J,K:g-6*K,L:k-8*L}
def dt(e): return sp.expand(sum(sp.diff(e,v)*rules[v] for v in rules))
u=(T-J)/2; v=(S-K)/2; w=-L/2
# stream equations -Lap(r^2 W sin m th) = -(Wdd+4Wd+(4-m^2)W) r^0 sin m th ; rho_x modes / r^0:
# rho_x coefficient at sin m th: (1/2)[b_{m-1}' -(m-1)/r b_{m-1} + b_{m+1}' + (m+1)/r b_{m+1}], b_j = r F_j
def src(Fm,Fp,m):  # b=rF: b' = F + Fdot ; divided by r^0 (b'/1 has units F)
    lo = (Fm+dt(Fm)) - (m-1)*Fm if Fm!=0 else 0
    hi = (Fp+dt(Fp)) + (m+1)*Fp if Fp!=0 else 0
    return sp.expand((lo+hi)/2)
for (W,m,Fm,Fp) in [(u,2,f,g),(v,4,g,k),(w,6,k,0)]:
    lhs=-(dt(dt(W))+4*dt(W)+(4-m*m)*W)
    print('stream mode',m,sp.simplify(lhs-src(Fm,Fp,m)))
rho_r=f*sp.sin(th)+g*sp.sin(3*th)+k*sp.sin(5*th)
psi_r2=u*sp.sin(2*th)+v*sp.sin(4*th)+w*sp.sin(6*th)
drho=rho_r+dt(rho_r); rhoth=sp.diff(rho_r,th); psith=sp.diff(psi_r2,th); dpsi=2*psi_r2+dt(psi_r2)
Rr=c*drho-(psith*drho-dpsi*rhoth)-rho_r
def proj(m): return sp.expand(sp.integrate(sp.expand(sp.expand_trig(Rr*sp.sin(m*th))),(th,0,2*sp.pi))/sp.pi)
E1,E3,E5=proj(1),proj(3),proj(5)
B=(J-T)/2-K+S; C=K-sp.Rational(3,2)*L-S
F1=(D+T)*f-f**2/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2
F3=(J+2*S)*f-f**2/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k
print('E1 claim',sp.simplify(E1-((c+u)*fd+B*gd+C*kd+F1)))
print('E3 claim',sp.simplify(E3-(B*fd+(c-sp.Rational(3,2)*L)*gd-u*kd+F3)))
E5c=c*kd+D*k+C*fd-u*gd+(2*J+T)*g+2*K*f-f*g-f*k/2-sp.Rational(3,4)*g**2
print('E5 claim',sp.simplify(E5-E5c))
# centre series in z=r^2 ; dot = 2 z d/dz
z=sp.symbols('z')
f2,f4,g2,g4,k4=sp.symbols('f2 f4 g2 g4 k4')
ser={f:a+f2*z+f4*z**2, g:g2*z+g4*z**2, k:k4*z**2,
     T:a/4-D-g2*z/2-g4*z**2/4, J:a/4+f2*z/6+f4*z**2/8, K:g2*z/8+g4*z**2/10,
     L:k4*z**2/12, S:H*z-k4*z**2/2}
# check the integral variables satisfy their ODEs to order z^2
for var in [T,J,K,L,S]:
    lhs=2*z*sp.diff(ser[var],z); rhs=rules[var].subs(ser)
    print('ode',var,sp.expand(sp.series(lhs-rhs,z,0,3).removeO()))
def dz(e): return sp.expand(2*z*sp.diff(e,z))
sub=dict(ser); sub[fd]=dz(ser[f]); sub[gd]=dz(ser[g]); sub[kd]=dz(ser[k])
def co(E,n): return sp.expand(sp.expand(E.subs(sub)).coeff(z,n))
print('E1,E3,E5 at z^0:',sp.simplify(co(E1,0)),sp.simplify(co(E3,0)),sp.simplify(co(E5,0)))
b_,e_=sp.symbols('b e')
# rho = a y + b x^2 y + e y^3 : f2=(b+3e)/4 ... use claim b=f2+3g2, e=f2-g2
e1=co(E1,1); e3=co(E3,1)
solb=sp.solve([e1,e3],[f2,g2],dict=True)[0]
A=2*c-1; Fc=a**2-(4*c+20)*a+128*c-64
bb=sp.simplify(solb[f2]+3*solb[g2]); ee=sp.simplify(solb[f2]-solb[g2])
print('f2 claim',sp.simplify(solb[f2]+24*H*a*(a-4*c+4)/Fc),' g2 claim',sp.simplify(solb[g2]-8*H*a*(a-4*c-4)/Fc))
print('b claim',sp.simplify(bb+192*H*a/Fc),' e claim',sp.simplify(ee+32*H*a*(a-4*c+2)/Fc))
print('6e-(a-2A)b',sp.simplify(6*ee-(a-2*A)*bb),'  H-e/a+(5b+3e)/96',sp.simplify(H-ee/a+(5*bb+3*ee)/96))
print('E5 at z^1 (cubic R5):',sp.simplify(co(E5,1).subs(solb)))
# next order
e1b=co(E1,2).subs(solb); e3b=co(E3,2).subs(solb)
sol4=sp.solve([e1b,e3b],[f4,g4],dict=True)[0]
C5=sp.simplify(co(E5,2).subs(solb).subs(sol4))
C5c=(-2*H*f2+(D-a/20)*g4-sp.Rational(3,4)*g2**2+(5*c-1-a/2)*k4).subs(sol4).subs(solb)
print('C5 claim (20):',sp.simplify(C5-C5c))
for cv in [2,3]:
    v0=sp.factor(sp.simplify(C5.subs({c:cv,k4:0})))
    print('c=',cv,'C5(k4=0)=',v0)
print('c=2 a=20:',sp.simplify(C5.subs({c:2,a:20})),'  c=3 a=20:',sp.simplify(C5.subs({c:3,a:20})))
# indicial determinant (15)
lam=sp.symbols('lam')
M=sp.Matrix([[(c+1)*lam/2-a/4, D*lam/2+2*D-a/4-a/lam],[D*lam/2-a/4+a/(lam+4), c*lam+D-a/2]])
I=a**2-4*((c+2)*lam-D)*a+4*(c**2+4*c-1)*lam**2-8*D*(c-3)*lam
print('16 det M - I',sp.simplify(16*M.det()-I),' I(a,2)-F',sp.simplify(I.subs(lam,2)-Fc))
# linearization check: delta f = x z^{lam/2} etc; compute E1,E3 linear terms around affine centre
x,y=sp.symbols('x y')
eps=sp.symbols('eps'); p=lam/2
lin={f:a+eps*x*z**p, g:eps*y*z**p, k:0, T:a/4-D-eps*y*z**p/lam, J:a/4+eps*x*z**p/(lam+4), K:eps*y*z**p/(lam+6), L:0, S:0,
     fd:eps*x*lam*z**p, gd:eps*y*lam*z**p, kd:0}
r1=sp.simplify(sp.diff(E1.subs(lin),eps).subs(eps,0)/z**p); r3=sp.simplify(sp.diff(E3.subs(lin),eps).subs(eps,0)/z**p)
Mv=M*sp.Matrix([x,y])
print('M row1',sp.simplify(r1-Mv[0]),' row2',sp.simplify(r3-Mv[1]))
