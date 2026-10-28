from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
k=F(1615536043799051,9007199254740992);A=2/k-1;D=4/k-1;S=A+D
assert D==2*A+1 and S==3*A+1
threshold=lambda delta:F(3,2)+delta*A/S
old=threshold(F(3,2));counter=threshold(F(8,5));new=threshold(F(9,5))
assert old<2 and counter<F(21,10) and new>F(41,20)
assert F(25,4)>F(1,2)+F(9,5)*D/S
for de in (F(3,2),F(9,5)):
 assert 1+(3+de)*A+S/2==S*(F(3,2)+de*A/S)
 assert 1-(3+de)*D-S/2==S*(-F(5,2)-de*D/S)
 assert -de*D-S/2==S*(-F(1,2)-de*D/S)
r={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'threshold_delta_1_5':str(old),'counterexample_threshold_tau_0_1':str(counter),
 'threshold_delta_1_8':str(new),'epsilon_ceiling':str(2*A/S-F(1,2)),
 'diagnostics':{'old':float(old),'counter':float(counter),'new':float(new),'epsilon_ceiling':float(2*A/S-F(1,2))},
 'proof_sha256':hashlib.sha256((Path(__file__).resolve().parents[1]/'PROOF.md').read_bytes()).hexdigest()}
(Path(__file__).resolve().parents[1]/'evidence/check.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
