from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[3]
from sectors import sectors as slow
from sectors_flint import sectors as fast
path=ROOT/'research/baseline/data/state131_independent.json'
state=json.loads(path.read_text());start=time.monotonic()
a=slow(state,qmax=2);b=fast(state,qmax=2)
for i in (1,2,3):
 assert a[i].keys()==b[i].keys()
 for key in a[i]:
  expected={n:Fraction(str(x)) for n,x in b[i][key].items()}
  assert a[i][key]==expected,(i,key)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
     'exact_equality_all_potential_density_residual_sectors':True,'qmax':2,'elapsed_seconds':time.monotonic()-start}
(ROOT/'research/sector_audit/verification/accelerator_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(out,flush=True)
