"""Independent additional quadrature at all claimed velocity comparison maxima."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,traceback
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_power_tail import PowerVerticalInverse
R=Path('research/hydrostatic_velocity_sequence_audit')
V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def dump(p,q): Path(p).write_text(json.dumps(q,indent=2)+'\n')
g=json.loads((V/'RUN.json').read_text())
assert g['status']=='PASS' and all(c['passed'] for c in g['checks'])
items={s['tag']:s for s in g['states']}
coords=np.array([[q['x'],q['y'],q['r']] for q in g['states'][0]['levels'][-1]['points']])
arrays={tag:np.array([q['V'] for q in s['levels'][-1]['points']]) for tag,s in items.items()}
selected={tag:set(36*k+j for k in range(7) for j in [0,8]) for tag in items}
selections=[]
for c in [2,3]:
    tags=sorted([t for t,s in items.items() if s['c']==c],key=lambda t:int(re.search(r'_N(\d+)',t)[1]))
    for a,b in zip(tags,tags[1:]):
        d=arrays[a]-arrays[b]
        for method,rd in [('nominal',coords[:,2]),('hypot',np.hypot(coords[:,0],coords[:,1]))]:
            w=(1+rd)**(1/c)
            for reg,lo,hi in [('inner',0,.1),('subunit',.1,1),('annulus',1,100),('far',100,10001)]:
                ii=np.flatnonzero((rd>=lo)&(rd<hi))
                ix=[int(ii[np.argmax(abs(d[ii,j])/w[ii])]) for j in [0,1]]
                ix += [int(ii[np.argmax(np.linalg.norm(d[ii],axis=1))])),int(ii[np.argmax(np.linalg.norm(arrays[b][ii],axis=1))]))]
                selected[a].update(ix);selected[b].update(ix)
                selections.append(dict(old=a,new=b,mask=method,region=reg,indices=ix,count=len(ii)))
for q in json.loads((V/'AXIS_DIAGNOSTIC.json').read_text()):
    if not q['agrees']: selected[q['tag']].add(q['index'])
checks=[]
def ck(n,b,e=None): checks.append(dict(name=n,passed=bool(b),evidence=e))
out=dict(status='RUNNING',started_utc=utc(),pid=os.getpid(),proof_sha256=sha(R/'WITNESS_PROOF.md'),driver_sha256=sha(__file__),raw_sha256=sha(V/'RUN.json'),input_sha256=sha(V/'INPUTS.json'),code_sha256={name:sha(Path('independent_code')/name) for name in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','hydrostatic_power_tail.py']},selection=selections,selected={t:sorted(ii) for t,ii in selected.items()},states=[],checks=checks)
dump(V/'REFINEMENT.json',out)
try:
    inputs=json.loads((V/'INPUTS.json').read_text())
    for item in inputs['states']:
        tag=item['tag'];ck('input '+tag,sha(item['state']['path'])==item['state']['sha256'])
        with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
            q=QLocalCheckpoint(item['state']['path'])
        jet=CartesianQJet(q)
        row=dict(tag=tag,p=q.p,status='RUNNING',levels=[])
        out['states'].append(row)
        for order,tail,split in [(88,320,512),(128,512,1024)]:
            inv=PowerVerticalInverse(jet.jet,q.p,order=order,tail_order=tail,tail_scale=split)
            level=dict(order=order,tail_order=tail,split=split,points=[]);row['levels'].append(level)
            for j,index in enumerate(sorted(selected[tag])):
                x,y,r=coords[index]
                val=inv.at(float(x),float(y))
                level['points'].append(dict(index=index,x=float(x),y=float(y),r=float(r),**val))
                if j%15==0:
                    out['updated_utc']=utc();dump(V/'REFINEMENT.json',out)
                    print('PROGRESS',tag,order,j+1,'/',len(selected[tag]),utc(),flush=True)
            ck(tag+' finite '+str(order),all(np.isfinite(q['V']).all() for q in level['points']))
            ck(tag+' parity '+str(order),all((q['x']!=0 or q['V'][0]==0) and (q['y']!=0 or q['V'][1]==0) for q in level['points']))
        row.update(status='DONE',finished_utc=utc());dump(V/'REFINEMENT.json',out)
    out.update(status='PASS' if all(q['passed'] for q in checks) else 'FAIL',finished_utc=utc(),count=len(checks));dump(V/'REFINEMENT.json',out);print(out['status'],len(checks),flush=True)
except Exception:
    out.update(status='ERROR',finished_utc=utc(),traceback=traceback.format_exc());dump(V/'REFINEMENT.json',out);raise
