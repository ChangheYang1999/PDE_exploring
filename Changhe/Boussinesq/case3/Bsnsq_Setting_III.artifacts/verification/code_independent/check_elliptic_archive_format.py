from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
import numpy as np
sys.path.insert(0,str(Path('code_independent').resolve()))
from r2_state_values import R2State
root=Path('verification/elliptic_cartesian_20261021T1336Z');m=json.loads((root/'manifest.json').read_text());rows=[]
for item in m['states']:
 p=root/item['snapshot'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'];s=R2State(p)
 checks={'basis_exponent_gt_one':s.bb>1,'length_positive':s.L>0,'degree_five':s.degree==5,'simple_interior_edges':bool(np.all(np.diff(s.edges)>0)),'clamp_zero_six':bool(np.all(s.knots[:6]==0) and s.knots[6]>0),'clamp_one_six':bool(np.all(s.knots[-6:]==1) and s.knots[-7]<1),'all_coefficients_finite':bool(np.isfinite(s.rawF).all() and np.isfinite(s.rawG).all()),'coefficient_dimensions':s.rawG.size==s.K*(s.Nt+5)}
 for k in range(s.K):
  checks[f'G_mask_{k}']=bool(np.all(s.Gs.c[:k//2,k]==0));checks[f'F_mask_{k}']=bool(np.all(s.Fs.c[:k//2,k]==0))
 assert all(checks.values())
 rows.append({'label':item['label'],'sha256':item['sha256'],'beta':s.beta,'b':s.bb,'K':s.K,'Nt':s.Nt,'L':s.L,'degree':s.degree,'checks':checks,'all_passed':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'states':rows,'all_passed':True,'count':sum(len(r['checks']) for r in rows)}
Path('research/171_independent_elliptic_residual_audit/verification/archive_format.json').write_text(json.dumps(out,indent=2)+'\n');print(out['count'],'format checks PASS')
