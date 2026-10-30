from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,time
from flint import arb,ctx
base=Path(__file__).resolve().parents[1]
ctx.prec=768;start=time.monotonic()
def digest(p):return sha256(p.read_bytes()).hexdigest()
cover_path=base/'verification/d2_signed_cover.json';cover=json.loads(cover_path.read_text())
assert cover['all_pass'] and not cover['pending'] and cover['complete_partition']
assert cover['code_sha256']==digest(base/'code/certify.py')
assert cover['proof_sha256']==digest(base/'PROOF.md')
assert all(r['pass'] and arb(r['schur_lower'])>=0 for r in cover['accepted'])
background_path=base/'source/T4_d2_background.json';bg=json.loads(background_path.read_text())
c=arb(4076476460239181)/2251799813685248;kappa=arb(bg['gradient_HS_norm'])
rate=c+1-arb(2)/25-kappa
assert rate>arb('2.0199')
record={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'d2','complete':True,
        'accepted_cells':len(cover['accepted']),'source_cover_cells':len(json.loads((base/'source/N4_L2_cover.json').read_text())['accepted']),
        'refinement_count':len(cover['refined']),
        'minimum_certified_schur_margin':min(arb(r['schur_lower']).lower() for r in cover['accepted']).str(70),
        'cover_sha256':digest(cover_path),'proof_sha256':digest(base/'PROOF.md'),
        'code_sha256':digest(Path(__file__)),'background_sha256':digest(background_path),
        'theta_upper':'2/25','kappa':kappa.str(70),'signed_L2_rate_lower':rate.str(70),
        'rate_greater_than_2_0199':True,'rate_greater_than_2':bool(rate>2),
        'cover_elapsed_seconds':cover['elapsed_seconds'],'postprocess_elapsed_seconds':time.monotonic()-start}
(base/'verification/SUMMARY.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
