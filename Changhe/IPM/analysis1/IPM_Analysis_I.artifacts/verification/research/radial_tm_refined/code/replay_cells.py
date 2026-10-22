"""Re-execute whole required cells with both engines and compare pinned candidates."""
import argparse,time
from common import *
from check_full import process_cell

def main(tag):
 start=time.monotonic();audit=load(OUT/(tag+'_output_audit.json'));summary=load(OUT/(tag+'_summary.json'))
 assert audit['status']=='PASS_OUTPUT_AND_FRESH_PARTICULAR_AUDIT' and audit['input_summary_sha256']==sha(OUT/(tag+'_summary.json'))
 assert current_pins()==summary['input_pins']==audit['source_pins']
 path=OUT/(tag+'_rows.jsonl');assert sha(path)==audit['rows_sha256']==summary['rows_sha256']
 lines=path.read_text().splitlines();header=parse(lines[0]);assert parse(lines[-1])['type']=='footer'
 events_path=OUT/(tag+'_restarts.jsonl');events=[parse(x) for x in events_path.read_text().splitlines()] if events_path.exists() else []
 # Reconstruct required set directly, instead of trusting the auditor's set.
 needed=set(replay_base())&set(header['cells'])
 for event in events:
  if event['actual_interruption']:
   for key in ('last_completed','first_uncompleted'):
    if event[key] is not None:needed.add(event[key])
 assert sorted(needed)==audit['replay_required_cells']
 saved={}
 for line in lines[1:-1]:
  row=parse(line)
  if row['cell'] in needed:saved[row['cell']]=row
 assert set(saved)==needed and needed
 data=Data();results=[]
 for ci in sorted(needed):
  row=process_cell(data,ci,header['modes']);old=saved[ci]
  assert not row['failures'] and row['array_manifest']==old['array_manifest']
  for key in ('a','b','h','wide','parent_span','counts','forcing','E_witnesses','witnesses','coefficient_refinements','fallbacks'):
   assert row[key]==old[key],('replay differs',ci,key)
  results.append({'cell':ci,'counts':row['counts'],'seconds':row['seconds'],'array_manifest':row['array_manifest']})
  print(canonical({'utc':utc(),'replayed_cell':ci,'seconds':row['seconds']}),flush=True)
 assert current_pins()==summary['input_pins'] and sha(path)==summary['rows_sha256']
 result={'utc':utc(),'status':'PASS_COMPLETE_CELL_REPLAY','required_cells':sorted(needed),'replayed_cells':[r['cell'] for r in results],'results':results,'source_pins':current_pins(),
 'output_audit_sha256':sha(OUT/(tag+'_output_audit.json')),'restart_events_sha256':sha(events_path) if events_path.exists() else None,'replay_seed':SEED,'seconds':time.monotonic()-start,
 'scope':'Exact candidate and complete two-engine replay on fixed and actual interruption cells. Full radial coverage still comes from the exhaustive stream.'}
 (OUT/(tag+'_replay.json')).write_text(canonical(result)+'\n');print(canonical({k:result[k] for k in ('utc','status','required_cells','replayed_cells','seconds')}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);args=ap.parse_args();main(args.tag)
