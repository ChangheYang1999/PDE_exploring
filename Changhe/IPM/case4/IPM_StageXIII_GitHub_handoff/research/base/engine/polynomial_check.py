"""Exact formal-polynomial check of the independent s=x²,t=y² formulation."""
from ipm_portable import output_dir, peak_rss_mib
from fractions import Fraction
class Sym:
 def __init__(self,value=0):self.c=value if isinstance(value,dict) else ({():Fraction(value)} if value else {})
 @staticmethod
 def var(name):return Sym({(name,):Fraction(1)})
 def __add__(self,other):
  other=other if isinstance(other,Sym) else Sym(other);d=self.c.copy()
  for k,v in other.c.items():d[k]=d.get(k,0)+v
  return Sym({k:v for k,v in d.items() if v})
 __radd__=__add__
 def __neg__(self):return Sym({k:-v for k,v in self.c.items()})
 def __sub__(self,o):return self+-o if isinstance(o,Sym) else self+(-Sym(o))
 def __rsub__(self,o):return Sym(o)+-self
 def __mul__(self,other):
  other=other if isinstance(other,Sym) else Sym(other);d={}
  for k,v in self.c.items():
   for l,w in other.c.items():m=tuple(sorted(k+l));d[m]=d.get(m,0)+v*w
  return Sym({k:v for k,v in d.items() if v})
 __rmul__=__mul__
 def __eq__(self,o):return self.c==(o.c if isinstance(o,Sym) else Sym(o).c)
def add(*args):
 out={}
 for p in args:
  for k,v in p.items():out[k]=out.get(k,Sym())+v
 return out
def mul(p,q):
 out={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():out[i+k,j+l]=out.get((i+k,j+l),Sym())+v*w
 return out
def diff(p,axis):
 return {(i-(axis==0),j-(axis==1)):v*(i,j)[axis] for (i,j),v in p.items() if (i,j)[axis]}
def scale(p,c):return {k:v*c for k,v in p.items()}
def check():
 L,a,b,c,d,ee,g,u,v,w,z,k=[Sym.var(name) for name in ['cl','a','b','c','d','e','g','u','v','w','z','k']]
 h=1-L;F={(0,0):a,(1,0):b,(0,1):c,(2,0):d,(1,1):ee,(0,2):g};H={(0,0):h,(1,0):u,(0,1):v,(2,0):w,(1,1):z,(0,2):k}
 ss={(1,0):Sym(1)};tt={(0,1):Sym(1)};Fs=diff(F,0);Ft=diff(F,1);Hs=diff(H,0);Ht=diff(H,1)
 tr=add(scale(mul(mul(ss,add({(0,0):L},scale(H,-1),scale(mul(tt,Ht),-2))),Fs),2),
        scale(mul(mul(tt,add({(0,0):L},H,scale(mul(ss,Hs),2))),Ft),2),
        mul(add({(0,0):L-1},H,scale(mul(ss,Hs),2)),F))
 expected={(0,0):Sym(),(1,0):2*(2*L-1)*b+3*a*u,(0,1):2*c+a*v,
           (2,0):4*(2*L-1)*d+b*u+5*a*w,(1,1):4*L*ee-5*b*v+9*c*u+3*a*z,(0,2):4*g+3*c*v+a*k}
 for key,value in expected.items():assert tr.get(key,Sym())==value,key
 po=add(scale(mul(ss,diff(Hs,0)),4),scale(Hs,6),scale(mul(tt,diff(Ht,1)),4),scale(Ht,6),scale(Fs,2))
 assert po[(0,0)]==6*(u+v)+2*b
 assert po[(1,0)]==20*w+6*z+4*d
 assert po[(0,1)]==6*z+20*k+2*ee
 return {'formal_coefficient_identities':True,'transport_coefficients_verified':6,'Poisson_coefficients_verified':3,'independent_variables':'s=x^2,t=y^2','arithmetic':'exact multivariate rational polynomial ring'}
