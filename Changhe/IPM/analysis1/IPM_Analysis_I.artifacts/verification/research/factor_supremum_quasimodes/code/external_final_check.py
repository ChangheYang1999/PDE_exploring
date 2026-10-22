"""Fresh all-pin check, including mandatory arithmetic follow-up omitted by old gate."""
import sys,json,importlib.util
from pathlib import Path
from datetime import datetime,timezone
if sys.flags.optimize:raise RuntimeError('optimized Python forbidden')
p=Path(__file__).with_name('gate.py');sp=importlib.util.spec_from_file_location('g213',p);g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
v=g.load(g.E/'verdict.json');pins=dict(v['files']);post=v['postreview'];g.check(v['status']=='CONFIRMED_FACTOR_SUPREMUM_STRAIN_ZERO_WEAK_NULL_QUASIMODES','status')
for n,h in pins.items():g.check(g.sha(g.ROOT/n)==h,'changed '+n)
supp=post['supplemental_files']
for n,h in supp.items():g.check(g.sha(g.ROOT/n)==h,'changed supplemental '+n);g.pin(pins,n,h)
a={};review=g.auth(a,'factor213_arithmetic_followup','CONFIRM_FACTOR_QUASIMODE_ARITHMETIC_CORRECTION_AND_PACKET')
for n,h in a.items():g.check(supp.get(n)==h or v['files'].get(n)==h,'unbound followup '+n)
g.check(post['arithmetic_followup']==review,'followup metadata');g.check(g.dt(v['actual_review']['end_utc'])<g.dt(review['start_utc'])<g.dt(review['end_utc'])<g.dt(post['utc']),'followup timing')
g.pin(pins,str((g.E/'verdict.json').relative_to(g.ROOT)))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_FINAL_AND_SUPPLEMENTAL_PINS_AND_ACTUAL_ARITHMETIC_FOLLOWUP','distinct_pins_including_verdict':len(pins),'verdict_sha256':g.sha(g.E/'verdict.json'),'arithmetic_followup':review,'scope':'Saved exact files and completed review correspondence; no new mathematical theorem or library attestation.'}
print(json.dumps(out))
if len(sys.argv)>1:g.save(g.E/sys.argv[1],out)
