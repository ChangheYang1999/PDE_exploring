"""Independent longer Cartesian prefixes and exact continuation boxes."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import Tuning,sine,ball,refine_root
from certified_prefix_majorant import PrefixMajorant,certificate,roundup,upper
from certified_initial_majorants import pack
from resonance_block_majorant import clean
from adaptive_majorant_boxes import try_box
ROOT=Path('research/176_other_certified_prefixes')

def run_one(family,index,N,bits):
    started=time.monotonic();ctx.prec=bits;paths=[]
    if family=='two_mode':
        p=Path('research/146_four_ninths_profiles/verification/algebraic_certificates.json');paths.append(p);data=json.loads(p.read_text())
        coeff=data['primitive_coefficients'];interval=data['real_roots'][index-1]['interval'];fixed={'1':'1'};B=4
        p=Path(f'research/164_four_ninths_response_minima/verification/root{index}_certificate.json.gz');paths.append(p)
        s=F(json.loads(gzip.decompress(p.read_bytes()))['uniform_lower_bound']);amplitude=F(1)
    else:
        p=Path('research/156_candidate_shaped_compatibility/verification/polynomial.json');paths.append(p);data=json.loads(p.read_text())
        p=Path('research/156_candidate_shaped_compatibility/verification/checks.json');paths.append(p);roots=json.loads(p.read_text())
        coeff=data['primitive_coefficients_ascending'];interval=roots['roots'][index-1]['interval'];fixed=data['fixed_normalized_coefficients'];B=20
        name='158_candidate_shaped_response' if index==3 else '163_other_candidate_shaped_roots'
        p=Path(f'research/{name}/verification/root{index}_checks.json');paths.append(p);response=json.loads(p.read_text())
        assert response['all_index_lower_bound_proved'];s=F(response['lower_bound']);amplitude=F(data['original_amplitude'])
    b,I=refine_root(coeff,interval,bits+64);solver=Tuning(2,9,B)
    initial=sine(solver.p(1),3,b)
    for mode,value in fixed.items():initial=initial+sine(solver.p(1),int(mode),ball(mpq(value)))
    f={1:initial};g={1:solver.poisson(initial,1)};harmonics=[];obstructions=[]
    for n in range(2,N+1):
        fn=solver.order(n,f,g)
        if solver.resonant(n):
            obstruction=fn.sine(solver.frequency(n)-1);assert obstruction.contains(0)
            fn=fn.project(B*n-1,1,solver.counts,zero_mode=solver.frequency(n)-1);f[n]=fn
            obstructions.append(dict(n=n,exact_dyadic=pack(obstruction)))
            if n<N:
                R=solver.continuation(n,f,g,arb(0));R1=solver.continuation(n,f,g,arb(1));S=R1-R
                assert not S.contains(0),('unresolved_response',family,index,n,str(S))
                H=-R/S;g[n]=solver.poisson(fn,n,H)
                harmonics.append(dict(n=n,H=H,sigma=S))
                print(json.dumps(dict(family=family,root=index,n=n,stage='tuned',sigma=S.str(30,radius=True),elapsed_s=time.monotonic()-started)),flush=True)
        else:f[n]=fn;g[n]=solver.poisson(fn,n)
    normrows=[];d={};e={};hrows=[]
    for n in range(1,N+1):
        value=f[n].norm()*n;d[n]=roundup(upper(value));assert d[n]>upper(value)
        normrows.append(dict(n=n,norm_times_n=pack(value),bound=d[n],root=(f[n].norm().log()/n).exp().str(40,radius=True)))
    for row in harmonics:
        n=row['n'];value=abs(row['H'])*n;e[n]=roundup(upper(value));assert e[n]>upper(value)
        hrows.append(dict(n=n,H=pack(row['H']),sigma=pack(row['sigma']),bound=e[n]))
    oldcomparisons=[]
    if family=='two_mode':
        path=Path(f'research/153_four_ninths_finite_prefixes/verification/root{index}_checks.json')
        if path.exists():
            old=json.loads(path.read_text());paths.append(path)
            for row in old['norms']:
                n=row['n']
                if n<=N:assert f[n].norm().overlaps(arb(row['density_norm']));oldcomparisons.append(n)
    cases=[]
    for M in range(1,N//9+1):
        last=M*9;delta=F(4,9);kap=B*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(last+1,last)
        model=PrefixMajorant(2,9,B,[d[n] for n in range(1,last+1)],[e[n] for n in range(9,last,9)],s,F(243,104),kap)
        result=certificate(model,2);baseq=result['w_dyadic_exponent'];q=baseq
        best,record=try_box(model,q);assert best;attempts=[record]
        while q>1:
            trial=q-1;box,record=try_box(model,trial);attempts.append(record)
            if box is None:break
            best=box;q=trial
        result['adaptive']=best;result['adaptive_attempts']=attempts
        if family=='candidate':
            assert amplitude**9<2**38
            result['restored_radius_exponent_integer']=(q+38)//4+1
        casepath=ROOT/'verification'/f'{family}{index}_N{last}_box.json';casepath.write_text(json.dumps(clean(result),indent=2)+'\n')
        cases.append(dict(N=last,box_q=baseq,adaptive_q=q,radius_exponent=F(q,4),scalar_checks=result['scalar_coefficient_checks'],path=str(casepath)))
        print(json.dumps(clean(dict(family=family,root=index,stage='box',case=cases[-1],elapsed_s=time.monotonic()-started))),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,family=family,root_index=index,root_interval=I,
        root=b.str(65,radius=True),bits=bits,N=N,B=B,s=s,norms=normrows,harmonics=hrows,obstructions=obstructions,counts=solver.counts,
        old_norm_overlap_indices=oldcomparisons,boxes=cases,inputs={str(p):sha256(p.read_bytes()).hexdigest() for p in paths},actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'{family}{index}_checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    brief={key:result[key] for key in ['family','root_index','N','bits','counts','boxes','actual_elapsed_s']};print(json.dumps(clean(brief)),flush=True);return brief

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=['two_mode','candidate','all'],default='all');ap.add_argument('--roots',default='1,2,3,4');ap.add_argument('--bits',type=int,default=1536);ap.add_argument('--N',type=int);args=ap.parse_args()
    started=time.monotonic();rows=[];failures=[]
    for family in (['two_mode','candidate'] if args.family=='all' else [args.family]):
        N=args.N or (36 if family=='two_mode' else 27)
        for index in map(int,args.roots.split(',')):
            try:rows.append(run_one(family,index,N,args.bits))
            except Exception as exc:
                fail=dict(family=family,root=index,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(t.filename).name,line=t.lineno) for t in traceback.extract_tb(exc.__traceback__)])
                (ROOT/'verification'/f'{family}{index}_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');failures.append(fail);print(json.dumps(fail),flush=True)
            (ROOT/'verification'/f'{args.family}_partial.json').write_text(json.dumps(clean(dict(rows=rows,failures=failures)),indent=2)+'\n')
    for name in ['other_certified_prefixes.py','pure_cartesian_ball.py','certified_prefix_majorant.py','resonance_block_majorant.py','certified_initial_majorants.py','adaptive_majorant_boxes.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    (ROOT/'verification'/f'{args.family}_checks.json').write_text(json.dumps(clean(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=not failures,rows=rows,failures=failures,actual_elapsed_s=time.monotonic()-started)),indent=2)+'\n')
if __name__=='__main__':main()
