"""Independent exact coverage and recombination of the six table37 certificates.

No transport optimizer or submitted aggregation program is imported.
Previously audited cell programs are identified by content, and all returned
ball endpoints are recombined at 320 bits with exact outward decimal rounding.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/table37_lead'; S=BASE/'source'
OLD=ROOT/'05_team_audit/closed_form37_lead/source/code'
ALPHAS=[Q(1,1000),Q(1,100),Q(1,20),Q(1,10),Q(1,5),Q(99,100)]
ctx.prec=320

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def ar(q): return arb(str(q))
def record(v):
    assert v.is_finite()
    return dict(lower=str(v.lower().fmpq()),upper=str(v.upper().fmpq()),display=v.str(50,more=True))
def upward(v,n=10):
    q=Q(str(v.upper().fmpq()));k=-((-q*10**n).__floor__())
    return f'{k//10**n}.{k%10**n:0{n}d}'
def array(values):
    assert len(values)==17
    vs=[arb(x) for x in values];assert all(x.is_finite() and x>=0 for x in vs)
    return vs

def main():
    snapshot=load(S/'snapshot_manifest.json')
    for name,h in snapshot['sha256'].items():assert sha(S/name)==h,('snapshot',name)
    same=['local_nodes.py','mid_nodes.py','certify_local_circles_greedy.py','local_circle_greedy.py','middle_circle_plan.py','circle_transport_plan.py','certify_far_circles.py']
    for name in same: assert sha(S/'code'/name)==sha(OLD/name),('audited helper',name)
    original=ROOT/'09_uniform_comparison/lead_certificate/source'
    assert sha(S/'code/refl_nodes.py')==sha(original/'refl_nodes.py')
    old=(original/'far_nodes.py').read_text().splitlines()
    new=(S/'code/far_nodes.py').read_text().splitlines()
    assert len(old)==len(new)
    changes=[(i,a,b) for i,(a,b) in enumerate(zip(old,new),1) if a!=b]
    assert len(changes)==1 and all('sys.path.insert' in x for x in changes[0][1:])
    aggregate=load(S/'results/table37.json')
    assert Q(aggregate['delta'])==Q(1,64) and aggregate['phase_intervals']==16
    for name,h in aggregate['source_sha256'].items():assert sha(S/name)==h
    submitted={Q(r['alpha']):r for r in aggregate['rows']};assert set(submitted)==set(ALPHAS)
    coverage=[];middle={a:[arb(0) for _ in range(17)] for a in ALPHAS};seen=set();ref=None
    for path in sorted((S/'mid').glob('n512_*.json')):
        d=load(path)
        params={k:d[k] for k in ['precision_bits','angles_per_half','radial_cells','phase_intervals','integer_unit','plan_trials','groups','source_hashes']}
        if ref is None:ref=params
        else:assert params==ref
        assert d['precision_bits']>=160 and d['angles_per_half']==512 and d['radial_cells']==512
        assert d['phase_intervals']==16 and d['integer_unit']==2**44 and d['plan_trials']==17
        for name,h in d['source_hashes'].items():assert sha(S/'code'/name)==h
        keys=[(Q(r['plan_reference_alpha']),Q(r['alpha'])) for r in d['rows']]
        assert len(keys)==len(set(keys)) and set(keys)=={(a,a) for a in ALPHAS}
        lo,hi=d['row_start'],d['row_stop'];assert 0<=lo<hi<=512
        for row in d['rows']:
            a=Q(row['alpha']);v=array(row['middle_phase_intervals']);rv=array(row['residual_intervals'])
            assert all(x<=y for x,y in zip(rv,v))
            for k in range(lo,hi):
                assert (a,k) not in seen;seen.add((a,k))
            middle[a]=[x+y for x,y in zip(middle[a],v)]
        coverage.append(dict(path=str(path.relative_to(ROOT)),kind='middle',row_start=lo,row_stop=hi,sha256=sha(path)))
    assert seen=={(a,k) for a in ALPHAS for k in range(512)}
    pi=arb.pi();delta=arb(1)/64;phase_factor=1/(pi/64).cos();results=[]
    for a in ALPHAS:
        aa=ar(a);a2=arb(2)**(1+aa/2)/(pi*(aa+2))
        small=2*a2*delta**aa/aa+(1+2*delta)**aa*delta**2/(2*(1-delta)**2)
        local=[arb(0) for _ in range(17)];cells=set();ref=None
        paths=sorted((S/'local').glob('r*_'+str(a).replace('/','_')+'.json'));assert paths
        for path in paths:
            d=load(path);params={k:d[k] for k in ['alpha','precision_bits','angles_per_circle','radial_cells','phase_intervals','delta','integer_unit','source_hashes']}
            if ref is None:ref=params
            else:assert ref==params
            assert Q(d['alpha'])==a and d['precision_bits']>=160 and d['angles_per_circle']==512
            assert d['radial_cells']==256 and d['phase_intervals']==16 and Q(d['delta'])==Q(1,64)
            assert d['integer_unit']==2**44 and d['repair_integer_mass']==0
            for name,h in d['source_hashes'].items():assert sha(S/'code'/name)==h
            lo,hi=d['row_start'],d['row_stop'];j0,j1=d['phase_start'],d['phase_stop']
            assert 0<=lo<hi<=256 and 0<=j0<j1<=17
            assert set(map(int,d['partial_phase_intervals']))==set(range(j0,j1))
            assert set(map(int,d['residual_phase_intervals']))==set(range(j0,j1))
            assert small.overlaps(arb(d['small_disk_upper']))
            for k in range(lo,hi):
                for j in range(j0,j1):assert (k,j) not in cells;cells.add((k,j))
            for text,value in d['partial_phase_intervals'].items():
                v=arb(value);rv=arb(d['residual_phase_intervals'][text])
                assert v.is_finite() and 0<=rv<=v;local[int(text)]+=v
            coverage.append(dict(path=str(path.relative_to(ROOT)),kind='local',alpha=str(a),row_start=lo,row_stop=hi,phase_start=j0,phase_stop=j1,sha256=sha(path)))
        assert cells=={(k,j) for k in range(256) for j in range(17)}
        farpath=S/'far'/('far_'+str(a).replace('/','_')+'.json');d=load(farpath)
        assert Q(d['plan_reference_alpha'])==a and d['precision_bits']>=160 and d['phase_intervals']==16
        assert d['angles']==512 and d['radial_cells']==128 and Q(d['umin'])==Q(1,4)
        assert d['integer_unit']==2**44 and d['plan_trials']==9 and d['source_sha256']==sha(S/'code/far_nodes.py')
        assert len(d['rows'])==1 and Q(d['rows'][0]['alpha'])==a
        assert sum(d['plan_counts'].values())==128*17
        row=d['rows'][0];far=array(row['far_phase_intervals']);tail=arb(row['tail_interval'])
        assert tail>0 and all(x>=tail for x in far)
        assert all(ar(Q(text))>=v for text,v in zip(row['safe_far_phase_upper'],far))
        values=[x+y+z for x,y,z in zip(local,middle[a],far)]
        maximum=values[0]
        for v in values[1:]:maximum=arb.max(maximum,v)
        rem=phase_factor*maximum;upper=small+rem;safe=upward(upper)
        assert Q(submitted[a]['C_upper'])>=Q(str(upper.upper().fmpq())),('unsafe endpoint',a)
        assert safe==submitted[a]['C_upper']
        assert upward(upper,6)==submitted[a]['C_upper_6']
        # A worst-phase label is informational; check that its upper endpoint is maximal.
        worst=max(range(17),key=lambda j:Q(str(values[j].upper().fmpq())))
        assert worst==submitted[a]['worst_phase']
        results.append(dict(alpha=str(a),small=record(small),remainder=record(rem),upper=record(upper),safe_upper_C=safe,worst_phase=worst,
                            local=[record(v) for v in local],middle=[record(v) for v in middle[a]],far=[record(v) for v in far],
                            phase_totals=[record(v) for v in values],far_path=str(farpath.relative_to(ROOT)),far_sha256=sha(farpath)))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=320,rows=results,coverage=coverage,
             source_snapshot_sha256=sha(S/'snapshot_manifest.json'),auditor_sha256=sha(Path(__file__)),source_path_change=changes,
             verdict='All six exact coverage, source identity, phase and outward recombination checks passed; selected independent geometric replay recorded separately.')
    (BASE/'verification').mkdir(exist_ok=True);(BASE/'verification/independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    for row in results:print(row['alpha'],row['safe_upper_C'],'phase',row['worst_phase'])
if __name__=='__main__':main()
