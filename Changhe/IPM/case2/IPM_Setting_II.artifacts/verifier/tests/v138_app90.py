# V138: symbolic checks for draft FR 9.0 (sha 14b0ab39), Steps 1-7.
import sympy as sp
ok=[]
def chk(name,cond):
    ok.append(bool(cond)); print(('OK  ' if cond else 'FAIL'), name)
x,y,r,s,th=sp.symbols('x y r s theta',real=True)
l=sp.symbols('l',positive=True)
# Step 1: kernel K = (Q_xy, -Q_xx)-type derivative of G = log|Z|/(2 pi)
G=sp.log(x**2+y**2)/(4*sp.pi)
K1=sp.simplify(sp.diff(G,x,y)); K2=sp.simplify(-sp.diff(G,x,2))
Z2=x**2+y**2
chk('K1 = -sin(2th)/(2 pi r^2)', sp.simplify(K1+2*x*y/Z2/(2*sp.pi*Z2))==0)
chk('K2 = cos(2th)/(2 pi r^2)', sp.simplify(K2-(x**2-y**2)/Z2/(2*sp.pi*Z2))==0)
chk('div K = 0 off 0', sp.simplify(sp.diff(K1,x)+sp.diff(K2,y))==0)
chk('curl K = 0 off 0', sp.simplify(sp.diff(K2,x)-sp.diff(K1,y))==0)
Kp=[k.subs({x:sp.cos(th),y:sp.sin(th)}) for k in (K1,K2)]
chk('K zero mean on circles', all(sp.simplify(sp.integrate(k,(th,0,2*sp.pi)))==0 for k in Kp))
# delta coefficient: radial rho, Q radial with Lap Q = rho, W(0) = (Q_xy, -Q_xx)(0) = (0, -rho(0)/2)
a0,a1=sp.symbols('a0 a1')
Q=a0*(x**2+y**2)/4+a1*(x**2+y**2)**2/16
rho_rad=sp.expand(sp.diff(Q,x,2)+sp.diff(Q,y,2))
chk('Lap Q = a0 + a1 r^2', sp.simplify(rho_rad-(a0+a1*(x**2+y**2)))==0)
chk('W(0) = -(rho(0)/2) e_2 for radial rho', sp.diff(Q,x,2).subs({x:0,y:0})==a0/2 and sp.diff(Q,x,y).subs({x:0,y:0})==0)
# Lap W_1 = rho_xy, Lap W_2 = -rho_xx from div W = 0, curl W = -rho_x (W = (-psi_y, psi_x), Lap psi = -rho_x)
f=sp.Function('f')(x,y); psi=sp.Function('psi')(x,y)
W1=-sp.diff(psi,y); W2=sp.diff(psi,x)
lap=lambda u: sp.diff(u,x,2)+sp.diff(u,y,2)
e1=sp.simplify(lap(W1)-(-sp.diff(lap(psi),y)))
e2=sp.simplify(lap(W2)-(sp.diff(lap(psi),x)))
chk('Lap W1 = -d_y Lap psi = rho_xy; Lap W2 = d_x Lap psi = -rho_xx', e1==0 and e2==0)
# Step 2 integrals
q,R=sp.symbols('q R',positive=True)
rp=sp.symbols('rp',positive=True); sp_=sp.symbols('sp_',positive=True)
chk('int_{2r}^inf s^(q-2) = (2r)^(q-1)/(1-q) (q = 0, 1/3, 7/20)', all(sp.simplify(sp.integrate(sp_**(qv-2),(sp_,2*rp,sp.oo))-(2*rp)**(qv-1)/(1-qv))==0 for qv in [sp.Integer(0),sp.Rational(1,3),sp.Rational(7,20)]))
# int_1^{2r} s^{q-1} <= (2r)^q log(2r): numeric scan
import math
good=True
for qq in [0.0,0.1,0.35,0.6,0.95]:
    for rr in [2,3,10,1e3,1e6]:
        lhs=math.log(2*rr) if qq==0 else ((2*rr)**qq-1)/qq
        good &= lhs <= (2*rr)**qq*math.log(2*rr)*(1+1e-12)
