"""Bind previously completed annular audits after the independent proof cross-read.

This performs only exact record/hash checks, not a new integration.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/note14_certificate/pole_profile/quadratic_lower'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())

def main():
    now=datetime.now(timezone.utc).isoformat()
    hashes={};records=[]
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    note=ROOT/'05_team_audit/lead_note31/NOTE31.md';bind(note)
    bind(BASE/'numerical_values/PROOF.md')
    expected={
        '05_team_audit/note14_certificate/pole_profile/quadratic_lower/PROOF.md':'fa18c4998a3dccfa416f49f52b72178c4cfcb7039208c5214a5e1bdcdc4aeb0c',
        '05_team_audit/note14_certificate/pole_profile/quadratic_clamp/PROOF.md':'04a0295662e394b3ee3af689d4179d4c51c6d3ead396511b5eefe8c6e87c4fb8',
        '05_team_audit/note14_certificate/homogeneous_tail/angular_error/PROOF.md':'590fab6eedf58e06bc7db4c1bd0a8a2549b59612be3a7b5f525963535b5ddac4'}
    for name,h in expected.items():assert sha(ROOT/name)==h;bind(ROOT/name)
    for sub in ['a50_prefix376','a75_prefix398','a90_prefix406','a50_fine_prefix1788']:
        p=BASE/'verification'/sub/'independent_audit.json';d=load(p);bind(p)
        for key in ['source_hashes','profile_certificate_sha256','analytic_sha256','dependency_sha256']:
            for name,h in d[key].items():assert sha(ROOT/name)==h,(sub,name);bind(ROOT/name)
        assert sha(ROOT/'code/audit_note14_annular_profile.py')==d['auditor_sha256'];bind(ROOT/'code/audit_note14_annular_profile.py')
        mp=ROOT/d['manifest_path'];assert sha(mp)==d['manifest_sha256'];bind(mp)
        assert len(d['task_files'])==d['task_count']
        for i,r in enumerate(d['task_files']):
            assert r['index']==i and sha(ROOT/r['path'])==r['sha256'];bind(ROOT/r['path'])
        assert d['one_sided'] and d['angular_tail']
        assert all(Q(r['lower'])>=0 for r in d['selected']['condition_margins'][:2])
        assert Q(d['tail_condition']['lower'])>=1
        safe=d['safe_D_lower_10_places'];assert Q(safe)<=Q(d['exact_D_lower'])<Q(safe)+Q(1,10**10)
        records.append(dict(alpha=d['alpha'],safe_D_lower=safe,source_audit=str(p.relative_to(ROOT)),
            manifest_path=d['manifest_path'],task_count=d['task_count'],epsilon=d['selected']['epsilon'],radius=d['radius']))
    best={}
    for r in records:
        if r['alpha'] not in best or Q(r['safe_D_lower'])>Q(best[r['alpha']]['safe_D_lower']):best[r['alpha']]=r
    bind(Path(__file__))
    result=dict(time_utc=now,ledger='V148',verdict='CONFIRMED',scope='Explicit quadratic pole and angular tail, with previously replayed finite tasks',
        records=records,best=list(best.values()),sha256=hashes,independent_cross_read=str(note.relative_to(ROOT)))
    out=BASE/'verification/accepted.json';out.write_text(json.dumps(result,indent=2)+'\n')
    registry=ROOT/'data/accepted_external_D.json';old=load(registry)
    entries=[r for r in old['entries'] if r['alpha'] not in best]
    for a,r in best.items():
        entries.append(dict(alpha=a,safe_D_lower=r['safe_D_lower'],family='projection cusp with quadratic pole integral and angular tail',
            verdict='CONFIRMED',audit='V148',audit_path=str(out.relative_to(ROOT)),audit_sha256=sha(out),
            source_path=str(ROOT/r['manifest_path']),source_sha256=sha(ROOT/r['manifest_path'])))
    old['time_utc']=now;old['entries']=entries;registry.write_text(json.dumps(old,indent=2)+'\n')
    print(now,'CONFIRMED',[(r['alpha'],r['safe_D_lower']) for r in best.values()])

if __name__=='__main__':main()
