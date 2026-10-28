"""Accept an independently replayed annular certificate after analytic cross-read."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def pair(v):return Q(v['lower']),Q(v['upper'])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--ledger',required=True);ap.add_argument('--proof',required=True)
    args=ap.parse_args();base=(ROOT/args.folder).resolve();proof=(ROOT/args.proof).resolve()
    assert base.is_relative_to(ROOT) and proof.is_relative_to(ROOT)
    p=base/'independent_audit.json';d=load(p);hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    bind(p);bind(proof)
    for key in ['source_hashes','profile_certificate_sha256','analytic_sha256','dependency_sha256']:
        for name,h in d[key].items():assert sha(ROOT/name)==h,(key,name);bind(ROOT/name)
    auditor=ROOT/'code/audit_note14_annular_profile.py';assert sha(auditor)==d['auditor_sha256'];bind(auditor)
    manifest=ROOT/d['manifest_path'];assert sha(manifest)==d['manifest_sha256'];bind(manifest)
    m=load(manifest);assert m['source_hashes']==d['source_hashes']
    assert len(d['task_files'])==d['task_count']<=len(m['tasks'])
    for i,r in enumerate(d['task_files']):
        t=ROOT/r['path'];assert r['index']==i and sha(t)==r['sha256'];bind(t)
        record=load(t);assert record['index']==i and record['task']==m['tasks'][i] and record['source_hashes']==d['source_hashes']
    assert d['one_sided'] and d['angular_tail'];s=d['selected']
    assert all(pair(v)[0]>=0 for v in s['condition_margins'][:2])
    assert pair(d['tail_condition'])[0]>=1
    near=pair(s['retained_near']);mid=pair(d['middle']);tm=pair(d['tail_main']);te=pair(d['tail_error']);sl=pair(d['sliver'])
    main=pair(s['main_per_pole']);ec=pair(s['clamp_error_per_pole']);es=pair(s['smooth_error_per_pole']);uc=pair(s['upper_clamp_per_pole'])
    if uc==(Q(0),Q(0)):assert pair(s['condition_margins'][2])[0]>=0
    lo=2*near[0]+mid[0]+tm[0]+2*main[0]-2*ec[1]-2*es[1]-te[1]-sl[1]
    hi=2*near[1]+mid[1]+tm[1]+2*main[1]+2*es[1]+2*uc[1]+te[1]+sl[1]
    assert (lo,hi)==pair(s['I0'])
    exact=max(Q(0),lo,-hi)+Q(1,2);safe=Q(d['safe_D_lower_10_places'])
    assert exact==Q(d['exact_D_lower']) and safe<=exact<safe+Q(1,10**10)
    parent=ROOT/'05_team_audit/note14_certificate/pole_profile/quadratic_lower/verification/accepted.json';aa=load(parent)
    assert aa['verdict']=='CONFIRMED' and aa['ledger']=='V148';bind(parent)
    for name,h in d['analytic_sha256'].items():
        assert aa['sha256'][name]==h
    note=ROOT/aa['independent_cross_read'];assert aa['sha256'][str(note.relative_to(ROOT))]==sha(note);bind(note)
    bind(Path(__file__))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',alpha=d['alpha'],safe_D_lower=d['safe_D_lower_10_places'],
        exact_D_lower=str(exact),task_count=d['task_count'],total_manifest_tasks=d['total_manifest_tasks'],epsilon=s['epsilon'],radius=d['radius'],
        cells=d['cells'],scope='Independent finite-task replay, analytic pole disks and analytic exterior, exact final recombination',sha256=hashes)
    dst=base/'accepted.json';dst.write_text(json.dumps(out,indent=2)+'\n')
    registry=ROOT/'data/accepted_external_D.json';old=load(registry)
    same=[r for r in old['entries'] if Q(r['alpha'])==Q(d['alpha'])]
    assert not same or safe>=max(Q(r['safe_D_lower']) for r in same)
    entries=[r for r in old['entries'] if Q(r['alpha'])!=Q(d['alpha'])]
    entries.append(dict(alpha=d['alpha'],safe_D_lower=d['safe_D_lower_10_places'],family='independent annular replay with quadratic pole and angular exterior',
        verdict='CONFIRMED',audit=args.ledger,audit_path=str(dst.relative_to(ROOT)),audit_sha256=sha(dst),source_path=str(manifest),source_sha256=sha(manifest)))
    old['entries']=entries;old['time_utc']=out['time_utc'];registry.write_text(json.dumps(old,indent=2)+'\n')
    print(out['time_utc'],out['alpha'],out['safe_D_lower'],out['verdict'])
if __name__=='__main__':main()
