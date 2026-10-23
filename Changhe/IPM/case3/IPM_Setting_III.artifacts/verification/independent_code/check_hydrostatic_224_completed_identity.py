import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,traceback
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
R=Path('research/hydrostatic_c2_resolved_224_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):
 checks.append({'name':n,'passed':bool(b)})
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);a=sha(p)
 if h:ck('binding '+str(p),a==h)
 bindings[str(p)]=a
 return p
out={}
try:
 for p in [Path(__file__),R/'COMPLETED_ARTIFACT_IDENTITY_PROOF.md','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
 g=json.loads(bind(V/'SOURCE_GATE.json','4634b43d4d696aa56e558f5aeecb41cafe6fe1ab35aface615621cf9350cb538').read_text());ck('source16PASS',g['count']==len(g['checks'])==16 and g['status']=='PASS' and all(z['passed'] for z in g['checks']));raw=bind(g['frozen'],g['source_sha256'])
 run=Path('../numerics/runs/hsG_c2.0_N224_log.pt');pub=Path('../numerics/artifacts/data/hs/hsG_c2.0_N224_log.pt');a=run.read_bytes();b=pub.read_bytes();c=run.read_bytes();ck('stable and published complete bytes',a==b==c);h=hashlib.sha256(a).hexdigest();ck('announced completed hash',h=='fd0bc052d8a5eb54d759cb4c29cbcaf2983d92c94e13eabc953503a131abc632')
 frozen=V/'hsG_c2.0_N224_log.completed.pt'
 if frozen.exists():ck('retained completed bytes',frozen.read_bytes()==a)
 else:frozen.write_bytes(a)
 bind(frozen,h)
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(raw);z=QLocalCheckpoint(frozen)
 for name in ['N','M','basis']:ck('exact discrete '+name,getattr(q,name)==getattr(z,name))
 for name in ['L','kappa','cl','p','eta']:ck('exact scalar '+name,Fraction(getattr(q,name))==Fraction(getattr(z,name)))
 for name in ['u','tk']:
  x,y=getattr(q,name),getattr(z,name);ck('shape '+name,x.shape==y.shape);ck('dtype '+name,x.dtype==y.dtype);ck('exact numeric bytes '+name,x.tobytes()==y.tobytes());ck('finite '+name,np.isfinite(x).all() and np.isfinite(y).all())
 ck('11060 coefficient entries',len(q.u)==sum(q.N+1-k for k in range(q.M))==11060);ck('stored nodes both files',q.meta['basis_nodes_source']==z.meta['basis_nodes_source']=='stored');ck('fixed c2 map',q.N==224 and q.M==56 and q.kappa==q.cl==2.)
 out.update(status='PASS',complete_source={'run':str(run),'published':str(pub),'frozen':str(frozen),'sha256':h,'bytes':len(a)},raw_source={'frozen':str(raw),'sha256':sha(raw)},equal_definition_fields=['N','M','basis','u','tk','L','kappa','cl'],metadata={'raw':q.meta,'complete':z.meta},additional_complete_keys=sorted(set(z.data)-set(q.data)))
except BaseException:out.update(status='FAIL',traceback=traceback.format_exc())
finally:
 out.update(utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Exact represented density identity only. Completed diagnostic numbers not accepted or substituted for independent289 evaluation. Full-planeUNRESOLVED.')
 (V/'COMPLETED_IDENTITY.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc']);print(out.get('traceback',''))
raise SystemExit(out['status']!='PASS')
