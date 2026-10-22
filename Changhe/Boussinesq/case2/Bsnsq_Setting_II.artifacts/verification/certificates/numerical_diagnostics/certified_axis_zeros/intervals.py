"""Outward fixed-denominator integer intervals, proved in PROOF.md sections3–4."""
from math import isqrt

class Arithmetic:
    def __init__(self,bits):
        assert type(bits) is int and bits>=2
        self.bits=bits;self.B=1<<bits
    @staticmethod
    def floor(n,d):
        if d==0:raise ZeroDivisionError
        if d<0:n,d=-n,-d
        return n//d
    @classmethod
    def ceil(cls,n,d):return -cls.floor(-n,d)
    def rational(self,n,d=1):
        if d==0:raise ZeroDivisionError
        if d<0:n,d=-n,-d
        return self.floor(self.B*n,d),self.ceil(self.B*n,d)
    @staticmethod
    def add(a,b):return a[0]+b[0],a[1]+b[1]
    @staticmethod
    def neg(a):return -a[1],-a[0]
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        corners=[x*y for x in a for y in b]
        return min(corners)//self.B,self.ceil(max(corners),self.B)
    def inv(self,a):
        if a[0]<=0<=a[1]:raise ZeroDivisionError('Interval contains zero')
        return self.floor(self.B*self.B,a[1]),self.ceil(self.B*self.B,a[0])
    def div(self,a,b):return self.mul(a,self.inv(b))
    def pow(self,a,n):
        assert type(n) is int
        if n<0:return self.pow(self.inv(a),-n)
        result=self.rational(1)
        while n:
            if n&1:result=self.mul(result,a)
            n>>=1
            if n:a=self.mul(a,a)
        return result
    def sqrt(self,a):
        if a[0]<0:raise ValueError('Negative square-root interval')
        lo=isqrt(a[0]*self.B);hi=isqrt(a[1]*self.B)
        if hi*hi<a[1]*self.B:hi+=1
        return lo,hi
    def horner(self,coefs,t):
        z=self.rational(0)
        for c in reversed(coefs):z=self.add(self.mul(z,t),c)
        return z
    def log(self,t,n):
        if not(0<t[0]<=t[1]<self.B):raise ValueError('Require 0<t<1')
        if type(n) is not int or n<1:raise ValueError('Positive log truncation')
        one=self.rational(1);v=self.div(self.sub(one,t),self.add(one,t))
        if not(0<v[0]<=v[1]<self.B):raise ValueError('Bad v enclosure')
        v2=self.mul(v,v);power=v;total=self.rational(0)
        for j in range(n):
            total=self.add(total,self.mul(self.rational(2,2*j+1),power))
            power=self.mul(power,v2)
        tail=self.div(self.mul(self.rational(2,2*n+1),power),self.sub(one,v2))
        if tail[0]<0:raise ArithmeticError('Negative geometric remainder')
        return self.neg(self.add(total,(0,tail[1])))
    def store(self,a):return {'lower_integer':str(a[0]),'upper_integer':str(a[1]),'denominator_power_two':self.bits}
    def restore(self,a):
        assert a['denominator_power_two']==self.bits
        l,u=int(a['lower_integer']),int(a['upper_integer'])
        assert l<=u
        return l,u
    @staticmethod
    def excludes_zero(a):return a[1]<0 or a[0]>0


def axis_enclosures(comp,t,ar,log_terms):
    """H,mu,nu,F,radius, from integer polynomial JSON and one t interval."""
    b=int(comp['beta']);D=int(comp['denominator'])
    one=ar.rational(1);q=ar.sub(one,ar.pow(t,2*b))
    assert 0<q[0]<=q[1]<ar.B
    logt=ar.log(t,log_terms)
    sum_xy=ar.rational(0);sum_mu=ar.rational(0)
    mode_bounds=[]
    for mode in comp['modes']:
        k,L,J=(int(mode[key])for key in ('k','L','J'))
        P,Q=([int(x)for x in mode[key]]for key in ('P','Q'))
        u,v=map(int,mode['moment'])
        icoef=[ar.rational(-x,j-L)if j!=L else ar.rational(0)for j,x in enumerate(P)]
        tl=ar.pow(t,L)
        ib=ar.add(ar.horner(icoef,t),ar.mul(tl,ar.rational(u,v)))
        if L<len(P):ib=ar.sub(ib,ar.mul(ar.mul(ar.rational(P[L]),tl),logt))
        ob=ar.horner([ar.rational(x,j+J)for j,x in enumerate(Q)],t)
        X=ar.mul(ar.mul(ar.pow(q,-k),ib),ar.rational(1,4*D))
        Y=ar.mul(ar.mul(ar.pow(q,k),ob),ar.rational(1,4*D))
        sum_xy=ar.add(sum_xy,ar.add(X,Y))
        sum_mu=ar.add(sum_mu,ar.add(ar.mul(ar.rational(2*k+1,2),X),ar.mul(ar.rational(1-2*k,2),Y)))
        mode_bounds.append({'k':k,'X':ar.store(X),'Y':ar.store(Y)})
    h=ar.sub(ar.rational(b),ar.mul(ar.div(t,ar.mul(ar.rational(2),q)),sum_xy))
    mu=ar.add(ar.rational(b),ar.mul(ar.div(t,q),sum_mu))
    aa=ar.rational(0)
    for m,coefs in enumerate(comp['A']):
        a=ar.horner([ar.rational(int(x),D)for x in coefs],t)
        aa=ar.add(aa,ar.mul(ar.pow(q,m),a))
    f=ar.mul(ar.mul(q,ar.pow(t,2)),aa)
    radius=ar.div(ar.sqrt(q),ar.pow(t,b))
    return {'H':h,'mu':mu,'nu':ar.sub(ar.rational(2*b),mu),'F':f,'radius':radius},mode_bounds
