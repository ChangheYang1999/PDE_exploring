from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,ast,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_composition'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(x,s):
 if not x:raise ValueError(s)
v=json.loads((D/'evidence/verdict.json').read_text());check(len(v['files'])==227,'old pin count')
for name,h in v['files'].items():check(sha(B/name)==h,'old pin '+name)
p=D/'FINAL_REVIEW_RESOLUTIONS.md';old=p.read_text();wrong='Each current candidate\nrange was separately contained by both independent reference methods.';right='Each independent reference interval is contained in the corresponding\nreported candidate range.'
check(old.count(wrong)==1,'unique reversed sentence');target=D/'FINAL_REVIEW_RESOLUTIONS_v2.md';new=old.replace(wrong,right)
if target.exists():check(target.read_text()==new,'immutable corrected version')
else:target.write_text(new)
checks=0;minimum=None;records=[]
for ci in [0,4102,7808]:
 for engine in ['exact','iv']:
  p=D/f'evidence/{engine}_{ci:04d}.json';a=json.loads(p.read_text());check(a['status']=='PASS' and a['ci']==ci,'record identity')
  for row in a['rows']:
   for r in row['ranges']:
    l,u=map(F,r['reference']);a0,b0=map(F,r['target']);check(a0<=l<=u<=b0 and r['contained'] is True,'direction')
    margins=[l-a0,b0-u];check(margins==list(map(F,r['margins'])) and min(margins)>0,'strict exact margin')
    minimum=min(margins) if minimum is None else min(minimum,*margins);checks+=1
  records.append({'file':str(p.relative_to(B)),'sha256':sha(p)})
check(checks==72,'complete comparison count')
bindings=[]
for name in ['exact_check.py','iv_check.py']:
 p=D/'code'/name;tree=ast.parse(p.read_text());expected=ast.dump(ast.parse('target[0]<=ref[0] and ref[1]<=target[1]',mode='eval').body,include_attributes=False)
 hits=[n for n in ast.walk(tree) if ast.dump(n,include_attributes=False)==expected];check(len(hits)==1,'source comparison '+name);bindings.append({'file':str(p.relative_to(B)),'line':hits[0].lineno,'sha256':sha(p),'expression':'target[0]<=ref[0] and ref[1]<=target[1]'})
p=D/'code/audit_outputs.py';tree=ast.parse(p.read_text());expected=ast.dump(ast.parse('tl<=lo<=hi<=th and result["contained"] is True',mode='eval').body,include_attributes=False);hits=[n for n in ast.walk(tree) if ast.dump(n,include_attributes=False)==expected];check(len(hits)==1,'auditor direction');bindings.append({'file':str(p.relative_to(B)),'line':hits[0].lineno,'sha256':sha(p),'expression':'tl<=lo<=hi<=th and result["contained"] is True'})
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_WORDING_ERRATUM_UNCHANGED_72_CONTAINMENTS','prior_verdict_sha256':sha(D/'evidence/verdict.json'),'old_pins_rechecked':227,'corrected_file_sha256':sha(target),'comparisons_checked':checks,'minimum_exact_margin':str(minimum),'records':records,'bindings':bindings,'code_sha256':sha(Path(__file__)),'scope':'Versioned wording erratum only. Every prior pin unchanged. Numerical theorem and all open gaps unchanged.'}
p=D/'evidence/erratum_checks.json';check(not p.exists(),'immutable result');p.write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],result['status'],sha(p))
