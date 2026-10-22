"""Exact all-basis linear strain maps and signed Laurent offsets; no cell evaluation."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[3];D=R/'research/inner_derivative_cells';E=D/'evidence';k=F(1615536043799051,9007199254740992);c=3/k-1;count=0;matrix=[]
for j in range(261):
 nu=2*j+1
 for which in ['eta','Deta']:
  eta=F(which=='eta');dt=F(which=='Deta');p={};q={}
  def add(d,f,v):
   if not v:return
   d[f]=d.get(f,F(0))+v
   if d[f]==0:del d[f]
  add(p,nu,dt/k-eta);add(p,nu+2,c*(nu*eta-dt)/2);add(p,abs(nu-2),(c/2 if nu==1 else -c/2)*(dt+nu*eta))
  def sine(f,v):add(q,abs(f),v if f>0 else -v)
  sine(nu,dt/k-eta)
  for f in [nu+2,nu-2]:sine(f,-c*dt/2)
  for f in [nu+2,2-nu]:sine(f,c*nu*eta/2)
  assert p==q and all(1<=f<=523 and f%2 for f in p);count+=262
  matrix.append({'j':j,'basis':which,'coefficients':{str(f):str(v) for f,v in sorted(p.items())}})
base=33;linear_positions=[]
for nu in range(1,524,2):
 for l in range(17):
  for sign in [-1,1]:
   original=(523+sign*nu)*base+l;shifted=520*base+original
   assert shifted==(1043+sign*nu)*base+l;linear_positions.append(shifted)
assert len(set(linear_positions))==len(linear_positions)==262*17*2
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
z={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_INNER_LINEAR_ANGULAR_MAP_CHECKS','linear_matrix_coefficients':count,'signed_Laurent_slots':len(linear_positions),'maximum_physical_primary_signed_shift':2086,'compressed_secondary_stride_count':1044,'radial_stride':33,'full_degree_bound':2086*33+32,'arb_source_sha256':sha(D/'code/engine_arb.py'),'iv_source_sha256':sha(D/'code/engine_iv.py'),'checker_source_sha256':sha(__file__),'matrix_sha256':hashlib.sha256(json.dumps(matrix,sort_keys=True).encode()).hexdigest(),'scope':'Exact finite angular algebra only; no numerical cell.'}
first=json.loads((E/'linear_angular_checks_initial.json').read_text())
for key in z:
 if key not in ['utc','checker_source_sha256']:assert z[key]==first[key],('initial replay mismatch',key)
z['initial_exact_replay_sha256']=sha(E/'linear_angular_checks_initial.json')
(E/'linear_angular_checks.json').write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z))
