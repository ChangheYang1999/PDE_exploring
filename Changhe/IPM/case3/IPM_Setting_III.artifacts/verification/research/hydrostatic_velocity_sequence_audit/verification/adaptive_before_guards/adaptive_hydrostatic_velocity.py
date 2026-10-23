"""Independent adaptive quadrature for the complete epsilon=0 vertical inverse.

Uses scalar Gauss-Kronrod on physical panels and the entire transformed tail.
No code from the producer or from the fixed Gauss inverse is imported.
"""
import math
import numpy as np
from scipy.integrate import quad

class AdaptiveVerticalVelocity:
    def __init__(self,jet,p,split=37.0,epsabs=2e-11,epsrel=2e-11,limit=150):
        if not 0<p<1: raise ValueError('Requires 0<p<1')
        if split<1: raise ValueError('Requires split>=1')
        self.jet=jet
        self.p=float(p)
        self.split=float(split)
        self.epsabs=float(epsabs)
        self.epsrel=float(epsrel)
        self.limit=int(limit)

    def at(self,x,y):
        xx=abs(float(x)); yy=abs(float(y))
        sx=-1 if x<0 else 1
        sy=-1 if y<0 else 1
        R=self.split*max(xx,yy,1.0)
        power=1/(1-self.p)
        messages=[];details=[]
        def integrate(f,a,b,label):
            if a==b: return 0.0,0.0
            q=quad(f,a,b,epsabs=self.epsabs,epsrel=self.epsrel,limit=self.limit,full_output=1)
            value,error,info=q[:3]
            if len(q)>3: messages.append(dict(label=label,message=str(q[3])))
            details.append(dict(label=label,a=a,b=b,value=float(value),error=float(error),neval=int(info['neval'])))
            return float(value),float(error)
        def finite(component,a,b,moment,label):
            if a==b: return 0.0,0.0
            cuts=[a,b];point=.02
            while point<b:
                if point>a: cuts.append(point)
                point*=3
            cuts=sorted(set(cuts));values=[];errors=[]
            def f(t):
                val=float(self.jet(xx,np.array([t]))[0,component])
                return t*val if moment else val
            for j,(lo,hi) in enumerate(zip(cuts,cuts[1:])):
                value,error=integrate(f,lo,hi,label+str(j))
                values.append(value);errors.append(error)
            return math.fsum(values),math.fsum(errors)
        def tail(component,label):
            def f(u):
                t=R/u**power
                return float(self.jet(xx,np.array([t]))[0,component])*power*R*u**(-power-1)
            return integrate(f,0.0,1.0,label)
        if xx==0:
            v1=e1=0.0
        else:
            finite_x,ef=finite(1,yy,R,False,'outer gx ')
            tail_x,et=tail(1,'tail gx')
            v1=-sx*(finite_x+tail_x);e1=ef+et
        if yy==0:
            v2=e2=0.0
        else:
            inner_xx,ei=finite(3,0.0,yy,True,'inner t gxx ')
            outer_xx,eo=finite(3,yy,R,False,'outer gxx ')
            tail_xx,et=tail(3,'tail gxx')
            v2=sy*(inner_xx+yy*(outer_xx+tail_xx));e2=ei+yy*(eo+et)
        return dict(V=[v1,v2],estimated_error=[e1,e2],messages=messages,details=details,split=R,power=power)
