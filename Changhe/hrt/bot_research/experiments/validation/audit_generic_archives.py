"""Audit archived declared inputs without assuming any particular bot data file."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
 p=argparse.ArgumentParser();p.add_argument('--campaigns',nargs='+',required=True);p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();inputs={};campaigns=[]
 for name in args.campaigns:
  folder=Path(name);assert not folder.is_absolute() and '..' not in folder.parts
  freeze_path=folder/'freeze.json';freeze=json.loads(freeze_path.read_text());inputs[str(freeze_path)]=digest(freeze_path)
  files=[p for p in freeze['source_sha256'] if p.endswith('.json') and digest(p)==freeze['manifest_sha256']];assert len(files)==1
  manifest=json.loads(Path(files[0]).read_text())
  for path,sha in manifest['input_sha256'].items():assert freeze['source_sha256'].get(path)==sha,path
  for path,sha in freeze['source_sha256'].items():
   q=Path(path);assert not q.is_absolute() and '..' not in q.parts
   assert digest(q)==sha and digest(folder/'sources'/q)==sha,path
  jobs=json.loads((folder/'jobs.json').read_text())
  for job in jobs:
   row=json.loads((folder/'results'/(job['id']+'.json')).read_text());assert not row['source_changed_during_match']
   for field in ('source_sha256','source_sha256_at_end'):
    for path,sha in row[field].items():assert freeze['source_sha256'].get(path)==sha,path
  assert len(jobs)==manifest['expected_conditions']
  campaigns.append(dict(campaign=name,archived_inputs=len(freeze['source_sha256']),results=len(jobs),declared_data=[p for p in manifest['input_sha256'] if '/data/' in p],all_passed=True))
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,checker_sha256=digest(__file__),inputs=inputs,campaigns=campaigns,scope='Byte identity of every declared input and archive, and every loaded source attestation. No particular data input is assumed. Original-engine replay is a separate check.');atomic_json(args.output,out,exclusive=True);print(json.dumps(out))

if __name__=='__main__':main()
