"""Run the small top-mode audit after the core17 equation audit."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
p=Path('/proc/2009385/cmdline')
while p.exists() and b'three_fifths_high_order_audit.py' in p.read_bytes():time.sleep(20)
with Path('scratch/three_fifths_top_mode_bounds.log').open('wb') as log:
    result=subprocess.run([sys.executable,'-B','code/three_fifths_top_mode_bounds.py'],stdout=log,stderr=subprocess.STDOUT)
print(json.dumps(dict(returncode=result.returncode,time=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
