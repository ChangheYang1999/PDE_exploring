# Lead's independent check of the verifier's exact trace with C_p = 0 (197)
import sympy as sp, mpmath as mp
x,y,p,L,s,t=sp.symbols('x y p L s t',positive=True)
C=1/(p+2); r=sp.sqrt(x**2+y**2)
f=C*y*r**(p-3)*(3*x**2+(p+2)*y**2)
Psi=-C*x*y*r**(p-1)
V1=C*x*r**(p-3)*(x**2+p*y**2); V2=-C*y*r**(p-3)*(p*x**2+y**2)
S=sp.simplify
print('V=(-Psi_y,Psi_x):',S(V1+sp.diff(Psi,y)),S(V2-sp.diff(Psi,x)))
print('-Psi_yy=f_x:',S(-sp.diff(Psi,y,2)-sp.diff(f,x)))
print('V1_y=f_x:',S(sp.diff(V1,y)-sp.diff(f,x)))
print('V2_y=-V1_x:',S(sp.diff(V2,y)+sp.diff(V1,x)))
print('V2_yy=-f_xx:',S(sp.diff(V2,y,2)+sp.diff(f,x,2)))
fy=S(sp.diff(f,y)); print('f_y=',sp.factor(fy))
fx=S(sp.diff(f,x)); print('f_x=',sp.factor(fx))
# Euler: (cX.grad - 1) f = 0 with c=1/p
print('Euler:',S((x*sp.diff(f,x)+y*sp.diff(f,y))/p-f))
# next term
Vg=S(V1*sp.diff(f,x)+V2*sp.diff(f,y))
cand=-C**2*y*r**(2*p-6)*(3*x**4+2*p*(p+2)*x**2*y**2+p*(p+2)*y**4)
print('V.grad f vs claim:',S(Vg-cand))
# trace
th=sp.symbols('theta')
Th=S(f.subs({x:sp.cos(th),y:sp.sin(th)}))
Thc=sp.sin(th)*(3*sp.cos(th)**2+(p+2)*sp.sin(th)**2)/(p+2)
print('trace:',S(sp.expand_trig(Th-Thc)))
eps=(1-p)/(3*(p+3))
print('sin+eps sin3 prop:',S(sp.expand_trig((sp.sin(th)+eps*sp.sin(3*th))/Thc)))
print('Theta prime:',S(sp.diff(Thc,th)-3*sp.cos(th)*(sp.cos(th)**2+p*sp.sin(th)**2)/(p+2)))
# perturbation identity int s[p(p-1)chi-2(p-1)s chi'+s^2 chi'']=(p+1)(p+2) int s chi, by parts symbolic
chi=sp.Function('chi')
# check with explicit polynomial bump on [1,2]
b=(s-1)**4*(2-s)**4
lhs=sp.integrate(s*(p*(p-1)*b-2*(p-1)*s*sp.diff(b,s)+s**2*sp.diff(b,s,2)),(s,1,2))
rhs=(p+1)*(p+2)*sp.integrate(s*b,(s,1,2))
print('perturbation identity:',S(lhs-rhs))
# numeric C_p from definition for a few p (direct full-tail)
for pv in (sp.Rational(1,3),sp.Rational(3,4),sp.Rational(9,10)):
    F=S(f.subs(x,1).subs(y,s).subs(p,pv))
    q=S(pv*(pv-1)*F-2*(pv-1)*s*sp.diff(F,s)+s**2*sp.diff(F,s,2))
    Qv=pv*(pv-1)/(pv+2)
    fn=sp.lambdify(s,s*(q-Qv*s**(pv-2)),'mpmath')
    mp.mp.dps=30
    val=mp.quad(fn,[0,1,10,100,mp.inf])
    print('p=',pv,'C_p numeric =',mp.nstr(val,12),' Q check',S(sp.limit(q/s**(pv-2),s,sp.oo)-Qv))
