"""Recompute the finite source remainder values and record this runtime only."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,platform,ctypes,math
from fractions import Fraction
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import flint
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_angular/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
libc=ctypes.CDLL(None);libc.fegetround.restype=ctypes.c_int
before=libc.fegetround();assert before==0
z=np.load(E/'finite_arrays.npz',allow_pickle=False);ds=z['distinct_half_widths'];saved=z['remainder_arrays'];n=np.arange(1,262,dtype=float)
u=2.0**-53;succ=lambda x:np.nextafter(x,np.inf);new=[];count=0
for d in ds:
 row=[]
 for family,pref in enumerate([(2*n)**3,2*n+6*n**2+8*n**3+4*n**4]):
  # Python float exponentiation is the exact source operation here.
  h=float(d);rr=succ(pref*succ(h**3)/6*(1+16*u));row.append(rr)
  for j,x in enumerate(rr,1):
   exact=(8*j**3 if family==0 else 4*j**4+8*j**3+6*j*j+2*j)*Fraction(h)**3/6
   assert Fraction(float(x))>=exact;count+=1
 new.append(row)
new=np.asarray(new);assert new.shape==saved.shape==(8,2,261)
assert np.array_equal(new.view(np.uint64),saved.view(np.uint64)) and count==4176
after=libc.fegetround();assert after==before
# Record loaded libraries, including libm and the numerical extension binaries.
loaded={}
for line in Path('/proc/self/maps').read_text().splitlines():
 pieces=line.split(maxsplit=5)
 if len(pieces)==6 and pieces[5].startswith('/'):
  p=Path(pieces[5]);name=str(p)
  if p.is_file() and (name.endswith('.so') or '.so.' in name or 'python3.12' in name):loaded[name]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','finite_values':count,'bitwise_reproduction':True,'rounding_mode_before':before,'rounding_mode_after':after,'python':sys.version,'python_executable':sys.executable,'python_executable_sha256':sha(sys.executable),'platform':platform.platform(),'libc':platform.libc_ver(),'numpy_version':np.__version__,'flint_version':flint.__version__,'source_code_sha256':sha(__file__),'arrays_sha256':sha(E/'finite_arrays.npz'),'loaded_binary_sha256':loaded,'scope':'This verifier process and these4176 finite remainder values only. Does not establish historical numerics-lane runtime provenance, actual BLAS reduction paths, or universal libm correctness.'}
(E/'runtime_remainders.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k!='loaded_binary_sha256'}))
