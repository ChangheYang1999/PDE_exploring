# compare the aud26 reflection form of h_*(0) with closed form (3) (K = 1, normalized by pKC_p/D)
from mpmath import mp,mpf,gamma,sin,cos,pi,sqrt
mp.dps=40
for p in [mpf('0.1'),mpf('0.25'),sqrt(2)-1,mpf('0.5'),mpf('0.6'),mpf('0.75'),mpf('0.9')]:
    K=1; lam=4*p**2*K/((p+1)**2*(1-p))
    a1=-p/2; a2=(1-p)/2; b1=p/(p+1); b2=mpf(2)
    E1=gamma(b1)*gamma(b2)*gamma(a2-a1)*lam**(-a1)/(gamma(a2)*gamma(b1-a1)*gamma(b2-a1))
    refl=E1*sin(pi*b1)/(cos(pi*a1)*sin(pi*(b1-a1)))
    cf=gamma((1-p)*(p+2)/(2*(p+1)))*gamma((1+p)/2)*lam**(p/2)/(sqrt(pi)*gamma(2+p/2)*gamma(1/(p+1)))
    print(mp.nstr(p,8), mp.nstr(refl,15), mp.nstr(cf,15), mp.nstr(abs(refl/cf-1),3))
