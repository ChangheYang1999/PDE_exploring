"""No floating point: alternating Machin pi and directed integer square roots.
The Fourier constants are reconstructed from angular averages and radial
integration coefficients rather than the specialized Arb formulas.
"""
from fractions import Fraction as F
from math import isqrt,factorial

class Box:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi);assert self.lo<=self.hi
    @staticmethod
    def of(a):return a if isinstance(a,Box) else Box(a)
    def __add__(self,a):
        a=Box.of(a);return Box(self.lo+a.lo,self.hi+a.hi)
    __radd__=__add__
    def __neg__(self):return Box(-self.hi,-self.lo)
    def __sub__(self,a):return self+-Box.of(a)
    def __rsub__(self,a):return Box.of(a)+-self
    def __mul__(self,a):
        a=Box.of(a);z=[x*y for x in (self.lo,self.hi) for y in (a.lo,a.hi)];return Box(min(z),max(z))
    __rmul__=__mul__
    def inverse(self):
        assert not self.lo<=0<=self.hi;return Box(1/self.hi,1/self.lo)
    def __truediv__(self,a):return self*Box.of(a).inverse()
    def __rtruediv__(self,a):return Box.of(a)*self.inverse()
    def sqrt(self,bits=256):
        assert self.lo>=0
        def floor_root(q):
            scaled=(q.numerator<<(2*bits))//q.denominator
            l=isqrt(scaled);assert F(l*l,1<<(2*bits))<=q<F((l+1)**2,1<<(2*bits));return l
        l=floor_root(self.lo);u=floor_root(self.hi)
        return Box(F(l,1<<bits),F(u+1,1<<bits))
    def record(self):return {'lower_exact':str(self.lo),'upper_exact':str(self.hi)}

def atan_recip(d,n):
    assert d>1 and n>0
    terms=[F((-1)**j,(2*j+1)*d**(2*j+1)) for j in range(n+1)]
    value=sum(terms[:-1],F());next_value=value+terms[-1]
    assert all(abs(terms[j+1])<abs(terms[j]) for j in range(n))
    return Box(min(value,next_value),max(value,next_value))

def evaluate(parameters):
    p={k:F(v) for k,v in parameters['inputs'].items()};s=p['s']
    pi=16*atan_recip(5,80)-4*atan_recip(239,30)
    assert 3<pi.lo<pi.hi<F(22,7)
    v={'pi':pi}
    for name,j,a,b in [('CU',0,1,1),('Csigma',1,2,1),('Cy',1,0,1),('CH',2,1,0)]:
        avg=F(factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))
        radial=F(factorial(j))
        for l in range(1,j+2):radial/=s-l
        v[name]=(avg*radial/(4*pi)).sqrt()
    # Group constant perturbation and affine contributions separately.
    v['c0']=v['CU']+(p['xmax']/3)*v['Csigma']
    v['c1']=v['Csigma']+v['Csigma']/3
    v['b1']=(p['MV']/p['m0'])*v['c0']+v['c1']
    v['b2']=(p['MV']/p['m0'])*v['c0']+2*v['Csigma']
    v['b3']=(p['Mrho']/p['m0'])*v['c0']
    v.update({'B'+str(j):p['H']*v['b'+str(j)] for j in (1,2,3)})
    v['e0']=p['H']*v['c0'];v['e1']=p['H']*v['c1'];v['e3']=p['H']*v['Cy']
    v['B3_density']=p['H']*(v['b3']+v['Cy']);v['m2']=p['H']*v['CH']
    v['d_bound']=(p['H']/p['m0'])*v['c0'];v['mR_lower']=Box(p['R']*p['m0'])
    v['delta_lower']=p['R0']/3-v['d_bound']/3
    v['box1_radius']=p['box1']/v['b1']
    v['kappa']=Box(1+F(10,2)+(F(1,2)-s)*F(101,100))
    v['source_multiplier']=Box(3*s+9*(s+F(1,2)))
    v['E']=p['delta_max']*((3*s+9*(s+F(1,2)))*(p['MV']+v['m2'])+3*p['Mrho'])
    v['K1']=(v['kappa']-v['E']).inverse()
    v['exclusion_lhs']=p['H_exclusion']*v['b1']
    v['exclusion_radius']=(p['defect_lower']-p['defect_error'])/v['b1']
    v['exclusion_e3']=p['H_exclusion']*v['Cy']
    v['exclusion_gradient_lower']=p['g_center']-p['g_error']-p['Mrho']*p['R0']-v['exclusion_e3']
    return {name:x.record() for name,x in v.items()}
