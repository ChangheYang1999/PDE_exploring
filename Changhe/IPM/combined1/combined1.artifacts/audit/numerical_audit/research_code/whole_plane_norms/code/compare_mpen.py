"""Compare the independent exact Mpen2 G0/G1 computations with N3."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3];ctx.prec=2048;start=time.monotonic()
peerpath=ROOT/'research/whole_plane_norms/data/N3_Mpen2_target.json'
peer=json.loads(peerpath.read_text());src=ROOT/'research/refit_audit/data/Mpen2_canonical.json'
canonical=json.loads(src.read_text())
assert canonical['source_sha256']==peer['source_sha256']
assert canonical['canonical_serialization_sha256']==peer['canonical_sha256']
rows=[]
def sha(p):return sha256(p.read_bytes()).hexdigest()
for label in ['G0','G1']:
 path=ROOT/f'research/whole_plane_norms/verification/Mpen2_{label}_ball_2048.json'
 own=json.loads(path.read_text());other=peer['norms'][label]
 assert own['source_sha256']==sha(src) and own['status']==other['status']=='FINITE'
 a,b=arb(own['norm_lower_ball']),arb(own['norm_upper_ball'])
 checks={'lower':a.overlaps(arb(other['norm_lower'])),'upper':b.overlaps(arb(other['norm_upper']))}
 assert all(checks.values())
 rows.append({'component':label,'own_norm_lower_ball':own['norm_lower_ball'],'own_norm_upper_ball':own['norm_upper_ball'],
 'comparison':checks,'own_sha256':sha(path),'own_elapsed_seconds':own['total_elapsed_seconds']})
 print(label,own['norm_lower_ball'],'both_comparisons_pass',flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':sha(src),
 'original_generator_sha256':canonical['source_sha256'],'canonical_serialization_sha256':peer['canonical_sha256'],
 'peer_sha256':sha(peerpath),'code_sha256':sha(Path(__file__)),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'research/whole_plane_norms/verification/Mpen2_N3_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
