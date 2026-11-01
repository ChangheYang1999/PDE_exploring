"""Independent Cartesian audit of fixed-stride cached logarithmic products."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from laurent_log_audit import Q,Poly,L,parse
from maximal_log_cartesian_check import poisson
from packed_log_audit import load_module,cols_to_laurent


def exact_case(mod,delta,initial,N):
    ring=mod.make_ring('fmpq',512)
    first=[str(initial.get(2*j+1,Q(0))) for j in range((max(initial)+1)//2)]
    obj=mod.LogFarField(ring,int(delta.p),int(delta.q),first)
    c=1/(1-delta);F,G,XF,YF,XG,YG={},{},{},{},{},{};rows=[]
    for n in range(1,N+1):
        p=1-n*delta
        if n==1:F[n]=parse(p,{k:[v] for k,v in initial.items()})
        else:
            non=L(p,0,[])
            for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
            lam=(n-1)*(c-1);term=non.scale(1/lam);ans=term
            while term.a:
                term=term.dt().scale(c/lam);ans=ans+term
            F[n]=ans
            assert (F[n].scale(-lam)+F[n].dt().scale(c)+non).zero()
            assert obj.step_fast2(N)==n
        G[n]=poisson(F[n]);XF[n],YF[n]=F[n].X(),F[n].Y();XG[n],YG[n]=G[n].X(),G[n].Y()
        assert (cols_to_laurent(obj.f[n],p,False)-F[n]).zero(),('cached density',n)
        assert (cols_to_laurent(obj.g[n],p+1,True)-G[n]).zero(),('cached stream',n)
        rows.append(dict(n=n,density_exact=True,stream_exact=True))
    return dict(delta=str(delta),initial={str(k):str(v) for k,v in initial.items()},N=N,checks=rows)


def main():
    start=time.monotonic();target=Path('research/45_cached_log_products');(target/'sources').mkdir(parents=True,exist_ok=True);(target/'verification').mkdir(exist_ok=True)
    hashes={}
    for filename in ['ffcore.py','logff.py']:
        raw=(Path('../a4-num/code')/filename).read_bytes();(target/'sources'/filename).write_bytes(raw);hashes[filename]=sha256(raw).hexdigest()
    load_module('ffcore',target/'sources/ffcore.py');mod=load_module('audited_cached_logff',target/'sources/logff.py')
    rows=[]
    for delta,initial,N in [(Q(2,3),{1:Q(1)},30),(Q(4,9),{1:Q(1)},30),(Q(1,2),{1:Q(2,3),3:Q(-1,5),5:Q(1,11)},16)]:
        rows.append(exact_case(mod,delta,initial,N));print('passed',str(delta),N,time.monotonic()-start,flush=True)
    # Test API behavior when a cached object is reused with an increased target.
    ring=mod.make_ring('fmpq',512);short=mod.LogFarField(ring,2,3,['1']);long=mod.LogFarField(ring,2,3,['1']);change=None
    for n in range(2,14):
        long.step_fast2(13)
        try:short.step_fast2(5 if n<=5 else 13)
        except Exception as e:
            change=dict(first_failure_n=n,kind=type(e).__name__,fixed_initial_target=5,increased_target=13);break
        actual=cols_to_laurent(short.f[n],1-Q(2,3)*n,False);expected=cols_to_laurent(long.f[n],1-Q(2,3)*n,False)
        if not (actual-expected).zero():
            change=dict(first_failure_n=n,kind='incorrect density after cached target increase',fixed_initial_target=5,increased_target=13);break
    record=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),source_sha256=hashes,
      code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),cartesian_cases=rows,cached_target_increase=change,
      actual_elapsed_s=time.monotonic()-start)
    (target/'verification/checks.json').write_text(json.dumps(record,indent=2)+'\n')
    print('target increase',change,'complete',record['actual_elapsed_s'],flush=True)

if __name__=='__main__':main()
