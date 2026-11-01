"""Independent Cartesian prefix and checkpoint checks for tuned single sines."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as F
import argparse, gzip, json, pickle, sys, time, traceback
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb, fmpq, ctx
from pure_cartesian_ball import Tuning, sine, ball
from integer_period_high_order_audit import Laurent,field
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/271_single_harmonic_finite_audit')
CASES={7:(2,5,'single_sin7_45_p1024'),9:(2,7,'single_sin9_47_p1024'),11:(2,9,'single_sin11_49_p1024'),17:(3,13,'single_sin17_613_p1024')}
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p,raw=None):
    if raw is None:raw=p.read_bytes()
    return dict(path=str(p),sha256=sha256(raw).hexdigest(),bytes=len(raw))
def disp(x):return x.str(38,radius=True)
def save(p,d):
    raw=json.dumps(d,separators=(',',':')).encode()
    p.write_bytes(gzip.compress(raw,mtime=0) if p.suffix=='.gz' else raw+b'\n')
def prefix(t,M,N):
    ff={1:sine(t.p(1),M,arb(1))};gg={1:t.poisson(ff[1],1)};hh=[]
    for n in range(2,N+1):
        fn=t.order(n,ff,gg)
        if t.resonant(n):
            obstruction=fn.sine(t.frequency(n)-1)
            fn=fn.project(t.B*n-1,1,t.counts,zero_mode=t.frequency(n)-1);ff[n]=fn
            R=t.continuation(n,ff,gg,arb(0));S=t.continuation(n,ff,gg,arb(1))-R
            assert not S.contains(0),('response',n,disp(S))
            H=-R/S;gg[n]=t.poisson(fn,n,H)
            hh.append(dict(n=n,H=H,sigma=S,obstruction=obstruction))
        else:ff[n]=fn;gg[n]=t.poisson(fn,n)
    return ff,gg,hh

def one(M,N,bits,nonlinear):
    start=time.monotonic();ctx.prec=bits;h,Q,tag=CASES[M];out=ROOT/'verification'/f'sin{M}';out.mkdir(exist_ok=True)
    source=Path('../a4-num/ckpt')/(tag+'.pkl');raw=source.read_bytes();meta=ref(source,raw);state=pickle.loads(raw);del raw
    hp=source.with_name(tag+'_H.json');hr=hp.read_bytes();hd=json.loads(hr)
    log=Path('../a4-num/logs')/(tag+'.jsonl');lr=log.read_bytes();logs=[json.loads(v) for v in lr.splitlines() if v.strip()];stats={r['n']:r for r in logs if 'n' in r and 'log10_l1' in r}
    assert state['ring']=='arb' and state['prec']==1024 and state['stopped'] is None
    assert F(str(state['delta_exact']))==F(2*h,Q)
    d=arb(*unpack(state['delta_pack']));c=arb(*unpack(state['c_l_pack']))
    assert d.contains(fmpq(2*h,Q)) and c.contains(fmpq(Q,Q-2*h))
    maximum=max(state['f']);assert max(state['g'])==maximum and maximum>=N+Q
    assert logs[-1].get('done') and logs[-1]['N']==maximum
    assert hd['period']==Q and F(hd['delta'])==F(2*h,Q)
    f={n:[arb(*unpack(v)) for v in state['f'][n]] for n in state['f']};g={n:[arb(*unpack(v)) for v in state['g'][n]] for n in state['g']}
    assert len(f[1])==(M+1)//2 and all(v.is_zero() for v in f[1][:-1]) and f[1][-1]==1
    producer=[]
    for name in ['ffcore.py','tuned_general.py','tuned_cQ.py','tuned_c3.py']:
        p=Path('../a4-num/code')/name;r=p.read_bytes();target=ROOT/'sources'/('producer_'+name);target.write_bytes(r);producer.append(ref(p,r))
    t=Tuning(h,Q,M+1);ff,gg,hh=prefix(t,M,N)
    counts=dict(prefix_f=0,prefix_g=0,prefix_tuning=0,poisson=0,denominators=0,responses=0,resolved_intervals=0,coefficient_intervals=0,statistics=0,nonlinear_coefficients=0,nonlinear_pairs=0)
    prefix_rows=[]
    for name,own,old,odd in [('f',ff,f,1),('g',gg,g,0)]:
        for n in range(1,N+1):
            row=[]
            for j,v in enumerate(old[n]):
                m=2*j+odd;value=own[n].sine(m) if m else arb(0)
                assert value.overlaps(v),('prefix',name,n,m,disp(value),disp(v))
                counts['prefix_'+name]+=1;row.append(pack(value))
            prefix_rows.append(dict(field=name,n=n,coefficients=row))
    hrows=[]
    for r in hh:
        n=r['n'];assert r['H'].overlaps(arb(hd['H'][str(n)]['str'])) and r['sigma'].overlaps(arb(hd['sigma'][str(n)]))
        counts['prefix_tuning']+=1;hrows.append({k:pack(v) if k!='n' else v for k,v in r.items()})
    for n,v in hd['sigma'].items():
        assert not arb(v).contains(0),('producer_response',n);counts['responses']+=1
    LF={n:field(f[n],True) for n in f};LG={n:field(g[n],False) for n in g};degree=lambda n:mpq(1)-mpq(2*h*n,Q)
    norms=[];max_log_error=arb(0);max_rad=arb(0);untuned=[]
    for n in range(1,maximum+1):
        P=2-n*d
        for j in range(1,len(g[n])):
            den=2*(4*j*j-P*P);resonance=n*2*h==2*Q*(j+1)
            assert den.contains(0)==resonance,('denominator',n,j);counts['denominators']+=1
        if n>=2:assert (n-1)*(c-1)>0
        rhs=LF[n].derivative(degree(n));a=LG[n].derivative(degree(n)+1);b=LG[n].derivative(degree(n)+1,True)
        residual=a.derivative(degree(n)).scale(-1)+b.derivative(degree(n),True)-rhs
        for v in residual.poly.coeffs():
            assert v.contains(0),('Poisson',n);counts['poisson']+=1
        excluded=(n%Q==0 and n>=Q and str(n) not in hd['H'])
        if excluded:untuned.append(n)
        row=dict(n=n)
        for name,vv in [('f',f[n]),('g',g[n])]:
            counts['coefficient_intervals']+=len(vv);counts['resolved_intervals']+=sum(v.is_zero() or not v.contains(0) for v in vv)
            norm=sum(map(abs,vv),arb(0));mid=sum((abs(v.mid()) for v in vv),arb(0));radius=sum((v.rad() for v in vv),arb(0))
            rel=radius/mid;max_rad=max_rad.max(rel)
            if name=='g' and excluded:row['g_status']='untuned final harmonic; full norm excluded';continue
            row[name+'_norm']=pack(norm);row[name+'_root']=disp((norm.log()/n).exp());row[name+'_relative_radius']=disp(rel)
            if name=='f':
                logarithm=norm.log()/arb(10).log();assert n in stats
                err=abs(arb(fmpq(str(F(str(stats[n]['log10_l1'])))))-logarithm);assert err<arb('1e-9'),('printed_log',n,disp(err));max_log_error=max_log_error.max(err);counts['statistics']+=1
        norms.append(row)
        if n%100==0:print(json.dumps(dict(at=stamp(),M=M,stage='norms_and_poisson',n=n,elapsed=time.monotonic()-start)),flush=True)
    nonlinear_rows=[]
    for n in nonlinear:
        assert 2<=n<=maximum
        total=Laurent()
        for i in range(1,n):
            j=n-i
            total=total+LG[i].derivative(degree(i)+1)*LF[j].derivative(degree(j),True)-LG[i].derivative(degree(i)+1,True)*LF[j].derivative(degree(j));counts['nonlinear_pairs']+=1
        expected=LF[n].scale(ball(mpq((n-1)*2*h,Q-2*h)));res=total-expected
        for v in res.poly.coeffs():assert v.contains(0),('nonlinear',n,disp(v));counts['nonlinear_coefficients']+=1
        rn=sum(map(abs,res.poly.coeffs()),arb(0));en=sum(map(abs,expected.poly.coeffs()),arb(0))
        nonlinear_rows.append(dict(n=n,pairs=n-1,relative_residual=disp(rn/en)))
        print(json.dumps(dict(at=stamp(),M=M,stage='nonlinear',n=n,elapsed=time.monotonic()-start)),flush=True)
    # Retain a bounded selected checkpoint, never the full producer file.
    selected={key:{n:state[key][n] for n in range(1,N+1)} for key in ['f','g']}
    raw=pickle.dumps(selected,protocol=4);compressed=gzip.compress(raw,mtime=0);sp=out/'source_prefix.pkl.gz';sp.write_bytes(compressed)
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,M=M,h=h,Q=Q,maximum_order=maximum,independent_prefix_order=N,bits=bits,counts=counts,independent_counts=t.counts,untuned_final_stream_orders=untuned,maximum_printed_l1_log_error=disp(max_log_error),maximum_norm_relative_radius=disp(max_rad),source=meta,harmonics=ref(hp,hr),log=ref(log,lr),producer_sources=producer,selected_source=ref(sp),selected_raw_sha256=sha256(raw).hexdigest(),norms=norms,independent_prefix=prefix_rows,independent_tuning=hrows,nonlinear=nonlinear_rows,scope='Finite interval checks and producer-induction hypotheses; no inferred sharp radius or asymptotic growth constant.',actual_elapsed_s=time.monotonic()-start)
    save(out/'checks.json.gz',result)
    for name in ['single_harmonic_finite_audit.py','pure_cartesian_ball.py','integer_period_high_order_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['norms','independent_prefix','independent_tuning','producer_sources']}),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--M',type=int,required=True);ap.add_argument('--N',type=int);ap.add_argument('--bits',type=int,default=2048);ap.add_argument('--nonlinear',default='50,100,200,300');a=ap.parse_args()
    try:one(a.M,a.N or 4*CASES[a.M][1],a.bits,list(map(int,a.nonlinear.split(','))))
    except Exception as exc:
        out=ROOT/'verification'/f'sin{a.M}';out.mkdir(exist_ok=True)
        fail=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        save(out/'FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)
