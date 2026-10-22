"""All-mode residual samples via independent density moments; no numerics code imports."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,time,hashlib,resource,bisect,itertools
import numpy as np
from pathlib import Path
from fractions import Fraction as F
from types import SimpleNamespace
from datetime import datetime,timezone
from flint import arb,ctx,fmpq,fmpq_mat
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import exact_poly
sys.path.insert(0,str(BASE/'research/exponential_moments/code'))
from moments import aa,phi
E=BASE/'research/residual_samples/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import export_ball
def utc():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(v):return F.from_float(float.fromhex(v))
def fq(v):return fmpq(v.numerator,v.denominator)
def dyad(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def out(x):return {'display':x.str(34),'lower_exact':str(dyad(x.lower())),'upper_exact':str(dyad(x.upper()))}
def main():
 ctx.prec=320;ctx.threads=1;ctx.cap=8;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 path=BASE/'data_exact/modal_v2.json';assert sha(path)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(path.read_text());ar=raw['arrays'];M,nb=ar['S']['shape'];t=[exact(v) for v in ar['knots']['hex']];sc={k:exact(v) for k,v in raw['scalars_hex'].items()};k,bi,bo=(sc[v] for v in ('k','bi','bo'));cl=1/aa(k)
 assert raw['degree']==7 and t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8 and len(t)==nb+8
 assert all(t[i]<t[i+1] for i in range(7,nb)) and 0<k<1 and bi>0
 alpha=[k-3-j*(1-k)-2*l for j,l in raw['outer_jl']]
 def get(name,m,j):return exact(ar[name]['hex'][m*ar[name]['shape'][1]+j])
 weights=[{} for _ in range(M+2)]
 for m in range(M):
  for f in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(f)-1)//2;weights[j][m]=weights[j].get(m,F(0))+F(1 if f>0 else -1,8)
 weights=[{m:w for m,w in row.items() if w} for row in weights];assert weights[-1]=={}
 sd=[[sum((w*get('S',m,l) for m,w in ws.items()),F(0)) for ws in weights] for l in range(nb)]
 def jets(c,kn,right):
  result=[]
  for p in range(7,0,-1):
   result.append(c[-1] if right else c[0]);c=[p*(c[i+1]-c[i])/(kn[i+p+1]-kn[i+1]) for i in range(len(c)-1)];kn=kn[1:-1]
  return result
 def corr(J,P,b):return [sum(((-b)**(i-l)*(J[l]-P[l])/math.factorial(l)/math.factorial(i-l) for l in range(i+1)),F(0)) for i in range(7)]
 zpath=BASE/'research/modal_repair/evidence/independent_gauss_iv.json';zr=json.loads(zpath.read_text())['values']['A00_correction'];z=aa(F(zr['lower_exact_dyadic'])).union(aa(F(zr['upper_exact_dyadic'])))
 inn=[];outer=[]
 for j,ws in enumerate(weights):
  C=ws.get(0,F(0));D=[sum((w*get('D',m,l) for m,w in ws.items()),F(0)) for l in range(7)];A=[sum((w*get('Aout',m,l) for m,w in ws.items()),F(0)) for l in range(len(alpha))]
  ji=jets([sd[l][j] for l in range(8)],t[:16],False);jo=jets([sd[l][j] for l in range(nb-8,nb)],t[-16:],True)
  pi=[sum((D[l]*(2*l+2)**v for l in range(7)),C if v==0 else F(0)) for v in range(7)];po=[sum((A[l]*alpha[l]**v for l in range(len(alpha))),F(0)) for v in range(7)]
  ei=corr(ji,pi,bi);eo=[aa(v) for v in corr(jo,po,-bo)];A=[aa(v) for v in A];A[0]+=aa(C)*z
  for l in range(7):eo[l]-=aa(C*(alpha[0]+bo)**l/F(math.factorial(l)))*z
  inn.append((C,D,ei));outer.append((A,eo))
 ns=range(1,M+2);iv=[];jv=[]
 for n in ns:
  m=2*n;C,D,ei=inn[n-1];A,eo=outer[n]
  assert all(m-4-v>0 for v in alpha) and m-4+bo>0
  iv.append(aa(C/F(m+4)+sum((D[l]/(m+6+2*l) for l in range(7)),F(0))+sum((ei[l]*(-1)**l*math.factorial(l)/(m+4+bi)**(l+1) for l in range(7)),F(0))))
  jv.append(sum((A[l]/aa(m-4-alpha[l]) for l in range(len(alpha))),arb(0))+sum((eo[l]*math.factorial(l)/aa(m-4+bo)**(l+1) for l in range(7)),arb(0)))
 # The comparison artifact supplies integer subdivision counts only, never velocity data.
 green=BASE.parent/'ipmA-num/data/cert_green.npz';gsha=sha(green)
 assert gsha=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
 gg=np.load(green,allow_pickle=False);parent=gg['parent'];tbm,tbr=gg['tb'],gg['tb_rad'];original=list(zip(sorted(set(t))[:-1],sorted(set(t))[1:]))
 groups=[(int(i),len(list(v))) for i,v in itertools.groupby(parent)]
 assert [i for i,c in groups]==list(range(len(original)))
 tb=[]
 for (a,b),(p,count) in zip(original,groups):tb.extend(a+(b-a)*F(v,count) for v in range(count))
 tb.append(t[-1]);assert len(tb)==len(parent)+1==len(tbm)==len(tbr)
 for i,v in enumerate(tb):
  m,r=F.from_float(float(tbm[i])),F.from_float(float(tbr[i]));assert r>=0 and m-r<=v<=m+r
 numpath=BASE.parent/'ipmA-num/runs/cert_resid_middle.json';rawnum=numpath.read_bytes();numsha=hashlib.sha256(rawnum).hexdigest();nr=json.loads(rawnum);assert nr['done'] and len(nr['rows'])==len(parent)
 assert [v['ci'] for v in nr['rows']]==list(range(len(parent)))
 peak=max(nr['rows'],key=lambda v:v['W_over_m'])['ci']
 selected=sorted(set([0,5,100,500,1500,2761,3925,4102,peak,4211,5622,7038,len(parent)-1]))
 targets={(tb[i]+tb[i+1])/2:i for i in selected};br=sorted(set(t)|set(targets));lo,hi=min(targets),max(targets)
 dummy=SimpleNamespace(t=t,deg=7);cache={};N=128;ivals={};jvals={};density={};maxarg=F(0)
 def poly(a,b):
  sp,B=exact_poly(dummy,a,b);assert t[sp]<=a<b<=t[sp+1]
  T=B*fmpq_mat([[fq(v) for v in row] for row in sd[sp-7:sp+1]])
  return [[F(str(T[q,j])) for q in range(8)] for j in range(M+2)]
 def shift(c,d,reverse=False):return [aa((-1 if reverse and q%2 else 1)*sum((math.comb(l,q)*c[l]*d**(l-q) for l in range(q,8)),F(0))) for q in range(8)]
 def moments(rate,h):
  nonlocal maxarg
  maxarg=max(maxarg,abs(rate*h));assert abs(rate*h)<N+1
  key=(rate,h)
  if key not in cache:cache[key]=[aa(h)**(l+1)*phi(l,aa(rate*h),N) for l in range(8)]
  return cache[key]
 def integral(rate,h,c):return sum((v*w for v,w in zip(c,moments(rate,h))),arb(0))
 emit(stage='prepared',modes=M+1,selected_cells=selected,total_boundaries_audited=len(tb),integration_cells=len(br)-1)
 for count,(a,b) in enumerate(zip(br[:-1],br[1:]),1):
  if a>=hi:break
  c=poly(a,b);h=b-a
  for n in ns:
   m=2*n;iv[n-1]=aa(-(m+4)*h).exp()*iv[n-1]+integral(-(m+4),h,shift(c[n-1],h/2,True))
  if b in targets:
   ivals[b]=list(iv);density[b]=[shift(v,h/2) for v in c]
  if count%100==0:emit(stage='forward',done=count,total=len(br)-1,seconds=time.monotonic()-start)
 for count,p in enumerate(range(len(br)-2,-1,-1),1):
  a,b=br[p:p+2]
  if b<=lo:break
  c=poly(a,b);h=b-a
  for n in ns:
   m=2*n;jv[n-1]=aa((4-m)*h).exp()*jv[n-1]+integral(4-m,h,shift(c[n],-h/2))
  if a in targets:jvals[a]=list(jv)
  if count%100==0:emit(stage='backward',done=count,total=len(br)-1,seconds=time.monotonic()-start)
 assert set(ivals)==set(jvals)==set(density)==set(targets)
 records=[]
 for tc,ci in sorted(targets.items()):
  R=[v[0] for v in density[tc]];D=[3*v[0]+v[1] for v in density[tc]];rr=aa(tc).exp();e3=rr**3;e4=rr**4
  A=[e4*((R[n-1]+R[n])/2-2*n*ivals[tc][n-1]) for n in ns]
  B=[e4*(2*n*jvals[tc][n-1]-(R[n-1]+R[n])/2) for n in ns]
  eps=[arb(0) for _ in range(2*M+2)]
  for j in range(M+1):eps[j]+=e3*(cl*D[j]-R[j])
  def add(freq,val):
   assert freq and abs(freq)%2==1
   index=(abs(freq)-1)//2;assert index<len(eps)
   eps[index]+=val if freq>0 else -val
  for n in ns:
   m=2*n;rad=-rr*(A[n-1]+B[n-1])/4;ang=rr*(B[n-1]-A[n-1])/4
   for j in range(M+1):
    nu=2*j+1;pr=rad*D[j];pt=ang*nu*R[j]
    add(nu+m,pr+pt);add(nu-m,pr);add(m-nu,pt)
  W=sum((abs(v) for v in eps),arb(0));u=rr/aa(sc['L']);weight=u**3*(1+u*u)**aa((k-3)/2);Wm=W/weight;L2=arb.pi()*sum((v*v for v in eps),arb(0))
  published=F.from_float(float(nr['rows'][ci]['W']));published_m=F.from_float(float(nr['rows'][ci]['W_over_m']))
  verdict='SAMPLE_CONSISTENT' if W.upper()<=aa(published) else ('REFUTED_AT_SAMPLE' if W.lower()>aa(published) else 'OVERLAP_ONLY')
  vm='SAMPLE_CONSISTENT' if Wm.upper()<=aa(published_m) else ('REFUTED_AT_SAMPLE' if Wm.lower()>aa(published_m) else 'OVERLAP_ONLY')
  rec={'cell':ci,'t_exact':str(tc),'cell_endpoints_exact':[str(tb[ci]),str(tb[ci+1])],'r':out(rr),'W':out(W),'W_over_m':out(Wm),'angular_L2_squared':out(L2),'published_W_exact':str(published),'published_W_over_m_exact':str(published_m),'W_comparison':verdict,'weighted_comparison':vm,'residual_coefficients':[export_ball(v) for v in eps],'density_polynomial_at_point':[[export_ball(v) for v in c] for c in density[tc]],'i':[export_ball(v) for v in ivals[tc]],'j':[export_ball(v) for v in jvals[tc]]}
  records.append(rec);emit(stage='sample',cell=ci,r=rr.str(15),W=W.str(18),Wm=Wm.str(18),comparison=verdict,weighted_comparison=vm,seconds=time.monotonic()-start)
 assert sha(green)==gsha
 result={'utc':utc(),'status':'COMPUTED_REQUIRES_SOURCE_AND_OUTPUT_AUDIT','method':'Exact density projection and six-jet/normalization definitions; all-mode canonical density moments; exact trig product identity; outward Arb finite residual coefficients at exact log cell midpoints','input_sha256':sha(path),'scalar_input_sha256':sha(zpath),'source_sha256':sha(__file__),'moments_sha256':sha(BASE/'research/exponential_moments/code/moments.py'),'Cox_sha256':sha(BASE/'research/canonical_inverse/code/exact_audit.py'),'ball_transport_sha256':sha(BASE/'research/ball_transport/code/dyadic_ball.py'),'green_comparison_sha256':gsha,'published_residual_sha256':numsha,'max_abs_moment_argument_exact':str(maxarg),'bits':ctx.prec,'stream_modes':M+1,'integration_cells':len(br)-1,'samples':records,'seconds':time.monotonic()-start,'scope':'Only these finite point residuals. Does not validate untested cells or global residual norm.'}
 (E/'published_residual_snapshot.json').write_bytes(rawnum)
 (E/'sample_result.json').write_text(json.dumps(result,indent=2)+'\n');emit(stage='done',seconds=result['seconds'])
if __name__=='__main__':main()
