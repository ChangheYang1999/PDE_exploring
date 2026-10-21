from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
A,g,I,t=s.symbols('A g I t',positive=True);beta=2/A;gs=2*A-2
K=(1-beta)*(3-beta)*(2-beta-g/A)/(6*A*g**(beta+2))
checks={
 'exceptional_coefficient':s.simplify(K.subs(g,gs)),
 'exceptional_derivative':s.simplify(s.diff(K,g).subs(g,gs)+(1-beta)*(3-beta)/(6*A**2*gs**(beta+2))),
 'sequence_limit':s.simplify(s.diff(K,g).subs(g,gs)*A*gs*I+(1-beta)*(3-beta)*I/(6*A*gs**(beta+1))),
}
b=s.symbols('b',positive=True);delta=s.symbols('delta',positive=True);v=s.Function('v')(delta)
# Adjoints of d_delta^2 and -(g/A)/delta*d_delta against delta^(beta-2).
coeff=s.diff(delta**(b-2),delta,2)+(g/A)*s.diff(delta**(b-3),delta)
checks['integration_by_parts_coefficient']=s.simplify(coeff-(3-b)*(2-b-g/A)*delta**(b-4))
# Exact interior logarithmic derivative with respect to t at t=0.
w,h=s.symbols('w h',nonzero=True)
checks['interior_source_log_derivative']=s.simplify(s.diff(-A*(1/(w+t*h)-1/w),t).subs(t,0)-A*h/w**2)
assert all(v==0 for v in checks.values()),checks
out={'date':datetime.now(timezone.utc).isoformat(),'checks':{k:str(v) for k,v in checks.items()},'result':'PASS','scope':'Exact algebra only; uniform estimates and sequence argument are in PROOF.md and require independent review','proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
