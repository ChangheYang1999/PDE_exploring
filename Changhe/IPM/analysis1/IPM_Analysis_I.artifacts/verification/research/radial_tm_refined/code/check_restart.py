"""Fault injection against actual resume parsing and actual independent audit."""
from common import *
from check_full import inspect_stream
from audit_output import required_replay,audit
import copy,argparse

def expect_fail(fn):
 try:fn()
 except (AssertionError,ValueError,KeyError,IndexError):return True
 raise AssertionError('fault not rejected')

def prepare():
 source=OUT/'smoke_refined_rows.jsonl';lines=source.read_bytes().splitlines(keepends=True);header=parse(lines[0]);rows=[parse(x) for x in lines[1:-1]]
 assert len(rows)==4 and header['cells']==[0,2955,4102,7808] and header['modes']==list(range(1,262))
 results={};faultdir=OUT/'restart_faults';faultdir.mkdir(exist_ok=True)
 def run_case(name,raw,allow=False):
  p=faultdir/(name+'.jsonl');assert not p.exists();p.write_bytes(raw);before=sha(p)
  try:value=inspect_stream(p,header,header['cells'],header['modes'],allow)
  finally:assert sha(p)==before,'read-only parser changed the stream'
  return value,p
 prefix=lines[0]+lines[1];broken=b'{"type":"cell",'
 parsed,p=run_case('truncated',prefix+broken,True)
 assert parsed[0]==rows[:1] and parsed[1] is None and parsed[2]=={'offset':len(prefix),'bytes':len(broken)}
 with p.open('r+b') as f:f.truncate(parsed[2]['offset']);f.flush();os.fsync(f.fileno())
 assert p.read_bytes()==prefix;results['truncated_tail_preserves_prior_complete_bytes']=True
 changed=copy.deepcopy(header);changed['engine_precisions']['arb_bits']=511
 results['changed_header_rejected']=expect_fail(lambda:run_case('header',(canonical(changed)+'\n').encode()+lines[1],True))
 changed=copy.deepcopy(rows[0]);changed['counts']['arb512']['coefficients']-=1
 results['wrong_count_rejected']=expect_fail(lambda:run_case('count',lines[0]+(canonical(changed)+'\n').encode(),True))
 results['duplicate_row_rejected']=expect_fail(lambda:run_case('duplicate',prefix+lines[1],True))
 changed=copy.deepcopy(rows[0]);changed['witnesses'][0]['candidate_hi_units']=str(-(1<<1200))
 results['invalid_saved_endpoint_rejected']=expect_fail(lambda:run_case('endpoint',lines[0]+(canonical(changed)+'\n').encode(),True))
 changed=copy.deepcopy(rows[0]);changed['a']=changed['b']
 results['zero_width_rejected']=expect_fail(lambda:run_case('width',lines[0]+(canonical(changed)+'\n').encode(),True))
 event={'completed':1,'actual_interruption':True,'last_completed':0,'first_uncompleted':2955}
 assert set(required_replay(header,[event]))=={0,2955,7808};results['actual_restart_requires_both_neighbor_cells']=True
 initial={'completed':0,'actual_interruption':False,'last_completed':None,'first_uncompleted':0}
 assert required_replay(header,[initial])==[0,2955,7808];results['initial_empty_resume_not_an_interruption']=True
 good,_=run_case('complete',b''.join(lines));assert good[1] is not None;results['complete_stream_footer_valid']=True
 # Feed coherent altered files to the actual auditor. Missing footer cannot pass its final audit.
 original_summary=load(OUT/'smoke_refined_summary.json')
 def audit_fault(tag,raw):
  p=OUT/(tag+'_rows.jsonl');s=OUT/(tag+'_summary.json');assert not p.exists() and not s.exists()
  p.write_bytes(raw);summary=copy.deepcopy(original_summary);summary['rows_sha256']=sha(p);s.write_text(canonical(summary)+'\n')
  before=(sha(p),sha(s))
  result=expect_fail(lambda:audit(tag,True));assert (sha(p),sha(s))==before
  return result
 results['actual_auditor_missing_footer_rejected']=audit_fault('fault_nofooter',b''.join(lines[:-1]))
 # Change only a claimed candidate hash, preserve all endpoint witnesses, repair footer/summary hashes.
 changed=copy.deepcopy(rows[0]);changed['array_manifest']['P_rad']['sha256']='0'*64
 changed_lines=[lines[0],(canonical(changed)+'\n').encode(),*lines[2:-1]]
 footer=parse(lines[-1]);footer['prior_stream_sha256']=hashlib.sha256(b''.join(changed_lines)).hexdigest()
 results['actual_auditor_altered_candidate_rejected']=audit_fault('fault_candidate',b''.join(changed_lines)+(canonical(footer)+'\n').encode())
 # Corrupt the known original failure row's refinement records while preserving valid other witnesses.
 refined=next(r for r in rows if r['cell']==2955);assert refined['coefficient_refinements']
 rowpos=header['cells'].index(2955)+1
 for kind in ('duplicate_refinement','changed_refinement_target','changed_refinement_original','changed_refinement_success'):
  changed=copy.deepcopy(refined)
  if kind=='duplicate_refinement':changed['coefficient_refinements'].append(copy.deepcopy(changed['coefficient_refinements'][0]))
  elif kind=='changed_refinement_target':changed['coefficient_refinements'][0]['candidate_lo_units']='0'
  elif kind=='changed_refinement_original':changed['coefficient_refinements'][0]['original_bounds']=changed['coefficient_refinements'][0]['refined_bounds']
  else:changed['coefficient_refinements'][0]['refined_bounds']=[[0,0],[0,0]]
  altered=list(lines[:-1]);altered[rowpos]=(canonical(changed)+'\n').encode()
  footer=parse(lines[-1]);footer['prior_stream_sha256']=hashlib.sha256(b''.join(altered)).hexdigest()
  results[kind+'_rejected']=audit_fault('fault_'+kind,b''.join(altered)+(canonical(footer)+'\n').encode())
 live=OUT/'restart_live_rows.jsonl';assert not live.exists();live.write_bytes(prefix+broken)
 out={'utc':utc(),'status':'PREPARED_REAL_RESUME_REQUIRED','checks':results,'source_sha256':sha(__file__),'smoke_rows_sha256':sha(source),'preserved_prefix_sha256':hashlib.sha256(prefix).hexdigest(),'preserved_prefix_bytes':len(prefix),'partial_bytes':len(broken),'scope':'Parser and actual auditor faults passed; execute the real producer, auditor and replay on restart_live before completion.'}
 (OUT/'restart_checks.json').write_text(canonical(out)+'\n');print(canonical(out))

