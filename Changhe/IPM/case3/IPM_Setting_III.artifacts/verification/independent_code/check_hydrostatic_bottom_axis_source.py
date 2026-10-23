"""Result202: independent finite algebra and countertests for the written proof."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import factorial,comb
import hashlib,json,time,itertools
import numpy as np
import sympy as s
import mpmath as mp
outdir=Path('research/hydrostatic_bottom_axis_source_audit/verification');start=time.monotonic();checks=[]
def check(name,ok,detail=None):checks.append(dict(name=name,pass_=bool(ok),detail=detail))
def zero(name,e):check(name,s.simplify(e)==0)
x,z,sg,c,eta,lam,b,a,gx,gy=s.symbols('x z sg c eta lam b a gx gy',real=True)
A=2*c-1;k=s.Function('k')(x);w=s.Function('w')(z);kp=s.diff(k,x);a0=A*k*z;b1=1-a0*kp/k
for n in range(1,7):
 dxu=(2*n+1)*k**(2*n)*kp*w+k**(2*n)*s.diff(w,z)
 zero('bottom conjugation n='+str(n),a0*dxu+((2*n+1)*b1-1)*k**(2*n+1)*w-k**(2*n+1)*(A*z*s.diff(w,z)+2*n*w))
zero('first bottom forcing',-(kp*kp/2-k*s.diff(k,x,2)/6)-(-kp**2/2+k*s.diff(k,x,2)/6))
# Monomial inverse including noninteger A: direct integration gives denominator m+A*j.
for m in range(1,9):
 for j in (0,1,2,7):zero('Euler inverse '+str((m,j)),A*z*s.diff(z**j/(m+A*j),z)+m*z**j/(m+A*j)-z**j)
ka=s.Function('ka')(z);W=s.Function('W')(z,sg);U=s.Function('U')(z,sg);Z=W/ka
left=A*ka*z*s.diff(Z,z)/ka+sg*s.diff(Z,sg)+A*z*s.diff(ka,z)*Z/ka
zero('isopycnal conjugated left',ka*left-(A*z*s.diff(W,z)+sg*s.diff(W,sg)))
right=s.diff(Z*s.diff(U/ka,z)/ka,z)/ka
zero('isopycnal conjugated nonlinear term',ka*right-s.diff(W/ka**2*s.diff(U/ka,z),z))
Hx,Yx,Zx,Zs,Z0=s.symbols('Hx Yx Zx Zs Z0',real=True)
h_at_x=Hx+Yx**2/Z0;b_at_y=(-Yx**2+a*Zx+Z0+sg*Zs)/Z0
flux=((c+Hx-A)*Z0+a*Zx+sg*Zs)/Z0
zero('converse h_x+b_y-c is flux/Z',h_at_x+b_at_y-c-flux)
mat=s.Matrix([[b*lam+s.I*a*eta-1,gx,gy],[-s.I*eta,lam,0],[0,s.I*eta,lam]])
zero('complete frozen determinant',mat.det()-(b*lam**3+(s.I*a*eta-1)*lam**2+s.I*gx*eta*lam+gy*eta**2))
G=s.Function('G')(x);v=G/s.diff(G,x)
zero('rational v second derivative',s.diff(v,x,2)-(-s.diff(G,x,2)/s.diff(G,x)-G*s.diff(G,x,3)/s.diff(G,x)**2+2*G*s.diff(G,x,2)**2/s.diff(G,x)**3))
zero('arctan v curvature',s.diff(c*x-(c-1)*s.atan(x),x,2)-2*(c-1)*x/(1+x*x)**2)
# Independent truncated Taylor algebra, retaining all derivatives needed at y0.
def trim(u,L):return (u+[F(0)]*L)[:L]
def add(u,v,L):return [a+b for a,b in zip(trim(u,L),trim(v,L))]
def scale(u,a,L):return [a*x for x in trim(u,L)]
def mul(u,v,L):
 u=trim(u,L);v=trim(v,L);return [sum((u[j]*v[i-j]for j in range(i+1)),F(0))for i in range(L)]
def deriv(u,L):return trim([(i+1)*u[i+1]for i in range(len(u)-1)],L)
def div(u,v,L):
 u=trim(u,L);v=trim(v,L);o=[]
 for i in range(L):o.append((u[i]-sum((v[j]*o[i-j]for j in range(1,i+1)),F(0)))/v[0])
 return o
def rec(data,nn,cc):
 L=len(data);gp=deriv(data,L);vv=div(data,gp,L);aa=add([2*cc],scale(deriv(vv,L),-1,L),L)
 gg={0:data,1:scale(deriv(deriv(vv,L),L),F(-1,2),L)};bb={0:vv};av={0:aa}
 for n in range(1,nn):
  rhs=add(gg[n],scale(mul(vv,deriv(gg[n],L),L),-1,L),L)
  rhs=add(rhs,scale(mul(aa,gg[n],L),-2*n,L),L)
  for i in range(1,n):
   j=n-i;rhs=add(rhs,scale(mul(av[i],gg[j],L),-2*j,L),L)
   rhs=add(rhs,scale(mul(bb[i],deriv(gg[j],L),L),-1,L),L)
  bb[n]=div(rhs,gp,L);av[n]=scale(deriv(bb[n],L),F(-1,2*n+1),L)
  gg[n+1]=scale(deriv(deriv(bb[n],L),L),F(-1,(2*n+1)*(2*n+2)),L)
 return [gg[n][0]for n in range(1,nn+1)]
for n in range(1,5):
 for seed in (1,3,7):
  L=3*n+4;data=[F((i*seed+2)%7-3,factorial(i)*(i+1))for i in range(L)];data[0]=F(2+seed,3);data[1]=F(3+seed,4)
  base=rec(data,n,F(5,2));changed=data.copy();changed[3*n]+=F(1,factorial(3*n));other=rec(changed,n,F(5,2));target=(data[0]/data[1]**2)**n/factorial(2*n)
  check('highest axis jet coefficient '+str((n,seed)),other[-1]-base[-1]==target,dict(expected=str(target),observed=str(other[-1]-base[-1])))
  check('lower axis coefficients unchanged '+str((n,seed)),other[:-1]==base[:-1])
# Majorant coefficient bound, with C1 scaled to1.
U=[F(1)]+[F(0)]*24
for m in range(1,len(U)):
 U[m]=sum((U[i]*U[m-2-i]/(m-i)for i in range(max(0,m-1))),F(0))
 if m%2:check('odd majorant zero '+str(m),U[m]==0)
 else:
  l=m//2;check('Catalan majorant '+str(m),U[m]<=F(comb(2*l,l),l+1)<=4**l)
# The C2 inverse regularity counterexample uses no transport assertion.
al=s.Rational(1,2);psi=s.exp(-x*x)*(1+x**(2+al));second=s.diff(psi,x,2)
zero('C2 density singular velocity coefficient',s.limit((second+2)/x**al,x,0,dir='+')-(2+al)*(1+al))
y=s.symbols('y',positive=True)
primitive=s.sqrt(s.pi)*s.erf(y)/4
zero('canonical regularity-example primitive derivative',s.diff(primitive,y)-s.exp(-y*y)/2)
zero('canonical regularity-example second derivative',s.diff(primitive,y,2)+y*s.exp(-y*y))
# Oscillatory perturbation norm bound on independently sampled complex strip points.
delta=.15;alpha=.7;beta=.8;y0=.9
zgrid=np.linspace(-10,10,401)[:,None]+1j*np.linspace(-delta,delta,11)[None,:]
t2=max(0.,3/beta-delta**2);C2=(t2+delta**2)**1.5*np.exp(-beta*t2/2)
t2=max(0.,6/beta-delta**2-y0**2);C3=np.exp(beta*delta**2)*(t2+delta**2+y0**2)**3*np.exp(-beta*t2/2)
for n in (1,2,4,8,12):
 P=zgrid**3*(zgrid*zgrid-y0*y0)**(3*n)*np.exp(-beta*n*zgrid*zgrid)
 val=float(np.max(np.abs(P)));check('strip norm bound sample n='+str(n),val<=C2*C3**n,dict(sample=val,bound=C2*C3**n))
with mp.workdps(55):
 yy=mp.mpf('0.9');alfa=mp.mpf('.7');be=mp.mpf('.8')
 for n in (1,2,3):
  fun=lambda t:t**3*(t*t-yy*yy)**(3*n)*mp.exp(-(alfa+be*n)*t*t)
  expected=mp.factorial(3*n)*yy**3*(2*yy)**(3*n)*mp.exp(-(alfa+be*n)*yy*yy)
  got=mp.diff(fun,yy,3*n);err=abs(got-expected)/(1+abs(expected));check('Gaussian highest jet n='+str(n),err<mp.mpf('1e-48'),str(err))
# Numerical roots supplement, and do not replace, the two frozen asymptotic balances.
rootrows=[]
for axis in (True,False):
 err=[]
 for freq in (1e2,1e4,1e6,1e8):
  bv=1.5;gv=.8;av=0 if axis else 1.2;xx=0 if axis else .3
  roots=np.roots([bv,1j*av*freq-1,1j*xx*freq,gv*freq**2])
  if axis:
   amp=(gv/bv)**(1/3)*freq**(2/3);pred=np.array([-amp,amp*np.exp(1j*np.pi/3),amp*np.exp(-1j*np.pi/3)])
  else:
   amp=np.sqrt(1j*gv*freq/av);pred=np.array([amp,-amp,-1j*av*freq/bv])
  best=min(max(abs(roots[j]-pred[k])for j,k in enumerate(perm))for perm in itertools.permutations(range(3)))
  err.append(float(best));check('frozen O(1) root correction '+str((axis,freq)),best<2.,float(best))
 rootrows.append(dict(axis=axis,corrections=err))
out=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start,checks=checks,pass_count=sum(t['pass_']for t in checks),fail_count=sum(not t['pass_']for t in checks),root_rows=rootrows,proof_sha256=hashlib.sha256((outdir.parent/'PROOF.md').read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Finite algebra and countertests; full informal proof in PROOF.md. Unrestricted C1 converse remains OPEN pending repair.')
out['status']='PASS'if out['fail_count']==0 else'FAIL';(outdir/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['pass_count'],out['fail_count'],out['seconds'],'seconds')
for t in checks:
 if not t['pass_']:print('FAIL',t)
if out['fail_count']:raise SystemExit(1)
