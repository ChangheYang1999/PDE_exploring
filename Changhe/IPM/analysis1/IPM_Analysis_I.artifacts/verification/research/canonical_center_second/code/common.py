"""Evidence and exact input gates for the independent center calculation."""
import os,sys
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,re
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_center_second';E=D/'evidence';R=B/'notes/reviews'
CELLS=[0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808]
COUNTS={'spans_I':1558,'spans_J':1558,'full_steps_I':406638,'full_steps_J':406638,'center_steps_I':3393,'center_steps_J':3393,'I_targets':3393,'J_targets':3393,'H_coefficients':27248,'exact_anchors':783}
SOURCE='data_exact/modal_v2.json';ZPATH='research/modal_repair/evidence/independent_gauss_iv.json';PARTITION='research/middle_residual/evidence/partition_exact.json';TARGET='research/residual_samples/evidence/sample_result.json';ENGINE='research/canonical_archive_second/code/engine.py';NEWTON='research/full_t_linkage/code/audit_coefficients.py';GREEN=B.parent/'ipmA-num/data/cert_green.npz'
FIXED_INPUTS={SOURCE:'57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6',ZPATH:'0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a',PARTITION:'56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2',TARGET:'0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c',ENGINE:'d6658c20197f2b5101bce5ffcd8aa8b0ab6c4a7cddf7ff9cc0c97700b45d80db',str(GREEN):'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1','research/residual_samples/code/certify_samples.py':'d393d06a70d8209f3eca0bbb67ca309d45153ff9ca23abd4a54a961076c92257','research/exponential_moments/code/moments.py':'6f9aa03d5f7f4f2dff22e5bc8319a861148313e96d89991c16ee979dfdf0489c','research/canonical_inverse/code/exact_audit.py':'331771590a0dd764208306640b4b3af63aec8cfe966ed6a0d086ec512d617b42','research/ball_transport/code/dyadic_ball.py':'6525060f436bf553f3b4a42e403ad2c27dc69d6a82a1460634995f95e755e3c3','research/residual_point_jets/evidence/preparation.json':'fff85c58b1856076c831413ea47dc72d42421c271ffd94f73ecba7ff0725d483'}
DEPS={'canonical_archive_second':('5e5a0879c90afca49df5586e8c602c3b8a990dbea61a5280918646fddb68e75f','CONFIRMED_COMPLETE_CANONICAL_MOMENT_ARCHIVE'),'full_t_linkage':('3732110a42745c75a1f10cf1e057d0d0d6b81a087bb74e3d9289ef0b0e33635b','CONFIRMED_COMPLETE_FINITE_SPLINE_T_AND_H_MEMBERSHIP'),'residual_point_jets':('9eb7bccad5217941ad1f0227d74829511620b6373cc2ecc1eb517aa067d2c531','CONFIRMED_FINITE_POINT_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED'),'residual_cell_cauchy':('c5ac5d88fde1a9e92925c45af26bdac920841a0378830027d4a9535565c1a04c','CONFIRMED_THREE_CELL_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED'),'residual_cell_bernstein':('cefa9a0e504ff3fb7ad3aa3e60aab57780745a5dcd8f030bcbc2d2d5f903c0d1','CONFIRMED_THREE_CELL_BERNSTEIN_ENCLOSURES_CANONICAL_INPUTS_INHERITED')}
PREFIX='You are Claude Opus 5.5 collaborating with GPT-6, reviewing a mathematical computer-assisted IPM proof. Restrictions on this delegated task: no JavaScript/TypeScript development or execution; no servers/listeners/tunnels; no RLScience cluster; no Lean/Lake builds; no outside writes; no people contact. Pure text review only. Return a concise substantive FINAL ANSWER, not just internal reasoning. Reconstruct claims and reject gaps. '
OWN=['PROOF.md','PROOF_ADJUDICATION.md','data_exact/proof_first.json','data_exact/proof_adjudication.json','code/common.py','code/full.py','code/audit.py','code/preparation.py','code/launch_review.py','code/freeze.py','code/extract.py','code/finalize.py','code/queue.sh','data_exact/review_files.json','data_exact/preparation_question.txt','data_exact/actual_question.txt']
def need(v,s):
 if not v:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def when(t):
 d=datetime.fromisoformat(t);need(d.tzinfo is not None,'timezone');return d

