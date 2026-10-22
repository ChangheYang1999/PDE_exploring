"""Nine dyadic cases: Arb vectors versus independent iv direct sums."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,hashlib,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];E=B/'research/double_remainder/evidence'
CASES=['SS','SL','LS','LL','SC','LC','CS','CL','CC']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ii(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ae(x):
 assert x.is_finite()
 def f(y):assert y.rad()==0;m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return f(x.lower()),f(x.upper())
def ie(x):
 out=[]
 for s,m,e,b in x._mpi_:assert b>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return tuple(out)
def pair(x,m):return ae(x) if m=='arb' else ie(x)
def pack(x,m):l,h=pair(x,m);return {'lower_exact':str(l),'upper_exact':str(h),'display':str(x)}
def maxima(xs,m):
 bounds=[pair(x,m) for x in xs];l=max(x[0] for x in bounds);h=max(x[1] for x in bounds)
 return aa(l).union(aa(h)) if m=='arb' else iv.mpf([ii(l).a,ii(h).b])
def arb_cases(N,M):
 def vec(n,kind):
  if kind=='S':return {n:aa(F(2)**(n+1)*F(4,3)**(n+1)/math.factorial(n))}
  if kind=='C':return {p:aa(F(4)*8**p/math.factorial(p)) for p in range(n)}
  v={p:aa(F(2)**(p+1)/math.factorial(p)) for p in range(n)} if kind=='L' else vec(n,'C')
  v[0]=v.get(0,arb(0))+(aa(F(8,3)) if kind=='L' else arb.pi());return v
 def D(p,q):return arb(math.factorial(p+q+1))/(2*arb.pi())
 def dot(v,w):return sum((x*y*D(p,q) for p,x in v.items() for q,y in w.items()),arb(0))
 out={}
 for c in CASES[:-1]:out[c]=dot(vec(N,'J' if c[0]=='C' else c[0]),vec(M,'J' if c[1]=='C' else c[1]))
 vx,vy=vec(N,'C'),vec(M,'C');out['CC']=1+arb.pi()*sum((x*D(p,0) for p,x in vx.items()),arb(0))+arb.pi()*sum((y*D(0,q) for q,y in vy.items()),arb(0))+dot(vx,vy)
 return out

def iv_cases(n,m):
 # Separate implementation from the explicit estimates, without vector construction.
 def fact(k):
  v=1
  for j in range(2,k+1):v*=j
  return v
 def d(p,q):return iv.mpf(fact(p+q+1))/(2*iv.pi)
 def small(k):return ii(F(2)**(k+1)*F(4,3)**(k+1)/fact(k))
 def large(k):return ii(F(2)**(k+1)/fact(k))
 def corr(k):return ii(F(4)*8**k/fact(k))
 sn,sm=small(n),small(m);v=ii(F(8,3));z=iv.mpf(0)
 out={'SS':sn*sm*d(n,m),
      'SL':sn*(v*d(n,0)+sum((large(q)*d(n,q) for q in range(m)),z)),
      'LS':sm*(v*d(0,m)+sum((large(p)*d(p,m) for p in range(n)),z)),
      'SC':sn*(iv.pi*d(n,0)+sum((corr(q)*d(n,q) for q in range(m)),z)),
      'CS':sm*(iv.pi*d(0,m)+sum((corr(p)*d(p,m) for p in range(n)),z))}
 out['LL']=v*v*d(0,0)+v*sum((large(p)*d(p,0) for p in range(n)),z)+v*sum((large(q)*d(0,q) for q in range(m)),z)+sum((large(p)*large(q)*d(p,q) for p in range(n) for q in range(m)),z)
 out['LC']=v*iv.pi*d(0,0)+iv.pi*sum((large(p)*d(p,0) for p in range(n)),z)+v*sum((corr(q)*d(0,q) for q in range(m)),z)+sum((large(p)*corr(q)*d(p,q) for p in range(n) for q in range(m)),z)
 out['CL']=v*iv.pi*d(0,0)+iv.pi*sum((large(q)*d(0,q) for q in range(m)),z)+v*sum((corr(p)*d(p,0) for p in range(n)),z)+sum((corr(p)*large(q)*d(p,q) for p in range(n) for q in range(m)),z)
 out['CC']=1+iv.pi*sum((corr(p)*d(p,0) for p in range(n)),z)+iv.pi*sum((corr(q)*d(0,q) for q in range(m)),z)+sum((corr(p)*corr(q)*d(p,q) for p in range(n) for q in range(m)),z)
 return out

def arb_L(n,a):
 d,e=F(n)+F(1,2)-a,a-F(n)+F(1,2);assert d>0 and e>0
 def pow2(x):return (aa(x)*arb(2).log()).exp()
 return sum((pow2(-a*j) for j in range(-2,3)),arb(0))+pow2(-3*d)/(1-pow2(-d))+pow2(-3*e)/(1-pow2(-e))

def iv_L(n,a):
 # Explicit 128-term tail sums and the exact geometric remainder after them.
 d,e=F(n)+F(1,2)-a,a-F(n)+F(1,2);assert d>0 and e>0
 def pow2(x):return iv.power(2,ii(x))
 value=sum((pow2(-a*j) for j in [-2,-1,0,1,2]),iv.mpf(0));tails=[]
 for delta in [d,e]:
  r=pow2(-delta);assert ie(r)[1]<1;term=r**3;partial=iv.mpf(0)
  for unused in range(128):partial+=term;term*=r
  remainder=term/(1-r);value+=partial+remainder
  tails.append({'delta_exact':str(delta),'terms':128,'first_power':3,'remainder_first_power':131,'ratio':pack(r,'iv'),'remainder':pack(remainder,'iv')})
 return value,tails

def main():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 contracts=0
 for q in [F(0),F(1),F(-7,8),F(1,3),F(1299,200)]:
  for v in [ae(aa(q)),ie(ii(q))]:assert v[0]<=q<=v[1];contracts+=1
 rejects=0
 for x in [iv.mpf('inf'),iv.mpf('-inf'),iv.mpf('nan')]:
  try:ie(x)
  except AssertionError:rejects+=1
  else:raise AssertionError('nonfinite accepted')
 rows=[];overlaps=0
 for n,m,a,b in [(6,3,F('6.45'),F('3.07')),(6,3,F('6.495'),F('3.403')),(0,0,F(0),F(0)),(0,3,F('-.49'),F('3.07')),(6,0,F('6.45'),F('.49')),(1,1,F(1),F(1))]:
  A=arb_cases(n,m);I=iv_cases(n,m);br=[]
  for c in CASES:
   al,ah=ae(A[c]);il,ih=ie(I[c]);assert max(al,il)<=min(ah,ih);overlaps+=1;br.append({'case':c,'arb':pack(A[c],'arb'),'iv':pack(I[c],'iv')})
  ba=maxima(list(A.values()),'arb');bi=maxima(list(I.values()),'iv');la,ma=arb_L(n,a),arb_L(m,b);li,lt=iv_L(n,a);mi,mt=iv_L(m,b)
  ca=(aa(abs(a)+abs(b))*arb(2).log()).exp()*ba*la*ma;ci=iv.power(2,ii(abs(a)+abs(b)))*bi*li*mi
  for v,w in [(ba,bi),(la,li),(ma,mi),(ca,ci)]:
   al,ah=ae(v);il,ih=ie(w);assert max(al,il)<=min(ah,ih);overlaps+=1
  upper=max(ae(ca)[1],ie(ci)[1]);lower=min(ae(ca)[0],ie(ci)[0]);ten=1
  while F(10)**ten<=upper:ten+=1
  assert 0<lower<=upper<F(10)**ten
  rows.append({'N':n,'M':m,'a_exact':str(a),'b_exact':str(b),'nine_cases':br,'B':{'arb':pack(ba,'arb'),'iv':pack(bi,'iv')},'Lx':{'arb':pack(la,'arb'),'iv':pack(li,'iv')},'Ly':{'arb':pack(ma,'arb'),'iv':pack(mi,'iv')},'C':{'arb':pack(ca,'arb'),'iv':pack(ci,'iv')},'iv_geometric_tails':{'x':lt,'y':mt},'joint_C_lower_exact':str(lower),'joint_C_upper_exact':str(upper),'strict_power10_upper_exponent':ten})
  print(json.dumps({'N':n,'M':m,'a':str(a),'b':str(b),'B':str(ba),'C':str(ca),'power10_upper':ten}),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SCALARS','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/double_remainder/PROOF.md'),'lead_snapshot_sha256':sha(E/'lead_corner_coupling.md'),'runtime':{'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_decimal_digits':iv.dps},'checks':{'endpoint_containments':contracts,'nonfinite_rejections':rejects,'case_and_global_overlaps':overlaps,'rows':len(rows)},'rows':rows,'seconds':time.monotonic()-start,'scope':'Explicit double-remainder constants only; no coupled operator or canonical moments on completed pure-weight data.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
