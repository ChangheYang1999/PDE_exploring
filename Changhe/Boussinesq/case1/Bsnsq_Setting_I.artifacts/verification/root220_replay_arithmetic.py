"""Independent512-bit endpoint implementation, monomial/Horner basis.
Does not import dyadic_root220 or scalar evaluation modules.
"""
from fractions import Fraction as Rat
from math import comb,factorial
BITS=512;UNIT=1<<BITS;LN_TERMS=220;EXP_TERMS=200
TRACE=None

def note(kind,value):
 if TRACE is not None:TRACE.setdefault(kind,[]).append(value)
def interval(a,b=None):
 b=a if b is None else b
 if a>b:raise ArithmeticError('invalid interval')
 return int(a),int(b)
def number(q):
 q=Rat(q);n=q.numerator*UNIT;d=q.denominator;return interval(n//d,-((-n)//d))
def plus(a,b):return interval(a[0]+b[0],a[1]+b[1])
def negative(a):return interval(-a[1],-a[0])
def minus(a,b):return plus(a,negative(b))
def product(a,b):
 vals=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]);return interval(min(vals)//UNIT,-((-max(vals))//UNIT))
def inverse(a):
 if a[0]<=0<=a[1]:raise ArithmeticError('zero divisor')
 return interval(UNIT*UNIT//a[1],-((-UNIT*UNIT)//a[0]))
def quotient(a,b):return product(a,inverse(b))
def scale(a,q):return product(a,number(q))
def power(a,n):
 if n<0:return power(inverse(a),-n)
 out=number(1)
 for _ in range(n):out=product(out,a)
 return out

def sixth(E):
 E=Rat(E)
 if E<1:raise ValueError('E>=1 required')
 target=(E.denominator<<(6*BITS))//E.numerator
 g=1<<((target.bit_length()+5)//6);count=0
 while True:
  h=(5*g+target//(g**5))//6;count+=1
  if h>=g:break
  g=h
  if count>4096:raise ArithmeticError('root iteration cap')
 while g**6>target:g-=1;count+=1
 while(g+1)**6<=target:g+=1;count+=1
 hi=g if E.numerator*g**6==E.denominator*(UNIT**6)else g+1
 if not E.numerator*g**6<=E.denominator*(UNIT**6)<=E.numerator*hi**6:raise ArithmeticError('root verification')
 note('root_iterations',count);return interval(g,hi)

def atanh_log(a):
 a=Rat(a)
 if not 0<=a<=Rat(1,3):raise ValueError('log reduction')
 a2=power(number(a),2);v=number(0)
 for n in reversed(range(LN_TERMS)):v=plus(product(v,a2),number(Rat(2,2*n+1)))
 out=product(number(a),v)
 tail=2*Rat(1,3)**(2*LN_TERMS+1)/((2*LN_TERMS+1)*(1-Rat(1,9)))
 return interval(out[0],out[1]+number(tail)[1])
L2=None

def ln_point(z):
 global L2
 z=Rat(z)
 if z<=0:raise ValueError('positive logarithm')
 if L2 is None:L2=atanh_log(Rat(1,3))
 # Exact bit-length estimate and at most a few corrections.
 j=z.numerator.bit_length()-z.denominator.bit_length();v=z/(Rat(2)**j)
 while v<1:v*=2;j-=1
 while v>=2:v/=2;j+=1
 note('log_reductions',j);return plus(atanh_log((v-1)/(v+1)),scale(L2,j))
def logarithm(a):
 if a[0]<=0:raise ValueError('positive interval logarithm')
 return interval(ln_point(Rat(a[0],UNIT))[0],ln_point(Rat(a[1],UNIT))[1])

def expminus_point(z):
 z=Rat(z)
 if z<0:raise ValueError('negative exponent argument')
 if z>=BITS:note('exp_reductions','tail');return interval(0,1)
 j=0;u=z
 while u>Rat(1,4):u/=2;j+=1
 note('exp_reductions',j)
 term=number(1);total=term;u=number(u)
 for n in range(1,EXP_TERMS+1):term=scale(product(term,u),Rat(1,n));total=plus(total,term)
 tail=Rat(2,4**(EXP_TERMS+1)*factorial(EXP_TERMS+1));total=interval(total[0],total[1]+number(tail)[1]);out=inverse(total)
 for _ in range(j):out=interval(out[0]*out[0]//UNIT,-((-out[1]*out[1])//UNIT))
 return out
def expminus(a):
 if a[0]<0:raise ValueError('nonnegative interval')
 return interval(expminus_point(Rat(a[1],UNIT))[0],expminus_point(Rat(a[0],UNIT))[1])

BASIS={0:[1]}
def basis(n):
 if n in BASIS:return BASIS[n]
 a=[Rat((-1)**(n-j)*n*4**j*comb(n+j,2*j),n+j)for j in range(n+1)]
 if any(z.denominator!=1 for z in a):raise ArithmeticError('noninteger Chebyshev formula')
 a=[z.numerator for z in a]
 if n==1:expected=[-1,2]
 else:
  last,prev=basis(n-1),basis(n-2);expected=[0]*(n+1)
  for k,v in enumerate(last):expected[k]-=2*v;expected[k+1]+=4*v
  for k,v in enumerate(prev):expected[k]-=v
 if a!=expected:raise ArithmeticError('basis identity')
 BASIS[n]=a;return a

def compile_tensor(raw):
 rows=[[Rat(q)for q in row]for row in raw];n=len(rows);m=len(rows[0])
 if not n or not m or any(len(row)!=m for row in rows):raise ValueError('rectangular tensor')
 D=max(z.denominator.bit_length()-1 for row in rows for z in row)
 if any(z.denominator&(z.denominator-1)for row in rows for z in row):raise ValueError('exactdyadicsrequired')
 den=1<<D;ints=[[z.numerator*(den//z.denominator)for z in row]for row in rows]
 temp=[[0]*m for _ in range(n)];out=[[0]*m for _ in range(n)]
 for i,row in enumerate(ints):
  for j,c in enumerate(row):
   if c:
    for k,z in enumerate(basis(j)):temp[i][k]+=c*z
 for i,row in enumerate(temp):
  for j,z in enumerate(basis(i)):
   for k,c in enumerate(row):out[j][k]+=z*c
 return [[number(Rat(z,den))for z in row]for row in out]

def horner(row,z):
 val=number(0);der=number(0)
 for c in reversed(row):der=plus(product(der,z),val);val=plus(product(val,z),c)
 return val,der

def polynomial(c,t,w):
 rowvals=[];rowders=[]
 for row in c:v,d=horner(row,w);rowvals.append(v);rowders.append(d)
 value,dt=horner(rowvals,t);dw,_=horner(rowders,t);return value,dt,dw

class Function:
 def __init__(self,data):
  if Rat(data['beta'])!=3 or Rat(data['alpha'])!=3 or data['M']!=3:raise ValueError('fixed exponent')
  self.s=Rat(data['s']);self.a=Rat(data['a'])
  if self.s<=0 or not self.a:raise ValueError('scale and amplitude')
  self.outer=compile_tensor(data['outer']);self.patches=[]
  for p in data['patches']:
   R,L=Rat(p['R']),Rat(p['L'])
   if R<=0 or L<=0:raise ValueError('patch scales')
   self.patches.append((R,L,compile_tensor(p['coefficients'])))
  self.k=minus(number(1),expminus(number(3)))
 def gx(self,x,h,trace=False):
  global TRACE
  TRACE={}if trace else None
  x,h=Rat(x),Rat(h);X=number(x);q=sixth(1+x*x+(h/self.s)**6);den=minus(number(1),product(self.k,q));t=scale(logarithm(den),Rat(-1,3));w=scale(power(q,2),(h/self.s)**2)
  qx=scale(power(q,7),-x/3);tx=scale(quotient(product(self.k,qx),den),Rat(1,3));wx=scale(product(q,qx),2*(h/self.s)**2)
  val,pt,pw=polynomial(self.outer,t,w);dx=plus(product(pt,tx),product(pw,wx))
  for R,L,c in self.patches:
   u=x*x/(R*R+x*x);v=h*h/(R*R+h*h);ux=2*x*R*R/(R*R+x*x)**2
   co,cu,_=polynomial(c,number(u),number(v));en=expminus(number((x*x+h*h)/(L*L)))
   val=plus(val,product(en,co));dx=plus(dx,product(en,minus(scale(cu,ux),scale(co,2*x/(L*L)))))
  q2=power(q,-2);out=scale(plus(product(plus(q2,scale(power(q,4),Rat(2,3)*x*x)),val),scale(product(q2,dx),x)),h)
  stats=TRACE;TRACE=None
  return(out,stats)if trace else out
