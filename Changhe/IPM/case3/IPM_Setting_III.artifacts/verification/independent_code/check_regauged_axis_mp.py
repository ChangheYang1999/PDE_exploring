import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as Fr
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from q_local_checkpoint import QLocalCheckpoint
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf
root=Path('research/regauged_density_audit/verification');source=root/'AUDIT.json';d=json.loads(source.read_text());rows=[]
for precision in [50,80]:
 with mp.workdps(precision):
  for r in d['states']:
   q=QLocalCheckpoint(r['source']);cc=q.exact_coefficients();m=MPQDensity(cc,Fr(q.L),Fr(q.kappa),Fr(q.cl));a=mf(r['a']);l=mf(r['dilation_length'])
   for axis in ['x','y']:
    radius=mf(r['axis'][axis]['bracketed_crossing'])/l
    ratio=m.at(radius,mp.mpf(0))[2]/a if axis=='x' else m.at(radius,mp.pi/2)[0]/a
    rows.append(dict(N=q.N,axis=axis,precision=precision,ratio=mp.nstr(ratio,precision),half_residual=mp.nstr(ratio-mp.mpf('.5'),precision)))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();out=dict(utc=datetime.now(timezone.utc).isoformat(),status='COMPUTED',rows=rows,maximum_half_residual=max(abs(float(r['half_residual']))for r in rows),source_sha256=sha(source),code_sha256=sha(Path(__file__)),proof_sha256=sha(root.parent/'PROOF.md'),scope='Repeated precision at bracketed numerical crossings; not a first-root or interval certificate.')
(root/'AXIS_MP.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'}))
