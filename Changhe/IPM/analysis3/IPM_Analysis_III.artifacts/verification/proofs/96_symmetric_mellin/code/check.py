from sympy import symbols,I,simplify,conjugate
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
sig,xi,n,N,a=symbols('sig xi n N a', real=True)
Ap=lambda s,v:(s+I*xi-v)/(s+I*xi+v+2)
Am=lambda s,v:(s+I*xi+v)/(s+I*xi-v+2)
z=N+I*xi
Fa=(a*a+N*N+xi*xi)/(a*a-z*z)
assert simplify((Ap(a-1,N-1)+conjugate(Am(a-1,N+1)))/2-Fa)==0
f=lambda v:(I*xi-v)/(I*xi+v)
assert simplify(Fa-f(N)-2*a*a*N/(z*(a*a-z*z)))==0
assert simplify(f(N)-(f(N-1)+f(N+1))/2+2*I*xi/(z*(z*z-1)))==0
assert simplify(Ap(sig,n)-f(n)-2*((sig+1)*n-I*xi)/((sig+I*xi+n+2)*(I*xi+n)))==0
assert simplify(Am(sig,n)-(I*xi+n)/(I*xi-n)+2*((sig+1)*n+I*xi)/((sig+I*xi-n+2)*(I*xi-n)))==0
p=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','arithmetic':'exact symbolic','checks':['shifted adjoint at n+2','symmetric full-family rational coefficient','midpoint first-order cancellation','central-average second-order cancellation','both full-minus-principal symbols'],'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(o['date'],o['status'])
