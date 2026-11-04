"""Run the admitted numerics_agent_2/core49 source request with finite resource limits."""
from pathlib import Path
import argparse,json,os,re,signal,subprocess,sys,time
import common_v01 as c
p=argparse.ArgumentParser();c.add_arguments(p);a=p.parse_args()
R=Path.cwd().resolve();C=R.parent
assert R.name=='numerics_agent_2';c.environment(49)
q,m,bindings=c.authenticate(C,a)
D=c.named(R,q['method_directory']);ip=D/'installation_v01.json';installation=c.read(ip)
assert installation['status']=='INSTALLED_NOT_STARTED'
for key,value in [('request_sha256',a.request_sha256),('review_sha256',a.review_sha256),('adoption_sha256',a.adoption_sha256),('method_manifest_sha256',q['method_manifest_sha256'])]:assert installation[key]==value
assert installation['bindings']==bindings
for name,h in installation['copies'].items():assert c.digest(c.named(R,name))==h
assert c.digest(Path(__file__))==m['files']['code/guard_v01.py']
assert c.digest(Path(c.__file__))==m['files']['code/common_v01.py']
for name,h in m['files'].items():assert c.digest(c.named(D,name))==h
installation_sha=c.digest(ip)
assert c.moment(q['created_utc'])<=c.moment(c.read(c.named(C,a.review))['received_utc'])<=c.moment(c.read(c.named(C,a.adoption))['received_utc'])<=c.moment(installation['started_utc'])
now=c.moment(c.stamp());assert now<c.moment(q['no_new_after'])
resources=c.usage(R);processes=c.processes(R,[os.getpid()])
assert not processes['conflicts'] and processes['host_rss_bytes']<q['max_host_rss_bytes']
assert q['lane_cap_bytes']-resources['lane_bytes']>=q['min_start_reserve_bytes']
assert resources['filesystem_free_bytes']>=q['min_filesystem_free_bytes']
V=c.named(R,q['output']);assert not V.exists() and not V.is_symlink();V.mkdir(parents=True)
script=D/'code/check_v01.py'
argv=['-B',str(script.relative_to(R)),'--roots',','.join(map(str,q['roots'])),'--output',q['output']]
start=c.stamp();tick=time.monotonic();reason=None;signals=[];samples=0
with (V/'run_v01.log').open('x') as log:
 child=subprocess.Popen([sys.executable,*argv],cwd=R,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
 c.save(V/'guard_start_v01.json',dict(started_utc=start,controller_pid=os.getpid(),child_pid=child.pid,argv=argv,installation_sha256=installation_sha,initial_resources=resources,initial_processes=processes,request_sha256=a.request_sha256))
 while child.poll() is None:
  elapsed=time.monotonic()-tick;resources=c.usage(R);processes=c.processes(R,[os.getpid(),child.pid]);samples+=1
  observation=dict(utc=c.stamp(),elapsed_seconds=elapsed,**resources,**processes)
  with (V/'resource_samples_v01.jsonl').open('a') as f:json.dump(observation,f);f.write('\n')
  if elapsed>=q['limit_seconds']:reason='7200-second source limit'
  elif c.moment(c.stamp())>=c.moment(q['stop_at']):reason='absolute stop time'
  elif resources['lane_bytes']>=q['stop_lane_bytes']:reason='host lane storage limit'
  elif resources['filesystem_free_bytes']<q['min_filesystem_free_bytes']:reason='filesystem free reserve'
  elif processes['host_rss_bytes']>=q['max_host_rss_bytes']:reason='host resident memory limit'
  elif processes['conflicts']:reason='another Python process pinned to core49'
  if reason:
   try:os.killpg(child.pid,signal.SIGTERM);signals.append('SIGTERM to own child process group')
   except ProcessLookupError:pass
   try:child.wait(timeout=10)
   except subprocess.TimeoutExpired:
    try:os.killpg(child.pid,signal.SIGKILL);signals.append('SIGKILL to own child process group')
    except ProcessLookupError:pass
    child.wait()
   break
  try:child.wait(timeout=min(10,max(.01,q['limit_seconds']-elapsed)))
  except subprocess.TimeoutExpired:pass
end=c.stamp();elapsed=time.monotonic()-tick
if elapsed>=q['limit_seconds']:reason=reason or 'source completed outside time limit'
if c.moment(end)>=c.moment(q['stop_at']):reason=reason or 'source completed after absolute stop'
final_resources=c.usage(R)
if final_resources['lane_bytes']>=q['stop_lane_bytes'] or final_resources['filesystem_free_bytes']<q['min_filesystem_free_bytes']:reason=reason or 'final storage reserve reached'
lp=V/'run_v01.log';text=lp.read_text()
text=re.sub(r'(File ")([^"\n]+)(")',lambda match:match.group(1)+Path(match.group(2)).name+match.group(3),text)
text=text.replace(str(R),'.').replace(str(C),'..');lp.write_text(text)
unchanged=c.recheck(C,bindings) and c.digest(ip)==installation_sha
unchanged=unchanged and all(c.digest(c.named(R,n))==h for n,h in installation['copies'].items())
cp=V/'check_v01.json';complete=False
if cp.is_file():
 check=c.read(cp)
 complete=check['status']=='COMPLETED_SOURCE_RECONSTRUCTION' and check['requested_roots']==q['roots'] and [r['root_index'] for r in check['results']]==q['roots']
record=dict(schema='ordinary-slab-host-execution-v1',status='COMPLETED' if child.returncode==0 and reason is None and unchanged and complete else 'FAILED',started_utc=start,finished_utc=end,elapsed_seconds=elapsed,limit_seconds=q['limit_seconds'],reason=reason,exit_code=child.returncode,child_pid=child.pid,controller_pid=os.getpid(),owner='numerics_agent_2',cpu=49,nice=19,threads=1,argv=argv,request=a.request,request_sha256=a.request_sha256,review=a.review,review_sha256=a.review_sha256,adoption=a.adoption,adoption_sha256=a.adoption_sha256,method_manifest_sha256=q['method_manifest_sha256'],installation_sha256=installation_sha,script_sha256=m['files']['code/check_v01.py'],script_unchanged=unchanged,complete_source_record=complete,source_sha256=c.SOURCE_SHA,old_process_signals=0,own_child_signals=signals,storage_checks=samples,final_resources=final_resources,log_sha256=c.digest(lp),check_sha256=c.digest(cp) if cp.is_file() else None,bindings=bindings)
c.save(V/'execution_v01.json',record)
print(record['status'],record['finished_utc'],record['elapsed_seconds'],flush=True)
sys.exit(0 if record['status']=='COMPLETED' else 1)
