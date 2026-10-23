# Hand-check helpers for referee strat3 (lead). Symbolic checks of the formulas used in 3.74.
import sympy as sp
x,y,k,e,al,be,D,K,kap1,kap2,s,t=sp.symbols('x y kappa eta alpha beta D K kappa1 kappa2 s t',real=True)
p=sp.symbols('p',positive=True)
# (1) Fourier form of u_xx = (E+1) u_yy on a Gaussian-moment test: check on u = monomials via symbol identity
# Use F(x d_x f) = -(1 + k d_k) fhat in each variable; verify operator identity on a generic fhat
f=sp.Function('f')(k,e)
Ehat=lambda F: -(2*F + k*sp.diff(F,k) + e*sp.diff(F,e))
lhs=-k**2*f                     # F(u_xx)
uyy=-e**2*f                     # F(u_yy)
rhs=Ehat(uyy)+uyy               # F((E+1)u_yy)
print('fourier eq residual:',sp.simplify(rhs-lhs - (e**2*(3*f+k*sp.diff(f,k)+e*sp.diff(f,e))+k**2*f)))
# (2) (9): vhat = |beta|^{-3-alpha^2} B(alpha) with kappa = alpha*beta, eta = beta (beta>0)
B=sp.Function('B')
b=sp.symbols('b',positive=True)
vh=b**(-3-al**2)*B(al)
# Euler operator k d_k + e d_e in (alpha,beta) coordinates is beta d_beta
expr=b**2*(3*vh+b*sp.diff(vh,b))+(al*b)**2*vh
print('(9) residual:',sp.simplify(expr))
# (3) Q_* and axis formulas for f_p = r^p Theta
X=sp.symbols('X',positive=True)
F=sp.Function('F')
fp=X**p*F(y/X)
fxx=sp.diff(fp,X,2)
Qs=sp.simplify((fxx*X**(2-p)).subs(y,s*X))
target=p*(p-1)*F(s)-2*(p-1)*s*sp.diff(F(s),s)+s**2*sp.diff(F(s),s,2)
print('Q_* residual:',sp.simplify(sp.expand(Qs-target.subs(s,s))))
# axis: T2 of B t^{p-2}: int_0^y t B t^{p-2} + y int_y^inf B t^{p-2}
Bc=sp.symbols('Bc')
yy=sp.symbols('yy',positive=True)
pp=sp.Rational(1,3)
T2=sp.integrate(t*Bc*t**(pp-2),(t,0,yy))+yy*sp.integrate(Bc*t**(pp-2),(t,yy,sp.oo))
print('axis T2 at p=1/3:',sp.simplify(T2-Bc*yy**pp/(pp*(1-pp))))
# consistency: f_{2p-1}(0,y) = KB y^{2p-1}/((1-p)D) equals the axis-ODE correction with c^2 p (1-p) = D
c=1/p
print('c^2 p(1-p) - D:',sp.simplify(c**2*p*(1-p)-(c-1)))
# (4) outer expansion K(D) y^{1/(1+D)}
Kd=1+kap1*D+kap2*D**2
yp=sp.symbols('yp',positive=True)
ser=sp.series(Kd*yp**(1/(1+D)),D,0,3).removeO()
u1=sp.simplify(ser.coeff(D,1)); w2=sp.simplify(ser.coeff(D,2))
print('u:',sp.simplify(u1-yp*(kap1-sp.log(yp))),' w:',sp.simplify(sp.expand(w2-yp*(kap2+(1-kap1)*sp.log(yp)+sp.log(yp)**2/2))))
# (5) d/dc r^{1/c} = -p^2 r^p log r
r,cc=sp.symbols('r cc',positive=True)
print('dc:',sp.simplify(sp.diff(r**(1/cc),cc)-(-(1/cc)**2*r**(1/cc)*sp.log(r))))
# (6) beta_n: c beta_n - 1 = -(n-1) D
n=sp.symbols('n')
print('beta_n:',sp.simplify(c*(n*p-(n-1))-1+(n-1)*(c-1)))
# (7) J identity Liouville check numerically on a model field W = c X + small div-free field
import numpy as np
from scipy.integrate import solve_ivp
cN=2.0; gam=0.5
def W(X):
    x_,y_=X; r2=1+x_*x_+y_*y_
    # psi = x y r2^{(gam-1)/2}*0.7 + 0.3*sin(x) y/(r2)^{0.2}: smooth, sublinear velocity (div-free part)
    # velocity (-psi_y, psi_x) by finite differences of psi
    def psi(a,b):
        rr=1+a*a+b*b
        return 0.7*a*b*rr**((gam-1)/2)+0.3*np.sin(a)*b*rr**(-0.2)
    h=1e-6
    py=(psi(x_,y_+h)-psi(x_,y_-h))/(2*h); px=(psi(x_+h,y_)-psi(x_-h,y_))/(2*h)
    return np.array([cN*x_-py, cN*y_+px])
def rhs_r(rr,z):  # z=(theta, tau): d theta/dr = q/(r w), d tau/dr = 1/w
    th,ta=z; X=rr*np.array([np.cos(th),np.sin(th)]); Wv=W(X)
    w=Wv@np.array([np.cos(th),np.sin(th)]); q=Wv@np.array([-np.sin(th),np.cos(th)])
    return [q/(rr*w),1/w]
R=5.0; R1=60.0
for om in [0.3,1.0,2.2]:
    d=1e-5; out=[]
    for o in [om-d,om,om+d]:
        sol=solve_ivp(rhs_r,[R,R1],[o,0.0],rtol=1e-11,atol=1e-12); out.append(sol.y[:,-1])
    J=(out[2][0]-out[0][0])/(2*d); th,ta=out[1]
    X1=R1*np.array([np.cos(th),np.sin(th)]); w1=W(X1)@np.array([np.cos(th),np.sin(th)])
    X0=R*np.array([np.cos(om),np.sin(om)]); w0=W(X0)@np.array([np.cos(om),np.sin(om)])
    print('J check om=%.1f: lhs %.8e rhs %.8e'%(om,R1*w1*J,R*w0*np.exp(2*cN*ta)))
