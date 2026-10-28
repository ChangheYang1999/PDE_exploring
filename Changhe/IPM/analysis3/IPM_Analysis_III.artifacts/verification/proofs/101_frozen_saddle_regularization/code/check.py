from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
k=Q(1615536043799051,9007199254740992)
A=2/k-1;D=4/k-1;S=A+D
beta=Q(24,5);lam=Q(31,10);s=Q(41,20);a=Q(17,4)
c=1+A*beta
kl=c+S/2-A*lam/2
ks=c+S/2-s*S
assert D==2*A+1
assert kl==1+(D-A)/2+a*A
assert (c+S/2)/S==Q(3,2)+Q(9,5)*A/S
assert ks>Q('0.97260878319')
assert 1/ks<Q('1.028164')
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'kappa_low_exact':str(kl),'kappa_high_exact':str(ks),'inverse_exact':str(1/ks),
 'kappa_high_float_diagnostic':float(ks),'inverse_float_diagnostic':float(1/ks),
 'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
