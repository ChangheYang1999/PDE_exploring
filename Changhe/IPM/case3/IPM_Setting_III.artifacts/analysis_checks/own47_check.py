import sympy as sp
x,y,D=sp.symbols('x y D',positive=True)
# symbolic check with a closed-form-free route: verify identities numerically
import mpmath as mp
mp.mp.dps=30
def fam(Dv):
    ell=1+Dv; eta=Dv/(1+Dv); a=4*Dv
    f=lambda r:(1+r*r)**(-eta/2)
    H=lambda r: mp.quad(lambda t:t**3*f(r*t),[0,1])
    rho=lambda X,Y:a*Y*f(mp.sqrt(X*X+Y*Y))
    psi=lambda X,Y:-a*X*Y*H(mp.sqrt(X*X+Y*Y))
    return ell,eta,a,rho,psi
worst=0
for Dv in [mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf(1)]:
    ell,eta,a,rho,psi=fam(Dv)
    for (X,Y) in [(0.3,0.7),(2,1),(5,-3),(0.01,0.02),(10,10),(1,0.001),(0,50),(30,1)]:
        X=mp.mpf(X);Y=mp.mpf(Y)
        px=mp.diff(lambda s:psi(s,Y),X); py=mp.diff(lambda s:psi(X,s),Y)
        U1=-py; U2=px
        rx=mp.diff(lambda s:rho(s,Y),X); ry=mp.diff(lambda s:rho(X,s),Y)
        R=(ell*X+U1)*rx+(ell*Y+U2)*ry-rho(X,Y)
        lap=mp.diff(lambda s:psi(s,Y),X,2)+mp.diff(lambda s:psi(X,s),Y,2)
        pde=-lap-rx
        q=abs(R/rho(X,Y))/Dv
        worst=max(worst,q)
        print(float(Dv),float(X),float(Y),'R/(rho D)=%.4f'%float(R/rho(X,Y)/Dv),'poisson err %.2e'%float(abs(pde)))
    ell,eta,a,rho,psi=fam(Dv)
    pxy=mp.diff(lambda s:mp.diff(lambda t:psi(s,t),mp.mpf(0)),mp.mpf(0))
print('max |R/rho|/D =',float(worst))
