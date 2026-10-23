"""Native exact determinant adapter. Own Bareiss/Gauss copied from original verifier.
The native routine is not a probabilistic determinant call.
"""
from flint import fmpz, fmpq, fmpz_mat
from exact_degree21 import coef,univ
def horner(co,z):
 out=fmpz(0)
 for q in reversed(co):out=out*z+fmpz(q)
 return out

def coeffs(p,i,N):return [univ(coef(p,i,k))for k in range(N,-1,-1)]

def matrix(a,b):
 m=len(a)-1;n=len(b)-1
 return [[fmpz(0)]*j+a+[fmpz(0)]*(n-j-1)for j in range(n)]+[[fmpz(0)]*j+b+[fmpz(0)]*(m-j-1)for j in range(m)]

def det(a):
 a=[r[:]for r in a];old=fmpz(1);sign=1;nd=0;ns=0
 for k in range(len(a)-1):
  pi=next((i for i in range(k,len(a))if a[i][k]),None)
  if pi is None:return fmpz(0),nd,ns
  if pi!=k:a[k],a[pi]=a[pi],a[k];sign=-sign;ns+=1
  pivot=a[k][k]
  for i in range(k+1,len(a)):
   aik=a[i][k]
   for j in range(k+1,len(a)):
    q,rem=divmod(a[i][j]*pivot-aik*a[k][j],old)
    if rem:raise ArithmeticError('nonexact integer Bareiss division')
    a[i][j]=q;nd+=1
   a[i][k]=fmpz(0)
  old=pivot
 return sign*a[-1][-1],nd,ns

def gauss(a):
 a=[[fmpq(v)for v in row]for row in a];out=fmpq(1)
 for k in range(len(a)):
  pi=next((i for i in range(k,len(a))if a[i][k]),None)
  if pi is None:return fmpq(0)
  if pi!=k:a[k],a[pi]=a[pi],a[k];out=-out
  pivot=a[k][k];out*=pivot
  for i in range(k+1,len(a)):
   ratio=a[i][k]/pivot
   for j in range(k+1,len(a)):a[i][j]-=ratio*a[k][j]
   a[i][k]=fmpq(0)
 return out

def native(a):
 return fmpz_mat(a).det()

def dispatch_metadata(a):
 n=len(a);bits=max((abs(int(z)).bit_length()for row in a for z in row),default=0)
 branch='cofactor'if n<5 else 'bareiss'if n<25 else 'modular_proved'if n<60 or n<bits else 'modular_accelerated_proved'
 return dict(dimension=n,max_entry_bits=bits,source_dispatch_prediction=branch)
