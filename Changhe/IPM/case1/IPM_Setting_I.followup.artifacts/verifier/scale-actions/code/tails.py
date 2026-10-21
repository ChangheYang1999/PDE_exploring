from fractions import Fraction as F
from math import isqrt
def tail_constants(d,V):
 H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1)
 ceil=lambda v:(v.numerator+v.denominator-1)//v.denominator
 B=ceil(max(abs(F(float(v))) for v in d.b.ravel()))
 eps=F(1,5)-1/F(d.cl);L=F(d.L);assert eps>0 and L>=1
 out=[]
 for j in range(V.shape[1]):
  Bd=ceil(max(abs(F(float(v))) for v in V[:-2,j]));dc=abs(F(float(V[-2,j])))
  out.append(L**3*H*(Bd+dc/(2*F(d.cl)**2)*B*(1+2*d.N*d.N)*(1+2/eps)))
 return L**3*H*B,out
