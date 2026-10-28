from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
k=Q(1615536043799051,9007199254740992)
A=2/k-1;D=4/k-1;S=A+D;delta=Q(9,5)
b=Q(9,4);lam=2*delta-Q(1,2);a=D*delta
kap=D*lam/2+S*(b-Q(1,2))-a
kap2=Q(3,2)*S-a
assert kap==1+(D-A)/2+Q(17,4)*A
assert kap2>0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'kappa_low_exact':str(kap),'kappa_2_exact':str(kap2),
 'kappa_2_float_diagnostic':float(kap2),'normal_inverse_float_diagnostic':float(1/kap2),
 'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
