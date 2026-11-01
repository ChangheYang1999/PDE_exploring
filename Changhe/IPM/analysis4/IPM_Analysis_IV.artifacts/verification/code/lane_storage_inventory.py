"""Read-only lane inventory with relative paths and unique-inode accounting."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,shutil
seen=set();files=logical=unique=allocated=0;large=[]
for base,dirs,names in os.walk('.'):
 for name in names:
  p=Path(base)/name
  try:st=p.stat()
  except FileNotFoundError:continue
  if not p.is_file():continue
  files+=1;logical+=st.st_size;key=(st.st_dev,st.st_ino)
  if key not in seen:
   seen.add(key);unique+=st.st_size;allocated+=st.st_blocks*512
   if st.st_size>1000000:large.append(dict(path=str(p),bytes=st.st_size,allocated=st.st_blocks*512))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),files=files,logical_bytes=logical,unique_bytes=unique,unique_allocated_bytes=allocated,shared_free_bytes=shutil.disk_usage('.').free,largest=sorted(large,key=lambda x:x['bytes'],reverse=True)[:20])
Path('artifacts/storage/inventory_latest.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='largest'}))
