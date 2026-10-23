# Lead check of ver result105: for rho/r = f sin th + g sin 3th (modes 1, 3 only, the ansatz of 3.61),
# the seventh sine projection is R_7/(pi r) = K (gdot + 4 g) - 3 g^2/4 (t = log r).
import sympy as sp
th,c=sp.symbols('theta c',real=True)
f,fd,fdd,g,gd,gdd,T,J,K=sp.symbols('f fd fdd g gd gdd T J K',real=True)
rules={f:fd,fd:fdd,g:gd,gd:gdd,T:-g,J:f-4*J,K:g-6*K}
def dt(e): return sp.expand(sum(sp.diff(e,v)*rules[v] for v in rules))
u=(T-J)/2; v=-K/2
rho_r=f*sp.sin(th)+g*sp.sin(3*th); psi_r2=u*sp.sin(2*th)+v*sp.sin(4*th)
drho=rho_r+dt(rho_r); rhoth=sp.diff(rho_r,th); psith=sp.diff(psi_r2,th); dpsi=2*psi_r2+dt(psi_r2)
Rr=c*drho-(psith*drho-dpsi*rhoth)-rho_r
def proj(m): return sp.expand(sp.integrate(sp.expand(sp.expand_trig(Rr*sp.sin(m*th))),(th,0,2*sp.pi))/sp.pi)
for m in [5,7,9]:
    print(m,sp.factor(proj(m)))
print('R7 claim diff',sp.simplify(proj(7)-(K*(gd+4*g)-sp.Rational(3,4)*g**2)))
