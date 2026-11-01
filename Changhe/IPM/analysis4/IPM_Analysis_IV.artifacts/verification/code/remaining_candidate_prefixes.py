"""Independent prefixes and exact radius certificates for Candidate roots 5..7."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import other_certified_prefixes as base
from resonance_block_majorant import clean
ROOT=Path('research/181_remaining_candidate_prefixes')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='5,6,7');args=ap.parse_args()
    start=time.monotonic();base.ROOT=ROOT;rows=[];failures=[]
    amplitude=F(json.loads(Path('research/156_candidate_shaped_compatibility/verification/polynomial.json').read_text())['original_amplitude'])
    assert amplitude**225<2**949
    for index in map(int,args.roots.split(',')):
        try:
            row=base.run_one('candidate',index,36,2048)
            best=min(row['boxes'],key=lambda x:x['adaptive_q']);q=best['adaptive_q']
            exponent=F(q,4)+F(949,100);E=-(-exponent.numerator//exponent.denominator)
            row['restored_radius_exponent']=E;row['amplitude_power_225_lt_2_power_949']=True
            p=ROOT/'verification'/f'candidate{index}_checks.json';data=json.loads(p.read_text());data['restored_radius_exponent']=E;data['amplitude_power_225_lt_2_power_949']=True;p.write_text(json.dumps(clean(data),indent=2)+'\n')
            rows.append(row)
        except Exception as exc:
            fail=dict(root=index,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            failures.append(fail);(ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True)
        (ROOT/'verification'/f'roots{args.roots}_partial.json').write_text(json.dumps(clean(dict(rows=rows,failures=failures)),indent=2)+'\n')
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=not failures,rows=rows,failures=failures,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'roots{args.roots}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['remaining_candidate_prefixes.py','other_certified_prefixes.py','pure_cartesian_ball.py','certified_prefix_majorant.py','resonance_block_majorant.py','adaptive_majorant_boxes.py','certified_initial_majorants.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
