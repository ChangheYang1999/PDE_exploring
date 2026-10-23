"""Administrative binding gate for the reviewed selected finite-tail diagnostic."""
from pathlib import Path
from datetime import datetime, timezone
import json,hashlib
R=Path('research/hydrostatic_tail_rule_provenance');V=R/'verification';root=Path.cwd().resolve()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
if (V/'DESIGN_ACCEPTANCE.json').exists():raise FileExistsError('preserve existing acceptance')
if (V/'CHECKS.json').exists():raise ValueError('candidate predates design acceptance')
bindings={}
def bind(p,h=None):
 p=Path(p).resolve();p.relative_to(root);hh=sha(p)
 if h is not None and hh!=h:raise ValueError('changed '+str(p))
 if str(p)in bindings and hh!=bindings[str(p)]:raise ValueError('inconsistent repeated path')
 bindings[str(p)]=hh
 return p
m=json.loads(bind(V/'MANUFACTURES.json').read_text())
if m['status']!='PASS_TAIL_RULE_MANUFACTURES' or m['count']!=len(m['checks'])or not all(z['passed']for z in m['checks']):raise ValueError('manufacture gate')
for p,h in m['bindings'].items():bind(p,h)
o=json.loads(bind(V/'SOURCE_OFFSET_CHECKS.json').read_text())
if o['status']!='PASS_CURRENT_BYTE_OFFSETS_AND_STATIC_READER_ASSIGNMENTS'or o['count']!=len(o['checks'])or not all(z['passed']for z in o['checks']):raise ValueError('static offset/reader gate')
for p,h in o['bindings'].items():bind(p,h)
for p in [__file__,R/'PROOF.md',R/'ENDPOINT_ROUNDING_PROOF.md',R/'REVIEW_REPAIR_PROOF.md',R/'DESIGN_CLOSURE_PROOF.md',V/'SOURCE_INPUTS.json',V/'SOURCE_OFFSETS.json',V/'before_endpoint_guard.py',V/'before_review_repairs.py',V/'before_closure_checker.py',V/'before_closure_MANUFACTURES.json',*V.glob('FAILURE_*.json')]:bind(p)
for row in json.loads((V/'SOURCE_INPUTS.json').read_text())['files']:bind(row['frozen'],row['sha256'])
reviews=[]
for lab in ['design','design_followup','design_closure']:
 v=V/('opus_'+lab);d=json.loads(bind(v/'metadata.json').read_text())
 if d['returned_model']!='claude-opus-5-5'or d['stop_reason']!='end_turn'or not d['answer_nonempty']:raise ValueError('actual completed Opus5.5 review '+lab)
 for name in ['request.txt','response.json','answer.md']:bind(v/name)
 reviews.append(dict(label=lab,metadata=d))
for p,h in list(bindings.items()):bind(p,h)
out=dict(status='ACCEPTED_FINITE_SELECTED_TAIL_DIAGNOSTIC',utc=datetime.now(timezone.utc).isoformat(),manufacture_assertion_entries=m['count'],static_assertion_entries=o['count'],bindings=bindings,reviews=reviews,scope='Candidate-free finite-tail design. Actual candidate requires318B,318MP,320 completion and cessation. No inverse accuracy, historical cause or primary endpoint accepted.')
(V/'DESIGN_ACCEPTANCE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(bindings),sha(V/'DESIGN_ACCEPTANCE.json'))
