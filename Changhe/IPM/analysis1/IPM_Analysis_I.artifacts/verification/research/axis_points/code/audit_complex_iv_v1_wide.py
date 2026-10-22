"""Independent complex error majorants: interval arithmetic plus exact coefficient bounds.
Does not reevaluate the large real tensor sum. All radial/angle complex boxes are covered.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,hashlib,time,resource
from pathlib import Path
from fractions import Fraction as F
from types import SimpleNamespace
from datetime import datetime,timezone
from mpmath import iv
from flint import fmpq,fmpq_mat
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/axis_points/evidence'
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import exact_poly
iv.dps=65

def utc():return datetime.now(timezone.utc).isoformat()
def emit(**v):print(json.dumps({'utc':utc(),**v}),flush=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(v):return F.from_float(float.fromhex(v))
def q(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
def iq(a,b):return iv.mpf([q(a).a,q(b).b])
def fq(v):return fmpq(v.numerator,v.denominator)
def hull(d):
 def ep(v):
  z=v.strip('[]').split(' +/- ');m=F(z[0]);r=F(z[1]) if len(z)>1 else F(0);return m-r,m+r
 return iq(ep(d['lower'])[0],ep(d['upper'])[1])
def cn(n):return q(F(math.factorial(n)**4,(2*n+1)*math.factorial(2*n)**2))
def inside(v,a,b):return v.a>=q(a).b and v.b<=q(b).a

def main():
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 path=BASE/'data_exact/x3.json';assert sha(path)=='1a8decfb0beb666a36bc14f08514d25b371b778872bdf13d5801c2a4c40b7946'
 coxpath=BASE/'research/canonical_inverse/code/exact_audit.py';assert sha(coxpath)=='331771590a0dd764208306640b4b3af63aec8cfe966ed6a0d086ec512d617b42'
 raw=json.loads(path.read_text());k,L=[q(exact(raw['scalars_hex'][v])) for v in ('k','L')];r0=q(exact(raw['scalars_hex']['origin_radius']))
 p=6+2*k/(2-k);bexp=2/(1-k);Bp=((p-2)/p)**((p-2)/2)*2/p
 z=[exact(v) for v in raw['z_hex']];M=raw['integers']['angular']+1;nb=raw['integers']['degree'];tail=z[1+M*nb:];assert len(tail)==6
 t=[exact(v) for v in raw['spline_knots_hex']];d=SimpleNamespace(t=t,deg=7)
 modes=[[F(0)]+z[1+m*nb:1+(m+1)*nb] for m in range(M)]
 co=[[fq(modes[m][j]) for m in range(M)] for j in range(nb+1)]
 cm=[q(max(map(abs,row))) for row in modes];csum=sum(cm,q(0));ct=q(sum(map(abs,tail),F(0)));globalM=iv.exp(csum+ct*Bp)
 # Convert the degree-five Chebyshev polynomial to exact monomials once.
 Ts=[[F(1)],[F(0),F(1)]]
 for n in range(2,6):
  v=[F(0)]*(n+1)
  for j,c in enumerate(Ts[-1]):v[j+1]+=2*c
  for j,c in enumerate(Ts[-2]):v[j]-=c
  Ts.append(v)
 tc=[sum((tail[n]*(Ts[n][j] if j<len(Ts[n]) else 0) for n in range(6)),F(0)) for j in range(6)]
 def tail_at(qq):
  zz=2*qq-1;v=iv.mpc(0)
  for c in tc[::-1]:v=v*zz+q(c)
  return v
 def radial(a,b,x):
  mid=(a+b)/2;h=(b-a)/2;sp,B=exact_poly(d,a,b);mat=B*fmpq_mat(co[sp-7:sp+1]);rad=iv.sqrt(13)*q(h)
  poly=[]
  for m in range(M):
   # A disc enclosing the whole complex rectangle: |q-mid| <= sqrt(13) h.
   v=sum((q(abs(F(str(mat[l,m]))))*rad**l for l in range(8)),q(0));poly.append(v.b)
  stack=[(mid-3*h,mid+3*h,-2*h,2*h,0)];bound=q(0);min_den=q(1);boxes=0
  while stack:
   ra,rb,ia,ib,depth=stack.pop();qq=iv.mpc(iq(ra,rb),iq(ia,ib));v=1-qq;okay=v.real.a>0
   if okay:
    ss=1-v**bexp;chi_den=ss+r0*r0*(1-ss);beta_den=L*L*ss+x*x*(1-ss)
    okay=ss.real.a>0 and abs(chi_den).a>0 and abs(beta_den).a>0
   if okay:
    chi=ss/chi_den;be=L*L*ss/beta_den;d2=((1-2*be)**2).real.a;okay=d2>0
   if not okay:
    assert depth<18,('radial rectangle could not be covered',str(a),str(b),depth)
    if rb-ra>=ib-ia:
     mm=(ra+rb)/2;stack.extend([(ra,mm,ia,ib,depth+1),(mm,rb,ia,ib,depth+1)])
    else:
     mm=(ia+ib)/2;stack.extend([(ra,rb,ia,mm,depth+1),(ra,rb,mm,ib,depth+1)])
    continue
   assert v.real.a>0 and ss.real.a>0
   chiabs=abs(chi).b;powchi=q(1);lm=q(0)
   for m,pb in enumerate(poly):
    if m>=2:powchi*=chiabs
    lm+=pb*powchi
   lm+=Bp*abs(ss**(p/2)).b*abs(tail_at(qq)).b
   lo=min(q(1),d2);ba=abs(be).b;ker=ba**2*(1+4*ba**2)/lo**2
   vv=iv.exp(lm)*ker;bound=max(bound,vv.b);min_den=min(min_den,lo);boxes+=1
  return q(b-a)*cn(28)*iv.pi/16*bound,boxes,min_den
 def beta_real(v,x):
  ss=1-(1-q(v))**bexp;return L*L*ss/(L*L*ss+x*x*(1-ss))
 def angular(a,b,delta0):
  mid=q((a+b)/2)*iv.pi/2;h=q((b-a)/2)*iv.pi/2;tr=iv.mpf([(mid-2*h).a,(mid+2*h).b]);zz=iv.mpc(tr,iv.mpf([-h.b,h.b]));cc=iv.cos(zz);ss=iv.sin(zz)
  assert cc.real.a>0
  sl=max(q(0),(iv.sin(tr)**2).a);lo=(delta0**2+(1-delta0**2)*sl-((iv.exp(h)-iv.exp(-h))/2)**2).a;assert lo>0,(str(a),str(b),str(lo))
  # Exact spline convex-hull bounds on the real q domain; chi <= 1 and s <= 1.
  lm=sum((cm[m]*abs(iv.cos(2*m*zz)).b for m in range(M)),q(0))+ct*abs(cc**(p-2)*ss**2).b
  ca,sa=abs(cc).b,abs(ss).b;ker=ca**2*sa**2*(1+4*ca**2)/lo**2
  return q(b-a)*iv.pi/2*cn(32)*2**64*iv.exp(lm)*ker
 public={7:{'U':('-54.520','-54.459'),'w':('-15.492','-15.432')},10:{'U':('-41.680','-41.590'),'w':('14.07','14.17')}}
 records=[]
 strainpath=BASE/'research/canonical_inverse/evidence/strain_arb_20_32_result.json';assert sha(strainpath)=='16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db';strain=hull(json.loads(strainpath.read_text())['strain'])
 for tag in ('axis7','axis10'):
  pp=E/(tag+'_partition.json');part=json.loads(pp.read_text());assert part['settings']['nq']==28 and part['settings']['nt']==32;x=q(part['settings']['x']);Er=q(0);boxes=0;mind=q(1)
  for count,(a,b) in enumerate(part['q'],1):
   val,n,lo=radial(F(a),F(b),x);Er+=val;boxes+=n;mind=min(mind,lo)
   if count%50==0:emit(stage='radial',tag=tag,done=count,total=len(part['q']),error=str(Er),boxes=boxes,seconds=time.monotonic()-start)
  ha,hb=map(F,part['removed_q_strip']);delta0=min((1-2*beta_real(ha,x)).a,(2*beta_real(hb,x)-1).a);assert delta0>0
  Et=sum((angular(F(a),F(b),delta0) for a,b in part['theta_over_pi_half']),q(0));cap=F(part['cap_q']);dd=q(F(part['cap_theta_normalized']))*iv.pi/2
  Eh=q(hb-ha)*3*iv.pi/16*globalM;Ec=2*q(cap)*3*iv.pi/16*globalM;Ea=dd**3/3*(1+4*dd**2)/(1-dd**2)**2*iv.exp(csum+ct*dd**(p-2))
  error=Er+Et+Eh+Ec+Ea;entries=[]
  for line in (E/(tag+'_run.log')).read_text().splitlines():
   try:entries.append(json.loads(line))
   except json.JSONDecodeError:pass
  last=[v for v in entries if v.get('stage')=='quadrature'][-1];assert last['done']==last['total']==len(part['q'])
  summation=hull(last['sum']);pref=4*L*L/(iv.pi*(1-k));U=x*pref*(summation+iv.mpf([-error.b,error.b]));w=x*(1+strain)/3+U
  for name,value in [('U',U),('w',w)]:assert inside(value,*public[int(part['settings']['x'])][name]),(tag,name,str(value))
  r={'tag':tag,'partition_sha256':sha(pp),'complex_radial_cells':len(part['q']),'complex_subboxes':boxes,'angular_cells':len(part['theta_over_pi_half']),'errors':{n:str(v) for n,v in [('radial_gauss',Er),('angular_gauss',Et),('singular_strip',Eh),('radial_caps',Ec),('angular_cap',Ea)]},'U':str(U),'w':str(w),'public_bounds':public[int(part['settings']['x'])],'min_radial_denominator':str(mind)};records.append(r);emit(stage='point_complete',**r)
 out={'utc':utc(),'status':'PASS','method':'mpmath.iv65, exact rational Cox polynomials, coefficient absolute-value disc majorants, outward complex rectangle coverage; independent Gaussian remainder and caps; reused one full Arb real quadrature per point','source_sha256':sha(__file__),'Cox_sha256':sha(coxpath),'input_sha256':sha(path),'points':records,'seconds':time.monotonic()-start}
 (E/'complex_iv_audit.json').write_text(json.dumps(out,indent=2)+'\n');emit(stage='done',seconds=out['seconds'])
if __name__=='__main__':main()
