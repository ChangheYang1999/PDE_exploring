# Checks for 3.78 v2: closed form (3) for h(0), axis relations w(0), h''(0), and the identity F = -mu C_p
# (smoothness of the inner canonical inverse (2) at z = 0), with A from the z^s coefficient. K = C_p = 1.
import mpmath as mp, sys
mp.mp.dps=30
def run(p):
    p=mp.mpf(p); K=1; Cp=1; c=1/p; D=c-1; mu=(p+1)/2; n=mu*p; s=p-1/mu
    lam=4*p**2*K/((p+1)**2*(1-p))
    a1=-p/2; a2=(1-p)/2; b1=p/(p+1); b2=mp.mpf(2)
    def ce(A1,A2,B1,B2):
        pre=mp.gamma(B1)*mp.gamma(B2)
        E=pre*mp.gamma(A2-A1)/(mp.gamma(A2)*mp.gamma(B1-A1)*mp.gamma(B2-A1))*lam**(-A1)
        O=pre*mp.gamma(A1-A2)/(mp.gamma(A1)*mp.gamma(B1-A2)*mp.gamma(B2-A2))*lam**(-A2)
        return E,O
    E1,O1=ce(a1,a2,b1,b2); E2,O2=ce(a1-b1+1,a2-b1+1,2-b1,3-b1)
    kap=p*K*Cp/D; r=O1/O2
    h=lambda z: kap*(z**p*mp.hyp2f2(a1,a2,b1,b2,-lam/z**2)-r*z**s*mp.hyp2f2(a1-b1+1,a2-b1+1,2-b1,3-b1,-lam/z**2))
    h0=kap*(E1-r*E2)
    cf=kap*mp.gamma((1-p)*(p+2)/(2*(p+1)))*mp.gamma((1+p)/2)*lam**(p/2)/(mp.sqrt(mp.pi)*mp.gamma(2+p/2)*mp.gamma(1/(p+1)))
    # h''(0) from relations, against a fit of h near 0
    w0=(1-n)*h0/(p**2*K); h2=n*(1-n)*w0
    zs=[mp.mpf(k)/100 for k in (2,3,4,5,6)]
    M=mp.matrix([[1,z,z**2,z**3,z**4] for z in zs]); sol=mp.lu_solve(M,mp.matrix([h(z) for z in zs]))
    # A from z^s coefficient of h, and A by quadrature (1/mu) int_0^inf t^{-s-1} h''
    A=(c*(1-mu)/(p*K))*(p+2-s)*(-kap*r)
    hpp=lambda t: mp.diff(h,t,2)
    Aq=mp.quad(lambda t: t**(-s-1)*hpp(t),[mp.mpf('0.05'),1,4,mp.inf])/mu
    # small-t part by the Taylor series of h at 0 (even, coefficients from the fit are too crude: use relation + fit)
    Aq+= (h2*mp.mpf('0.05')**(-s)/(-s))/mu
    # F: z^p G(z) - h''(0)/p at small z, G(z) = int_z^inf t^{-p-1} h''
    Fs=[]
    for z in (mp.mpf('0.1'),mp.mpf('0.07'),mp.mpf('0.05')):
        G=mp.quad(lambda t: t**(-p-1)*hpp(t),[z,1,4,mp.inf])
        Fs.append((z,(z**p*G-h2/p)/z**p))
    return dict(p=p,h0=h0,cf=cf,fit0=sol[0],fit1=sol[1],fit2=2*sol[2],h2=h2,A=A,Aq=Aq,Fs=Fs,mu=mu)
for p in sys.argv[1:]:
    d=run(p)
    print('p',mp.nstr(d['p'],8),'h0 conn',mp.nstr(d['h0'],12),'closed',mp.nstr(d['cf'],12),'fit',mp.nstr(d['fit0'],10),
          'odd fit',mp.nstr(d['fit1'],3),"h''(0) rel",mp.nstr(d['h2'],10),'fit',mp.nstr(d['fit2'],8))
    print('   A from z^s coeff',mp.nstr(d['A'],10),' quad (approx small-t part)',mp.nstr(d['Aq'],8),
          ' F/mu at z=.1,.07,.05:',[mp.nstr(F/d['mu'],6) for z,F in d['Fs']],' (expect -1 up to O(z^{2-p}))',flush=True)
