"""Exact rational Cartesian prefix for one automatically compatible harmonic."""
from laurent_log_audit import L,Q,Poly,parse

def coefficient(a,m):
    assert len(a.a)<=1
    return 2*a.a[0][a.M+m] if a.a and a.M+m>=0 else Q(0)

def poisson(a):
    forcing=a.X();degree=a.q+1;out=[]
    for index,v in enumerate(forcing.a[0].coeffs() if forcing.a else []):
        mode=index-forcing.M;den=mode*mode-degree*degree
        if den:out.append(v/den)
        else:assert not v;out.append(Q(0))
    g=L(degree,forcing.M,[Poly(out)])
    assert (g.X().X().scale(-1)+g.Y().Y()-forcing).zero()
    return g

class ExactSingle:
    def __init__(self,h,period):
        self.h=h;self.period=period;self.mode=period+2*h-2;self.B=self.mode+1
        self.delta=Q(2*h,period);self.d=self.delta/(1-self.delta)
        self.F={};self.G={};self.FX={};self.FY={};self.GX={};self.GY={}
    def p(self,n):return 1-n*self.delta
    def setf(self,n,f):self.F[n]=f;self.FX[n]=f.X();self.FY[n]=f.Y()
    def setg(self,n,g):self.G[n]=g;self.GX[n]=g.X();self.GY[n]=g.Y()
    def density(self,n):
        total=L(self.p(n),0,[])
        for i in range(1,n):
            j=n-i;total=total+self.GX[i]*self.FY[j]-self.GY[i]*self.FX[j]
        return total.scale(1/((n-1)*self.d))
    def initialize(self):
        self.setf(1,parse(self.p(1),{str(self.mode):['1']}));self.setg(1,poisson(self.F[1]))
        for n in range(2,self.period+1):self.setf(n,self.density(n));self.setg(n,poisson(self.F[n]))
        assert coefficient(self.F[self.period],2*self.h-3)==0
