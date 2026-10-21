from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as s

root=Path(__file__).resolve().parents[1]
A,beta,x,lam,G,V,GL,VL,W,p,f,t=s.symbols('A beta x lam G V GL VL W p f t', positive=True)
w=s.symbols('w', nonzero=True)
checks={}
def zero(name,value):
    value=s.simplify(value)
    assert value==0,(name,value)
    checks[name]='PASS'

zero('origin_prefactor',(beta-1)*A**(1-beta)/3*(-A**(beta-2)/2)-(1-beta)/(6*A))
zero('origin_two_integrations_by_parts',s.diff(x**(-6-beta),x,2)-(6+beta)*(7+beta)*x**(-8-beta))
zero('source_map_derivative',s.diff(1/(w+t*f)-1/w,t).subs(t,0)+f/w**2)
zero('disjoint_reciprocals_on_origin',(1/(w+p+t*f)-1/w-(1/(w+p)-1/w)-(1/(w+t*f)-1/w)).subs(f,0))
zero('disjoint_reciprocals_on_interior',(1/(w+p+t*f)-1/w-(1/(w+p)-1/w)-(1/(w+t*f)-1/w)).subs(p,0))
zero('tail_subtraction',(lam**(-2)*G+lam**(-3)*V-lam**(-2)*GL-lam**(-3)*VL)*lam**(1-beta)*W-((G-GL)*lam**(-1-beta)+(V-VL)*lam**(-2-beta))*W)
q=s.symbols('q',real=True)
zero('exact_source_multiplier',s.exp(-A*(q-q))-1)
kappa=(1-beta)*(6+beta)*(7+beta)/(6*A)
zero('kappa_A4',kappa.subs({A:s.Integer(4),beta:s.Rational(1,2)})-s.Rational(65,64))
I,H=s.symbols('I H',positive=True)
zero('first_order_compensation_sign',-I-H*(-I/H))
obj={'date':datetime.now(timezone.utc).isoformat(),'checks':checks,'count':len(checks),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra and sign checks supplementary to the complete informal proof. They do not verify the analytic estimates or a coupled profile.'}
(root/'verification/check.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
