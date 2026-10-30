from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,time
R=Path(__file__).resolve().parents[3];B=R/'research/dual_convergence_scope';start=time.monotonic();now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:sha256(p.read_bytes()).hexdigest()
pf=json.loads((B/'verification/PROOF_FIRST.json').read_text());assert not pf['checker_exists'];assert sha(B/'PROOF.md')==pf['proof_sha256']
m=json.loads((B/'source/MANIFEST.json').read_text());assert sha(B/'source/N3_NOTES.md')==m['sha256']
text=(B/'source/N3_NOTES.md').read_text();checks={
 'source_contains_two_basis_agreement':'converged to 12 digits under a 2.3-fold larger basis' in text,
 'source_contains_intrinsic_inference':'intrinsic slack of the mode-1 Hardy inequality for this profile' in text,
 'source_contains_basis_exclusion': 'not a basis defect' in text,
 'same_exact_projection_norm':Q(3,8)**2==Q(9,64),
 'exact_full_norm_square':Q(3,8)**2+Q(1,4)**2==Q(13,64),
 'full_norm_strictly_larger':Q(13,64)>Q(9,64),
 'full_norm_above_seven_sixteenths':Q(13,64)>Q(7,16)**2,
 'exact_orthogonal_remainder':Q(13,64)-Q(9,64)==Q(1,16)}
assert all(checks.values())
files=[B/'PROOF.md',B/'verification/PROOF_FIRST.json',B/'source/MANIFEST.json',B/'source/N3_NOTES.md',Path(__file__)]
inputs={str(p.relative_to(R)):sha(p) for p in files}
result={'utc':now(),'inputs':inputs,'checks':checks,'check_count':len(checks),'counterexample':{'space':'R3','V1':'span(e1)','V2':'span(e1,e2)','f':['3/8','0','1/4'],'squared_projection_norm':'9/64','squared_full_norm':'13/64'},'scope':'The inference from basis stability to certified omitted-component control is refuted. Actual candidate016 norm and strict Hardy slack remain unaffected.','elapsed_seconds':time.monotonic()-start,'verdict':'REFUTED as a certified inference; observed basis stability is numerical evidence only'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'utc':result['utc'],'checks':len(checks),'result_sha256':sha(B/'verification/result.json'),'elapsed_seconds':result['elapsed_seconds']}))