def chronology(*ts):
 v=list(map(when,ts));need(all(a<b for a,b in zip(v,v[1:])) and v[-1]<=datetime.now(timezone.utc),'strict actual chronology')
def unique(pairs):
 d={}
 for k,v in pairs:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def parse(s):return json.loads(s,object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def load(p):return parse(Path(p).read_text())
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,v):
 p=Path(p);need(p.resolve().is_relative_to(D),'write restricted to174 directory')
 with p.open('x') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()+b'\n'
cache={}
def pin(pins,n,h=None):
 p=(B/Path(n)).resolve();need(p.is_relative_to(B) or p.is_relative_to(B.parent/'ipmA-num'),'allowed read dependency');key=str(p.relative_to(B)) if p.is_relative_to(B) else str(p)
 if key not in cache:cache[key]=sha(p)
 current=cache[key];need(h is None or h==current,'fixed input hash '+key);need(key not in pins or pins[key]==current,'same input path digest');pins[key]=current;return current
def merge(p,v):
 for n,h in v['files'].items():pin(p,n,h)
def rehash(p):
 for n,h in p.items():need(sha(B/n)==h,'current unchanged dependency '+n)
def auth(p,tag,verdict,required,question=None):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();req=(R/(tag+'_request.txt')).read_text()
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and 'availability_error' not in m,'actual complete Opus5.5 review');need(m['files']==required and len(required)==len(set(required)),'fixed exact review bundle')
 need(text=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n' and re.findall(r'(?m)^VERDICT:\s*(\w+)\s*$',text)==[verdict] and text.rstrip().splitlines()[-1]=='VERDICT: '+verdict,'actual response text and scoped verdict')
 prefix=req.split('\n\nFILE ',1)[0];need(prefix.startswith(PREFIX),'complete restriction prefix')
 if question is not None:need(prefix==PREFIX+(D/'data_exact'/question).read_text(),'exact fixed review question')
 need(req==prefix+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in required) and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'current complete request bytes');need(when(m['start_utc'])<when(m['end_utc'])<=datetime.now(timezone.utc),'actual review times')
 for n in required:pin(p,n)
 for suffix in ['metadata.json','request.txt','response.json','response.md']:pin(p,R/(tag+'_'+suffix))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
def post(p,tag,review,stem):
 v=load(E/(stem+'.json'));a=D/(stem+'.md');body=a.read_text();m=load(R/(tag+'_metadata.json'))
 need(v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==review['request_id'] and v['input_sha256']==review['input_sha256'] and v['response_sha256']==sha(R/(tag+'_response.json')) and v['adjudication_sha256']==sha(a) and v['all_substantive_objections_resolved'] is True,'separately later actual response-bound adjudication');need(review['request_id'] in body and v['response_sha256'] in body,'written response identity');chronology(review['end_utc'],v['utc']);need(str(a.relative_to(B)) not in m['files'] and str((E/(stem+'.json')).relative_to(B)) not in m['files'],'later disposition outside original bundle');pin(p,a);pin(p,E/(stem+'.json'));return v

