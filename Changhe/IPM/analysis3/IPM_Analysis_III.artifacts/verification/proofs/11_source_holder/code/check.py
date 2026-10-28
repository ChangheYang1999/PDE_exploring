from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as S
A,a,sigma,beta=S.symbols('A a sigma beta',positive=True)
b=(A-1)/A;p=A/(A-1);q=a-(a-1)/A;r=b*sigma+1/A
checks={
 'crossover':(a-1)*b-(q-1),
 'first_sum':-q+b*(a-sigma)+r,
 'second_sum':-1+b*(1-sigma)+r,
 'packet_N_power':sigma+1/(A-1)+2*p+(a-A-2)/(A-1)-p*a+a-sigma-1,
 'packet_threshold':p*r-sigma-1/(A-1),
 'same_order_growth':p*sigma-sigma-1/(A-1)-(sigma-1)/(A-1),
 'ceiling_lambda_power':q+1+1/A+(a-A-2)/A-a,
 'low_input_N_power':a+1-(a-A-1)/A-(q+2),
 'low_input_lambda_power':1-a+(a-A-1)/A+q,
}
for name,value in checks.items():assert S.simplify(value)==0,(name,S.simplify(value))
A0=S.Rational(101507,10000);g0=S.Rational(119,4);a0=g0/(A0-1)
assert 1<a0<A0+1
root=Path(__file__).resolve().parents[1]
result={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'exact_identities':{k:'PASS' for k in checks},'illustration_only':{'A':str(A0),'g':str(g0),'a':str(a0),'q':str((1+g0)/A0)},'scope':'analytic exponent checks; illustrative rationals are not candidate certificates'}
(root/'evidence/check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
