"""Compare every independent third-pass node against the frozen lead input."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, hashlib
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'09_uniform_comparison/pass3'
ctx.prec=256

def load(path): return json.loads(path.read_text())
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    checks=[]; inputs=[Path(__file__)]; failures=[]
    original={}; replay={}
    for folder,target in [('data/local',original),('verification/local',replay)]:
        for path in sorted((BASE/folder).glob('*.json')):
            d=load(path); inputs.append(path)
            assert d['angles_per_circle']==512 and d['radial_cells']==256
            assert d['phase_intervals']==16 and Q(d['delta'])==Q(1,64)
            assert d['integer_unit']==2**44
            target.setdefault(Q(d['alpha']),[]).append(d)
    assert set(original)==set(replay), (set(original)-set(replay),set(replay)-set(original))
    local_count=0
    for alpha,olds in original.items():
        news=replay[alpha]
        for label,parts in [('original',olds),('replay',news)]:
            cover=[[0]*17 for _ in range(256)]
            for d in parts:
                assert 0<=d['row_start']<d['row_stop']<=256
                assert 0<=d['phase_start']<d['phase_stop']<=17
                assert set(map(int,d['partial_phase_intervals']))==set(range(d['phase_start'],d['phase_stop']))
                for row in range(d['row_start'],d['row_stop']):
                    for phase in range(d['phase_start'],d['phase_stop']):cover[row][phase]+=1
            assert all(v==1 for row in cover for v in row),(alpha,label,'coverage')
        for old in olds:
            group=[n for n in news if old['row_start']<=n['row_start'] and n['row_stop']<=old['row_stop']]
            assert sum(n['row_stop']-n['row_start'] for n in group)==old['row_stop']-old['row_start']
            for phase in range(17):
                a=arb(old['partial_phase_intervals'][str(phase)])
                b=sum((arb(n['partial_phase_intervals'][str(phase)]) for n in group),arb(0))
                contained=a.contains(b); overlap=a.overlaps(b)
                record=dict(region='local',alpha=str(alpha),start=old['row_start'],stop=old['row_stop'],phase=phase,contained=contained,overlap=overlap)
                if not overlap:failures.append(record)
                checks.append(record);local_count+=1
    oldm={};newm={}
    for folder,target in [('data/mid',oldm),('verification/mid',newm)]:
        cover=[0]*512
        for path in sorted((BASE/folder).glob('*.json')):
            d=load(path);inputs.append(path)
            assert d['angles_per_half']==d['radial_cells']==512 and d['phase_intervals']==16
            key=(d['row_start'],d['row_stop']);assert key not in target
            assert 0<=key[0]<key[1]<=512
            for row in range(*key):cover[row]+=1
            target[key]=d
        assert cover==[1]*512,(folder,'coverage')
    assert set(oldm)==set(newm)
    mid_count=0
    for key,old in oldm.items():
        new=newm[key];assert old['groups']==new['groups']
        oldrows={(Q(r['plan_reference_alpha']),Q(r['alpha'])):r for r in old['rows']}
        newrows={(Q(r['plan_reference_alpha']),Q(r['alpha'])):r for r in new['rows']}
        assert len(oldrows)==len(old['rows'])==27 and set(oldrows)==set(newrows)
        for pair,oldrow in oldrows.items():
            newrow=newrows[pair]
            assert len(oldrow['middle_phase_intervals'])==len(newrow['middle_phase_intervals'])==17
            for phase,(x,y) in enumerate(zip(oldrow['middle_phase_intervals'],newrow['middle_phase_intervals'])):
                a,b=arb(x),arb(y);contained=a.contains(b);overlap=a.overlaps(b)
                record=dict(region='middle',reference=str(pair[0]),alpha=str(pair[1]),start=key[0],stop=key[1],phase=phase,contained=contained,overlap=overlap)
                if not overlap:failures.append(record)
                checks.append(record);mid_count+=1
    # Every replay source must remain the file actually used by the worker.
    for p in list((BASE/'verification/local').glob('*.json'))+list((BASE/'verification/mid').glob('*.json')):
        for name,expected in load(p)['source_hashes'].items():
            src=ROOT/name;assert digest(src)==expected,(p,name,'changed source');inputs.append(src)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,local_exponents=len(original),local_comparisons=local_count,middle_comparisons=mid_count,all_overlap=not failures,all_contained=all(c['contained'] for c in checks),noncontained=[c for c in checks if not c['contained']],failures=failures,source_hashes={str(p.relative_to(ROOT)):digest(p) for p in sorted(set(inputs))},checks=checks)
    out=BASE/'verification/full_replay_comparison.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print({k:result[k] for k in ['local_exponents','local_comparisons','middle_comparisons','all_overlap','all_contained']})
    assert not failures,failures[:5]
if __name__=='__main__':main()
