"""Verifier-owned exact rational interval and complex disk arithmetic."""
from flint import fmpq


def rational(x):
 return x if isinstance(x,fmpq)else fmpq(x)


class Interval:
 __slots__=('lo','hi')
 def __init__(self,a=0,b=None):
  if isinstance(a,Interval):self.lo,self.hi=a.lo,a.hi;return
  self.lo=rational(a);self.hi=rational(a if b is None else b)
  if self.lo>self.hi:raise ValueError('reversed interval')
 def __add__(self,b):
  b=Interval(b);return Interval(self.lo+b.lo,self.hi+b.hi)
 __radd__=__add__
 def __neg__(self):return Interval(-self.hi,-self.lo)
 def __sub__(self,b):return self+-Interval(b)
 def __rsub__(self,b):return Interval(b)+-self
 def __mul__(self,b):
  b=Interval(b);p=[a*c for a in [self.lo,self.hi]for c in [b.lo,b.hi]]
  return Interval(min(p),max(p))
 __rmul__=__mul__
 def inverse(self):
  if self.lo<=0<=self.hi:raise ZeroDivisionError('interval denominator contains zero')
  return Interval(1/self.hi,1/self.lo)
 def __truediv__(self,b):return self*Interval(b).inverse()
 def __rtruediv__(self,b):return Interval(b)*self.inverse()
 def __pow__(self,n):
  if not isinstance(n,int):raise TypeError('integer exponent required')
  if n<0:return self.inverse()**(-n)
  out=Interval(1);p=self
  while n:
   if n%2:out=out*p
   p=p*p;n//=2
  return out
 def upper(self):return max(abs(self.lo),abs(self.hi))
 def lower(self):return 0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi))
 def contains(self,q):return self.lo<=q<=self.hi
 def __eq__(self,b):
  b=Interval(b);return self.lo==b.lo and self.hi==b.hi
 def saved(self):return [str(self.lo),str(self.hi)]


class Rectangle:
 __slots__=('re','im')
 def __init__(self,a=0,b=0):
  if isinstance(a,Rectangle):self.re,self.im=a.re,a.im;return
  self.re,self.im=Interval(a),Interval(b)
 def __add__(self,b):
  b=Rectangle(b);return Rectangle(self.re+b.re,self.im+b.im)
 __radd__=__add__
 def __neg__(self):return Rectangle(-self.re,-self.im)
 def __sub__(self,b):return self+-Rectangle(b)
 def __rsub__(self,b):return Rectangle(b)+-self
 def __mul__(self,b):
  b=Rectangle(b);return Rectangle(self.re*b.re-self.im*b.im,self.re*b.im+self.im*b.re)
 __rmul__=__mul__
 def upper(self):return self.re.upper()+self.im.upper()
 def lower(self):return max(self.re.lower(),self.im.lower())
 def saved(self):return [self.re.saved(),self.im.saved()]


def polynomial(p,values):
 """Nested Horner over all three variables; values may be exact or intervals."""
 terms=[(tuple(map(int,k)),int(c))for k,c in p.terms()]
 def go(rows,i):
  if not rows:return Interval(0)
  if i==3:return Interval(sum(c for k,c in rows))
  by={}
  for k,c in rows:by.setdefault(k[i],[]).append((k,c))
  out=Interval(0)
  for j in range(max(by),-1,-1):out=out*values[i]+go(by.get(j,[]),i+1)
  return out
 return go(terms,0)


def derivative(p,i):
 ctx=p.context();out={}
 for ex,c in p.terms():
  if ex[i]:
   k=list(ex);v=k[i];k[i]-=1;out[tuple(k)]=v*c
 return ctx.from_dict(out)


def qvalue(q,values):return polynomial(q.n,values)/polynomial(q.d,values)


def taylor_at(coefficients,center):
 """Descending polynomial coefficients to ascending powers of z-center."""
 out=[];center=Rectangle(center)
 for a in coefficients:
  old=out;out=[Rectangle(0)for _ in range(len(old)+1)]
  for j,c in enumerate(old):out[j]=out[j]+center*c;out[j+1]=out[j+1]+c
  out[0]=out[0]+Rectangle(a)
 return out


def fixed_point(equations,center,radius):
 vals=[Interval(center[0]),Interval(0),Interval(center[1])]
 box=[Interval(center[0]-radius,center[0]+radius),Interval(0),Interval(center[1]-radius,center[1]+radius)]
 derivatives=[[derivative(f,i)for i in [0,2]]for f in equations]
 exactF=[polynomial(f,vals)for f in equations]
 assert all(v.lo==v.hi for v in exactF)
 J0=[[polynomial(f,vals).lo for f in row]for row in derivatives]
 determinant=J0[0][0]*J0[1][1]-J0[0][1]*J0[1][0]
 if not determinant:raise ArithmeticError('singular center Jacobian')
 Y=[[J0[1][1]/determinant,-J0[0][1]/determinant],[-J0[1][0]/determinant,J0[0][0]/determinant]]
 J=[[polynomial(f,box)for f in row]for row in derivatives]
 E=[[Interval(int(i==j))-sum((J[k][j]*Y[i][k]for k in range(2)),Interval(0))for j in range(2)]for i in range(2)]
 rows=[sum((v.upper()for v in row),rational(0))for row in E];q=max(rows)
 b=[sum((Y[i][k]*exactF[k].lo for k in range(2)),rational(0))for i in range(2)]
 margins=[radius-abs(v)-q*radius for v in b]
 return dict(box=box,exactF=exactF,J0=J0,Y=Y,J=J,E=E,determinant=determinant,row_bounds=rows,q=q,b=b,margins=margins)
