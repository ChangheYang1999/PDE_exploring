"""Independent sequential recomputation of selected producer tasks."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,sys,time
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/note14_certificate/producer_fine_a50'
sys.path.insert(0,str(B/'sources'))
import certify_note14 as C
from flint import arb,ctx

def stamp():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    d=json.loads((B/'n14_a12_c15_ff.json').read_text());ss=json.loads((B/'n14_a12_c15_ff.json.tasks.json').read_text());recs=ss['tasks'];audit=json.loads((B/'import_audit.json').read_text())
    for name,h in audit['sha256'].items():assert sha(R/name)==h
    selected=set()
    for kind,ids in audit['task_indices'].items():
        for k in range(13):selected.add(ids[(len(ids)-1)*k//12])
        selected.update(ids[:2]);selected.update(ids[-2:])
    for i in range(1,len(recs)):
        a,b=recs[i-1]['task'],recs[i]['task']
        if a['kind']!=b['kind'] or a['ntheta']!=b['ntheta']:selected.update([i-1,i])
    ctx.prec=320
    for category in {cat for rec in recs for cat in rec['errors']}:
        values=[(Q(str(arb(rec['errors'].get(category,'0')).upper().fmpq())),i) for i,rec in enumerate(recs)]
        selected.update(i for _,i in sorted(values,reverse=True)[:2])
    selected=sorted(selected);out=B/'selected_replays';out.mkdir(exist_ok=True)
    sources={str(p.relative_to(R)):sha(p) for p in [Path(__file__),B/'import_audit.json',B/'n14_a12_c15_ff.json.tasks.json',*[B/'sources'/n for n in d['source_sha256']]]}
    plan=dict(time_utc=stamp(),indices=selected,sha256=sources,selection='Endpoints, twelfths, both sides of every angular-count transition, and two largest contributions in each error category')
    pp=out/'plan.json'
    if pp.exists():old=json.loads(pp.read_text());assert old['indices']==selected and old['sha256']==sources
    else:pp.write_text(json.dumps(plan,indent=2)+'\n')
    print(stamp(),len(selected),'selected tasks',flush=True)
    for index in selected:
        op=out/f'task_{index:05d}.json'
        if op.exists():v=json.loads(op.read_text());assert v['verdict']=='EXACT_REPLAY_MATCH' and v['sha256']==sources;continue
        ctx.prec=80;rec=recs[index];tk=rec['task'];C.setup(tk['alpha_q'],tk['b_q'],tk['c_q'],tk['lam_q']);C.ERR.clear();edges=list(map(arb,tk['rho_edges']));total=arb(0);cells=0;started=time.monotonic()
        center=(arb(1),arb(0)) if tk['kind']=='near_e1' else (arb(1)/2,arb(0));nt=tk['ntheta']
        for lo,hi in zip(edges,edges[1:]):
            for k in range(nt):
                t0,t1=2*C.PI*k/nt,2*C.PI*(k+1)/nt
                if tk['kind']=='near_e1':val,n=C.polar_value(center,lo,hi,t0,t1,0,tk['maxdepth'],'near')
                else:val,n=C.m_cell(center,lo,hi,t0,t1,0,tk['maxdepth'])
                assert val.is_finite();total+=val;cells+=n
        actual=dict(mid=total.mid().str(30),rad=total.rad().str(10),cells=cells,errors={k:v.str(10,radius=True) for k,v in C.ERR.items()})
        assert actual=={k:rec[k] for k in actual},(index,actual,rec)
        result=dict(time_utc=stamp(),index=index,task=tk,actual=actual,exact_interval=dict(lower=str(total.lower().fmpq()),upper=str(total.upper().fmpq())),elapsed_seconds=time.monotonic()-started,sha256=sources,verdict='EXACT_REPLAY_MATCH')
        op.write_text(json.dumps(result,indent=2)+'\n');print(result['time_utc'],index,cells,round(result['elapsed_seconds'],3),'EXACT_REPLAY_MATCH',flush=True)
    hashes={str(p.relative_to(R)):sha(p) for p in [pp,*[out/f'task_{i:05d}.json' for i in selected]]}
    result=dict(time_utc=stamp(),task_count=len(selected),total_tasks=len(recs),indices=selected,cells=sum(recs[i]['cells'] for i in selected),sha256={**sources,**hashes},verdict='ALL_SELECTED_TASKS_MATCH',scope='Selected complete-task recomputations only; unsampled tasks were imported and audited structurally')
    (out/'completed.json').write_text(json.dumps(result,indent=2)+'\n');print(result['time_utc'],result['verdict'],result['task_count'],result['cells'],flush=True)
if __name__=='__main__':main()