chk('int_1^{2r} s^(q-1) ds <= (2r)^q log(2r)', good)
# Step 3: m' <= a m + C  =>  m <= (m0 + C s) e^{a s}
aa,CC,m0=sp.symbols('a C m0',positive=True)
msol=m0*sp.exp(aa*s)+CC*(sp.exp(aa*s)-1)/aa
good=all(float(((m0+CC*s)*sp.exp(aa*s)-msol).subs({aa:av,CC:cv,m0:mv,s:sv}))>=-1e-9 for av in [0.1,1,3] for cv in [0.5,2] for mv in [1,5] for sv in [0,0.5,3,10])
chk('comparison solution <= (m0 + C s) e^{a s}', good)
# Step 4: jet algebra
M11,M12,M21,M22=sp.symbols('M11 M12 M21 M22')
VX=sp.Matrix([[M11,M12],[M21,M22]])*sp.Matrix([x,y])
P=sp.Poly(sp.expand(VX[0]*2*x - x**2),x,y)
sol=sp.solve([P.coeff_monomial(x**2),P.coeff_monomial(x*y)],[M11,M12],dict=True)
chk('V.grad rho = rho at order 2 gives M11 = 1/2, M12 = 0', sol==[{M11:sp.Rational(1,2),M12:0}])
c=sp.symbols('c')
ps=c*x*y  # psi with psi_xy = c, psi_xx = psi_yy = 0
DW=sp.Matrix([[sp.diff(-sp.diff(ps,y),x),sp.diff(-sp.diff(ps,y),y)],[sp.diff(sp.diff(ps,x),x),sp.diff(sp.diff(ps,x),y)]])
chk('DW(0) = diag(-c, c) for psi_xy(0) = c', DW==sp.Matrix([[-c,0],[0,c]]))
chk('l + DW_11 = 1/2 gives DV(0) = diag(1/2, 2l - 1/2)', sp.solve(l-c-sp.Rational(1,2),c)==[l-sp.Rational(1,2)] and sp.simplify((l+c).subs(c,l-sp.Rational(1,2))-(2*l-sp.Rational(1,2)))==0)
# Step 5: decay of r^(g-1)(1 + log r) and integrability bound
g=sp.symbols('gamma',positive=True)
der=sp.simplify(sp.diff(r**(g-1)*(1+sp.log(r)),r)*r**(2-g))
chk('d/dr[r^(g-1)(1+log r)] = r^(g-2)[(g-1)(1+log r)+1]', sp.simplify(der-((g-1)*(1+sp.log(r))+1))==0)
# Step 6: polar form and Holder exponent
p=1/l
rho=sp.Function('rho')(r)
lhs=l*r**(p+1)*sp.diff(r**(-p)*rho,r)
chk('l r^{p+1} d_r(r^-p rho) = l r rho_r - rho', sp.simplify(sp.expand(lhs-(l*r*sp.diff(rho,r)-rho)))==0)
d,gg,pp=sp.symbols('d gamma_ p_',positive=True)
rr=d**(-1/(1-pp))
e_grad=sp.simplify(sp.expand_log(sp.log(d*rr**(gg-pp)),force=True)/sp.log(d))
e_tail=sp.simplify(sp.expand_log(sp.log(rr**(gg-1)),force=True)/sp.log(d))
chk('both Holder terms have exponent (1-gamma)/(1-p)', sp.simplify(e_grad-(1-gg)/(1-pp))==0 and sp.simplify(e_tail-(1-gg)/(1-pp))==0)
tt=sp.symbols('tt',positive=True); r1=1+tt
good=True
for gv in [sp.Rational(1,3),sp.Rational(7,20),sp.Rational(9,10)]:
    I=sp.integrate(sp_**(gv-2)*(1+sp.log(sp_)),(sp_,r1,sp.oo))
    for tv in [sp.Rational(1,2),3,40]:
        good &= abs(float((I-r1**(gv-1)*((1+sp.log(r1))/(1-gv)+1/(1-gv)**2)).subs(tt,tv)))<1e-12
chk('int_r^inf s^(g-2)(1+log s) = r^(g-1)[(1+log r)/(1-g) + 1/(1-g)^2] (r > 1)', good)
# Step 7 (F4) on a nonlinear example: xi = x + y^2, V = ((x + y^2)/2 - 2 b y^2, b y), b = 2l - 1/2
b=2*l-sp.Rational(1,2)
xi=x+y**2; Vv=sp.Matrix([(x+y**2)/2-2*b*y**2, b*y]); rh=xi**2
chk('example: div V = 2l', sp.simplify(sp.diff(Vv[0],x)+sp.diff(Vv[1],y)-2*l)==0)
chk('example: V.grad rho = rho', sp.simplify(Vv[0]*sp.diff(rh,x)+Vv[1]*sp.diff(rh,y)-rh)==0)
# on Gamma: x = -y^2, orbit y(s) = y0 e^{b s}
y0=sp.symbols('y0',positive=True)
ys=y0*sp.exp(b*s); xs=-ys**2
chk('Gamma point moves along V', sp.simplify(sp.diff(xs,s)-Vv[0].subs({x:xs,y:ys}))==0 and sp.simplify(sp.diff(ys,s)-Vv[1].subs({x:xs,y:ys}))==0)
H=sp.hessian(rh,(x,y)).subs({x:xs,y:ys})
gx=sp.Matrix([sp.diff(xi,x),sp.diff(xi,y)]).subs({x:xs,y:ys}); N=gx/sp.sqrt(gx.dot(gx))
h=sp.simplify((N.T*H*N)[0])
chk('h = 2|grad xi|^2 on Gamma', sp.simplify(h-2*gx.dot(gx))==0)
V2=sp.simplify(Vv.subs({x:xs,y:ys}).dot(Vv.subs({x:xs,y:ys})))
chk('(F4): d/ds log(h/|V|^2) = 1 - 4l', sp.simplify(sp.diff(sp.log(h/V2),s)-(1-4*l))==0)
# matrix ODE dH/ds = H - DV^T H - H DV along Gamma
DV=Vv.jacobian([x,y]).subs({x:xs,y:ys})
Hs=sp.hessian(rh,(x,y)).subs({x:xs,y:ys})
chk('dH/ds = H - DV^T H - H DV on Gamma', sp.simplify(sp.diff(Hs,s)-(Hs-DV.T*Hs-Hs*DV))==sp.zeros(2,2))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
