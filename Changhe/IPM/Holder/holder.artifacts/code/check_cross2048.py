"""Independent Cartesian diagnostics and provenance for the cross-disk refinement.
The Gaussian comparisons are diagnostic only; PROOF.md supplies interval rigor.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json, re, time
import numpy as np
from numpy.polynomial.legendre import leggauss
R=Path(__file__).resolve().parents[1]
B=R/'05_team_audit/cross2048'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def ends(s):
    if not s.startswith('['): return Q(s),Q(s)
    m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s); assert m,s
    c,e=map(Q,m.groups());return c-e,c+e

def cartesian(alpha, phases, n):
    x,w=leggauss(n);x=(x+1)/2;w=w/2
    X=x[:,None];top=np.sqrt(X*(1-X));Y=top*x[None,:]
    den=(X+.5)**2+Y**2
    kr=np.abs(((X+.5)**2-Y**2)/(2*np.pi*den**2))
    ki=np.abs(-(X+.5)*Y/(np.pi*den**2))
    h=(2*X)**alpha;v=(2*Y)**alpha;d=(2*np.hypot(X,Y))**alpha
    area=top*w[:,None]*w[None,:];values=[]
    for phi in phases:
        a=kr*np.cos(phi);b=ki*np.sin(phi)
        values.append(float(np.sum(2*np.maximum(a*h+b*(d-h),a*(d-v)+b*v)*area)))
    return values

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',default='05_team_audit/cross2048/source/cross_disk_certificate_2048.json');args=ap.parse_args()
    started=time.monotonic();p=R/args.source;d=load(p);snapshot=load(B/'verification/source_snapshot.json');hashes={}
    post=load(B/'verification/postrun_snapshot.json')
    assert post['source_unchanged_since_prelaunch'] and sha(p)==post['output_sha256']
    assert sha(B/'source/prelaunch.txt')==post['prelaunch_sha256']
    assert post['source_sha256']==snapshot['source_sha256']
    assert d['cells_per_axis']==2048 and d['phase_intervals']==16 and d['precision_bits']==160
    assert set(d['source_hashes'])=={'code/certify_cross_only.py','code/certify_reflection_chunk.py','code/certify_far_circles.py'}
    for rel,h in snapshot['source_sha256'].items():
        q=B/'source'/rel;assert sha(q)==h and sha(R/rel)==h
        if rel in d['source_hashes']: assert d['source_hashes'][rel]==h
        hashes[str(q.relative_to(R))]=h
    assert [Q(r['alpha']) for r in d['rows']]==list(map(Q,['1/5','3/10','1/2','3/4','9/10','99/100']))
    old={r['alpha']:r for r in load(R/'data/cross_disk_certificate.json')['rows']}
    phases=np.arange(17)*np.pi/32;rows=[]
    for r in d['rows']:
        assert len(r['cross_phase_intervals'])==len(r['safe_cross_upper'])==17
        enclosures=list(map(ends,r['cross_phase_intervals']));u=cartesian(float(Q(r['alpha'])),phases,256);v=cartesian(float(Q(r['alpha'])),phases,512)
        for j,((lo,hi),x,y,safe) in enumerate(zip(enclosures,u,v,r['safe_cross_upper'])):
            assert 0<=lo<hi and lo<Q(safe)<=hi,(r['alpha'],j,'rounded producer field')
            assert float(lo)<x<float(hi) and float(lo)<y<float(hi),(r['alpha'],j,x,y,str(lo),str(hi))
        oldep=list(map(ends,old[r['alpha']]['cross_phase_intervals']))
        rows.append(dict(alpha=r['alpha'],upper_endpoints=[str(hi) for lo,hi in enclosures],cartesian_gauss_256=u,cartesian_gauss_512=v,max_gauss_change=max(abs(x-y) for x,y in zip(u,v)),all_34_comparisons_inside=True,all_new_uppers_below_old=all(h<oh for (l,h),(ol,oh) in zip(enclosures,oldep))))
        print(r['alpha'],rows[-1]['max_gauss_change'],rows[-1]['all_new_uppers_below_old'],flush=True)
    for q in [p,B/'PROOF.md',B/'verification/source_snapshot.json',B/'verification/postrun_snapshot.json',B/'source/run.log',B/'source/prelaunch.txt',Path(__file__),R/'data/cross_disk_certificate.json']:
        hashes[str(q.relative_to(R))]=sha(q)
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started,status='PROVENANCE AND INDEPENDENT FLOATING CHECKS PASS; numerical acceptance requires review',rows=rows,sha256=hashes,scope='204 Cartesian Gaussian comparisons at two resolutions; no full interval rerun claimed')
    (B/'verification/independent_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'])
if __name__=='__main__': main()
