"""Third-method exact interval tests of the outward integer convolution.
No JS/TS, servers, RLScience, Lean/Lake; writes only this lane.
Finite tests supplement the algebraic proof and are not full output closure.
"""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,importlib.util
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('candidate_iv',D/'code/engine_iv.py');M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M);M.iv.dps=180
# Deterministic exact rational endpoint construction: negative, positive,
# sign-crossing, nonbinary endpoints, missing indices and translated support.
def make(t,n,shift):
 out={}
 for j in range(n):
  if (t+j)%5==0:continue
  p=Q(((t+3)*(j+7))%41-20,3+2*((t+j)%13));r=Q((7*t+3*j)%11,7+2*((t+2*j)%17));out[j+shift]=(p-r,p+r)
 if not out:out[shift]=(Q(0),Q(0))
 return out
def exact_cv(x,y):
 d={}
 for j,(a,b) in x.items():
  for k,(c,e) in y.items():
   z=[a*c,a*e,b*c,b*e];l,h=d.get(j+k,(Q(0),Q(0)));d[j+k]=(l+min(z),h+max(z))
 return d
count=0
for t in range(96):
 x=make(t,1+t%9,-7+t%5);y=make(97-t,1+t%8,-11+t%7)
 xb={j:M.bound(*v) for j,v in x.items()};yb={j:M.bound(*v) for j,v in y.items()}
 # The interval method can be wider than ordinary interval multiplication,
 # but must contain that exact full independent interval evaluation.
 result=M.cv(xb,yb);reference=exact_cv(x,y)
 for j,(lo,hi) in reference.items():
  ll,hh=map(M.ep,result[j]._mpi_);assert ll<=lo<=hi<=hh,(t,j);count+=1
 for j in set(result)-set(reference):
  ll,hh=map(M.ep,result[j]._mpi_);assert ll<=0<=hh
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FINITE_EXACT_RATIONAL_CONVOLUTION_TESTS_ONLY','cases':96,'output_boxes_checked':count,'method':'Full independent exact rational interval multiplication and accumulation against outward512bit integer convolution; nonbinary inputs and sparse translated supports','engine_sha256':hashlib.sha256((D/'code/engine_iv.py').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Not a full H2 output audit, no theorem closure or model acceptance.'}
(D/'evidence/integer_convolution_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
