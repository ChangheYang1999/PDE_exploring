"""Verify archived inputs and raw/conversion equivalence using verifier reader only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import numpy as np
from q_checkpoint_reader import QCheckpoint
link=json.loads(Path('evidence/MANIFEST.json').read_text())
manifest_path=Path(link['latest']);d=json.loads(manifest_path.read_text())
checks=[]
def check_file(f,label):
 p=Path(f['path']);actual=hashlib.sha256(p.read_bytes()).hexdigest()
 assert actual==f['sha256'],(label,str(p),actual,f['sha256'])
 checks.append(dict(label=label,path=str(p),sha256=actual))
for row in d['code_snapshot']:check_file(row,'frozen_source')
for s in d['states']:
 check_file(s['file'],s['id'])
 if 'original_archive' in s:check_file(s['original_archive'],s['id']+'_raw')
 for k in ['metadata','result','independent_grid']:
  if k in s:check_file(s[k],s['id']+'_'+k)
 for f in s['diagnostics']:check_file(f,s['id']+'_diagnostic')
pairs=[]
for pair in d['raw_to_converted']:
 raw=QCheckpoint(pair['raw']['path']);converted=QCheckpoint(pair['converted']['path'])
 assert np.array_equal(raw.u,converted.u)
 for key in ['N','M','L','kappa','cl','mu','Lf']:
  assert getattr(raw,key)==getattr(converted,key),(key,pair)
 pairs.append(dict(raw=pair['raw']['sha256'],converted=pair['converted']['sha256'],coefficient_count=len(raw.u),binary_coefficient_and_parameter_equality=True))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',manifest=str(manifest_path),files_checked=len(checks),raw_conversion_pairs=pairs,checks=checks,scope='Artifact integrity and identical numeric input to the independent reader. Does not reproduce optimizer trajectories or certify continuum residuals.')
(manifest_path.parent/'integrity_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
