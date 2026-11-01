"""Replay long-prefix boxes and rounded coefficient bounds using exact fractions."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant
from resonance_block_majorant import clean
ROOT=Path('research/220_high_prefix_three_fifths_radii')
def upper(v):
    a,b,c,d=v
    return F(int(a))*F(2)**int(b)+F(int(c))*F(2)**int(d)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');args=ap.parse_args()
    for index in map(int,args.roots.split(',')):
        start=time.monotonic();cp=ROOT/'verification'/f'root{index}_checks.json';c=json.loads(cp.read_text());assert c['all_checks_pass']
        inp=c['inputs'];ip=Path(inp['path']);raw=ip.read_bytes();assert sha256(raw).hexdigest()==inp['sha256'];iraw=gzip.decompress(raw);assert sha256(iraw).hexdigest()==inp['raw_sha256'];d=json.loads(iraw)
        db={};eb={}
        for key,target in [('density',db),('harmonics',eb)]:
            for row in d[key]:
                target[row['n']]=F(row['bound']);assert target[row['n']]>row['n']*upper(row['enclosure'])
        rows=[]
        for case in c['cases']:
            path=Path(case['receipt']['path']);raw=path.read_bytes();assert sha256(raw).hexdigest()==case['receipt']['sha256'];a=json.loads(gzip.decompress(raw));N=a['N']
            assert list(map(F,a['initial_density']))==[db[j] for j in range(1,N+1)]
            assert list(map(F,a['initial_harmonics']))==[eb[j] for j in range(10,N,10)]
            assert a['h']==3 and a['Q']==10 and a['B']==4 and F(a['s'])==F(d['s']) and F(a['L'])==F(75,29) and F(a['kappa'])==F(16,3)*F(N+1,N)
            m=PrefixMajorant(3,10,4,list(map(F,a['initial_density'])),list(map(F,a['initial_harmonics'])),F(a['s']),F(a['L']),F(a['kappa']))
            assert m.constant==list(map(F,a['constant'])) and m.Y0==list(map(F,a['Y0'])) and m.J==[list(map(F,row)) for row in a['J']]
            best=a['adaptive'];box=list(map(F,best['box']));q=best['q'];image=m.transformed(F(1,2**q),box)
            assert image==list(map(F,best['image'])) and all(0<=v<=b and b>=y0 for v,b,y0 in zip(image,box,m.Y0))
            rows.append(dict(N=N,q=q,radius_exponent=F(q,6),dimension=m.dimension,maximum_ratio=max(v/b for v,b in zip(image,box)),exact_box_verified=True,receipt=case['receipt']))
        out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,coefficient_upper_bounds=len(db),harmonic_upper_bounds=len(eb),cases=rows,actual_elapsed_s=time.monotonic()-start)
        p=ROOT/'verification'/f'root{index}_review.json';assert not p.exists();p.write_text(json.dumps(clean(out),indent=2)+'\n');print(json.dumps(clean(out)),flush=True)
    (ROOT/'sources'/'high_prefix_three_fifths_replay.py').write_bytes(Path(__file__).read_bytes())
if __name__=='__main__':main()
