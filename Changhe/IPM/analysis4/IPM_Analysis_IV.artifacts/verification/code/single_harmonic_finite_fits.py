"""Independent interval fits of the fully audited finite density norms."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import argparse,gzip,json,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx,fmpq
from stream_precision_audit import dyadic
from single_harmonic_finite_audit import CASES
ap=argparse.ArgumentParser();ap.add_argument('--M',type=int,required=True);a=ap.parse_args()
start=time.monotonic();now=datetime.now(timezone.utc).isoformat(timespec='seconds');ctx.prec=2304
root=Path('research/276_single_harmonic_finite_fits');out=root/'verification'/f'sin{a.M}';out.mkdir(exist_ok=True)
prior=Path(f'research/271_single_harmonic_finite_audit/verification/sin{a.M}/checks.json.gz')
data=json.loads(gzip.decompress(prior.read_bytes()));assert data['all_checks_pass']
h,Q,tag=CASES[a.M];delta=arb(fmpq(2*h,Q));N=data['maximum_order']
for key in ['harmonics','log']:
 p=Path(data[key]['path']);assert sha256(p.read_bytes()).hexdigest()==data[key]['sha256']
text=lambda z:z.str(50,radius=True)
ref=lambda p:{'path':str(p),'sha256':sha256(Path(p).read_bytes()).hexdigest()}
ln10=arb(10).log();norms={v['n']:arb(dyadic(v['f_norm'][0],v['f_norm'][1]),dyadic(v['f_norm'][2],v['f_norm'][3])) for v in data['norms']}
assert all(v>0 for v in norms.values());ys={n:v.log()/ln10 for n,v in norms.items()}
def fit(L,U,three):
 ns=list(range(L,U+1));rows=[[arb(n),arb(n).log()/ln10,arb(1)] if three else [arb(n),arb(1)] for n in ns];p=len(rows[0])
 mat=[[sum((x[i]*x[j] for x in rows),arb(0)) for j in range(p)]+[sum((x[i]*ys[n] for n,x in zip(ns,rows)),arb(0))] for i in range(p)]
 pivots=[]
 for j in range(p):
  assert not mat[j][j].contains(0);v=mat[j][j];pivots.append(text(v));mat[j]=[z/v for z in mat[j]]
  for i in range(p):
   if i==j:continue
   v=mat[i][j];mat[i]=[x-v*y for x,y in zip(mat[i],mat[j])]
 sol=[mat[i][-1] for i in range(p)];rms=(sum(((ys[n]-sum((v*s for v,s in zip(x,sol)),arb(0)))**2 for n,x in zip(ns,rows)),arb(0))/len(ns)).sqrt()
 slope=sol[0];A=(slope*ln10).exp();R=(slope*ln10/delta).exp()
 return {'L':L,'U':U,'sample_count':len(ns),'model':'n,log10(n),1' if three else 'n,1','coefficients':list(map(text,sol)),'A':text(A),'R_fit':text(R),'rms':text(rms),'pivots':pivots}
fits=[fit(L,N,three) for L in [100,150,200] if L+20<N for three in [False,True]]
slopes=[]
for lo in range(100,N-9,10):
 hi=lo+10;s=(ys[hi]-ys[lo])/10;slopes.append({'L':lo,'U':hi,'slope':text(s)})
endpoint=(ys[N]-ys[100])/(N-100)
hs=json.loads(Path(data['harmonics']['path']).read_text());last=max(map(int,hs['H']));H=arb(hs['H'][str(last)]['str']);hroot=(abs(H).log()/last).exp()
sig={int(n):arb(v) for n,v in hs['sigma'].items()};minimum=min(sig,key=lambda n:float(abs(sig[n]).mid()))
assert all(abs(sig[minimum])<abs(v) for n,v in sig.items() if n!=minimum)
response={'last_harmonic_order':last,'last_harmonic_root':text(hroot),'last_harmonic_log10':text(abs(H).log()/ln10),'minimum_response_order':minimum,'minimum_response_index':minimum//Q,'minimum_response_value':text(sig[minimum]),'signs':{str(n//Q):1 if v>0 else -1 if v<0 else 0 for n,v in sig.items()}}
if a.M==7:
 response['absolute_response_decreases_from_k6']=all(abs(sig[n+Q])<abs(sig[n]) for n in range(6*Q,last,Q))
checks=[]
def rounded(label,computed,value,unit):
 z=arb(computed);q=arb(fmpq(str(F(value))));half=arb(fmpq(str(F(unit)/2)))
 checks.append({'claim':label,'computed':text(z),'reported':value,'rounding_unit':unit,'matches_rounding':bool(z>q-half and z<q+half)})
if a.M==7:
 for L,A in [(150,'0.589'),(200,'0.653')]:rounded(f'three-parameter A on {L}..{N}',next(f['A'] for f in fits if f['L']==L and f['model']=='n,log10(n),1'),A,'0.001')
 rounded('three-parameter beta on150..N',next(f['coefficients'][1] for f in fits if f['L']==150 and f['model']=='n,log10(n),1'),'-7.2','0.1')
 rounded('line A on150..N',next(f['A'] for f in fits if f['L']==150 and f['model']=='n,1'),'0.570','0.001')
 rounded('endpoint A on100..N',(endpoint*ln10).exp(),'0.574','0.001')
 rounded('last harmonic root',hroot,'0.5535','0.0001')
 rounded('last harmonic log10',abs(H).log()/ln10,'-75.8','0.1')
result={'checked_at_utc':now,'complete':True,'M':a.M,'h':h,'Q':Q,'N':N,'bits':ctx.prec,'prior':ref(prior),'harmonics':data['harmonics'],'fits':fits,'endpoint100_to_N':{'slope':text(endpoint),'A':text((endpoint*ln10).exp()),'R_fit':text((endpoint*ln10/delta).exp())},'ten_order_slopes':slopes,'response':response,'printed_rounding_checks':checks,'all_checked_roundings_pass':all(v['matches_rounding'] for v in checks),'source':ref('code/single_harmonic_finite_fits.py'),'scope':'Finite interval statistics only; endpoint and least-squares slopes distinguished.','actual_elapsed_s':time.monotonic()-start}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/single_harmonic_finite_fits.py').write_bytes(Path('code/single_harmonic_finite_fits.py').read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['ten_order_slopes','response','fits']}),flush=True)
print(json.dumps({'fits':[{k:v for k,v in f.items() if k!='pivots'} for f in fits],'response':response}),flush=True)
