"""Exact reference tests for the separately implemented Taylor audit."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json
p=Path(__file__).with_name('audit_boundaries.py');sp=importlib.util.spec_from_file_location('third_method',p);a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
count=0
for degree in range(8):
 y=[F(j==degree) for j in range(8)]
 for rate in (0,2,-2,-6,-518,-526):
  forcing=[a.aq(((j+1)*y[j+1] if j<7 else F(0))-rate*y[j]) for j in range(8)]
  for u in (F(0),F(1,1000),F(1,100),F(199,10000)):
   value,tail=a.taylor_solution(a.aq(y[0]),forcing,rate,u);lo,hi=a.endpoints(value);expected=u**degree;assert lo<=expected<=hi and tail>=0;count+=1
assert a.arb(0).is_zero()
faults=0
for v in ('inf','-inf','nan'):
 try:a.endpoints(a.arb(v))
 except (AssertionError,ValueError):faults+=1
 else:raise AssertionError(('nonfinite accepted',v))
assert faults==3
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_DIAGNOSTIC_ONLY','third_method_exact_polynomial_cases':count,'nonfinite_cases_rejected':faults,'arb_bits':a.ctx.prec,'Taylor_degree':a.K,'auditor_source_sha256':a.sha(p),'source_sha256':a.sha(Path(__file__)),'scope':'Exact polynomial fixtures for the separate third method, not canonical data membership.'}
(a.E/'third_manufactured.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
