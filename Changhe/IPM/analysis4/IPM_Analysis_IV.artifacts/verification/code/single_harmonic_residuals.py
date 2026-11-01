"""Finite Cartesian residuals and rigorous full-circle supremum brackets."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import argparse,gzip,json,pickle,sys,time,traceback
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,acb,acb_poly,ctx
from integer_period_high_order_audit import Laurent,field,ball
from stream_precision_audit import unpack
from tuned_residual_continuum import sine_coefficients,supremum,text
from single_harmonic_finite_audit import CASES
ROOT=Path('research/272_single_harmonic_residuals')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def dump(p,d):p.write_bytes(gzip.compress(json.dumps(d,separators=(',',':')).encode(),mtime=0))
def ref(p,r):return dict(path=str(p),sha256=sha256(r).hexdigest(),bytes=len(r))
def main(a):
    start=time.monotonic();ctx.prec=a.bits;h,period,tag=CASES[a.M]
    out=ROOT/'verification'/f'sin{a.M}';out.mkdir(exist_ok=True)
    prior_path=Path('research/271_single_harmonic_finite_audit/verification')/f'sin{a.M}/checks.json.gz'
    priorraw=prior_path.read_bytes();prior=json.loads(gzip.decompress(priorraw));assert prior['all_checks_pass']
    source=Path('../a4-num/ckpt')/(tag+'.pkl');raw=source.read_bytes();source_ref=ref(source,raw)
    assert source_ref['sha256']==prior['source']['sha256'];state=pickle.loads(raw);del raw
    assert state['ring']=='arb' and state['prec']==1024 and Fraction(state['delta_exact'])==Fraction(2*h,period)
    hp=source.with_name(tag+'_H.json');hr=hp.read_bytes();hs=json.loads(hr);assert sha256(hr).hexdigest()==prior['harmonics']['sha256']
    assert all(str(n) in hs['H'] for n in range(period,81,period))
    f={n:field([arb(*unpack(v)) for v in state['f'][n]],True) for n in range(1,82)}
    g={n:field([arb(*unpack(v)) for v in state['g'][n]],False) for n in range(1,81)};del state
    delta=Q(2*h,period);cm=Q(2*h,period-2*h);p=lambda n:Q(1)-n*delta
    FX={n:f[n].derivative(p(n)) for n in range(1,81)};FY={n:f[n].derivative(p(n),True) for n in range(1,81)}
    GX={n:g[n].derivative(p(n)+1) for n in g};GY={n:g[n].derivative(p(n)+1,True) for n in g}
    suffix=tag.replace('_p1024','');ep=Path('../a4-num/notes')/('eval_'+suffix+'.json');er=ep.read_bytes();data=json.loads(er)
    (ROOT/'sources'/f'sin{a.M}_peer_evaluation.json').write_bytes(er)
    radii=list(map(Q,a.radii.split(','))) if a.radii else sorted({Q(str(v['R'])) for v in data['rows']})
    points=[acb((arb.pi()*j/a.steps).cos(),(arb.pi()*j/a.steps).sin()) for j in range(a.steps+1)]
    rows=[]
    for N in [10,20,40,80]:
        for R in radii:
            z=(-ball(delta)*ball(R).log()).exp();A=Laurent();B=Laurent();C=Laurent();D=Laurent();lin=Laurent();part=Laurent();power=arb(1)
            for n in range(1,N+1):
                A=A+GX[n].scale(power);B=B+GY[n].scale(power);C=C+FX[n].scale(power);D=D+FY[n].scale(power)
                lin=lin+f[n].scale(-ball(cm)*(n-1)*power);part=part+f[n].scale(power);power*=z
            res=sine_coefficients(lin+(A*D-B*C).scale(z));tail=sine_coefficients(f[N+1].scale(z**N));part=sine_coefficients(part)
            bounds={str(k):supremum(res,k,points) for k in range(3)};tails={str(k):supremum(tail,k,points) for k in range(3)}
            poly=acb_poly([acb(v) for v in part]);partials=[]
            for angle in [Q(3,10),Q(9,10),Q(13,10)]:
                th=ball(angle);partials.append(poly(acb(th.cos(),th.sin())).imag)
            peer=next(v for v in data['rows'] if v['N']==N and Q(str(v['R']))==R);comparison={}
            for name,target,prefix in [('residual',bounds,'resid_k'),('next_term',tails,'tail_k')]:
                comparison[name]={}
                for k,v in target.items():
                    x=ball(Q(str(peer[prefix+k])));lo=arb(v['lower']);hi=arb(v['upper'])
                    comparison[name][k]=dict(within_one_percent=bool(x>lo*ball(Q(99,100)) and x<hi*ball(Q(101,100))),reported_over_lower=text(x/lo),reported_over_upper=text(x/hi))
            rows.append(dict(N=N,R=str(R),residual_bounds=bounds,next_term_bounds=tails,partial_sums=list(map(text,partials)),partial_sum_errors=[text(abs(x-ball(Q(str(y))))) for x,y in zip(partials,peer['S_N_at_angles'])],reported=peer,comparison=comparison))
            dump(out/'progress.json.gz',dict(checked_at_utc=stamp(),complete=False,rows=rows,actual_elapsed_s=time.monotonic()-start))
            print(json.dumps(dict(at=stamp(),M=a.M,N=N,R=str(R),residual0=bounds['0'],elapsed_s=time.monotonic()-start)),flush=True)
    changes=[]
    for R in radii:
        group=[v for v in rows if v['R']==str(R)]
        for before,after in zip(group,group[1:]):
            for name in ['residual_bounds','next_term_bounds']:
                for k,v in before[name].items():
                    w=after[name][k];changes.append(dict(R=str(R),from_N=before['N'],to_N=after['N'],quantity=name,derivative=k,strict_decrease=bool(arb(w['upper'])<arb(v['lower'])),strict_increase=bool(arb(w['lower'])>arb(v['upper']))))
    result=dict(checked_at_utc=stamp(),complete=True,M=a.M,h=h,Q=period,bits=a.bits,grid_steps=a.steps,source=source_ref,prior_audit=ref(prior_path,priorraw),harmonics=ref(hp,hr),peer_evaluation=ref(ep,er),rows=rows,changes=changes,all_reported_within_one_percent=all(v['within_one_percent'] for r in rows for c in r['comparison'].values() for v in c.values()),actual_elapsed_s=time.monotonic()-start,scope='Finite continuum enclosures, conditional on the independently inspected producer enclosure hypotheses in271. No infinite convergence threshold inferred.')
    dump(out/'checks.json.gz',result)
    for name in ['single_harmonic_residuals.py','tuned_residual_continuum.py','single_harmonic_finite_audit.py','integer_period_high_order_audit.py','stream_precision_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    (ROOT/'sources'/'peer_evaluate_series.py').write_bytes(Path('../a4-num/code/evaluate_series.py').read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','changes']}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--M',type=int,required=True);p.add_argument('--bits',type=int,default=1024);p.add_argument('--steps',type=int,default=2048);p.add_argument('--radii');a=p.parse_args()
    try:main(a)
    except Exception as e:
        out=ROOT/'verification'/f'sin{a.M}';out.mkdir(exist_ok=True)
        failure=dict(at=stamp(),error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(e.__traceback__)])
        dump(out/'FAILURE.json.gz',failure);print(json.dumps(failure),flush=True);raise SystemExit(1)
