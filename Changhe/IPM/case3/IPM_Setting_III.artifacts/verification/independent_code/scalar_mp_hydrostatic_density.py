"""Scalar density and independent numerical Cartesian differentiation in mp."""
import mpmath as mp

class ScalarMPDensity:
    def __init__(self,coeff,L,P,basis='cheb',tk=None):
        self.coeff=[[mp.mpf(float(a))for a in row]for row in coeff]
        self.L=mp.mpf(float(L));self.P=mp.mpf(float(P));self.basis=basis
        self.tk=None if tk is None else[mp.mpf(float(a))for a in tk]
        assert self.L>0 and self.P>1 and self.basis in ['cheb','local']
    @staticmethod
    def cheb(row,z):
        b,c=mp.mpf(0),mp.mpf(0)
        for u in reversed(row[1:]):b,c=u+2*z*b-c,b
        return row[0]+z*b-c
    def weight(self,r2):
        if not r2:return mp.mpf(1)
        A=r2/self.L**2;P=self.P;lo=mp.mpf(0);hi=mp.mpf(1);w=min(mp.mpf('.9'),(1/A)**(1/(2*P))/2)
        tol=64*mp.eps
        for _ in range(2000):
            power=A*(2*w)**(2*P);f=w+power-1
            if abs(f)<=tol*(1+abs(w)+abs(power)):return w
            if f>0:hi=w
            else:lo=w
            next_w=w-f/(1+2*P*power/w)
            if not lo<next_w<hi:next_w=(lo+hi)/2
            if next_w==w:raise ArithmeticError('MP Newton stagnated before residual tolerance')
            w=next_w
        raise ArithmeticError('MP scalar compact map did not converge')
    def density(self,x,y):
        x=mp.mpf(x);y=mp.mpf(y);r2=x*x+y*y
        if not r2:return mp.mpf(0)
        w=self.weight(r2);s=1-w;t=1-2*w;z=mp.mpc(x,y)**2/r2;power=mp.mpc(1);s_power=mp.mpf(1);total=mp.mpf(0)
        for k,row in enumerate(self.coeff):
            arg=(2*t-1-self.tk[k])/(1-self.tk[k])if self.basis=='local'else t
            total+=s_power*self.cheb(row,arg)*mp.re(power)
            power*=z;s_power*=s
        return y*w*total
    def jet(self,x,y):
        x=mp.mpf(x);y=mp.mpf(y)
        return [self.density(x,y),mp.diff(lambda a:self.density(a,y),x,addprec=40),mp.diff(lambda b:self.density(x,b),y,addprec=40),mp.diff(lambda a:self.density(a,y),x,2,addprec=40)]
