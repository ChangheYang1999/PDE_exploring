"""Heuristic component proposals, admitted only by complete exact rational boxes."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,math,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from resonance_block_majorant import BlockMajorant,clean
from certified_prefix_majorant import PrefixMajorant
ROOT=Path('research/174_adaptive_majorant_boxes')


def float_model(m):
    f=object.__new__(type(m));f.__dict__=m.__dict__.copy()
    for key in ['L','s','kappa']:setattr(f,key,float(getattr(m,key)))
    for key in ['d','Y0','constant']:setattr(f,key,list(map(float,getattr(m,key))))
    f.J=[list(map(float,row)) for row in m.J]
    if hasattr(m,'e'):
        f.e=list(map(float,m.e))
        f.fixed={r:[list(map(float,row)) for row in data] for r,data in m.fixed.items()}
        f.known_residue={key:[(a,float(v)) for a,v in row] for key,row in m.known_residue.items()}
    return f


def round_upper(v,bits=48):
    assert v>0
    exponent=v.numerator.bit_length()-v.denominator.bit_length()
    unit=F(2)**(exponent-bits)
    z=v/unit
    return F(-(-z.numerator//z.denominator))*unit


def try_box(m,q,max_steps=180):
    f=float_model(m);w=2.**(-q);t=[1.]*m.dimension;attempts=0
    for iteration in range(1,max_steps+1):
        Y=[a*x for a,x in zip(f.Y0,t)]
        try:
            phiw=f.phi(w,Y);phi0=f.phi(0.,Y)
            rem=[max(a-b,0.) for a,b in zip(phiw,phi0)]
            image=[a+b for a,b in zip(f.Y0,f.precondition(rem))]
            nxt=[a/b for a,b in zip(image,f.Y0)]
        except (OverflowError,ValueError):return None,dict(q=q,iterations=iteration,reason='heuristic overflow')
        if any(not math.isfinite(v) or v>1e20 for v in nxt):return None,dict(q=q,iterations=iteration,reason='heuristic growth limit')
        defect=max(a/b for a,b in zip(nxt,t))
        if defect<1.00001 or iteration%30==0:
            attempts+=1
            proposed=[round_upper(a*F.from_float(max(x,y))*F(1000001,1000000)) for a,x,y in zip(m.Y0,t,nxt)]
            assert all(a>=b for a,b in zip(proposed,m.Y0))
            exact=m.transformed(F(1,2**q),proposed)
            if all(a<=b for a,b in zip(exact,proposed)):
                return dict(q=q,w=F(1,2**q),radius_exponent=F(q,2*m.h),box=proposed,image=exact,Y0=m.Y0,maximum_ratio=max(a/b for a,b in zip(exact,proposed))),dict(q=q,iterations=iteration,exact_attempts=attempts,passed=True)
        t=[max(x,y)*(1+1e-10) for x,y in zip(t,nxt)]
    return None,dict(q=q,iterations=max_steps,exact_attempts=attempts,reason='iteration budget')


def solve(name,m,startq,sources):
    begin=time.monotonic();attempts=[]
    best,record=try_box(m,startq);attempts.append(record);assert best,(name,'initial proposal failed',record)
    q=startq
    while q>8:
        trial=q-8;result,record=try_box(m,trial);attempts.append(record)
        if result is None:low,high=trial,q;break
        best=result;q=trial
    else:low,high=0,q
    while high-low>1:
        trial=(low+high)//2;result,record=try_box(m,trial);attempts.append(record)
        if result is None:low=trial
        else:high=trial;best=result
    assert best['q']==high
    best.update(name=name,all_exact_checks_pass=True,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),attempts=attempts,initial_q=startq,h=m.h,Q=m.Q,B=m.B,s=m.s,L=m.L,kappa=m.kappa,
        inputs={str(p):sha256(p.read_bytes()).hexdigest() for p in sources},actual_elapsed_s=time.monotonic()-begin)
    (ROOT/'verification'/f'{name}.json').write_text(json.dumps(clean(best),indent=2)+'\n')
    brief={k:best[k] for k in ['name','q','radius_exponent','initial_q','actual_elapsed_s']};brief['maximum_ratio']=float(best['maximum_ratio'])
    print(json.dumps(clean(brief)),flush=True);return brief


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=['prefix','block','all'],default='all');args=ap.parse_args()
    start=time.monotonic();rows=[]
    if args.family in ['prefix','all']:
        for N in [9,18,90]:
            path=Path(f'research/172_certified_prefix_majorant/verification/two_mode5_N{N}.json');data=json.loads(path.read_text())
            for sharp in [False,True]:
                s=F(data['s']);sources=[path]
                if sharp:
                    source=Path('research/164_four_ninths_response_minima/verification/root5_certificate.json.gz')
                    s=F(json.loads(gzip.decompress(source.read_bytes()))['uniform_lower_bound']);sources.append(source)
                m=PrefixMajorant(2,9,4,list(map(F,data['initial_density'])),list(map(F,data['initial_harmonics'])),s,F(data['L']),F(data['kappa']))
                rows.append(solve(f'prefix_N{N}_'+('sharp' if sharp else 'old'),m,data['w_dyadic_exponent'],sources))
    if args.family in ['block','all']:
        for family,indices in [('two_mode',range(1,5)),('candidate',[2,3,4])]:
            for index in indices:
                path=Path(f'research/171_resonance_block_majorant/verification/{family}_root{index}_improved.json');data=json.loads(path.read_text());sources=[path]
                s=F(data['s'])
                if family=='two_mode':
                    source=Path(f'research/164_four_ninths_response_minima/verification/root{index}_certificate.json.gz');sources.append(source)
                    s=F(json.loads(gzip.decompress(source.read_bytes()))['uniform_lower_bound'])
                m=BlockMajorant(2,9,data['B'],list(map(F,data['initial'])),s,F(data['L']),F(data['kappa']))
                row=solve(f'{family}_{index}',m,data['w_dyadic_exponent'],sources)
                rows.append(row)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'{args.family}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['adaptive_majorant_boxes.py','resonance_block_majorant.py','certified_prefix_majorant.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(clean(result)),flush=True)

if __name__=='__main__':main()
