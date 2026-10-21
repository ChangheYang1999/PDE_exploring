from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
b,A,g,delta=s.symbols('b A g delta',positive=True)
checks={
 'critical_cancellation':s.simplify((2-b-g/A).subs({b:2/A,g:2*A-2})),
 'integration_by_parts':s.simplify(s.diff(delta**(b-2),delta,2)+(g/A)*s.diff(delta**(b-3),delta)-(3-b)*(2-b-g/A)*delta**(b-4)),
 'smooth_exponential_error_weight':s.simplify(delta**(2-b)*delta**(b-2)-1),
 'quadratic_error_weight':s.simplify(delta**(3-2*b)*delta**(b-2)-delta**(1-b)),
}
assert all(v==0 for v in checks.values()),checks
out={'date':datetime.now(timezone.utc).isoformat(),'checks':{k:str(v) for k,v in checks.items()},'result':'PASS','scope':'Algebra only, estimate requires the complete proof and independent review','proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
