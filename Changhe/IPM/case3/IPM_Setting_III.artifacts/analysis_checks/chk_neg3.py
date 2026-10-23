# s = -1: (i) closed form of c_O; (ii) h_1 = z^p 2F2(a1,a2;b1,b2;lam/z^2) has the exponential coefficient
# Gamma(b1)Gamma(b2)/(Gamma(a1)Gamma(a2)) (DLMF 16.11.7, kappa = 1): ratio 2F2(X)/(e^X X^{a1+a2-b1-b2}) -> that constant.
import mpmath as mp
mp.mp.dps=40
for p in [mp.mpf('0.1'),mp.mpf('0.25'),mp.sqrt(2)-1,mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('0.9')]:
    a1=-p/2; a2=(1-p)/2; b1=p/(p+1); b2=mp.mpf(2)
    cO=mp.gamma(a2)*mp.gamma(1-b1+a2)*mp.gamma(a1-a2)/mp.gamma(b2-a2)
    cOc=-2*mp.sqrt(mp.pi)*mp.gamma((1-p)/2)*mp.gamma((3-p**2)/(2*(p+1)))/mp.gamma((3+p)/2)
    cE=mp.gamma(a1)*mp.gamma(1-b1+a1)*mp.gamma(a2-a1)/mp.gamma(b2-a1)
    ex=mp.gamma(b1)*mp.gamma(b2)/(mp.gamma(a1)*mp.gamma(a2))
    rat=[mp.hyp2f2(a1,a2,b1,b2,X)/(mp.e**X*X**(a1+a2-b1-b2)) for X in (mp.mpf(100),mp.mpf(400),mp.mpf(1600))]
    # second solution h_2 (z^s branch): X^{1-b1} 2F2(a1-b1+1,a2-b1+1;2-b1,b2-b1+1;X), exponential coefficient
    a1p=a1-b1+1; a2p=a2-b1+1; b1p=2-b1; b2p=b2-b1+1
    ex2=mp.gamma(b1p)*mp.gamma(b2p)/(mp.gamma(a1p)*mp.gamma(a2p))
    print('p=%s cO=%s closed=%s rel=%s cE=%s'%(mp.nstr(p,6),mp.nstr(cO,12),mp.nstr(cOc,12),mp.nstr((cO-cOc)/cO,3),mp.nstr(cE,10)))
    print('    exp coeff of 2F2: predicted %s, ratios at X=100,400,1600: %s ; exp coeff of h_2 series %s'%(mp.nstr(ex,10),', '.join(mp.nstr(r,10) for r in rat),mp.nstr(ex2,8)))
