"""Long-prefix exact majorant certificates, conditional on admitted source receipts."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,os,pickle,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
from certified_prefix_majorant import PrefixMajorant,certificate,roundup,upper
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/220_high_prefix_three_fifths_radii')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def savegz(path,data):
    raw=json.dumps(clean(data),separators=(',',':')).encode();compressed=gzip.compress(raw,compresslevel=6,mtime=0)
    total=sum(p.stat().st_size for base,dirs,names in os.walk('.') for name in names for p in [Path(base,name)])
    assert total+len(compressed)<3_000_000_000
    path.write_bytes(compressed)
    return dict(path=str(path),sha256=sha256(compressed).hexdigest(),raw_sha256=sha256(raw).hexdigest(),bytes=len(compressed))

def one(index,prefixes):
    started=time.monotonic();ctx.prec=1536;zero=arb(0)
    ep=Path(f'research/209_three_fifths_high_order/verification/root{index}_checks.json');er=json.loads(ep.read_text());assert er['all_checks_pass'] and er['completed_order']==300
    rp=Path(f'research/204_three_fifths_response_bounds/verification/root{index}_checks.json');rr=json.loads(rp.read_text());assert rr['all_checks_pass'] and rr['coverage']['exact_partition_replay_passes'];s=F(rr['s'])
    pp=Path(f'research/208_three_fifths_producer_enclosure/verification/root{index}_checks.json');pr=json.loads(pp.read_text());assert pr['all_checks_pass'] and pr['maximum_order']==300 and pr['source']['sha256']==er['source']['sha256']
    source=Path(er['source']['path']);raw=source.read_bytes();assert sha256(raw).hexdigest()==er['source']['sha256'];state=pickle.loads(raw);del raw
    assert str(state['delta_exact'])=='3/5' and state['prec']==1024 and max(state['f'])==300
    d={};e={};normrecords=[];harmrecords=[]
    for n in range(1,max(prefixes)+1):
        norm=sum((abs(arb(*unpack(v))) for v in state['f'][n]),zero)
        d[n]=roundup(n*upper(norm));assert d[n]>n*upper(norm)
        normrecords.append(dict(n=n,enclosure=pack(norm),bound=d[n]))
        if n%10==0 and n<max(prefixes):
            H=abs(arb(*unpack(state['g'][n][3*(n//10)-1])))
            e[n]=roundup(n*upper(H));assert e[n]>n*upper(H)
            harmrecords.append(dict(n=n,enclosure=pack(H),bound=e[n]))
    del state
    inputs=dict(root_index=index,source=er['source'],producer_receipt=dict(path=str(pp),sha256=sha256(pp.read_bytes()).hexdigest()),equation_receipt=dict(path=str(ep),sha256=sha256(ep.read_bytes()).hexdigest()),response_receipt=dict(path=str(rp),sha256=sha256(rp.read_bytes()).hexdigest()),s=s,density=normrecords,harmonics=harmrecords)
    inp=savegz(ROOT/'verification'/f'root{index}_inputs.json.gz',inputs)
    rows=[]
    for N in prefixes:
        begin=time.monotonic();m=PrefixMajorant(3,10,4,[d[j] for j in range(1,N+1)],[e[j] for j in range(10,N,10)],s,F(75,29),F(16,3)*F(N+1,N))
        result=certificate(m,2);q=result['w_dyadic_exponent'];best,attempt=try_box(m,q);assert best;attempts=[attempt]
        while q>1:
            box,attempt=try_box(m,q-1);attempts.append(attempt)
            if box is None:break
            best=box;q-=1
        result.update(root_index=index,adaptive=best,adaptive_attempts=attempts,inputs=inp,checked_at_utc=stamp(),actual_elapsed_s=time.monotonic()-begin)
        receipt=savegz(ROOT/'verification'/f'root{index}_N{N}.json.gz',result)
        row=dict(N=N,q=q,radius_exponent=F(q,6),receipt=receipt,actual_elapsed_s=result['actual_elapsed_s']);rows.append(row)
        print(json.dumps(clean(dict(root_index=index,**row))),flush=True)
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,root_index=index,cases=rows,inputs=inp,actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');ap.add_argument('--prefixes',default='60,100,150,200,300');a=ap.parse_args()
    for index in map(int,a.roots.split(',')):one(index,list(map(int,a.prefixes.split(','))))
    for name in ['high_prefix_three_fifths_radii.py','stream_precision_audit.py','certified_initial_majorants.py','certified_prefix_majorant.py','resonance_block_majorant.py','adaptive_majorant_boxes.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':
    try:main()
    except Exception as exc:
        row=dict(checked_at_utc=stamp(),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification'/'FAILURE.json').write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row),flush=True);raise SystemExit(1)