def base():
 p={};deps={}
 for n,(h,status) in DEPS.items():
  path=B/'research'/n/'evidence/verdict.json';v=load(path);pin(p,path,h);need(v['status']==status,'accepted dependency '+n);merge(p,v);deps[n]=v
 for n,h in FIXED_INPUTS.items():pin(p,n,h)
 for n in ['residual_point_jets','residual_cell_cauchy','residual_cell_bernstein']:need(deps[n]['files'][TARGET]==FIXED_INPUTS[TARGET],'identical inherited center targets')
 need(deps['full_t_linkage']['files'][PARTITION]==FIXED_INPUTS[PARTITION] and deps['full_t_linkage']['files'][str(GREEN)]==FIXED_INPUTS[str(GREEN)],'accepted partition and cert_green identity')
 poly=load(B/'research/residual_point_jets/evidence/preparation.json');need(poly['status']=='PASS_EXACT_INTERIOR_DENSITY_POLYNOMIALS_AND_ORDER_FIVE_ALGEBRA' and poly['exact_density_coefficients']==27248 and [v['cell'] for v in poly['points']]==CELLS,'complete accepted143 density binding');merge(p,poly)
 need(deps['residual_point_jets']['counts']['points']==13 and deps['residual_point_jets']['counts']['exact_Wiener_checks']==273 and deps['residual_cell_cauchy']['counts']['cell_derivative_bounds']==63 and deps['residual_cell_bernstein']['counts']['cell_derivative_bounds']==63 and deps['residual_cell_cauchy']['comparison_counts']=={'INDEPENDENT_UPPER_TOO_LARGE_TO_VALIDATE_SAVED_CAP':63} and deps['residual_cell_bernstein']['comparison_counts']=={'VALIDATES_SAVED_CAP_ON_SELECTED_CELL':63},'unchanged precise descendant scope and comparisons')
 pf=load(D/'data_exact/proof_first.json');need(pf['sha256']==sha(D/'PROOF.md') and pf['new_code_written'] is False,'unchanged proof first');m=load(R/'canonical_center_second_proof_metadata.json');pr=auth(p,'canonical_center_second_proof','CONFIRM_CENTER_INTEGRATION_PROOF_PREPARATION_ONLY',m['files']);need(pr['request_id']=='71aff874-43bf-4eb7-89e0-010a4c059b07' and pr['input_sha256']=='9b1cd30a8b2bb0e1ad5f9c9bd224ac8c7aa50a9695884e622ace9ee3c5a8db99','fixed actual proof review')
 pa=load(D/'data_exact/proof_adjudication.json');need(pa['status']=='CONFIRMED_PROOF_PROTOCOL_ONLY_AFTER_COMPLETE_ACTUAL_REVIEW' and pa['request_id']==pr['request_id'] and pa['input_sha256']==pr['input_sha256'] and pa['response_sha256']==sha(R/'canonical_center_second_proof_response.json') and pa['adjudication_sha256']==sha(D/'PROOF_ADJUDICATION.md') and pa['all_substantive_objections_resolved'] is True and pa['new_code_written'] is False,'independent proof disposition');birth=load(D/'data_exact/code_birth.json');need(birth['files']=={str((D/n).relative_to(B)):sha(D/n) for n in OWN},'unchanged reviewed source birth');chronology(pf['utc'],pr['start_utc'],pr['end_utc'],pa['utc'],birth['utc']);merge(p,birth);pin(p,D/'data_exact/code_birth.json');pin(p,NEWTON);pin(p,R/'focused_review.py');return p,deps

def coordinates():
 raw=load(B/SOURCE);knots=sorted(set(Q.from_float(float.fromhex(x)) for x in raw['arrays']['knots']['hex']));part=load(B/PARTITION);samples=load(B/TARGET);need(part['input_sha256']==samples['input_sha256']==FIXED_INPUTS[SOURCE] and part['grid_sha256']==samples['green_comparison_sha256']==FIXED_INPUTS[str(GREEN)] and samples['scalar_input_sha256']==FIXED_INPUTS[ZPATH],'same source normalizer and partition construction')
 need(samples['bits']==320 and samples['stream_modes']==261 and samples['integration_cells']==1571 and samples['source_sha256']==FIXED_INPUTS['research/residual_samples/code/certify_samples.py'],'unchanged primary method');need(len(knots)==1559 and len(part['spans'])==1558 and part['cells']==7809 and [p['cell'] for p in samples['samples']]==CELLS,'complete grid/center list')
 owners={};first=0
 for si,p in enumerate(part['spans']):
  a,b=knots[si:si+2];count=p['count'];need(type(count) is int and count>0 and p=={'span':si,'first_cell':first,'count':count,'a_exact':str(a),'b_exact':str(b)},'complete original partition identity')
  for ci in CELLS:
   if first<=ci<first+count:
    l=a+(b-a)*Q(ci-first,count);r=l+(b-a)/count;owners[ci]=(si,l,r,(l+r)/2)
  first+=count
 need(first==7809 and len(owners)==13,'all exact cell ownership');out=[]
 for s in samples['samples']:
  ci=s['cell'];si,l,r,tc=owners[ci];a,b=knots[si:si+2];need(list(map(Q,s['cell_endpoints_exact']))==[l,r] and Q(s['t_exact'])==tc and a<=l<tc<r<=b,'closed cell, strictly interior exact midpoint');need(len(s['i'])==len(s['j'])==261 and len(s['density_polynomial_at_point'])==262 and all(len(x)==8 for x in s['density_polynomial_at_point']),'all target shapes');out.append({'cell':ci,'span':si,'t_exact':str(tc),'cell_endpoints_exact':list(map(str,[l,r])),'a_exact':str(a),'b_exact':str(b),'xi_exact':str((tc-a)/(b-a))})
 return out,{s['cell']:s for s in samples['samples']}

