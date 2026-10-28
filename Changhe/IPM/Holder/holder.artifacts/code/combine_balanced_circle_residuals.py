"""Exact coverage and outward replacement of accepted local residual costs."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates'
T37=ROOT/'05_team_audit/table37_lead'
ALPHAS=['1/1000','1/100','1/20','1/10','1/5','3/10','1/2','3/4','9/10','99/100']
ctx.prec=320

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def endpoints(text):
    if not text.startswith('['):return Q(text),Q(text)
    m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',text);assert m,text
    c,r=map(Q,m.groups());assert r>=0;return c-r,c+r

def pair(d):
    lo,hi=Q(d['lower']),Q(d['upper']);assert lo<=hi;return lo,hi

def rec(x):
    assert x.is_finite();return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()),display=x.str(42,more=True))

def ceil10(x):
    q=Q(str(x.upper().fmpq()));k=-((-q*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'

def main():
    hashes={};replay=[];ref=None
    def bind(p):hashes[str(p.relative_to(ROOT))]=sha(p)
    for k in range(256):
        p=BASE/'verification/mass_replay'/f'row_{k:03d}.json';d=load(p);bind(p)
        assert d['row']==k and d['angles']==512 and d['radial_rows']==256 and d['phase_intervals']==16
        left=Q(1,64)+(Q(1,2)-Q(1,64))*k/256
        right=Q(1,64)+(Q(1,2)-Q(1,64))*(k+1)/256
        assert pair(d['radial_left'])==(left,left) and pair(d['radial_right'])==(right,right)
        assert d['integer_unit']==2**44 and d['precision_bits']==160 and d['alphas']==ALPHAS
        if ref is None:ref=d['source_hashes']
        else:assert d['source_hashes']==ref
        assert len(d['phases'])==17
        for j,v in enumerate(d['phases']):
            assert v['phase']==j and len(v['masses'])==512 and all(type(x) is int for x in v['masses'])
            assert sum(v['masses'])==v['signed_integer_sum'] and sum(map(abs,v['masses']))==v['absolute_integer_sum']
        replay.append(d)
    for name,h in ref.items():assert sha(ROOT/name)==h;bind(ROOT/name)
    acceptance=load(T37/'verification/accepted.json');assert acceptance['verdict']=='CONFIRMED'
    for name,h in acceptance['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    table=load(T37/'verification/independent_audit.json');trows={x['alpha']:x for x in table['rows']}
    snapshot=load(T37/'source/snapshot_manifest.json')
    for name,h in snapshot['sha256'].items():assert sha(T37/'source'/name)==h
    bind(T37/'source/snapshot_manifest.json')
    results=[]
    for a in ALPHAS:
        if a in trows:
            chunks=sorted((T37/'source/local').glob('r*_'+a.replace('/','_')+'.json'))
            srcroot=T37/'source/code';tr=trows[a]
            oldphases=[pair(v)[1] for v in tr['phase_totals']]
            small=pair(tr['small'])[1];oldbound=tr['safe_upper_C']
        else:
            suffix={'3/10':'a30','1/2':'a50','3/4':'a75','9/10':'a90'}[a]
            aggregate_path=ROOT/'data'/('local_circle_composite_'+suffix+'.json');d=load(aggregate_path);bind(aggregate_path)
            for name,h in d['input_hashes'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
            assert len(d['rows'])==1 and d['rows'][0]['alpha']==a
            tr=d['rows'][0];oldphases=[endpoints(v)[1] for v in tr['middle_plus_local_plus_far']]
            small=endpoints(tr['small_disk_upper'])[1];oldbound=tr['safe_upper_C']
            chunks=[ROOT/name for name in d['input_hashes'] if name.startswith('data/local_circle_chunks/')]
            srcroot=ROOT
        assert len(oldphases)==17
        residual_lo=[Q(0) for _ in range(17)];new_hi=[Q(0) for _ in range(17)];coverage=set();checks=[]
        for p in chunks:
            d=load(p);bind(p)
            assert Q(d['alpha'])==Q(a) and d['angles_per_circle']==512 and d['radial_cells']==256
            assert d['phase_intervals']==16 and Q(d['delta'])==Q(1,64) and d['integer_unit']==2**44
            assert d['precision_bits']==160 and d['repair_integer_mass']==0
            for name,h in d['source_hashes'].items():assert sha(srcroot/name)==h;bind(srcroot/name)
            lo,hi,j0,j1=d['row_start'],d['row_stop'],d['phase_start'],d['phase_stop']
            assert 0<=lo<hi<=256 and 0<=j0<j1<=17
            assert set(map(int,d['residual_phase_intervals']))==set(range(j0,j1))
            for j in range(j0,j1):
                old_l=old_u=Q(0);new_u=Q(0)
                for k in range(lo,hi):
                    assert (k,j) not in coverage;coverage.add((k,j))
                    v=replay[k]['phases'][j];l,u=pair(v['old'][a]);old_l+=l;old_u+=u
                    new_u+=pair(v['new'][a])[1]
                sl,su=endpoints(d['residual_phase_intervals'][str(j)])
                assert max(sl,old_l)<=min(su,old_u),('old residual replay mismatch',a,p.name,j,str(old_l-sl),str(old_u-su))
                residual_lo[j]+=sl;new_hi[j]+=new_u
                checks.append(dict(chunk=str(p.relative_to(ROOT)),phase=j,old_intervals_overlap=True))
        assert coverage=={(k,j) for k in range(256) for j in range(17)}
        newphase=[oldphases[j]-residual_lo[j]+new_hi[j] for j in range(17)]
        assert all(x>=0 for x in newphase)
        assert all(x<=y for x,y in zip(newphase,oldphases))
        worst=max(range(17),key=lambda j:newphase[j]);factor=1/(arb.pi()/64).cos()
        upper=arb(str(small))+factor*arb(str(newphase[worst]));safe=ceil10(upper)
        results.append(dict(alpha=a,old_C_upper=oldbound,new_C_upper=safe,worst_phase=worst,
            upper=rec(upper),small_upper=str(small),phase_upper=list(map(str,newphase)),
            old_residual_lower=list(map(str,residual_lo)),new_residual_upper=list(map(str,new_hi)),
            coverage_cells=len(coverage),old_residual_replay_checks=checks))
        print(a,oldbound,'->',safe,'phase',worst,flush=True)
    bind(Path(__file__))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='CHECKS PASS; pending independent analytic cross-read and final acceptance',
        rows=results,sha256=hashes,mass_replay_source_hashes=ref)
    (BASE/'verification/independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
