from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,pickle,math,time
start=time.monotonic()
root=Path('research/102_edge_recurrence_reference')
out=root/'verification/float_edge1_20261031T0749Z'
out.mkdir(exist_ok=True)
raw=Path('../a4-num/ckpt/log23_edge1_float.pkl').read_bytes()
(out/'input_checkpoint.pkl.gz').write_bytes(gzip.compress(raw,compresslevel=3,mtime=0))
d=pickle.loads(raw)
assert d['ring']=='float' and d['A']=='2' and d['B']=='3'
refpath=root/'verification/exact_reference.json'
ref=json.loads(refpath.read_text())['variants']['1']['rows']
maxrel=(Fraction(0),None); maxnorm=(Fraction(0),None); maxabs=(Fraction(0),None)
checks=0; zero_mismatches=[]
for row in ref:
 n=row['n']
 for field,name in [('f','density'),('g','stream')]:
  exact={(int(q),int(k)):Fraction(v) for q,c in row[name].items() for k,v in c.items()}
  approx={(q,2*j+(1 if field=='f' else 0)):Fraction.from_float(float(v)) for q,c in enumerate(d[field][n]) for j,v in enumerate(c)}
  norm=Fraction(row[name+'_plain_norm'])
  for key in set(exact)|set(approx):
   x=exact.get(key,Fraction(0));y=approx.get(key,Fraction(0)); e=abs(x-y);loc=[field,n,*key]
   checks+=1
   if e>maxabs[0]:maxabs=(e,loc)
   if e/norm>maxnorm[0]:maxnorm=(e/norm,loc)
   if x and e/abs(x)>maxrel[0]:maxrel=(e/abs(x),loc)
   if not x and y:zero_mismatches.append(dict(location=loc,float_value=str(y)))
rows=[];staterror=0.;nonfinite=0;subnormal=0
for n in sorted(d['f']):
 rec=dict(n=n)
 for field,name,stkey in [('f','density','log10_sum_cols'),('g','stream','log10_sum_gcols')]:
  cols=[]
  for c in d[field][n]:
   vals=[float(v) for v in c]
   nonfinite+=sum(not math.isfinite(v) for v in vals)
   subnormal+=sum(0<abs(v)<float.fromhex('0x1p-1022') for v in vals)
   cols.append(math.fsum(abs(v) for v in vals))
  assert all(math.isfinite(x) for x in cols)
  norm=math.fsum(cols);log=math.log10(norm)
  vals=[(math.lgamma(q+1)/math.log(10)+math.log10(v/cols[0]),q) for q,v in enumerate(cols) if q and v]
  rec[name]=dict(log10_plain_norm=log,root=10**(log/n),log_degree=max(q for q,v in enumerate(cols) if v),factorial_max=max(vals)[0] if vals else None,factorial_argmax=max(vals)[1] if vals else None)
  if len(cols)>30 and cols[30]:rec[name]['factorial_q30']=math.lgamma(31)/math.log(10)+math.log10(cols[30]/cols[0])
  st=d['stats'][n].get(stkey)
  if st is not None:staterror=max(staterror,abs(log-st))
 rec['log10_N_over_M']=rec['stream']['log10_plain_norm']-rec['density']['log10_plain_norm']
 rows.append(rec)
lookup={r['n']:r for r in rows}
slopes={}
for n in [100,150,185,193,200,max(d['f'])]:
 if n not in lookup or n<27:continue
 fit={}
 for name in ['density','stream']:
  x=list(range(n-26,n+1));mid=n-13
  fit[name]=math.fsum((i-mid)*lookup[i][name]['log10_plain_norm'] for i in x)/math.fsum((i-mid)**2 for i in x)
 slopes[str(n)]=fit
summary=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),source_path='../a4-num/ckpt/log23_edge1_float.pkl',source_sha256=sha256(raw).hexdigest(),source_bytes=len(raw),exact_reference_sha256=sha256(refpath.read_bytes()).hexdigest(),N=max(d['f']),exact_comparisons=checks,exact_orders=18,max_absolute_error=dict(value=float(maxabs[0]),location=maxabs[1]),max_relative_error=dict(value=float(maxrel[0]),location=maxrel[1]),max_error_over_order_norm=dict(value=float(maxnorm[0]),location=maxnorm[1]),exact_zero_mismatches=zero_mismatches,nonfinite_values=nonfinite,subnormal_nonzero_values=subnormal,max_stored_log_stat_difference=staterror,slopes_27=slopes,selected_rows=[lookup[n] for n in [100,120,150,160,185,186,187,188,193,200,max(d['f'])] if n in lookup],scope='Floating diagnostics only. No error enclosure, no all-order growth inference; subnormal tails and rounding may affect high-order values.',actual_elapsed_s=time.monotonic()-start)
(out/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'all_rows.json').write_text(json.dumps(rows,indent=2)+'\n')
(root/'sources/edge_float_audit.py').write_text(Path(__file__).read_text())
print(json.dumps(summary,indent=2))
