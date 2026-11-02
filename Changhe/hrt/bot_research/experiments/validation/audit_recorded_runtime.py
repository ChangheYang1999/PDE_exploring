"""Summarize attested whole-decision timing, without claiming a branch trace."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row


def main():
 p=argparse.ArgumentParser();p.add_argument('--campaigns',nargs='+',required=True);p.add_argument('--candidate',required=True);p.add_argument('--threshold',type=float,default=3);p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter();inputs={};rows=[];groups=[];specs=set()
 for folder in map(Path,a.campaigns):
  chosen=[]
  for job in json.loads((folder/'jobs.json').read_text()):
   c=job['condition']
   if c['candidate_id']!=a.candidate:continue
   path=folder/'results'/(job['id']+'.json');row=checked_row(str(path),inputs);specs.add(c['candidate_spec']);timing=row['decision_seconds_candidate_first'][0]
   record=dict(result_path=str(path),candidate_spec=c['candidate_spec'],opponent=c['opponent_id'],side=c['candidate_side'],**timing);chosen.append(record);rows.append(record)
  assert chosen
  groups.append(dict(campaign=str(folder),conditions=len(chosen),calls=sum(r['calls'] for r in chosen),decision_seconds=sum(r['total'] for r in chosen),max_decision_seconds=max(r['max'] for r in chosen),conditions_at_or_above_threshold=sum(r['max']>=a.threshold for r in chosen)))
 assert len(specs)==1
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=inputs,candidate=a.candidate,candidate_spec=next(iter(specs)),threshold_seconds=a.threshold,conditions=len(rows),calls=sum(r['calls'] for r in rows),maximum=max(rows,key=lambda r:r['max']),conditions_at_or_above_threshold=sum(r['max']>=a.threshold for r in rows),campaigns=groups,scope='Recorded whole-decision wall durations; repeated or paired conditions are not independent samples. This does not inspect deadline branches or establish future deterministic behavior.')
 atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','conditions','calls','maximum','conditions_at_or_above_threshold')}))

if __name__=='__main__':main()
