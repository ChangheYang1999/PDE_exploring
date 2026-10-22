"""Analytically differentiated inputs, compressed integer interval convolution."""
import sys,os,math,hashlib,time,importlib.util
from pathlib import Path
from fractions import Fraction as F
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
sys.dont_write_bytecode=True
from flint import fmpz_poly
from mpmath import iv
ROOT=Path(__file__).resolve().parents[3];PATH=ROOT/'research/outer_cells/code/cell_integer_iv.py'
assert hashlib.sha256(PATH.read_bytes()).hexdigest()=='34b9b2a7d6784f71051946093c7a55d1e4d2acf57b23f399f0bffacb5c402797'
spec=importlib.util.spec_from_file_location('outer180_iv_parent',PATH);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
iq=old.iq;ends=old.ends;out=old.out;top=old.top

def binary_le(x,y):
 for s,m,e,bc in [x,y]:assert s in (0,1) and m>=0 and bc>=0 and bc==int(m).bit_length()
 e=min(x[2],y[2]);a=(-1 if x[0] else 1)*(int(x[1])<<(x[2]-e));b=(-1 if y[0] else 1)*(int(y[1])<<(y[2]-e))
 return a<=b

def falling(n,p):
 z=1
 for j in range(p):z*=n-j
 return z

def setup(Q=16):
 assert 8<=Q<=32
 iv.dps=200;d=old.setup(Q,512);d['input_precision_digits']=200;return d