def readiness(p):
 v=load(E/'preparation_checks.json');x=load(E/'preparation_extract.json');need(v['status']=='PASS_CENTER_PREPARATION_AND_SHORT_DIAGNOSTICS_ONLY' and v['full_result_exists'] is False and v['failures']==[] and all(c['pass'] for c in v['cases']) and v['case_count']==len(v['cases']) and v['future_full_counts_required']==COUNTS,'completed preparation diagnostics');need({k:a for k,a in x.items() if k!='utc'}=={'status':'EXACT_CENTER_PREPARATION_PROJECTION_ONLY','preparation_sha256':sha(E/'preparation_checks.json'),'preparation':{k:a for k,a in v.items() if k!='files'}},'exact preparation projection');merge(p,v);pin(p,E/'preparation_checks.json');pin(p,E/'preparation_extract.json');chronology(load(D/'data_exact/code_birth.json')['utc'],v['actual_smoke']['start_utc'],v['actual_smoke']['utc'],v['actual_smoke_audit']['start_utc'],v['actual_smoke_audit']['utc'],v['utc'],x['utc']);return v,x

def preflight():
 p,deps=base();ready,x=readiness(p);v=load(E/'preflight_manifest.json');need(v['status']=='ACCEPTED_CENTER_INTEGRATION_PREPARATION_ONLY' and v['full_result_exists'] is False,'accepted preparation only');merge(p,v);pin(p,E/'preflight_manifest.json');pr=auth(p,'canonical_center_second_preparation','CONFIRM_CENTER_INTEGRATION_PREPARATION_ONLY',mandatory(False),'preparation_question.txt');po=post(p,'canonical_center_second_preparation',pr,'PREFLIGHT_ADJUDICATION');need(pr==v['actual_review'] and po==v['postreview'],'same accepted preparation review/disposition');need(v['preparation_sha256']==sha(E/'preparation_checks.json') and v['extract_sha256']==sha(E/'preparation_extract.json'),'same accepted readiness');chronology(x['utc'],pr['start_utc'],pr['end_utc'],po['utc'],v['utc']);rehash(p);return p,deps,v

