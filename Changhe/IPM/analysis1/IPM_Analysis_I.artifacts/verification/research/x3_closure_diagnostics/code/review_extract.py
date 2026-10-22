"""Extract actual audited statistics, preserving the dependency map."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
B=Path(__file__).resolve().parents[3];D=B/'research/x3_closure_diagnostics'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
r=load(D/'evidence/check.json');s=load(D/'evidence/supplement.json');pins=dict(r['files'])
for n,h in s['files'].items():
 if n in pins:assert pins[n]==h
 pins[n]=h
for p in [Path(__file__),D/'evidence/check.json',D/'evidence/supplement.json',D/'evidence/supplement_v2.log',D/'code/finalize.py',D/'RESULT_INTERPRETATION.md']:
 pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h
rec=[{k:v for k,v in x.items() if k!='near_center_maxima'}|{'near_center_maxima':{k:{a:b for a,b in v.items() if a!='identity_over_stored'}|{'identity_over_stored_exact':v['identity_over_stored']['exact']} for k,v in x['near_center_maxima'].items()}} for x in s['records']]
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'ACTUAL_SAVED_SCALAR_AUDIT_EXTRACT_REQUIRES_REVIEW','primary_utc':r['utc'],'primary_status':r['status'],'primary_counts':r['counts'],'parameters':r['parameters'],'summary':r['summary'],'supplement_utc':s['utc'],'supplement_status':s['status'],'supplement_counts':s['counts'],'derived_p_exact':s['derived_p_exact'],'provenance_order':s['provenance_order'],'near_center_records':rec,'equalities':[{k:v for k,v in e.items() if k not in ['equal_maxima','changed_maxima']} for e in s['exact_equality_observations']],'files':dict(sorted(pins.items())),'scope':r['scope']+' '+s['scope']}
with (D/'evidence/review_extract.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins)}))
