"""Independent original manual-IEEE imports and reverse edge-formula interval evaluation."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from mpmath import iv
import numpy as np,json,gzip,hashlib,struct,time
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_row_functionals';iv.dps=100;ROWS=['L2','L2q','H1','H1q']
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def binary(v):
 bits=struct.unpack('>Q',struct.pack('>d',float(v)))[0];e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e!=2047,'finite original binary');return (-1 if bits>>63 else 1)*F(((1<<52)+m) if e else m)*F(2)**(e-1075 if e else -1074)
def ii(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ep(t):
 s,m,e,b=t;need(b>=0,'finite iv endpoint');return (-1)**s*F(m)*F(2)**e
def box(v):return list(map(ep,v._mpi_))
def ss(v):return list(map(str,box(v)))
def overlap(v,b):
 a=box(v);b=list(map(F,b));need(max(a[0],b[0])<=min(a[1],b[1]),'two independent interval enclosures overlap')
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();primary=json.loads((D/'evidence/arb.json').read_text());pins=dict(primary['files'])
for n,h in pins.items():need(sha(B/n)==h,'unchanged primary inputs')
with gzip.open(D/'data_exact/selected_arrays.json.gz','rt') as f:cases=json.load(f)
original_selection=[('M16_s8_o40_p4','L2q',[0,2,4]),('M16_s8_o40_p4','H1q',[0]),('M24_s16_o40_p4','L2q',[0]),('M24_s16_o40_p4','H1q',[0])];need([(r['case'],r['row_mode'],[x['index'] for x in r['directions']]) for r in cases]==original_selection,'preselected six directions');checks=0;overlaps=0;points=0;edgecount=0;allout=[];cursor=0
for rec in cases:
 with np.load(D/'sources'/(rec['stem']+'_vec.npz'),allow_pickle=False) as z:
  n=int(z['Ne']);M=int(z['Mout']);need(M==40 and n==rec['Ne'] and str(z['ROWS'])==rec['row_mode'] and int(z['NJ'])==1,'original source metadata');need(z['t_eval'].dtype==z['w_i'].dtype==z['Fminus_img'].dtype==z['Fminus_hGh'].dtype==z['Fminus_sigma'].dtype==np.dtype('float64'),'binary64 source types');t=list(map(binary,z['t_eval']));w=list(map(binary,z['w_i']));need([str(x) for x in t]==rec['t_exact'] and [str(x) for x in w]==rec['w_exact'],'every geometry datum versus exact export');checks+=2*n;delta=[b-a for a,b in zip(t,t[1:])];need(len(t)==len(w)==n and all(x>0 for x in delta+w),'positive exact geometry');weight=[ii(x*x) for x in w];de=[ii(x) for x in delta];dcoef=[ii((w[i]+w[i+1])**2/(4*delta[i]**2)) for i in range(n-1)];qcoef=[ii((w[i]+w[i+1])**2/(4*delta[i])) for i in range(n-1)];saved=json.loads((D/'sources'/(rec['stem']+'_imgeval_Fminus.json')).read_text());need(saved['vec']=='runs/c2/'+rec['stem']+'_vec.npz' and saved['section']=='Fminus' and saved['rows_mode_of_run']==rec['row_mode'],'saved scalar source identity');fi=z['Fminus_img'];need(fi.shape==(n*M,5) and z['Fminus_hGh'].shape==z['Fminus_sigma'].shape==(5,),'actual source array shapes')
  for d in rec['directions']:
   j=d['index'];g=binary(z['Fminus_hGh'][j]);sigma=binary(z['Fminus_sigma'][j]);sq={r:binary(saved['quotients'][r][j]) for r in ROWS};need(str(g)==d['g_exact'] and str(sigma)==d['sigma_exact'] and {k:str(v) for k,v in sq.items()}==d['saved_quotients_exact'] and saved['sigma_saved'][j]==float(z['Fminus_sigma'][j]) and g>0,'original denominator and saved scalar values');checks+=6;energy=[iv.mpf(0) for _ in ROWS]
   for N in reversed(range(M)):
    vals=[]
    for i in range(n):
     q=binary(fi[i*M+N,j]);need(q==F(d['image_exact'][i][N]),'every original image value versus export');checks+=1;vals.append(ii(q));points+=1
    squares=[weight[i]*vals[i]**2 for i in range(n)];fac=1+(2*N+1)**2
    for i in reversed(range(n)):energy[0]+=squares[i];energy[2]+=fac*squares[i]
    for i in reversed(range(n-1)):
     trap=de[i]*(squares[i]+squares[i+1])/2;diff=(vals[i+1]-vals[i])**2;energy[1]+=trap;energy[3]+=fac*trap+qcoef[i]*diff;energy[2]+=dcoef[i]*diff;edgecount+=1
   p=primary['results'][cursor];cursor+=1;need((p['case'],p['row_mode'],p['index'],p['g_exact'])==(rec['case'],rec['row_mode'],j,str(g)),'actual primary direction identity');out={}
   for r,e in zip(ROWS,energy,strict=True):
    q=iv.sqrt(e/ii(g));overlap(e,p['rows'][r]['energy_arb']);overlap(q,p['rows'][r]['quotient_arb']);overlaps+=2;lo,hi=box(q);err=max(abs(lo-sq[r]),abs(hi-sq[r]));need(err<F(1,10**10)*max(F(1),abs(sq[r])),'saved scalar explicit tolerance');out[r]={'energy_iv':ss(e),'quotient_iv':ss(q),'saved_absolute_error_bound':str(err)}
   ratio=iv.sqrt(energy[3]/energy[1]);overlap(ratio,p['H1q_over_L2q_arb']);overlaps+=1;need(box(energy[2]-2*energy[0])[0]>0 and box(energy[3]-2*energy[1])[0]>0,'actual strict inequalities');allout.append({'case':rec['case'],'row_mode':rec['row_mode'],'index':j,'rows':out,'H1q_over_L2q_iv':ss(ratio)})
need(points==174160 and edgecount==173920 and checks==179484 and overlaps==54 and cursor==6,'complete image/source/energy counts')
for p in [Path(__file__),D/'evidence/arb.json',D/'evidence/arb.log']:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'unchanged final independent inputs')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_ORIGINAL_IMAGE_IMPORT_AND_EDGE_FUNCTIONALS_ONLY','iv_dps':iv.dps,'manual_ieee_source_checks':checks,'image_values':points,'edge_differences':edgecount,'interval_overlaps':overlaps,'selected_directions':6,'results':allout,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Six exact finite source images and literal positive denominators only. No g norm validation, actual operator image, singular minimum, inverse or PDE endpoint.'}
with (D/'evidence/independent.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['files','results']},indent=2))