def verify():
 state=load(OUT/'restart_checks.json');assert state['status']=='PREPARED_REAL_RESUME_REQUIRED' and state['source_sha256']==sha(__file__)
 p=OUT/'restart_live_rows.jsonl'
 with p.open('rb') as f:prefix=f.read(state['preserved_prefix_bytes'])
 assert hashlib.sha256(prefix).hexdigest()==state['preserved_prefix_sha256']
 summary=load(OUT/'restart_live_summary.json');a=load(OUT/'restart_live_output_audit.json');r=load(OUT/'restart_live_replay.json')
 assert summary['status']=='COMPUTED_REQUIRES_SEPARATE_OUTPUT_AUDIT' and summary['cells_complete']==4 and summary['rows_sha256']==sha(p)
 assert a['status']=='PASS_OUTPUT_AND_FRESH_PARTICULAR_AUDIT' and a['cells_audited']==4 and not a['full_middle']
 assert r['status']=='PASS_COMPLETE_CELL_REPLAY' and r['required_cells']==r['replayed_cells']==a['replay_required_cells']==[0,2955,7808]
 events=[parse(x) for x in (OUT/'restart_live_restarts.jsonl').read_text().splitlines()];assert len(events)==1
 event=events[0];assert event['actual_interruption'] and event['completed']==1 and event['last_completed']==0 and event['first_uncompleted']==2955
 assert event['partial_tail_removed']=={'offset':state['preserved_prefix_bytes'],'bytes':state['partial_bytes']}
 assert current_pins()==summary['input_pins']==a['source_pins']==r['source_pins']
 state['checks'].update(real_resumed_continuation_preserves_complete_bytes=True,real_resumed_continuation_audited=True,real_replay_covers_both_restart_neighbors=True)
 state.update(utc=utc(),status='PASS_RESTART_AND_REAL_CONTINUATION_DIAGNOSTICS',live_rows_sha256=sha(p),live_summary_sha256=sha(OUT/'restart_live_summary.json'),live_audit_sha256=sha(OUT/'restart_live_output_audit.json'),live_replay_sha256=sha(OUT/'restart_live_replay.json'),scope='Fault injection plus real resumed continuation, actual independent audit and complete two-engine replay. Four cells only; no full result.')
 (OUT/'restart_checks.json').write_text(canonical(state)+'\n');print(canonical(state))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=('prepare','verify'),required=True);args=ap.parse_args();prepare() if args.phase=='prepare' else verify()
