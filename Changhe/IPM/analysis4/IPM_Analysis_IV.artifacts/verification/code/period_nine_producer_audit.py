"""Finite independent Cartesian checks of the Q9 largest-root checkpoint."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import gzip,json,pickle,sys,time,traceback
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,fmpq,ctx
from pure_cartesian_ball import Tuning,refine_root,ball
from integer_period_high_order_audit import Laurent,field
from compact_response_bounds import Response
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/273_period_nine_finite_audit');OUT=ROOT/'verification'
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p,r=None):
    if r is None:r=p.read_bytes()
    return dict(path=str(p),sha256=sha256(r).hexdigest(),bytes=len(r))
def disp(x):return x.str(40,radius=True)
def main():
    start=time.monotonic();ctx.prec=1024
    pp=Path('research/267_period_nine_tuning/verification/obstruction_checks.json');pr=pp.read_bytes();pol=json.loads(pr);assert pol['all_checks_pass']
    b,I=refine_root(list(map(int,pol['primitive_coefficients'])),pol['real_roots'][9]['interval'],1152)
    source=Path('../a4-num/ckpt/q9_r10_check_p512.pkl');raw=source.read_bytes();source_ref=ref(source,raw);state=pickle.loads(raw);del raw
    assert state['ring']=='arb' and state['prec']==512 and state['stopped'] is None and F(state['delta_exact'])==F(2,9)
    assert max(state['f'])==99 and max(state['g'])==99
    d=arb(*unpack(state['delta_pack']));c=arb(*unpack(state['c_l_pack']));assert d.contains(fmpq(2,9)) and c.contains(fmpq(9,7))
    f={n:[arb(*unpack(v)) for v in vs] for n,vs in state['f'].items()};g={n:[arb(*unpack(v)) for v in vs] for n,vs in state['g'].items()}
    assert f[1][0]==1 and len(f[1])==2 and f[1][1].contains(b)
    hp=source.with_name(source.stem+'_H.json');hr=hp.read_bytes();hd=json.loads(hr);assert hd['period']==9 and F(hd['delta'])==F(2,9)
    lp=Path('../a4-num/logs/q9_r10_check_p512.jsonl');lr=lp.read_bytes();logs=[json.loads(v) for v in lr.splitlines()];stats={r['n']:r for r in logs if 'log10_l1' in r};assert logs[-1]['done']
    t=Tuning(1,9,4);ff,gg,hh=t.prefix(b,36);prefix=[];pc=0
    for name,own,old,odd in [('f',ff,f,1),('g',gg,g,0)]:
        for n in own:
            values=[]
            for j,v in enumerate(old[n]):
                m=2*j+odd;x=own[n].sine(m) if m else arb(0);assert x.overlaps(v),(name,n,m);pc+=1;values.append(pack(x))
            prefix.append(dict(field=name,n=n,coefficients=values))
    for r in hh:
        n=r['n'];assert r['H'].overlaps(arb(hd['H'][str(n)]['str'])) and r['sigma'].overlaps(arb(hd['sigma'][str(n)]))
    response=Response(1,9,b);responses=[]
    for n,old in sorted(hd['sigma'].items(),key=lambda v:int(v[0])):
        k=int(n)//9;x=response.full(k);assert not x.contains(0) and x.overlaps(arb(old));responses.append(dict(n=int(n),k=k,value=pack(x),display=disp(x)))
    LF={n:field(v,True) for n,v in f.items()};LG={n:field(v,False) for n,v in g.items()};degree=lambda n:mpq(1)-mpq(2*n,9)
    norms=[];counts=dict(prefix=pc,poisson=0,denominators=0,coefficient_intervals=0,resolved_intervals=0,statistics=0,nonlinear_pairs=0,nonlinear_coefficients=0);maxerr=arb(0)
    for n in range(1,100):
        P=2-n*d
        for j in range(1,len(g[n])):
            den=2*(4*j*j-P*P);assert den.contains(0)==(2*n==18*(j+1));counts['denominators']+=1
        r=LG[n].derivative(degree(n)+1).derivative(degree(n)).scale(-1)+LG[n].derivative(degree(n)+1,True).derivative(degree(n),True)-LF[n].derivative(degree(n))
        for v in r.poly.coeffs():assert v.contains(0),('poisson',n);counts['poisson']+=1
        row=dict(n=n)
        for name,vs in [('f',f[n]),('g',g[n])]:
            counts['coefficient_intervals']+=len(vs);counts['resolved_intervals']+=sum(v.is_zero() or not v.contains(0) for v in vs)
            if name=='g' and n==99:row['g_status']='final harmonic unset; full stream norm excluded';continue
            norm=sum(map(abs,vs),arb(0));log=norm.log()/arb(10).log();row[name+'_norm']=pack(norm);row[name+'_log']=disp(log);row[name+'_root']=disp((norm.log()/n).exp())
            row[name+'_norm_relative_radius']=disp(sum((v.rad() for v in vs),arb(0))/sum((abs(v.mid()) for v in vs),arb(0)))
            if name=='f':
                e=abs(ball(mpq(str(stats[n]['log10_l1'])))-log);assert e<arb('1e-9');maxerr=maxerr.max(e);counts['statistics']+=1
        norms.append(row)
    nonlinear=[]
    for n in [50,99]:
        total=Laurent()
        for i in range(1,n):
            j=n-i;total=total+LG[i].derivative(degree(i)+1)*LF[j].derivative(degree(j),True)-LG[i].derivative(degree(i)+1,True)*LF[j].derivative(degree(j));counts['nonlinear_pairs']+=1
        e=LF[n].scale(ball(mpq(2*(n-1),7)));r=total-e
        for v in r.poly.coeffs():assert v.contains(0),('nonlinear',n);counts['nonlinear_coefficients']+=1
        nonlinear.append(dict(n=n,relative_residual=disp(sum(map(abs,r.poly.coeffs()),arb(0))/sum(map(abs,e.poly.coeffs()),arb(0)))))
    ns=list(range(45,100));xs=[arb(n) for n in ns];ys=[arb(norms[n-1]['f_log']) for n in ns];xm=sum(xs,arb(0))/len(xs);ym=sum(ys,arb(0))/len(ys)
    slope=sum(((x-xm)*(y-ym) for x,y in zip(xs,ys)),arb(0))/sum(((x-xm)**2 for x in xs),arb(0))
    ctx.prec=512;v=f[99];maximum=max(map(abs,v),key=lambda x:float(x.mid()));monitor=max((x/maximum).rad() for x in v);mon=monitor.log()/arb(10).log();assert abs(float(mon.mid())-stats[99]['log10_rad_over_max'])<1e-5;ctx.prec=1024
    result=dict(at=stamp(),all_checks_pass=True,source=source_ref,polynomial=ref(pp,pr),harmonics=ref(hp,hr),log=ref(lp,lr),root_interval=I,root_ball=pack(b),initial_b=pack(f[1][1]),bits=1024,counts=counts,independent_counts=t.counts,prefix=prefix,responses=responses,norms=norms,nonlinear=nonlinear,fit_orders=[45,99],fit_slope=disp(slope),division_monitor_log10=disp(mon),maximum_printed_log_error=disp(maxerr),actual_elapsed_s=time.monotonic()-start,scope='Finite interval checks under the producer execution hypotheses. Infinite convergence is established separately in267.')
    (OUT/'checks.json.gz').write_bytes(gzip.compress(json.dumps(result,separators=(',',':')).encode(),mtime=0))
    for name in ['period_nine_producer_audit.py','pure_cartesian_ball.py','integer_period_high_order_audit.py','compact_response_bounds.py','stream_precision_audit.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    for name in ['ffcore.py','tuned_general.py','tuned_cQ.py','tuned_c3.py']:(ROOT/'sources'/('producer_'+name)).write_bytes(Path('../a4-num/code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['prefix','norms','responses','root_ball','initial_b','root_interval']}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as e:
        d=dict(at=stamp(),error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(e.__traceback__)])
        (OUT/'FAILURE.json').write_text(json.dumps(d)+'\n');print(json.dumps(d),flush=True);raise SystemExit(1)
