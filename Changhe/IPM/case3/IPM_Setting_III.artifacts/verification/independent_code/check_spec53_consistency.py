from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
R=Path('research/spec53_consistency_audit');V=R/'verification';checks=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();flat=lambda x:' '.join(x.split())
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
for x in json.loads((V/'INPUTS.json').read_text())['files']:ck('hash '+x['file'],sha(V/x['file'])==x['sha256'])
for n,c in[(260,27),(267,204),(268,26)]:
 g=json.loads((V/f'gate{n}.json').read_text());ck(f'gate{n}',g['status']=='PASS'and g['count']==c and all(q['passed']for q in g['checks']))
A=(V/'SPEC_v52.md').read_text();B=(V/'SPEC_v53.md').read_text();AA=A.splitlines(True);BB=B.splitlines(True);changes=json.loads((V/'CHANGES.json').read_text());ck('four changed blocks',len(changes)==4);rev=BB[:];fwd=AA[:]
for i,c in reversed(list(enumerate(changes))):
 a,b=c['old_lines'];h,k=c['new_lines'];ck('old'+str(i),c['old']==''.join(AA[a:b]));ck('new'+str(i),c['new']==''.join(BB[h:k]));rev[h:k]=c['old'].splitlines(True);fwd[a:b]=c['new'].splitlines(True)
ck('reverse exact',''.join(rev)==A);ck('forward exact',''.join(fwd)==B)
def item(t,start,end):return t.split(start,1)[1].split(end,1)[0]
a43=item(A,' (G43)',' (G44)');b43=item(B,' (G43)',' (G44)');ck('G43 theorem unchanged',flat(a43.split('polynomial axis data.',1)[1])==flat(b43.split('polynomial axis data.',1)[1]));ck('G43 stale phrase removed','to be installed'not in b43);ck('G43 supersession recorded','superseded in draft 77 by G45'in b43)
ck('G44 unchanged',item(A,' (G44)',' (G45)')==item(B,' (G44)',' (G45)'))
g=item(B,' (G45)','## CHANGELOG');ck('older sections unchanged',A.split(' (G43)',1)[0].split('\n',3)[3]==B.split(' (G43)',1)[0].split('\n',3)[3]);ck('history preserved',A.split('## CHANGELOG',1)[1].lstrip()==B.split('- v52 ',1)[1].join(['- v52 ','']) if False else B.split('- v52 ',1)[1]==A.split('- v52 ',1)[1])
for i,t in enumerate(['d >= 11: PROVED','both INSTALLED in draft 77 (17:59Z','d78 preliminary','ecedbd50...','[PROVED-lead, sent to the checker 17:52Z] d = 15','would give d >= 17, P >= 19/2','NOT a NO endpoint','no degree-uniform residual bound, no statement on limits']):ck('scope'+str(i),t in flat(g))
ck('unchecked integer claim attributed','[CONJ/OPEN]'in g and 'external x3j'in g and 'no integer solution with n <= 1000'in g)
ck('noninteger example correct scope data','d = 107' in g and 'n in (1, 1.001), checker 261'in g)
ck('hypotheses generalization',all(x in g for x in ['H nonzero with H(0) = 0','h(0) != 0, n >= 1','P = n + d/2','b - A_1 > 2n','d >= 15, P >= 17/2']))
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),open_claims=['No integer e=2 solution for n<=1000: external finite reduction and execution not independently reproduced.','Two necessary inequalities attributed to x3j, not yet independently proved in this result.'],wording_caveats=['Positive weights Aj are residues in u, not residues of transformed phi in v.','Integrality essential applies to this necessary residue obstruction, not every possible proof.'],scope='Text and verified finite theorem consistency only. Full-plane OPEN.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([x for x in checks if not x['passed']]);raise SystemExit(out['status']!='PASS')
