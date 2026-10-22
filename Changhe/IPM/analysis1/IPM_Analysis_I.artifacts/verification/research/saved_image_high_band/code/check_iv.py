"""Fresh original IEEE754 imports, reverse edge sums and fmpq summary differences."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from flint import fmpq
from mpmath import iv
import numpy as np,json,gzip,hashlib,struct,time
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_high_band';U=B/'research/saved_image_row_functionals';iv.dps=100;ROWS=['L2','L2q','H1','H1q']
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def binary(v):
 bits=struct.unpack('>Q',struct.pack('>d',float(v)))[0];e=(bits>>52)&2047;m=bits&((1<<52)-1);assert e!=2047;return (-1 if bits>>63 else 1)*F(((1<<52)+m) if e else m)*F(2)**(e-1075 if e else -1074)
def ii(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ep(t):
 s,m,e,b=t;assert b>=0;return (-1)**s*F(m)*F(2)**e
def bb(x):return list(map(ep,x._mpi_))
def ss(x):return list(map(str,bb(x)))
def overlap(x,b):
 a=bb(x);b=list(map(F,b));assert max(a[0],b[0])<=min(a[1],b[1])
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();primary=json.loads((D/'evidence/arb.json').read_text());pins=dict(primary['files'])
for n,h in pins.items():assert sha(B/n)==h
with gzip.open(U/'data_exact/selected_arrays.json.gz','rt') as f:cases=[r for r in json.load(f) if r['case']=='M24_s16_o40_p4']
assert [r['row_mode'] for r in cases]==['L2q','H1q'];points=0;edges=0;scalars=0;overlaps=0;results=[]
for rec,p in zip(cases,primary['results'],strict=True):
 with np.load(U/'sources'/(rec['stem']+'_vec.npz'),allow_pickle=False) as z:
  assert(int(z['Ne']),int(z['Mout']),int(z['NJ']),str(z['ROWS']))==(467,40,1,rec['row_mode']);n=467;M=40;assert z['Fminus_img'].shape==(n*M,5) and z['Fminus_img'].dtype==z['t_eval'].dtype==z['w_i'].dtype==np.dtype('float64');t=list(map(binary,z['t_eval']));w=list(map(binary,z['w_i']));assert list(map(str,t))==rec['t_exact'] and list(map(str,w))==rec['w_exact'];scalars+=2*n;delta=[b-a for a,b in zip(t,t[1:])];assert len(t)==len(w)==n and all(q>0 for q in delta+w);w2=[ii(q*q) for q in w];dd=[ii(q) for q in delta];dcoef=[ii((w[i]+w[i+1])**2/(4*delta[i]**2)) for i in range(n-1)];qcoef=[ii((w[i]+w[i+1])**2/(4*delta[i])) for i in range(n-1)];total=[iv.mpf(0) for _ in ROWS];high=[iv.mpf(0) for _ in ROWS]
  for N in reversed(range(M)):
   vals=[]
   for i in range(n):
    q=binary(z['Fminus_img'][i*M+N,0]);assert q==F(rec['directions'][0]['image_exact'][i][N]);scalars+=1;points+=1;vals.append(ii(q))
   squares=[w2[i]*vals[i]**2 for i in range(n)];fac=1+(2*N+1)**2;mode=[iv.mpf(0) for _ in ROWS]
   for i in reversed(range(n)):mode[0]+=squares[i];mode[2]+=fac*squares[i]
   for i in reversed(range(n-1)):
    trap=dd[i]*(squares[i]+squares[i+1])/2;diff=(vals[i+1]-vals[i])**2;mode[1]+=trap;mode[2]+=dcoef[i]*diff;mode[3]+=fac*trap+qcoef[i]*diff;edges+=1
   for j in range(4):
    total[j]+=mode[j]
    if N>=32:high[j]+=mode[j]
  out={};assert p['row_mode']==rec['row_mode'] and p['index']==0
  for R,a,b in zip(ROWS,total,high,strict=True):
   frac=b/a;assert bb(a-b)[0]>0 and bb(b)[0]>0
   for v,key in [(a,'total'),(b,'high'),(frac,'fraction')]:overlap(v,p['rows'][R][key+'_arb']);overlaps+=1
   out[R]={'total_iv':ss(a),'high_iv':ss(b),'fraction_iv':ss(frac)}
  results.append({'row_mode':rec['row_mode'],'index':0,'rows':out})
summ=json.loads((D/'data_exact/summaries.json').read_text());numbers=[];metadata=[(24,16,32,4,467,1,'H1q',2750),(24,16,40,4,467,1,'H1q',2750),(24,8,32,4,855,1,'H1q',5078)]
for r,meta in zip(summ,metadata,strict=True):
 x=json.loads((B/r['source']).read_text());assert tuple(x[k] for k in ['Mh','stride','Mout','ppc','Ne','NJ','rows_mode'])+(x['sections']['Fminus']['n_kept'],)==meta
 v=list(map(binary,x['sections']['Fminus']['sigma_small5']));assert len(v)==5 and list(map(str,v))==r['small5_exact'];numbers.append([fmpq(q.numerator,q.denominator) for q in v]);scalars+=5
ratios=[];cursor=0
for label,i,j in [('cutoff_s16',0,1),('stride_o32',2,0)]:
 for k in range(5):
  u,v=numbers[i][k],numbers[j][k];ratio=abs(u-v)/abs(v);p=primary['summary_differences'][cursor];cursor+=1;assert(label,k,str(ratio),str(u-v))==(p['comparison'],p['index'],p['relative_exact'],p['signed_difference_exact']);assert ratio>0
  if label=='cutoff_s16':assert ratio<fmpq(3,100000)
  ratios.append({'comparison':label,'index':k,'relative_exact':str(ratio),'signed_difference_exact':str(u-v)})
assert points==37360 and edges==37280 and scalars==39243 and overlaps==24 and cursor==10
for p in [Path(__file__),D/'evidence/arb.json',D/'evidence/arb.log']:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h
x={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_LITERAL_HIGH_BAND_AND_SUMMARIES_ONLY','iv_dps':100,'manual_ieee_scalars':scalars,'image_values':points,'edge_differences':edges,'interval_overlaps':overlaps,'exact_summary_comparisons':10,'results':results,'summary_differences':ratios,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick}
with (D/'evidence/independent.json').open('x') as f:json.dump(x,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in x.items() if k not in ['files','results','summary_differences']},indent=2))
