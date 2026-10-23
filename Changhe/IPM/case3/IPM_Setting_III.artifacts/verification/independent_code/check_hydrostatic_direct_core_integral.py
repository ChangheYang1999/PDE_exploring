"""Result217 direct density-curvature integral cross-check, independent of primitive."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
import torch
from scipy.special import roots_jacobi,gamma
from independent_hydrostatic import CartesianQJet,finite_nodes
from q_local_checkpoint import QLocalCheckpoint
ROOT=Path('research/hydrostatic_axis_core_moment');V=ROOT/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def integral(gxx,p,Q,order,tail,R):
    t,w=finite_nodes(0.,R,order,.125)
    finite=float(np.dot(w*t,gxx(t)))-Q*R**p/p
    z,jw=roots_jacobi(tail,0.,-2*p);u=(z+1)/2;weights=jw*2**(2*p-1);s=R/u
    raw=s*gxx(s)-Q*s**(p-1)
    exterior=float(np.dot(weights,raw*R*u**(2*p-2)))
    return dict(value=finite+exterior,finite=finite,tail=exterior,order=order,tail_order=tail,split=R,largest_evaluation=float(s.max()))

def main():
    data=json.loads((V/'CHECKS.json').read_text());assert data['status']=='DONE'
    out=dict(utc_started=datetime.now(timezone.utc).isoformat(),proof_sha256=sha(ROOT/'INTEGRAL_PROOF.md'),code_sha256=sha(__file__),checks=[],manufactures=[],states=[])
    def check(name,passed,evidence=None):out['checks'].append(dict(name=name,passed=bool(passed),evidence=evidence));assert passed,name
    levels=[(32,128,8.),(48,256,32.),(64,384,128.),(88,640,512.)]
    for p in [.25,1/3,.4]:
        ref=-np.sqrt(np.pi)*gamma(-p/2)/(2*gamma((1-p)/2))
        rows=[integral(lambda t:(p-1)*t*(1+t*t)**((p-3)/2),p,p-1,*level)for level in levels]
        out['manufactures'].append(dict(p=p,expected=ref,levels=rows))
        check('manufactured radial moment p'+str(p),abs(rows[-1]['value']-ref)<1e-5,abs(rows[-1]['value']-ref))
    inputs=json.loads((V/'INPUTS.json').read_text())
    for state in data['states']:
        if 'm0'not in state['values'][-1]:continue
        tag=state['tag'];src=next(r['frozen']for r in inputs['states']if r['tag']==tag)
        with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(src)
        assert sha(src)==state['source_sha256'];jet=CartesianQJet(q)
        coeff=state['values'][-1];p=float(coeff['map_p']);Q=float(coeff['Q']);ref=float(coeff['m0'])
        rows=[integral(lambda t:jet.jet(0.,t)[:,3],p,Q,*level)for level in levels]
        for r in rows:r['difference_from_beta']=r['value']-ref
        out['states'].append(dict(tag=tag,source_sha256=sha(src),reference=ref,levels=rows,empirical_finest_difference=rows[-1]['value']-ref))
        (V/'DIRECT_INTEGRAL.json').write_text(json.dumps(out,indent=2)+'\n')
        print(tag,'beta',ref,'direct',[r['value']for r in rows],'difference',rows[-1]['difference_from_beta'],flush=True)
    out.update(status='DONE',utc_finished=datetime.now(timezone.utc).isoformat());(V/'DIRECT_INTEGRAL.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
