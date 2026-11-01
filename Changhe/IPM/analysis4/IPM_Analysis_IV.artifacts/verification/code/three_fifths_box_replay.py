"""Replay saved exact residue maps, independently of the box search."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant
from resonance_block_majorant import clean
ROOT=Path('research/205_three_fifths_prefix_radii')

def one(index):
    started=time.monotonic();rows=[]
    for N in [10,20,30,40]:
        path=ROOT/'verification'/f'root{index}_N{N}.json';d=json.loads(path.read_text())
        m=PrefixMajorant(d['h'],d['Q'],d['B'],list(map(F,d['initial_density'])),list(map(F,d['initial_harmonics'])),F(d['s']),F(d['L']),F(d['kappa']))
        assert m.constant==list(map(F,d['constant'])) and m.Y0==list(map(F,d['Y0']))
        assert m.J==[list(map(F,row)) for row in d['J']]
        a=d['adaptive'];q=a['q'];box=list(map(F,a['box']));image=m.transformed(F(1,2**q),box)
        assert image==list(map(F,a['image']))
        assert all(0<=y<b and b>=y0 for y,b,y0 in zip(image,box,m.Y0))
        rows.append(dict(path=str(path),sha256=sha256(path.read_bytes()).hexdigest(),q=q,dimensions=m.dimension,strict_invariance=True,maximum_ratio=max(y/b for y,b in zip(image,box))))
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-started)
    p=ROOT/'verification'/f'root{index}_review.json';assert not p.exists(),'Preserve the previous successful review.'
    p.write_text(json.dumps(clean(out),indent=2)+'\n');print(json.dumps(clean(out)),flush=True)
    (ROOT/'sources'/'three_fifths_box_replay.py').write_bytes(Path(__file__).read_bytes())
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='1');a=ap.parse_args()
    for index in map(int,a.roots.split(',')):one(index)
