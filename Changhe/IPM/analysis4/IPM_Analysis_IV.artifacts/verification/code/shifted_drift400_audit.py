"""Directed multiplier fits on saved coefficient intervals, without NumPy."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,pickle,re,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from stream_precision_audit import unpack,dyadic
from certified_initial_majorants import pack
ROOT=Path('research/254_reset400_conditional_audit')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x):return x.str(42,radius=True)
def put(path,data):
    tmp=path.with_name(path.name+'.new');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(path)
def fit(xs,ys):
    count=len(xs);assert count==len(ys) and count>1
    xm=sum(xs,arb(0))/count;ym=sum(ys,arb(0))/count
    den=sum(((x-xm)**2 for x in xs),arb(0));assert den>0
    slope=sum(((x-xm)*(y-ym) for x,y in zip(xs,ys)),arb(0))/den
    intercept=ym-slope*xm
    rms=(sum(((y-intercept-slope*x)**2 for x,y in zip(xs,ys)),arb(0))/count).sqrt()
    return dict(slope=text(slope),intercept=text(intercept),rms=text(rms),slope_ball=pack(slope),intercept_ball=pack(intercept))
def main():
    start=time.monotonic();ctx.prec=768
    path=Path('../a4-num/ckpt/log_sin1_c3_from329.pkl');raw=path.read_bytes();metadata=dict(path=str(path),sha256=sha256(raw).hexdigest(),bytes=len(raw));state=pickle.loads(raw);del raw
    assert (state['A'],state['B'],state['ring'],state['prec'])==('2','3','arb',512)
    assert max(state['f'])>=400
    oldpath=Path('research/215_shifted_multiplier_growth/verification/drift_fit_checks.json');old=json.loads(oldpath.read_text());assert old['all_checks_pass']
    oldrows={(r['n'],r['field']):r for r in old['rows']}
    cache={};rows=[];zero=arb(0);comparisons=0
    def vector(field,n):
        key=field,n
        if key not in cache:cache[key]={(q,j):arb(*unpack(v)) for q,col in enumerate(state[field][n]) for j,v in enumerate(col) if any(v)}
        return cache[key]
    for n in range(348,401):
        for field,label in [('f','F'),('g','G')]:
            prev=vector(field,n-3);current=vector(field,n)
            aa=sum((v*v for v in prev.values()),zero);bb=sum((v*v for v in current.values()),zero)
            ab=sum((v*current.get((q,j+1),zero) for (q,j),v in prev.items()),zero)
            assert aa>0 and bb>0
            a=ab/aa;e2sq=1-ab*ab/(aa*bb);assert e2sq>0
            e2=e2sq.sqrt();ratio=(bb/aa).sqrt();assert (abs(a)/(1-e2*e2).sqrt()).overlaps(ratio)
            if (n,label) in oldrows:
                prior=oldrows[n,label]
                assert a.overlaps(arb(prior['multiplier_display']))
                assert e2.overlaps(arb(prior['relative_l2_display']))
                comparisons+=2
            rows.append(dict(n=n,field=label,multiplier=pack(a),multiplier_display=text(a),relative_l2=pack(e2),relative_l2_display=text(e2),norm_ratio_display=text(ratio),log_abs_multiplier=pack(abs(a).log()/arb(10).log())))
        for key in list(cache):
            if key[1]<n-3:del cache[key]
        print(json.dumps(dict(checked_at_utc=stamp(),completed_order=n,actual_elapsed_s=time.monotonic()-start)),flush=True)
    fits={}
    for lower in [348,351,357,360,370]:
        block={}
        for label in ['F','G']:
            picked=[r for r in rows if r['field']==label and r['n']>=lower]
            ns=[arb(r['n']) for r in picked];ys=[arb(dyadic(v[0],v[1]),dyadic(v[2],v[3])) for r in picked for v in [r['log_abs_multiplier']]]
            logarithmic=fit([n.log()/arb(10).log() for n in ns],ys);inverse=fit([1/n for n in ns],ys)
            cinf=arb(inverse['intercept']);inverse['limiting_multiplier_display']=text((cinf*arb(10).log()).exp());inverse['conditional_array_radius_display']=text((-cinf*arb(10).log()/3).exp())
            block[label]=dict(logarithmic=logarithmic,inverse_order=inverse,per_order=fit(ns,ys))
        fits[str(lower)]=block
    holdout=[];period_changes=[]
    for row in rows:
        label=row['field'];n=row['n'];observed=arb(row['multiplier_display']);y=abs(observed).log()/arb(10).log()
        if n>=372:
            predictions={}
            for model,feature in [('logarithmic',arb(n).log()/arb(10).log()),('inverse_order',1/arb(n))]:
                previous_fit=old['fits'][label][model]
                prediction=arb(previous_fit['intercept'])+arb(previous_fit['slope'])*feature
                predictions[model]=dict(prediction=text(prediction),observed_minus_predicted=text(y-prediction))
            holdout.append(dict(n=n,field=label,observed=text(y),predictions=predictions))
        if n>=351 and n%3==0:
            prev=next(r for r in rows if r['n']==n-3 and r['field']==label)
            change=y-abs(arb(prev['multiplier_display'])).log()/arb(10).log()
            period_changes.append(dict(n=n,field=label,change_log10_abs_multiplier=text(change)))
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,source=metadata,bits=768,orders=[348,400],count_per_field=53,scope='Finite fits conditional on reset input at329; no all-order tail model is assumed.',prior_interval_comparisons=comparisons,rows=rows,fits=fits,old_fit_extrapolation=holdout,three_order_multiplier_changes=period_changes,actual_elapsed_s=time.monotonic()-start)
    put(ROOT/'verification/drift_fit_checks.json',result)
    for name in ['shifted_drift400_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    pp=Path('../a4-num/code/cycle_diag.py');(ROOT/'sources'/'producer_cycle_diag.py').write_bytes(pp.read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        record=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification/FAILURE.json',record);print(json.dumps(record),flush=True);raise SystemExit(1)
