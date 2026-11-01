"""Compare the producer's finite-fit rounding and sampling conventions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from shifted_drift390_audit import fit
from unpack_dyadic4 import unpack
ROOT=Path('research/235_reset390_conditional_audit')
start=time.monotonic();ctx.prec=512
src=ROOT/'verification/drift_fit_checks.json';data=json.loads(src.read_text());assert data['all_checks_pass']
producer=Path('../a4-num/notes/drift_fit_348_390.txt');text=producer.read_text();rows=[]
for row in data['rows']:
    if row['field']!='F':continue
    a=arb(*unpack(row['multiplier']));rounded=f'{float(a):.5f}'
    assert abs(a-arb(rounded))<arb('0.000005')
    rows.append(dict(n=row['n'],exact=a,rounded=arb(rounded),display=rounded))
printed=[(int(n),v) for n,v in re.findall(r'(\d{3}):(-?\d+\.\d+)',text)]
for n,v in printed:
    assert next(r['display'] for r in rows if r['n']==n)==v,(n,v)
results=[]
for low,high in [(348,370),(348,390),(357,390),(370,390)]:
    for sampling in ['all_orders','class_zero']:
        for precision in ['exact','rounded']:
            picked=[r for r in rows if low<=r['n']<=high and (sampling=='all_orders' or r['n']%3==0)]
            ns=[arb(r['n']) for r in picked];ys=[abs(r[precision]).log()/arb(10).log() for r in picked]
            inverse=fit([1/n for n in ns],ys);inverse['limiting_multiplier']=((arb(inverse['intercept'])*arb(10).log()).exp()).str(35,radius=True)
            results.append(dict(window=[low,high],sampling=sampling,coefficient_precision=precision,orders=[r['n'] for r in picked],power=fit([n.log()/arb(10).log() for n in ns],ys),inverse=inverse,linear_n=fit(ns,ys)))
checks=[]
for lo,hi,beta,rms,c1,limit,irms in [(348,370,'0.555','0.0023','-86.6','0.04091','0.0023'),(348,390,'0.488','0.0018','-78.1','0.03874','0.0018'),(357,390,'0.456','0.00050','-73.8','0.03773','0.00051'),(370,390,'0.469','0.00046','-77.3','0.03854','0.00046')]:
    for sampling in ['all_orders','class_zero']:
        v=next(r for r in results if r['window']==[lo,hi] and r['sampling']==sampling and r['coefficient_precision']=='rounded')
        fields=[('power_slope',v['power']['slope'],beta,'0.0005'),('power_rms',v['power']['rms'],rms,str(0.5*10**(-len(rms.split('.')[1])))),('inverse_slope',v['inverse']['slope'],c1,'0.05'),('inverse_limit',v['inverse']['limiting_multiplier'],limit,'0.000005'),('inverse_rms',v['inverse']['rms'],irms,str(0.5*10**(-len(irms.split('.')[1]))))]
        checks.append(dict(window=[lo,hi],sampling=sampling,printed_roundings=[dict(field=k,printed=p,tolerance=t,passes=bool(abs(arb(actual)-arb(p))<=arb(t))) for k,actual,p,t in fields]))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,scope='Finite fits only, conditional on329 reset; rounded values are deterministic inputs, not certified canonical coefficients.',input=dict(path=str(src),sha256=sha256(src.read_bytes()).hexdigest()),producer=dict(path=str(producer),sha256=sha256(producer.read_bytes()).hexdigest()),printed_class_zero_values_checked=len(printed),fits=results,display_comparisons=checks,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/rounded_fit_checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/rounded_drift390_audit.py').write_bytes(Path(__file__).read_bytes());(ROOT/'sources/producer_drift_348_390.txt').write_text(text)
print(json.dumps({k:v for k,v in out.items() if k!='fits'}),flush=True)
