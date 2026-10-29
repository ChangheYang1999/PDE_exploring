#!/usr/bin/env python3
"""Audit a frozen prefix of process counters; report lower bounds, not totals."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
ROOT=Path(__file__).resolve().parent;LANE=ROOT.parent

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists() or not out.is_relative_to(LANE):raise ValueError('Fresh own-lane directory required')
 out.mkdir(parents=True);start=time.perf_counter();cpu=time.process_time()
 source=ROOT/'results/resource_observations_20261029T0057Z.jsonl';raw=source.read_bytes();end=raw.rfind(b'\n')+1;prefix=raw[:end]
 if not prefix:raise ValueError('No complete observations')
 (out/'observations.jsonl').write_bytes(prefix)
 observations=[json.loads(line)for line in prefix.splitlines()];processes={};checks=[];previous=None
 for oi,obs in enumerate(observations):
  ts=datetime.fromisoformat(obs['recorded_utc'])
  if previous is not None and ts<=previous:raise ValueError('Observation clock is not increasing')
  previous=ts;seen=set()
  for row in obs['processes']:
   key=(row['pid'],row['start_ticks']);assert key not in seen;seen.add(key)
   counter=row['user_cpu_seconds']+row['system_cpu_seconds'];assert counter>=0
   old=processes.get(key)
   if old is not None:
    if counter+1e-9<old['last_observed_cpu_seconds']:raise ValueError('Nonmonotone per-process CPU counter')
    old.update(last_seen_utc=obs['recorded_utc'],last_observed_cpu_seconds=counter,maximum_resident_bytes=max(old['maximum_resident_bytes'],row['resident_bytes']))
    old['observations']+=1
   else:
    processes[key]=dict(pid=key[0],start_ticks=key[1],first_seen_utc=obs['recorded_utc'],last_seen_utc=obs['recorded_utc'],first_observed_cpu_seconds=counter,last_observed_cpu_seconds=counter,maximum_resident_bytes=row['resident_bytes'],command=row['command'],lane_scripts=row['lane_scripts'],observations=1)
 records=list(processes.values())
 for row in records:
  row['scope']='observer bookkeeping' if any(Path(s).name=='resource_monitor.py'for s in row['lane_scripts']) else 'observed lane process'
 observed=sum(r['last_observed_cpu_seconds']for r in records);bookkeeping=sum(r['last_observed_cpu_seconds']for r in records if r['scope']=='observer bookkeeping')
 # Sum only increases actually bracketed by two observations for the strict window lower bound.
 bracketed=sum(r['last_observed_cpu_seconds']-r['first_observed_cpu_seconds']for r in records)
 intervals=[(datetime.fromisoformat(b['recorded_utc'])-datetime.fromisoformat(a['recorded_utc'])).total_seconds()for a,b in zip(observations,observations[1:])]
 result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),source=str(source.relative_to(LANE)),snapshot_sha256=hashlib.sha256(prefix).hexdigest(),source_prefix_bytes=end,ignored_unterminated_bytes=len(raw)-end,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),observation_count=len(observations),distinct_process_identities=len(records),first_observation_utc=observations[0]['recorded_utc'],last_observation_utc=observations[-1]['recorded_utc'],maximum_observation_gap_seconds=max(intervals,default=0),observed_lifetime_CPU_lower_bound_seconds=observed,observer_bookkeeping_included_seconds=bookkeeping,other_observed_lifetime_CPU_lower_bound_seconds=observed-bookkeeping,bracketed_CPU_increase_lower_bound_seconds=bracketed,processes=records,wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,checks=['complete JSON-line prefix parsed','strictly increasing observation times','unique PID/start-tick identity per observation','nonnegative and monotone per-process CPU counters'],scope='Only the maximum lifetime counter for each PID/start-tick identity is summed. This is an incomplete campaign CPU lower bound, not an exact total or GPU utilization. The bracketed increase is a separate lower bound within the observation window. Short-lived and pre-observer jobs may be absent; final unobserved CPU is omitted. Do not add these totals to overlapping job CPU records.')
 (out/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
 (out/'AUDIT.md').write_text(f"# Process-counter audit\n\nRecorded {result['completed_utc']}. The frozen prefix contains {len(observations)} observations, from {result['first_observation_utc']} to {result['last_observation_utc']}, covering {len(records)} distinct PID/start-tick identities. Per-process counters are nonnegative and monotone.\n\nSumming each process's largest observed lifetime CPU counter once gives a campaign lower bound of {observed:.2f} CPU seconds, including {bookkeeping:.2f} seconds of observer bookkeeping. Summing only increases bracketed by observations gives a separate window lower bound of {bracketed:.2f} CPU seconds. These quantities overlap and must not be added.\n\nThe observer omits earlier jobs, processes too short to be sampled and final counter increases after the last sample. Job timing records may improve individual contributions, but require explicit deduplication. No exact full-campaign CPU total or GPU utilization is established here. Audit data, process identities and hashes are in audit.json.\n")
 print(json.dumps({k:v for k,v in result.items()if k not in ['processes','checks']},indent=2))
if __name__=='__main__':main()
