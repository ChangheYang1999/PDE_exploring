"""One selected cell: physical Green ODE, Arb series and ordinary polynomial products."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math,argparse
import flint
from flint import arb,arb_poly,ctx
assert not sys.flags.optimize and flint.__version__=='0.9.0'
ctx.prec=448;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy';DEG=64;STRIDE=129

def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aq(q):q=F(q);return arb(q.numerator)/q.denominator
def frac(x):
 assert x.is_finite() and x.rad()==0;m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ends(x):return frac(x.lower()),frac(x.upper())
def box(x):
 assert x.is_finite();m,e=x.mid().man_exp();r,s=x.rad().man_exp();return {'mid_m':str(m),'mid_e':int(e),'rad_m':str(r),'rad_e':int(s),'schema':'arb-dyadic-mid-radius-v1'}
def decode(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return aq(m-r).union(aq(m+r))
def out(x):
 a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display_only':x.str(16)}
def write(p,x):
 with p.open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n');f.flush();os.fsync(f.fileno())
start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,required=True);args=ap.parse_args();manifest=json.loads((D/'data_exact/manifest.json').read_text());record=next(x for x in manifest['cells'] if x['cell']==args.cell);pins=dict(manifest['files'])
for n,hsh in pins.items():assert sha(B/n)==hsh
for p in [D/'data_exact/manifest.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
sample=next(x for x in json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'] if x['cell']==args.cell);tc=F(record['center_exact']);h=F(record['h_exact']);assert h>0 and sample['t_exact']==str(tc)
trial=json.loads((B/'data_exact/modal_v2.json').read_text());k=F.from_float(float.fromhex(trial['scalars_hex']['k']));c=aq(1/k);H=[[decode(v) for v in p] for p in sample['density_polynomial_at_point']];I=list(map(decode,sample['i']));J=list(map(decode,sample['j']));assert len(H)==262 and all(len(p)==8 for p in H) and all(ends(x)==(0,0) for x in H[-1])
ht=aq(h);rad=4*ht;e4=aq(4*tc).exp();e3=aq(3*tc).exp();e2=aq(2*tc).exp();eminus2=aq(-2*tc).exp()
gpoly=[];A0=[];B0=[]
for n in range(1,262):
 m=2*n;S=(H[n-1][0]+H[n][0])/2;A0.append(e4*(S-m*I[n-1]));B0.append(e4*(m*J[n-1]-S));gpoly.append([((q+1)*(H[n-1][q+1]+H[n][q+1]) if q<7 else 0)/2+((4-m)*H[n-1][q]+(4+m)*H[n][q])/2 for q in range(8)])
C=[sum((abs(v)*rad**q for q,v in enumerate(p)),arb(0)) for p in H]
HP=[[3*p[q]+((q+1)*p[q+1] if q<7 else 0) for q in range(8)] for p in H]
CP=[sum((abs(v)*rad**q for q,v in enumerate(p)),arb(0)) for p in HP]
Ds=[aq(3*tc).exp()*(3*rad).exp()*v for v in C[:261]];Es=[aq(3*tc).exp()*(3*rad).exp()*v for v in CP[:261]]
Pb=[];Qb=[]
for n in range(1,262):
 G=e4*(4*rad).exp()*sum((abs(v)*rad**q for q,v in enumerate(gpoly[n-1])),arb(0));bound=eminus2*(2*rad).exp()*(2*n*rad).exp()*(abs(A0[n-1])+abs(B0[n-1])+2*rad*G)/2;Pb.append(bound);Qb.append(bound)
DS=[sum(((2*a+1)**j*v for a,v in enumerate(Ds)),arb(0)) for j in range(7)];ES=[sum(((2*a+1)**j*v for a,v in enumerate(Es)),arb(0)) for j in range(6)];PS=[sum(((2*n)**j*v for n,v in enumerate(Pb,1)),arb(0)) for j in range(6)];QS=[sum(((2*n)**j*v for n,v in enumerate(Qb,1)),arb(0)) for j in range(6)]
Bs=[abs(c)*ES[j]+DS[j]+sum((math.comb(j,l)*(PS[l]*ES[j-l]+QS[l]*DS[j-l+1]) for l in range(j+1)),arb(0)) for j in range(6)]
tails={}
for i in range(6):
 for j in range(6-i):tails['W_%d_%d'%(i,j)]=out(Bs[j]*aq(h**(-i)*F(math.factorial(65)//math.factorial(65-i),4**65)/(1-F(66,4*(66-i)))))
pre={'utc':datetime.now(timezone.utc).isoformat(),'cell':args.cell,'status':'COMPUTED_PHYSICAL_DISK_MAJORANTS_BEFORE_PRODUCTS','B_j':[out(x) for x in Bs],'tail_upper_inputs':tails,'h_exact':str(h),'radius_exact':'4','degree':64,'files':dict(sorted(pins.items()))}
write(D/'evidence'/('arb_preflight_%d.json'%args.cell),pre)
print(json.dumps({'phase':'disk_preflight','cell':args.cell,'B0':pre['B_j'][0]['display_only'],'tail_5_0':tails['W_5_0']['display_only'],'seconds':time.monotonic()-start}),flush=True)
exps={}
for beta in [-2,3,4]:
 vals=[arb(1)]
 for q in range(1,65):vals.append(vals[-1]*(beta*ht)/q)
 exps[beta]=arb_poly(vals)
def expmul(p,beta,scale):
 product=arb_poly(p)*exps[beta];return [scale*product[q] for q in range(65)]
scaled=[[v*ht**q for q,v in enumerate(p)] for p in H]
R=[expmul(p,3,e3) for p in scaled[:261]];Rt=[expmul([v*ht**q for q,v in enumerate(p)],3,e3) for p in HP[:261]]
Pv=[];Qv=[]
for n in range(1,262):
 g=expmul([v*ht**q for q,v in enumerate(gpoly[n-1])],4,e4);a=[A0[n-1]];b=[B0[n-1]]
 for q in range(64):a.append(ht*(-2*n*a[-1]+g[q])/(q+1));b.append(ht*(2*n*b[-1]-g[q])/(q+1))
 Pv.append(expmul([-(x+y)/2 for x,y in zip(a,b)],-2,eminus2));Qv.append(expmul([(y-x)/2 for x,y in zip(a,b)],-2,eminus2))
def pack(values,even,sine,theta_derivative=False):
 offset=522 if even else 521;arr=[arb(0) for _ in range((2*offset)*STRIDE+65)]
 for n,row in enumerate(values):
  freq=2*(n+1) if even else 2*n+1
  for q,x in enumerate(row):
   val=x*freq if theta_derivative else x
   if not sine:val/=2
   arr[(offset+freq)*STRIDE+q]=val;arr[(offset-freq)*STRIDE+q]=-val if sine else val
 return arb_poly(arr)
product=pack(Pv,True,False)*pack(Rt,False,True)+pack(Qv,True,True)*pack(R,False,False,True)
assert product.degree()<=2086*STRIDE+128
coef=[];point=json.loads((B/'research/residual_point_jets/evidence'/('arb_%d.json'%args.cell)).read_text());jetchecks=0
for N in range(522):
 row=[]
 for q in range(65):
  val=product[(1043+2*N+1)*STRIDE+q]
  if N<261:val+=c*Rt[N][q]-R[N][q]
  row.append(box(val))
  if q<=5:
   a,b=ends(val*aq(F(math.factorial(q))*h**(-q)));u,v=ends(decode(point['coefficient_boxes'][q][N]));assert max(a,u)<=min(b,v),('POINT',args.cell,N,q);jetchecks+=1
 coef.append(row)
assert jetchecks==3132
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_PHYSICAL_GREEN_CELL_TAYLOR_NEEDS_INDEPENDENT_AUDIT','cell':args.cell,'degree':64,'modes':522,'coefficient_boxes':coef,'point_jet_comparisons':jetchecks,'ball_polynomial_products':2,'B_j':pre['B_j'],'bits':ctx.prec,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Selected cell analytic coefficients and disk majorants; no accepted cell bound before full independent audit.'}
write(D/'evidence'/('arb_%d.json'%args.cell),result)
print(json.dumps({k:result[k] for k in ['utc','status','cell','point_jet_comparisons','seconds']}),flush=True)
