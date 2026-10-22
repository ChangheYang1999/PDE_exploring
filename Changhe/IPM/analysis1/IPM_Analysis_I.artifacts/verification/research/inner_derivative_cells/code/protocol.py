"""Inner derivative sources, canonical parent content and actual-review gates."""
import sys,os,json,hashlib,importlib.util
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
sys.dont_write_bytecode=True
assert not sys.flags.optimize
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
ROOT=Path(__file__).resolve().parents[3];DIR=ROOT/'research/inner_derivative_cells';OUT=DIR/'evidence';REV=ROOT/'notes/reviews'
UP=ROOT/'research/full_derivative_norm_bound_v2/code/protocol.py'
assert hashlib.sha256(UP.read_bytes()).hexdigest()=='b57406959b9857d3acf994d7c1067fe4f534fa3b2362d2ddc3ed785be2cdcdcf'
sp=importlib.util.spec_from_file_location('review181_parent_util',UP);u=importlib.util.module_from_spec(sp);sp.loader.exec_module(u)
load,sha,write,pin,rehash,auth,when,now,parse=u.load,u.sha,u.write,u.pin,u.rehash,u.auth,u.when,u.now,u.parse
PREP=ROOT/'research/full_derivative_norm_bound_v2/evidence/preparation_acceptance.json'
PREPSHA='e6802cf6c6be05de8583241e803b2f2a6e15d46df7a1f6432c37884c900cbb02'
MANIFEST=ROOT/'research/inner_cells/evidence/full_q16_manifest.json'
COEFFICIENTS=ROOT/'research/inner_majorant/evidence/exact_inner_coefficients.json'
TAILS=ROOT/'research/derivative_end_tails/evidence/checks.json'
SMOKE=[0,15,43];REPLAY=[0,15,43]
ENGINE_HASHES={'engine_arb.py':'1c81c3a7e0bb82f3c4a675030d2de202ea46d6b0fddd4ea59b39fda4a4cb8c0a','engine_iv.py':'78233c2fc3d6b2b995b6d407a205978ff1300bb3bbce0d94447a8993d5729832'}
OWN=['PROOF.md','PROOF_ADJUDICATION.md','ENGINE_ADJUDICATION.md','WORKFLOW_ADJUDICATION.md','EXECUTION_PROTOCOL.md','SOURCE_LINEAGE.md','REVIEW_PRECISION_NOTE.md','REVIEW_PRECISION_RESOLUTION.md','evidence/proof_first.json','evidence/proof_adjudication.json','evidence/ENGINE_ADJUDICATION.json','evidence/WORKFLOW_ADJUDICATION.json','evidence/algebra_checks.json','evidence/linear_angular_checks_initial.json','evidence/linear_angular_checks.json','evidence/workflow_birth.json','evidence/workflow_selfcheck.json','code/algebra_checks.py','code/linear_angular_checks.py','code/engine_arb.py','code/engine_iv.py','code/protocol.py','code/run.py','code/audit.py','code/replay.py','code/gate.py','code/queue.sh','code/selfcheck.py','review_files.json','workflow_question.txt','preparation_question.txt','actual_question.txt']

def parents():
 assert sha(PREP)==PREPSHA
 p=load(PREP);assert p['status']=='CONFIRMED_FULL_DERIVATIVE_NORM_PREPARATION_ONLY';pins=dict(p['files']);rehash(pins);pin(pins,PREP,PREPSHA)
 for n,status in [('research/inner_cells/evidence/verdict.json','CONFIRMED'),('research/canonical_residual_composition/evidence/verdict.json','CONFIRMED_CANONICAL_RESIDUAL_ARCHIVE_PREMISE_DISCHARGED'),('research/derivative_end_tails/evidence/verdict.json','CONFIRMED_CANONICAL_DERIVATIVE_END_TAILS_CONDITIONAL_FULL_PLANE_COMPOSITION')]:
  assert n in pins and load(ROOT/n)['status']==status
 for path in [MANIFEST,COEFFICIENTS,TAILS]:assert str(path.relative_to(ROOT)) in pins
 return pins,{'accepted_content_parent_sha256':PREPSHA,'historical_source_rebindings':p['parents']['tails']['explicit_content_rebindings'],'scope':'Only45/171/178 inner mathematics reused;179/180 full results are not mathematical prerequisites.'}

