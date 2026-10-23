# closed form (3) of h(0) against the connection-coefficient expression, 40 digits, K = C_p = 1
import mpmath as mp
mp.mp.dps=40
for ps in ('0.1','0.25','0.4142135623730950488016887242096980785697','0.5','0.6','0.75','0.9'):
    p=mp.mpf(ps); K=1; c=1/p; D=c-1; lam=4*p**2*K/((p+1)**2*(1-p))
    a1=-p/2; a2=(1-p)/2; b1=p/(p+1); b2=mp.mpf(2)
    def ce(A1,A2,B1,B2):
        pre=mp.gamma(B1)*mp.gamma(B2)
        return (pre*mp.gamma(A2-A1)/(mp.gamma(A2)*mp.gamma(B1-A1)*mp.gamma(B2-A1))*lam**(-A1),
                pre*mp.gamma(A1-A2)/(mp.gamma(A1)*mp.gamma(B1-A2)*mp.gamma(B2-A2))*lam**(-A2))
    E1,O1=ce(a1,a2,b1,b2); E2,O2=ce(a1-b1+1,a2-b1+1,2-b1,3-b1)
    h0=(p*K/D)*(E1-O1/O2*E2)
    cf=(p*K/D)*mp.gamma((1-p)*(p+2)/(2*(p+1)))*mp.gamma((1+p)/2)*lam**(p/2)/(mp.sqrt(mp.pi)*mp.gamma(2+p/2)*mp.gamma(1/(p+1)))
    print(ps[:6],mp.nstr(h0,15),'rel diff',mp.nstr(abs(h0-cf)/abs(cf),3),'O2',mp.nstr(O2,6))
