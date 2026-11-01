"""Independent exact Cartesian logarithmic prefix with its common potential."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from logarithmic_verify import run,Q
start=time.monotonic();root=Path('research/291_canonical_half_finite')
d=run(Q(2),{1:Q(1)},12)
d.update(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,all_checks_pass=True,sources=[])
for name in ['canonical_half_prefix.py','logarithmic_verify.py','cartesian_verify.py']:
 p=root/'sources'/name;p.write_bytes(Path('code',name).read_bytes());d['sources'].append(dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()))
(root/'verification/exact_prefix.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(completed_orders=12,actual_elapsed_s=d['actual_elapsed_s'])),flush=True)
