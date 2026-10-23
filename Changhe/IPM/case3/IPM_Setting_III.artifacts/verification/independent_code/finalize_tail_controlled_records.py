"""Bind the manually reviewed finite record result; no producer execution."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/hydrostatic_tail_rule_provenance');V=R/'verification';root=Path.cwd().resolve();bindings={};checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,value):
 checks.append(dict(name=name,passed=bool(value)))
 if not value:raise ValueError(name)
def bind(p,h=None):
 p=Path(p).resolve();p.relative_to(root);a=sha(p);ck('binding '+str(p),(h is None or h==a)and(str(p)not in bindings or bindings[str(p)]==a));bindings[str(p)]=a;return p
def gate(name,status):
 d=json.loads(bind(V/name).read_text());ck('semantic '+name,d['status']==status and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
 return d
out=V/'CONTROLLED_FINAL_BINDINGS.json';ck('final absent',not out.exists())
a=json.loads(bind(V/'CONTROLLED_DESIGN_ACCEPTANCE.json').read_text());ck('design accepted',a['status']=='ACCEPTED_CONTROLLED_PRINTED_RECORD_DESIGN'and a['controlled_snapshot_absent']is True)
for p,h in a['bindings'].items():bind(p,h)
for name,status in [('CONTROLLED_RECORD_MANUFACTURES.json','PASS_CONTROLLED_RECORD_MANUFACTURES'),('CONTROLLED_PREFLIGHT.json','PASS_323_RELATIVE_SCHEMA_AND_ACCEPTED_HEADERS'),('CONTROLLED_RECORD_CHECKS.json','CONFIRMED_CONTROLLED_PRINTED_RECORD_EQUALITIES_REQUIRES_REVIEW')]:gate(name,status)
reviews=[]
for lab in ['controlled_design','controlled_design_followup','controlled_design_closure','controlled_final','controlled_final_closure']:
 v=V/('opus_'+lab);m=json.loads(bind(v/'metadata.json').read_text());ck('actual completed model '+lab,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']=='claude-opus-5-5'and m['stop_reason']=='end_turn'and m['answer_nonempty']);bind(v/'request.txt',m['request_sha256'])
 for n in ['response.json','answer.md']:bind(v/n)
 reviews.append(dict(label=lab,metadata=m))
for p in [__file__,*R.glob('CONTROLLED*.md'),V/'CONTROLLED_NOTE_SOURCE.json',V/'producer_note176_176a.txt',V/'before_controlled_final_timestamp.md']:bind(p)
d=json.loads((V/'CONTROLLED_RECORD_CHECKS.json').read_text());ck('six regional differences and no argmax difference',len(d['changed_region_tokens'])==6 and not d['changed_argmax_tokens']);ck('three maxima and three medians',sum(z['field']=='median_Rf'for z in d['changed_region_tokens'])==3)
res=(R/'CONTROLLED_RESULTS.md').read_text();ck('revision time after closure','Revised 'in res and 'after both actual final reviews' in res)
for p,h in list(bindings.items()):bind(p,h)
z=dict(status='CONFIRMED_FINITE_CONTROLLED_RECORD_AUDIT',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,reviews=reviews,scope='Specified printed record lines and six-token difference list only. Execution, state identity beyond headers, unrounded equality, general chunk invariance, causality and inverse accuracy OPEN. Independent selected-tail candidate unexecuted. Primary IPM UNRESOLVED.')
out.write_text(json.dumps(z,indent=2)+'\n');print(z['status'],z['count'],len(bindings),sha(out))
