"""Analytic falling-factorial remainders, full Fourier Arb convolution."""
import sys,os,math,json,hashlib,time,importlib.util
from pathlib import Path
from fractions import Fraction as F
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
sys.dont_write_bytecode=True
from flint import arb,arb_poly,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3]
PATH=ROOT/'research/outer_cells/code/cell_arb.py'
assert hashlib.sha256(PATH.read_bytes()).hexdigest()=='f16dbd13a2362c3ea7f9029af5c7b76ee4ee7a53ece53b9e68251f9641cd122c'
spec=importlib.util.spec_from_file_location('outer180_arb_parent',PATH);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
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
 started=time.monotonic();a,b=F(left),F(right);assert 0<=a<b
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
 beta=d['beta'];rho=[combine(cs,beta,d['r3']) for cs in d['density']]
 D=[combine(cs,beta,d['r3']) for cs in d['dt']];H=[scale(x,arb(2*j+1)) for j,x in enumerate(rho)]
 E=[combine(cs,beta,d['r3']) for cs in d['linear']];P=[];S=[];rates=[v-1 for v in beta]
 for n in range(1,262):
  tr=scale(term([d['hs'][n-1]],F(-2*n-2)),d['r2'])
  P.append(add(combine(d['pv'][n-1],rates,d['r2']),tr));S.append(add(combine(d['sv'][n-1],rates,d['r2']),tr))
 def sums(models):
  ns=[];es=[]
  for p in range(3):
   ns.append(sum((upper(cs[l])*fall(l,p)/ha**p for cs,rs in models for l in range(p,Q+1)),arb(0)).upper())
   es.append(sum((rs[p] for cs,rs in models),arb(0)).upper())
  return ns,es
 norms={name:sums(v) for name,v in [('P',P),('S',S),('D',D),('H',H),('E',E)]}
 def angular(v,freqs,shift,sine):return core.angular([(cs,rs[0]) for cs,rs in v],freqs,shift,sine,Q)
 odd=list(range(1,522,2));even=list(range(2,523,2))
 pe=angular(P,even,522,False);se=angular(S,even,522,True);de=angular(D,odd,521,True);he=angular(H,odd,521,False);le=angular(E,odd,521,True)
 product=pe[0]*de[0]+se[0]*he[0]+arb_poly([arb(0)]*(522*base)+list(le[0]));assert product.degree()<=2086*base+2*Q
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
 tleft=d['tb']+a;weight=aa(d['L']**6)*aa(-4*tleft).exp()*(1+aa(2*tleft).exp()/aa(d['L']**2))**aa(F(3,2)-d['k']);fac=arb.pi()*aa(b-a)*weight
 sq=[fac*(bs[0]**2+bs[1]**2+angs[0]**2),fac*((bs[0]+bs[1])**2+(bs[1]+bs[2])**2+(angs[0]+angs[1])**2)]
 rec={'left_exact':str(a),'right_exact':str(b),'Q':Q,'max_abs_lambda_h_exact':str(524*h),'input_precision_bits':d['input_precision_bits'],'evaluation_precision_bits':512,'B':[out(x) for x in bs],'C':[out(x) for x in angs[:2]],'parts':parts,'norm_squares':[out(x) for x in sq],'seconds':time.monotonic()-started}
 if keep:rec['coefficients']=[[out(x) for x in row] for row in coeffs]
 return rec
