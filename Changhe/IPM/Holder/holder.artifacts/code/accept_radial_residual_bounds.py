"""Accept the completed rational-subdivision residual evaluation after cross-read."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement'
OLD=BASE.parent/'existing_certificates'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
    hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    src=BASE/'verification/independent_audit.json';d=load(src);bind(src)
    assert d['subdivisions']==8 and d['precision_bits']==256
    for name,h in d['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    cross=ROOT/'05_team_audit/lead_note33/accepted.json';ac=load(cross)
    assert ac['verdict']=='CONFIRMED' and ac['ledger']=='V159';bind(cross)
    for name,h in ac['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    prior=load(OLD/'verification/independent_audit.json')
    assert len(prior['rows'])==10 and len(d['rows'])==10 and len(d['details'])==256
    proof=BASE/'numerical_values/PROOF.md';bind(proof)
    printed=dict(re.findall(r'^\| ([0-9]+/[0-9]+) \| ([0-9]+\.[0-9]+) \|$',proof.read_text(),re.M))
    assert len(printed)==10
    alphas=[r['alpha'] for r in prior['rows']]
    sums={a:[Q(0)]*17 for a in alphas}
    for k,row in enumerate(d['details']):
        assert row['row']==k and len(row['phases'])==17
        for j,r in enumerate(row['phases']):
            assert r['phase']==j and set(r['new_upper'])==set(alphas)
            for a in alphas:
                x=Q(r['new_upper'][a]);assert x>=0;sums[a][j]+=x
    rows=[]
    for old,r in zip(prior['rows'],d['rows']):
        a=r['alpha'];assert a==old['alpha'] and r['previous_upper_C']==old['new_C_upper']
        assert list(map(Q,r['residual_upper']))==sums[a]
        phases=[Q(x)-Q(y)+z for x,y,z in zip(old['phase_upper'],old['new_residual_upper'],sums[a])]
        assert phases==list(map(Q,r['phase_upper']))
        assert all(0<=x<=Q(y) for x,y in zip(phases,old['phase_upper']))
        assert r['worst_phase']==max(range(17),key=lambda j:phases[j])
        q=Q(r['upper']['upper']);s=Q(r['safe_upper_C'])
        assert q<=s<q+Q(1,10**10) and s<=Q(old['new_C_upper'])
        assert printed[a]==r['safe_upper_C']
        rows.append(dict(alpha=a,safe_upper_C=r['safe_upper_C'],worst_phase=r['worst_phase']))
    bind(Path(__file__))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V161',verdict='CONFIRMED',rows=rows,
             scope='Complete C upper bounds with eight rational subdivisions in each accepted radial row; no new optimization',sha256=hashes)
    (BASE/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['time_utc'],'V161 CONFIRMED',len(rows),'exponents')
if __name__=='__main__':main()
