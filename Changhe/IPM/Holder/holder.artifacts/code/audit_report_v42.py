from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import difflib, json
import mpmath as m
m.mp.dps=40
root=Path(__file__).resolve().parents[1]
out=root/'05_team_audit/report_v42'; lead=root.parent/'the lead work'
report=(lead/'FINAL_REPORT.md').read_bytes()
assert b'Draft version 42' in report
(out/'FINAL_REPORT.md').write_bytes(report)
old=(root/'05_team_audit/report_v41/FINAL_REPORT.md').read_text()
(out/'changes.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),report.decode().splitlines(True),fromfile='accepted_v41',tofile='v42')))
data=root/'09_uniform_comparison/lead_certificate/data'
nodes=json.loads((data/'nodes2.json').read_text()); groups=[]
for i,g in enumerate(nodes['groups']):
    d=json.loads((data/f'lower2_g{i}.json').read_text())
    assert Q(d['a'])==Q(g['shape'])
    X=sorted(map(Q,g['nodes'])); assert X[0]<Q(g['start']) and X[-1]>Q(g['end'])
    assert set(X)<=set(Q(r['alpha']) for r in d['rows'])
    groups.append(dict(group=i,shape=g['shape'],extra_nodes=[str(X[0]),str(X[-1])]))
def an(n,a):
    return n/m.pi*m.quad(lambda t:m.sin(n*t)*(2*m.sin(t))**a,[0,m.pi/(2*n)])
def pair(a):
    a2=2**(1+a/2)/(m.pi*(a+2)); A=m.gamma(1+a/2)/(2*m.sqrt(m.pi)*m.gamma((3+a)/2))
    B=2*an(3,a)/(1-a)+min((an(3,a)+an(1,a))/2,2**(a+1)/(3*m.pi))
    F=2*a2*((1-a)*B/(2*a2))**a/(a*(1-a))
    G=2*A*((1-a)*B/(2*A))**a/(a*(1-a))+m.mpf('.5')
    Fs=4*2**(-a/2)/(m.pi*a*(a+2))+m.mpf(209)/500/(1-a)+m.mpf(1353)/2500
    Gs=2**(1-a)*A/a+m.mpf(209)/500/(1-a)+m.mpf(72)/125+m.mpf('.5')
    return Fs-F,Gs-G
cross=[str(m.findroot(lambda a:pair(a)[i],(.97,.985))) for i in [0,1]]
assert Q('2.645079')/Q('2.089155')>Q('1.266')
for name in ['a10v7_combined.json','a20v7_combined.json','a30v7_combined.json']:
    assert (lead/'artifacts/lead_projection/verification'/name).is_file()
assert (root/'05_team_audit/closed_form_lead/PROOF.md').is_file()
stamp=datetime.now(timezone.utc).isoformat()
paths=[Path(__file__),out/'PROOF.md',root/'08_improved_upper_bounds/local_functional_audit/all_phases/PROOF.md',lead/'FINAL_REPORT.md',lead/'NOTES_FOR_TEAM.md',root.parent/'the numerics work/NUM_REPORT.md']
rec=dict(timestamp_utc=stamp,verdict='CONFIRMED',report_version=42,report_sha256=sha256(report).hexdigest(),groups=groups,floating_crossovers_C_D=cross,sha256={str(p.relative_to(root) if p.is_relative_to(root) else p):sha256(p.read_bytes()).hexdigest() for p in paths})
(out/'accepted.json').write_text(json.dumps(rec,indent=2)+'\n')
print(stamp,cross,rec['report_sha256'])