def cell(d,left,right,primary=None):
 started=time.monotonic();a,b=F(left),F(right);assert 0<=a<b
 Q=d['Q'];tc=(a+b)/2;h=(b-a)/2;ha=iq(h);tca=iq(tc);base=2*Q+1;Pint=d['Pint']
 hp=[ha**l for l in range(7)];tp=[tca**l for l in range(7)];cache={};input_checks=0;input_hasher=hashlib.sha256()
 def expansion(c,lam,degree):
  assert degree>=len(c)-1
  key=(lam,degree)
  if key not in cache:
   ell=iq(lam*h);x=abs(ell);fac=iv.exp(iq(lam*tc));co=[iv.mpf(1)]
   for j in range(1,degree+1):co.append(co[-1]*ell/j)
   tails=[fac*iv.exp(x)*x**(degree-l+1)/math.factorial(degree-l+1) for l in range(7)]
   cache[key]=co,fac,tails
  co,fac,tails=cache[key]
  shifted=[sum((math.comb(j,l)*c[j]*tp[j-l]*hp[l] for j in range(l,len(c))),iv.mpf(0)) for l in range(len(c))]
  poly=[iv.mpf(0)]*(degree+1)
  for l,v in enumerate(shifted):
   for q in range(l,degree+1):poly[q]+=v*co[q-l]
  return [fac*x for x in poly],top(sum((abs(v)*tails[l] for l,v in enumerate(shifted)),iv.mpf(0)))
 def term(c,lam):
  nonlocal input_checks
  if all(ends(v)==(0,0) for v in c):return [iv.mpf(0)]*(Q+1),[iv.mpf(0)]*3
  poly,er=expansion(c,lam,Q);rem=[er];cp=list(c)
  for p in [1,2]:
   cp=[iq(lam)*v+((j+1)*cp[j+1] if j+1<len(cp) else 0) for j,v in enumerate(cp)]
   dp,er=expansion(cp,lam,Q-p);rem.append(er)
   for l,v in enumerate(dp):
    x=poly[l+p]*falling(l+p,p)/ha**p;xe=x._mpi_;ve=v._mpi_
    assert binary_le(xe[0],ve[1]) and binary_le(ve[0],xe[1]),('input derivative disjoint',lam,p,l)
    input_hasher.update((str(lam)+' '+str(p)+' '+str(l)+' '+str(xe)+' '+str(ve)+'\n').encode());input_checks+=1
  return poly,rem
 def add(x,y):return [a+b for a,b in zip(x[0],y[0])],[top(a+b) for a,b in zip(x[1],y[1])]
 def scale(x,s):return [v*s for v in x[0]],[top(v*abs(s)) for v in x[1]]
 def combine(cs,lams,s):
  z=([iv.mpf(0)]*(Q+1),[iv.mpf(0)]*3)
  for c,lam in zip(cs,lams):z=add(z,term(c,lam))
  return scale(z,s)
 beta=d['beta'];rho=[combine(cs,beta,d['r3']) for cs in d['density']];D=[combine(cs,beta,d['r3']) for cs in d['dt']]
 H=[scale(x,iq(2*j+1)) for j,x in enumerate(rho)];E=[combine(cs,beta,d['r3']) for cs in d['linear']];P=[];S=[];rates=[x-1 for x in beta]
 for n in range(1,262):
  tr=scale(term([d['hs'][n-1]],F(-2*n-2)),d['r2'])
  P.append(add(combine(d['pv'][n-1],rates,d['r2']),tr));S.append(add(combine(d['sv'][n-1],rates,d['r2']),tr))
 def sums(models):
  ns=[];es=[]
  for p in range(3):
   ns.append(top(sum((abs(cs[l])*falling(l,p)/ha**p for cs,rs in models for l in range(p,Q+1)),iv.mpf(0))))
   es.append(top(sum((rs[p] for cs,rs in models),iv.mpf(0))))
  return ns,es
 norms={name:sums(v) for name,v in [('P',P),('S',S),('D',D),('H',H),('E',E)]}
 def quant(x,p):
  lo,hi=ends(x);lo*=2**p;hi*=2**p;il=lo.numerator//lo.denominator;ih=-((-hi.numerator)//hi.denominator);mid=(il+ih)//2;rad=max(mid-il,ih-mid)
  assert rad>=0 and F(mid-rad,2**p)<=ends(x)[0]<=ends(x)[1]<=F(mid+rad,2**p)
  return mid,rad
 def angular(models,kind):
  even=kind in ['velocity_cos','velocity_sin'];size=(523 if even else 522)*base;ms=[0]*size;rs=[0]*size
  for j,(poly,rem) in enumerate(models):
   positive=261+j+1 if even else 261+j;negative=261-j-1 if even else 260-j
   for l,v in enumerate(poly):
    if kind in ['velocity_cos','density_cos']:v=v/2
    m,r=quant(v,Pint);ms[positive*base+l]=m;rs[positive*base+l]=r;ms[negative*base+l]=-m if kind in ['velocity_sin','density_sin'] else m;rs[negative*base+l]=r
  return ms,rs
 pe=angular(P,'velocity_cos');se=angular(S,'velocity_sin');de=angular(D,'density_sin');he=angular(H,'density_cos')
 def convolution(x,y):
  mx,rx=fmpz_poly(x[0]),fmpz_poly(x[1]);my,ry=fmpz_poly(y[0]),fmpz_poly(y[1])
  return mx*my,fmpz_poly([abs(v) for v in x[0]])*ry+rx*fmpz_poly([abs(v) for v in y[0]])+rx*ry
 m1,r1=convolution(pe,de);m2,r2=convolution(se,he);mc,rc=m1+m2,r1+r2;assert mc.degree()<1044*base and rc.degree()<1044*base
 den=2**(2*Pint);fact=d['factorialQ'];mat=d['matrix'];poly_sums=[F(0)]*3;theta_sums=[F(0)]*3;overlaps=0;digest=hashlib.sha256()
 assert primary is None or (primary['left_exact']==str(a) and primary['right_exact']==str(b) and primary['Q']==Q)
 for n in range(522):
  centers=[int(mc[(522+n)*base+l]) for l in range(2*Q+1)];radii=[int(rc[(522+n)*base+l]) for l in range(2*Q+1)]
  if n<261:
   for l,v in enumerate(E[n][0]):m,r=quant(v,2*Pint);centers[l]+=m;radii[l]+=r
  assert all(v>=0 for v in radii)
  for l,(m,r) in enumerate(zip(centers,radii)):
   digest.update((str(m)+' '+str(r)+'\n').encode())
   if primary is not None:
    x=primary['coefficients'][n][l];assert max(F(x['lower_exact']),F(m-r,den))<=min(F(x['upper_exact']),F(m+r,den)),('residual coefficient disjoint',n,l)
    overlaps+=1
  for p in range(3):
   cc=[centers[l+p]*falling(l+p,p) for l in range(2*Q+1-p)]+[0]*p;rr=[radii[l+p]*falling(l+p,p) for l in range(2*Q+1-p)]+[0]*p
   high=sum(abs(cc[l])+rr[l] for l in range(Q+1,2*Q+1));maximum=0
   for row in mat:
    center=sum(x*y for x,y in zip(cc,row));radius=sum(x*abs(y) for x,y in zip(rr,row));maximum=max(maximum,abs(center)+radius)
   val=(F(maximum,den*fact)+F(high,den))/h**p;poly_sums[p]+=val;theta_sums[p]+=(2*n+1)*val
 bs=[];cs=[];parts=[]
 for p in range(3):
  er=norms['E'][1][p]
  for l in range(p+1):
   for A,B in [('P','D'),('S','H')]:
    na,ea=norms[A];nb,eb=norms[B];er+=math.comb(p,l)*(na[l]*eb[p-l]+nb[p-l]*ea[l]+ea[l]*eb[p-l])
  er=top(er);bs.append(top(iq(poly_sums[p])+er));cs.append(top(iq(theta_sums[p])+1043*er));parts.append({'polynomial_upper_exact':str(poly_sums[p]),'theta_polynomial_upper_exact':str(theta_sums[p]),'error':out(er)})
 t=d['tb']+a;w=iq(d['L']**6)*iv.exp(iq(-4*t))*iv.exp(iq(F(3,2)-d['k'])*iv.log(1+iv.exp(iq(2*t))/iq(d['L']**2)));fac=iv.pi*iq(b-a)*w
 sq=[fac*(bs[0]**2+bs[1]**2+cs[0]**2),fac*((bs[0]+bs[1])**2+(bs[1]+bs[2])**2+(cs[0]+cs[1])**2)]
 return {'left_exact':str(a),'right_exact':str(b),'Q':Q,'max_abs_lambda_h_exact':str(524*h),'input_precision_digits':200,'B':[out(x) for x in bs],'C':[out(x) for x in cs[:2]],'parts':parts,'norm_squares':[out(x) for x in sq],'coefficient_overlap_checks':overlaps,'derivative_input_checks':input_checks,'derivative_input_sha256':input_hasher.hexdigest(),'integer_coefficient_sha256':digest.hexdigest(),'exact_integer_convolutions':8,'exact_Green_scalar_checks':d['exact_Green_scalar_checks'],'seconds':time.monotonic()-started}
