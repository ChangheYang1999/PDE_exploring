import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import hashlib,json,sys,time
import numpy as np
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/04_modal_scalar/code'));import recompute as R
ctx.prec=512;ctx.threads=1
SRC=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):return arb(q.numerator)/q.denominator
def pack(a):
 def bd(x):n,e=x.mid().man_exp();return [str(n),int(e)]
 return {'ball':a.str(40),'lo_binary':bd(a.lower()),'hi_binary':bd(a.upper())}
start=time.monotonic();assert sha(SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
dat=np.load(SRC,allow_pickle=False);knots=[F(float(x)) for x in dat['knots']];S=dat['S']
co=[sum((F(float(S[m,j]))*((-1)**m) for m in range(260)),F(0)) for j in range(S.shape[1])]
T=knots[:];d=co[:]
for degree in range(7,0,-1):
 den=[T[j+degree+1]-T[j+1] for j in range(len(d)-1)];assert all(x>0 for x in den)
 d=[degree*(d[j+1]-d[j])/den[j] for j in range(len(d)-1)];T=T[1:-1]
spans=[i for i in range(7,len(knots)-8) if knots[i]<knots[i+1]];last=spans[-31:]
selected=sorted(set(range(698,704))|set(last));raw={}
for i in selected:
 p=R.deboor_poly(knots,co,7,i);h=knots[i+1]-knots[i];D=d[i-7]
 assert p[7]*factorial(7)/h**7==D
 A=sum((v*F(1,2)**j for j,v in enumerate(p)),F(0));assert A!=0
 raw[i]={'h':h,'D':D,'A':A,'t':knots[i]}
rows=[];zs={}
for i in selected:
 r=raw[i];entry={'span':i,'t_exact':str(r['t']),'width_exact':str(r['h']),'D7_exact':str(r['D']),'A_mid_exact':str(r['A']),'D7_decimal':str(aa(r['D'])),'A_mid_decimal':str(aa(r['A']))}
 if i-1 in raw:
  alt=aa(abs(r['D']-raw[i-1]['D']))/2*(aa(r['h'])/arb.pi())**7;z=alt/aa(abs(r['A']));assert z>0
  zs[i]=z;entry['a']=pack(alt);entry['z']=pack(z)
 rows.append(entry)
ratios=[]
for i in last:
 if i in zs and i-3 in zs:
  z=zs[i]/zs[i-3];ratios.append({'span':i,'ratio':pack(z),'mid':float(z.mid())})
lead=LANE.parent/'s2-lead/work/farres';copies={}
for fn in ('knot_scan.json','knot_noise.json','knot_scan.py','knot_noise.py'):
 b=(lead/fn).read_bytes();(TOP/'evidence/source'/fn).write_bytes(b);copies[fn]=hashlib.sha256(b).hexdigest()
old=json.loads((TOP/'evidence/source/knot_scan.json').read_text());by={r['span']:r for r in old};errors=[]
for i in last[1:]:
 z=zs[i];v=by[i]['altA']/abs(by[i]['A']);errors.append(abs(aa(F(v))-z)/z)
noise=json.loads((TOP/'evidence/source/knot_noise.json').read_text());nb={r['span']:r for r in noise}
central=[{'span':i,'exact_decimal':str(aa(raw[i]['D'])),'lead_float':nb[i]['A7'],'relative_difference':pack(abs(aa(F(nb[i]['A7']))-aa(raw[i]['D']))/aa(abs(raw[i]['D'])))} for i in range(698,704)]
res={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED numerical diagnostic, not an inverse obstruction','source_sha256':sha(SRC),'selected_spans':selected,'last31':last,'rows':rows,'central_comparison':central,'three_span_ratios':ratios,'last30_max_relative_float_difference':pack(max(x.upper() for x in errors)),'last30_three_span_ratio_mid_min':min(r['mid'] for r in ratios),'last30_three_span_ratio_mid_max':max(r['mid'] for r in ratios),'last30_three_span_ratio_mid_median':sorted(r['mid'] for r in ratios)[len(ratios)//2],'lead_snapshots':copies,'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(Path(__file__)),'seconds':time.monotonic()-start}
(TOP/'evidence/check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ('rows','three_span_ratios','selected_spans','last31')},indent=2))
