"""Fail-closed review, immutable input and completed-run acceptance helpers."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_archive_second';E=D/'evidence';R=B/'notes/reviews'
COUNTS={'H':3265568,'I':406638,'J':406638,'I_steps':406638,'J_steps':406638}
def need(x,s):
 if not x:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def when(s):return datetime.fromisoformat(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def unique(items):
 out={}
 for k,v in items:need(k not in out,'duplicate JSON key');out[k]=v
 return out
def load(p):return json.loads(Path(p).read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def write(p,v):
 with Path(p).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def pin(pins,p,expected=None):
 p=Path(p);p=(p if p.is_absolute() else B/p).resolve();need(p.is_relative_to(B),'lane-only evidence pin');n=str(p.relative_to(B));h=sha(p);need(expected is None or h==expected,'input pin '+n);need(n not in pins or pins[n]==h,'pin conflict '+n);pins[n]=h;return h
def merge(pins,mapping):
 for n,h in mapping.items():pin(pins,n,h)
def auth(pins,tag,verdict,required):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text();answer=(R/(tag+'_response.md')).read_text();need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and 'availability_error' not in m,'actual completed Opus5.5');need(len(m['files'])==len(set(m['files'])) and set(required)<=set(m['files']),'complete review bundle');prefix=request.split('\n\nFILE ',1)[0];need(all(s in prefix for s in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds','no outside writes','no people contact']),'delegation restrictions');rebuilt=prefix+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']);need(rebuilt==request and hashlib.sha256(request.encode()).hexdigest()==m['input_sha256'],'actual unchanged request bundle');need(answer=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n','actual response text');need(re.search(r'(?m)^VERDICT:\s*'+re.escape(verdict)+r'\s*$',answer) is not None,'exact actual verdict');need(when(m['start_utc'])<=when(m['end_utc'])<=datetime.now(timezone.utc),'actual review chronology')
 for n in m['files']:pin(pins,n)
 for suffix in ['metadata.json','request.txt','response.json','response.md']:pin(pins,R/(tag+'_'+suffix))
 return {k:m[k] for k in ['start_utc','end_utc','request_id','input_sha256','actual_response_model','stop_reason']}
def preparation():
 pins={};p=load(E/'preflight_manifest.json');need(p['status']=='ACCEPTED_PREPARATION_ONLY','accepted preparation');merge(pins,p['files']);pin(pins,E/'preflight_manifest.json');return pins,p
def completed():
 pins,pre=preparation();s=load(E/'full_summary.json');a=load(E/'full_output_audit.json');q=load(E/'queue_status.json');need(s['status']=='COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT' and a['status']=='PASS_COMPLETE_ARCHIVE_SAVED_OUTPUT_AND_INDEPENDENT_NEWTON_ANCHOR_AUDIT' and q['status']=='COMPUTATION_AND_AUDIT_COMPLETE_REQUIRES_VERIFIER_CLOSURE','actual completed stages');need(s['counts']==a['counts']==COUNTS and s['archive_footer_read'] is True and a['archive_footer_read'] is True and s['exact_anchor_checks']==3915 and s['iv_dps']==200,'all complete full counts');need(a['saved_moment_checks']==15580 and a['selected_H_Newton_checks']==1558 and a['independent_exact_anchors']==783,'complete auditor counts');need(s['output_sha256']==a['output_sha256']==pin(pins,E/'full_spans.jsonl') and a['summary_sha256']==pin(pins,E/'full_summary.json') and q['audit_sha256']==pin(pins,E/'full_output_audit.json'),'actual data binding');need(s['preflight_sha256']==a['preflight_sha256']==sha(E/'preflight_manifest.json') and s['producer_sha256']==sha(D/'code/full.py') and s['engine_sha256']==sha(D/'code/engine.py') and a['auditor_sha256']==sha(D/'code/audit.py'),'actual operative sources');need(when(pre['utc'])<when(s['start_utc'])<when(s['utc'])<when(a['start_utc'])<when(a['utc'])<=when(q['utc']),'preparation/computation/audit chronology');events=[json.loads(line) for line in (E/'queue_execution.jsonl').read_text().splitlines()];expected=[('full_independent_propagation',['python3','research/canonical_archive_second/code/full.py']),('full_output_and_anchor_audit',['python3','research/canonical_archive_second/code/audit.py'])];need(len(events)==2,'two actual stages')
 for ev,(name,cmd),obj in zip(events,expected,[s,a],strict=True):
  need(ev['stage']==name and ev['command']==cmd and ev['returncode']==0 and ev['queue_source_sha256']==sha(D/'code/run_queue.sh'),'actual stage success/source');need(when(ev['start_utc'])<=when(obj['start_utc'])<when(obj['utc'])<=when(ev['end_utc']),'actual output within stage');pin(pins,ev['log'],ev['log_sha256'])
 need(when(events[0]['end_utc'])<=when(events[1]['start_utc']),'sequential stages');pin(pins,E/'queue_execution.jsonl');pin(pins,E/'queue_status.json');return pins,pre,s,a,q
