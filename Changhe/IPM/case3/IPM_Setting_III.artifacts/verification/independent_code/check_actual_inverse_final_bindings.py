from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=str(p);hh=sha(p);ck('binding '+p,(h is None or hh==h)and(p not in bindings or bindings[p]==hh));bindings[p]=hh;return Path(p)
for p in [__file__,R/'FINAL_REVIEW_RESOLUTION_PROOF.md',R/'RESULTS_DRAFT.md',R/'RESULTS_REPAIRED_DRAFT.md',Path('independent_code/prepare_actual_inverse_final_followup.py'),V/'FINAL_FOLLOWUP_INPUTS.json',V/'FINAL_REVIEW_INPUTS.json']:bind(p)
for name,count,status,h in [('FINAL_SUMMARY_CHECKS.json',60871,'PASS_FINITE_RECOMPUTATION_REQUIRES_ACTUAL_REVIEW','35cf718cf57daedec9c2ff9e0203e6a1a45e9a736a3c79840c4e725c89669f58'),('FINAL_COMPONENT_CHECKS.json',3258,'PASS_FINITE_COMPONENTS_AND_MAP_DECOMPOSITION',None)]:
 d=json.loads(bind(V/name,h).read_text());ck('accepted gate '+name,d['count']==count==len(d['checks'])and d['status']==status and all(q['passed']for q in d['checks']))
 for p,hh in d['bindings'].items():bind(p,hh)
for stem,reqid in [('final','8909e38f-be19-4a58-b718-2db62657a945'),('final_followup','1b5c8c75-5cd4-463d-89b1-d4f4c6341602')]:
 p=V/('opus_'+stem);m=json.loads(bind(p/'metadata.json').read_text());r=json.loads(bind(p/'response.json').read_text());ans=bind(p/'answer.md').read_text();bind(p/'request.txt',m['request_sha256']);bind(V/('OPUS_'+stem.upper()+'_REQUEST.txt'),m['request_sha256'])
 ck('actual returned model '+stem,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==r['model']=='claude-opus-5-5'and m['request_id']==reqid)
 ck('completed actual review '+stem,m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty']and ans.strip()=='\n\n'.join(x.get('text','')for x in r['content']if x['type']=='text').strip())
 ck('review timing '+stem,datetime.fromisoformat(m['started_utc'])<datetime.fromisoformat(m['finished_utc'])<=datetime.now(timezone.utc))
 ck('request context contains exact draft '+stem,(R/('RESULTS_REPAIRED_DRAFT.md'if stem.endswith('followup')else'RESULTS_DRAFT.md')).read_text()in(p/'request.txt').read_text())
 if stem.endswith('followup'):ck('resolved desk objections','No blocking mathematical or interpretive issue remains.'in ans and 'My "≤3.9e' in ans)
for name in ['FINAL_REVIEW_INPUTS.json','FINAL_FOLLOWUP_INPUTS.json']:
 d=json.loads((V/name).read_text())
 for p,h in d['files'].items():bind(p,h)
for p in sorted((V/'component_initial_dictionary_failure').iterdir()):bind(p)
s=(R/'RESULTS_REPAIRED_DRAFT.md').read_text()
for clause in ['Which velocity is closer to the exact integral\nremains OPEN.','three rules of one independent inverse implementation','C\nchecked at the selected 30 points only','at the twelve regional maximizing entries','The principal verdict\nremains UNRESOLVED.']:
 ck('scope '+clause.lower(),clause.lower()in s.lower())
for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
now=datetime.now(timezone.utc).isoformat();out=dict(status='CONFIRMED_FINITE_ACTUAL_NODE_INVERSE_COMPARISON',utc=now,count=len(checks),checks=checks,bindings=bindings,reviewed_draft_sha256=sha(R/'RESULTS_REPAIRED_DRAFT.md'),scope='Finite auxiliary hydrostatic N96 actual-node residual, component and empirical MP comparison. Exact integral accuracy OPEN; full-plane IPM UNRESOLVED.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),len(bindings),now,sha(V/'FINAL_BINDINGS.json'))