def mandatory(actual):
 own=[str((D/n).relative_to(B)) for n in OWN]+[str((D/'data_exact/code_birth.json').relative_to(B)),str((E/'preparation_extract.json').relative_to(B))]
 parents=[ENGINE,NEWTON,'research/canonical_archive_second/PROOF.md','research/canonical_archive_second/ADDENDUM.md','research/canonical_archive_second/AUDIT_METHOD.md','research/canonical_archive_second/POSTREVIEW_ADJUDICATION.md','research/residual_samples/PROOF.md','research/residual_samples/code/certify_samples.py','research/exponential_moments/code/moments.py','notes/reviews/canonical_center_second_proof_response.md']
 for n in ['residual_point_jets','residual_cell_cauchy','residual_cell_bernstein']:
  parents+=['research/'+n+'/'+s for s in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md']]
 parents+=['research/residual_point_jets/POSTREVIEW.md','research/residual_cell_bernstein/POSTREVIEW_ADJUDICATION.md']
 if actual:own +=[str((E/n).relative_to(B)) for n in ['review_extract.json','preflight_manifest.json','PREFLIGHT_ADJUDICATION.json']]+[str((D/'PREFLIGHT_ADJUDICATION.md').relative_to(B))];parents+=['notes/reviews/canonical_center_second_preparation_response.md']
 return own+parents

def output_fields(s,a,q):
 need(s['status']=='COMPUTED_COMPLETE_CENTERS_REQUIRES_INDEPENDENT_AUDIT' and s['full_run'] is True and s['counts']==COUNTS and s['center_cells']=={'I':CELLS,'J':list(reversed(CELLS))} and s['iv_dps']==200 and s['anchor_checks']==3915,'actual complete center producer')
 need(a['status']=='PASS_COMPLETE_CENTER_SAVED_PAIR_NEWTON_DENSITY_AND_ANCHOR_AUDIT' and a['full_run'] is True and a['counts']==COUNTS and a['all_saved_moment_pairs']==6786 and a['independent_exact_density_coefficients']==27248 and a['independent_exact_anchors']==783 and a['center_cells']==s['center_cells'],'actual exhaustive center audit')
 need(q['status']=='COMPLETE_CENTER_COMPUTATION_AND_AUDIT_REQUIRES_REVIEW','actual completed center queue')
 need(a['output_sha256']==s['output_sha256'] and a['worst_relative_margins']==s['worst_relative_margins'] and Q(a['minimum_nonzero_abs_zeta_exact'])==Q(s['minimum_nonzero_abs_zeta_exact'])>0,'actual shared complete center output')

def collect():
 s=load(E/'full_summary.json');p,deps,prep=preflight();a=load(E/'full_output_audit.json');q=load(E/'queue_status.json');output_fields(s,a,q)
 need(s['output_sha256']==a['output_sha256']==sha(E/'full_centers.jsonl.gz') and a['summary_sha256']==q['summary_sha256']==sha(E/'full_summary.json') and q['audit_sha256']==sha(E/'full_output_audit.json'),'actual complete file cross-hashes');need(s['producer_sha256']==sha(D/'code/full.py') and s['engine_sha256']==sha(B/ENGINE) and a['auditor_sha256']==sha(D/'code/audit.py') and a['Newton_source_sha256']==sha(B/NEWTON),'executed unchanged producer and independent auditor');need(s['code_birth_sha256']==a['code_birth_sha256']==sha(D/'data_exact/code_birth.json') and s['preflight_sha256']==a['preflight_sha256']==sha(E/'preflight_manifest.json'),'executed frozen sources and accepted preparation')
 for key,n in [('source_sha256',SOURCE),('target_sha256',TARGET),('normalization_sha256',ZPATH),('partition_sha256',PARTITION)]:need(s[key]==FIXED_INPUTS[n],'complete defining source '+key)
 chronology(prep['utc'],s['start_utc'],s['utc'],a['start_utc'],a['utc'],q['utc'])
 for n in ['full_summary.json','full_output_audit.json','full_centers.jsonl.gz','queue_status.json']:pin(p,E/n)
 return p,deps,prep,s,a,q

def projection(deps,prep,s,a,q):
 return {'status':'ACTUAL_COMPLETE_CENTER_REVIEW_EXTRACT_NOT_FINAL','producer':s,'auditor':a,'queue':q,'preflight_sha256':sha(E/'preflight_manifest.json'),'preflight':{k:v for k,v in prep.items() if k!='files'},'dependencies':{n:{'path':'research/'+n+'/evidence/verdict.json','sha256':DEPS[n][0],'utc':v['utc'],'status':v['status'],'counts':v.get('counts'),'comparison_counts':v.get('comparison_counts'),'scope':v['scope']} for n,v in deps.items()},'scope':'Current complete producer/auditor/queue after all transitive inputs rehashed. Explicit application only to center membership in143/144/145, preserving their numerical values and all other hypotheses.'}
