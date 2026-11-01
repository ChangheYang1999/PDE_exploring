"""Directed finite cycle diagnostics, independent of the producer's NumPy code."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip, json, pickle, sys, time, traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/207_shifted_cycle_audit')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x):return x.str(42,radius=True)

def main():
    start=time.monotonic();ctx.prec=768
    path=Path('../a4-num/ckpt/log_sin1_c3_from329.pkl')
    raw=path.read_bytes();digest=sha256(raw).hexdigest();size=len(raw);state=pickle.loads(raw);del raw
    assert (state['A'],state['B'],state['ring'],state['prec'])==('2','3','arb',512)
    archived=[]
    for topic in ['189_reset350_conditional_audit','199_reset360_conditional_audit']:
        p=Path('research')/topic/'verification/selected.pkl.gz';raw=p.read_bytes()
        saved=pickle.loads(gzip.decompress(raw))
        count=changed=0
        for field in ['f','g']:
            for n,value in saved[field].items():
                current=state[field][int(n)]
                assert len(current)==len(value)
                for current_col,previous_col in zip(current,value):
                    assert len(current_col)==len(previous_col)
                    for new,old in zip(current_col,previous_col):
                        nm,nr=unpack(new);om,orr=unpack(old)
                        assert nm==om and nr>=orr,(topic,field,n,'not an outward reload')
                        changed+=int(new!=old)
                count+=1
        archived.append(dict(path=str(p),sha256=sha256(raw).hexdigest(),matching_midpoint_arrays=count,outward_radius_changes=changed))
        del raw,saved
    tables={};copies=[]
    for path in sorted(Path('../a4-num/notes').glob('cycle_diag_*.txt')):
        raw=path.read_bytes()
        for line in raw.decode().splitlines():
            bits=line.split()
            if len(bits)>=9 and bits[0].isdigit() and bits[2] in ['F','G']:
                tables[int(bits[0]),bits[2]]=bits
        (ROOT/'sources'/path.name).write_bytes(raw)
        copies.append(dict(path=str(path),sha256=sha256(raw).hexdigest()))
    orders=list(range(330,351))+list(range(358,min(367,max(state['f']))+1))
    cache={}
    def vector(field,n):
        key=field,n
        if key not in cache:
            cache[key]={(q,j):arb(*unpack(v)) for q,col in enumerate(state[field][n]) for j,v in enumerate(col) if any(v)}
        return cache[key]
    rows=[];positions=printed=0
    zero=arb(0)
    for n in orders:
        for field,label in [('f','F'),('g','G')]:
            A=vector(field,n-3);B=vector(field,n)
            for shift in [0,1]:
                shifted={(q,j+shift):v for (q,j),v in A.items()}
                keys=set(shifted)|set(B)
                aa=bb=ab=zero
                for key in keys:
                    a,b=shifted.get(key,zero),B.get(key,zero)
                    aa+=a*a;bb+=b*b;ab+=a*b
                assert aa>0 and bb>0
                slope=ab/aa;rss=rsum=bnorm=zero
                for key in keys:
                    b=B.get(key,zero);res=b-slope*shifted.get(key,zero)
                    rss+=res*res;rsum+=abs(res);bnorm+=abs(b)
                assert rss>0 and bnorm>0
                e2=(rss/bb).sqrt();e1=rsum/bnorm
                row=dict(n=n,field=label,shift=shift,multiplier=pack(slope),relative_l2=pack(e2),relative_l1=pack(e1),
                    multiplier_display=text(slope),relative_l2_display=text(e2),relative_l1_display=text(e1),positions=len(keys))
                old=tables.get((n,label))
                if old:
                    offset=3+3*shift
                    for value,token,kind in [(slope,old[offset],'scientific'),(e2,old[offset+1],'fixed'),(e1,old[offset+2],'fixed')]:
                        tol=arb('0.00051')
                        if kind=='scientific':
                            exponent=int(token.lower().split('e')[1]);tol=arb('0.00051')*(arb(10)**exponent)
                        assert value.overlaps(arb(token)+arb(0,tol)),(n,label,shift,text(value),token)
                        printed+=1
                    row['printed_comparisons_pass']=True
                rows.append(row);positions+=len(keys)
            print(json.dumps(dict(checked_at_utc=stamp(),n=n,field=label,elapsed_s=time.monotonic()-start)),flush=True)
        for key in list(cache):
            if key[1]<n-3:del cache[key]
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,bits=768,
        source=dict(path=str(Path('../a4-num/ckpt/log_sin1_c3_from329.pkl')),sha256=digest,bytes=size,maximum_order=max(state['f'])),
        scope='Conditional on reset midpoint input through329; discarded uncertainty excluded.',
        archived_comparisons=archived,source_tables=copies,rows=rows,total_positions=positions,printed_comparisons=printed,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['shifted_cycle_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as exc:
        result=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result),flush=True)
        raise SystemExit(1)
