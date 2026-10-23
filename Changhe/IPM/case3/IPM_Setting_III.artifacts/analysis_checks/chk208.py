# lead hand check of checker 208: closed-form C_p for traces Theta = pref sin(th) B(cos^2 th)
import mpmath as mp
mp.mp.dps=40
def closed(p,a,pref=1):
    Jp=mp.sqrt(mp.pi)*mp.gamma(1-p/2)/(2*mp.gamma((3-p)/2))
    I=[(1-p)*Jp/(p*(p+2)),-Jp/p,Jp/(3-p)]
    while len(I)<len(a): j=len(I)-1; I.append(I[j]*(2*j-p-2)/(2*j+1-p))
    return (p+1)*(p+2)*pref*sum(a[j]*I[j] for j in range(len(a)))
def direct(p,a,pref=1):
    # C_p = int_0^inf s (q - Q s^(p-2)) ds, q = p(p-1)F - 2(p-1) s F' + s^2 F'' ; F via exact formula
    F=lambda s: pref*sum(a[j]*s*(1+s**2)**((p-1)/2-j) for j in range(len(a)))
    Q=pref*((p-1)*a[0]+2*a[1])
    def q(s):
        tot=0
        for j in range(len(a)):
            al=(p-1)/2-j; u=1+s**2
            f0=s*u**al; f1=u**al+2*al*s**2*u**(al-1)
            f2=2*al*s*u**(al-1)+4*al*s*u**(al-1)+4*al*(al-1)*s**3*u**(al-2)
            tot+=pref*a[j]*(p*(p-1)*f0-2*(p-1)*s*f1+s**2*f2)
        return tot
    f=lambda s: s*(q(s)-Q*s**(p-2))
    S=mp.mpf(10)**4
    d=lambda n: pref*sum(a[j]*mp.binomial((p-1)/2-j,n-j) for j in range(min(n,len(a)-1)+1))
    tail=sum(d(n)*2*n*(2*n-1)*S**(p+2-2*n)/(2*n-p-2) for n in range(2,12))
    return mp.quad(f,[0,1,10,100,1000,S])+tail
for p in (mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf(2)/3,mp.mpf('0.85')):
    for a in ([1,0.3,-0.2,0.1],[0.5,-1,2,0,0.7]):
        a=[mp.mpf(x) for x in a]
        c1=closed(p,a); c2=direct(p,a)
        print(float(p),mp.nstr(c1,15),mp.nstr(c2,15),mp.nstr(abs(c1-c2)/abs(c1),3))
