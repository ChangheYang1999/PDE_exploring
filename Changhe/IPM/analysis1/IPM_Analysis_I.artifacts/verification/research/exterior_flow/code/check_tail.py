"""Two complete exterior-flow enclosures, sharing audited canonical inputs.
Arb: Green forcing plus original-basis exact monomial maxima.
iv: density-moment recurrence plus shifted exponential-series bounds.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/exterior_flow/evidence'
ctx.prec=512;ctx.threads=1;iv.dps=180
Z=(F(0),F(0))
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1<<20),b''):h.update(x)
 return h.hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def dy(x):assert x.is_finite() and x.rad()==0;m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return dy(x.lower()),dy(x.upper())
def ie(x):
 out=[]
 for s,m,e,b in x._mpi_:assert b>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return tuple(out)
def pack(x,method):
 l,h=ae(x) if method=='arb' else ie(x);return {'lower_exact':str(l),'upper_exact':str(h),'display':str(x)}
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def mul(x,q):return tuple(a*q for a in x)
def parse(poly):return [tuple(map(F,x)) for x in poly]
def inv(poly,lam):
 assert lam!=0;out=[Z]*len(poly)
 for l in range(len(poly)-1,-1,-1):out[l]=mul(add(poly[l],mul(out[l+1],-(l+1)) if l+1<len(poly) else Z),1/lam)
 for l in range(len(poly)):assert add(mul(out[l],lam),mul(out[l+1],l+1) if l+1<len(poly) else Z)==poly[l]
 return out

def main():
 assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 for value in [F(0),F(-1),F(3,8),F(-17,64),F(1,3)]:
  l,h=ie(iq(value));assert l<=value<=h
  if value.denominator&(value.denominator-1)==0:assert l==h==value
 for bad in [iv.mpf('inf'),iv.mpf('-inf'),iv.mpf('nan')]:
  try:ie(bad)
  except AssertionError:pass
  else:raise AssertionError('nonfinite endpoint accepted')
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 vp=B/'research/outer_majorant/evidence/verdict.json';assert sha(vp)=='7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac'
 v=json.loads(vp.read_text());assert v['status']=='CONFIRMED';pins={str(vp.relative_to(B)):sha(vp)}
 for f,h in v['files'].items():assert sha(B/f)==h,(f,'dependency changed');pins[f]=h
 cp=B/'research/outer_majorant/evidence/exact_outer_coefficients.json';rp=cp.with_name('outer_result.json');co=json.loads(cp.read_text());old=json.loads(rp.read_text())
 assert sha(cp)=='0e41f96d69aaee902b4c360db5dc4be41abaa6041a620129b16e7d1e5504fb9c'
 tr=B/'data_exact/modal_v2.json';assert sha(tr)==co['input_sha256']==old['dependency_pins']['input']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';pins[str(tr.relative_to(B))]=sha(tr)
 beta=list(map(F,co['beta_exact']));k=F(old['scalars_exact']['k']);cl=1/k;omega=1-k;tb=F(co['tb_exact']);assert k==F(1615536043799051,9007199254740992) and tb==F(2289893859708677,281474976710656) and 0<k<1 and beta[0]==k and len(beta)==11
 assert beta==[k-j*(1-k)-2*l for j,l in [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]]+[3-F(old['scalars_exact']['bo'])]
 zl,zh=map(F,co['correction_parameter_exact_interval']);za=aa(zl).union(aa(zh));zi=iv.mpf([iq(zl).a,iq(zh).b]);assert zl<=zh<0
 def ea(q):return aa(q[0])+aa(q[1])*za
 def ei(q):return iq(q[0])+iq(q[1])*zi
 cs=[]
 for j,row in enumerate(co['rows']):
  assert row['j']==j and len(row['basis'])==11;c=[parse(x) for x in row['basis']];assert [len(x) for x in c]==[1]*10+[7];cs.append(c)
 assert len(cs)==262 and all(x==Z for p in cs[-1] for x in p) and len(old['green'])==261
 modes=[];identities=overlaps=boundary=ode=0;mind=None
 for n,row in enumerate(old['green'],1):
  assert row['n']==n;assert len(row['plus_exact'])==len(row['minus_exact'])==11;m=2*n
  i0=row['i_right'];i0i=iv.mpf([iq(F(i0['lower_exact'])).a,iq(F(i0['upper_exact'])).b]);Ci=i0i;polys=[]
  for z,b in enumerate(beta):
   left,right=cs[n-1][z],cs[n][z];li=b+1+m;lj=b+1-m;assert li!=0 and lj<0
   md=min(abs(li),abs(lj));mind=md if mind is None else min(mind,md)
   qi=inv(left,li);qj=[mul(x,-1) for x in inv(right,lj)];ode+=len(qi)+len(qj);Ci-=ei(qi[0]);qp=parse(row['plus_exact'][z]);qm=parse(row['minus_exact'][z]);assert len(qp)==len(qm)==len(left)
   pa=[];sa=[];pi=[];si=[]
   for l in range(len(left)):
    H=mul(add(left[l],right[l]),F(1,2));assert qp[l]==add(H,mul(qi[l],-m));assert qm[l]==add(mul(H,-1),mul(qj[l],m));identities+=2
    p=mul(add(qp[l],qm[l]),F(-1,2));s=mul(add(qm[l],mul(qp[l],-1)),F(1,2));p2=mul(add(qi[l],mul(qj[l],-1)),F(m,2));s2=add(mul(add(qi[l],qj[l]),F(m,2)),mul(H,-1));assert p==p2 and s==s2;identities+=2
    xa,ya,xi,yi=ea(p),ea(s),ei(p2),ei(s2)
    for u,w in [(xa,xi),(ya,yi)]:a1,a2=ae(u);b1,b2=ie(w);assert max(a1,b1)<=min(a2,b2);overlaps+=1
    pa.append(xa);sa.append(ya);pi.append(xi);si.append(yi)
   polys.append((1-b,pa,sa,pi,si))
  hb=row['H_over_R4'];hal=aa(F(hb['lower_exact'])).union(aa(F(hb['upper_exact'])));ha=-hal/2;hi=iq(F(m,2))*Ci
  x,y=ae(ha),ie(hi);assert max(x[0],y[0])<=min(x[1],y[1]);boundary+=1
  modes.append((m,polys,ha,hi))
 assert identities==17748 and overlaps==8874 and boundary==261 and ode==8874
 r2a=aa(2*tb).exp();r2i=iv.exp(iq(2*tb));cases=[];scalar_checks=0
 for T in [F(0),F(1,16),F(1,8),F(1,4),F(1),F(9)]:
  P=arb(0);Q=arb(0);Pi=iv.mpf(0);Qi=iv.mpf(0);max_cache={};iv_cache={}
  def ab(poly,a):
   d=a-omega;assert d>=0
   if d==0:assert len(poly)==1;return abs(poly[0])*aa(-a*T).exp()
   total=arb(0)
   for l,c in enumerate(poly):
    key=(d,l)
    if key not in max_cache:
     x=max(T,F(l)/d);max_cache[key]=aa(x**l)*aa(-d*x-omega*T).exp()
    total+=abs(c)*max_cache[key]
   return total
  def ib(poly,a):
   d=a-omega;assert d>=0
   if d==0:assert len(poly)==1;return abs(poly[0])*iv.exp(iq(-a*T))
   key=(a,len(poly))
   if key not in iv_cache:iv_cache[key]=[iv.exp(iq(-a*T))*iq(F(math.factorial(j))/d**j) for j in range(len(poly))]
   total=iv.mpf(0)
   for j in range(len(poly)):
    shifted=iv.mpf(0)
    for l in range(j,len(poly)):shifted+=poly[l]*iq(F(math.comb(l,j))*T**(l-j))
    total+=abs(shifted)*iv_cache[key][j]
   return total
  for m,polys,ha,hi in modes:
   x=ab([ha],F(m+2));y=ib([hi],F(m+2));P+=x;Q+=(m+1)*x;Pi+=y;Qi+=(m+1)*y
   for a,pa,sa,pi,si in polys:
    x=ab(pa,a);z=ab(sa,a);y=ib(pi,a);w=ib(si,a);P+=x;Q+=x+m*z;Pi+=y;Qi+=y+m*w
  P*=r2a;Q*=r2a;Pi*=r2i;Qi*=r2i
  jointp=max(ae(P)[1],ie(Pi)[1]);jointq=max(ae(Q)[1],ie(Qi)[1]);ra=aa(tb+T).exp();ri=iv.exp(iq(tb+T));assert max(ae(ra)[0],ie(ri)[0])<=min(ae(ra)[1],ie(ri)[1]);scalar_checks+=1
  cases.append({'T_exact':str(T),'P_arb':pack(P,'arb'),'P_iv':pack(Pi,'iv'),'Q_arb':pack(Q,'arb'),'Q_iv':pack(Qi,'iv'),'joint_P_upper_exact':str(jointp),'joint_Q_upper_exact':str(jointq),'radius_arb':pack(ra,'arb'),'radius_iv':pack(ri,'iv'),'radial_drift_lower_exact':str(cl-jointp),'both_component_drift_lower_exact':str(cl-jointq)})
  print(json.dumps({'utc':utc(),'T':str(T),'P_arb':str(P),'P_iv':str(Pi),'Q_arb':str(Q),'Q_iv':str(Qi)}),flush=True)
 # Exact cosine-polynomial identity behind |sin(m theta)| <= m sin(theta),
 # represented by the m unit complex summands of (z^m-z^-m)/(z-z^-1).
 angular=0
 for m in range(2,523,2):
  terms=list(range(-(m-1),m,2));d={}
  for l in terms:d[l+1]=d.get(l+1,0)+1;d[l-1]=d.get(l-1,0)-1
  assert {p:c for p,c in d.items() if c}=={m:1,-m:-1};assert len(terms)==m;angular+=1
 out={'utc':utc(),'status':'PASS_COMPUTATION_REQUIRES_ADVERSARIAL_AUDIT','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/exterior_flow/PROOF.md'),'dependencies_sha256':pins,'parameters_exact':{'k':str(k),'cl':str(cl),'omega':str(omega),'tb':str(tb)},'checks':{'exact_affine_identities':identities,'velocity_coefficient_overlaps':overlaps,'boundary_overlaps':boundary,'density_ode_coefficients':ode,'angular_Laurent_identities':angular,'radius_overlaps':scalar_checks,'minimum_abs_denominator_exact':str(mind)},'cases':cases,'runtime':{'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_decimal_digits':iv.dps,'endpoint_rational_contracts':5,'nonfinite_rejections':3},'seconds':time.monotonic()-start,'scope':'Entire exterior velocity, polar radial quotient, both Cartesian axis quotients and conditional outward-drift scalar bounds. Shared previously audited canonical boundary integrals. No finite-domain flow, coupled inverse or endpoint.'}
 tmp=E/'checks.json.tmp';tmp.write_text(json.dumps(out,indent=2)+'\n');os.replace(tmp,E/'checks.json');print(json.dumps({'utc':utc(),'status':out['status'],'checks':out['checks'],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
