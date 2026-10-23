from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib
R=Path('research/spec52_consistency_audit');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();flat=lambda t:' '.join(t.split())
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
manifest=json.loads((V/'INPUTS.json').read_text())
for f in manifest['files']:ck('frozen '+Path(f['frozen']).name,sha(f['frozen'])==f['sha256'])
A=(V/'SPEC_v51.md').read_text();B=(V/'SPEC_v52.md').read_text();ck('v52 published hash',sha(V/'SPEC_v52.md')=='853d191978e97e3cd8f07488bd56aa5bcbac601e5a4b13f5cbf82c53c3ff01a2');g=json.loads((V/'gate250.json').read_text());ck('250 gate',g['status']=='PASS'and g['count']==43 and all(q['passed']for q in g['checks']));ck('250 proof',g['proof_sha256']==sha(Path('research/spec50_consistency_audit/V51_PROOF.md')))
part=lambda t,start,end:t[t.index(start):t.index(end,t.index(start))]
a43=part(A,' (G43)',' (G44)');b43=part(B,' (G43)',' (G44)');a44=part(A,' (G44)','## CHANGELOG');b44=part(B,' (G44)',' (G45)');b45=part(B,' (G45)','## CHANGELOG')
oldmath=flat(a43[a43.index('Finite polynomial axis data.'):]).replace('C = 0 gives G = 0 and the claim fails','C = 0 does not parametrize positive y');newmath=flat(b43[b43.index('Finite\n      polynomial axis data.'):]);ck('G43 entire mathematical statement',oldmath==newmath)
ck('G43 positive coordinate domain','C > 0 (C = 0 does not parametrize positive y)'in b43);ck('G43 installed74','INSTALLED in draft 74, 16:41Z'in b43);ck('G43 old stale header disclosed','to be installed as 3.80 + A.3.80 in draft 74'in b43)
ck('G44 finite full inverse','finite axis search using the complete inverse on 100 <= y <= 1e12'in flat(b44));ck('G44 no certified extrema','dense scan maxima, not certified suprema; no claim of root completeness'in flat(b44));ck('G44 extrema comparison preserved',flat(a44[a44.index('maxRf'):a44.index('Reported in')])==flat(b44[b44.index('maxRf'):b44.index('Reported in')]))
ck('G44 preliminary confirmation','preliminary CONFIRMED (252, 213 checks)'in b44);ck('G44 formal trial','trial 26b06fe8... posted 16:52Z'in b44)
for text in ['IN PROGRESS','not adopted','lead derivation unchecked','Not in the report until checked by the checker and audited.','m = 11 e = 2 excluded']:
 ck('G45 scope '+text,text in flat(b45))
ck('G45 generalized253','P = n + m/2, m = deg[t h(1 - t^2)] odd >= 5'in b45);ck('G45 necessary hypotheses','H nonzero with H(0) = 0'in b45 and 'n >= 1'in b45)
ch=part(B,'- v52','- v51');ck('changelog proper250','16:07Z are checker 250, not 249'in flat(ch));ck('changelog unresolved','No change to the endpoint: UNRESOLVED'in flat(ch));ck('historical changelog unchanged',A[A.index('- v51'):]==B[B.index('- v51'):]);ck('prefix excluding header unchanged',A[:A.index(' (G43)')].replace(A.splitlines()[2],B.splitlines()[2],1)==B[:B.index(' (G43)')])
la=A.splitlines(True);lb=B.splitlines(True);ops=[z for z in difflib.SequenceMatcher(a=la,b=lb,autojunk=False).get_opcodes()if z[0]!='equal'];rev=lb[:]
for op,l,h,k,m in reversed(ops):rev[k:m]=la[l:h]
ck('reverse entire bytes',''.join(rev)==A)
changes=[dict(op=op,old_lines=[l,h],new_lines=[k,m],old=''.join(la[l:h]),new=''.join(lb[k:m]))for op,l,h,k,m in ops];(V/'CHANGES.json').write_text(json.dumps(changes,indent=2)+'\n')
out=dict(status='PASS'if all(z['passed']for z in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,changed_blocks=len(changes),proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(Path(__file__)),scope='Requested local repairs confirmed; G45 lead elimination m>=11 not verified; stale G43 to-be-installed phrase disclosed.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['changed_blocks']);print([z for z in checks if not z['passed']]);raise SystemExit(out['status']!='PASS')
