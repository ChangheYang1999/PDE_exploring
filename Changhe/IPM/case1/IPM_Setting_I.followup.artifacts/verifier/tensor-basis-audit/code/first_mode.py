from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inner-cutoff/code'));sys.path.insert(0,str(ROOT.parent/'center-moment/code'))
from hessian import tensor_coefficients
from certify import moment
ctx.prec=256;b=np.tile([1.,-1.],(3,1));co=tensor_coefficients(b);rt2=arb(2).sqrt()
assert all((co[i][j]-(rt2 if (i,j)==(0,1) else 0)).contains(0) for i in range(3) for j in range(2))
r=np.array([1.,-1.,1.]);b=1+np.outer(r-1,[1.,-1.])/8;assert np.all(b[0]==1)
c=moment(tensor_coefficients(b),arb(2),arb(6),arb(0));target=arb(6)/5-rt2/10;assert (c-target).contains(0)
out={'utc':datetime.now(timezone.utc).isoformat(),'angular_first_mode_target':rt2.str(50),'enclosure':co[0][1].str(50),'moment_target':'6/5-sqrt(2)/10','moment_enclosure':c.str(50),'all_targets_enclosed':True,'module_sha256':{str(p.relative_to(ROOT.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT.parent/'inner-cutoff/code/hessian.py',ROOT.parent/'center-moment/code/certify.py',ROOT.parent/'exact-data/code/nodal_input.py']},'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'verification/first_mode.json').write_text(json.dumps(out,indent=2)+'\n');print('FIRST_ANGULAR_MODE_PASS')
