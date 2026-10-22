"""Tamper diagnostics plus real resumed computation of an interrupted prefix."""
from common import *
import argparse

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=('prepare','verify'),required=True);args=ap.parse_args()
 nodes,keys,tables,dep,selected=load_geometry();startup=startup_remainders(nodes,keys,tables,selected);sourcepath=E/'smoke_rows.jsonl'
 lines=sourcepath.read_bytes().splitlines(keepends=True);h=json.loads(lines[0]);indices=h['indices'];assert h==header(indices,dep,startup)
 if args.phase=='prepare':
  checks={};testpath=E/'fault_test_rows.jsonl'
  def rejected(name,raw):
   testpath.write_bytes(raw)
   try:read_stream(testpath,h,nodes,keys,tables,selected)
   except (AssertionError,ValueError,KeyError,TypeError,IndexError):checks[name]=True;return
   raise AssertionError('accepted '+name)
  modified=dict(h);modified['source_precision_bits']=127;rejected('changed_header',(canon(modified)+'\n').encode()+b''.join(lines[1:]))
  first=json.loads(lines[1]);first['coefficient_checks']['arb512']-=1;rejected('changed_count',lines[0]+(canon(first)+'\n').encode()+b''.join(lines[2:]))
  rejected('duplicate_row',b''.join(lines[:2])+lines[1]+b''.join(lines[2:]))
  rejected('reordered_rows',lines[0]+lines[2]+lines[1]+b''.join(lines[3:]))
  rejected('newline_terminated_bad_json',b''.join(lines[:2])+b'{bad}\n')
  rejected('incomplete_footer',b''.join(lines[:3])+lines[-1])
  changed=json.loads(lines[1]);changed['endpoint_record']['balls'][0][0][0]+=1
  rejected('changed_ball_with_resealed_chain',lines[0]+(canon(append_chain({k:v for k,v in changed.items() if k not in ('chain','previous_chain')},digest(h)))+'\n').encode())
  for p in (E/'restart_live_rows.jsonl',E/'restart_live_restarts.jsonl',E/'restart_live_summary.json'):assert not p.exists(),p
  (E/'restart_live_rows.jsonl').write_bytes(b''.join(lines[:3])+b'{"uncommitted_partial":')
  testpath.unlink();write_json(E/'restart_preparation.json',{'utc':utc(),'status':'READY_FOR_REAL_RESUME','checks':checks,'rows_retained':2,'source_sha256':sha(__file__),'smoke_rows_sha256':sha(sourcepath)})
 else:
  p=load(E/'restart_preparation.json');s=load(E/'restart_live_summary.json');a=load(E/'restart_live_output_audit.json');r=load(E/'restart_live_replay.json')
  assert p['source_sha256']==sha(__file__) and p['smoke_rows_sha256']==sha(sourcepath)
  assert s['resumed_from']==2 and s['status']=='COMPUTED_REQUIRES_OUTPUT_AUDIT' and s['cells_complete']==len(indices)
  assert a['status']=='PASS_STRUCTURE_REQUIRES_FULL_FRESH_REPLAY' and r['status']=='PASS_EVERY_BOX_FRESH_REPLAY_REQUIRES_VERIFIER_CLOSURE'
  resumed=(E/'restart_live_rows.jsonl').read_bytes().splitlines(keepends=True);assert resumed==lines
  events=[json.loads(x) for x in (E/'restart_live_restarts.jsonl').read_text().splitlines()]
  assert [e['action'] for e in events]==['remove_uncommitted_trailing_line','authenticated_resume'] and events[1]['complete_rows']==2
  checks={**p['checks'],'real_continuation':True,'complete_stream_bitwise_equal':True,'trailing_repair_logged':True,'fresh_replay_after_restart':True}
  write_json(E/'restart_checks.json',{'utc':utc(),'status':'PASS_RESTART_AND_REAL_CONTINUATION_DIAGNOSTICS','checks':checks,'source_sha256':sha(__file__),'restart_stream_sha256':sha(E/'restart_live_rows.jsonl'),'restart_events_sha256':sha(E/'restart_live_restarts.jsonl')});print(canon(checks),flush=True)
if __name__=='__main__':main()
