"""Compare one selected displacement in a specified relative coefficient norm."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,pickle,sys,time,traceback
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/224_sample_amplification')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x):return x.str(38,radius=True)
def main():
    start=time.monotonic();ctx.prec=768;states=[];sources=[]
    for name in ['log_sin1_c3_from329.pkl','log_sin1_c3_pert329.pkl']:
        p=Path('../a4-num/ckpt')/name;raw=p.read_bytes();sources.append(dict(path=str(p),bytes=len(raw),sha256=sha256(raw).hexdigest()));state=pickle.loads(raw);del raw
        assert (state['A'],state['B'],state['ring'],state['prec'])==('2','3','arb',512) and max(state['f'])>=340
        for field in ['f','g']:state[field]={n:a for n,a in state[field].items() if n<=340}
        states.append(state)
    rows=[];input_max=arb(0);max_row=None;positions=0
    for n in range(1,341):
        for field in ['f','g']:
            old,new=(s[field][n] for s in states);assert len(old)==len(new)
            denom=arb(0);other=arb(0);difference=arb(0)
            for a,b in zip(old,new):
                assert len(a)==len(b)
                for av,bv in zip(a,b):
                    x=arb(*unpack(av));y=arb(*unpack(bv));denom+=abs(x);other+=abs(y);difference+=abs(y-x);positions+=1
            if denom.is_zero():assert difference.is_zero();relative=arb(0);normdifference=arb(0)
            else:
                assert denom>0
                relative=difference/denom;normdifference=abs(other/denom-1)
                assert relative.overlaps(normdifference) or relative>normdifference
            row=dict(n=n,field=field,relative_difference=text(relative),relative_difference_dyadic=pack(relative),relative_norm_change=text(normdifference))
            if n<=329:
                if max_row is None or relative>arb(max_row['relative_difference']):max_row=row
                input_max=input_max.max(relative)
            else:rows.append(row)
        if n%50==0:print(json.dumps(dict(time=stamp(),n=n,elapsed_s=time.monotonic()-start)),flush=True)
    assert input_max>0
    for row in rows:
        relative=arb(row['relative_difference']);row['amplification_factor']=text(relative/input_max);row['above_input_max']=bool(relative>input_max);row['below_input_max']=bool(relative<input_max)
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,sources=sources,positions=positions,input_maximum=text(input_max),largest_input_row=max_row,output_rows=rows,scope='Selected finite input configurations only, relative full-array l1 norm.',actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['sample_amplification.py','stream_precision_audit.py','certified_initial_majorants.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k!='output_rows'}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        d=dict(checked_at_utc=stamp(),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True);raise SystemExit(1)
