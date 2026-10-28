"""Import producer task balls conservatively, without calling them replays."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,hashlib,json
from flint import arb,ctx
R=Path(__file__).resolve().parents[1]
B=R/'05_team_audit/note14_certificate/producer_fine_a50'
OLD=R/'05_team_audit/note14_certificate/sources_refined_0732'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ep(x,up=False):
    assert x.is_finite();return Q(str((x.upper() if up else x.lower()).fmpq()))
def strip_main(p):
    t=ast.parse(p.read_text());t.body=[x for x in t.body if not isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef)) or x.name!='main'];return ast.dump(t,include_attributes=False)
def main():
    ctx.prec=320;d=json.loads((B/'n14_a12_c15_ff.json').read_text());ss=json.loads((B/'n14_a12_c15_ff.json.tasks.json').read_text());hh=d['source_sha256']
    assert d['source_unchanged_during_run'] and hh==d['source_sha256_at_end']==ss['source_sha256_at_start']
    for n,h in hh.items():assert sha(B/'sources'/n)==h
    assert strip_main(B/'sources/certify_note14.py')==strip_main(OLD/'certify_note14.py')
    for n in ['certify_lb.py','zcurve.py']:assert sha(B/'sources'/n)==sha(OLD/n)
    assert (d['alpha'],d['b'],d['c'],d['lam'])==('1/2','3/4','-3/20','1000/1021') and d['prec_bits']==80
    p=d['params'];src={str(x.relative_to(R)):sha(x) for x in [Path(__file__),B/'PROOF.md',B/'n14_a12_c15_ff.json',B/'n14_a12_c15_ff.json.tasks.json',*[B/'sources'/n for n in hh]]}
    out=B/'imported_tasks';out.mkdir(exist_ok=True);tasks=[];cells=0;totals={k:[Q(0),Q(0)] for k in ['near','middle']};cursor={'near':Q(str(p['rho_min'])),'middle':Q(str(p['rho_m']))};indices={k:[] for k in cursor}
    for i,rec in enumerate(ss['tasks']):
        t=rec['task'];assert (t['alpha_q'],t['b_q'],t['c_q'],t['lam_q'])==(d['alpha'],d['b'],d['c'],d['lam']);assert t['maxdepth']==p['maxdepth']
        assert isinstance(t['ntheta'],int) and t['ntheta']>0 and t['ntheta']%2==0
        assert t['kind'] in ['near_e1','m_system'];kind='near' if t['kind']=='near_e1' else 'middle'
        ed=list(map(Q,t['rho_edges']));assert len(ed)>=2 and ed[0]==cursor[kind] and all(x<y for x,y in zip(ed,ed[1:]));cursor[kind]=ed[-1];indices[kind].append(i)
        m,rad=arb(rec['mid']),arb(rec['rad']);assert ep(rad)>=0
        lo,hi=ep(m)-ep(rad,True),ep(m,True)+ep(rad,True);assert lo<=hi;totals[kind][0]+=lo;totals[kind][1]+=hi
        assert isinstance(rec['cells'],int) and rec['cells']>=0;cells+=rec['cells']
        errors={}
        for k,v in rec['errors'].items():
            e=arb(v);assert ep(e)>=0;errors[k]={'lower':str(ep(e)),'upper':str(ep(e,True))}
        task=dict(kind=kind,edges=t['rho_edges'],ntheta=t['ntheta'],depth=t['maxdepth']);tasks.append(task)
        obj=dict(index=i,task=task,source_hashes=src,interval=dict(lower=str(lo),upper=str(hi)),cells=rec['cells'],errors=errors,provenance='Imported producer ball; not a verifier task replay')
        (out/f'task_{i:05d}.json').write_text(json.dumps(obj,indent=2)+'\n')
    assert cursor=={'near':Q(1,2),'middle':Q(str(p['rho_max']))};assert cells==d['cells'] and len(tasks)==4019
    assert indices['near']+indices['middle']==list(range(len(tasks)))
    params=dict(alpha=d['alpha'],b=d['b'],c=d['c'],lam=d['lam'],prec=d['prec_bits'],depth=p['maxdepth'],rho_min=p['rho_min'],rho_m=p['rho_m'],rho_max=p['rho_max'],delta=p['delta'])
    manifest=dict(time_utc=datetime.now(timezone.utc).isoformat(),params=params,source_hashes=src,tasks=tasks,provenance='Producer sidecar imported as conservative exact rational task intervals; selected replays separate')
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    summary=dict(time_utc=datetime.now(timezone.utc).isoformat(),task_count=len(tasks),cells=cells,task_indices=indices,totals={k:dict(lower=str(v[0]),upper=str(v[1])) for k,v in totals.items()},source_sha256=hh,sha256=src,verdict='IMPORT_AND_EXACT_COVERAGE_PASSED',scope='All serialized balls included; no independent replay claimed')
    (B/'import_audit.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary['time_utc'],summary['verdict'],len(tasks),'tasks',cells,'cells')
if __name__=='__main__':main()
