"""New nodal formulas in Arb on all six exact exported finite images."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from flint import arb,ctx
import json,gzip,hashlib,time
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_row_functionals';ctx.prec=320
ROWS=['L2','L2q','H1','H1q']
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def aa(s):
 q=F(s);return arb(q.numerator)/arb(q.denominator)
def box(v):
 need(v.is_finite(),'finite Arb enclosure');return [str(v.lower().fmpq()),str(v.upper().fmpq())]
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();manifest=json.loads((D/'data_exact/manifest.json').read_text());pins=dict(manifest['files'])
for n,h in pins.items():need(sha(B/n)==h,'fixed actual exact data/source')
with gzip.open(D/'data_exact/selected_arrays.json.gz','rt') as f:cases=json.load(f)
results=[];points=0;edges=0
for rec in cases:
 n=rec['Ne'];M=rec['Mout'];t=list(map(F,rec['t_exact']));w=list(map(aa,rec['w_exact']));delta=[t[i+1]-t[i] for i in range(n-1)];need(all(x>0 for x in delta) and all(x>0 for x in w),'positive exact weights/grid');omega=[delta[0]/2]+[(delta[i-1]+delta[i])/2 for i in range(1,n-1)]+[delta[-1]/2];om=list(map(aa,omega));dd=list(map(aa,delta));wb=[(w[i]+w[i+1])/2 for i in range(n-1)]
 for direction in rec['directions']:
  image=[[aa(s) for s in rr] for rr in direction['image_exact']];need(len(image)==n and all(len(rr)==M for rr in image),'complete exported image');energy=[arb(0) for _ in ROWS]
  for i in range(n):
   for N in range(M):
    val=(w[i]*image[i][N])**2;fac=1+(2*N+1)**2;energy[0]+=val;energy[1]+=om[i]*val;energy[2]+=fac*val;energy[3]+=om[i]*fac*val;points+=1
  for i in range(n-1):
   for N in range(M):
    val=(wb[i]*(image[i+1][N]-image[i][N])/dd[i])**2;energy[2]+=val;energy[3]+=dd[i]*val;edges+=1
  g=aa(direction['g_exact']);need(g>0,'positive literal denominator');qs=[(e/g).sqrt() for e in energy];need(energy[2]>2*energy[0] and energy[3]>2*energy[1],'strict actual same-image derivative inequalities');bounds={}
  for j,(row,v) in enumerate(zip(ROWS,qs,strict=True)):
   q=F(direction['saved_quotients_exact'][row]);error=abs(v-aa(q));need(error<aa(F(1,10**10))*max(arb(1),abs(aa(q))),'saved diagnostic within explicit scalar tolerance');bounds[row]={'energy_arb':box(energy[j]),'quotient_arb':box(v),'saved_exact':str(q),'saved_absolute_error_arb':box(error),'display':float(v)}
  ratio=(energy[3]/energy[1]).sqrt();results.append({'case':rec['case'],'row_mode':rec['row_mode'],'index':direction['index'],'Ne':n,'Mout':M,'g_exact':direction['g_exact'],'sigma_exact':direction['sigma_exact'],'rows':bounds,'H1q_over_L2q_arb':box(ratio),'H1q_over_L2q_display':float(ratio),'nodal_weight_extrema_exact':[str(min(omega)),str(max(omega))],'nodal_edge_weight_extrema_exact':[str(min(omega+delta)),str(max(omega+delta))]})
need(len(results)==6 and points==174160 and edges==173920,'all selected exact finite sums')
for p in [Path(__file__),D/'data_exact/manifest.json',D/'evidence/capture.log']:pins[str(p.relative_to(B))]=sha(p)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARB_EXACT_SAVED_IMAGE_FUNCTIONALS_ONLY','arb_bits':ctx.prec,'selected_directions':6,'image_values':points,'edge_differences':edges,'quotient_enclosures':24,'results':results,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Exact finite saved arrays, positive literal g, four discrete functionals. Not continuous image, g norm validity, singular minimum or IPM inverse.'}
with (D/'evidence/arb.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'seconds':out['seconds'],'results':[{'case':r['case'],'rows_mode':r['row_mode'],'index':r['index'],'quotients':{n:v['display'] for n,v in r['rows'].items()},'ratio':r['H1q_over_L2q_display']} for r in results]},indent=2))
