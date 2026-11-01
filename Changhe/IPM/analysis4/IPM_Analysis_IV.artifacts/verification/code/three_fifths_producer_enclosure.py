"""Artifact hypotheses for the delta3/5 tuned interval producer."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import argparse,gzip,json,pickle,sys,time,traceback
sys.dont_write_bytecode=True
from flint import arb,fmpq,ctx
from pure_cartesian_ball import refine_root
from stream_precision_audit import unpack
ROOT=Path('research/208_three_fifths_producer_enclosure')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')

def one(index):
    start=time.monotonic();ctx.prec=1536
    op=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');ob=json.loads(op.read_text())
    b,I=refine_root(ob['primitive_coefficients'],ob['real_roots'][index-1]['interval'],1600)
    cp=Path('research/202_three_fifths_numerical_audit/verification')/f'root{index}_checks.json';prev=json.loads(cp.read_text())
    path=Path('../a4-num/ckpt')/f'tuned35_r{index}_p1024.pkl';raw=path.read_bytes();digest=sha256(raw).hexdigest();size=len(raw);state=pickle.loads(raw);del raw
    assert state['ring']=='arb' and state['prec']==1024 and state['stopped'] is None
    assert Fraction(state['delta_exact'])==Fraction(3,5) and max(state['f'])==300
    d=arb(*unpack(state['delta_pack']));c=arb(*unpack(state['c_l_pack']))
    assert d.contains(fmpq(3,5)) and c.contains(fmpq(5,2))
    f1=[arb(*unpack(v)) for v in state['f'][1]]
    assert len(f1)==2 and f1[0]==1 and f1[1].contains(b)
    sp=Path(prev['source']['archive']);compressed=sp.read_bytes();assert sha256(compressed).hexdigest()==prev['source']['archive_sha256']
    saved=pickle.loads(gzip.decompress(compressed));compared=0
    for field in ['f','g']:
        for n,values in saved[field].items():
            if n>40:continue
            assert state[field][n]==values,(index,field,n)
            compared+=len(values)
    hp=path.with_name(path.stem+'_H.json');hr=hp.read_bytes();hd=json.loads(hr)
    assert hd['period']==10 and hd['delta']=='3/5'
    responses=[]
    for n in range(10,300,10):
        sigma=arb(hd['sigma'][str(n)])
        assert not sigma.contains(0) and str(n) in hd['H']
        responses.append(n)
    assert '300' not in hd['H']
    denominator_checks=density_checks=0;resonances=[]
    for n in range(1,301):
        P=2-n*d
        if n>=2:
            assert (n-1)*(c-1)>0;density_checks+=1
        for j in range(1,len(state['g'][n])):
            denominator=2*(4*j*j-P*P)
            resonant=3*n==10*(j+1)
            assert denominator.contains(0)==resonant,(index,n,j)
            denominator_checks+=1
            if resonant:resonances.append(n)
    assert resonances==list(range(10,301,10))
    sources=[]
    for name in ['ffcore.py','tuned_general.py','tuned_cQ.py','tuned_c3.py']:
        p=Path('../a4-num/code')/name;raw=p.read_bytes()
        archived=Path('research/202_three_fifths_numerical_audit/sources')/('numerical_'+name)
        assert archived.read_bytes()==raw
        (ROOT/'sources'/name).write_bytes(raw)
        sources.append(dict(path=str(p),sha256=sha256(raw).hexdigest()))
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,root_index=index,maximum_order=300,parameter_containment=True,root_containment=True,
        prefix_coefficients_compared=compared,poisson_denominator_positions=denominator_checks,
        nonresonant_denominator_checks=denominator_checks-len(resonances),positive_density_divisors=density_checks,
        resonant_orders=resonances,nonzero_response_orders=responses,root_interval=I,
        source=dict(path=str(path),sha256=digest,bytes=size,harmonics_path=str(hp),harmonics_sha256=sha256(hr).hexdigest()),
        source_files=sources,final_stream_status='Order300 has an untuned kernel and its full stream norm is excluded.',actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['root_interval','source_files','source']}),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4,1,3,2');args=ap.parse_args()
    for index in map(int,args.roots.split(',')):
        try:one(index)
        except Exception as exc:
            result=dict(checked_at_utc=stamp(),root=index,error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            (ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);raise SystemExit(1)
    for name in ['three_fifths_producer_enclosure.py','pure_cartesian_ball.py','stream_precision_audit.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())

if __name__=='__main__':main()