# V2 from full-tail formula at x=1, y=0.7, p=3/4 numerically
pv=sp.Rational(3,4)
fxx=sp.lambdify((x,t),sp.diff(f,x,2).subs(y,t).subs(p,pv),'mpmath')
xv,yv=mp.mpf(1),mp.mpf('0.7')
V2n=mp.quad(lambda tt:tt*fxx(xv,tt),[0,yv])+yv*mp.quad(lambda tt:fxx(xv,tt),[yv,1,10,mp.inf])
print('V2 numeric vs formula:',mp.nstr(V2n,15),mp.nstr(sp.N(V2.subs({x:1,y:sp.Rational(7,10),p:pv}),20),15))
fxn=sp.lambdify((x,t),sp.diff(f,x).subs(y,t).subs(p,pv),'mpmath')
V1n=-mp.quad(lambda tt:fxn(xv,tt),[yv,1,10,mp.inf])
print('V1 numeric vs formula:',mp.nstr(V1n,15),mp.nstr(sp.N(V1.subs({x:1,y:sp.Rational(7,10),p:pv}),20),15))
# smooth lift
CL=sp.symbols('C_L',positive=True); R=sp.sqrt(L**2+x**2+y**2)
gL=CL*y*R**(p-3)*(3*(L**2+x**2)+(p+2)*y**2); PsiL=-CL*x*y*R**(p-1)
V1L=-sp.diff(PsiL,y); V2L=sp.diff(PsiL,x)
print('lift -Psi_yy=g_x:',S(-sp.diff(PsiL,y,2)-sp.diff(gL,x)))
print('lift V1 formula:',S(V1L-CL*x*R**(p-3)*(L**2+x**2+p*y**2)),' V2 formula:',S(V2L+CL*y*R**(p-3)*(L**2+p*x**2+y**2)))
sub={CL:L**(1-p)/3}
G=sp.series(gL.subs(sub).subs(x,0),y,0,5).removeO(); v2=sp.series(V2L.subs(sub).subs(x,0),y,0,5).removeO()
print('G=',S(G)); print('V2L=',S(v2))
c=sp.Rational(4,3)
res=sp.expand(S((c*y+v2)*sp.diff(G,y)-G).subs(p,sp.Rational(3,4)))
print('axis residual (c=4/3,p=3/4) to O(y^5):',sp.series(res,y,0,5))
print('--- refinement')
print('f_x claim:',S(fx-C*(p-1)*x*y*r**(p-5)*(3*x**2+p*y**2)))
print('f_y claim:',S(fy-C*r**(p-5)*(3*x**4+6*p*x**2*y**2+p*(p+2)*y**4)))
mp.mp.dps=40
for pv in (sp.Rational(1,3),sp.Rational(3,4),sp.Rational(9,10)):
    F=S(f.subs(x,1).subs(y,s).subs(p,pv))
    q=S(pv*(pv-1)*F-2*(pv-1)*s*sp.diff(F,s)+s**2*sp.diff(F,s,2))
    Qv=pv*(pv-1)/(pv+2)
    fn=sp.lambdify(s,s*(q-Qv*s**(pv-2)),'mpmath')
    a=mp.quad(fn,[0,1]); b=mp.quad(lambda u: fn(mp.e**u)*mp.e**u,[0,5,20,60,200])
    print('p=',pv,'C_p (log tail) =',mp.nstr(a+b,15))
pv=sp.Rational(3,4)
fxx=sp.lambdify((x,t),sp.diff(f,x,2).subs(y,t).subs(p,pv),'mpmath')
xv,yv=mp.mpf(1),mp.mpf('0.7')
tail=mp.quad(lambda u: fxx(xv,yv*mp.e**u)*yv*mp.e**u,[0,2,10,40,200])
V2n=mp.quad(lambda tt:tt*fxx(xv,tt),[0,yv])+yv*tail
print('V2 numeric(log tail) vs formula:',mp.nstr(V2n,20),mp.nstr(sp.N(V2.subs({x:1,y:sp.Rational(7,10),p:pv}),25),20))
