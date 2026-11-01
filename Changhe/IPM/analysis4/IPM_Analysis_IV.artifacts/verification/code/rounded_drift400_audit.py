"""Reproduce rounded multiplier fits and distinguish them from full-ball fits."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
from hashlib import sha256
import json,re,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from shifted_drift400_audit import fit
from unpack_dyadic4 import unpack
ROOT=Path('research/254_reset400_conditional_audit')
start=time.monotonic();ctx.prec=512
src=ROOT/'verification/drift_fit_checks.json';data=json.loads(src.read_text());assert data['all_checks_pass']
producer=Path('../a4-num/notes/drift_fit_348_400.txt');text=producer.read_text();rows=[]
for row in data['rows']:
 if row['field']!='F':continue
 a=arb(*unpack(row['multiplier']));rounded=f'{float(a):.5f}'
 assert abs(a-arb(rounded))<arb('0.000005')
 rows.append(dict(n=row['n'],exact=a,rounded=arb(rounded),display=rounded))
printed=[(int(n),v) for n,v in re.findall(r'(\d{3}):(-?\d+\.\d+)',text)]
for n,v in printed:assert next(r['display'] for r in rows if r['n']==n)==v,(n,v)
results=[]
for low,high in [(357,400),(370,400),(381,400)]:
 for sampling in ['all_orders','class_zero']:
  for precision in ['exact','rounded']:
   picked=[r for r in rows if low<=r['n']<=high and (sampling=='all_orders' or r['n']%3==0)]
   ns=[arb(r['n']) for r in picked];ys=[abs(r[precision]).log()/arb(10).log() for r in picked]
   inverse=fit([1/n for n in ns],ys);inverse['limiting_multiplier']=((arb(inverse['intercept'])*arb(10).log()).exp()).str(35,radius=True)
   results.append(dict(window=[low,high],sampling=sampling,coefficient_precision=precision,orders=[r['n'] for r in picked],power=fit([n.log()/arb(10).log() for n in ns],ys),inverse=inverse,linear_n=fit(ns,ys)))
checks=[]
pattern=r'window (\d+)\.\.(\d+): power beta = ([\d.e+-]+) \(rms ([\d.e+-]+)\); 1/n: \|a_inf\| = ([\d.e+-]+) \(rms ([\d.e+-]+)\); linear in n: slope ([\d.e+-]+)/order \(rms ([\d.e+-]+)\)'
parsed=re.findall(pattern,text);assert len(parsed)==3
for lo,hi,beta,prms,limit,irms,slope,lrms in parsed:
 for sampling in ['all_orders','class_zero']:
  for precision in ['exact','rounded']:
   v=next(r for r in results if r['window']==list(map(int,[lo,hi])) and r['sampling']==sampling and r['coefficient_precision']==precision)
   fields=[('power_slope',v['power']['slope'],beta),('power_rms',v['power']['rms'],prms),('inverse_limit',v['inverse']['limiting_multiplier'],limit),('inverse_rms',v['inverse']['rms'],irms),('linear_slope',v['linear_n']['slope'],slope),('linear_rms',v['linear_n']['rms'],lrms)]
   comparisons=[]
   for label,actual,printedvalue in fields:
    tol=Decimal(5).scaleb(Decimal(printedvalue).as_tuple().exponent-1)
    comparisons.append(dict(field=label,printed=printedvalue,tolerance=str(tol),passes=bool(abs(arb(actual)-arb(printedvalue))<=arb(str(tol)))))
   checks.append(dict(window=[int(lo),int(hi)],sampling=sampling,coefficient_precision=precision,all_printed_roundings_match=all(r['passes'] for r in comparisons),comparisons=comparisons))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,scope='Finite fits conditional on329 reset. Rounded multiplier displays are deterministic inputs, not certified canonical coefficients.',input=dict(path=str(src),sha256=sha256(src.read_bytes()).hexdigest()),producer=dict(path=str(producer),sha256=sha256(producer.read_bytes()).hexdigest()),printed_class_zero_values_checked=len(printed),fits=results,display_comparisons=checks,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/rounded_fit_checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/rounded_drift400_audit.py').write_bytes(Path(__file__).read_bytes());(ROOT/'sources/producer_drift_348_400.txt').write_text(text)
print(json.dumps({k:v for k,v in out.items() if k!='fits'}),flush=True)
