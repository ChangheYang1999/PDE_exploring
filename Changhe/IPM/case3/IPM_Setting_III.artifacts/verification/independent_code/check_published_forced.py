"""Read raw forced states and independently reconstruct their center moment."""
from pathlib import Path
from datetime import datetime,timezone
import json
from candidate_reader import Candidate
from candidate_moments import strain
sources=[Path('../numerics/artifacts/data/rf_s1_cl1.5_b4_N96M48.pt'),Path('../numerics/artifacts/data/rf_s1_cl3_b4_N96M48.pt'),Path('../numerics/runs/rf_s1_cl3.0_N96M48.pt')]
folder=Path('evidence/published_forced');folder.mkdir(parents=True,exist_ok=True)
rows=[]
for path in sources:
 if not path.exists():raise FileNotFoundError(path)
 c=Candidate(path,project_center=True)
 snapshot=folder/(path.stem+'.npz');c.save_snapshot(snapshot)
 reread=Candidate(snapshot,project_center=True)
 assert reread.meta['mu']==c.meta['mu'] and reread.meta['beta']==c.meta['beta']
 checks=[strain(c,n,256,1e-16,16.) for n in (128,256,512)]
 last=checks[-1]
 row={'utc':datetime.now(timezone.utc).isoformat(),'source':c.meta,'snapshot':str(snapshot),'checks':checks,'forced_jet_defect':last['a0']*last['cl_plus_c_minus_one']-c.meta['mu'],'first_radial_mean_jet':float(c.endpoint_t_jets(1)[1,0])}
 rows.append(row);print(json.dumps(row),flush=True)
(folder/'center_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
