"""Search identity allocations using the exact marginal transportation LP.
Only floating quadrature diagnostics are produced.
"""
from pathlib import Path
from datetime import datetime,timezone
from local_circle_lp_diagnostic import evaluate
import json,time,numpy as np
start=time.monotonic();rows=[]
for p in [.2,.35,.5,.7]:
 for j in [0,8,12,16,24,32]:
  val=evaluate(.5,j*np.pi/32,n=64,nr=40,power=p)
  # The omitted near interval [0,1e-7] has atom mass .5*(2e-7)^p.
  atom=.5*(2e-7)**p
  row=dict(alpha=.5,power=p,phase_index=j,local_cost=val,omitted_atom_mass=atom,local_plus_omitted_atom=val+atom);rows.append(row);print(row,flush=True)
Path('data/diagonal_allocation_diagnostic.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,elapsed_seconds=time.monotonic()-start,status='Numerical diagnostics, no certificate'),indent=2)+'\n')
