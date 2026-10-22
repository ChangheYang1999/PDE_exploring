"""Fresh nodal finite sums and exact saved-summary differences."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from flint import arb,ctx
import json,gzip,hashlib,time
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_high_band';U=B/'research/saved_image_row_functionals';ctx.prec=320;ROWS=['L2','L2q','H1','H1q']
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aa(q):
 q=F(q);return arb(q.numerator)/arb(q.denominator)
def box(x):
 assert x.is_finite();return [str(x.lower().fmpq()),str(x.upper().fmpq())]
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();pins=json.loads((D/'data_exact/manifest.json').read_text())['files']
for n,h in pins.items():assert sha(B/n)==h
with gzip.open(U/'data_exact/selected_arrays.json.gz','rt') as f:cases=[r for r in json.load(f) if r['case']=='M24_s16_o40_p4']
assert [(x['row_mode'],[d['index'] for d in x['directions']]) for x in cases]==[('L2q',[0]),('H1q',[0])]
results=[];points=0;edges=0
for rec in cases:
 n=rec['Ne'];M=rec['Mout'];assert(n,M)==(467,40);t=list(map(F,rec['t_exact']));w=list(map(aa,rec['w_exact']));delta=[t[i+1]-t[i] for i in range(n-1)];assert all(x>0 for x in delta) and all(x>0 for x in w);omega=[delta[0]/2]+[(delta[i-1]+delta[i])/2 for i in range(1,n-1)]+[delta[-1]/2];dd=list(map(aa,delta));om=list(map(aa,omega));im=[[aa(q) for q in rr] for rr in rec['directions'][0]['image_exact']];assert len(im)==n and all(len(rr)==M for rr in im);total=[arb(0) for _ in ROWS];high=[arb(0) for _ in ROWS]
 for i in range(n):
  for N in range(M):
   val=(w[i]*im[i][N])**2;fac=1+(2*N+1)**2;terms=[val,om[i]*val,fac*val,fac*om[i]*val]
   for j in range(4):
    total[j]+=terms[j]
    if N>=32:high[j]+=terms[j]
   points+=1
 for i in range(n-1):
  for N in range(M):
   z=((w[i]+w[i+1])*(im[i+1][N]-im[i][N])/(2*dd[i]))**2;total[2]+=z;total[3]+=dd[i]*z
   if N>=32:high[2]+=z;high[3]+=dd[i]*z
   edges+=1
 out={}
 for R,a,b in zip(ROWS,total,high,strict=True):
  assert a>b>0;ratio=b/a;out[R]={'total_arb':box(a),'high_arb':box(b),'fraction_arb':box(ratio),'fraction_display':float(ratio)}
 results.append({'row_mode':rec['row_mode'],'index':0,'Ne':n,'Mout':M,'rows':out})
assert points==37360 and edges==37280
summ=json.loads((D/'data_exact/summaries.json').read_text());ratios=[]
for label,i,j in [('cutoff_s16',0,1),('stride_o32',2,0)]:
 a,b=summ[i],summ[j];assert a['metadata']['Mh']==b['metadata']['Mh']==24 and a['metadata']['NJ']==b['metadata']['NJ']==1 and a['metadata']['rows_mode']==b['metadata']['rows_mode']=='H1q' and a['metadata']['ppc']==b['metadata']['ppc']==4
 for k,(u,v) in enumerate(zip(a['small5_exact'],b['small5_exact'],strict=True)):
  u,v=F(u),F(v);ratio=abs(u-v)/abs(v);assert ratio>0
  if label=='cutoff_s16':assert ratio<F(3,100000)
  ratios.append({'comparison':label,'index':k,'relative_exact':str(ratio),'relative_display':float(ratio),'signed_difference_exact':str(u-v)})
for p in [Path(__file__),D/'data_exact/manifest.json']:pins[str(p.relative_to(B))]=sha(p)
x={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARB_OBSERVED_HIGH_BAND_ONLY','arb_bits':320,'image_values':points,'edge_differences':edges,'energy_enclosures':16,'fraction_enclosures':8,'results':results,'summary_differences':ratios,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick}
with (D/'evidence/arb.json').open('x') as f:json.dump(x,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in x.items() if k not in ['files','results']},indent=2));print(json.dumps([{r['row_mode']:{k:v['fraction_display'] for k,v in r['rows'].items()}} for r in results]))
