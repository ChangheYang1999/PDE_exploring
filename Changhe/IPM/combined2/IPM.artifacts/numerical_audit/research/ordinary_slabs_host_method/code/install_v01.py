"""Install one already admitted ordinary-slab host method, without launching it."""
from pathlib import Path
import argparse,os,shutil,time
import common_v01 as c
p=argparse.ArgumentParser();c.add_arguments(p);a=p.parse_args()
R=Path.cwd().resolve();C=R.parent
assert R.name=='numerics_agent_2';c.environment(49)
tick=time.monotonic();start=c.stamp();q,m,bindings=c.authenticate(C,a)
assert c.moment(c.stamp())<c.moment(q['no_new_after'])
assert c.digest(Path(__file__))==m['files']['code/install_v01.py']
assert c.digest(Path(c.__file__))==m['files']['code/common_v01.py']
resources=c.usage(R);processes=c.processes(R,[os.getpid()])
assert q['lane_cap_bytes']-resources['lane_bytes']>=q['min_start_reserve_bytes']
assert resources['filesystem_free_bytes']>=q['min_filesystem_free_bytes']
assert not processes['conflicts'] and processes['host_rss_bytes']<q['max_host_rss_bytes']
D=c.named(R,q['method_directory']);assert not D.exists() and not D.is_symlink()
assert not c.named(R,q['output']).exists()
D.mkdir(parents=True);src=c.named(C,m['source_directory']);copies={}
for name,h in m['files'].items():
 target=c.named(D,name);target.parent.mkdir(parents=True,exist_ok=True)
 with c.named(src,name).open('rb') as inp,target.open('xb') as out:shutil.copyfileobj(inp,out)
 assert c.digest(target)==h;copies[str(target.relative_to(R))]=h
contract=D/'contract';contract.mkdir()
for name,path,h in [('request',a.request,a.request_sha256),('review',a.review,a.review_sha256),('adoption',a.adoption,a.adoption_sha256),('method_manifest',q['method_manifest'],q['method_manifest_sha256'])]:
 target=contract/(name+'_v01.json')
 with c.named(C,path).open('rb') as inp,target.open('xb') as out:shutil.copyfileobj(inp,out)
 assert c.digest(target)==h;copies[str(target.relative_to(R))]=h
assert c.recheck(C,bindings)
record=dict(schema='ordinary-slab-host-installation-v1',status='INSTALLED_NOT_STARTED',started_utc=start,finished_utc=c.stamp(),elapsed_seconds=time.monotonic()-tick,owner='numerics_agent_2',cpu=49,method_manifest_sha256=q['method_manifest_sha256'],request=a.request,request_sha256=a.request_sha256,review=a.review,review_sha256=a.review_sha256,adoption=a.adoption,adoption_sha256=a.adoption_sha256,bindings=bindings,copies=copies,initial_resources=resources,initial_processes=processes,scope='Authenticated installation only. No source reconstruction executed.')
c.save(D/'installation_v01.json',record)
print(record['status'],record['finished_utc'],c.digest(D/'installation_v01.json'),flush=True)
