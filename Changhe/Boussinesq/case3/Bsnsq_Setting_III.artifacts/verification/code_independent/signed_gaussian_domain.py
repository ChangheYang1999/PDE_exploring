"""Short own exact-source stationary-point and time-budget diagnostic."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,math
import numpy as np
from scipy.optimize import root
from signed_gaussian_feedback import SignedGaussianFlow,cases,ROOT
start=time.monotonic();data=list(cases().values())
for p in (ROOT/'sources_later').glob('*.json'):
 doc=json.loads(p.read_text())
 if 'results' in doc:data += [{'data':r,'file':str(p)} for r in doc['results']]
data=[q for q in data if q['data'].get('unfinished',0)]
out={'started_utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((ROOT.parent/'PROOF.md').read_bytes()).hexdigest(),'cases':[]}
for d in data:
 r=d['data'];g=SignedGaussianFlow(r['c_in'],r['lobes']);found=[]
 for x in [0.,.2,.7,1.5,3.,5.,8.,12.]:
  for y in [-10.,-6.,-3.,-1.,0.,1.,2.,3.,4.,6.,10.]:
   sol=root(lambda X:g.field(X)[1],[x,y],jac=lambda X:g.field(X)[3],tol=1e-11)
   z=np.asarray(sol.x);z[0]=abs(z[0]);norm=float(np.linalg.norm(g.field(z)[1]))
   if norm<1e-8 and np.linalg.norm(z)<100 and all(np.linalg.norm(z-q['point'])>1e-5 for q in found):
    D=g.field(z)[3];found.append({'point':z.tolist(),'residual_norm':norm,'determinant':float(np.linalg.det(D)),'eigenvalues':[[float(e.real),float(e.imag)] for e in np.linalg.eigvals(D)]})
 tests=[]
 for point in [[.1,1.],[1.,1.],[2.,3.],[4.,4.],[1.,-4.],[20.,10.],[1e3,1e3],[1e8,1e8]]:
  ans=g.evaluate(point,r_in=1e-3,rtol=2e-9,max_time=80.)
  tests.append({'point':point,**ans})
 out['cases'].append({'case':r['case'],'num_unfinished':r['unfinished'],'num_steps':r['steps'],'roots':found,'trajectory_tests':tests})
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(ROOT/'domain_diagnostics.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
for r in out['cases']:print(r['case'],'ROOTS',r['roots'],'TIMES',[(q['point'],q['status'],q['T']) for q in r['trajectory_tests']],flush=True)
print(out['started_utc'],out['ended_utc'],out['elapsed_seconds'])
