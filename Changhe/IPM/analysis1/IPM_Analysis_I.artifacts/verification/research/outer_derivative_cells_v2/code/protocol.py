"""Fixed sources, authenticated parent content and actual-review gates."""
import sys,os,json,hashlib,importlib.util,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
sys.dont_write_bytecode=True
assert not sys.flags.optimize
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
ROOT=Path(__file__).resolve().parents[3];DIR=ROOT/'research/outer_derivative_cells_v2';OUT=DIR/'evidence';REV=ROOT/'notes/reviews'
UP=ROOT/'research/full_derivative_norm_bound_v2/code/protocol.py'
assert hashlib.sha256(UP.read_bytes()).hexdigest()=='b57406959b9857d3acf994d7c1067fe4f534fa3b2362d2ddc3ed785be2cdcdcf'
sp=importlib.util.spec_from_file_location('review180_parent_util',UP);u=importlib.util.module_from_spec(sp);sp.loader.exec_module(u)
load,sha,write,pin,rehash,auth,when,now,parse=u.load,u.sha,u.write,u.pin,u.rehash,u.auth,u.when,u.now,u.parse
PREP=ROOT/'research/full_derivative_norm_bound_v2/evidence/preparation_acceptance.json'
PREPSHA='e6802cf6c6be05de8583241e803b2f2a6e15d46df7a1f6432c37884c900cbb02'
MANIFEST=ROOT/'research/outer_cells/evidence/full_q16_manifest.json'
TAILS=ROOT/'research/derivative_end_tails/evidence/checks.json'
SMOKE=[0,39,88];REPLAY=[0,39,88]
OWN=['SOURCE_LINEAGE.md','evidence/v2_birth.json','PROOF.md','PROOF_ADJUDICATION.md','EXACT_ENDPOINT_COMPARISONS.md','EXECUTION_PROTOCOL.md','ENGINE_ADJUDICATION.md','evidence/proof_first.json','evidence/proof_adjudication.json','evidence/ENGINE_ADJUDICATION.json','evidence/endpoint_optimization_checks.json','evidence/angular_map_checks.json','evidence/workflow_selfcheck.json','code/engine_arb.py','code/engine_iv.py','code/protocol.py','code/run.py','code/audit.py','code/replay.py','code/gate.py','code/queue.sh','review_files.json','preparation_question.txt','actual_question.txt']

def parents():
 assert sha(PREP)==PREPSHA
 p=load(PREP);assert p['status']=='CONFIRMED_FULL_DERIVATIVE_NORM_PREPARATION_ONLY';pins=dict(p['files']);rehash(pins);pin(pins,PREP,PREPSHA)
 for n,status in [('research/outer_cells/evidence/verdict.json','CONFIRMED'),('research/canonical_residual_composition/evidence/verdict.json','CONFIRMED_CANONICAL_RESIDUAL_ARCHIVE_PREMISE_DISCHARGED'),('research/derivative_end_tails/evidence/verdict.json','CONFIRMED_CANONICAL_DERIVATIVE_END_TAILS_CONDITIONAL_FULL_PLANE_COMPOSITION')]:
  assert n in pins and load(ROOT/n)['status']==status
 assert str(MANIFEST.relative_to(ROOT)) in pins and str(TAILS.relative_to(ROOT)) in pins
 return pins,{'accepted_content_parent_sha256':PREPSHA,'historical_source_rebindings':p['parents']['tails']['explicit_content_rebindings'],'scope':'Only43/171/178 exterior mathematics reused;179 full result is not a prerequisite.'}

def cells():
 z=load(MANIFEST);assert z['Q']==16 and len(z['cells'])==89
 cs=[(F(a),F(b)) for a,b in z['cells']];assert cs[0][0]==0 and cs[-1][1]==17
 for j,(a,b) in enumerate(cs):assert a<b and (j==0 or cs[j-1][1]==a)
 return cs

def post(pins,tag,review,stem):
 v=load(OUT/(stem+'.json'));a=DIR/(stem+'.md');rh=sha(REV/(tag+'_response.json'))
 assert v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==review['request_id'] and v['input_sha256']==review['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(a) and v['all_substantive_objections_resolved'] is True
 assert when(review['end_utc'])<when(v['utc'])<datetime.now(timezone.utc)
 assert review['request_id'] in a.read_text() and rh in a.read_text()
 assert str(a.relative_to(ROOT)) not in load(REV/(tag+'_metadata.json'))['files']
 pin(pins,a);pin(pins,OUT/(stem+'.json'));return v

def source():
 for n in ['code/engine_arb.py','code/engine_iv.py']:assert sha(DIR/n)==sha(ROOT/'research/outer_derivative_cells'/n)
 p,deps=parents();f=load(OUT/'source_freeze.json');assert f['files']==dict(sorted({str((DIR/n).relative_to(ROOT)):sha(DIR/n) for n in OWN}.items()))
 assert load(OUT/'proof_first.json')['sha256']==sha(DIR/'PROOF.md')
 m=load(OUT/'parent_manifest.json');assert m['files']==dict(sorted(p.items())) and m['parents']==deps
 r=auth(p,'outer_derivative_cells_engines','CONFIRM_OUTER_DERIVATIVE_CELL_ENGINES_ONLY');post(p,'outer_derivative_cells_engines',r,'ENGINE_ADJUDICATION')
 for n,h in f['files'].items():pin(p,n,h)
 pin(p,OUT/'source_freeze.json');pin(p,OUT/'parent_manifest.json');return p,deps

def interval(v):
 assert set(['lower_exact','upper_exact'])<=set(v)
 lo,hi=F(v['lower_exact']),F(v['upper_exact']);assert 0<=lo<=hi;return lo,hi

def tail_squares():
 t=load(TAILS);assert t['status']=='PASS_CANONICAL_DERIVATIVE_END_TAILS_REQUIRES_ACTUAL_REVIEW'
 vals=t['strict_decimal_ceilings']['tail_norms'];names=['outer_eps','outer_eps_minus_eps_t'];bounds=[]
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
 for name in ['arb','iv']:
  z=r[name];assert (F(z['left_exact']),F(z['right_exact']))==cs[idx] and z['Q']==16
  assert F(z['max_abs_lambda_h_exact'])==262*(cs[idx][1]-cs[idx][0])
  assert len(z['B'])==3 and len(z['C'])==2 and len(z['parts'])==3 and len(z['norm_squares'])==2
  for key in ['B','C','norm_squares']:
   for v in z[key]:interval(v)
  for part in z['parts']:interval(part['error'])
 assert r['iv']['coefficient_overlap_checks']==17226 and r['iv']['derivative_input_checks']==445005 and r['iv']['exact_integer_convolutions']==8 and r['iv']['exact_Green_scalar_checks']==17748
 assert len(r['iv']['integer_coefficient_sha256'])==len(r['iv']['derivative_input_sha256'])==64
 assert r['arb']['input_precision_bits']==384 and r['arb']['evaluation_precision_bits']==512 and r['iv']['input_precision_digits']==200
