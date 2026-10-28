"""Accept an audited producer certificate with explicitly partial replay scope."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/note14_certificate/producer_fine_a50'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def pair(d):return Q(d['lower']),Q(d['upper'])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);args=ap.parse_args();hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(R);hashes[str(p.relative_to(R))]=sha(p)
    def check(p,field,verdict):
        d=load(p);assert d[field]==verdict;bind(p)
        for n,h in d['sha256'].items():assert sha(R/n)==h,n;bind(R/n)
        return d
    imported=check(B/'import_audit.json','verdict','IMPORT_AND_EXACT_COVERAGE_PASSED')
    selected=check(B/'selected_replays/completed.json','verdict','ALL_SELECTED_TASKS_MATCH')
    original=check(B/'original_recombination.json','verdict','EXACT_ORIGINAL_RECOMBINATION_PASSED')
    assert imported['task_count']==4019 and imported['cells']==24900260
    assert selected['total_tasks']==4019 and selected['task_count']==len(selected['indices'])==52
    p=B/'quadratic_recombination/independent_audit.json';d=load(p);bind(p)
    assert d['alpha']=='1/2' and d['b']=='3/4' and d['shift']=='-3/20' and d['lam']=='1000/1021'
    for field in ['source_hashes','profile_certificate_sha256','analytic_sha256','dependency_sha256']:
        for n,h in d[field].items():assert sha(R/n)==h;bind(R/n)
    auditor=R/'code/audit_note14_annular_profile.py';assert sha(auditor)==d['auditor_sha256'];bind(auditor)
    manifest=R/d['manifest_path'];assert sha(manifest)==d['manifest_sha256'];bind(manifest);m=load(manifest)
    assert m['source_hashes']==d['source_hashes'] and len(m['tasks'])==d['task_count']==4019
    cells=0
    for i,record in enumerate(d['task_files']):
        q=R/record['path'];assert record['index']==i and sha(q)==record['sha256'];bind(q);obj=load(q)
        assert obj['index']==i and obj['task']==m['tasks'][i] and obj['source_hashes']==d['source_hashes'];cells+=obj['cells']
    assert len(d['task_files'])==4019 and cells==d['cells']==imported['cells']
    s=d['selected'];assert d['one_sided'] and d['angular_tail'] and pair(d['tail_condition'])[0]>=1
    assert all(pair(v)[0]>=0 for v in s['condition_margins'][:2])
    near=pair(s['retained_near']);mid=pair(d['middle']);tm=pair(d['tail_main']);te=pair(d['tail_error']);sl=pair(d['sliver'])
    main=pair(s['main_per_pole']);ec=pair(s['clamp_error_per_pole']);es=pair(s['smooth_error_per_pole']);uc=pair(s['upper_clamp_per_pole'])
    if uc==(Q(0),Q(0)):assert pair(s['condition_margins'][2])[0]>=0
    lo=2*near[0]+mid[0]+tm[0]+2*main[0]-2*ec[1]-2*es[1]-te[1]-sl[1]
    hi=2*near[1]+mid[1]+tm[1]+2*main[1]+2*es[1]+2*uc[1]+te[1]+sl[1]
    assert (lo,hi)==pair(s['I0']);exact=max(Q(0),lo,-hi)+Q(1,2);safe=Q(d['safe_D_lower_10_places'])
    assert exact==Q(d['exact_D_lower']) and safe<=exact<safe+Q(1,10**10)
    parent=check(R/'05_team_audit/note14_certificate/pole_profile/quadratic_lower/verification/accepted.json','verdict','CONFIRMED');assert parent['ledger']=='V148'
    for n,h in d['analytic_sha256'].items():assert parent['sha256'][n]==h
    full=check(R/'05_team_audit/note14_certificate/replay_fine_a50/full_quadratic/accepted.json','verdict','CONFIRMED');assert full['ledger']=='V164'
    assert exact>Q(full['exact_D_lower']) and exact>Q(original['exact_D_lower'])
    for q in [B/'PROOF.md',B/'quadratic_recombination/PROOF.md',Path(__file__)]:bind(q)
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',alpha='1/2',safe_D_lower=d['safe_D_lower_10_places'],exact_D_lower=str(exact),task_count=4019,cells=cells,selected_task_replays=52,selected_cells=selected['cells'],epsilon=s['epsilon'],radius=d['radius'],scope='Audited producer interval certificate: all 4019 task records, exact coverage and recombination, unchanged audited cell formulas, 52 selected complete-task replays. This is not a full independent replay of the finer mesh. Separate complete delta=.005 replay is V164.',sha256=hashes)
    dst=B/'quadratic_recombination/accepted.json';dst.write_text(json.dumps(out,indent=2)+'\n')
    registry=R/'data/accepted_external_D.json';old=load(registry);same=[r for r in old['entries'] if Q(r['alpha'])==Q(1,2)];assert not same or safe>=max(Q(r['safe_D_lower']) for r in same)
    entries=[r for r in old['entries'] if Q(r['alpha'])!=Q(1,2)]
    entries.append(dict(alpha='1/2',safe_D_lower=d['safe_D_lower_10_places'],family='audited producer fine mesh with 52 selected task replays, quadratic poles and angular tail',verdict='CONFIRMED',audit=args.ledger,audit_path=str(dst.relative_to(R)),audit_sha256=sha(dst),source_path=str(manifest),source_sha256=sha(manifest)))
    old['entries']=entries;old['time_utc']=out['time_utc'];registry.write_text(json.dumps(old,indent=2)+'\n');print(out['time_utc'],args.ledger,out['safe_D_lower'])
if __name__=='__main__':main()
