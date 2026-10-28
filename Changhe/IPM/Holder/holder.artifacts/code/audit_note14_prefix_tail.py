"""Independent prefix coverage and exact recombination with a homogeneous tail.

The cell driver is not imported. Only immutable completed task records are read.
The analytic tail is proved in note14_certificate/homogeneous_tail/PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json
from flint import arb, ctx
from audit_note14_replay import check_profile
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'05_team_audit/note14_certificate/homogeneous_tail/PROOF.md'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ar(x): return arb(str(x))
def exact(v):
    assert v.is_finite()
    return Q(str(v.lower().fmpq())),Q(str(v.upper().fmpq()))
def floor(v,n=10):
    k=(v*10**n).__floor__(); sign='-' if k<0 else ''; k=abs(k)
    return f'{sign}{k//10**n}.{k%10**n:0{n}d}'
def record(v):
    lo,hi=exact(v)
    return dict(lower=str(lo),upper=str(hi),display=v.str(45,more=True))
def a3(a,N=100):
    # Independent arrangement of the positive series in the tail proof.
    coefficient=arb(1); total=arb(0)
    for k in range(N):
        total+=coefficient*arb(4)**(-k)*(3/(a+2+2*k)-1/(a+4+2*k))
        coefficient*=arb(2*k+1)/(2*k+2)
    total*=3/(4*arb.pi())
    remainder=3*arb(4)**(-N)/(arb.pi()*(a+2+2*N))
    return total+arb(0).union(remainder)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('directory'); parser.add_argument('--task-count',type=int,required=True)
    parser.add_argument('--out',required=True); parser.add_argument('--claimed')
    args=parser.parse_args()
    base=(ROOT/args.directory).resolve(); out=(ROOT/args.out).resolve()
    assert base.is_relative_to(ROOT) and out.is_relative_to(ROOT)
    m=json.loads((base/'manifest.json').read_text()); p=m['params']; source=m['source_hashes']
    assert 1<=args.task_count<=len(m['tasks'])
    for name,h in source.items(): assert sha(ROOT/name)==h,(name,'source')
    aq,bq,cq,lq=map(Q,(p['alpha'],p['b'],p['c'],p['lam']))
    assert 0<aq<1 and bq>0 and lq>0
    profile=check_profile(aq,lq)
    low=Q(str(p['rho_min'])); middle=Q(str(p['rho_m']))
    assert 0<low<Q(1,2) and 0<middle<1 and p['prec']>=80 and p['depth']>=0
    sums={'near':[Q(0),Q(0)],'middle':[Q(0),Q(0)]}
    cover={'near':[],'middle':[]}; cells=0; records=[]
    for index,task in enumerate(m['tasks'][:args.task_count]):
        path=base/f'task_{index:05d}.json'; r=json.loads(path.read_text())
        assert r['index']==index and r['task']==task and r['source_hashes']==source
        kind=task['kind']; assert kind in cover and task['depth']==p['depth']
        nt=task['ntheta']; assert isinstance(nt,int) and nt>=4 and nt%2==0
        edges=list(map(Q,task['edges'])); assert len(edges)>=2
        for left,right in zip(edges,edges[1:]):
            assert 0<left<right; cover[kind].append((left,right))
        lo,hi=map(Q,(r['interval']['lower'],r['interval']['upper'])); assert lo<=hi
        sums[kind][0]+=lo; sums[kind][1]+=hi
        assert isinstance(r['cells'],int) and r['cells']>=0; cells+=r['cells']
        for e in r['errors'].values(): assert Q(e['lower'])>=0 and Q(e['upper'])>=Q(e['lower'])
        records.append(dict(index=index,path=str(path.relative_to(ROOT)),sha256=sha(path),cells=r['cells']))
    ends={}
    for kind,start in [('near',low),('middle',middle)]:
        assert cover[kind]
        cursor=start
        for left,right in sorted(cover[kind]):
            assert left==cursor,(kind,'gap or overlap',left,cursor);cursor=right
        ends[kind]=cursor
    assert ends['near']==Q(1,2) and ends['middle']>1
    # Explicitly ensure every prescribed near task has been included.
    assert sum(t['kind']=='near' for t in m['tasks'])==sum(m['tasks'][i]['kind']=='near' for i in range(args.task_count))
    ctx.prec=320; a,b,c,lam=map(ar,(aq,bq,cq,lq)); R=ar(ends['middle'])
    condition=lam*(1+arb(2)**(-a)); assert condition>=1,'projection does not dominate limiting cone'
    H=((b+arb(1)/2)**2+b*b).sqrt()
    B=arb.max(H**a+abs(c),arb(1)/2+arb(2)**(-a))
    q=1/(4*R*R); factor=(1-q)**2
    tail_main=2*a3(a)*R**(a-1)/(1-a)
    tail_error=2*B/(R*factor)+R**(a-3)/(2*(3-a)*factor)
    eps=ar(low);eta=ar(middle)
    inner=eps**a/a+eps*eps*(arb(1)/2+eps**a)/(2*(1-eps)**2)
    sliver=arb(2)**(a+3)*eta**(a+3)/(arb.pi()*(a+3)*(1-eta*eta).sqrt())
    error=2*exact(inner)[1]+exact(sliver)[1]+exact(tail_error)[1]
    lo=2*sums['near'][0]+sums['middle'][0]+exact(tail_main)[0]-error
    hi=2*sums['near'][1]+sums['middle'][1]+exact(tail_main)[1]+error
    lower=max(Q(0),lo,-hi)+Q(1,2)
    if args.claimed: assert Q(args.claimed)<=lower
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(aq),b=str(bq),shift=str(cq),lam=str(lq),
        task_count=args.task_count,total_manifest_tasks=len(m['tasks']),cells=cells,radius=str(ends['middle']),
        source_hashes=source,manifest_sha256=sha(base/'manifest.json'),profile_certificate_sha256=profile,
        task_files=records,radial_intervals={k:len(v) for k,v in cover.items()},
        near=dict(lower=str(sums['near'][0]),upper=str(sums['near'][1])),
        middle=dict(lower=str(sums['middle'][0]),upper=str(sums['middle'][1])),
        tail_main=record(tail_main),tail_error=record(tail_error),H=record(H),B=record(B),
        projection_condition=record(condition),a3=record(a3(a)),inner=record(inner),sliver=record(sliver),
        I0=dict(lower=str(lo),upper=str(hi),lower_decimal=floor(lo,16),upper_decimal=floor(hi+Q(1,10**16),16)),
        exact_D_lower=str(lower),safe_D_lower_10_places=floor(lower),
        analytic_proof_sha256=sha(PROOF),auditor_sha256=sha(Path(__file__)),
        profile_auditor_sha256=sha(ROOT/'code/audit_note14_replay.py'),
        verdict='NUMERICAL CHECK PASSED; theorem acceptance additionally requires the independent homogeneous-tail proof audit')
    out.mkdir(parents=True,exist_ok=True);(out/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['time_utc','alpha','task_count','cells','radius','safe_D_lower_10_places']},indent=2))
    print('tail main',tail_main.str(20,more=True),'tail error',tail_error.str(20,more=True))
if __name__=='__main__': main()
