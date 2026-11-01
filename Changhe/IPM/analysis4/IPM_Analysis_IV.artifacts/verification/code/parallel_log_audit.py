"""Audit fork-worker arithmetic without creating processes or listeners."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time, sys, multiprocessing as mp
sys.dont_write_bytecode = True
from flint import arb, fmpq, ctx
from laurent_log_audit import Q, L, parse
from maximal_log_cartesian_check import poisson
from packed_log_audit import load_module

calls=[]
class InlinePool:
    def __init__(self, workers): self.workers=workers
    def __enter__(self): return self
    def __exit__(self, *exc): return False
    def map(self, fn, args):
        chunks=[list(chunk) for chunk,n in args]
        n=args[0][1]
        assert sorted(i for chunk in chunks for i in chunk)==list(range(1,n))
        assert len(chunks)==self.workers
        calls.append(dict(n=n,workers=self.workers,chunks=chunks))
        return [fn(arg) for arg in args]
class InlineContext:
    Pool=InlinePool

def contains_rational(ball, value):
    mm, me = ball.mid().man_exp(); rm, re = ball.rad().man_exp()
    mid = Q(int(mm)) * Q(2)**int(me); rad = Q(int(rm)) * Q(2)**int(re)
    return mid-rad <= value <= mid+rad

def compare(A, cols, even):
    count=0
    K=max(A.M,max((2*len(col) for col in cols),default=0))
    for power in range(max(len(A.a),len(cols))):
        for mode in range(0 if even else 1,K+1,2):
            k=mode//2
            actual=cols[power][k] if power<len(cols) and k<len(cols[power]) else arb(0)
            expected=2*A.a[power][A.M+mode] if power<len(A.a) and 0<mode<=A.M else Q(0)
            assert contains_rational(actual, expected),(power,mode,str(actual),str(expected))
            count+=1
    return count

def main():
    start=time.monotonic(); root=Path('research/65_parallel_log_audit'); hashes={}
    for name in ['ffcore.py','logff.py']:
        data=Path('../a4-num/code',name).read_bytes();(root/'sources'/name).write_bytes(data);hashes[name]=sha256(data).hexdigest()
    load_module('ffcore',root/'sources/ffcore.py');mod=load_module('parallel_audited_logff',root/'sources/logff.py')
    original=mp.get_context
    def inline_context(kind):
        assert kind=='fork'
        return InlineContext()
    mp.get_context=inline_context
    rows=[]
    try:
        for delta, initial, N in [(Q(2,3),{1:Q(1)},24),(Q(4,9),{1:Q(1)},24),(Q(1,2),{1:Q(2,3),3:Q(-1,5),5:Q(1,11)},18)]:
            first=[str(initial.get(2*j+1,Q(0))) for j in range((max(initial)+1)//2)]
            obj=mod.LogFarField(mod.make_ring('arb',512),int(delta.p),int(delta.q),first)
            c=1/(1-delta); F={};G={};XF={};YF={};XG={};YG={};counts=0
            for n in range(1,N+1):
                p=1-n*delta
                if n==1:F[n]=parse(p,{m:[a] for m,a in initial.items()})
                else:
                    non=L(p,0,[])
                    for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
                    lam=(n-1)*(c-1);term=non.scale(1/lam);ans=term
                    while term.a:
                        term=term.dt().scale(c/lam);ans=ans+term
                    F[n]=ans
                    assert obj.step_fast_parallel([2,4,7][n%3])==n
                G[n]=poisson(F[n]);XF[n]=F[n].X();YF[n]=F[n].Y();XG[n]=G[n].X();YG[n]=G[n].Y()
                counts+=compare(F[n],obj.f[n],False)+compare(G[n],obj.g[n],True)
            rows.append(dict(delta=str(delta),input={str(m):str(a) for m,a in initial.items()},N=N,coefficient_containments=counts,all_pass=True))
            print(json.dumps(rows[-1]),flush=True)
    finally:mp.get_context=original
    # Check exact dyadic serialization at precisions and scales not confined to the recurrence.
    packchecks=[]
    for prec in [80,512,768]:
        ctx.prec=prec
        for exponent in [-2000,-400,0,400,2000]:
            for sign in [-1,0,1]:
                midpoint=arb(sign)*arb(2)**exponent*(1+arb(2)**(-prec+8))
                x=arb(midpoint,arb(2)**(exponent-prec+16))
                p=mod._arb_pack(x); y=mod._arb_unpack(p)
                assert y.contains(x),(prec,exponent,sign)
                packchecks.append(dict(precision=prec,exponent=exponent,sign=sign,enclosure_preserved=True))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),source_sha256=hashes,
        method='actual worker and parent arithmetic, with Pool.map replaced by sequential calls; no child process or listener created',
        cases=rows,partition_checks=calls,dyadic_pack_checks=packchecks,all_pass=True,actual_elapsed_s=time.monotonic()-start)
    (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['parallel_log_audit.py','laurent_log_audit.py','maximal_log_cartesian_check.py','packed_log_audit.py']:
        (root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(all_pass=True,actual_elapsed_s=result['actual_elapsed_s'],partition_count=len(calls))),flush=True)

if __name__=='__main__':main()
