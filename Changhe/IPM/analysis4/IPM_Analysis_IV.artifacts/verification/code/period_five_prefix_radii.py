"""Apply the proved integer-period prefix map to independently audited Q5 data."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from unpack_dyadic4 import unpack
from certified_prefix_majorant import PrefixMajorant,certificate,roundup,upper
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/182_period_five_prefix_radii')

def one(index):
    start=time.monotonic();ctx.prec=2048
    source=Path(f'research/180_period_five_numerical_audit/verification/root{index}_checks.json');data=json.loads(source.read_text())
    assert data['all_checks_pass'] and data['independent_maximum_order']>=50
    response=Path(f'research/175_integer_period_prefix/verification/Q5_root{index}.json');s=F(json.loads(response.read_text())['s'])
    d={r['n']:roundup(r['n']*upper(arb(*unpack(r['F'])))) for r in data['independent_norms']}
    e={5:F(0)}
    for r in data['harmonics']:e[r['n']]=roundup(r['n']*upper(abs(arb(*unpack(r['H'])))))
    cases=[]
    for N in [10,20,30,40,50]:
        model=PrefixMajorant(1,5,4,[d[j] for j in range(1,N+1)],[e[j] for j in range(5,N,5)],s,F(75,56),F(66,5)*F(N+1,N))
        result=certificate(model,2);q=result['w_dyadic_exponent'];best,record=try_box(model,q);assert best;attempts=[record]
        while q>1:
            box,record=try_box(model,q-1);attempts.append(record)
            if box is None:break
            best=box;q-=1
        result['adaptive']=best;result['adaptive_attempts']=attempts;result['inputs']={str(p):sha256(p.read_bytes()).hexdigest() for p in [source,response]}
        path=ROOT/'verification'/f'root{index}_N{N}.json';path.write_text(json.dumps(clean(result),indent=2)+'\n')
        cases.append(dict(N=N,box_q=result['w_dyadic_exponent'],adaptive_q=q,radius_exponent=F(q,2),scalar_checks=result['scalar_coefficient_checks'],path=str(path)))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,cases=cases,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n');print(json.dumps(clean(result)),flush=True);return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='6');args=ap.parse_args();start=time.monotonic();rows=[];failures=[]
    for index in map(int,args.roots.split(',')):
        try:rows.append(one(index))
        except Exception as exc:
            fail=dict(root=index,type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            failures.append(fail);(ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=not failures,rows=rows,failures=failures,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'roots{args.roots}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['period_five_prefix_radii.py','unpack_dyadic4.py','certified_prefix_majorant.py','resonance_block_majorant.py','adaptive_majorant_boxes.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
