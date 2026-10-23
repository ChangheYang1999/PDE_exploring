"""Independent high-precision scalar compact map and analytic Q derivative."""
import mpmath as mp

class MPQDensity:
    def __init__(self,coeff,L,kappa,ell):
        # Python floats convert to their exact binary value at the active precision.
        self.coeff=[[mp.mpf(float(v)) for v in cc] for cc in coeff]
        self.L=mp.mpf(float(L));self.kappa=mp.mpf(float(kappa));self.ell=mp.mpf(float(ell))
    def coords(self,r):
        target=mp.log(r/self.L);k=self.kappa;eps=256*mp.eps*(1+abs(target)+k)
        if target<=-mp.log(2)/2:
            lo=mp.mpf(0);hi=mp.mpf('.5');q=min(mp.mpf('.49'),mp.exp(2*(target+k*mp.log(2))))
            for unused in range(1000):
                f=mp.log(q)/2-k*mp.log(2*(1-q))-target
                if abs(f)<=eps:return q,1-q
                if f>0:hi=q
                else:lo=q
                new=q-f/(1/(2*q)+k/(1-q))
                if not lo<new<hi:new=(lo+hi)/2
                if new==q:return q,1-q
                q=new
        else:
            lo=mp.mpf(0);hi=mp.mpf('.5');q=min(mp.mpf('.499'),mp.exp(-target/k)/2)
            for unused in range(1000):
                f=k*mp.log(2*q)-mp.log1p(-q)/2+target
                if abs(f)<=eps:return 1-q,q
                if f>0:hi=q
                else:lo=q
                new=q-f/(k/q+1/(2*(1-q)))
                if not lo<new<hi:new=(lo+hi)/2
                if new==q:return 1-q,q
                q=new
        raise ArithmeticError('MP compact map failed')
    @staticmethod
    def clenshaw(cc,t):
        b1=b2=d1=d2=mp.mpf(0)
        for c in cc[:0:-1]:
            b0=c+2*t*b1-b2;d0=2*b1+2*t*d1-d2
            b2,b1=b1,b0;d2,d1=d1,d0
        return cc[0]+t*b1-b2,b1+t*d1-d2
    def at(self,r,theta):
        s,w=self.coords(r);t=2*s-1 if s<mp.mpf('.5') else 1-2*w
        f=fs=ft=mp.mpf(0)
        for j,cc in enumerate(self.coeff):
            val,der=self.clenshaw(cc,t);cs=mp.cos(2*j*theta);sn=mp.sin(2*j*theta);power=s**j
            f+=power*val*cs
            fs+=(j*s**(j-1)*val+2*power*der if j else 2*der)*cs
            ft-=2*j*power*val*sn
        sd=2*s*w/(w+2*self.kappa*s);sn=mp.sin(theta);cs=mp.cos(theta)
        value=w*sn*f;rad=sn*(w*f+sd*(-f+w*fs));tan=w*(cs*f+sn*ft)
        return value,cs*rad-sn*tan,sn*rad+cs*tan
