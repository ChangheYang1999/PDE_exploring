"""All-mode source scalars via independent exact density moments, no num imports."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,time,hashlib,resource,bisect
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
E=BASE/'research/modal_source/evidence'
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
 raw=json.loads(path.read_text());ar=raw['arrays'];M,nb=ar['S']['shape'];t=[exact(v) for v in ar['knots']['hex']];sc={k:exact(v) for k,v in raw['scalars_hex'].items()};k,bi,bo=(sc[v] for v in ('k','bi','bo'));cl=3/aa(k)/3
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
 tc=F.from_float(math.log(8.600063805));span=bisect.bisect_right(t,tc)-1;assert t[span]<tc<t[span+1]
 br=sorted(set(t)|{tc});cut=br.index(tc);dummy=SimpleNamespace(t=t,deg=7);cache={};N=128
 def poly(a,b):
  sp,B=exact_poly(dummy,a,b);T=B*fmpq_mat([[fq(v) for v in row] for row in sd[sp-7:sp+1]])
  return [[F(str(T[q,j])) for q in range(8)] for j in range(M+2)]
 def shift(c,d,reverse=False):return [aa((-1 if reverse and q%2 else 1)*sum((math.comb(l,q)*c[l]*d**(l-q) for l in range(q,8)),F(0))) for q in range(8)]
 def moments(rate,h):
  key=(rate,h)
  if key not in cache:
   zz=aa(rate*h);assert abs(zz)<N+1
   cache[key]=[aa(h)**(l+1)*phi(l,zz,N) for l in range(8)]
  return cache[key]
 def integral(rate,h,c):return sum((v*w for v,w in zip(c,moments(rate,h))),arb(0))
 emit(stage='prepared',modes=M+1,original_spans=nb-7,integration_cells=len(br)-1,center_log_exact=str(tc),source_span=span)
 for count,(a,b) in enumerate(zip(br[:cut],br[1:cut+1]),1):
  c=poly(a,b);h=b-a
  for n in ns:
   m=2*n;iv[n-1]=aa(-(m+4)*h).exp()*iv[n-1]+integral(-(m+4),h,shift(c[n-1],h/2,True))
  if count%100==0:emit(stage='forward',done=count,total=cut,seconds=time.monotonic()-start)
 for count,p in enumerate(range(len(br)-2,cut-1,-1),1):
  a,b=br[p:p+2];c=poly(a,b);h=b-a
  for n in ns:
   m=2*n;jv[n-1]=aa((4-m)*h).exp()*jv[n-1]+integral(4-m,h,shift(c[n],-h/2))
  if count%100==0:emit(stage='backward',done=count,total=len(br)-1-cut,seconds=time.monotonic()-start)
 # Exact polynomial at t_c from the entire original knot span, not a rounded fitted polynomial.
 cm=poly(t[span],t[span+1]);Cs=[shift(c,tc-(t[span]+t[span+1])/2) for c in cm]
 def evaluate(x):
  tt=x.log();assert aa(t[span])<tt and tt<aa(t[span+1]);delta=tt-aa(tc);right=[];Rv=[];Rt=[]
  for c in Cs:
   Rv.append(sum((c[l]*delta**l for l in range(8)),arb(0)));Rt.append(sum((l*c[l]*delta**(l-1) for l in range(1,8)),arb(0)))
   right.append([(-1)**q*sum((math.comb(l,q)*c[l]*delta**(l-q) for l in range(q,8)),arb(0)) for q in range(8)])
  ii=[];jj=[]
  for n in ns:
   m=2*n
   def local(rate,c):
    zz=rate*delta;assert abs(zz)<1
    return sum((c[l]*delta**(l+1)*phi(l,zz,32) for l in range(8)),arb(0))
   ii.append((-(m+4)*delta).exp()*iv[n-1]+local(-(m+4),right[n-1]))
   jj.append(((m-4)*delta).exp()*jv[n-1]-local(m-4,right[n]))
  w=cl*x+x**3/2*sum((2*n*(ii[n-1]-jj[n-1]) for n in ns),arb(0))
  mu=cl+x**2/2*sum((2*n*((2*n+1)*ii[n-1]+(2*n-1)*jj[n-1]-Rv[n-1]-Rv[n]) for n in ns),arb(0))
  g=x**2*sum(((2*j+1)*Rv[j] for j in range(M+1)),arb(0))
  gp=x*sum(((2*j+1)*(2*Rv[j]+Rt[j]) for j in range(M+1)),arb(0))
  return dict(w=w,mu=mu,g=g,gprime=gp,wprime=2*cl-mu)
 a,b=F('8.600063805156'),F('8.600063805159');left,right=evaluate(aa(a)),evaluate(aa(b));assert left['w']<0 and right['w']>0
 initial=evaluate(aa(a).union(aa(b)));assert initial['wprime']>0
 history=[{'a_exact':str(a),'b_exact':str(b),'w_a':out(left['w']),'w_b':out(right['w']),'wprime_on_box':out(initial['wprime'])}]
 for step in range(28):
  mid=(a+b)/2;v=evaluate(aa(mid))['w']
  if v<0:a=mid
  elif v>0:b=mid
  else:break
  if step%5==4:emit(stage='bisection',step=step+1,width=str(b-a),seconds=time.monotonic()-start)
 vals=evaluate(aa(a).union(aa(b)));assert vals['wprime']>0
 final={'xstar':aa(a).union(aa(b)),'mu_minus_1':vals['mu']-1,'g':vals['g'],'gprime':vals['gprime'],'A_exact_solution_relation':2*cl-1,'A_trial':vals['wprime'],'cl':cl,'sigma':3/aa(k)-1}
 result={'utc':utc(),'status':'COMPUTED_REQUIRES_SOURCE_AND_OUTPUT_AUDIT','method':'All finite density modes, exact Cox polynomials, closed head/tail density moments, outward Arb Taylor moments with geometric tails; rational sign bisection and exact divergence derivative','input_sha256':sha(path),'scalar_input_sha256':sha(zpath),'source_sha256':sha(__file__),'moments_sha256':sha(BASE/'research/exponential_moments/code/moments.py'),'Cox_sha256':sha(BASE/'research/canonical_inverse/code/exact_audit.py'),'bits':ctx.prec,'stream_modes':M+1,'integration_cells':len(br)-1,'center_log_exact':str(tc),'initial_root_proof':history,'final_root_endpoints_exact':[str(a),str(b)],'final_values':{k:out(v) for k,v in final.items()},'seconds':time.monotonic()-start,'scope':'Canonical exact modal trial scalars and one local root. Not original X3 scalar values, global residual, or exact stationary solution.'}
 (E/'source_result.json').write_text(json.dumps(result,indent=2)+'\n');emit(stage='done',seconds=result['seconds'],values={k:v.str(22) for k,v in final.items()})
if __name__=='__main__':main()
