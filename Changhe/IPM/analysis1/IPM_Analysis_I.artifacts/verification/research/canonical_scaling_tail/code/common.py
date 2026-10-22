"""Concrete review and immutable-input gates for topic176. No source modules executed."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import sys
sys.dont_write_bytecode=True
import json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_scaling_tail';E=D/'evidence';R=B/'notes/reviews'
PTAG='canonical_scaling_tail_proof_v2';ATAG='canonical_scaling_tail_actual'
PSCOPE='CONFIRM_CANONICAL_TAIL_PROOF_ONLY';ASCOPE='CONFIRM_CANONICAL_SCALING_FIELD_EXTERIOR_NONMEMBERSHIP'
S='data_exact/modal_v2.json';SH='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
Z='research/modal_repair/evidence/independent_gauss_iv.json';ZH='0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a'
V='research/saved_vector_external_constraints/sources/c2gram2_M16_s16_p4_H1m_NJ1_rowsH1q_vec.npz';VH='4fd4ff818efd62aa03cb4392d8d56dcaf8f948188962fc1133c38c561099ba2e'
PARENTS={'156':('research/canonical_archive_second/evidence/verdict.json','5e5a0879c90afca49df5586e8c602c3b8a990dbea61a5280918646fddb68e75f','CONFIRMED_COMPLETE_CANONICAL_MOMENT_ARCHIVE'),'172':('research/scaling_tail_obstruction/evidence/verdict.json','ad2ad78915ee17d084fb55f2179fdfde21f425d7e3974120773b5a340f4bbfc6','CONFIRMED_EXPLICIT_STORED_TAIL_OBSTRUCTION')}
EXTERNAL={str(B.parent/'ipmA-num/data/trial_v2_h0.008.npz'):'a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'}
OWN=['PROOF.md','evidence/proof_first.json','PROOF_ADJUDICATION.md','evidence/PROOF_ADJUDICATION.json','code/common.py','code/check.py','code/extract.py','code/launch_actual.py','code/finalize.py','proof_files.json','proof_question.txt','actual_files.json','actual_question.txt','SOURCE_SCOPE.md']
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
def base():
 p={};parents={}
 for label,(n,h,status) in PARENTS.items():
  pin(p,n,h);v=load(B/n);need(v['status']==status and len(v['files'])==({'156':64,'172':31}[label]),'actual parent verdict');parents[label]={'path':n,'sha256':h,'utc':v['utc'],'status':status,'pins':len(v['files'])}
  for x,z in v['files'].items():pin(p,x,z)
 for n,h in [(S,SH),(Z,ZH),(V,VH)]:pin(p,n,h)
 a=load(B/'research/modal_repair/evidence/audit_verdict.json');need(a['verdict']=='CONFIRMED' and a['actual_second_model']=='claude-opus-5-5','accepted normalization definition')
 for n,h in a['source_and_evidence_sha256'].items():pin(p,n,h)
 proof=load(E/'proof_first.json');need(proof['sha256']==sha(D/'PROOF.md'),'immutable proof first');r=auth(p,PTAG,PSCOPE,load(D/'proof_files.json'),'proof_question.txt');po=post(p,PTAG,r,'PROOF_ADJUDICATION');fr=load(E/'source_freeze.json');expected={str((D/n).relative_to(B)):sha(D/n) for n in OWN}
 need(fr['files']==dict(sorted(expected.items())) and when(proof['utc'])<when(r['start_utc'])<when(r['end_utc'])<when(po['utc'])<when(fr['utc'])<datetime.now(timezone.utc),'proof, review, later own disposition and frozen implementation')
 for n,h in fr['files'].items():pin(p,n,h)
 pin(p,E/'source_freeze.json');return p,parents,r
EXPECTED_COUNTS={'manual_and_numpy_dyadics':523,'integer_metadata_identities':1,'full_Aout_hex_two_parsers':2600,'leading_source_identities':260,'literal_B_recipe':261,'exact_and_rounded_rates_each_two_methods':20,'rate_bound_comparisons':20,'determinant_endpoints_two_exact_methods':2,'directed_affine_enclosures':2,'piece_shift_cases_two_exact_methods':4,'rounding_manufactured_cases':8,'guard_cases':14,'guard_rejections':11}
def complete():
 p,parents,r=base();v=load(E/'checks.json');need(v['status']=='PASS_CANONICAL_SCALING_EXTERIOR_NONMEMBERSHIP_REQUIRES_ACTUAL_REVIEW' and v['counts']==EXPECTED_COUNTS,'complete exact checks')
 need(v['parents']==parents and v['proof_review']==r and v['files']==dict(sorted(p.items())),'same complete input records');need(when(load(E/'source_freeze.json')['utc'])<when(v['start_utc'])<when(v['utc'])<datetime.now(timezone.utc),'actual computation after source freeze');pin(p,E/'checks.json');return p,v
