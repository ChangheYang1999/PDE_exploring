"""Second exact derivation of n=111, directly from potential endpoint values.

The base chi's p-leading angular products cannot reach n=111 at this power;
the phi contribution is simply (c*p-1)*(-Delta phi) at its leading exponent.
"""
import json,sys
from pathlib import Path
from flint import fmpq as Q
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,C
e=Evaluator();n=111;p=Q(-11375183046454913,4076476460239181);beta=p+2
terms=[];potential=Q(0)
for kind,N,b,t,v,P in e.groups:
    if kind=='s'and N==n and n+2*b-2*v==beta:
        a=P(Q(1));potential+=a
        terms.append({'b':str(b),'t':str(t),'v':v,'endpoint_P1':str(a)})
rho=(n*n-beta*beta)*potential
coefficient=(C*p-1)*rho
reference=json.loads((HERE/'exact_far_result.json').read_text())['powers'][0]
expected=next(q for q in reference['coefficients']if q['n']==n)
assert coefficient==Q(expected['value'])
result={'status':'EXACT_INDEPENDENT_ENDPOINT_IDENTITY','n':n,'residual_power':str(p),'potential_power':str(beta),'potential_coefficient':str(potential),'rho_coefficient':str(rho),'residual_coefficient':str(coefficient),'float':float(coefficient),'terms':terms,'matches_convolution':True}
(HERE/'leading_mode_independent.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items()if k!='terms'},flush=True)
