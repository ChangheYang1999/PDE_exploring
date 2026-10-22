"""DRAFT: density-moment inner ODE defects and integer interval convolution."""
import sys,os,math,hashlib,time,importlib.util
from pathlib import Path
from fractions import Fraction as F
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
sys.dont_write_bytecode=True
from flint import fmpz_poly
from mpmath import iv
ROOT=Path(__file__).resolve().parents[3];PATH=ROOT/'research/inner_cells/code/cell_integer_iv.py'
assert hashlib.sha256(PATH.read_bytes()).hexdigest()=='eac8b71b67e28f780c1f5e8a539cb89e46ba35f3ec328692967577cb9e69b809'
spec=importlib.util.spec_from_file_location('inner181_iv_parent',PATH);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
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
 started=time.monotonic();a,b=F(left),F(right);assert -5<=a<b<=0
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
 alpha=d['alpha'];zero=([iv.mpf(0)]*(Q+1),[iv.mpf(0)]*3)
 def mix(ps,offset,s):return combine([[iq(v) for v in p] for p in ps],[al+offset for al in alpha],s)
 def pn(poly,p):return top(sum((abs(poly[l])*falling(l,p)/ha**p for l in range(p,len(poly))),iv.mpf(0)))
 def multiply(x,y):
  poly=[iv.mpf(0)]*(2*Q+1)
  for j,u in enumerate(x[0]):
   for l,v in enumerate(y[0]):poly[j+l]+=u*v
  errors=[]
  for p in range(3):
   er=sum((abs(poly[l])*falling(l,p)/ha**p for l in range(Q+1,2*Q+1)),iv.mpf(0))
   for j in range(p+1):er+=math.comb(p,j)*(pn(x[0],j)*y[1][p-j]+pn(y[0],p-j)*x[1][j]+x[1][j]*y[1][p-j])
   errors.append(top(er))
  return poly[:Q+1],errors
 def ode(y0,lam,sig,G):
  ell=iq(lam*h);powers=[iv.mpf(1)]
  for q in range(1,Q+1):powers.append(powers[-1]*ell)
  poly=[]
  for q in range(Q+1):
   val=y0*powers[q]/math.factorial(q)
   for l in range(q):val+=sig*ha*G[0][l]*math.factorial(l)*powers[q-l-1]/math.factorial(q)
   poly.append(val)
  defect=top(abs(iq(lam)*poly[Q]+sig*G[0][Q]));rate=iq(abs(lam))
  e0=top(iv.exp(abs(ell))*ha*(defect/(Q+1)+G[1][0]));e1=top(rate*e0+G[1][0]+defect);e2=top(rate*e1+G[1][1]+Q*defect/ha)
  return poly,[e0,e1,e2]
 def derivative(ps):return [[(al+3)*p[l]+((l+1)*p[l+1] if l+1<len(p) else 0) for l in range(len(p))] for al,p in zip(alpha,ps)]
 Hhat=[mix(ps,0,iv.mpf(1)) for ps in d['cs']];rho=[];D=[];H=[];Eta=[];ED=[]
 for j,ps in enumerate(d['cs'][:261]):
  rho.append(mix(ps,3,d['R3']));D.append(mix(derivative(ps),3,d['R3']));H.append(scale(rho[-1],iq(2*j+1)))
  es=[[F(0)]]+ps[1:];Eta.append(mix(es,3,d['R3']));ED.append(mix(derivative(es),3,d['R3']))
 E=[zero for _ in range(262)];c=iq(3/d['k']-1)
 def sine_add(nu,model,scalar):
  assert nu!=0;dest=(abs(nu)-1)//2;E[dest]=add(E[dest],scale(model,scalar if nu>0 else -scalar))
 for j,(eta,dt) in enumerate(zip(Eta,ED)):
  nu=2*j+1;sine_add(nu,dt,1/iq(d['k']));sine_add(nu,eta,iq(-1))
  for freq in [nu+2,nu-2]:sine_add(freq,dt,-c/2)
  for freq in [nu+2,2-nu]:sine_add(freq,eta,c*nu/2)
 er2=scale(term([iv.mpf(1)],F(2)),d['R2']);P=[];S=[]
 for n in range(1,262):
  m=2*n;i0=iv.mpf(0)
  for al,p in zip(alpha,d['cs'][n-1]):
   if any(p):
    q=old.inverse_explicit(p,m+4+al);val=sum((x*tc**l for l,x in enumerate(q)),F(0));i0+=iv.exp(iq(al*tc))*iq(val)
  im=ode(i0,-m-4,1,Hhat[n-1]);avg=scale(add(Hhat[n-1],Hhat[n]),iq(F(1,2)));Adiv=multiply(er2,add(avg,scale(im,iq(-m))))
  if n==1:Bdiv=mix(d['b1'],2,d['R2'])
  else:
   j0=iv.exp(iq((m-4)*tc))*d['J0'][n-1]
   for al,p in zip(alpha,d['cs'][n]):
    if any(p):j0+=iv.exp(iq(al*tc))*old.integrals.integrate(p,tc,-tc,4-m+al)
   jm=ode(j0,m-4,-1,Hhat[n]);Bdiv=multiply(er2,add(scale(jm,iq(m)),scale(avg,iq(-1))))
  P.append(scale(add(Adiv,Bdiv),iq(F(-1,2))));S.append(scale(add(Bdiv,scale(Adiv,iq(-1))),iq(F(1,2))))
 cross_input_checks=0;cross_input_hash=hashlib.sha256()
 if primary is not None:
  assert primary['Q']==Q and primary['left_exact']==str(a) and primary['right_exact']==str(b)
  for name,models in [('P',P),('S',S),('D',D),('H',H),('E',E)]:
   targets=primary['input_coefficients'][name];assert len(targets)==len(models)
   for j,(poly,er) in enumerate(models):
    assert len(targets[j])==len(poly)==Q+1
    for p in range(3):
     for l in range(p,Q+1):
      target=targets[j][l];factor=F(falling(l,p),1)/h**p;lo,hi=F(target['lower_exact'])*factor,F(target['upper_exact'])*factor;v=poly[l]*iq(factor);vlo,vhi=ends(v)
      assert max(lo,vlo)<=min(hi,vhi),('inner independent input jets disjoint',name,j,p,l)
      cross_input_hash.update((name+' '+str(j)+' '+str(p)+' '+str(l)+' '+str(lo)+' '+str(hi)+' '+str(vlo)+' '+str(vhi)+'\n').encode());cross_input_checks+=1
  assert cross_input_checks==(4*261+262)*(3*Q)
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
  if n<262:
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
 t=d['ta']+a;w=iq(d['L']**6)*iv.exp(iq(-4*t))*iv.exp(iq(F(3,2)-d['k'])*iv.log(1+iv.exp(iq(2*t))/iq(d['L']**2)));fac=iv.pi*iq(b-a)*w
 sq=[fac*(bs[0]**2+bs[1]**2+cs[0]**2),fac*((bs[0]+bs[1])**2+(bs[1]+bs[2])**2+(cs[0]+cs[1])**2)]
 return {'left_exact':str(a),'right_exact':str(b),'Q':Q,'max_abs_lambda_h_exact':str(526*h),'input_precision_digits':200,'B':[out(x) for x in bs],'C':[out(x) for x in cs[:2]],'parts':parts,'norm_squares':[out(x) for x in sq],'coefficient_overlap_checks':overlaps,'derivative_input_checks':input_checks,'derivative_input_sha256':input_hasher.hexdigest(),'integer_coefficient_sha256':digest.hexdigest(),'exact_integer_convolutions':8,'cross_method_input_jet_checks':cross_input_checks,'cross_method_input_jet_sha256':cross_input_hash.hexdigest(),'moment_modes':261,'seconds':time.monotonic()-started}
