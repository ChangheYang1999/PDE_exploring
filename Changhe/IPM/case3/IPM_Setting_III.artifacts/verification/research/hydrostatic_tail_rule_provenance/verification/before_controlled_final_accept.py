"""Bind the reviewed controlled-record design before any candidate comparison."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/hydrostatic_tail_rule_provenance');V=R/'verification';root=Path.cwd().resolve();bindings={}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p,h=None):
 p=Path(p).resolve();p.relative_to(root);hh=sha(p)
 if h is not None and hh!=h:raise ValueError('changed '+str(p))
 if str(p)in bindings and bindings[str(p)]!=hh:raise ValueError('inconsistent binding')
 bindings[str(p)]=hh;return p
if (V/'CONTROLLED_DESIGN_ACCEPTANCE.json').exists()or(V/'CONTROLLED_RECORD_CHECKS.json').exists():raise ValueError('preserve previous acceptance/result')
for name,status in [('CONTROLLED_RECORD_MANUFACTURES.json','PASS_CONTROLLED_RECORD_MANUFACTURES'),('CONTROLLED_PREFLIGHT.json','PASS_323_RELATIVE_SCHEMA_AND_ACCEPTED_HEADERS')]:
 d=json.loads(bind(V/name).read_text())
 if d['status']!=status or d['count']!=len(d['checks'])or not all(z['passed']for z in d['checks']):raise ValueError('semantic gate '+name)
 key=str(Path('independent_code/check_tail_controlled_records.py').resolve())
 if d['bindings'].get(key)!=sha(key):raise ValueError('own script pin')
 for p,h in d['bindings'].items():bind(p,h)
for p in [__file__,*R.glob('CONTROLLED*.md'),*V.glob('before_controlled*'),V/'CONTROLLED_PREFLIGHT_FAILURE.json']:bind(p)
reviews=[]
for lab in ['controlled_design','controlled_design_followup','controlled_design_closure']:
 v=V/('opus_'+lab);d=json.loads(bind(v/'metadata.json').read_text())
 if d['requested_model']!='us.anthropic.claude-opus-5-5'or d['returned_model']!='claude-opus-5-5'or d['stop_reason']!='end_turn'or not d['answer_nonempty']:raise ValueError('actual completed review '+lab)
 for name in ['request.txt','response.json','answer.md']:bind(v/name)
 reviews.append(dict(label=lab,metadata=d))
for p,h in list(bindings.items()):bind(p,h)
d=dict(status='ACCEPTED_CONTROLLED_PRINTED_RECORD_DESIGN',utc=datetime.now(timezone.utc).isoformat(),bindings=bindings,reviews=reviews,scope='Before controlled record comparison. Current entry-file identity is static only. No authenticated historical execution, unrounded equality, causal proof or primary endpoint.')
(V/'CONTROLLED_DESIGN_ACCEPTANCE.json').write_text(json.dumps(d,indent=2)+'\n')
print(d['status'],len(bindings),sha(V/'CONTROLLED_DESIGN_ACCEPTANCE.json'))
