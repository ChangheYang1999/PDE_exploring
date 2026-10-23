from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,numpy as np
from q_local_checkpoint import QLocalCheckpoint
root=Path('research/dynamic_local_reconstruction/verification/stored_nodes');root.mkdir(parents=True,exist_ok=True)
N=6;M=3;tk=-np.cos(2*np.pi*np.arange(N+1)/(2*N+1));tk[1]+=.0001;u=np.arange(sum(N+1-k for k in range(M)),dtype=float)/17
params=dict(N=N,M=M,L=1.,p=1.5,cl=3.,basis='local',u=u)
np.savez(root/'manufacture.npz',**params,tk=tk);np.savez(root/'fallback.npz',**params)
a=QLocalCheckpoint(root/'manufacture.npz');b=QLocalCheckpoint(root/'fallback.npz');assert np.array_equal(a.tk,tk)
t=np.array([-.9,-.1,.7]);z=(2*t-1-tk[1])/(1-tk[1]);reference=np.polynomial.chebyshev.chebval(z,a.coeff[1]);err=max(abs(reference-a.polynomial(1,t)));assert err<1e-13
assert max(abs(a.polynomial(1,t)-b.polynomial(1,t)))>1e-5
a.save_snapshot(root/'roundtrip.npz');c=QLocalCheckpoint(root/'roundtrip.npz');assert np.array_equal(a.tk,c.tk) and np.array_equal(a.rho(t,.7),c.rho(t,.7))
np.savez(root/'invalid.npz',**params,tk=tk[::-1])
try:QLocalCheckpoint(root/'invalid.npz')
except ValueError:pass
else:raise AssertionError('Invalid nodes accepted')
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=6,reference_error=err,changed_field_max=float(max(abs(a.polynomial(1,t)-b.polynomial(1,t)))),reader_sha256=hashlib.sha256(Path('independent_code/q_local_checkpoint.py').read_bytes()).hexdigest())
(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
