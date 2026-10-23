"""Adaptive Gauss-Kronrod resolution of four printed velocity discrepancies."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']: os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,traceback
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from adaptive_hydrostatic_velocity import AdaptiveVerticalVelocity
R=Path('research/hydrostatic_velocity_sequence_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def dump(q): (V/'ADAPTIVE.json').write_text(json.dumps(q,indent=2)+'\n')
checks=[]
def ck(name,b,e=None): checks.append(dict(name=name,passed=bool(b),evidence=e))
ref=json.loads((V/'REFINEMENT.json').read_text())
assert ref['status']=='PASS' and all(q['passed'] for q in ref['checks']), 'Prior heavy job must finish first'
gate=json.loads((V/'ADAPTIVE_MANUFACTURE.json').read_text())
assert gate['status']=='PASS' and all(q['passed'] for q in gate['checks'])
ck('manufacture module binding',gate['module_sha256']==sha('independent_code/adaptive_hydrostatic_velocity.py'))
ck('manufacture proof binding',gate['proof_sha256']==sha(R/'WITNESS_PROOF.md'))
ck('manufacture checker binding',gate['driver_sha256']==sha('independent_code/check_adaptive_hydrostatic_velocity.py'))
selected={'hsG_c2.0_N96_log':[27,30,216],'hsG_c2.0_N128_log_cont':[27,30,35],'hsG_c2.0_N192_log':[180]}
raw=json.loads((V/'RUN.json').read_text());coords=raw['states'][0]['levels'][-1]['points']
inputs=json.loads((V/'INPUTS.json').read_text())
items={x['tag']:x for x in inputs['states']}
out=dict(status='RUNNING',started_utc=utc(),pid=os.getpid(),proof_sha256=sha(R/'WITNESS_PROOF.md'),driver_sha256=sha(__file__),raw_sha256=sha(V/'RUN.json'),refinement_sha256=sha(V/'REFINEMENT.json'),gate_sha256=sha(V/'ADAPTIVE_MANUFACTURE.json'),module_sha256=sha('independent_code/adaptive_hydrostatic_velocity.py'),selection=selected,states=[],checks=checks)
dump(out)
try:
    for tag,indices in selected.items():
        item=items[tag];ck('coefficient hash '+tag,sha(item['state']['path'])==item['state']['sha256'])
        with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
            q=QLocalCheckpoint(item['state']['path'])
        jet=CartesianQJet(q)
        inv=AdaptiveVerticalVelocity(jet.jet,q.p,split=37,epsabs=2e-11,epsrel=2e-11)
        row=dict(tag=tag,p=q.p,status='RUNNING',points=[]);out['states'].append(row)
        for index in indices:
            point=coords[index]
            print('START',tag,index,utc(),flush=True)
            value=inv.at(point['x'],point['y'])
            row['points'].append(dict(index=index,x=point['x'],y=point['y'],r=point['r'],**value))
            ck(tag+' finite '+str(index),np.isfinite(value['V']).all() and np.isfinite(value['estimated_error']).all())
            ck(tag+' no quadrature warnings '+str(index),not value['messages'],value['messages'])
            out['updated_utc']=utc();dump(out)
            print('DONE',tag,index,'V',value['V'],'errors',value['estimated_error'],'messages',len(value['messages']),utc(),flush=True)
        row.update(status='DONE',finished_utc=utc());dump(out)
    out.update(status='PASS' if all(q['passed'] for q in checks) else 'FAIL',finished_utc=utc(),count=len(checks));dump(out);print(out['status'],len(checks),flush=True)
except Exception:
    out.update(status='ERROR',finished_utc=utc(),traceback=traceback.format_exc());dump(out);raise
