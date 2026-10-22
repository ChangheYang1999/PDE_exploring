"""Independent exact endpoint products and translated tensor Bernstein hulls."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,argparse,time
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_composition';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def exact(x):return F(float(x))
def pt(x):x=F(x);return (x,x)
def box(m,r):m,r=exact(m),exact(r);assert r>=0;return (m-r,m+r)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 v=[a*b for a in x for b in y];return min(v),max(v)
def scale(x,c):return mul(x,pt(c))
def mag(x):return max(abs(x[0]),abs(x[1]))
def total(xs):
 lo=hi=F(0)
 for x in xs:lo+=x[0];hi+=x[1]
 return lo,hi

def translated_range(poly,ell):
 endpoints=[]
 for alpha in (F(0),ell):
  powers=[alpha**j for j in range(13)]
  shifted=[total(scale(poly[i],comb(i,j)*powers[i-j]) for i in range(j,13)) for j in range(13)]
  bern=[total(scale(shifted[j],ell**j*F(comb(k,j),comb(12,j))) for j in range(k+1)) for k in range(13)]
  endpoints.extend(bern)
 return min(x[0] for x in endpoints),max(x[1] for x in endpoints)
def tensor_range(q,err,d,ell):
 hull=[]
 for typ in range(3):
  if typ==1:p=[sub(q[0][j],scale(q[2][j],d*d)) for j in range(13)]
  else:p=[add(add(q[0][j],scale(q[1][j],(-d if typ==0 else d))),scale(q[2][j],d*d)) for j in range(13)]
  hull.append(translated_range(p,ell))
 return min(x[0] for x in hull)-err,max(x[1] for x in hull)+err

def run(a,ai):
 h=exact(a['scalar'][0]);H=list(map(exact,a['scalar'][9:22]));ell=exact(a['ell'][0]);d=exact(a['d'][ai]);assert h>0 and 2*ell>=h and all(w>=h**j for j,w in enumerate(H))
 mu=box(*a['scalar'][7:9]);cl=box(*a['cl']);alpha=F(129,20);beta=F(307,100)
 coeff={X:[[box(m,r) for m,r in zip(mm,rr,strict=True)] for mm,rr in zip(a[X+'_mid'],a[X+'_rad'],strict=True)] for X in ('P','R')}
 radial_rem={X:list(map(exact,a[X+'_rem'])) for X in ('P','R')}
 radial_mag={X:[sum((mag(v)*w for v,w in zip(row,H,strict=True)),F(0)) for row in coeff[X]] for X in coeff}
 q=[];errs=[]
 for fam,X in enumerate(('P','R','R')):
  f=[[box(m,r) for m,r in zip(a['angular_mid'][ai,fam,k],a['angular_rad'][ai,fam,k],strict=True)] for k in range(3)]
  rf=list(map(exact,a['angular_rem'][ai,fam]));assert all(x>=0 for x in rf+radial_rem[X])
  q.append([[total(mul(f[k][n],coeff[X][n][j]) for n in range(261)) for j in range(13)] for k in range(3)])
  errs.append(sum((rf[n]*radial_mag[X][n]+(sum((mag(f[k][n])*d**k for k in range(3)),F(0))+rf[n])*radial_rem[X][n] for n in range(261)),F(0)))
 sp,sc,ss=q;ep,ec,es=errs
 sq=[[neg(x) for x in row] for row in sp];sq[0][0]=add(cl,sq[0][0])
 v2=[[add(sq[k][j],sc[k][j]) for j in range(13)] for k in range(3)]
 v1=[[sub(sq[k][j],ss[k][j]) for j in range(13)] for k in range(3)]
 tq=[[add(add(scale(ss[k][j],-alpha),scale(sc[k][j],beta)),mul(mu,sq[k][j])) for j in range(13)] for k in range(3)]
 tq[0][0]=sub(tq[0][0],add(pt(1),cl))
 results=[]
 for name,qq,ee in [('s',sq,ep),('v2y',v2,ep+ec),('v1x',v1,ep+es),('T0',tq,alpha*es+beta*ec+mag(mu)*ep)]:
  ref=tensor_range(qq,ee,d,ell);target=tuple(exact(a['target_'+name+'_'+s][ai]) for s in ('lo','hi'));assert ref[0]<=ref[1] and target[0]<=target[1]
  result={'name':name,'reference':[str(x) for x in ref],'target':[str(x) for x in target],'analytic_error':str(ee),'contained':target[0]<=ref[0] and ref[1]<=target[1],'margins':[str(ref[0]-target[0]),str(target[1]-ref[1])]}
  results.append(result)
 return {'angular_index':ai,'node':a['nodes'][ai].tolist(),'ranges':results,'modal_products':3*3*13*261,'degree':12,'radial_subintervals':2}

ap=argparse.ArgumentParser();ap.add_argument('--ci',type=int,required=True,choices=[0,4102,7808]);args=ap.parse_args();start=utc();t=time.monotonic()
p=E/f'packet_{args.ci:04d}.npz';prep=json.loads((E/'preparation.json').read_text());entry=next(x for x in prep['packets'] if x['ci']==args.ci);assert sha(p)==entry['sha256']
with np.load(p,allow_pickle=False) as z:a={k:z[k] for k in z.files}
for k,v in a.items():assert np.isfinite(v).all(),k
rows=[run(a,i) for i in range(3)];passed=all(r['contained'] for row in rows for r in row['ranges'])
out={'start_utc':start,'end_utc':utc(),'elapsed_seconds':time.monotonic()-t,'method':'exact Fraction interval endpoints, translated radial powers, tensor Bernstein','ci':args.ci,'status':'PASS' if passed else 'OPEN_SUFFICIENT_COMPARISON_FAILED','rows':rows,'packet_sha256':sha(p),'code_sha256':sha(__file__),'preparation_sha256':sha(E/'preparation.json')}
dest=E/f'exact_{args.ci:04d}.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('end_utc','elapsed_seconds','ci','status')}),flush=True)
