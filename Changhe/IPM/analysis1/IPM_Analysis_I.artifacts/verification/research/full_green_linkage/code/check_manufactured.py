"""Exact polynomial reference fixtures and finite/rounding fault tests."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
import importlib.util,json,hashlib,math
from fractions import Fraction as F
from datetime import datetime,timezone
p=Path(__file__).with_name('check_boundaries.py');sp=importlib.util.spec_from_file_location('boundary_checker',p);b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
q=lambda v:b.qa(v)
ref=lambda p,x:sum((c*x**j for j,c in enumerate(p)),F(0))
polys=[[F(j==d) for j in range(8)] for d in range(8)]+[[F((-1)**j*(j+1),j+2) for j in range(8)]]
count=0
for rate in (0,2,-2,-6,-518,-526):
 for y in polys:
  force=[((j+1)*y[j+1] if j<7 else F(0))-rate*y[j] for j in range(8)]
  pp=b.particular([q(v) for v in force],-rate,1)
  for u in (F(0),F(1,10000),F(1,1000),F(1,100),F(199,10000)):
   expected=ref(y,u)
   va=b.horner(pp,q(u))+b.expa(rate,u)*(q(y[0])-b.horner(pp,q(0)))
   vi=b.propagated(b.qi(y[0]),[b.qi(v) for v in force],rate,u)
   for value in (va,vi):
    lo,hi=b.ends(value);assert lo<=expected<=hi,(rate,u,expected,lo,hi)
   count+=1
translated=0
for y in polys:
 for rate in (0,2,-2,-518):
  force=[((j+1)*y[j+1] if j<7 else F(0))+rate*y[j] for j in range(8)]
  h=F(199,10000);mid=h/2
  midpoint=[sum((force[k]*F(math.comb(k,j))*mid**(k-j) for k in range(j,8)),F(0)) for j in range(8)]
  backward=b.endpoint_poly([b.qi(v) for v in midpoint],h/2,True)
  for u in (F(0),h/3,h):
   vi=b.propagated(b.qi(ref(y,h)),[-v for v in backward],rate,u)
   lo,hi=b.ends(vi);expected=ref(y,h-u);assert lo<=expected<=hi
   translated+=1
faults=[]
for value in ('inf','-inf','nan'):
 for engine in ('arb','iv'):
  try:b.ends(b.arb(value) if engine=='arb' else b.iv.mpf(value))
  except (AssertionError,ValueError):faults.append(engine+':'+value)
  else:raise AssertionError(('nonfinite accepted',engine,value))
assert len(faults)==6
cases=[((F(0),F(1),F(0),F(1)),'CONTAINED'),((F(0),F(0),F(0),F(0)),'CONTAINED'),((F(-1),F(1),F(0),F(1)),'OVERLAP_ONLY'),((F(1),F(2),F(0),F(1)),'OVERLAP_ONLY'),((F(1)+F(1,2**1074),F(2),F(0),F(1)),'DISJOINT')]
for args,status in cases:assert b.classification(*args)==status
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_DIAGNOSTIC_ONLY','manufactured_polynomial_solutions':count,'engine_enclosures_checked':2*count,'backward_translated_enclosures':translated,'nonfinite_faults_rejected':faults,'exact_comparison_cases':len(cases),'checker_sha256':b.sha(p),'source_sha256':b.sha(Path(__file__)),'scope':'Analytic polynomial fixtures and deliberate failures. No canonical Green artifact membership claimed.'}
(b.E/'manufactured.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
