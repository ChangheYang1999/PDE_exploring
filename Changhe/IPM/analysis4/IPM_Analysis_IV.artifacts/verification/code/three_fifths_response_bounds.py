"""Exact dyadic interval covers of every delta3/5 tuning response."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse, gzip, json, sys, time, traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb, ctx
from compact_response_bounds import Response, ball, refine_root
from certified_initial_majorants import pack
ROOT=Path('research/204_three_fifths_response_bounds')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator

def exact_lower(v):
    m,e,r,re=pack(v)
    return abs(F(m)*F(2)**e)-F(r)*F(2)**re

def put(path,data):
    raw=(json.dumps(data,indent=2)+'\n').encode()
    path.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)

def cover(response,s):
    stack=[(F(0),F(1,40),'')];nodes=[];splits=0;started=time.monotonic()
    while stack:
        a,b,address=stack.pop()
        lower=max(7,ceil((1/b+2)/6));upper=None if not a else floor((1/a+2)/6)
        node=dict(address=address,a=str(a),b=str(b),lower=lower,upper=upper)
        if upper is not None and upper<lower:
            node['status']='empty';nodes.append(node)
        else:
            value=response.compact(ball(mpq(str(a))).union(ball(mpq(str(b)))))
            if value is not None and exact_lower(value)>s:
                node.update(status='accepted',response_exact_dyadic=pack(value));nodes.append(node)
            else:
                assert len(address)<80, ('cover_depth',address,str(a),str(b))
                mid=(a+b)/2;stack.append((mid,b,address+'1'));stack.append((a,mid,address+'0'));splits+=1
        if (len(nodes)+splits)%500==0:
            print(json.dumps(dict(stage='cover',leaves=len(nodes),splits=splits,pending=len(stack),elapsed_s=time.monotonic()-started)),flush=True)
        assert len(nodes)+splits<100000
    return dict(nodes=nodes,splits=splits,starting_index=7,lower_bound=str(s),elapsed_s=time.monotonic()-started)

def replay(data):
    s=F(data['lower_bound']);leaves=[];accepted=empty=0
    for node in data['nodes']:
        address=node['address'];den=2**len(address);num=int(address,2) if address else 0
        a,b=F(num,40*den),F(num+1,40*den)
        assert [a,b]==[F(node['a']),F(node['b'])]
        lower=max(7,ceil((1/b+2)/6));upper=None if not a else floor((1/a+2)/6)
        assert (lower,upper)==(node['lower'],node['upper'])
        if node['status']=='empty':
            assert upper is not None and upper<lower;empty+=1
        else:
            assert node['status']=='accepted'
            m,e,r,re=node['response_exact_dyadic'];rad=F(r)*F(2)**re
            assert rad>=0 and abs(F(m)*F(2)**e)-rad>s;accepted+=1
        leaves.append((a,b))
    leaves.sort()
    assert leaves[0][0]==0 and leaves[-1][1]==F(1,40)
    assert all(left[1]==right[0] for left,right in zip(leaves,leaves[1:]))
    assert len(leaves)==data['splits']+1
    return dict(accepted=accepted,empty=empty,leaves=len(leaves),exact_partition_replay_passes=True)

def one(index,bits):
    started=time.monotonic();ctx.prec=bits
    source=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json')
    data=json.loads(source.read_text());assert data['all_checks_pass']
    b,I=refine_root(data['primitive_coefficients'],data['real_roots'][index-1]['interval'],bits+64)
    response=Response(3,10,b);finite=[]
    for k in range(1,17):
        v=response.full(k);assert exact_lower(v)>0,('finite_unresolved',k)
        if k>=7:assert response.compact(ball(mpq(1,6*k-2))).overlaps(v)
        finite.append(dict(k=k,sigma_exact_dyadic=pack(v),sigma_display=v.str(45,radius=True)))
    limit=response.compact(arb(0));assert exact_lower(limit)>0
    least=exact_lower(limit)
    for row in finite:
        m,e,r,re=row['sigma_exact_dyadic'];least=min(least,abs(F(m)*F(2)**e)-F(r)*F(2)**re)
    s=F(1)
    while s>=least/4:s/=2
    print(json.dumps(dict(stage='finite',root=index,s=str(s),limit=limit.str(30,radius=True),elapsed_s=time.monotonic()-started)),flush=True)
    coverage=cover(response,s)
    receipt=replay(coverage)
    cp=ROOT/'verification'/f'root{index}_coverage.json.gz';put(cp,coverage)
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,root_index=index,bits=bits,root_interval=I,s=str(s),finite=finite,
                limiting_response=pack(limit),coverage_path=str(cp),coverage_sha256=sha256(cp.read_bytes()).hexdigest(),coverage=receipt,
                counts=response.solver.counts,source_path=str(source),source_sha256=sha256(source.read_bytes()).hexdigest(),actual_elapsed_s=time.monotonic()-started)
    put(ROOT/'verification'/f'root{index}_checks.json',result)
    print(json.dumps({k:result[k] for k in ['checked_at_utc','root_index','s','coverage','actual_elapsed_s']}),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');ap.add_argument('--bits',type=int,default=768);args=ap.parse_args()
    for index in map(int,args.roots.split(',')):
        try:one(index,args.bits)
        except Exception as exc:
            result=dict(checked_at_utc=stamp(),root=index,error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            put(ROOT/'verification'/f'root{index}_FAILURE.json',result);print(json.dumps(result),flush=True);raise SystemExit(1)
    for name in ['three_fifths_response_bounds.py','compact_response_bounds.py','pure_cartesian_ball.py','certified_initial_majorants.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())

if __name__=='__main__':main()
