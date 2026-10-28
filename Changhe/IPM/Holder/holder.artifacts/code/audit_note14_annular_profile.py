"""Independent annular recombination with explicit inner and outer integrals.

Every mesh radius is an exact rational. The selected pole cutoff is chosen from
completed task endpoints. Dropped annuli are replaced by the proved quadratic
clamp enclosure. Finite optimization only selects among valid lower bounds.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,hashlib,json
from flint import arb,ctx
from audit_note14_replay import check_profile
from audit_note14_prefix_tail import a3
ROOT=Path(__file__).resolve().parents[1]
POLE=ROOT/'05_team_audit/note14_certificate/pole_profile/quadratic_clamp/PROOF.md'
PARENT=POLE.parent.parent/'PROOF.md'
TAIL=ROOT/'05_team_audit/note14_certificate/homogeneous_tail/PROOF.md'
LOWER=ROOT/'05_team_audit/note14_certificate/pole_profile/quadratic_lower/PROOF.md'
ANGULAR=ROOT/'05_team_audit/note14_certificate/homogeneous_tail/angular_error/PROOF.md'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ar(v):return arb(str(v))
def exact(v):
    assert v.is_finite()
    return Q(str(v.lower().fmpq())),Q(str(v.upper().fmpq()))
def bounds(v):
    lo,hi=Q(v['lower']),Q(v['upper']);assert lo<=hi;return lo,hi

def floor(v,n=10):
    k=(v*10**n).__floor__();s='-' if k<0 else '';k=abs(k)
    return f'{s}{k//10**n}.{k%10**n:0{n}d}'
def rec(v):
    lo,hi=exact(v);return dict(lower=str(lo),upper=str(hi),display=v.str(40,more=True))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory')
    ap.add_argument('--task-count',type=int,required=True)
    ap.add_argument('--skip-near',type=int,default=0)
    ap.add_argument('--optimize-inner',action='store_true')
    ap.add_argument('--one-sided',action='store_true',help='Use the quadratic lower bound without the sign restriction')
    ap.add_argument('--angular-tail',action='store_true')
    ap.add_argument('--out',required=True);args=ap.parse_args()
    base=(ROOT/args.directory).resolve();out=(ROOT/args.out).resolve()
    assert base.is_relative_to(ROOT) and out.is_relative_to(ROOT)
    m=json.loads((base/'manifest.json').read_text());p=m['params'];src=m['source_hashes']
    for path,h in src.items():assert sha(ROOT/path)==h,(path,'source')
    aq,bq,cq,lq=map(Q,(p['alpha'],p['b'],p['c'],p['lam']))
    assert 0<aq<1 and bq>0 and lq>0 and p['prec']>=80
    profile=check_profile(aq,lq)
    nc=sum(t['kind']=='near' for t in m['tasks'])
    assert 0<nc<args.task_count<=len(m['tasks'])
    assert all(t['kind']=='near' for t in m['tasks'][:nc])
    assert all(t['kind']=='middle' for t in m['tasks'][nc:])
    sums={k:[Q(0),Q(0)] for k in ('near','middle')};covers={k:[] for k in sums}
    near_ends=[Q(str(p['rho_min']))];near_prefix=[(Q(0),Q(0))]
    records=[];cells=0
    for index,t in enumerate(m['tasks'][:args.task_count]):
        path=base/f'task_{index:05d}.json';r=json.loads(path.read_text())
        assert r['index']==index and r['task']==t and r['source_hashes']==src
        assert t['depth']==p['depth'] and t['ntheta']>=4 and t['ntheta']%2==0
        assert isinstance(r['cells'],int) and r['cells']>=0;cells+=r['cells']
        kind=t['kind'];edges=list(map(Q,t['edges']));assert len(edges)>=2
        for left,right in zip(edges,edges[1:]):assert 0<left<right;covers[kind].append((left,right))
        lo,hi=bounds(r['interval']);sums[kind][0]+=lo;sums[kind][1]+=hi
        for value in r['errors'].values():assert 0<=Q(value['lower'])<=Q(value['upper'])
        if kind=='near':
            assert edges[0]==near_ends[-1]
            near_ends.append(edges[-1]);near_prefix.append(tuple(sums[kind]))
        records.append(dict(index=index,path=str(path.relative_to(ROOT)),sha256=sha(path),cells=r['cells']))
    ends={}
    for kind,start in [('near',Q(str(p['rho_min']))),('middle',Q(str(p['rho_m'])))]:
        cursor=start
        for left,right in sorted(covers[kind]):assert left==cursor;cursor=right
        ends[kind]=cursor
    assert ends['near']==Q(1,2) and ends['middle']>1
    assert len(near_ends)==nc+1
    ctx.prec=320;a,b,c,lam=map(ar,(aq,bq,cq,lq));R=ar(ends['middle']);eta=ar(Q(str(p['rho_m'])))
    condition_tail=lam*(1+arb(2)**(-a));assert condition_tail>=1
    H=((b+arb(1)/2)**2+b*b).sqrt();B=arb.max(H**a+abs(c),arb(1)/2+arb(2)**(-a))
    q=1/(4*R*R);factor=(1-q)**2
    tm=2*a3(a)*R**(a-1)/(1-a)
    te_original=2*B/(R*factor)+R**(a-3)/(2*(3-a)*factor)
    te_angular=4*B/(arb.pi()*R)+B/(3*R**3*factor)+R**(a-3)/(2*(3-a)*factor)
    te=arb.min(te_original,te_angular) if args.angular_tail else te_original
    sliver=arb(2)**(a+3)*eta**(a+3)/(arb.pi()*(a+3)*(1-eta*eta).sqrt())
    fixed_error=exact(te)[1]+exact(sliver)[1]
    gammaA=(1+a/2).gamma()/(2*arb.pi().sqrt()*(arb(3)/2+a/2).gamma())
    k=arb(2)**(a-1);candidates=[];selected=None;rejected=0
    indices=range(nc) if args.optimize_inner else [args.skip_near]
    for skip in indices:
        assert 0<=skip<nc
        epsq=near_ends[skip];eps=ar(epsq);assert 0<eps<arb(1)/2
        Ce=(1-2*eps)**(a-1)
        margins=[c+arb(1)/2-(lam+k)*eps**a,arb(1)/2-lam*eps**a,lam/2-a*Ce*eps**(1-a)]
        if not all(v>=0 for v in (margins[:2] if args.one_sided else margins)):
            assert args.optimize_inner, 'quadratic pole conditions fail'
            rejected+=1;continue
        main=lam*gammaA*eps**a/a+eps*eps/4
        ec=a*Ce**3*eps**(3-2*a)/(6*arb.pi()*lam*lam*(3-2*a))
        es=eps**(a+2)/((a+2)*(1-eps)**2)
        upper_clamp=arb(0) if margins[2]>=0 else a*Ce*eps/arb.pi()
        nearlo=sums['near'][0]-near_prefix[skip][0]
        nearhi=sums['near'][1]-near_prefix[skip][1]
        lo=2*nearlo+sums['middle'][0]+exact(tm)[0]+2*exact(main)[0]-2*exact(ec)[1]-2*exact(es)[1]-fixed_error
        hi=2*nearhi+sums['middle'][1]+exact(tm)[1]+2*exact(main)[1]+2*exact(es)[1]+2*exact(upper_clamp)[1]+fixed_error
        assert lo<=hi
        dl=max(Q(0),lo,-hi)+Q(1,2)
        candidates.append(dict(skip_near_tasks=skip,epsilon=str(epsq),safe_D_lower=floor(dl)))
        if selected is None or dl>selected[0]:
            selected=(dl,dict(skip_near_tasks=skip,epsilon=str(epsq),condition_margins=[rec(v) for v in margins],
                main_per_pole=rec(main),clamp_error_per_pole=rec(ec),upper_clamp_per_pole=rec(upper_clamp),smooth_error_per_pole=rec(es),
                retained_near=dict(lower=str(nearlo),upper=str(nearhi)),
                I0=dict(lower=str(lo),upper=str(hi),lower_decimal=floor(lo,16),upper_decimal=floor(hi+Q(1,10**16),16))))
    assert selected is not None
    dl,best=selected
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(aq),b=str(bq),shift=str(cq),lam=str(lq),
        one_sided=args.one_sided,angular_tail=args.angular_tail,task_count=args.task_count,total_manifest_tasks=len(m['tasks']),cells=cells,source_hashes=src,
        manifest_path=str((base/'manifest.json').relative_to(ROOT)),manifest_sha256=sha(base/'manifest.json'),
        profile_certificate_sha256=profile,task_files=records,radius=str(ends['middle']),
        tail_main=rec(tm),tail_error=rec(te),tail_error_original=rec(te_original),tail_error_angular=rec(te_angular),sliver=rec(sliver),A=rec(gammaA),H=rec(H),B=rec(B),
        tail_condition=rec(condition_tail),middle=dict(lower=str(sums['middle'][0]),upper=str(sums['middle'][1])),
        selected=best,exact_D_lower=str(dl),safe_D_lower_10_places=floor(dl),
        candidates=candidates,rejected_condition_candidates=rejected,
        analytic_sha256={str(v.relative_to(ROOT)):sha(v) for v in (POLE,PARENT,TAIL,LOWER,ANGULAR)},
        auditor_sha256=sha(Path(__file__)),dependency_sha256={str(v.relative_to(ROOT)):sha(v) for v in (ROOT/'code/audit_note14_replay.py',ROOT/'code/audit_note14_prefix_tail.py')},
        verdict='NUMERICAL CHECK PASSED; operator acceptance requires independently audited pole and tail proofs')
    out.mkdir(parents=True,exist_ok=True)
    (out/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['time_utc','alpha','task_count','radius','safe_D_lower_10_places']},indent=2))
    print('selected skip',best['skip_near_tasks'],'epsilon',best['epsilon'],'admissible candidates',len(candidates))

if __name__=='__main__':main()
