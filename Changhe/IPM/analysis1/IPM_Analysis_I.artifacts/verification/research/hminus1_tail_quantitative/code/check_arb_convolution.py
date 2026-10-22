"""Exact rational input tests of the Arb Laurent convolution wrapper.
No JavaScript/TypeScript, servers, RLScience, Lean/Lake, or outside writes.
These tests supplement the algebraic proof and complete output audit.
"""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,importlib.util
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('arb_candidate',D/'code/engine_arb.py')
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
M.ctx.prec=512;M.ctx.threads=1
cases=count=0
for t in range(64):
 def make(seed,n,shift):
  result={}
  for j in range(n):
   if (j+seed)%4==0:continue
   c=Q((seed*11+j*17)%53-26,2+(seed+j)%19)
   r=Q((seed+3*j)%7,13+2*j) if t%2 else Q(0)
   result[j+shift]=(c-r,c+r)
  if not result:result[shift]=(Q(0),Q(0))
  return result
 x=make(t,1+t%11,-13+t%7);y=make(65-t,1+t%9,-3-t%5)
 exact={}
 for i,(a,b) in x.items():
  for j,(c,d) in y.items():
   terms=(a*c,a*d,b*c,b*d);lo,hi=exact.get(i+j,(Q(0),Q(0)))
   exact[i+j]=(lo+min(terms),hi+max(terms))
 actual=M.cv({i:M.a(a).union(M.a(b)) for i,(a,b) in x.items()},
             {i:M.a(a).union(M.a(b)) for i,(a,b) in y.items()})
 for i in set(actual)|set(exact):
  lo,hi=exact.get(i,(Q(0),Q(0)));z=actual[i]
  assert M.ep(z.lower())<=lo<=hi<=M.ep(z.upper()),(t,i)
  count+=1
 cases+=1
out={'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_EXACT_RATIONAL_ARB_WRAPPER_TESTS_ONLY',
 'cases':cases,'output_boxes_checked':count,
 'engine_sha256':hashlib.sha256((D/'code/engine_arb.py').read_bytes()).hexdigest(),
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'method':'Independent exact rational interval multiplication, signed sparse translated Laurent supports, point and interval inputs.',
 'scope':'Finite wrapper tests. Full theorem also requires analytic argument, complete finite output audit and review.'}
(D/'evidence/arb_convolution_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
