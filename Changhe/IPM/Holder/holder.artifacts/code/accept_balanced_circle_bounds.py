"""Bind the completed residual replay and numerical upper-bound theorem."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
    p=BASE/'verification/independent_audit.json';d=load(p);hashes={}
    def bind(p):hashes[str(p.relative_to(ROOT))]=sha(p)
    bind(p)
    for name,h in d['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    parent=BASE.parent/'verification/accepted.json';a=load(parent)
    assert a['verdict']=='CONFIRMED' and a['ledger']=='V150';bind(parent)
    for name,h in a['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    proof=BASE/'numerical_values/PROOF.md';bind(proof)
    printed=dict(re.findall(r'^\| ([0-9]+/[0-9]+) \| ([0-9]+\.[0-9]+) \|$',proof.read_text(),re.M))
    assert len(printed)==10 and len(d['rows'])==10
    rows=[]
    for r in d['rows']:
        assert r['coverage_cells']==256*17
        q=Q(r['upper']['upper']);s=Q(r['new_C_upper'])
        assert q<=s<q+Q(1,10**10) and s<=Q(r['old_C_upper'])
        assert printed[r['alpha']]==r['new_C_upper']
        assert all(c['old_intervals_overlap'] for c in r['old_residual_replay_checks'])
        rows.append(dict(alpha=r['alpha'],safe_upper_C=r['new_C_upper'],worst_phase=r['worst_phase']))
    bind(Path(__file__))
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V152',verdict='CONFIRMED',rows=rows,
                scope='Full operator C upper bounds from accepted transports and completely replayed balanced residuals; no new transport optimization',sha256=hashes)
    (BASE/'verification/accepted.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['time_utc'],'V152 CONFIRMED',len(rows),'exponents')
if __name__=='__main__':main()
