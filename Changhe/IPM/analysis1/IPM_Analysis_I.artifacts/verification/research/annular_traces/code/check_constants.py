"""Arb formula evaluation and independently arranged positive-integral iv bounds."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,hashlib,time,resource
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/annular_traces/evidence'
TRACES=[('u10',False,0,1),('u12',False,2,1),('u21',False,1,0),('v11',True,1,0),('v13',True,3,0),('v15',True,5,0),('v20',True,0,1),('v22',True,2,1),('v24',True,4,1)]
PARAMS=[(F('6.45'),F('3.07')),(F('6.495'),F('3.403'))]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ii(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ae(x):
 assert x.is_finite()
 def one(y):assert y.rad()==0;m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return one(x.lower()),one(x.upper())
def ie(x):
 out=[]
 for s,m,e,b in x._mpi_:assert b>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return tuple(out)
def interval(l,h):assert l<=h;return iv.mpf([ii(l).a,ii(h).b])
def pack(x,method):l,h=ae(x) if method=='arb' else ie(x);return {'lower_exact':str(l),'upper_exact':str(h),'display':str(x)}
def amax(v):
 z=[ae(x) for x in v];return aa(max(x[0] for x in z)).union(aa(max(x[1] for x in z)))
def imax(v):
 z=[ie(x) for x in v];return interval(max(x[0] for x in z),max(x[1] for x in z))
def powi(x,p):
 x,p=F(x),F(p)
 if x==0:assert p>0;return iv.mpf(0)
 assert x>0;return iv.exp(ii(p)*iv.log(ii(x)))
def positive_integral(kind,p,q=None,N=4096,T=64):
 """Endpoint/unique-maximum sums, exact rational mesh; independent of special functions."""
 p=F(p);assert p>1
 if kind=='beta':
  q=F(q);assert q>1;left,right=F(0),F(1);peak=(p-1)/(p+q-2)
  def val(t):return iv.mpf(0) if t in (0,1) else powi(t,p-1)*powi(1-t,q-1)
 elif kind=='gamma':
  left,right=F(0),F(T);assert right>p-1;peak=p-1
  def val(t):return iv.mpf(0) if t==0 else powi(t,p-1)*iv.exp(-ii(t))
 else:raise ValueError(kind)
 step=(right-left)/N;last=val(left);lower=F(0);upper=F(0);vpeak=val(peak);critical=0
 for n in range(N):
  l=left+n*step;r=l+step;new=val(r);lo=min(ie(last)[0],ie(new)[0]);hi=max(ie(last)[1],ie(new)[1])
  if l<=peak<=r:hi=max(hi,ie(vpeak)[1]);critical+=1
  assert 0<=lo<=hi;lower+=step*lo;upper+=step*hi;last=new
 assert critical in (1,2)
 tail=iv.mpf(0)
 if kind=='gamma':tail=val(right)/(1-ii((p-1)/right));assert ie(tail)[0]>0;upper+=ie(tail)[1]
 value=interval(lower,upper)
 record={'kind':kind,'p_exact':str(p),'q_exact':None if q is None else str(q),'cells':N,'left_exact':str(left),'right_exact':str(right),'peak_exact':str(peak),'critical_cells':critical,'sum_lower_exact':str(lower),'sum_upper_with_tail_exact':str(upper),'tail_upper':pack(tail,'iv'),'enclosure':pack(value,'iv')}
 print(json.dumps({'stage':'positive_integral','kind':kind,'p':str(p),'q':str(q),'value':str(value)}),flush=True)
 return value,record

def arb_row(a,b,j,parity):
 A=a+b;t=A-j-1;sig=b-j-F(1,2);s=sig.numerator//sig.denominator;theta=sig-s;K=s+1
 assert sig>0 and 0<theta<1
 ls=[p for p in range(24) if p%2==parity and p<t];P=min(p for p in range(24) if p%2==parity and p>t)
 assert all(F(p)!=t for p in range(24) if p%2==parity)
 mu=t-max(ls) if ls else A+1
 def d(l):return arb(math.factorial(l+j+1))/(2*arb.pi())
 def p2(x):return (aa(x)*arb(2).log()).exp()
 Q=(2*(aa(a+F(1,2)).gamma()*aa(b+F(1,2)).gamma()/aa(A+1).gamma())*(p2(2*A+2)-1)/aa(2*A+2)).sqrt()
 J=aa(2*(s+1)+4+F(2)/((1-theta)*(3-2*theta))).sqrt();S=aa(s+1+F(1)/(1-theta)+F(4)/theta).sqrt()
 hs={p:max(F(math.factorial(p),math.factorial(p-d))*2**(p-d) for d in range(min(K,p)+1)) for p in ls}
 flow=p2(b)/(math.factorial(j)*aa(2*b+1).sqrt());fhigh=p2(-b-1)*aa(2*b+1).gamma().sqrt()/math.factorial(j)
 FF=p2(sig/2)*amax([flow,fhigh])
 near=Q*J/math.factorial(j)*amax([aa(F(2)**max(P-d0,0)/math.factorial(max(P-d0,0)))*d(max(P,d0))*aa(F(4,3))**(2+j+max(P,d0)) for d0 in range(K+1)])
 far=Q*J*(amax([d(d0)*aa(F(4,3))**(2+j+d0) for d0 in range(K+1)])/math.factorial(j)+sum((aa(hs[p])*d(p)/math.factorial(p)/math.factorial(j) for p in ls),arb(0)))
 mid=aa(4)**aa(abs(t))*(2*aa(4)**aa(sig)*S*p2(a)*FF+Q*J*sum((aa(4**p*hs[p])*d(p)/math.factorial(p)/math.factorial(j) for p in ls),arb(0)))
 near_tail=p2(-3*(P-t))/(1-p2(-(P-t)));far_tail=p2(-3*mu)/(1-p2(-mu));total=near*near_tail+5*mid+far*far_tail
 return {'a_exact':str(a),'b_exact':str(b),'j':j,'parity':parity,'t_exact':str(t),'sigma_exact':str(sig),'s':s,'theta_exact':str(theta),'K':K,'powers':ls,'P':P,'near_exponent_exact':str(P-t),'far_exponent_exact':str(mu),'H_exact':{str(p):str(v) for p,v in hs.items()}},{'Q':Q,'J':J,'S':S,'F_low':flow,'F_high':fhigh,'F':FF,'C_near':near,'C_far':far,'C_mid':mid,'near_tail':near_tail,'far_tail':far_tail,'C':total}

def iv_row(a,b,j,parity,beta,gamma):
 # Independently arranged from derivative bounds on every individual monomial.
 totalweight=a+b;degree_gap=totalweight-1-j;sigma=b-F(1,2)-j
 s=0
 while s+1<sigma:s+=1
 theta=sigma-s;K=s+1;assert 0<theta<1
 powers=[];p=parity
 while p<degree_gap:powers.append(p);p+=2
 assert p>degree_gap;P=p;delta=P-degree_gap;mu=degree_gap-powers[-1] if powers else totalweight+1
 Q=iv.sqrt(beta*2*(iv.power(2,ii(2*totalweight+2))-1)/ii(2*totalweight+2))
 J=iv.sqrt(2*K+4+2/(ii(1-theta)*ii(3-2*theta)))
 S=iv.sqrt(K+1/ii(1-theta)+4/ii(theta))
 low=iv.power(2,ii(b))/(math.factorial(j)*iv.sqrt(ii(2*b+1)))
 high=iv.sqrt(gamma)*iv.power(2,ii(-b-1))/math.factorial(j)
 FF=iv.power(2,ii(sigma/2))*imax([low,high])
 def kernel(n):
  v=iv.mpf(1)/(2*iv.pi)
  for d in range(1,n+j+2):v*=d
  return v
 hs={}
 for p in powers:
  vals=[]
  for d in range(min(p,K)+1):
   deriv=F(1)
   for z in range(d):deriv*=p-z
   vals.append(deriv*F(2)**(p-d))
  hs[p]=max(vals)
 near_terms=[];primary_terms=[]
 for d in range(K+1):
  n=max(P,d);factor=F(1)
  for z in range(1,max(P-d,0)+1):factor*=F(2,z)
  near_terms.append(ii(factor*F(4,3)**(2+j+n))*kernel(n))
  primary_terms.append(ii(F(4,3)**(2+j+d))*kernel(d))
 near=imax(near_terms)*Q*J/math.factorial(j)
 moments=[ii(hs[p])*kernel(p)/(math.factorial(p)*math.factorial(j)) for p in powers]
 far=Q*J*(imax(primary_terms)/math.factorial(j)+sum(moments,iv.mpf(0)))
 poly_mid=sum((ii(4**p)*v for p,v in zip(powers,moments)),iv.mpf(0))
 mid=iv.power(4,ii(abs(degree_gap)))*(2*iv.power(4,ii(sigma))*S*iv.power(2,ii(a))*FF+Q*J*poly_mid)
 tails=[];records=[]
 for gap in [delta,mu]:
  ratio=iv.power(2,-ii(gap));assert 0<ie(ratio)[0]<=ie(ratio)[1]<1
  term=ratio**3;partial=iv.mpf(0)
  for unused in range(128):partial+=term;term*=ratio
  remainder=term/(1-ratio);tails.append(partial+remainder)
  records.append({'gap_exact':str(gap),'terms':128,'first_power':3,'remainder_first_power':131,'ratio':pack(ratio,'iv'),'remainder':pack(remainder,'iv')})
 return {'Q':Q,'J':J,'S':S,'F_low':low,'F_high':high,'F':FF,'C_near':near,'C_far':far,'C_mid':mid,'near_tail':tails[0],'far_tail':tails[1],'C':near*tails[0]+5*mid+far*tails[1]},records,{'powers':powers,'P':P,'s':s,'K':K,'H_exact':{str(p):str(v) for p,v in hs.items()}}

def main():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 count=0
 for q in [F(0),F(-7,8),F(1,3),F(1299,200),F(1,10**40)]:
  for lo,hi in [ae(aa(q)),ie(ii(q))]:assert lo<=q<=hi;count+=1
 rejects=0
 for v in [iv.mpf('nan'),iv.mpf('inf'),iv.mpf('-inf')]:
  try:ie(v)
  except AssertionError:rejects+=1
  else:raise AssertionError('nonfinite accepted')
 integral_records=[];rows=[];overlaps=0;special_contains=0
 for orig_a,orig_b in PARAMS:
  beta,br=positive_integral('beta',orig_a+F(1,2),orig_b+F(1,2));integral_records.append(br)
  ab=aa(orig_a+F(1,2)).gamma()*aa(orig_b+F(1,2)).gamma()/aa(orig_a+orig_b+1).gamma()
  assert ie(beta)[0]<=ae(ab)[0]<=ae(ab)[1]<=ie(beta)[1];special_contains+=1
  gammas={}
  for b in [orig_a,orig_b]:
   g,gr=positive_integral('gamma',2*b+1);integral_records.append(gr);gammas[b]=g
   ag=aa(2*b+1).gamma();assert ie(g)[0]<=ae(ag)[0]<=ae(ag)[1]<=ie(g)[1];special_contains+=1
  for label,swap,j,parity in TRACES:
   a,b=(orig_b,orig_a) if swap else (orig_a,orig_b)
   meta,av=arb_row(a,b,j,parity);ivv,traces,imeta=iv_row(a,b,j,parity,beta,gammas[b])
   assert all(meta[k]==v for k,v in imeta.items())
   vals={}
   for key,v in av.items():
    x,y=ae(v);l,h=ie(ivv[key]);assert max(l,x)<=min(h,y),(label,key);overlaps+=1;vals[key]={'arb':pack(v,'arb'),'iv':pack(ivv[key],'iv')}
   lo=min(ae(av['C'])[0],ie(ivv['C'])[0]);hi=max(ae(av['C'])[1],ie(ivv['C'])[1]);assert 0<lo<=hi
   unit=F(1)
   while hi>=unit*10000:unit*=10
   while hi<unit*1000:unit/=10
   ceiling=(hi//unit+1)*unit;assert hi<ceiling and ceiling/unit==int(ceiling/unit)
   row={'trace':label,'original_a_exact':str(orig_a),'original_b_exact':str(orig_b),'metadata':meta,'constants':vals,'iv_dyadic_tails':traces,'joint_C_lower_exact':str(lo),'joint_C_upper_exact':str(hi),'strict_public_C_upper_exact':str(ceiling)};rows.append(row)
   print(json.dumps({'trace':label,'a':str(orig_a),'b':str(orig_b),'C_arb':str(av['C']),'C_iv':str(ivv['C']),'strict_public_upper':str(ceiling)}),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_METHOD_CONSTANTS','source_sha256':sha(__file__),'proof_sha256':sha(BASE/'research/annular_traces/PROOF.md'),'runtime':{'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_decimal_digits':iv.dps},'checks':{'endpoint_containments':count,'nonfinite_rejections':rejects,'special_function_containments':special_contains,'constant_overlaps':overlaps,'rows':len(rows)},'positive_integrals':integral_records,'rows':rows,'seconds':time.monotonic()-start,'scope':'Annular traces with natural homogeneous subtraction only; no coupled inverse, canonical moments on pure-weight completion, or PDE endpoint.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['rows','positive_integrals']}))
if __name__=='__main__':main()
