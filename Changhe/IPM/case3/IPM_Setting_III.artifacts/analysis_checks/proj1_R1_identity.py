# Lead hand check of the first-projection identity R_1/(pi r) = L fdot - N for
# rho = r f sin th + r g sin 3th, psi = r^2 Z2 sin 2th + r^2 Z4 sin 4th, Z2=(T-J)/2, Z4=-K/2,
# with Tdot=-g, Jdot=f-4J, Kdot=g-6K (t = log r). Also the stream equation.
import sympy as sp
th,t,l=sp.symbols('theta t ell',real=True)
f,fd,fdd,g,gd,gdd,T,J,K=sp.symbols('f fd fdd g gd gdd T J K',real=True)
D=l-1
# time derivatives as linear maps on polynomial expressions in (f,fd,g,gd,T,J,K)
def dt(e):
    rules={f:fd,fd:fdd,g:gd,gd:gdd,T:-g,J:f-4*J,K:g-6*K}
    return sum(sp.diff(e,v)*rules[v] for v in rules)
r=sp.exp(t)
Z2=(T-J)/2; Z4=-K/2
rho_r = f*sp.sin(th)+g*sp.sin(3*th)          # rho / r
psi_r2= Z2*sp.sin(2*th)+Z4*sp.sin(4*th)      # psi / r^2
# r rho_r = d_t rho = r (rho/r + d_t(rho/r)); psi_theta, d_t psi
drho = rho_r+dt(rho_r)          # (d_t rho)/r
rhoth= sp.diff(rho_r,th)        # rho_theta / r
psith= sp.diff(psi_r2,th)       # psi_theta / r^2
dpsi = 2*psi_r2+dt(psi_r2)      # (d_t psi)/r^2
# R = l d_t rho - (psi_th d_t rho - d_t psi rho_th)/r^2 - rho ; all divided by r
Rr = l*drho - (psith*drho - dpsi*rhoth) - rho_r
R1 = sp.integrate(sp.expand(sp.expand_trig(Rr*sp.sin(th))),(th,0,2*sp.pi))/sp.pi
L=l+(T-J)/2
N=f**2/4-(D+T)*f-f*g/2+(2*T+J-2*K)*g+((T-J)/2+K)*gd
print('R1/(pi r) - (L fd - N) =',sp.simplify(R1-(L*fd-N)))
R3 = sp.integrate(sp.expand(sp.expand_trig(Rr*sp.sin(3*th))),(th,0,2*sp.pi))/sp.pi
R5 = sp.integrate(sp.expand(sp.expand_trig(Rr*sp.sin(5*th))),(th,0,2*sp.pi))/sp.pi
print('R3/(pi r) =',sp.expand(R3))
print('R5/(pi r) =',sp.expand(R5))
# stream: -Lap psi = rho_x mode by mode. For psi_m = r^2 W sin m th: -Lap -> -(W'' +4W' +(4-m^2)W)
lap2 = -(dt(dt(Z2))+4*dt(Z2))
lap4 = -(dt(dt(Z4))+4*dt(Z4)+(4-16)*Z4)
print('mode2 check:',sp.simplify(lap2-(fd+gd+4*g)/2),' mode4 check:',sp.simplify(lap4-(gd-2*g)/2))
