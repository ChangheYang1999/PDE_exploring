"""Immutable parent and actual review bindings for topic178."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import sys
sys.dont_write_bytecode=True
import json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_end_tails';E=D/'evidence';R=B/'notes/reviews'
PTAG='derivative_end_tails_proof_v2';ATAG='derivative_end_tails_actual'
PSCOPE='CONFIRM_DERIVATIVE_END_TAIL_PROOF_ONLY';ASCOPE='CONFIRM_CANONICAL_DERIVATIVE_END_TAILS_AND_CONDITIONAL_COMPOSITION'
SH='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
PARENTS={'inner': ('research/inner_majorant/evidence/verdict.json', '69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc', 'CONFIRMED', 7), 'outer': ('research/outer_majorant/evidence/verdict.json', '7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac', 'CONFIRMED', 29), '171': ('research/canonical_residual_composition/evidence/verdict.json', '902700a07aa5078bcdeb4082a6d217d42382c9b88a60632e5040dfb387328222', 'CONFIRMED_CANONICAL_RESIDUAL_ARCHIVE_PREMISE_DISCHARGED', 1022), '166': ('research/modal_annular_regularity/evidence/verdict.json', 'f830e308944bc1b37c488e190c7c417b513d2cf25497c0329bfb3bfdaa0f1b55', 'CONFIRMED_EXACT_MODAL_ANNULAR_REGULARITY', 227), '163': ('research/coherent_derivative_norm_composition/evidence/verdict.json', '45fc4988bd3234fa9654c587819151daac06afe98df1d98fb1b192730823f818', 'CONFIRMED_CONDITIONAL_COHERENT_ANNULUS_X_NORM_COMPOSITION', 195)}
EXTERNAL={'numerics/data/cert_green.npz': 'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1', 'numerics/data/cert_inner_green.npz': '4ba853bbad32a43894fe2f21a9f419b6ec23d7079b5a38a8b3a5b4702c20e8ee', 'numerics/data/cert_outer_green.npz': 'db1138f81d3dca243d2e3cd1ca07830740c89b32f526de5b75adf1d4329f2858', 'numerics/data/trial_v2_h0.008.npz': 'a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874', 'numerics/src/cert_green.py': '7f1c067b15d087b0688e3b4f1dc0b3abaf301a421b600ce96f5cedf662d6f8f0', 'numerics/src/cert_green_outer.py': 'aed9892b6b89720374c9ff4d6cbf5f455e2ea7c39572376675ea87a387d3b60e', 'numerics/src/cert_resid.py': '1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053', 'numerics/src/cert_resid_deriv.py': '38e45bcd4400d119fb0a887794c4866bcc1d61eed1c3d69f58616eb7c95d5ac8', 'numerics/src/midrad.py': '5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e', 'numerics/src/xnorm_cert.py': '4ea4f2717ccfa8c4b6ec5ee223ee39efae22b486138bbd558418e9c4d899f882'}
OWN=['PROOF.md', 'evidence/proof_first.json', 'PROOF_ADJUDICATION.md', 'evidence/PROOF_ADJUDICATION.json', 'code/common.py', 'code/check.py', 'code/extract.py', 'code/launch_actual.py', 'code/finalize.py', 'proof_files.json', 'proof_question.txt', 'actual_files.json', 'actual_question.txt', 'SOURCE_SCOPE.md']
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
 for label,(n,h,status,count) in PARENTS.items():
  pin(p,n,h);v=load(B/n);need(v['status']==status and len(v['files'])==count,'accepted entire parent');parents[label]={'path':n,'sha256':h,'utc':v['utc'],'status':status,'pins':count}
  for x,z in v['files'].items():pin(p,x,z)
 pin(p,'data_exact/modal_v2.json',SH)
 proof=load(E/'proof_first.json');need(proof['proof_sha256']==sha(D/'PROOF.md'),'immutable proof first');r=auth(p,PTAG,PSCOPE,load(D/'proof_files.json'),'proof_question.txt');po=post(p,PTAG,r,'PROOF_ADJUDICATION');fr=load(E/'source_freeze.json');expected={str((D/n).relative_to(B)):sha(D/n) for n in OWN}
 need(fr['files']==dict(sorted(expected.items())) and when(proof['utc'])<when(r['start_utc'])<when(r['end_utc'])<when(po['utc'])<when(fr['utc'])<datetime.now(timezone.utc),'proof, actual review, own disposition and frozen code')
 for n,h in fr['files'].items():pin(p,n,h)
 pin(p,E/'source_freeze.json');return p,parents,r
EXPECTED_COUNTS={'outer_constituent_intervals':346,'outer_product_blocks':2992,'outer_linear_blocks':10,'outer_exponents':1864,'outer_monomials':3508,'outer_lineage_exact_equalities':7016,'saved_interval_overlap_checks':3508,'inner_slots':3668,'inner_cubic_checks':262,'inner_derivative_exact_equalities':14672,'inner_monotonicity_checks':14672,'outer_derivative_exact_equalities':10524,'independent_weight_intersections':3508,'strict_decimal_ceiling_checks':12,'guard_cases':6,'guard_rejections':6}
def complete():
 from fractions import Fraction as F
 p,parents,r=base();v=load(E/'checks.json');counts=v['counts'];need({k:z for k,z in counts.items() if k!='maximum_coefficient_inflation_exact'}==EXPECTED_COUNTS and F(counts['maximum_coefficient_inflation_exact'])>=1,'complete executed coverage')
 need(v['status']=='PASS_CANONICAL_DERIVATIVE_END_TAILS_REQUIRES_ACTUAL_REVIEW','actual computation completed');pin(p,E/'coefficient_upper_bounds.json')
 need(v['parents']==parents and v['proof_review']==r and v['files']==dict(sorted(p.items())),'same full input and coefficient record');need(when(load(E/'source_freeze.json')['utc'])<when(v['start_utc'])<when(v['utc'])<datetime.now(timezone.utc),'actual computation after freeze');pin(p,E/'checks.json');return p,v
