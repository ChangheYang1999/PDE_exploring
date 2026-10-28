"""Replace the symmetric inner-disk remainder in an audited prefix integral.

No integration driver is imported. Completed task intervals are summed as exact
rationals. The new local analytic formula is evaluated independently at 320 bits.
This produces a numerical check, whose theorem use requires the pole proof audit.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json
from flint import arb, ctx
from audit_note14_replay import check_profile
ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'05_team_audit/note14_certificate/pole_profile/PROOF.md'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def bounds(record):
    lo, hi = Q(record['lower']), Q(record['upper'])
    assert lo <= hi
    return lo, hi

def abounds(value):
    assert value.is_finite()
    return Q(str(value.lower().fmpq())), Q(str(value.upper().fmpq()))

def rec(value):
    lo, hi = abounds(value)
    return dict(lower=str(lo), upper=str(hi), display=value.str(45, more=True))

def floor(value, n=10):
    k = (value*10**n).__floor__()
    s = '-' if k < 0 else ''
    k = abs(k)
    return f'{s}{k//10**n}.{k%10**n:0{n}d}'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('audit')
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    audit, manifest, out = [(ROOT/v).resolve() for v in (args.audit,args.manifest,args.out)]
    assert all(p.is_relative_to(ROOT) for p in (audit,manifest,out))
    old = json.loads(audit.read_text()); m = json.loads(manifest.read_text()); p = m['params']
    assert sha(manifest) == old['manifest_sha256']
    assert sha(ROOT/'code/audit_note14_prefix_tail.py') == old['auditor_sha256']
    assert sha(ROOT/'code/audit_note14_replay.py') == old['profile_auditor_sha256']
    assert sha(ROOT/'05_team_audit/note14_certificate/homogeneous_tail/PROOF.md') == old['analytic_proof_sha256']
    assert m['source_hashes'] == old['source_hashes']
    for name,h in m['source_hashes'].items(): assert sha(ROOT/name)==h
    aq,bq,cq,lq = map(Q,(p['alpha'],p['b'],p['c'],p['lam']))
    assert (str(aq),str(bq),str(cq),str(lq)) == (old['alpha'],old['b'],old['shift'],old['lam'])
    profile=check_profile(aq,lq)
    assert profile == old['profile_certificate_sha256']
    sums={k:[Q(0),Q(0)] for k in ('near','middle')}
    coverage={k:[] for k in sums}; cells=0
    assert len(old['task_files']) == old['task_count']
    for index,entry in enumerate(old['task_files']):
        path=manifest.parent/f'task_{index:05d}.json'
        assert path == ROOT/entry['path'] and sha(path)==entry['sha256']
        r=json.loads(path.read_text()); task=m['tasks'][index]
        assert index==r['index']==entry['index'] and r['task']==task
        assert r['source_hashes']==m['source_hashes']
        assert r['cells']==entry['cells']; cells+=r['cells']
        kind=task['kind']; lo,hi=bounds(r['interval'])
        sums[kind][0]+=lo; sums[kind][1]+=hi
        edges=list(map(Q,task['edges']))
        coverage[kind].extend(zip(edges,edges[1:]))
    assert cells==old['cells']
    epsq=Q(str(p['rho_min'])); etaq=Q(str(p['rho_m']))
    for kind,begin,end in [('near',epsq,Q(1,2)),('middle',etaq,Q(old['radius']))]:
        cursor=begin
        for left,right in sorted(coverage[kind]):
            assert left==cursor and left<right
            cursor=right
        assert cursor==end and tuple(sums[kind])==bounds(old[kind])
    assert sum(t['kind']=='near' for t in m['tasks']) == sum(t['kind']=='near' for t in m['tasks'][:old['task_count']])
    inn=bounds(old['inner'])[1]; sli=bounds(old['sliver'])[1]
    tm=bounds(old['tail_main']); te=bounds(old['tail_error'])[1]
    base_lo=2*sums['near'][0]+sums['middle'][0]+tm[0]
    base_hi=2*sums['near'][1]+sums['middle'][1]+tm[1]
    assert (base_lo-2*inn-sli-te,base_hi+2*inn+sli+te)==bounds(old['I0'])
    ctx.prec=320
    a,b,c,lam,eps=[arb(str(v)) for v in (aq,bq,cq,lq,epsq)]
    assert 0<a<1 and b>0 and lam>0 and 0<eps<arb(1)/2
    k=arb(2)**(a-1)
    condition1=c+arb(1)/2-(lam+k)*eps**a
    condition2=arb(1)/2-lam*eps**a
    assert condition1>=0 and condition2>=0
    A=(1+a/2).gamma()/(2*arb.pi().sqrt()*(arb(3)/2+a/2).gamma())
    main=lam*A*eps**a/a+eps*eps/4
    clamp_error=a*eps/(arb.pi()*(1-2*eps)**(1-a))
    cross_error=eps**(a+2)/((a+2)*(1-eps)**2)
    error=clamp_error+cross_error
    ml,mh=abounds(main); eu=abounds(error)[1]
    lo=base_lo+2*ml-2*eu-sli-te
    hi=base_hi+2*mh+2*eu+sli+te
    assert lo<=hi
    lower=max(Q(0),lo,-hi)+Q(1,2)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(aq),b=str(bq),shift=str(cq),lam=str(lq),epsilon=str(epsq),
        old_audit_path=str(audit.relative_to(ROOT)),old_audit_sha256=sha(audit),manifest_path=str(manifest.relative_to(ROOT)),
        manifest_sha256=sha(manifest),task_count=old['task_count'],cells=cells,profile_certificate_sha256=profile,
        condition1_margin=rec(condition1),condition2_margin=rec(condition2),A=rec(A),main_per_pole=rec(main),
        clamp_error_per_pole=rec(clamp_error),cross_error_per_pole=rec(cross_error),error_per_pole=rec(error),
        I0=dict(lower=str(lo),upper=str(hi),lower_decimal=floor(lo,16),upper_decimal=floor(hi+Q(1,10**16),16)),
        exact_D_lower=str(lower),safe_D_lower_10_places=floor(lower),
        gain_over_old_lower=str(lower-Q(old['exact_D_lower'])),
        analytic_proof_sha256=sha(PROOF),auditor_sha256=sha(Path(__file__)),
        verdict='NUMERICAL CHECK PASSED; theorem use requires separate acceptance of the pole-disk analytic proof')
    out.mkdir(parents=True,exist_ok=True)
    (out/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('time_utc','alpha','epsilon','task_count','safe_D_lower_10_places')},indent=2))

if __name__=='__main__': main()