def cells():
 z=load(MANIFEST);assert z['Q']==16 and len(z['cells'])==54
 cs=[(F(a),F(b)) for a,b in z['cells']][10:]
 expected=[(F(-5)+F(j,5),F(-5)+F(j+1,5)) for j in range(15)]+[(F(-2)+F(j,10),F(-2)+F(j+1,10)) for j in range(19)]+[(F(-1,10)+F(j,100),F(-1,10)+F(j+1,100)) for j in range(10)]
 assert cs==expected and len(cs)==44 and cs[0][0]==-5 and cs[-1][1]==0
 for j,(a,b) in enumerate(cs):assert a<b and (j==0 or cs[j-1][1]==a)
 assert [cs[i] for i in SMOKE]==[(F(-5),F(-24,5)),(F(-2),F(-19,10)),(F(-1,100),F(0))]
 return cs

def post(pins,tag,review,stem):
 v=load(OUT/(stem+'.json'));a=DIR/(stem+'.md');rh=sha(REV/(tag+'_response.json'))
 assert v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==review['request_id'] and v['input_sha256']==review['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(a) and v['all_substantive_objections_resolved'] is True
 assert when(review['end_utc'])<when(v['utc'])<datetime.now(timezone.utc)
 assert review['request_id'] in a.read_text() and rh in a.read_text()
 fs=load(REV/(tag+'_metadata.json'))['files'];assert str(a.relative_to(ROOT)) not in fs and str((OUT/(stem+'.json')).relative_to(ROOT)) not in fs
 pin(pins,a);pin(pins,OUT/(stem+'.json'));return v

def prior_reviews(p):
 tag='inner_derivative_cells_theorem_complete';r=auth(p,tag,'CONFIRM_INNER_DERIVATIVE_CELL_ANALYTIC_THEOREM_ONLY')
 q=load(OUT/'proof_adjudication.json');md=DIR/'PROOF_ADJUDICATION.md';rh=sha(REV/(tag+'_response.json'))
 assert q['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and q['request_id']==r['request_id'] and q['input_sha256']==r['input_sha256'] and q['response_sha256']==rh and q['adjudication_sha256']==sha(md) and q['proof_sha256']==sha(DIR/'PROOF.md') and q['all_substantive_objections_resolved'] is True
 assert when(r['end_utc'])<when(q['utc'])<datetime.now(timezone.utc)
 assert r['request_id'] in md.read_text() and rh in md.read_text() and str(md.relative_to(ROOT)) not in load(REV/(tag+'_metadata.json'))['files']
 pin(p,md);pin(p,OUT/'proof_adjudication.json')
 z=load(OUT/'ENGINE_ADJUDICATION.json');md=DIR/'ENGINE_ADJUDICATION.md'
 assert z['status']=='CONFIRMED_DRAFT_SOURCE_REVIEW_PENDING_EXECUTION' and z['actual_model']=='claude-opus-5-5' and z['source_sha256']==ENGINE_HASHES and z['adjudication_sha256']==sha(md) and z['all_source_review_objections_resolved'] is True and z['numerical_cells_executed']==0 and z['numerical_verdict']=='OPEN'
 tags=[('inner_derivative_cells_engines_draft','CONFIRM_DRAFT_INNER_DERIVATIVE_ENGINES_PENDING_EXECUTION'),('inner_derivative_cells_engines_precision','CONFIRM_ANGULAR_ENCODING_PRECISION_NOTE'),('inner_derivative_cells_engines_precision_resolved','CONFIRM_PRECISION_AND_EXTERNAL_ALGEBRA_EVIDENCE')]
 assert [v['tag'] for v in z['reviews']]==[t for t,v in tags]
 for (tag,verdict),rec in zip(tags,z['reviews']):
  r=auth(p,tag,verdict);rh=sha(REV/(tag+'_response.json'))
  for key in ['request_id','input_sha256','end_utc']:assert rec[key]==r[key]
  assert rec['response_sha256']==rh and r['request_id'] in md.read_text() and rh in md.read_text()
  assert when(r['end_utc'])<when(z['utc'])<datetime.now(timezone.utc)
  assert str(md.relative_to(ROOT)) not in load(REV/(tag+'_metadata.json'))['files']
 for n,h in ENGINE_HASHES.items():pin(p,DIR/'code'/n,h)
 pin(p,md);pin(p,OUT/'ENGINE_ADJUDICATION.json')


def source():
 p,deps=parents();prior_reviews(p)
 r=auth(p,'inner_derivative_cells_workflow','CONFIRM_INNER_DERIVATIVE_WORKFLOW_PENDING_EXECUTION',load(DIR/'review_files.json')['workflow'],(DIR/'workflow_question.txt').read_text());post(p,'inner_derivative_cells_workflow',r,'WORKFLOW_ADJUDICATION')
 f=load(OUT/'source_freeze.json');assert f['files']==dict(sorted({str((DIR/n).relative_to(ROOT)):sha(DIR/n) for n in OWN}.items()))
 assert load(OUT/'proof_first.json')['sha256']==sha(DIR/'PROOF.md')
 m=load(OUT/'parent_manifest.json');pp,dd=parents();assert m['files']==dict(sorted(pp.items())) and m['parents']==dd==deps
 for n,h in f['files'].items():pin(p,n,h)
 pin(p,OUT/'source_freeze.json');pin(p,OUT/'parent_manifest.json');return p,deps

def interval(v):
 assert set(['lower_exact','upper_exact'])<=set(v)
 lo,hi=F(v['lower_exact']),F(v['upper_exact']);assert 0<=lo<=hi;return lo,hi

def tail_squares():
 t=load(TAILS);assert t['status']=='PASS_CANONICAL_DERIVATIVE_END_TAILS_REQUIRES_ACTUAL_REVIEW'
 vals=t['strict_decimal_ceilings']['tail_norms'];names=['inner_eps','inner_eps_minus_eps_t'];bounds=[]
 assert [vals[n] for n in names]==['0.000002273735','0.000035059554']
 for n in names:
  q=F(vals[n]);assert q>0
  for engine in ['arb512','iv200']:assert q>interval(t['enclosures'][engine]['tail_norms'][n])[1]
  bounds.append(q*q)
 return bounds

def root_bounds(sums):
 import engine_arb as a,engine_iv as b
 from flint import ctx
 from mpmath import iv
 ctx.prec=512;iv.dps=200
 aa=[a.out(a.aa(v).sqrt()) for v in sums];bb=[b.out(iv.sqrt(b.iq(v))) for v in sums];ceil=[]
 for v,x,y in zip(sums,aa,bb):
  assert max(interval(x)[0],interval(y)[0])<=min(interval(x)[1],interval(y)[1]);hi=max(interval(x)[1],interval(y)[1]);scale=10**12;n=hi.numerator*scale//hi.denominator+1;c=F(n,scale);assert c>hi and c*c>v
  ceil.append(str(n//scale)+'.'+str(n%scale).zfill(12))
 return {'arb512':aa,'iv200':bb,'strict_decimal_ceilings':ceil}

def check_record(r,idx,cs):
 assert r['type']=='cell' and r['cell']==idx
 for name,rate in [('arb',522),('iv',526)]:
  z=r[name];assert (F(z['left_exact']),F(z['right_exact']))==cs[idx] and z['Q']==16
  assert F(z['max_abs_lambda_h_exact'])==rate*(cs[idx][1]-cs[idx][0])/2
  assert len(z['B'])==3 and len(z['C'])==2 and len(z['parts'])==3 and len(z['norm_squares'])==2
  assert 'coefficients' not in z and 'input_coefficients' not in z
  for key in ['B','C','norm_squares']:
   for v in z[key]:interval(v)
  for part in z['parts']:interval(part['error'])
 counts=load(OUT/'workflow_selfcheck.json')['expected_checks_per_cell']
 for key in ['coefficient_overlap_checks','derivative_input_checks','exact_integer_convolutions','cross_method_input_jet_checks','moment_modes']:assert r['iv'][key]==counts[key]
 for key in ['integer_coefficient_sha256','derivative_input_sha256','cross_method_input_jet_sha256']:assert len(r['iv'][key])==64 and all(c in '0123456789abcdef' for c in r['iv'][key])
 assert r['arb']['input_precision_bits']==384 and r['arb']['evaluation_precision_bits']==512 and r['iv']['input_precision_digits']==200
