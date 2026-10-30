"""Exact rational interval audit, independent of T4's Arb arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
from datetime import datetime,timezone
import json,hashlib,time
BASE=Path(__file__).resolve().parents[1]
class I:
    def __init__(self,a,b=None):
        if isinstance(a,I):self.a,self.b=a.a,a.b;return
        self.a=Q(a);self.b=Q(a if b is None else b);assert self.a<=self.b
    def __add__(self,x):
        x=I(x);return I(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,x):return self+-I(x)
    def __rsub__(self,x):return I(x)+-self
    def __mul__(self,x):
        x=I(x);v=[self.a*x.a,self.a*x.b,self.b*x.a,self.b*x.b];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I(x);assert not x.a<=0<=x.b;return self*I(1/x.b,1/x.a)
    def __rtruediv__(self,x):return I(x)/self
    def __pow__(self,n):
        assert n>=0 and int(n)==n
        z=I(1)
        for _ in range(n):z=z*self
        return z
    def sqrt(self):
        assert self.a>=0;D=10**70
        low=isqrt(self.a.numerator*D*D//self.a.denominator)
        high=isqrt(self.b.numerator*D*D//self.b.denominator)+1
        return I(Q(low,D),Q(high,D))
    def record(self):return {'lower':str(self.a),'upper':str(self.b),'midpoint_float':float((self.a+self.b)/2),'width_float':float(self.b-self.a)}
def atan(x,N):
    x=Q(x);v=sum(((-1)**k*x**(2*k+1)/(2*k+1) for k in range(N)),Q(0));w=v+(-1)**N*x**(2*N+1)/(2*N+1)
    return I(min(v,w),max(v,w))
def run():
    start=time.monotonic();oldpath=BASE/'data/T4_rational_box.json';old=json.loads(oldpath.read_text())
    s=I(old['s']);r=list(map(I,old['box']));f=list(map(I,old['forcing_upper_bounds']))
    n=(r[0]**2+2*r[1]**2+r[2]**2).sqrt();nu=n/s.sqrt()
    A=I('127/50')+I('653/5')*s;B=I('9/5')*(1+44*s)
    H=I('19/5')-2*s;b=I('11/4')-3882*s-I('3/10')*nu
    a=I('9/10')-4290*s-I('13/10')*nu;P=I('1/2')-4708*s-(A+B)*nu
    q=476*s+nu;kappa=q/H;den=1-kappa/b.sqrt()
    Gb=(f[2]/b+f[3]/(H*b.sqrt()))/den;GH=f[3]/H+kappa*Gb
    Ga=(f[1]+(6+1360*s)*Gb)/a
    alpha=I('347/5')+5440*s+B*nu;beta=10+34816*s
    GP=(f[0]+alpha*Ga+beta*Gb)/P+(40/P).sqrt()*Ga
    gamma=[GP,Ga,Gb,GH];slacks=[u-v for u,v in zip(r,gamma)]
    pi=16*atan(Q(1,5),80)-4*atan(Q(1,239),20)
    d=n/(2*(pi*s*(1+s)).sqrt());ratio=d/(I('19/5')-d)
    assert all(x.a>0 for x in [H,b,a,P,den]+slacks)
    assert ratio.b<Q(3331,1000000)
    ell=I('5/2');assert (b-q/2-ell).a>0 and (H-1-q/2-ell).a>0
    M=(41+alpha**2/P)/a;L=(1+beta**2/P+(M*(6+1360*s))**2/2)/ell
    # Parse finite Arb display intervals using exact decimal rationals.
    def parse(text):
        z=text.strip('[]').split('+/-')
        if len(z)==1:return I(z[0].strip())
        mid,rad=map(lambda v:Q(v.strip()),z);return I(mid-rad,mid+rad)
    comparisons={}
    for key,vals,prior in [('Gamma',gamma,old['Gamma']),('slacks',slacks,old['positive_slacks']),('aux',[I(1),M,L,L],old['auxiliary_energy_weights_P_a_b_H'])]:
        overlaps=[max(v.a,parse(w).a)<=min(v.b,parse(w).b) for v,w in zip(vals,prior)]
        assert all(overlaps);comparisons[key]=overlaps
    for label,v in [('nu',nu),('low_contraction',ratio),('gradient_bound',d)]:
        w=parse(old[label]);assert max(v.a,w.a)<=min(v.b,w.b);comparisons[label]=True
    margins=dict(zip(['mH','m0','m1','m2','feedback_denominator'],[H,b,a,P,den]))
    for label,v in margins.items():
        w=parse(old['margins'][label]);assert max(v.a,w.a)<=min(v.b,w.b)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Exact rational interval arithmetic with integer square roots and Machin alternating-series pi enclosure',
         'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [oldpath,BASE/'data/T4_PROOF.md',Path(__file__)]},
         'margin_positive':True,'self_map_positive':True,'contraction_below_0_003331':True,
         'margins':{k:v.record() for k,v in margins.items()},'Gamma':[v.record() for v in gamma],
         'slacks':[v.record() for v in slacks],'contraction':ratio.record(),'gradient_bound':d.record(),
         'prior_overlap':comparisons,'elapsed_seconds':time.monotonic()-start}
    (BASE/'verification/rational_intervals.json').write_text(json.dumps(out,indent=2)+'\n')
    print('confirmed all scalar inequalities and overlaps',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
