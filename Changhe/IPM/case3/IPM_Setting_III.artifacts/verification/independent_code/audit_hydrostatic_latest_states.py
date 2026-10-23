"""Result219: sequential complete-plane hydrostatic quadrature refinement.
Only independently written modules are imported; producer checkpoints are numeric inputs.
"""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,sys,contextlib,traceback
import numpy as np
import torch
import audit_hydrostatic_states as base
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet,VerticalInverse
from hydrostatic_power_tail import PowerVerticalInverse

ROOT=Path('research/hydrostatic_latest_state_audit');V=ROOT/'verification'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,obj):Path(p).write_text(json.dumps(obj,indent=2)+'\n')
def compare(a,b):
    assert len(a)==len(b)
    rows=[]
    for x,y in zip(a,b):
        assert (x['x'],x['y'])==(y['x'],y['y'])
        row=dict(x=x['x'],y=x['y'],r=x['r'])
        for key in ('V1','V2','R','R_Nf','R_Nv'):
            row['delta_'+key]=y[key]-x[key] if x[key] is not None and y[key] is not None else None
        rows.append(row)
    maxima={}
    for key in ('V1','V2','R','R_Nf','R_Nv'):
        valid=[r for r in rows if r['delta_'+key] is not None]
        maxima[key]=max(valid,key=lambda r:abs(r['delta_'+key])) if valid else None
    return dict(maximum_pointwise_changes=maxima,points=rows)

def main():
    assert json.loads(Path('research/hydrostatic_axis_core_moment/verification/CHECKS.json').read_text())['status']=='DONE','Result217 remains the sole heavy job'
    gate=json.loads(Path('research/hydrostatic_power_tail_inverse/parent_regression/verification/GATE.json').read_text())
    assert gate['status']=='PASS' and gate['evaluator_sha256']==sha('independent_code/independent_hydrostatic.py')
    powergate=json.loads(Path('research/hydrostatic_power_tail_inverse/verification/GATE.json').read_text())
    assert powergate['status']=='PASS' and powergate['module_sha256']==sha('independent_code/hydrostatic_power_tail.py')
    inputs=json.loads((V/'INPUTS.json').read_text());base.root=V
    files=[Path(__file__),Path(base.__file__),ROOT/'PROOF.md',Path('independent_code/independent_hydrostatic.py'),Path('independent_code/q_local_checkpoint.py'),Path('independent_code/hydrostatic_power_tail.py')]
    pipe=dict(status='RUNNING',utc_started=utc(),pid=os.getpid(),input_sha256=sha(V/'INPUTS.json'),code_and_proof_sha256={str(p):sha(p)for p in files},states=[])
    def checkpoint():pipe['utc_updated']=utc();write(V/'PIPELINE.json',pipe)
    checkpoint()
    for item in inputs['states']:
        tag=item['tag'];assert sha(item['frozen'])==item['sha256'];start=time.monotonic()
        entry=dict(tag=tag,status='BASE_RUNNING',utc_started=utc());pipe['states'].append(entry);checkpoint()
        print(utc(),tag,'BASE START',flush=True)
        with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
            base.state(tag,'all')
            q=QLocalCheckpoint(item['frozen'])
        raw=json.loads((V/(tag+'.json')).read_text());assert raw['status']=='DONE' and raw['source_sha256']==item['sha256']
        jet=CartesianQJet(q);previous=raw['samples'];assert len(previous)==774
        result=dict(tag=tag,status='RUNNING',source_sha256=item['sha256'],base_result_sha256=sha(V/(tag+'.json')),levels=[],comparisons=[])
        def save():write(V/(tag+'.refined.json'),result)
        chosen={(0.,0.),(.137,.219),(.5,.5),(0.,3.),(6.,8.),(30.,40.)}
        for table in raw['regions'].values():
            for key in ('R','R_Nf','R_Nv'):
                if key in table:chosen.add((table[key]['x'],table[key]['y']))
        previous_label='linear baseline20/112/64'
        for method,order,tail,split in [('linear',40,320,512.),('linear',64,512,2048.),('power',40,128,32.),('power',64,192,128.)]:
            level=dict(method=method,order=order,tail_order=tail,split=split,inner_scale=.125,points=[])
            cls=VerticalInverse if method=='linear'else PowerVerticalInverse
            result['levels'].append(level);inv=cls(jet.jet,q.p,order,tail,split,.125)
            level['center']=inv.center();level['center_error']=abs(level['center']-raw['exact']['cH_float'])
            for i,point in enumerate(raw['samples']):
                level['points'].append(base.point_record(jet.jet,inv,q.cl,point['x'],point['y']))
                if i%100==0:save();print(utc(),tag,order,i+1,'/774',flush=True)
            level['regions']=base.sample_summary(level['points'])
            comparison=compare(previous,level['points']);label=f'{method} {order}/{tail}/{split}';comparison.update(from_setting=previous_label,to_setting=label)
            result['comparisons'].append(comparison);previous=level['points'];previous_label=label
            for table in level['regions'].values():
                for key in ('R','R_Nf','R_Nv'):
                    if key in table:chosen.add((table[key]['x'],table[key]['y']))
            save();print(utc(),tag,'LEVEL DONE',order,'center error',level['center_error'],flush=True)
        result['witnesses']=[]
        for method,cls,order,tail,split in [('linear',VerticalInverse,88,768,4096.),('power',PowerVerticalInverse,88,256,512.)]:
            inv=cls(jet.jet,q.p,order,tail,split,.125)
            witness=dict(method=method,order=order,tail_order=tail,split=split,inner_scale=.125,center=inv.center(),points=[])
            for x,y in sorted(chosen):witness['points'].append(base.point_record(jet.jet,inv,q.cl,x,y))
            result['witnesses'].append(witness);save()
        result.update(status='DONE',utc_finished=utc(),seconds=time.monotonic()-start);save()
        entry.update(status='DONE',utc_finished=utc(),seconds=result['seconds'],base_sha256=sha(V/(tag+'.json')),refined_sha256=sha(V/(tag+'.refined.json')));checkpoint()
        print(utc(),tag,'DONE',result['seconds'],flush=True)
    pipe.update(status='DONE',utc_finished=utc());checkpoint();print(utc(),'ALL DONE',flush=True)

if __name__=='__main__':main()
