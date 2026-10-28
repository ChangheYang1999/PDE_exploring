"""Audit the 4096 cross-disk file and reuse the recorded Cartesian diagnostics.
The reused Gaussian numbers are diagnostics, not an interval replay.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json, re
R=Path(__file__).resolve().parents[1]
B=R/'05_team_audit/cross4096'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def ends(s):
    if not s.startswith('['): return Q(s),Q(s)
    m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s); assert m,s
    c,e=map(Q,m.groups());assert e>=0;return c-e,c+e
def main():
    hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(R);hashes[str(p.relative_to(R))]=sha(p)
    p=B/'source/cross_disk_certificate_4096.json';d=load(p)
    post=load(B/'verification/postrun_snapshot.json')
    assert post['source_unchanged_since_prelaunch'] and sha(p)==post['output_sha256']
    assert sha(B/'source/prelaunch.txt')==post['prelaunch_sha256']
    pre=(B/'source/prelaunch.txt').read_text()
    assert d['cells_per_axis']==4096 and d['phase_intervals']==16 and d['precision_bits']==160
    assert set(d['source_hashes'])=={'code/certify_cross_only.py','code/certify_reflection_chunk.py','code/certify_far_circles.py'}
    for rel,h in post['source_sha256'].items():
        q=B/'source'/rel;assert sha(q)==sha(R/rel)==h
        assert f'{h}  {rel}' in pre
        if rel in d['source_hashes']:assert d['source_hashes'][rel]==h
        bind(q)
    prior_path=R/'05_team_audit/cross2048/verification/independent_diagnostic.json'
    prior=load(prior_path);bind(prior_path)
    for name,h in prior['sha256'].items():assert sha(R/name)==h;bind(R/name)
    diagnostics={r['alpha']:r for r in prior['rows']}
    old={r['alpha']:r for r in load(R/'data/cross_disk_certificate.json')['rows']}
    prev={r['alpha']:r for r in load(R/'05_team_audit/cross2048/source/cross_disk_certificate_2048.json')['rows']}
    assert [r['alpha'] for r in d['rows']]==['1/5','3/10','1/2','3/4','9/10','99/100']
    rows=[]
    for r in d['rows']:
        assert len(r['cross_phase_intervals'])==len(r['safe_cross_upper'])==17
        enc=list(map(ends,r['cross_phase_intervals'])); diag=diagnostics[r['alpha']]
        u,v=diag['cartesian_gauss_256'],diag['cartesian_gauss_512']
        for j,((lo,hi),x,y,safe) in enumerate(zip(enc,u,v,r['safe_cross_upper'])):
            assert 0<=lo<hi and lo<Q(safe)<=hi,(r['alpha'],j,'producer decimal')
            assert lo<Q(str(x))<hi and lo<Q(str(y))<hi,(r['alpha'],j,'Gaussian consistency')
        oldep=list(map(ends,old[r['alpha']]['cross_phase_intervals']))
        prevep=list(map(ends,prev[r['alpha']]['cross_phase_intervals']))
        assert all(h<oh for (l,h),(ol,oh) in zip(enc,oldep))
        assert all(h<oh for (l,h),(ol,oh) in zip(enc,prevep))
        rows.append(dict(alpha=r['alpha'],upper_endpoints=[str(hi) for lo,hi in enc],cartesian_gauss_256=u,cartesian_gauss_512=v,max_gauss_change=diag['max_gauss_change'],all_34_comparisons_inside=True,all_new_uppers_below_old=True,all_new_uppers_below_2048=True))
    for q in [p,B/'PROOF.md',B/'verification/postrun_snapshot.json',B/'verification/precompletion_hashes.txt',B/'source/run.log',B/'source/prelaunch.txt',Path(__file__),R/'data/cross_disk_certificate.json',R/'05_team_audit/cross2048/source/cross_disk_certificate_2048.json']:bind(q)
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='PROVENANCE AND REUSED INDEPENDENT FLOATING CHECKS PASS; numerical acceptance requires review',rows=rows,sha256=hashes,scope='All204 comparisons reuse previously computed independent Cartesian diagnostics; no new Gaussian computation and no full4096 interval replay')
    (B/'verification/independent_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['time_utc'],'all204 comparisons pass')
if __name__=='__main__':main()
