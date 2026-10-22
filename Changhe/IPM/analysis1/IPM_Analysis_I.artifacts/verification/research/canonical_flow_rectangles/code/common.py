"""Immutable parent composition and exact review authentication for topic175."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,ast,struct,zipfile,math
from flint import fmpq,arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_flow_rectangles';E=D/'evidence';R=B/'notes/reviews'
DEPS={
 '73':('research/flow_angular/evidence/verdict.json','e6c80c31f03640391d892ccbcce36dee43039ec32383860014dd03c41d155547','CONFIRMED_FINITE_ANGULAR_RESULT'),
 '75':('research/flow_scalars/evidence/verdict.json','e33bea8fe8df2688b66963cfa5bb7562a849d16105726ad0238b4e5365edcf4b','CONFIRMED_FINITE_SCALAR_SCOPE_ONLY'),
 '93':('research/radial_tm_instance/evidence/verdict.json','5094d932431eb3abf2a0fedce225d3cd0e15b1ff499f7ef06471d2390710e6db','CONFIRMED_SELECTED_FINITE_INPUT_ODE_ENCLOSURES'),
 '125':('research/flow_composition/evidence/verdict.json','83020eb2da815fe56e0f2d5e5eeef8c93042978dd36dd4be3a5720b3c1ec6009','CONFIRMED_FINITE_SELECTED_FLOW_COMPOSITION'),
 '156':('research/canonical_archive_second/evidence/verdict.json','5e5a0879c90afca49df5586e8c602c3b8a990dbea61a5280918646fddb68e75f','CONFIRMED_COMPLETE_CANONICAL_MOMENT_ARCHIVE'),
 '157':('research/canonical_three_cell_linkage/evidence/verdict.json','094d96a64c1c15d31851de9b6426c94ff437d8de48f99e8229d4316282ef075f','CONFIRMED_THREE_SELECTED_CANONICAL_RADIAL_MODELS_CONDITIONAL_ON_ARCHIVE_MOMENTS'),
 '173':('research/canonical_boundary_composition/evidence/verdict.json','5e6bb7974b245fd4903f762951c1bb072221819fd84fe4e0f0ce7c8036e70f4a','CONFIRMED_CANONICAL_BOUNDARIES_AND_THREE_RADIAL_CELLS'),
 '125correction':('notes/completion_review/extension_6000/verdict.json','369421343dd42825bd546ab90934d9ae43f57465554db6b2c2dd9e1945a8d22d','CONFIRMED_COMMITTED_6000_PREFIX_AND_VERSIONED_PROSE_ERRATA')}
SOURCE='data_exact/modal_v2.json';SSHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';ZPATH='research/modal_repair/evidence/independent_gauss_iv.json';ZSHA='0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a';PART='research/middle_residual/evidence/partition_exact.json';PSHA='56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2'
K=F(1615536043799051,9007199254740992);CELLS=[0,4102,7808];NODES=[[0,1,7],[12800,12801,7],[25599,25600,7]];NAMES=['s','v2y','v1x','T0'];PTAG='canonical_flow_rectangles_proof';ATAG='canonical_flow_rectangles_actual'
PREFIX='You are Claude Opus 5.5 collaborating with GPT-6, reviewing a mathematical computer-assisted IPM proof. Restrictions on this delegated task: no JavaScript/TypeScript development or execution; no servers/listeners/tunnels; no RLScience cluster; no Lean/Lake builds; no outside writes; no people contact. Pure text review only. Return a concise substantive FINAL ANSWER, not just internal reasoning. Reconstruct claims and reject gaps. '
OWN=['PROOF.md','evidence/proof_first.json','PROOF_ADJUDICATION.md','evidence/PROOF_ADJUDICATION.json','proof_files.json','code/common.py','code/check.py','code/extract.py','code/launch_actual.py','code/finalize.py','actual_files.json','actual_question.txt','AUDIT_REPAIRS.md']
def need(v,s):
 if not v:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def when(s):return datetime.fromisoformat(s)
def unique(items):
 d={}
 for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def load(p):return json.loads(Path(p).read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,v):
 with Path(p).open('x') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
cache={}
def pin(pins,n,h=None):
 p=(B/n).resolve();key=str(p.relative_to(B)) if p.is_relative_to(B) else str(p)
 if key not in cache:cache[key]=sha(p)
 a=cache[key];need(h is None or a==h,'source hash '+key);need(key not in pins or pins[key]==a,'conflicting immutable source');pins[key]=a;return a
def merge(pins,v):
 for n,h in v['files'].items():pin(pins,n,h)
def rehash(pins):
 for n,h in pins.items():need(sha(B/n)==h,'final unchanged source '+n)
def qf(q):return F(int(q.numerator),int(q.denominator))
def ff(s):
 q=F(s);need(q==qf(fmpq(s)),'two exact rational parsers');return q
def auth(pins,tag,verdict,required,question=None):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();req=(R/(tag+'_request.txt')).read_text()
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and 'availability_error' not in m,'actual complete Opus5.5');need(m['files']==required and len(required)==len(set(required)),'fixed ordered review bundle')
 pre=req.split('\n\nFILE ',1)[0];need(all(x in pre for x in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds','no outside writes','no people contact']),'all delegated restrictions')
 if question is not None:need(pre==PREFIX+(D/question).read_text(),'fixed actual review question')
 need(req==pre+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in required) and sha(R/(tag+'_request.txt'))==m['input_sha256'],'actual complete request bytes');need(text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n','actual complete response bytes');need(re.findall(r'(?m)^VERDICT:\s*(\w+)\s*$',text)==[verdict] and text.rstrip().splitlines()[-1]=='VERDICT: '+verdict,'unique scoped final verdict');need(when(m['start_utc'])<=when(m['end_utc'])<=datetime.now(timezone.utc),'real review time')
 for n in required:pin(pins,n)
 for suf in ['metadata.json','request.txt','response.json','response.md']:pin(pins,R/(tag+'_'+suf))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
def post(pins,tag,r,stem):
 v=load(E/(stem+'.json'));a=D/(stem+'.md');rh=sha(R/(tag+'_response.json'));need(v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==r['request_id'] and v['input_sha256']==r['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(a) and v['all_substantive_objections_resolved'] is True,'actual separately later own disposition');need(r['request_id'] in a.read_text() and rh in a.read_text(),'own written actual response binding');need(when(r['end_utc'])<when(v['utc'])<=datetime.now(timezone.utc),'strict later own disposition');files=load(R/(tag+'_metadata.json'))['files'];need(str(a.relative_to(B)) not in files and str((E/(stem+'.json')).relative_to(B)) not in files,'own post outside its original bundle');pin(pins,a);pin(pins,E/(stem+'.json'));return v

def proof(pins):
 pf=load(E/'proof_first.json');need(pf['sha256']==sha(D/'PROOF.md'),'unchanged proof');r=auth(pins,PTAG,'CONFIRM_NINE_RECTANGLE_PROOF_ONLY',load(D/'proof_files.json'));need(r['request_id']=='75260b14-0520-4eec-a01b-f654470fafe3' and r['input_sha256']=='202ff68d28b17e642ba044b813cdb6f8ef4a7209a035bc0e738eafadf4e85e0c' and sha(R/(PTAG+'_response.json'))=='58ad88c47f5eb3e53d4046cd8c13c32ac20401424e4a3be560253b1f648dad17','fixed actually read proof review');p=post(pins,PTAG,r,'PROOF_ADJUDICATION');birth=load(E/'source_birth.json');need(birth['files']=={str((D/n).relative_to(B)):sha(D/n) for n in OWN},'all current sources match pre-computation birth');need(when(pf['utc'])<when(r['start_utc'])<when(r['end_utc'])<when(p['utc'])<when(birth['utc']),'proof review own disposition before code birth');merge(pins,birth);pin(pins,E/'source_birth.json');return r

def parents(pins):
 deps={}
 for tag,(n,h,status) in DEPS.items():pin(pins,n,h);v=load(B/n);need(v['status']==status,'fixed accepted parent status '+tag);merge(pins,v);deps[tag]=v
 x=deps['173'];need(x['source_sha256']==SSHA and x['normalization_sha256']==ZSHA and x['cells']==CELLS and x['modes']==261 and x['degree']==12,'actual173 exact normalized selected theorem')
 for tag in ['156','157']:need(x['accepted_dependencies'][tag]=={'path':DEPS[tag][0],'sha256':DEPS[tag][1],'utc':deps[tag]['utc']},'actual173 exact direct edge '+tag)
 edge=next(z for z in deps['157']['dependency_verdicts'] if z['topic']=='radial_tm_instance');need(edge['verdict_sha256']==DEPS['93'][1] and edge['utc']==deps['93']['utc'] and edge['status']==DEPS['93'][2],'actual157 direct93 edge')
 for tag in ['75','93','157','173']:need(deps[tag]['files'].get(PART)==PSHA or deps[tag]['files'].get(str(B/PART))==PSHA,'identical complete partition '+tag)
 for tag in ['156','157','173']:need(deps[tag]['files'][SOURCE]==SSHA and deps[tag]['files'][ZPATH]==ZSHA,'same exact canonical source and normalization '+tag)
 v=deps['125'];need(v['radial_cells']==CELLS and v['angular_nodes']==NODES and v['rectangles']==9 and v['source_ranges']==36 and v['reference_range_checks']==72 and v['modal_products_per_engine']==274833,'actual125 complete selected computation');need(deps['125correction']['125_comparisons']==72 and deps['125correction']['old_final_pin_counts']==[70,227,67],'actual accepted containment correction')
 for tag in ['73','75','93']:need(v['files'][DEPS[tag][0]]==DEPS[tag][1],'same125 finite premise '+tag)
 for n in ['research/flow_composition/ERRATUM_FINAL.md','notes/completion_review/extension_6000/FINAL_ADJUDICATION.md']:pin(pins,n)
 for n,h in [(SOURCE,SSHA),(ZPATH,ZSHA),(PART,PSHA)]:pin(pins,n,h)
 return deps

def required():
 own=OWN+['evidence/source_birth.json','evidence/review_extract.json']
 parents=['research/flow_composition/PROOF.md','research/flow_composition/ADDENDUM.md','research/flow_composition/FINAL_ADJUDICATION.md','research/flow_composition/ERRATUM_FINAL.md','notes/completion_review/extension_6000/FINAL_ADJUDICATION.md','research/flow_angular/PROOF.md','research/flow_scalars/PROOF.md','research/radial_tm_instance/PROOF.md','research/canonical_three_cell_linkage/PROOF.md','research/canonical_boundary_composition/PROOF.md','research/canonical_boundary_composition/REVIEW_RESOLUTION.md','research/canonical_boundary_composition/POSTREVIEW_ADJUDICATION.md','research/canonical_archive_second/PROOF.md','research/canonical_archive_second/ADDENDUM.md','research/canonical_archive_second/POSTREVIEW_ADJUDICATION.md','notes/reviews/canonical_flow_rectangles_proof_response.md']
 return [str((D/n).relative_to(B)) for n in own]+parents

def collect():
 p={};proof(p);deps=parents(p);v=load(E/'checks.json');merge(p,v);pin(p,E/'checks.json');need(v['status']=='PASS_NINE_CANONICAL_FLOW_RECTANGLES_REQUIRES_ACTUAL_REVIEW' and v['source_sha256']==SSHA and v['normalization_sha256']==ZSHA and v['partition_sha256']==PSHA,'actual completed selected check');need(v['accepted_dependencies']=={n:{'path':DEPS[n][0],'sha256':DEPS[n][1],'utc':d['utc'],'status':d['status']} for n,d in deps.items()},'exact actual dependency edges');need(v['counts']['saved_reference_containments_two_exact_methods']==72 and v['counts']['saved_margins_two_exact_methods']==144 and len(v['comparisons'])==72,'complete finite containment audit');targets=load(E/'targets_exact.json');need(v['targets_sha256']==sha(E/'targets_exact.json') and len(targets['rectangles'])==9 and sum(len(x['targets']) for x in targets['rectangles'])==36,'complete exact rectangle publication');need([(x['cell'],x['node']) for x in targets['rectangles']]==[(c,n) for c in CELLS for n in NODES],'exact nine rectangle order');need(load(D/'actual_files.json')==required(),'fixed actual complete review bundle');need(when(load(E/'source_birth.json')['utc'])<when(v['start_utc'])<when(v['utc']),'source birth before actual complete check');need(all(when(d['utc'])<when(v['start_utc']) for d in deps.values()),'all actual accepted dependencies before computation');rehash(p);return p,deps,v,targets

def projection(deps,v,targets):return {'checks_sha256':sha(E/'checks.json'),'targets_sha256':sha(E/'targets_exact.json'),'checks':{k:x for k,x in v.items() if k!='files'},'targets':targets,'parent_verdicts':{n:{k:x for k,x in d.items() if k!='files'} for n,d in deps.items()}}
