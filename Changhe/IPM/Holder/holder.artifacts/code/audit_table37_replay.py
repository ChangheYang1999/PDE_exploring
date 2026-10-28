"""Independent coverage and phase comparison of the alpha=1/5 replay.

Reads only output records and hashes. It imports no optimizer or transport
program. Every region and phase must be completely present.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/table37_lead'
REPLAY=BASE/'verification/replay_a20'
ctx.prec=320

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def record(v):
    assert v.is_finite()
    return dict(lower=str(v.lower().fmpq()), upper=str(v.upper().fmpq()), display=v.str(50,more=True))
def enclose(r): return arb(r['lower']).union(arb(r['upper']))
def check_sources(d):
    for p,h in d['source_hashes'].items(): assert sha(ROOT/p)==h, ('source',p)
def upward(v,n=10):
    k=-((-Q(str(v.upper().fmpq()))*10**n).__floor__())
    return f'{k//10**n}.{k%10**n:0{n}d}'

def main():
    local=[arb(0) for _ in range(17)];middle=[arb(0) for _ in range(17)]
    seen=set();inputs=[];local_cells=set()
    for p in sorted(REPLAY.glob('local_*_1_5.json')):
        d=load(p);check_sources(d)
        assert Q(d['alpha'])==Q(1,5) and Q(d['delta'])==Q(1,64)
        assert d['angles_per_circle']==512 and d['radial_cells']==256 and d['phase_intervals']==16
        assert d['precision_bits']>=160 and d['integer_unit']==2**44 and d['repair_integer_mass']==0
        lo,hi=d['row_start'],d['row_stop'];j0,j1=d['phase_start'],d['phase_stop']
        assert 0<=lo<hi<=256 and j0==0 and j1==17
        assert set(map(int,d['partial_phase_intervals']))==set(range(17))
        for k in range(lo,hi):
            for j in range(17):
                assert (k,j) not in local_cells;local_cells.add((k,j))
        for j in range(17):
            v=arb(d['partial_phase_intervals'][str(j)])
            r=arb(d['residual_phase_intervals'][str(j)])
            assert 0<=r<=v;local[j]+=v
        inputs.append(dict(path=str(p.relative_to(ROOT)),sha256=sha(p),kind='local',start=lo,stop=hi))
    assert local_cells=={(k,j) for k in range(256) for j in range(17)}, 'Incomplete local replay'
    for p in sorted(REPLAY.glob('middle_*.json')):
        d=load(p);check_sources(d)
        assert d['angles_per_half']==512 and d['radial_cells']==512 and d['phase_intervals']==16
        assert d['precision_bits']>=160 and d['integer_unit']==2**44 and d['plan_trials']==17
        assert len(d['rows'])==1 and Q(d['rows'][0]['alpha'])==Q(1,5)
        lo,hi=d['row_start'],d['row_stop'];assert 0<=lo<hi<=512
        for k in range(lo,hi): assert k not in seen;seen.add(k)
        row=d['rows'][0];assert len(row['middle_phase_intervals'])==len(row['residual_intervals'])==17
        for j,(v,r) in enumerate(zip(row['middle_phase_intervals'],row['residual_intervals'])):
            vv,rr=arb(v),arb(r);assert 0<=rr<=vv;middle[j]+=vv
        inputs.append(dict(path=str(p.relative_to(ROOT)),sha256=sha(p),kind='middle',start=lo,stop=hi))
    assert seen==set(range(512)), 'Incomplete middle replay'
    p=REPLAY/'far.json';d=load(p)
    assert d['angles']==512 and d['radial_cells']==128 and d['phase_intervals']==16
    assert Q(d['umin'])==Q(1,4) and d['integer_unit']==2**44 and d['plan_trials']==9
    assert d['precision_bits']>=160 and len(d['rows'])==1 and Q(d['rows'][0]['alpha'])==Q(1,5)
    for name,h in d['source_hashes'].items(): assert sha(ROOT/'code'/name)==h
    for name,h in d['input_hashes'].items(): assert sha(ROOT/name)==h
    far=list(map(arb,d['rows'][0]['far_phase_intervals']));assert len(far)==17 and all(v>0 for v in far)
    assert sum(d['plan_counts'].values())==128*17
    inputs.append(dict(path=str(p.relative_to(ROOT)),sha256=sha(p),kind='far'))
    submitted=load(BASE/'verification/independent_audit.json')
    row=next(r for r in submitted['rows'] if Q(r['alpha'])==Q(1,5))
    comparisons={}
    for name,values in [('local',local),('middle',middle),('far',far)]:
        overlap=[v.overlaps(enclose(q)) for v,q in zip(values,row[name])]
        comparisons[name]=dict(all_phases_overlap=all(overlap),phase_overlap=overlap,
            absolute_differences=[record(abs(v-enclose(q))) for v,q in zip(values,row[name])])
        assert all(overlap), ('Different replay intervals',name,overlap)
    a=arb(1)/5;delta=arb(1)/64;pi=arb.pi();a2=2**(1+a/2)/(pi*(a+2))
    small=2*a2*delta**a/a+(1+2*delta)**a*delta**2/(2*(1-delta)**2)
    values=[l+m+e for l,m,e in zip(local,middle,far)]
    maximum=values[0]
    for v in values[1:]:maximum=arb.max(maximum,v)
    upper=small+maximum/(pi/64).cos()
    assert upper.overlaps(enclose(row['upper']))
    safe=upward(upper);assert safe==row['safe_upper_C']=='3.7444366045'
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha='1/5',precision_bits=320,
        input_files=inputs,local=[record(v) for v in local],middle=[record(v) for v in middle],
        far=[record(v) for v in far],small=record(small),upper=record(upper),safe_upper_C=safe,
        comparisons=comparisons,source_audit_sha256=sha(BASE/'verification/independent_audit.json'),
        auditor_sha256=sha(Path(__file__)),
        verdict='CONFIRMED: full independent geometric replay, exact coverage and all51regionalphase comparisons pass')
    (REPLAY/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['time_utc'],result['verdict'],safe)
if __name__=='__main__':main()
