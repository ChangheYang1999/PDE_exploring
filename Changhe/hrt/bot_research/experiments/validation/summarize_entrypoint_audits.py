"""Bind complete fresh entry-point checks to their current source and game bytes."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import argparse,hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--audit-dirs',nargs='+',required=True);p.add_argument('--candidate-sha256',required=True);p.add_argument('--expected',type=int,required=True);p.add_argument('--output',required=True);args=p.parse_args()
 inputs={};sources={};seen=set();cases=[];groups=Counter()
 def bind(path):
  path=str(path);value=digest(path)
  if path in inputs:assert inputs[path]==value
  inputs[path]=value
  return json.loads(Path(path).read_text())
 for directory in args.audit_dirs:
  root=Path(directory);summary=bind(root/'summary.json');meta=bind(root/'metadata.json')
  assert summary['all_passed'] and summary['counts']=={'passed':summary['planned_jobs']}
  assert summary['campaign']==meta['campaign']
  for path,sha in meta['inputs'].items():assert digest(path)==sha;inputs[path]=sha
  campaign=Path(summary['campaign']);all_jobs=bind(campaign/'jobs.json')
  jobs=[j for j in all_jobs if j['bots'][j['condition']['candidate_side']].get('spec','').partition(':')[0]=='bot_research.bots.best']
  jobs=[j for i,j in enumerate(jobs) if i%meta['shards']==meta['shard']]
  assert [j['id'] for j in jobs]==[c['job'] for c in summary['cases']]
  for job,case in zip(jobs,summary['cases']):
   key=(str(campaign),job['id']);assert key not in seen;seen.add(key)
   assert case['status']=='passed';record=bind(case['audit_path']);assert digest(case['audit_path'])==case['audit_sha256']
   assert record['all_passed'] and record['count']==1 and not record['source_changed_during_run']
   assert record['candidate_sha256']==args.candidate_sha256 and record['candidate_module']=='bot_research.bots.best'
   assert record['source_sha256']['bot_research/bots/best.py']==args.candidate_sha256
   for path,sha in record['source_sha256'].items():
    assert digest(path)==sha
    if path in sources:assert sources[path]==sha
    sources[path]=sha
   for path,sha in record['input_sha256'].items():assert digest(path)==sha;inputs[path]=sha
   detail=record['cases'][0];assert detail['passed'] and not detail['differences'] and detail['all_fresh_actions_legal'] and detail['observations_unchanged']
   prefix=len(job.get('prefixes',[[],[]])[job['condition']['candidate_side']])
   assert prefix==detail['skipped_prefix_rounds']
   rounds=detail['entrypoint_rounds'];assert len(rounds)==detail['rounds']
   for rnd,row in enumerate(rounds,1):
    assert row['round']==rnd and row['policy_invoked']==(rnd>prefix)
    assert row['direct_matches_record'] and row['factory_matches_record'] and row['entrypoints_agree']
   group='standard' if not prefix else 'continuation';groups[group]+=1
   cases.append(dict(campaign=str(campaign),job=job['id'],condition=job['condition'],rounds=len(rounds),prefix_rounds=prefix,policy_rounds=len(rounds)-prefix,audit_path=case['audit_path'],passed=True))
 assert len(cases)==args.expected
 sources[str(Path(__file__).relative_to(Path.cwd()))]=digest(__file__)
 output=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,candidate_sha256=args.candidate_sha256,count=len(cases),groups=dict(groups),policy_rounds=sum(c['policy_rounds'] for c in cases),skipped_prefix_rounds=sum(c['prefix_rounds'] for c in cases),input_sha256=inputs,source_sha256=sources,cases=cases,scope='Every direct and factory call agrees with its frozen recorded public history. No additional independent strength evidence.')
 atomic_json(args.output,output,exclusive=True)
 print(json.dumps({k:output[k] for k in ('time_utc','all_passed','count','groups','policy_rounds','skipped_prefix_rounds')}))
if __name__=='__main__':main()
