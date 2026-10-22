"""Independent global Bernstein conversion and exact/Arb midpoint subdivision."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math,argparse
import flint
from flint import fmpq,fmpq_poly,arb,arb_poly,ctx
assert not sys.flags.optimize and flint.__version__=='0.9.0';ctx.prec=512;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein';SOURCE=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def aq(q):q=F(q);return arb(q.numerator)/q.denominator
def fq(q):q=F(q);return fmpq(q.numerator,q.denominator)
def frac(q):return F(int(q.numerator),int(q.denominator))
def ends(v):
 out=[]
 for x in [v.lower(),v.upper()]:assert x.is_finite() and x.rad()==0;m,e=x.man_exp();out.append(F(int(m))*F(2)**int(e))
 return out

def split(v):
 row=v[:];left=[row[0]];right=[row[-1]]
 while len(row)>1:
  row=[(row[j]+row[j+1])/2 for j in range(len(row)-1)];left.append(row[0]);right.append(row[-1])
 return left,list(reversed(right))
start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,required=True);ap.add_argument('--chunk',type=int,required=True);args=ap.parse_args();manifest=json.loads((D/'data_exact/manifest.json').read_text());plan=json.loads((D/'data_exact/arithmetic_plan.json').read_text());assert plan['arb_bits']==ctx.prec and plan['subcells']==8;assert args.cell in manifest['cells'];lo,hi=manifest['chunks'][args.chunk];pins=dict(plan['files'])
for n,h in pins.items():assert sha(B/n)==h
primarypath=D/'evidence'/('exact_%d_%d.json'%(args.cell,args.chunk));primary=json.loads(primarypath.read_text());assert primary['status']=='COMPUTED_EXACT_LOCAL_BERNSTEIN_MAXIMA_NEEDS_INDEPENDENT_CHECK' and primary['cell']==args.cell and primary['chunk']==args.chunk and primary['mode_range']==[lo,hi]
for n,h in primary['files'].items():assert sha(B/n)==h and (n not in pins or pins[n]==h);pins[n]=h
first=json.loads((SOURCE/'evidence'/('arb_%d.json'%args.cell)).read_text());second=json.loads((SOURCE/'evidence'/('iv_%d.json'%args.cell)).read_text());matrixQ={};matrixA={}
for order in range(6):
 d=64-order;matrixQ[order]=[[fq(F(math.comb(k,q),math.comb(d,q))) for q in range(k+1)] for k in range(d+1)];matrixA[order]=[[aq(F(math.comb(k,q),math.comb(d,q))) for q in range(k+1)] for k in range(d+1)]
records=[];coefficient_checks=0;maximum_checks=0;radius_checks=0;max_width=F(0)
for N in range(lo,hi):
 saved=primary['records'][N-lo];assert saved['mode_index']==N and saved['frequency']==2*N+1;mids=[];rads=[]
 for q in range(65):
  a,b=be(first['coefficient_boxes'][N][q]);u,v=be(second['coefficient_boxes'][N][q]);lower,upper=max(a,u),min(b,v);assert lower<=upper;mids.append((lower+upper)/2);rads.append((upper-lower)/2)
 polyQ=fmpq_poly([fq(x) for x in mids]);polyA=arb_poly([aq(x) for x in mids]);radcoeff=rads[:];orders=[]
 for order in range(6):
  if order:polyQ=polyQ.derivative();polyA=polyA.derivative();radcoeff=[(q+1)*radcoeff[q+1] for q in range(len(radcoeff)-1)]
  error=sum(radcoeff,F(0));savedorder=saved['orders'][order];assert savedorder['order']==order and str(error)==savedorder['coefficient_radius_exact'];radius_checks+=1;d=64-order
  globalQ=polyQ(fmpq_poly([-1,2]));globalA=polyA(arb_poly([-1,2]));betaQ=[sum((globalQ[q]*weight for q,weight in enumerate(row)),fmpq(0)) for row in matrixQ[order]];betaA=[sum((globalA[q]*weight for q,weight in enumerate(row)),arb(0)) for row in matrixA[order]];piecesQ=[betaQ];piecesA=[betaA]
  for depth in range(3):piecesQ=[p for old in piecesQ for p in split(old)];piecesA=[p for old in piecesA for p in split(old)]
  assert len(piecesQ)==len(piecesA)==8;stream=hashlib.sha256();maxboxes=[];localcount=0
  for s in range(8):
   assert len(piecesQ[s])==len(piecesA[s])==d+1;maxlo=F(0);maxhi=F(0)
   for kk,(exact,ball) in enumerate(zip(piecesQ[s],piecesA[s])):
    l,r=ends(ball);value=frac(exact);assert l<=value<=r,('COEFFICIENT',args.cell,N,order,s,kk);coefficient_checks+=1;localcount+=1;stream.update(('%d %d %d %d %s\n'%(N,order,s,kk,exact)).encode());l,r=ends(abs(ball));maxlo=max(maxlo,l);maxhi=max(maxhi,r)
   exactmax=max(abs(x) for x in piecesQ[s]);assert str(exactmax)==savedorder['bernstein_maxima_exact'][s];assert maxlo<=frac(exactmax)<=maxhi;maximum_checks+=1;max_width=max(max_width,maxhi-maxlo);maxboxes.append({'lower_exact':str(maxlo),'upper_exact':str(maxhi)})
  assert stream.hexdigest()==savedorder['bernstein_coefficients_sha256'] and localcount==savedorder['bernstein_coefficient_count'];orders.append({'order':order,'coefficient_radius_exact':str(error),'bernstein_maxima_boxes':maxboxes,'coefficient_stream_sha256':stream.hexdigest(),'bernstein_coefficient_checks':localcount})
 records.append({'mode_index':N,'frequency':2*N+1,'orders':orders})
assert coefficient_checks==(hi-lo)*8*375 and maximum_checks==(hi-lo)*48 and radius_checks==(hi-lo)*6
for p in [D/'data_exact/manifest.json',D/'data_exact/arithmetic_plan.json',primarypath,Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_AND_ARB_SUBDIVISION_AND_DIRECT_STREAM_BINDING','cell':args.cell,'chunk':args.chunk,'mode_range':[lo,hi],'subcells':8,'records':records,'bernstein_coefficient_checks':coefficient_checks,'modal_subcell_maximum_checks':maximum_checks,'coefficient_radius_checks':radius_checks,'largest_maximum_enclosure_width_exact':str(max_width),'arb_bits':ctx.prec,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Independent exact and Arb midpoint subdivision; every reconstructed Bernstein coefficient enclosed and entire streams bind to direct local rational composition. Final range/tail aggregation pending.'}
p=D/'evidence'/('subdivision_%d_%d.json'%(args.cell,args.chunk))
with p.open('x') as f:json.dump(out,f,separators=(',',':'));f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','cell','chunk','bernstein_coefficient_checks','modal_subcell_maximum_checks','seconds']}),flush=True)
