"""Rebuild retained prefix maps and test the same box at twice the radius variable."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant
from resonance_block_majorant import clean

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--topics',default='176,178,179,181');args=parser.parse_args();start=time.monotonic();rows=[]
    roots=[]
    for number in args.topics.split(','):roots.extend(Path('research').glob(number+'_*/verification'))
    for root in roots:
        for path in sorted(root.glob('*_N*.json')):
            data=json.loads(path.read_text())
            if 'initial_density' not in data or 'adaptive' not in data:continue
            model=PrefixMajorant(data['h'],data['Q'],data['B'],list(map(F,data['initial_density'])),list(map(F,data['initial_harmonics'])),F(data['s']),F(data['L']),F(data['kappa']))
            assert model.Y0==list(map(F,data['Y0']))
            a=data['adaptive'];q=a['q'];w=F(1,2**q);box=list(map(F,a['box']));image=model.transformed(w,box)
            assert image==list(map(F,a['image']))
            assert all(0<=y<=b and 0<=v<=b for y,v,b in zip(model.Y0,image,box))
            image2=model.transformed(2*w,box)
            failed=[i for i,(v,b) in enumerate(zip(image2,box)) if v>b]
            row=dict(path=str(path),sha256=sha256(path.read_bytes()).hexdigest(),q=q,all_admitted_checks_pass=True,twice_w_same_box_fails=bool(failed),failed_components=failed,maximum_ratio_at_twice_w=max(v/b for v,b in zip(image2,box)))
            if not failed:row['improved_same_box_certificate']=dict(q=q-1,box=box,image=image2,Y0=model.Y0)
            rows.append(row)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,boxes=len(rows),rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Only these retained boxes are tested. Failure of one box does not exclude other supersolutions.')
    out=Path('research/174_adaptive_majorant_boxes/verification/prefix_box_replay.json');out.write_text(json.dumps(clean(result),indent=2)+'\n');print(json.dumps(dict(boxes=len(rows),same_box_double_failures=sum(r['twice_w_same_box_fails'] for r in rows),actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':main()
