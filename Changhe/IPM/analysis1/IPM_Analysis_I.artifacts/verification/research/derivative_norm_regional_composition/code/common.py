"""Regional scalar composition, fixed sources and complete parent gates."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,hashlib,importlib.util
sys.dont_write_bytecode=True
assert not sys.flags.optimize
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/derivative_norm_regional_composition';E=D/'evidence';REV=ROOT/'notes/reviews'
UP=ROOT/'research/full_derivative_norm_bound_v2/code/protocol.py'
assert hashlib.sha256(UP.read_bytes()).hexdigest()=='b57406959b9857d3acf994d7c1067fe4f534fa3b2362d2ddc3ed785be2cdcdcf'
spec=importlib.util.spec_from_file_location('regional183_review_util',UP);u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
load,sha,write,pin,rehash,auth,when,now=u.load,u.sha,u.write,u.pin,u.rehash,u.auth,u.when,u.now
MODES=['coarse','exterior','both'];REGIONS=['inner','middle','outer'];ENGINES=['arb512','iv220']
PARENTS={
 '179':('full_derivative_norm_bound_v2','CONFIRMED_COMPLETE_CANONICAL_PHYSICAL_DERIVATIVE_NORM_BOUNDS','full_derivative_norm_v2_actual','CONFIRM_COMPLETE_CANONICAL_PHYSICAL_DERIVATIVE_NORM_BOUNDS'),
 '180':('outer_derivative_cells_v2','CONFIRMED_COMPLETE_CANONICAL_EXTERIOR_DERIVATIVE_NORM_BOUNDS','outer_derivative_cells_v2_actual','CONFIRM_COMPLETE_CANONICAL_EXTERIOR_DERIVATIVE_NORM_BOUNDS'),
 '181':('inner_derivative_cells_v2','CONFIRMED_COMPLETE_CANONICAL_INNER_DERIVATIVE_NORM_BOUNDS','inner_derivative_cells_v2_actual','CONFIRM_COMPLETE_CANONICAL_INNER_DERIVATIVE_NORM_BOUNDS')}
FIXED=['PROOF.md','evidence/constants.json','evidence/identity_expected.json','evidence/proof_first.json','code/common.py','code/extract.py','code/evaluate.py','code/replay.py','code/gate.py','code/selfcheck.py','evidence/selfcheck.json','review_files.json','workflow_question.txt','actual_question.txt']

def rational(s):
 assert type(s) is str
 return F(s)

def pair(v):
 a,b=rational(v['lower_exact']),rational(v['upper_exact']);assert 0<=a<=b;return a,b

def dyad(v):
 assert type(v) is list and len(v)==2
 m,e=v;assert type(m) is str and type(e) is int and len(m)<1000 and abs(e)<100000
 return F(int(m))*F(2)**e

def compact(v):
 a,b=dyad(v['lo']),dyad(v['hi']);assert 0<=a<=b;return a,b

def two(v):
 assert type(v) is list and len(v)==2
 out=list(map(rational,v));assert min(out)>=0;return out

def post(pins,tag,review,base):
 md=base.with_suffix('.md');jp=base.parent/(base.name+'.json');z=load(jp);rh=sha(REV/(tag+'_response.json'))
 assert z['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and z['request_id']==review['request_id'] and z['input_sha256']==review['input_sha256'] and z['response_sha256']==rh and z['adjudication_sha256']==sha(md) and z['all_substantive_objections_resolved'] is True
 assert when(review['end_utc'])<when(z['utc'])<datetime.now(timezone.utc)
 assert review['request_id'] in md.read_text() and rh in md.read_text()
 fs=load(REV/(tag+'_metadata.json'))['files'];assert str(md.relative_to(ROOT)) not in fs and str(jp.relative_to(ROOT)) not in fs
 pin(pins,md);pin(pins,jp);return z

def source():
 z=load(E/'source_freeze.json');expected={str((D/n).relative_to(ROOT)):sha(D/n) for n in FIXED}
 assert z['files']==dict(sorted(expected.items()));p=dict(z['files']);rehash(p);pin(p,E/'source_freeze.json');pin(p,UP)
 first=load(E/'proof_first.json');assert first['proof_sha256']==sha(D/'PROOF.md') and first['constants_sha256']==sha(E/'constants.json') and first['code_files']==[]
 sc=load(E/'selfcheck.json');assert sc['source_sha256']==sha(D/'code/selfcheck.py') and sc['status']=='PASS_REGIONAL_SCALAR_WORKFLOW_SELF_CHECKS'
 files=load(D/'review_files.json')['workflow'];assert {str((D/n).relative_to(ROOT)) for n in FIXED}<=set(files) and len(files)==len(set(files))
 rev=auth(p,'derivative_regional_workflow','CONFIRM_REGIONAL_COMPOSITION_SOURCE_PENDING_PARENT_FINALS',files,(D/'workflow_question.txt').read_text())
 ad=post(p,'derivative_regional_workflow',rev,D/'WORKFLOW_ADJUDICATION');assert when(ad['utc'])<when(z['utc'])
 return p

def parent(pins,label):
 folder,status,tag,expected=PARENTS[label];d=ROOT/'research'/folder;vp=d/'evidence/verdict.json';v=load(vp)
 assert v['status']==status,('parent is not FINAL',label)
 count={'179':7809,'180':89,'181':44}[label];assert v['cells']==count
 if label!='179':assert v['full_exterior' if label=='180' else 'full_inner'] is True
 rehash(v['files'])
 for n,h in v['files'].items():pin(pins,n,h)
 pin(pins,vp)
 fs=d/'evidence/source_freeze.json';expectedfreeze=load(E/'constants.json')['source_freezes'][label]
 assert v['files'].get(str(fs.relative_to(ROOT)))==expectedfreeze==sha(fs)
 raw=load(fs)
 for n,h in raw['files'].items():assert v['files'][n]==h
 files=load(d/'review_files.json')['actual'];rev=auth(pins,tag,expected,files,(d/'actual_question.txt').read_text())
 ad=v['own_postreview'];assert ad['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and ad['request_id']==rev['request_id'] and ad['input_sha256']==rev['input_sha256'] and ad['response_sha256']==sha(REV/(tag+'_response.json')) and ad['all_substantive_objections_resolved'] is True
 assert ad['adjudication_sha256']==sha(d/'POSTREVIEW_ADJUDICATION.md') and load(d/'evidence/POSTREVIEW_ADJUDICATION.json')==ad
 assert when(rev['end_utc'])<when(ad['utc'])<when(v['utc'])
 identity=load(E/'identity_expected.json')
 for n,h in identity['files'].items():assert v['files'].get(n)==h==sha(ROOT/n),('canonical identity',label,n)
 return v,d,{'path':str(vp.relative_to(ROOT)),'sha256':sha(vp),'status':v['status'],'utc':v['utc'],'source_freeze_sha256':expectedfreeze,'pins':len(v['files']),'actual_review':rev}

def selected(mode):
 assert mode in MODES
 return ['179']+(['180'] if mode in ['exterior','both'] else [])+(['181'] if mode=='both' else [])

def extract(mode):
 p=source();constants=load(E/'constants.json');parents={};vs={};dirs={}
 om=load(ROOT/'research/outer_majorant/evidence/outer_result.json');im=load(ROOT/'research/inner_majorant/evidence/inner_result.json');modal=load(ROOT/'data_exact/modal_v2.json')
 assert F(om['tb_exact'])==F(constants['b']) and F(im['ta_exact'])==F(constants['a'])
 for key in ['k','L']:
  assert F(om['scalars_exact'][key])==F(im[key+'_exact'])==F(float.fromhex(modal['scalars_hex'][key]))==F(constants[key])
 for label in selected(mode):vs[label],dirs[label],parents[label]=parent(p,label)
 def read(label,name):
  path=dirs[label]/'evidence'/name;n=str(path.relative_to(ROOT));assert vs[label]['files'].get(n)==sha(path);return load(path)
 s=read('179','full_summary.json');t=read('179','full_tails.json')
 assert s['status']=='COMPUTED_COMPLETE_DERIVATIVE_NORM_BOUNDS_REQUIRES_INDEPENDENT_AUDIT' and s['full_middle'] is True and s['cells']==7809
 assert t['status']=='PASS_ENTIRE_INNER_OUTER_DERIVATIVE_TAIL_CALCULATIONS'
 assert t['geometry_exact']=={k:constants[k] for k in ['a','b','k','L']}
 assert s['tails_sha256']==sha(dirs['179']/'evidence/full_tails.json')
 assert s['strict_decimal_ceilings']==vs['179']['strict_decimal_ceilings']
 regional={r:[] for r in REGIONS};origin={r:[] for r in REGIONS}
 for j in range(2):
  middle=[];inner=[];outer=[]
  for engine in ['arb512','iv200']:
   mid=two(s['engines'][engine]['middle_bound_sums_exact'])[j];ii=compact(t['bounds'][engine]['inner_norm_squares'][j])[1];oo=compact(t['bounds'][engine]['outer_norm_squares'][j])[1]
   assert pair(s['engines'][engine]['whole_plane_bound_squares'][j])[0]<=mid+ii+oo<=pair(s['engines'][engine]['whole_plane_bound_squares'][j])[1]
   middle.append(mid);inner.append(ii);outer.append(oo)
  for region,values in [('middle',middle),('inner',inner),('outer',outer)]:
   regional[region].append(str(max(values)));origin[region].append({'parent':'179','field':'engines.*.middle_bound_sums_exact' if region=='middle' else 'bounds.*.'+region+'_norm_squares','norm_index':j,'engine_upper_bounds':list(map(str,values))})
 tc=load(ROOT/'research/derivative_end_tails/evidence/checks.json')
 assert tc['status']=='PASS_CANONICAL_DERIVATIVE_END_TAILS_REQUIRES_ACTUAL_REVIEW'
 for label,region,ncells,flag in [('180','outer',89,'full_exterior'),('181','inner',44,'full_inner')]:
  if label not in dirs:continue
  ref=read(label,'full_summary.json')
  assert ref['status']==('COMPUTED_OUTER_DERIVATIVE_CELLS_REQUIRES_AUDIT_AND_REVIEW' if label=='180' else 'COMPUTED_INNER_DERIVATIVE_CELLS_REQUIRES_AUDIT_AND_REVIEW')
  assert ref[flag] is True and ref['cells']==ncells and ref['indices']==list(range(ncells))
  assert ref['source_freeze_sha256']==constants['source_freezes'][label] and ref['norms']['strict_decimal_ceilings']==vs[label]['strict_decimal_ceilings']
  cs=two(ref['cell_squares_upper_exact']);ts=two(ref['accepted_tail_squares_upper_exact']);total=two(ref['combined_squares_upper_exact'])
  manifest=ROOT/('research/outer_cells/evidence/full_q16_manifest.json' if label=='180' else 'research/inner_cells/evidence/full_q16_manifest.json')
  assert vs[label]['files'].get(str(manifest.relative_to(ROOT)))==sha(manifest)
  ma=load(manifest);assert ma['Q']==16;cells=[tuple(map(rational,v)) for v in ma['cells']];cells=cells if label=='180' else cells[10:]
  assert len(cells)==ncells and cells[0][0]==F(0 if label=='180' else -5) and cells[-1][1]==F(17 if label=='180' else 0)
  for i,(a,b) in enumerate(cells):assert a<b and (i==0 or cells[i-1][1]==a)
  if label=='181':
   ir=load(ROOT/'research/inner_majorant/evidence/inner_result.json');assert all(F(ir[n])==F(constants[k]) for n,k in [('k_exact','k'),('L_exact','L'),('ta_exact','a')])
  for j,suffix in enumerate(['eps','eps_minus_eps_t']):
   q=rational(tc['strict_decimal_ceilings']['tail_norms'][region+'_'+suffix]);assert q>0 and ts[j]==q*q and total[j]==cs[j]+ts[j]
   for engine in ['arb512','iv200']:assert q>pair(tc['enclosures'][engine]['tail_norms'][region+'_'+suffix])[1]
   regional[region][j]=str(total[j]);origin[region][j]={'parent':label,'field':'combined_squares_upper_exact','norm_index':j,'finite_cells_sq_upper_exact':str(cs[j]),'accepted_tail_sq_upper_exact':str(ts[j]),'tail_added_exactly_once':True}
 rehash(p)
 data={'schema':'canonical-derivative-regional-squares-v1','mode':mode,'norms':constants['norms'],'geometry_exact':{k:constants[k] for k in ['a','b','k','L']},'regions':constants['regions'],'region_sq_upper_exact':regional,'origins':origin,'parents':parents,'canonical_identity':load(E/'identity_expected.json'),'original179_whole_plane_ceilings':vs['179']['strict_decimal_ceilings'],'source_freeze_sha256':sha(E/'source_freeze.json'),'files':dict(sorted(p.items())),'scope':'Exact parent-derived regional squared upper bounds for the same canonical trial. Requires this application scalar evaluation, actual review and later adjudication before acceptance.'}
 return data
