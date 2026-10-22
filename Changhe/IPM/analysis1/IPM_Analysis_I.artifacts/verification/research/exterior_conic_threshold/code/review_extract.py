"""Bounded exact outward extraction for review; raw large fractions stay archived."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
sys.set_int_max_str_digits(200000)
B=Path(__file__).resolve().parents[3];D=B/'research/exterior_conic_threshold';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
s=load(E/'scalars.json');q=load(E/'audit.json');scale=10**40
assert q['scalar_sha256']==sha(E/'scalars.json')
def floor(x):return F(x.numerator*scale//x.denominator,scale)
def ceil(x):return -floor(-x)
methods={}
for method,rows in s['methods'].items():
 methods[method]={}
 for key,pair in rows.items():
  l,u=map(F,pair);a,b=floor(l),ceil(u);assert a<=l<=u<=b
  methods[method][key]=[str(a),str(b)]
margins={}
for method,rows in q['strict_margins_exact'].items():
 margins[method]={}
 for key,x in rows.items():
  x=F(x);z=floor(x);assert 0<z<=x;margins[method][key]=str(z)
v=load(B/'research/exterior_flow/evidence/verdict.json');assert v['files']['research/exterior_flow/evidence/checks.json']==sha(B/'research/exterior_flow/evidence/checks.json')
old=load(B/'research/exterior_flow/evidence/checks.json');assert s['inherited_row']==next(r for r in old['cases'] if r['T_exact']=='1')
entries=[]
for f in ['research/exterior_flow/evidence/verdict.json','research/exterior_flow/evidence/checks.json','research/exterior_flow/code/audit_output.py','research/exterior_flow/code/check_tail.py','research/exterior_conic_threshold/evidence/scalars.json','research/exterior_conic_threshold/evidence/audit.json','research/exterior_conic_threshold/code/compute.py','research/exterior_conic_threshold/code/audit.py','research/exterior_conic_threshold/code/review_extract.py','research/exterior_conic_threshold/ADDENDUM.md']:
 entries.append({'file':f,'sha256':sha(B/f)})
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'EXACT_OUTWARD_REVIEW_EXTRACT','raw_parameters_exact':s['parameters_exact'],'accepted_T1_row':s['inherited_row'],'all_accepted_rows':[r['T_exact'] for r in old['cases']],'outward_40decimal_rational_scalar_intervals':methods,'positive_40decimal_rational_lower_margins':margins,'audit_counts':q['counts'],'producer_start_utc':s['start_utc'],'producer_end_utc':s['end_utc'],'producer_seconds':s['seconds'],'entries':entries,'scope':'Each short interval contains the full saved scalar interval by exact rational comparison. Raw series remain in hash-bound scalars.json; this is a view, not an independent enclosure method.'}
p=E/'review_extract.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(p.stat().st_size,sha(p))
