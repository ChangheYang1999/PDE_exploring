from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
import json, time, sys
sys.set_int_max_str_digits(0)
b=Path(__file__).resolve().parents[1]
source=b.parent/'basis_rank_audit/source/canonical007.json'
start=time.perf_counter(); raw=source.read_bytes()
assert sha256(raw).hexdigest()=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
j=json.loads(raw); gamma=Q(2251799813685248,4076476460239181);delta=1-gamma
amp=defaultdict(Q)
for key,v in zip(j['order'],j['coefficients']):
 jj,m,k=map(int,key);amp[jj,m]+=Q(v)
rows=[]
for jj in range(8):
 e=1-(jj+1)*delta;d=3+e
 value=-amp[jj,0]*d*d*(d-2)+amp[jj,1]*(d*d-4)*d/2
 assert value!=0
 rows.append({'j':jj,'exponent':str(e),'first_sine_exact':str(value),'first_sine_float':float(value),'nonzero':True})
mat=[[Q(z**k-1) for k in range(1,5)] for z in (2,3,4,5)]
det=Q(1)
for i in range(4):
 pivot=mat[i][i];assert pivot;det*=pivot
 for r in range(i+1,4):
  q=mat[r][i]/pivot
  for cc in range(i,4):mat[r][cc]-=q*mat[i][cc]
assert det!=0
cuts=[4*gamma-2,3*gamma-1,2*gamma,1+gamma]
assert Q(0)<cuts[0]<cuts[1]<cuts[2]<cuts[3]
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,
 'source_sha256':sha256(raw).hexdigest(),'proof_sha256':sha256((b/'PROOF.md').read_bytes()).hexdigest(),
 'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'branches':rows,
 'dimension_thresholds':list(map(str,cuts)),'thresholds_float':list(map(float,cuts)),
 'vandermonde_determinant':str(det),'checks':'all8 first harmonics nonzero; exact threshold order; nonzero4x4 determinant'}
(b/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='branches'},indent=2))
for row in rows:print(row['j'],row['first_sine_float'])
