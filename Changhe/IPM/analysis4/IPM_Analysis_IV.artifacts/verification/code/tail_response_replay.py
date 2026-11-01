"""Exact partition, coefficient-bound, polynomial-map and box replay for223."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from certified_prefix_majorant import PrefixMajorant
from resonance_block_majorant import clean
ROOT=Path('research/223_tail_response_radii')
def lower(v):
    m,e,r,re=v;return abs(F(m)*F(2)**int(e))-F(r)*F(2)**int(re)
def upper(v):
    m,e,r,re=v;return F(m)*F(2)**int(e)+F(r)*F(2)**int(re)
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator
def read(receipt):
    p=Path(receipt['path']);raw=p.read_bytes();assert sha256(raw).hexdigest()==receipt['sha256'];raw=gzip.decompress(raw);assert sha256(raw).hexdigest()==receipt['raw_sha256'];return json.loads(raw)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4,1,2,3');ap.add_argument('--K',type=int,default=30);a=ap.parse_args()
    for index in map(int,a.roots.split(',')):
        start=time.monotonic();p=ROOT/'verification'/f'root{index}_K{a.K}_checks.json';r=json.loads(p.read_text());assert r['all_checks_pass'];K=r['K'];s=F(r['s']);c=read(r['coverage']);edge=F(1,6*K-2);assert K==c['K'] and s==F(c['s']) and edge==F(c['edge'])
        leaves=[];accepted=empty=0
        for node in c['nodes']:
            address=node['address'];den=2**len(address);num=int(address,2) if address else 0;lo=edge*F(num,den);hi=edge*F(num+1,den);assert (lo,hi)==(F(node['a']),F(node['b']))
            klow=max(K,ceil((1/hi+2)/6));khigh=None if not lo else floor((1/lo+2)/6);assert (klow,khigh)==(node['lower'],node['upper'])
            if node['status']=='empty':assert khigh is not None and khigh<klow;empty+=1
            else:
                assert node['status']=='accepted' and lower(node['enclosure'])>s
                if node.get('method')=='singleton':assert klow==khigh==node['k']
                elif node.get('method')=='taylor':assert node['degree']==2
                else:assert 'method' not in node
                accepted+=1
            leaves.append((lo,hi))
        leaves.sort();assert leaves[0][0]==0 and leaves[-1][1]==edge and all(u[1]==v[0] for u,v in zip(leaves,leaves[1:])) and len(leaves)==c['splits']+1
        box=read(r['box']);inp=read(box['inputs']);db={v['n']:F(v['bound']) for v in inp['density']};eb={v['n']:F(v['bound']) for v in inp['harmonics']}
        for row in inp['density']+inp['harmonics']:assert F(row['bound'])>row['n']*upper(row['enclosure'])
        N=10*K;assert N==box['N'] and F(box['s'])==s and F(box['L'])==F(75,29) and F(box['kappa'])==F(16,3)*F(N+1,N)
        assert list(map(F,box['initial_density']))==[db[n] for n in range(1,N+1)] and list(map(F,box['initial_harmonics']))==[eb[n] for n in range(10,N,10)]
        m=PrefixMajorant(3,10,4,[db[n] for n in range(1,N+1)],[eb[n] for n in range(10,N,10)],s,F(75,29),F(16,3)*F(N+1,N));assert m.J==[list(map(F,v)) for v in box['J']] and m.Y0==list(map(F,box['Y0'])) and m.constant==list(map(F,box['constant']))
        best=box['adaptive'];q=best['q'];B=list(map(F,best['box']));image=m.transformed(F(1,2**q),B);assert image==list(map(F,best['image'])) and all(0<=v<=b and b>=y for v,b,y in zip(image,B,m.Y0))
        out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,K=K,accepted=accepted,empty=empty,leaves=len(leaves),s=s,q=q,radius_exponent=F(q,6),exact_partition_replay=True,exact_box_replay=True,actual_elapsed_s=time.monotonic()-start)
        (ROOT/'verification'/f'root{index}_K{K}_review.json').write_text(json.dumps(clean(out),indent=2)+'\n');print(json.dumps(clean(out)),flush=True)
    (ROOT/'sources/tail_response_replay.py').write_bytes(Path(__file__).read_bytes())
if __name__=='__main__':main()
