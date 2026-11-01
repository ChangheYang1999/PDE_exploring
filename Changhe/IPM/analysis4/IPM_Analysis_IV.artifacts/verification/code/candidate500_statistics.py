"""Independent finite statistics from the checked N500 Candidate007 prefix."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,pickle,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
start=time.monotonic();ctx.prec=2304
root=next(Path('research/91_candidate_checkpoint_audit/verification').glob('N500_*'))
a=json.loads((root/'checks.json').read_text());source=Path(a['input_path']);raw=source.read_bytes()
assert sha256(raw).hexdigest()==a['checkpoint_sha256'];state=pickle.loads(raw);del raw
assert max(state['f'])==500
vals=[arb(*unpack(z)) for z in state['f'][500]];i=max(range(len(vals)),key=lambda i:abs(vals[i].mid()));mx=abs(vals[i]);assert all(mx.lower()>=abs(v).upper() for j,v in enumerate(vals) if j!=i)
maximum_root=(mx.log()/500).exp()
# Match the producer's division monitor at its own precision, without importing it.
ctx.prec=2048;monitor=max((v/mx).rad() for v in vals);monitor_log=monitor.log()/arb(10).log()
assert abs(float(monitor_log.mid())-state['stats'][500]['log10_rad_over_max'])<1e-5
ctx.prec=2304
rows={x['n']:x for x in a['fields']['f']['rows']};logs={n:arb(x['log10_l1_norm'])*arb(10).log() for n,x in rows.items()}
smoothed={str(n):((logs[n]-logs[n-10])/10).exp().str(40,radius=True) for n in [250,500]}
ns=list(range(250,501));xs=[arb(1)/n for n in ns];ys=[(logs[n]-logs[n-1]).exp() for n in ns];xm=sum(xs,arb(0))/len(xs);ym=sum(ys,arb(0))/len(ys)
slope=sum(((x-xm)*(y-ym) for x,y in zip(xs,ys)),arb(0))/sum(((x-xm)**2 for x in xs),arb(0));L=ym-slope*xm
rms=(sum(((y-L-slope*x)**2 for x,y in zip(xs,ys)),arb(0))/len(xs)).sqrt()
assert f'{float(maximum_root.mid()):.4f}'=='3.4953'
assert f'{float(L.mid()):.2f}'=='3.66'
assert f'{float(rms.mid()):.1f}'=='0.7'
assert f'{float(arb(smoothed["250"]).mid()):.2f}'=='3.47'
assert f'{float(arb(smoothed["500"]).mid()):.2f}'=='3.52'
checks=[]
for n,expected in [(400,'3.4981'),(450,'3.5078'),(480,'3.5111'),(500,'3.5113')]:
 assert f'{float(arb(rows[n]["l1_root"]).mid()):.4f}'==expected;checks.append(dict(n=n,expected=expected))
assert f'{float(arb(rows[500]["l2_root"]).mid()):.4f}'=='3.4990'
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,checkpoint_sha256=a['checkpoint_sha256'],precision_bits=2304,maximum_coefficient_index=i,maximum_frequency=2*i+1,maximum_coefficient_root=maximum_root.str(40,radius=True),monitor_precision_bits=2048,monitor_log10=monitor_log.str(40,radius=True),reported_monitor=state['stats'][500]['log10_rad_over_max'],smoothed_10step=smoothed,fit_orders=[250,500],fit_L=L.str(40,radius=True),fit_rms=rms.str(40,radius=True),root_roundings=checks,actual_elapsed_s=time.monotonic()-start,scope='Finite statistics only; no asymptotic model is certified.')
(root/'statistics_checks.json').write_text(json.dumps(out,indent=2)+'\n')
(root/'sources/candidate500_statistics.py').write_bytes(Path('code/candidate500_statistics.py').read_bytes())
(root/'sources/producer_numerical_report.md').write_bytes(Path('../a4-num/FARFIELD_NUMERICAL_EXPERIMENTS.md').read_bytes())
print(json.dumps(out))
