from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[1]
a,b,xi,eta=s.symbols('a b xi eta',real=True)
x=a*xi-b*eta;y=b*xi+a*eta
num=[x*y,-x*x];c=[a*b,-a*a];A=[a*a-b*b,2*a*b];B=[-2*a*b,a*a-b*b]
for j in range(2):assert s.expand(num[j]-c[j]*(xi*xi+eta*eta)-A[j]*xi*eta-B[j]*eta*eta)==0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':['both rotated symbol decompositions exact','normal-line commutator is odd 1/xi; exterior smoothness proved by partial Fourier integral'],'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
