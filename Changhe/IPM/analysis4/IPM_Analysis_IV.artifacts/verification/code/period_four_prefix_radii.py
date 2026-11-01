"""Exact continuation boxes for independently certified Q4 prefixes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from unpack_dyadic4 import unpack
from certified_prefix_majorant import PrefixMajorant,certificate,roundup,upper
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/178_period_four_prefix_radii')

def run_one(index):
    start=time.monotonic();ctx.prec=1536
    source=Path(f'research/177_period_four_numerical_audit/verification/root{index}_checks.json')
    old=json.loads(source.read_text());assert old['all_checks_pass'] and old['independent_maximum_order']==40
    response=Path(f'research/175_integer_period_prefix/verification/Q4_root{index}.json')
    base=json.loads(response.read_text());s=F(base['s'])
    d={row['n']:roundup(upper(arb(*unpack(row['F'])))*row['n']) for row in old['independent_norms']}
    e={4:F(0)}
    for row in old['harmonics']:
        n=row['n'];e[n]=roundup(upper(abs(arb(*unpack(row['H']))))*n)
    cases=[]
    for N in [8,16,24,32,40]:
        m=PrefixMajorant(1,4,4,[d[n] for n in range(1,N+1)],[e[n] for n in range(4,N,4)],s,F(12,11),8*F(N+1,N))
        result=certificate(m,2);q=result['w_dyadic_exponent'];best,rec=try_box(m,q);assert best;attempts=[rec]
        while q>1:
            box,rec=try_box(m,q-1);attempts.append(rec)
            if box is None:break
            best=box;q-=1
        result['adaptive']=best;result['adaptive_attempts']=attempts
        result['inputs']={str(p):sha256(p.read_bytes()).hexdigest() for p in [source,response]}
        path=ROOT/'verification'/f'root{index}_N{N}.json';path.write_text(json.dumps(clean(result),indent=2)+'\n')
        brief=dict(N=N,box_q=result['w_dyadic_exponent'],adaptive_q=q,radius_exponent=F(q,2),scalar_checks=result['scalar_coefficient_checks'],path=str(path));cases.append(brief)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,cases=cases,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n');print(json.dumps(clean(result)),flush=True);return result

def main():
    start=time.monotonic();rows=[];failures=[]
    for index in range(1,7):
        try:rows.append(run_one(index))
        except Exception as exc:
            fail=dict(root=index,type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            failures.append(fail);(ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=not failures,rows=rows,failures=failures,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['period_four_prefix_radii.py','certified_prefix_majorant.py','resonance_block_majorant.py','adaptive_majorant_boxes.py','stream_precision_audit.py','unpack_dyadic4.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':main()
