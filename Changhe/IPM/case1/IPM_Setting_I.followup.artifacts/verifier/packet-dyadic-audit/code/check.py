"""Exact algebra checks supporting the separately written dyadic proof."""
from pathlib import Path
import sympy as s
import json,hashlib,datetime
p=Path(__file__).resolve().parents[1]
A,g=s.symbols('A g',positive=True); x,r=s.symbols('xi r',positive=True)
q=2*(A-1); b=g/q; t=x/r**A; Phi=s.Function('Phi')
a=r**(-A-2)*(1+x*x/(r*r))**(-b)*Phi(t)
D=lambda f:A*x*s.diff(f,x)+r*s.diff(f,r)
checks={
 'characteristic_coordinate':s.simplify(D(t)),
 'frozen_fourier_equation':s.simplify(D(a)+(A+2+g*x*x/(x*x+r*r))*a),
 'high_frequency_density_degree':s.simplify(-1-q*b+(1+g)),
 'growth_exponent_gap_factorization':s.simplify(1-A*(1-q)-(2*A-1)*(A-1)),
}
j=s.symbols('j',integer=True)
checks['normalized_axis_trace_power']=s.simplify((1+g-j)/A+(j-1)/A-g/A)
assert all(v==0 for v in checks.values()),checks
v={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'exact_checks':{k:str(z) for k,z in checks.items()},'verdict':'PASS','scope':'Five symbolic identities only; analytic bounds and all quantifiers are proved in PROOF.md.'}
(p/'verification/algebra.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps(v,indent=2))
