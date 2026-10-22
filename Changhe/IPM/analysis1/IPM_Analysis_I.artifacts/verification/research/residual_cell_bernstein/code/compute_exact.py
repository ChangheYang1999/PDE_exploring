"""Exact affine composition and power-to-Bernstein conversion for one mode chunk."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math,argparse
import flint
from flint import fmpq,fmpq_poly,ctx
assert not sys.flags.optimize and flint.__version__=='0.9.0';ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein';SOURCE=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def fq(q):q=F(q);return fmpq(q.numerator,q.denominator)
start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,required=True);ap.add_argument('--chunk',type=int,required=True);args=ap.parse_args();manifest=json.loads((D/'data_exact/manifest.json').read_text());plan=json.loads((D/'data_exact/arithmetic_plan.json').read_text());assert args.cell in manifest['cells'];lo,hi=manifest['chunks'][args.chunk];pins=dict(plan['files'])
for n,h in pins.items():assert sha(B/n)==h
first=json.loads((SOURCE/'evidence'/('arb_%d.json'%args.cell)).read_text());second=json.loads((SOURCE/'evidence'/('iv_%d.json'%args.cell)).read_text());transforms=[fmpq_poly([fq(-1+F(s,4)),fq(F(1,4))]) for s in range(8)];matrices={}
for order in range(6):
 degree=64-order;matrices[order]=[[fq(F(math.comb(k,q),math.comb(degree,q))) for q in range(k+1)] for k in range(degree+1)]
records=[];count=0;derivatives=0
for N in range(lo,hi):
 mids=[];rads=[]
 for q in range(65):
  a,b=be(first['coefficient_boxes'][N][q]);u,v=be(second['coefficient_boxes'][N][q]);l,r=max(a,u),min(b,v);assert l<=r;mids.append((l+r)/2);rads.append((r-l)/2)
 poly=fmpq_poly([fq(x) for x in mids]);orders=[]
 for order in range(6):
  if order:poly=poly.derivative()
  degree=64-order;error=sum((F(math.factorial(q)//math.factorial(q-order))*rads[q] for q in range(order,65)),F(0));maxima=[];stream=hashlib.sha256();coefficient_count=0
  for s,linear in enumerate(transforms):
   translated=poly(linear);beta=[sum((translated[q]*w for q,w in enumerate(row)),fmpq(0)) for row in matrices[order]];assert len(beta)==degree+1;maximum=max(abs(x) for x in beta);maxima.append(str(maximum));count+=1
   for kk,x in enumerate(beta):stream.update(('%d %d %d %d %s\n'%(N,order,s,kk,x)).encode());coefficient_count+=1
  orders.append({'order':order,'coefficient_radius_exact':str(error),'bernstein_maxima_exact':maxima,'bernstein_coefficients_sha256':stream.hexdigest(),'bernstein_coefficient_count':coefficient_count});derivatives+=1
 records.append({'mode_index':N,'frequency':2*N+1,'orders':orders})
for p in [D/'data_exact/manifest.json',D/'data_exact/arithmetic_plan.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_EXACT_LOCAL_BERNSTEIN_MAXIMA_NEEDS_INDEPENDENT_CHECK','cell':args.cell,'chunk':args.chunk,'mode_range':[lo,hi],'subcells':8,'records':records,'modal_subcell_maxima':count,'modal_derivatives':derivatives,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Exact midpoint-polynomial Bernstein majorants plus exact coefficient-radius error; Cauchy tail aggregation pending.'}
p=D/'evidence'/('exact_%d_%d.json'%(args.cell,args.chunk))
with p.open('x') as f:json.dump(out,f,separators=(',',':'));f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','cell','chunk','mode_range','modal_subcell_maxima','seconds']}),flush=True)
