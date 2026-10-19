# Independent check of the strain and orientation moments at the origin (my own code):
#   psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX,   psi_yy(0) = -(1/pi) int rho r^-3 cos 3th dX,
# with W = (-psi_y, psi_x), Lap psi = -rho_x (omega = -rho_x), i.e. psi = -d_x phi, Lap phi = rho.
# Test density: a Gaussian blob rho = exp(-|X - X0|^2/s^2), radial about X0, so phi is radial about X0 with
# phi'(t) = (1/t) int_0^t rho(u) u du = (s^2/2)(1 - exp(-t^2/s^2))/t.  Exact third derivatives of phi at 0 by sympy;
# moments by polar quadrature (trapezoid in theta, Gauss-Legendre in r).  Also: parity under x -> -x.
import sympy as sp, numpy as np
x,y=sp.symbols('x y',real=True)
def exact(X0,s):
    t=sp.sqrt((x-X0[0])**2+(y-X0[1])**2)
    g=(sp.Rational(1,2)*s**2*(1-sp.exp(-t**2/s**2))/t)/t      # phi'(t)/t
    phx=g*(x-X0[0]); phy=g*(y-X0[1])                          # grad phi
    psi_x=-sp.diff(phx,x); psi_y=-sp.diff(phx,y)              # psi = -phi_x
    pxy=sp.diff(psi_x,y); pyy=sp.diff(psi_y,y); pxx=sp.diff(psi_x,x)
    sub={x:0,y:0}
    return [float(sp.N(e.subs(sub),30)) for e in (pxy,pyy,pxx)]
def moments(X0,s,Nr=400,Nt=512,r0=1e-3,r1=None):
    d=np.hypot(*X0); r1=r1 or d+12*s; r0=max(r0,d-12*s)
    u,w=np.polynomial.legendre.leggauss(Nr); r=0.5*(r1-r0)*u+0.5*(r1+r0); w=0.5*(r1-r0)*w
    th=2*np.pi*np.arange(Nt)/Nt; R,T=np.meshgrid(r,th,indexing='ij')
    rho=np.exp(-((R*np.cos(T)-X0[0])**2+(R*np.sin(T)-X0[1])**2)/s**2)
    f=lambda a: (2*np.pi/Nt)*np.sum(w[:,None]*R**-2*rho*a)     # r^-3 * r dr dth
    return f(np.sin(3*T))/np.pi, -f(np.cos(3*T))/np.pi
# Disk principal value: the delta part of D^2 N gives core terms when grad rho(0) != 0:
#   psi_xy(0) = PV moment - rho_y(0)/4,  psi_yy(0) = PV moment - rho_x(0)/4,  psi_xx + psi_yy = -rho_x(0)
# (zero for states with the jet rho = x^2 + O(r^3), where grad rho(0) = 0).
def grad0(X0,s):
    r0=np.exp(-(X0[0]**2+X0[1]**2)/s**2); return 2*X0[0]/s**2*r0, 2*X0[1]/s**2*r0
ok=True
for X0,s in [((1.5,0.8),0.3),((-1.5,0.8),0.3),((0.4,-1.1),0.25),((2.0,0.0),0.4)]:
    pxy,pyy,pxx=exact(X0,s); mxy,myy=moments(X0,s); rx,ry=grad0(X0,s)
    print(f"   core: rho_x(0) {rx:.3e} rho_y(0) {ry:.3e}; psi_xy - moment {pxy-mxy:.3e} vs -rho_y/4 {-ry/4:.3e}; psi_yy - moment {pyy-myy:.3e} vs -rho_x/4 {-rx/4:.3e}")
    ok&= abs(pxy-mxy+ry/4)<1e-12 and abs(pyy-myy+rx/4)<1e-12 and abs(pxx+pyy+rx)<1e-13
    mxy-=ry/4; myy-=rx/4
    e1=abs(pxy-mxy)/max(abs(pxy),1e-300); e2=abs(pyy-myy)/max(abs(pyy),1e-12)
    print(f"X0={X0} s={s}: psi_xy exact {pxy:.12e} moment {mxy:.12e} (rel {e1 if abs(pxy)>1e-14 else 0:.1e}); psi_yy exact {pyy:.12e} moment {myy:.12e} (rel {e2:.1e}); psi_xx + psi_yy = {pxx+pyy:.1e}")
    ok&= (e1<1e-9 or abs(pxy)<1e-14) and e2<1e-9
a=exact((1.5,0.8),0.3); b=exact((-1.5,0.8),0.3)
print("parity x->-x: psi_xy", a[0], b[0], " psi_yy", a[1], b[1])
ok&= abs(a[0]-b[0])<1e-14 and abs(a[1]+b[1])<1e-14
print("ALL OK" if ok else "FAIL")
