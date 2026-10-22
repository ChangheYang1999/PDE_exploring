"""Review and immutable-input gates for topic177. No source modules executed."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import sys
sys.dont_write_bytecode=True
import json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];D=B/'research/source_graph_nonlinearity';E=D/'evidence';R=B/'notes/reviews'
PTAG='source_graph_nonlinearity_proof';ATAG='source_graph_nonlinearity_actual'
PSCOPE='CONFIRM_SOURCE_GRAPH_NONLINEARITY_PROOF_ONLY';ASCOPE='CONFIRM_WEAK_SOURCE_GRAPH_NONLINEAR_DISCONTINUITY'
OWN=['PROOF.md','ADDENDUM.md','evidence/proof_birth.json','PROOF_ADJUDICATION.md','evidence/PROOF_ADJUDICATION.json','code/common.py','code/check.py','code/extract.py','code/launch_actual.py','code/finalize.py','proof_files.json','proof_question.txt','actual_files.json','actual_question.txt','parents.json','PROTOCOL.md']
EXTERNAL={str(B.parent/'ipmA-num/data/cert_green.npz'):'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'}
PREFIX='You are Claude Opus 5.5 collaborating with GPT-6, reviewing a mathematical computer-assisted IPM proof. Restrictions on this delegated task: no JavaScript/TypeScript development or execution; no servers/listeners/tunnels; no RLScience cluster; no Lean/Lake builds; no outside writes; no people contact. Pure text review only. Return a concise substantive FINAL ANSWER, not just internal reasoning. Reconstruct claims and reject gaps. '
def now():return datetime.now(timezone.utc).isoformat()
def when(x):
 t=datetime.fromisoformat(x);need(t.tzinfo is not None,'UTC-aware timestamp');return t
def need(v,s):
 if not v:raise ValueError(s)
def load(p):return json.loads(Path(p).read_text())
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,v):
 p=Path(p);need(p.resolve().is_relative_to(B),'only lane writes')
 with p.open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def pin(p,n,h=None):
 q=(B/n).resolve();need(q.is_relative_to(B) or EXTERNAL.get(str(q))==h and h is not None,'only fixed external input');key=str(q.relative_to(B)) if q.is_relative_to(B) else str(q);got=sha(q);need(h is None or got==h,'unchanged '+key);need(key not in p or p[key]==got,'consistent pin '+key);p[key]=got;return got
def rehash(p):
 for n,h in p.items():need(sha(B/n)==h,'unchanged final '+n)
def auth(p,tag,verdict,files,question):
 m=load(R/(tag+'_metadata.json'));r=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();request=(R/(tag+'_request.txt')).read_text()
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==r['model']=='claude-opus-5-5' and m['stop_reason']==r['stop_reason']=='end_turn' and 'availability_error' not in m,'actual complete Opus5.5')
 need(m['files']==files and len(files)==len(set(files)),'exact fixed complete review list')
 expected=PREFIX+(D/question).read_text()+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in files)
 need(request==expected and hashlib.sha256(request.encode()).hexdigest()==m['input_sha256'],'entire actual request identity')
 need(text=='\n\n'.join(x['text'] for x in r['content'] if x['type']=='text')+'\n','full actual response identity')
 need(re.findall(r'(?m)^(?:\*\*)?VERDICT:\s*(\w+)(?:\*\*)?\s*$',text)==[verdict],'unique exact scoped review verdict');need(tag==PTAG or text.rstrip().splitlines()[-1]=='VERDICT: '+verdict,'actual final scoped verdict')
 need(when(m['start_utc'])<when(m['end_utc'])<datetime.now(timezone.utc),'review chronology')
 for n in files:pin(p,n)
 for suffix in ['metadata.json','request.txt','response.json','response.md']:pin(p,R/(tag+'_'+suffix))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
def post(p,tag,r,stem):
 a=D/(stem+'.md');record=E/(stem+'.json');v=load(record);rh=sha(R/(tag+'_response.json'));need(v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==r['request_id'] and v['input_sha256']==r['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(a) and v['all_substantive_objections_resolved'] is True,'later own review binding')
 need(r['request_id'] in a.read_text() and rh in a.read_text(),'written actual disposition');need(when(r['end_utc'])<when(v['utc'])<datetime.now(timezone.utc),'later own disposition')
 m=load(R/(tag+'_metadata.json'));need(str(a.relative_to(B)) not in m['files'] and str(record.relative_to(B)) not in m['files'],'own post outside reviewed files');pin(p,a);pin(p,record);return v
def parent_gate(v,expected):
 need(v['status']==expected['status'] and len(v['files'])==expected['pins'],'exact accepted parent')
 need(when(v['utc'])<datetime.now(timezone.utc),'past parent')
def base():
 p={};parents={}
 for label,z in load(D/'parents.json').items():
  pin(p,z['path'],z['sha256']);v=load(B/z['path']);parent_gate(v,z)
  parents[label]={**z,'utc':v['utc']}
  for n,h in v['files'].items():pin(p,n,h)
 proof=load(E/'proof_birth.json');need(proof['proof_sha256']==sha(D/'PROOF.md'),'immutable proof first')
 r=auth(p,PTAG,PSCOPE,load(D/'proof_files.json'),'proof_question.txt');po=post(p,PTAG,r,'PROOF_ADJUDICATION')
 fr=load(E/'source_freeze.json');expected={str((D/n).relative_to(B)):sha(D/n) for n in OWN}
 need(fr['files']==dict(sorted(expected.items())),'complete unchanged source freeze')
 need(when(proof['utc'])<when(r['start_utc'])<when(r['end_utc'])<when(po['utc'])<when(fr['utc'])<datetime.now(timezone.utc),'proof, review, own disposition and implementation')
 for n,h in fr['files'].items():pin(p,n,h)
 pin(p,E/'source_freeze.json');return p,parents,r
EXPECTED_COUNTS={'symbolic_axis_derivatives':2,'quotient_axis_derivatives':2,'all_axis_polynomial_coefficients':7,'two_packet_scale_identity':1,'rational_translated_cases':12,'normalization_identities':3,'inherited_gradient_coefficients':210,'fresh_aggregate_energy_terms':405,'fresh_unaggregated_energy_pairs':22050,'integrability_identities':5,'bracket_order_inequalities':2,'parent_guard_cases':15,'parent_guard_rejections':10}
def complete():
 p,parents,r=base();v=load(E/'checks.json')
 need(v['status']=='PASS_SOURCE_GRAPH_NONLINEARITY_FINITE_CHECKS_REQUIRES_ACTUAL_REVIEW','completed finite checks')
 need(v['counts']==EXPECTED_COUNTS,'complete finite counters')
 need(v['parents']==parents and v['proof_review']==r and v['files']==dict(sorted(p.items())),'same complete inputs')
 need(when(load(E/'source_freeze.json')['utc'])<when(v['start_utc'])<when(v['utc'])<datetime.now(timezone.utc),'complete execution chronology')
 pin(p,E/'checks.json');return p,v
