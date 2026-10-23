from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib
import sympy as s
R=Path('research/spec55_consistency_audit');V=R/'verification';checks=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();flat=lambda x:' '.join(x.split())
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
for x in json.loads((V/'INPUTS.json').read_text())['files']:ck('hash '+Path(x['frozen']).name,sha(x['frozen'])==x['sha256'])
for filename,count in [('gate270.json',36),('gate267.json',204),('review267.json',16),('gate271.json',1019)]:
 g=json.loads((V/filename).read_text());ck(filename,g['status']=='PASS'and g['count']==count and all(z['passed']for z in g['checks']))
A=(V/'SPEC_v53.md').read_text();B=(V/'SPEC_v55.md').read_text();ck('base hash',sha(V/'SPEC_v53.md')=='5ee35cfee83304b85279c5198971102c0a29d50db064da2aa2db48a48029fb7c');ck('target hash',sha(V/'SPEC_v55.md')=='2bdd93d3cb10f3235a80d1068dd32013941fb16f44f59c1018988051862f09ef')
old=A.split(' (G45)',1)[0];new=B.split(' (G45)',1)[0];ck('all prior mathematics unchanged',old.replace('Version v53, 2026-10-21T18:02Z','Version v55, 2026-10-21T18:26Z')==new)
a=A.split(' (G45)',1)[1].split('## CHANGELOG',1)[0];b=B.split(' (G45)',1)[1].split('## CHANGELOG',1)[0]
reps=[('positive even weights A_j at nodes v_j, odd A_0 at v = 1; delta = 1, pi\'(z) = 0, M_l = 0 for l <= e, (A7))','positive even u-residues A_j (weights) at the poles u_j, attached to the transformed nodes v_j = 1/(1 + u_j) (the\n      v-residue is -A_j v_j^2, not A_j), odd A_0 at u = 0 (v = 1); delta = 1, pi\'(z) = 0, M_l = 0 for l <= e, (A7))'),('''[PROVED-lead, sent to the checker 17:52Z] d = 15: the four remaining patterns ((1;1,3,3), (3;2,2,1,1), (1;3,2,1,1),
      (1;2,2,1,1,1)) excluded for every real n >= 1 (research/p_ext/classify.py, e3_2211.py, m15_res.py); would give
      d >= 17, P >= 19/2.''','''[PROVED, checker 267 (204 + 16 checks, independent method, 18:13Z); lead's own derivation also; external audit of
      a report text still needed] d = 15: the four remaining patterns ((1;1,3,3), (3;2,2,1,1), (1;3,2,1,1),
      (1;2,2,1,1,1)) excluded for every real n >= 1: d >= 17, P >= 19/2 (for d79). [PROVED-lead, sent to the checker
      18:15Z] d = 17: all nine patterns excluded for every real n >= 1 (two-class and three-class resultants,
      research/p_ext/tc.py, res3g.py, res3.py, e3_two_class.py): would give d >= 19, P >= 21/2. d = 19, 21: running
      (research/p_ext/drv.py).'''),('integrality of n is essential.','integrality of n is essential to the necessary residue argument (that solution gives no polynomial H and no profile).')]
c=a
for i,(u,v)in enumerate(reps):ck('unique G45 replacement'+str(i),c.count(u)==1);c=c.replace(u,v,1)
ck('all G45 bytes reconstructed',c==b)
newhist='''- v55 2026-10-21T18:26Z: (G45) the two repairs of checker 270: u-residues A_j distinguished from the transformed
  nodes v_j; 'integrality essential' scoped to the necessary residue argument.
- v54 2026-10-21T18:18Z: (G45) d = 15 closure CONFIRMED by checker 267 (d >= 17, P >= 19/2; for d79); d = 17 closure
  by the lead sent to the checker (note 18:15Z); d = 19, 21 scan started.
'''
ck('all changelog bytes reconstructed',B.split('## CHANGELOG\n',1)[1]==newhist+A.split('## CHANGELOG\n',1)[1])
AA=A.splitlines(True);BB=B.splitlines(True);changes=[dict(op=op,old_lines=[i,j],new_lines=[k,l],old=''.join(AA[i:j]),new=''.join(BB[k:l]))for op,i,j,k,l in difflib.SequenceMatcher(a=AA,b=BB,autojunk=False).get_opcodes()if op!='equal'];rev=BB[:]
for z in reversed(changes):i,j=z['old_lines'];k,l=z['new_lines'];rev[k:l]=AA[i:j]
ck('whole reverse bytes',''.join(rev)==A)
u,v,vj,Aj,A0=s.symbols('u v vj Aj A0');term=Aj/(1/v-1-(1/vj-1));ck('residue transform rational',s.cancel(term-Aj*v*vj/(vj-v))==0);ck('v residue sign and factor',s.cancel(((v-vj)*term)).subs(v,vj)==-Aj*vj*vj);ck('A0 coordinate',s.cancel(A0/(1/v-1)-A0*v/(1-v))==0)
for i,x in enumerate(['d >= 17, P >= 19/2 (for d79)','external audit of a report text still needed','[PROVED-lead, sent to the checker 18:15Z] d = 17','would give d >= 19, P >= 21/2','[CONJ/OPEN] e = 2 in general','no integer solution with n <= 1000','no degree-uniform residual bound, no statement on limits','NOT a NO endpoint','necessary residue argument (that solution gives no polynomial H and no profile)']):ck('scope'+str(i),x in flat(b))
ck('271 newer finite arithmetic evidence',datetime.fromisoformat(json.loads((V/'gate271.json').read_text())['utc'])>datetime.fromisoformat('2026-10-21T18:26:00+00:00'))
(V/'CHANGES.json').write_text(json.dumps(changes,indent=2)+'\n');out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),open_claims=['All nine degree17 exclusions are awaiting independent verification in this audit.','Degree19/21 running statements are attributed source status only.','No all-n e2 exclusion, no full-plane exclusion.'],resolved_later='Result271 independently confirms the n<=1000 e2 arithmetic and inequalities; v55 predates that confirmation.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([x for x in checks if not x['passed']]);raise SystemExit(out['status']!='PASS')
