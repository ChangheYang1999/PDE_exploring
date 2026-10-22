"""DRAFT: physical inner Green ODE derivative defects and full Arb convolution."""
import sys,os,math,json,hashlib,time,importlib.util
from pathlib import Path
from fractions import Fraction as F
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
sys.dont_write_bytecode=True
from flint import arb,arb_poly,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3]
PATH=ROOT/'research/inner_cells/code/cell_arb.py'
assert hashlib.sha256(PATH.read_bytes()).hexdigest()=='d926b24078976f62edaf2bd1bae5816ec19e5d514971cb14efa70d458cca3d10'
spec=importlib.util.spec_from_file_location('inner181_arb_parent',PATH);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
core=old.core;aa=old.aa;upper=old.upper;out=old.out

def fall(n,p):return math.factorial(n)//math.factorial(n-p) if n>=p else 0

def setup(Q=16):
 assert 8<=Q<=32
 d=old.setup(Q);ctx.prec=512;ctx.threads=1
 # The reused setup constructs sound384-bit input enclosures.
 # Subsequent derivative models, convolutions and bounds use512 bits.
 d['input_precision_bits']=384;d['evaluation_precision_bits']=512
 return d

def cell(d,left,right,keep=False):
 started=time.monotonic();a,b=F(left),F(right);assert -5<=a<b<=0
 Q=d['Q'];tc=(a+b)/2;h=(b-a)/2;base=2*Q+1;ha=aa(h);tca=aa(tc)
 cache={};hp=[ha**l for l in range(7)];tp=[tca**l for l in range(7)]
 def term(c,lam):
  if all(x.is_zero() for x in c):return ([arb(0)]*(Q+1),[arb(0)]*3)
  assert len(c)<=7
  if lam not in cache:
   ell=aa(lam)*ha;x=upper(ell);fac=(aa(lam)*tca).exp();powers=[arb(1)]
   for q in range(1,Q+1):powers.append(powers[-1]*ell/q)
   tails=[]
   for p in range(3):
    row=[]
    for l in range(7):
     N=Q-l+1;assert N>2
     v=sum((aa(F(math.comb(p,q)*fall(l,p-q),math.factorial(N-q))) for q in range(p+1)),arb(0))
     row.append(fac*x.exp()*x**N*v/ha**p)
    tails.append(row)
   cache[lam]=(powers,fac,tails)
  powers,fac,tails=cache[lam]
  shifted=[hp[l]*sum((math.comb(j,l)*c[j]*tp[j-l] for j in range(l,len(c))),arb(0)) for l in range(len(c))]
  poly=[fac*sum((shifted[l]*powers[q-l] for l in range(min(q,len(c)-1)+1)),arb(0)) for q in range(Q+1)]
  rem=[sum((upper(x)*tails[p][l] for l,x in enumerate(shifted)),arb(0)).upper() for p in range(3)]
  return poly,rem
 def add(x,y):return [u+v for u,v in zip(x[0],y[0])],[upper(u+v) for u,v in zip(x[1],y[1])]
 def scale(x,s):return [v*s for v in x[0]],[upper(v*upper(s)) for v in x[1]]
 def combine(cs,lams,s):
  z=([arb(0)]*(Q+1),[arb(0)]*3)
  for c,lam in zip(cs,lams):z=add(z,term(c,lam))
  return scale(z,s)
 alpha=d['alpha'];zero=([arb(0)]*(Q+1),[arb(0)]*3)
 def mix(ps,offset,s):return combine([[aa(v) for v in p] for p in ps],[al+offset for al in alpha],s)
 def pn(x,p):return sum((upper(x[l])*fall(l,p)/ha**p for l in range(p,len(x))),arb(0)).upper()
 def multiply(x,y):
  full=arb_poly(x[0])*arb_poly(y[0]);cs=[full[l] for l in range(2*Q+1)];errs=[]
  for p in range(3):
   er=sum((upper(cs[l])*fall(l,p)/ha**p for l in range(Q+1,2*Q+1)),arb(0))
   for j in range(p+1):er+=math.comb(p,j)*(pn(x[0],j)*y[1][p-j]+pn(y[0],p-j)*x[1][j]+x[1][j]*y[1][p-j])
   errs.append(er.upper())
  return cs[:Q+1],errs
 def ode(y0,lam,sig,G):
  lam=aa(lam);sig=arb(sig);poly=[y0]
  for q in range(Q):poly.append(ha*(lam*poly[q]+sig*G[0][q])/(q+1))
  defect=upper(lam*poly[Q]+sig*G[0][Q]);rate=upper(lam)
  e0=(upper(lam*ha).exp()*ha*(defect/(Q+1)+G[1][0])).upper()
  e1=(rate*e0+G[1][0]+defect).upper();e2=(rate*e1+G[1][1]+Q*defect/ha).upper()
  return poly,[e0,e1,e2]
 def point_sum(ps,offset):return sum((aa((al+offset)*tc).exp()*sum((aa(v)*tp[l] for l,v in enumerate(p)),arb(0)) for p,al in zip(ps,alpha)),arb(0))
 def derivative(ps):return [[(3+al)*v+((l+1)*p[l+1] if l+1<len(p) else 0) for l,v in enumerate(p)] for p,al in zip(ps,alpha)]
 rho=[];D=[];H=[];Eta=[];ED=[]
 for j,ps in enumerate(d['cs'][:261]):
  rho.append(mix(ps,3,d['R3']));D.append(mix(derivative(ps),3,d['R3']));H.append(scale(rho[-1],arb(2*j+1)))
  es=[[F(0)]]+ps[1:];Eta.append(mix(es,3,d['R3']));ED.append(mix(derivative(es),3,d['R3']))
 E=[zero for _ in range(262)];c=aa(3/d['k']-1)
 for j,(eta,dt) in enumerate(zip(Eta,ED)):
  nu=2*j+1;E[j]=add(E[j],add(scale(dt,1/aa(d['k'])),scale(eta,arb(-1))))
  high=scale(add(scale(eta,arb(nu)),scale(dt,arb(-1))),c/2);E[j+1]=add(E[j+1],high)
  low=scale(add(dt,scale(eta,arb(nu))),c/2 if nu==1 else -c/2);dest=(abs(nu-2)-1)//2;E[dest]=add(E[dest],low)
 P=[];S=[];neg2=scale(term([arb(1)],F(-2)),1/d['R2'])
 for n in range(1,262):
  m=2*n;fs=d['forcing'][n-1];A0=d['R4']*point_sum(d['lower'][n-1],4)
  if n==1:B0=d['R4']*point_sum(d['b1'],4)
  else:
   val=aa(m*tc).exp()*d['B0'][n-1]
   for al,p in zip(alpha,fs):
    if any(p):val+=aa((4+al)*tc).exp()*old.moments.integ([aa(x) for x in p],tc,-tc,4+al-m)
   B0=d['R4']*val
  G=mix(fs,4,d['R4']);Am=ode(A0,-m,1,G);Bm=ode(B0,m,-1,G)
  P.append(scale(multiply(neg2,add(Am,Bm)),arb(-1)/2));S.append(scale(multiply(neg2,add(Bm,scale(Am,arb(-1)))),arb(1)/2))
 def sums(models):
  ns=[];es=[]
  for p in range(3):
   ns.append(sum((upper(cs[l])*fall(l,p)/ha**p for cs,rs in models for l in range(p,Q+1)),arb(0)).upper())
   es.append(sum((rs[p] for cs,rs in models),arb(0)).upper())
  return ns,es
 norms={name:sums(v) for name,v in [('P',P),('S',S),('D',D),('H',H),('E',E)]}
 def angular(v,freqs,shift,sine):return core.angular([(cs,rs[0]) for cs,rs in v],freqs,shift,sine,Q)
 odd=list(range(1,522,2));even=list(range(2,523,2))
 pe=angular(P,even,522,False);se=angular(S,even,522,True);de=angular(D,odd,521,True);he=angular(H,odd,521,False);le=angular(E,list(range(1,524,2)),523,True)
 product=pe[0]*de[0]+se[0]*he[0]+arb_poly([arb(0)]*(520*base)+list(le[0]));assert product.degree()<=2086*base+2*Q
 coeffs=[[product[(1043-nu)*base+l]-product[(1043+nu)*base+l] for l in range(2*Q+1)] for nu in range(1,1044,2)]
 errors=[];bs=[];angs=[];parts=[]
 for p in range(3):
  er=norms['E'][1][p]
  for l in range(p+1):
   for A,B in [('P','D'),('S','H')]:
    na,ea=norms[A];nb,eb=norms[B]
    er+=math.comb(p,l)*(na[l]*eb[p-l]+nb[p-l]*ea[l]+ea[l]*eb[p-l])
  er=er.upper();errors.append(er)
  deriv=[[row[l+p]*fall(l+p,p)/ha**p for l in range(2*Q+1-p)]+[arb(0)]*p for row in coeffs]
  bern=arb_mat([row[:Q+1] for row in deriv])*d['Bern'].transpose()
  modes=[max(upper(bern[n,l]) for l in range(Q+1))+sum((upper(x) for x in deriv[n][Q+1:]),arb(0)) for n in range(522)]
  plain=sum(modes,arb(0)).upper();weighted=sum(((2*n+1)*x for n,x in enumerate(modes)),arb(0)).upper()
  bs.append((plain+er).upper());angs.append((weighted+1043*er).upper());parts.append({'polynomial':out(plain),'theta_polynomial':out(weighted),'error':out(er)})
 tleft=d['ta']+a;weight=aa(d['L']**6)*aa(-4*tleft).exp()*(1+aa(2*tleft).exp()/aa(d['L']**2))**aa(F(3,2)-d['k']);fac=arb.pi()*aa(b-a)*weight
 sq=[fac*(bs[0]**2+bs[1]**2+angs[0]**2),fac*((bs[0]+bs[1])**2+(bs[1]+bs[2])**2+(angs[0]+angs[1])**2)]
 rec={'left_exact':str(a),'right_exact':str(b),'Q':Q,'max_abs_lambda_h_exact':str(522*h),'input_precision_bits':d['input_precision_bits'],'evaluation_precision_bits':512,'B':[out(x) for x in bs],'C':[out(x) for x in angs[:2]],'parts':parts,'norm_squares':[out(x) for x in sq],'seconds':time.monotonic()-started}
 if keep:
  rec['coefficients']=[[out(x) for x in row] for row in coeffs]
  rec['input_coefficients']={name:[[out(x) for x in poly] for poly,errs in vals] for name,vals in [('P',P),('S',S),('D',D),('H',H),('E',E)]}
 return rec
