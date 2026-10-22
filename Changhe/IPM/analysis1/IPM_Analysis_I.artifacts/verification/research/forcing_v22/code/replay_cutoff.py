"""Bounded contemporary replay with before/after hashes and immutable old outputs."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,os,hashlib,json,argparse,time
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=D/'replay'
ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,required=True);ap.add_argument('--end',type=int,required=True);a=ap.parse_args();assert 0<=a.start<a.end<=43949

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
files=[D/'code/check_cutoff_exact.py',R/'code/check_cutoff_exact.py',D/'source/runs/forcing/v22_p9_merged.json',Path(__file__)]
pins={str(p.relative_to(B)):sha(p) for p in files}
assert pins[str(files[0].relative_to(B))]==pins[str(files[1].relative_to(B))]=='2b3e3c5127941b0a02b2431a58279957ffa3f603a9e12ec2060c132b3eabf084'
assert pins[str(files[2].relative_to(B))]=='b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201'
assert (R/'source/runs/forcing/v22_p9_merged.json').resolve()==files[2]
tag=f'cutoff_full_bernstein_{a.start:06d}_{a.end:06d}';op=R/'evidence'/(tag+'.json');assert not op.exists()
cmd=[sys.executable,str(files[1]),'--start',str(a.start),'--count',str(a.end-a.start)]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1');env.pop('PYTHONOPTIMIZE',None)
tic=time.monotonic();start=datetime.now(timezone.utc).isoformat();p=subprocess.run(cmd,capture_output=True,text=True,timeout=100,env=env,cwd=B)
record=dict(start_utc=start,end_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-tic,command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,pins=pins,code_sha256=pins[str(files[1].relative_to(B))],start_index=a.start,end_index=a.end)
for f,h in pins.items():assert sha(B/f)==h,f
assert p.returncode==0,record
old=json.loads((D/'evidence'/(tag+'.json')).read_text());new=json.loads(op.read_text());assert new['status']=='PASS_V22_SIX_CUTOFF_FULL_POLYNOMIAL_BERNSTEIN'
for k in ['utc','seconds']:old.pop(k);new.pop(k)
assert old==new
record.update(status='PASS_CONTEMPORARY_PINNED_CUTOFF_REPLAY',output_file=str(op.relative_to(B)),output_sha256=sha(op),original_file=str((D/'evidence'/(tag+'.json')).relative_to(B)),original_sha256=sha(D/'evidence'/(tag+'.json')),all_nontime_output_fields_identical=True,checks=new['checks'])
(R/'evidence'/(f'attestation_{a.start:06d}_{a.end:06d}.json')).write_text(json.dumps(record,indent=2)+'\n');print(record['end_utc'],record['status'],new['checks'],'checks',record['seconds'],'seconds',flush=True)
