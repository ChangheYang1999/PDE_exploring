"""Run grid audit, budget inventory, and tail certificates serially on core 17."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,shutil,subprocess,sys,time
p=Path('/proc/2910482/cmdline')
while p.exists() and b'after_sample_queue.py' in p.read_bytes():time.sleep(20)
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def run(script,args,label):
    print(json.dumps(dict(utc=stamp(),event='start',job=label)),flush=True)
    with Path('scratch',label+'.log').open('wb') as log:
        r=subprocess.run([sys.executable,'-B','code/'+script+'.py']+args,stdout=log,stderr=subprocess.STDOUT)
    print(json.dumps(dict(utc=stamp(),event='exit',job=label,code=r.returncode)),flush=True)
    return r.returncode==0
if not run('modular_grid_audit',[],'modular_grid_audit'):raise SystemExit(1)
logical=unique=files=0;seen=set()
for root,dirs,names in os.walk('.'):
    for name in names:
        path=Path(root,name)
        if path.is_symlink():continue
        stat=path.stat();logical+=stat.st_size;files+=1;inode=(stat.st_dev,stat.st_ino)
        if inode not in seen:seen.add(inode);unique+=stat.st_size
row=dict(checked_at_utc=stamp(),files=files,logical_bytes=logical,unique_inode_bytes=unique,filesystem_free_bytes=shutil.disk_usage('.').free)
Path('artifacts/storage/inventory_after_modular.json').write_text(json.dumps(row,indent=2)+'\n')
print(json.dumps(row),flush=True)
if logical>2_990_000_000 or row['filesystem_free_bytes']<20_000_000_000:raise SystemExit('Storage margin too small for new tail certificates.')
for Q in [4,5,6]:
    for index in range(1,7):
        args=['--periods',str(Q),'--roots',str(index)]
        if not run('integer_period_tail_radii',args,f'integer_tail_Q{Q}_root{index}'):raise SystemExit(1)
        if not run('integer_period_tail_replay',args,f'integer_tail_replay_Q{Q}_root{index}'):raise SystemExit(1)
