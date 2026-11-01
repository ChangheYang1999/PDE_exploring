"""Independent Cartesian and continuum residual audit of the frozen tuned prefix."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from types import SimpleNamespace
from fractions import Fraction as Rat
import ast
import gzip
import json
import pickle
import sys
import time
sys.dont_write_bytecode = True
from flint import arb, ctx
from gmpy2 import mpq as Q
from stream_precision_audit import unpack


def run():
    start = time.monotonic()
    ctx.prec = 1536
    root = Path('research/162_deep_tuned_residuals')
    out = root/'verification'
    helper = Path('code/tuned_checkpoint_audit.py')
    tree = ast.parse(helper.read_text())
    definitions = [node for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))]
    namespace = {'__name__': 'independent_residual_helpers', 'zero': arb(0),
                 'text': lambda x: x.str(50, radius=True)}
    exec(compile(ast.Module(body=definitions, type_ignores=[]), helper.name, 'exec'), namespace)
    L, rb, field, certified_sup, evaluate = [namespace[name] for name in ['L','rb','field','certified_sup','evaluate']]
    sources = {}
    reconstruction = Path('research/141_tuned_completed_prefix/verification/reconstruction.json')
    rec = json.loads(reconstruction.read_text())
    state = {'f':{}, 'g':{}}
    for path, expected in [(Path(rec['base_archive']),rec['base_uncompressed_sha256']),
                           (reconstruction.parent/rec['extension_archive'],rec['extension_uncompressed_sha256'])]:
        raw = gzip.decompress(path.read_bytes())
        assert sha256(raw).hexdigest() == expected
        piece = pickle.loads(raw)
        sources[str(path)] = dict(raw_sha256=expected,compressed_sha256=sha256(path.read_bytes()).hexdigest())
        for key in state:
            state[key].update({n:v for n,v in piece[key].items() if n<=321})
        del raw,piece
    f = {n:[arb(*unpack(v)) for v in row] for n,row in state['f'].items()}
    g = {n:[arb(*unpack(v)) for v in row] for n,row in state['g'].items()}
    assert all(n in f and n in g for n in range(1,322))
    F = {n:field(row,True) for n,row in f.items()}
    G = {n:field(row,False) for n,row in g.items()}
    XG = {n:G[n].diff(Q(2)-Q(2*n,3)) for n in G}
    YG = {n:G[n].diff(Q(2)-Q(2*n,3),True) for n in G}
    XF = {n:F[n].diff(Q(1)-Q(2*n,3)) for n in F}
    YF = {n:F[n].diff(Q(1)-Q(2*n,3),True) for n in F}
    reference = Path('../a4-num/notes/eval_tuned_b1_p1024_N320.json')
    data = json.loads(reference.read_text())
    (root/'sources/peer_evaluation.json').write_bytes(reference.read_bytes())
    (root/'sources/peer_evaluate_series.py').write_bytes(Path('../a4-num/code/evaluate_series.py').read_bytes())
    rows=[]
    text=lambda x:x.str(50,radius=True)
    steps=4096
    for N in [40,80,160,320]:
        for R in [Q(1,5),Q(1,4),Q(1,2),Q(1)]:
            z=(-rb(Q(2,3))*rb(R).log()).exp()
            moments=3 if N==320 else 1
            transforms=[]
            for series in [XG,YG,XF,YF,F]:
                sums=[L() for _ in range(moments)]
                power=arb(1)
                for n in range(1,N+1):
                    for j in range(moments):
                        sums[j]=sums[j]+series[n].scale(power*(n-1)**j)
                    power*=z
                transforms.append(sums)
            A,B,C,D,P=transforms
            linear=[]
            for j in range(moments):
                acc=L()
                for n in range(1,N+1):
                    acc=acc+F[n].scale(-2*(n-1)**(j+1)*z**(n-1))
                linear.append(acc)
            T0=A[0]*D[0]-B[0]*C[0]
            residual=linear[0]+T0.scale(z)
            coeff=residual.sine_coeffs()
            bounds={str(k):certified_sup(coeff,k,steps) for k in range(3)}
            increment=F[N+1].scale(z**N).sine_coeffs()
            nextbounds={str(k):certified_sup(increment,k,steps) for k in range(3)}
            radial={}
            if N==320:
                T1=A[1]*D[0]+A[0]*D[1]-B[1]*C[0]-B[0]*C[1]
                T2=A[2]*D[0]+(A[1]*D[1]).scale(2)+A[0]*D[2]-B[2]*C[0]-(B[1]*C[1]).scale(2)-B[0]*C[2]
                E1=linear[1]+(T0+T1).scale(z)
                E2=linear[2]+(T0+T1.scale(2)+T2).scale(z)
                first=residual.scale(rb(Q(1,3)))-E1.scale(rb(Q(2,3)))
                second=residual.scale(rb(Q(-2,9)))+E1.scale(rb(Q(2,9)))+E2.scale(rb(Q(4,9)))
                radial={'1':certified_sup(first.sine_coeffs(),0,steps),'2':certified_sup(second.sine_coeffs(),0,steps)}
            partial=P[0].sine_coeffs()
            partials=[evaluate(partial,th) for th in [Q(3,10),Q(9,10),Q(13,10)]]
            reported=next(row for row in data['rows'] if row['N']==N and Q(str(row['R']))==R)
            comparison={}
            for label,target,key in [('residual',bounds,'resid_k'),('next_increment',nextbounds,'tail_k')]:
                comparison[label]={}
                for k in range(3):
                    value=rb(Q(str(reported[key+str(k)])))
                    lo,hi=arb(target[str(k)]['lower']),arb(target[str(k)]['upper'])
                    comparison[label][str(k)]=dict(reported_over_lower=text(value/lo),reported_over_upper=text(value/hi),within_one_percent=bool(value>lo*rb(Q(99,100)) and value<hi*rb(Q(101,100))))
            errors=[abs(v-rb(Q(str(w)))) for v,w in zip(partials,reported['S_N_at_angles'])]
            row=dict(N=N,R=str(R),residual_bounds=bounds,next_increment_bounds=nextbounds,radial_residual_bounds=radial,partial_sums=list(map(text,partials)),reported=reported,comparison=comparison,partial_sum_float_errors=list(map(text,errors)))
            rows.append(row)
            (out/'progress.json').write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
            print(json.dumps(dict(N=N,R=str(R),residual0=bounds['0'],actual_elapsed_s=time.monotonic()-start)),flush=True)
    decreases=[]
    for R in ['1/5','1/4','1/2','1']:
        group=[r for r in rows if r['R']==R]
        for prev,nextrow in zip(group,group[1:]):
            for key in ['residual_bounds','next_increment_bounds']:
                for k in ['0','1','2']:
                    passed=bool(arb(nextrow[key][k]['upper'])<arb(prev[key][k]['lower']))
                    assert passed,('decrease',R,prev['N'],nextrow['N'],key,k)
                    decreases.append(dict(R=R,N_previous=prev['N'],N_next=nextrow['N'],quantity=key,derivative=k,strict_decrease=True))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_continuum_bounds_pass=True,arithmetic_bits=ctx.prec,grid_steps=steps,input_archives=sources,source_evaluation_sha256=sha256(reference.read_bytes()).hexdigest(),rows=rows,strict_decreases=decreases,all_reported_grid_values_within_one_percent=all(v['within_one_percent'] for r in rows for label in r['comparison'].values() for v in label.values()),actual_elapsed_s=time.monotonic()-start,scope='Finite exact-profile continuum enclosures; no smaller infinite convergence radius claimed.')
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for p in [Path(__file__),helper,Path('code/stream_precision_audit.py')]:
        (root/'sources'/p.name).write_bytes(p.read_bytes())
    print(json.dumps(dict(all_continuum_bounds_pass=True,strict_decreases=len(decreases),actual_elapsed_s=result['actual_elapsed_s'])),flush=True)


if __name__=='__main__':
    try:
        run()
    except Exception as exc:
        import traceback
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/162_deep_tuned_residuals/verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure),flush=True)
        raise SystemExit(1)
