from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[3];B=R/'research/candidate007_weighted_laplacian'
def H(p):return sha256(p.read_bytes()).hexdigest()
man=B/'verification/manifest.json';diag=B/'source/N1_007_weaktests_float.json';code=B/'source/N1_weak_tests.py'
m=json.loads(man.read_text());d=json.loads(diag.read_text());modes=m['modes'];N=180
assert modes==list(range(1,320,2)) and max(modes)<2*N
assert 'midpoint 180' in d['rule'] and 'angular_midpoint(ANG)' in code.read_text()
assert d['sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
assert m['inputs']['research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json']=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
files=[man,diag,code,B/'ANGULAR_RULE.md',Path(__file__),R/'research/angular_resolution/PROOF.md']
out=B/'verification/angular_rule.json';assert not out.exists()
out.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'angular_modes':len(modes),'largest_mode':max(modes),'midpoint_nodes':N,'exact_square_rule':True,'scope':'Ideal angular rule only; no certification of floating samples, radial quadrature or full norm','inputs':{str(p.relative_to(R)):H(p) for p in files}},indent=2)+'\n')
print(H(out))
