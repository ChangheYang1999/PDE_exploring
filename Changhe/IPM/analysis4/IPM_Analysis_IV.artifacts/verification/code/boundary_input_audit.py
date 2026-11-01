"""Replay one selected boundary input using the frozen certified prefix."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gc,gzip,json,pickle,random,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from stream_precision_audit import unpack
ROOT=Path('research/217_boundary_sensitivity_audit')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(p,obj):
    q=p.with_name(p.name+'.new');q.write_text(json.dumps(obj,indent=2)+'\n');q.replace(p)
def main():
    started=time.monotonic()
    mp=Path('research/82_weighted_loss_criterion/update_N329_20261031T093225Z/verification/input_manifest.json')
    manifest=json.loads(mp.read_text());sp=Path(manifest['input_path']);raw=gzip.decompress(sp.read_bytes())
    assert len(raw)==manifest['raw_bytes'] and sha256(raw).hexdigest()==manifest['raw_sha256']
    old=pickle.loads(raw);del raw
    pp=Path('../a4-num/ckpt/log_sin1_c3_pert329.pkl');raw=pp.read_bytes()
    meta=dict(path=str(pp),sha256=sha256(raw).hexdigest(),bytes=len(raw));sample=pickle.loads(raw);del raw
    assert max(old['f'])==329 and max(sample['f'])>=340
    assert all((s['A'],s['B'],s['ring'],s['prec'])==('2','3','arb',512) for s in [old,sample])
    for key in ['f','g']:sample[key]={n:sample[key][n] for n in old[key]}
    gc.collect();rng=random.Random(20261031)
    counts=dict(coefficients=0,chosen_endpoints=0,exact_input_points=0,interval_input_enclosures=0,positive_signs=0,negative_signs=0)
    largest_input_relative_radius=arb(0);examples=[]
    for key in ['f','g']:
        for n,cols in old[key].items():
            assert len(cols)==len(sample[key][n])
            for q,col in enumerate(cols):
                assert len(col)==len(sample[key][n][q])
                for j,v in enumerate(col):
                    ctx.prec=512
                    loaded=arb(*unpack(v))
                    radius=loaded.rad();mid=loaded.mid();sign=0
                    if not radius.is_zero():
                        sign=1 if rng.random()<0.5 else -1
                        counts['chosen_endpoints']+=1
                        counts['positive_signs' if sign>0 else 'negative_signs']+=1
                    ctx.prec=2048
                    target=mid+sign*radius
                    if not target.is_exact():
                        ctx.prec=4096;target=mid+sign*radius
                    assert target.is_exact(),(key,n,q,j,'endpoint not exact')
                    actual=arb(*unpack(sample[key][n][q][j]))
                    assert actual.contains(target),(key,n,q,j,'selected endpoint absent')
                    counts['coefficients']+=1
                    if actual.is_exact():counts['exact_input_points']+=1
                    else:
                        counts['interval_input_enclosures']+=1
                        if len(examples)<3:examples.append(dict(field=key,n=n,q=q,j=j,sign=sign,target=str(target),actual=str(actual)))
                        if not actual.mid().is_zero():largest_input_relative_radius=largest_input_relative_radius.max(actual.rad()/abs(actual.mid()))
            if n%50==0:print(json.dumps(dict(stage='input_replay',field=key,completed_order=n,counts=counts,time=stamp(),elapsed_s=time.monotonic()-started)),flush=True)
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,seed=20261031,source_manifest=dict(path=str(mp),sha256=sha256(mp.read_bytes()).hexdigest()),perturbed_source=meta,counts=counts,largest_input_relative_radius=largest_input_relative_radius.str(30,radius=True),nonzero_radius_examples=examples,scope='Every intended endpoint of the reloaded certified input is enclosed; this is one selected configuration, not a bound over the whole input box.',actual_elapsed_s=time.monotonic()-started)
    put(ROOT/'verification'/'input_replay.json',result)
    for name in ['boundary_input_audit.py','stream_precision_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(result),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        d=dict(checked_at_utc=stamp(),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification'/'input_FAILURE.json',d);print(json.dumps(d),flush=True);raise SystemExit(1)
