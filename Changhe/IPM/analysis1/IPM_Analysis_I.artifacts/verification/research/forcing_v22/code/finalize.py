"""Freeze finite v22 components, preserving all physical hypotheses and failures."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
a=read(D/'evidence/finite_audit.json');assert a['status']=='PASS_V22_FINITE_AUDIT_REVIEW_PENDING_PHYSICAL_OPEN'
pins=dict(a['pins']);assert len(pins)==291
for f,h in pins.items():assert sha(B/f)==h,f
packet=read(D/'evidence/review_packet.json');assert packet['finite_audit_sha256']==sha(D/'evidence/finite_audit.json') and packet['pin_count']==291
s=read(D/'evidence/provenance_supplement.json');assert s['status']=='PASS_V22_EXACT_REGIMES_AND_PRIOR_TRIAL_LINKAGE'
assert s['direct_regime_checks']==s['source_sigma_branch_checks']==43949 and s['prior_pins_rehashed']==179
assert s['classifications']=={'inside':26079,'transition':16502,'straddle':1368}
assert s['code_sha256']==sha(D/'code/check_provenance_supplement.py') and s['data_sha256']==a['source_data_sha256']
for f,h in s['pins'].items():assert sha(B/f)==h;assert f not in pins or pins[f]==h;pins[f]=h
for name,x in s['external_inputs'].items():assert sha(Path(x['path']))==x['sha256']==a['external_inputs'][name]['sha256']
first=read(D/'evidence/provenance_supplement_first.json');assert first['proof_sha256']==sha(D/'FINAL_PROVENANCE_SUPPLEMENT.md')
replays=[];position=0;totalchecks=0
for oldrange in a['exact_cutoff_ranges']:
 start,end=oldrange['start'],oldrange['end'];assert position==start
 p=D/'replay/evidence'/f'attestation_{start:06d}_{end:06d}.json';r=read(p)
 assert r['status']=='PASS_CONTEMPORARY_PINNED_CUTOFF_REPLAY' and r['returncode']==0 and r['all_nontime_output_fields_identical']
 assert r['start_index']==start and r['end_index']==end and r['checks']==6*(end-start)
 assert r['code_sha256']==first['replay_source_sha256']==sha(D/'code/check_cutoff_exact.py')==sha(D/'replay/code/check_cutoff_exact.py')
 for f,h in r['pins'].items():assert sha(B/f)==h,f
 assert r['original_file']==oldrange['file'] and r['original_sha256']==oldrange['sha256']==sha(B/r['original_file'])
 assert r['output_sha256']==sha(B/r['output_file'])
 old,new=read(B/r['original_file']),read(B/r['output_file'])
 assert new['status']=='PASS_V22_SIX_CUTOFF_FULL_POLYNOMIAL_BERNSTEIN' and new['failure_count']==0
 for k in ['utc','seconds']:old.pop(k);new.pop(k)
 assert old==new
 replays.append({'start':start,'end':end,'attestation_sha256':sha(p),'output_sha256':r['output_sha256'],'code_sha256':r['code_sha256']});position=end;totalchecks+=r['checks']
assert len(replays)==9 and position==43949 and totalchecks==263694
reviews={}
for tag,expected,stop in [
 ('forcing_v22_first','e21599cc05a17f2d4cfab7e3c45310562c7cd105b47ff0a9f972567ed4e59996','max_tokens'),
 ('forcing_v22_completed_followup','e922abc48a9a2d4e3b28f15dbfa53dadb1d72b515d38751247cef127a26cc629',None),
 ('forcing_v22_completed_adaptive','8125e83370fe50b8c6e1caca79092b05392a670f061c6e629e59763476ccf323','end_turn')]:
 m=read(R/(tag+'_metadata.json'));req=(R/(tag+'_request.txt')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']==expected
 assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if stop is None:
  assert 'actual_response_model' not in m and 'ValidationException' in m['availability_error'] and not (R/(tag+'_response.json')).exists()
  reviews[tag]=dict(status='PROVIDER_CONFIGURATION_REJECTED_NO_MODEL_EXECUTION',input_sha256=expected,availability_error=m['availability_error'],start_utc=m['start_utc'],end_utc=m['end_utc']);suffixes=['_metadata.json','_request.txt']
 else:
  raw=read(R/(tag+'_response.json'));assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']==stop
  text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert text==(R/(tag+'_response.md')).read_text()
  if stop=='end_turn':assert 'I accept the restricted conditional finite theorem' in text and 'No physical forcing norm, inverse estimate, fixed point or IPM endpoint follows.' in text
  reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']};reviews[tag]['accepted_restricted_theorem']=(stop=='end_turn');suffixes=['_metadata.json','_request.txt','_response.json','_response.md']
 for suffix in suffixes:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
# Include the mandatory addenda, original failures, finite audit and complete replays.
# Recheck immutable old pins before adding newly created files.
for root in [D,D/'code',D/'evidence',D/'replay/code',D/'replay/evidence']:
 for p in root.iterdir():
  if not p.is_file() or p.is_symlink() or p.name=='verdict.json':continue
  f=str(p.relative_to(B));h=sha(p);assert f not in pins or pins[f]==h,f;pins[f]=h
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_V22_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN',prior_finite_pins=291,rows=43949,canonical_points=7810,geometry_cases_inherited_each_engine=106496,cutoff_checks_each_engine=263694,pointwise_checks_each_engine=137235,active_series_scalar_tails=331,conditional_strict_norm_ceilings=a['conditional_strict_norm_ceilings'],contemporary_exact_cutoff_replays=replays,reviews=reviews,refuted=['Original auxiliary Hessian export comparison with producer T2F on26079constant rows; repaired separately; no core or aggregate dependence'],remaining_hypotheses=['H0 physical residual and weak regularity','H1 physical G fields on27447rows','H2 physical composed F fields on16502rows','Additional unretained B3 partial suprema require separate physical ancestry'],files=dict(sorted(pins.items())),scope='PROOF and mandatory addenda plus FINAL_ADJUDICATION. Finite and conditional components only. Full Green/T/P/R, nonlinear residual jets, composed arithmetic ancestry, actual BLAS kernel and every physical forcing/IPM endpoint remain OPEN.')
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
