"""Exact prefix-majorant certificates for the four delta3/5 profiles."""
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
ROOT=Path('research/205_three_fifths_prefix_radii')

def one(index):
    started=time.monotonic();ctx.prec=3072
    source=Path(f'research/202_three_fifths_numerical_audit/verification/root{index}_checks.json')
    data=json.loads(source.read_text());assert data['all_checks_pass'] and data['independent_maximum_order']>=40
    response=Path(f'research/204_three_fifths_response_bounds/verification/root{index}_checks.json')
    rd=json.loads(response.read_text());assert rd['all_checks_pass'] and rd['coverage']['exact_partition_replay_passes']
    s=F(rd['s']);assert s>0
    d={r['n']:roundup(r['n']*upper(arb(*unpack(r['F'])))) for r in data['independent_norms']}
    e={r['n']:roundup(r['n']*upper(abs(arb(*unpack(r['H']))))) for r in data['harmonics']}
    rows=[]
    for N in [10,20,30,40]:
        model=PrefixMajorant(3,10,4,[d[j] for j in range(1,N+1)],[e[j] for j in range(10,N,10)],s,F(75,29),F(16,3)*F(N+1,N))
        result=certificate(model,2);q=result['w_dyadic_exponent'];best,record=try_box(model,q);assert best;attempts=[record]
        while q>1:
            box,record=try_box(model,q-1);attempts.append(record)
            if box is None:break
            best=box;q-=1
        result['adaptive']=best;result['adaptive_attempts']=attempts
        result['inputs']={str(p):sha256(p.read_bytes()).hexdigest() for p in [source,response]}
        path=ROOT/'verification'/f'root{index}_N{N}.json';path.write_text(json.dumps(clean(result),indent=2)+'\n')
        row=dict(N=N,q=q,radius_exponent=F(q,6),initial_box_q=result['w_dyadic_exponent'],scalar_checks=result['scalar_coefficient_checks'],path=str(path))
        rows.append(row);print(json.dumps(clean(dict(root=index,**row))),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,s=s,cases=rows,actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    print(json.dumps(clean(result)),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');args=ap.parse_args()
    for index in map(int,args.roots.split(',')):
        try:one(index)
        except Exception as exc:
            result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),root=index,error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            (ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);raise SystemExit(1)
    for name in ['three_fifths_prefix_radii.py','unpack_dyadic4.py','certified_prefix_majorant.py','resonance_block_majorant.py','adaptive_majorant_boxes.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':main()
